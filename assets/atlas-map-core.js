/* Tech Atlas map: the arithmetic, with no page or library behind it, so it can
   be tested on its own (node --test). The scene draws with it.

   A camera is {x, y, k}: the map point at the centre of the view, and the
   scale from map units to screen pixels. */
(function (root, factory) {
  var api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.AtlasMapCore = api;
})(this, function () {
  "use strict";

  var FLIGHT_MIN = 800, FLIGHT_MAX = 1200;
  var R_UNRATED = 5, R_MIN = 7, R_MAX = 19;
  var RADAR_FLOOR = 0.12;
  // zoom, as a multiple of the zoom that fits the whole galaxy, where planets give way to companies
  var SHOW = { planetsUntil: 1.45, sectorsFrom: 2.1 };
  var SQRT2 = Math.SQRT2;
  // input: how long a wheel gesture may rest and still be the same gesture, and how fast a swipe pans
  var GESTURE_REST_MS = 120, RELEASE_GAP_MS = 60, PAN_TAU = 45, DECAYED = 0.35, MIN_GLIDE = 0.05;

  function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }

  /* ------------------------------------------------------------ camera */
  function toScreen(cam, view, p) {
    return { x: (p.x - cam.x) * cam.k + view.w / 2, y: (p.y - cam.y) * cam.k + view.h / 2 };
  }
  function toWorld(cam, view, s) {
    return { x: (s.x - view.w / 2) / cam.k + cam.x, y: (s.y - view.h / 2) / cam.k + cam.y };
  }

  /** The camera that fits box [x0, y0, x1, y1] in the view with pad pixels to spare. */
  function fitCam(box, view, pad, limits) {
    var k = Math.min((view.w - 2 * pad) / (box[2] - box[0]), (view.h - 2 * pad) / (box[3] - box[1]));
    return { x: (box[0] + box[2]) / 2, y: (box[1] + box[3]) / 2, k: clamp(k, limits.min, limits.max) };
  }

  /** Zoom to scale k while the map point under screen point s stays under it. */
  function zoomAround(cam, view, s, k) {
    var w = toWorld(cam, view, s);
    return { x: w.x - (s.x - view.w / 2) / k, y: w.y - (s.y - view.h / 2) / k, k: k };
  }

  /** Hold the zoom limits and keep the view's centre over the map. */
  function clampCam(cam, box, limits) {
    return { x: clamp(cam.x, box[0], box[2]), y: clamp(cam.y, box[1], box[3]), k: clamp(cam.k, limits.min, limits.max) };
  }

  /** Move v towards target with time constant tau (ms): smooth, frame-rate independent, no overshoot. */
  function approach(v, target, dt, tau) {
    return target + (v - target) * Math.exp(-dt / tau);
  }

  /** One frame of glide after a drag: velocity in px/ms decays, and null once it has stopped. */
  function glide(v, dt, tau) {
    var f = Math.exp(-dt / tau), n = { x: v.x * f, y: v.y * f };
    return Math.hypot(n.x, n.y) < 0.01 ? null : n;
  }

  /** van Wijk and Nuij's smooth zoom and pan between two cameras: a long jump zooms out mid-way. */
  function flight(a, b, view) {
    var w0 = view.w / a.k, w1 = view.w / b.k, dx = b.x - a.x, dy = b.y - a.y, d2 = dx * dx + dy * dy;
    var rho = SQRT2, rho2 = 2, rho4 = 4, S, at;
    if (d2 < 1e-12) {
      S = Math.log(w1 / w0) / rho;
      at = function (t) { return { x: a.x + t * dx, y: a.y + t * dy, k: view.w / (w0 * Math.exp(rho * t * S)) }; };
    } else {
      var d1 = Math.sqrt(d2);
      var b0 = (w1 * w1 - w0 * w0 + rho4 * d2) / (2 * w0 * rho2 * d1);
      var b1 = (w1 * w1 - w0 * w0 - rho4 * d2) / (2 * w1 * rho2 * d1);
      var r0 = Math.log(Math.sqrt(b0 * b0 + 1) - b0), r1 = Math.log(Math.sqrt(b1 * b1 + 1) - b1);
      S = (r1 - r0) / rho;
      at = function (t) {
        if (t >= 1) return { x: b.x, y: b.y, k: b.k };
        var s = t * S, c0 = Math.cosh(r0);
        var u = w0 / (rho2 * d1) * (c0 * Math.tanh(rho * s + r0) - Math.sinh(r0));
        return { x: a.x + u * dx, y: a.y + u * dy, k: view.w / (w0 * c0 / Math.cosh(rho * s + r0)) };
      };
    }
    return { at: at, duration: Math.abs(S) * 1000 };
  }

  /** How long a camera flight lasts, from the suggested duration. */
  function flightMs(suggested, reduced) {
    return reduced ? 0 : clamp(Math.round(suggested), FLIGHT_MIN, FLIGHT_MAX);
  }

  /** Cubic ease-in-out: speed up, cruise, slow down. */
  function easeInOut(t) {
    return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
  }

  /** How far from planets (0) to companies (1) the view is, at zoom z (a multiple of the galaxy fit). */
  function detail(z) {
    return clamp((z - SHOW.planetsUntil) / (SHOW.sectorsFrom - SHOW.planetsUntil), 0, 1);
  }

  /* ------------------------------------------------------------ labels */
  function overlap(a, b, m) {
    return !(a.x + a.w + m <= b.x || b.x + b.w + m <= a.x || a.y + a.h + m <= b.y || b.y + b.h + m <= a.y);
  }
  // view may reserve strips at the top and bottom (for controls) where no label goes
  function inside(b, view) {
    return b.x >= 0 && b.y >= (view.top || 0) && b.x + b.w <= view.w && b.y + b.h <= view.h - (view.bottom || 0);
  }

  /** Which labels to show, and where. Each item offers boxes in order of preference
      ({id, p, alts: [{x, y, w, h}], avoid, force}). Highest priority picks first. A
      label never covers another, an `avoid` label never covers a node box, and a
      `force` label takes its first position if none is free. Returns Map id -> alt index. */
  function collide(items, view, margin, nodeBoxes) {
    var kept = [], shown = new Map(), blocks = nodeBoxes || [];
    items.slice().sort(function (a, b) { return b.p - a.p; }).forEach(function (it) {
      var pick = -1;
      for (var i = 0; i < it.alts.length && pick < 0; i++) {
        var b = it.alts[i];
        if (!inside(b, view)) continue;
        if (kept.some(function (o) { return overlap(b, o, margin); })) continue;
        if (it.avoid && blocks.some(function (o) { return overlap(b, o, 0); })) continue;
        pick = i;
      }
      if (pick < 0 && it.force && inside(it.alts[0], view)) pick = 0;
      if (pick < 0) return;
      kept.push(it.alts[pick]);
      shown.set(it.id, pick);
    });
    return shown;
  }

  /** A sector name as one line, or two lines split as evenly as its words allow. */
  function splitTitle(name) {
    if (name.length < 15) return [name];
    var w = name.split(" "), best = 1, gap = Infinity;
    for (var i = 1; i < w.length; i++) {
      var d = Math.abs(w.slice(0, i).join(" ").length - w.slice(i).join(" ").length);
      if (d < gap) { gap = d; best = i; }
    }
    return [w.slice(0, best).join(" "), w.slice(best).join(" ")];
  }

  /** The words under a sector's title at galaxy zoom: {count, top: [three lines]}. Sectors rank
      by OVR. Owners and backers have no OVR, so they rank by how many companies each backs,
      counting each company once, with ties in name order. */
  function sectorSummary(sid, mains, ent, edges) {
    function byName(a, b) { return ent[a].name < ent[b].name ? -1 : ent[a].name > ent[b].name ? 1 : 0; }
    if (sid === "backers") {
      var backed = {};
      edges.forEach(function (e) {
        if (e.group === "backers" && mains.indexOf(e.a) > -1) (backed[e.a] = backed[e.a] || {})[e.b] = true;
      });
      var n = function (id) { return Object.keys(backed[id] || {}).length; };
      return {
        count: mains.length + (mains.length === 1 ? " owner or backer" : " owners and backers"),
        top: mains.filter(function (id) { return n(id) > 0; })
          .sort(function (a, b) { return n(b) - n(a) || byName(a, b); }).slice(0, 3)
          .map(function (id) { return ent[id].name + " · " + n(id) + " backed"; })
      };
    }
    return {
      count: mains.length + (mains.length === 1 ? " company" : " companies"),
      top: mains.filter(function (id) { return ent[id].ovr !== null && ent[id].ovr !== undefined; })
        .sort(function (a, b) { return ent[b].ovr - ent[a].ovr || byName(a, b); }).slice(0, 3)
        .map(function (id) { return ent[id].name + "  " + ent[id].ovr; })
    };
  }

  /** Move every sector of a layout between its wide and narrow arrangements, in place. The wide
      arrangement is remembered the first time. Returns how far each sector moved, {sid: {x, y}}. */
  function relayout(map, narrow) {
    if (!map.wide) {
      var saved = {};
      Object.keys(map.sectors).forEach(function (sid) { saved[sid] = [map.sectors[sid].x, map.sectors[sid].y]; });
      map.wide = { centres: saved, bounds: map.bounds.slice() };
    }
    var to = narrow ? map.narrow : map.wide, moved = {};
    Object.keys(map.sectors).forEach(function (sid) {
      var t = map.sectors[sid], dx = to.centres[sid][0] - t.x, dy = to.centres[sid][1] - t.y;
      moved[sid] = { x: dx, y: dy };
      t.x += dx; t.y += dy;
      t.rows.forEach(function (r) { r.x += dx; r.y += dy; });
      t.spokes.forEach(function (s) { s[0] += dx; s[1] += dy; s[2] += dx; s[3] += dy; });
    });
    map.cards.forEach(function (c) { c.x += moved[c.sector].x; c.y += moved[c.sector].y; });
    map.bounds = to.bounds.slice();
    return moved;
  }

  /** The camera that fits every sector's label on screen at galaxy zoom. centres are the sectors'
      map points, block the largest label {w, h} in pixels, and safe the strips the controls need
      {top, bottom, side}. The centre of the labels lands in the centre of what the strips leave. */
  function galaxyFit(centres, block, view, safe) {
    var xs = centres.map(function (c) { return c.x; }), ys = centres.map(function (c) { return c.y; });
    var x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs), y0 = Math.min.apply(null, ys), y1 = Math.max.apply(null, ys);
    var room = view.h - safe.top - safe.bottom;
    var k = Math.min((view.w - 2 * safe.side - block.w) / Math.max(1, x1 - x0), (room - block.h) / Math.max(1, y1 - y0));
    k = Math.max(k, 1e-4);
    return { x: (x0 + x1) / 2, y: (y0 + y1) / 2 - (safe.top + room / 2 - view.h / 2) / k, k: k };
  }

  /** Whether no two boxes {x, y, w, h} come within margin of each other. */
  function blocksClear(boxes, margin) {
    return !boxes.some(function (a, i) { return boxes.some(function (b, j) { return j > i && overlap(a, b, margin); }); });
  }

  /* ------------------------------------------------------------- lines */
  /** A curved line from a to b that stops short of both ends, with the direction it arrives in. */
  function arc(a, b, ra, rb, bend, gap, ida, idb) {
    var dx = b.x - a.x, dy = b.y - a.y, d = Math.hypot(dx, dy) || 1;
    // bend to the same side whichever end comes first, so A-B and B-A share a curve
    var flip = ida !== undefined && idb !== undefined && ida > idb ? -1 : 1;
    var nx = -dy / d * flip, ny = dx / d * flip;
    var ctrl = { x: (a.x + b.x) / 2 + nx * bend * d, y: (a.y + b.y) / 2 + ny * bend * d };
    var s = unit(ctrl.x - a.x, ctrl.y - a.y), e = unit(b.x - ctrl.x, b.y - ctrl.y);
    var start = { x: a.x + s.x * (ra + gap), y: a.y + s.y * (ra + gap) };
    var end = { x: b.x - e.x * (rb + gap), y: b.y - e.y * (rb + gap) };
    return {
      d: "M" + r1(start.x) + " " + r1(start.y) + " Q" + r1(ctrl.x) + " " + r1(ctrl.y) + " " + r1(end.x) + " " + r1(end.y),
      start: start, end: end, ctrl: ctrl, dir: e
    };
  }
  function unit(x, y) { var l = Math.hypot(x, y) || 1; return { x: x / l, y: y / l }; }
  function r1(v) { return Math.round(v * 10) / 10; }

  /** A point t (0..1) along an arc's quadratic curve. */
  function onCurve(c, t) {
    var u = 1 - t;
    return { x: u * u * c.start.x + 2 * u * t * c.ctrl.x + t * t * c.end.x,
             y: u * u * c.start.y + 2 * u * t * c.ctrl.y + t * t * c.end.y };
  }

  /** Lines between sectors, one per pair of home sectors, counted by kind. */
  function bundles(edges, homeOf) {
    var by = {};
    edges.forEach(function (e) {
      var a = homeOf[e.a], b = homeOf[e.b];
      if (!a || !b || a === b) return;
      var lo = a < b ? a : b, hi = a < b ? b : a, key = lo + "|" + hi;
      var x = by[key] || (by[key] = { a: lo, b: hi, count: 0, by: { allies: 0, rivals: 0, backers: 0 } });
      x.count++;
      x.by[e.group]++;
    });
    return Object.keys(by).sort().map(function (k) { return by[k]; });
  }
  function bundleText(b, names) {
    var parts = [["allies", "ally"], ["rivals", "rival"], ["backers", "backer"]]
      .filter(function (g) { return b.by[g[0]]; }).map(function (g) { return b.by[g[0]] + " " + g[1]; });
    return names[b.a] + " ↔ " + names[b.b] + ": " + parts.join(", ");
  }

  /* ------------------------------------------------------- focus ring */
  var SIDE = { left: Math.PI, right: 0, top: -Math.PI / 2, bottom: Math.PI / 2 };

  /** Where each neighbour sits around the selected company, relative to it. Each side
      spreads over an arc of up to 80 degrees and adds an outer ring when crowded. */
  function focusRing(groups, radius, gap) {
    var out = {}, half = 40 * Math.PI / 180;
    Object.keys(SIDE).forEach(function (side) {
      var ids = groups[side] || [], placed = 0, ring = 0;
      while (placed < ids.length) {
        var r = radius + ring * gap;
        var room = Math.max(1, Math.floor(2 * half * r / gap) + 1);
        var take = ids.slice(placed, placed + room), step = take.length > 1 ? 2 * Math.asin(Math.min(1, gap / (2 * r))) : 0;
        take.forEach(function (id, i) {
          var ang = SIDE[side] + (i - (take.length - 1) / 2) * step;
          out[id] = { x: r * Math.cos(ang), y: r * Math.sin(ang) };
        });
        placed += take.length;
        ring++;
      }
    });
    return out;
  }

  /** On a narrow screen: every neighbour on one ellipse, evenly spaced, the top group
      centred at the top and the others following clockwise (right, bottom, left). */
  function ellipseRing(groups, rx, ry) {
    var order = [].concat(groups.top || [], groups.right || [], groups.bottom || [], groups.left || []);
    var n = order.length, out = {}, step = 2 * Math.PI / Math.max(1, n);
    var start = -Math.PI / 2 - ((groups.top || []).length - 1) * step / 2;
    if (!(groups.top || []).length) start = -Math.PI / 2 + step / 2;
    order.forEach(function (id, i) {
      var a = start + i * step;
      out[id] = { x: rx * Math.cos(a), y: ry * Math.sin(a) };
    });
    return out;
  }

  /* ------------------------------------------------------------ input */
  /** What a wheel event is: "pinch" (zoom), "wheel" (a mouse wheel, zoom) or "pan" (a trackpad swipe).
      prev is the last gesture {kind, t}: a gesture keeps its kind until it rests GESTURE_REST_MS.
      1. ctrlKey set: browsers report a trackpad pinch this way.
      2. deltaMode 1 or 2 (lines or pages): only wheels report that.
      3. Any deltaX: a sideways swipe, which a plain mouse wheel cannot make.
      4. wheelDeltaY (Chrome, Edge, Safari): a multiple of 120 is a wheel notch. -3 x deltaY marks a
         trackpad in Chrome, but Safari reports that ratio for wheels too, so it counts only for small steps.
      5. Otherwise large whole-number steps (50 and up) are a wheel, and small or fractional ones a swipe.
      A swipe starts with small steps, so its first event decides it, and the gesture keeps that kind. */
  function wheelKind(ev, prev, now) {
    if (ev.ctrlKey) return "pinch";
    if (prev && prev.kind !== "pinch" && now - prev.t <= GESTURE_REST_MS) return prev.kind;
    if (ev.deltaMode) return "wheel";
    if (ev.deltaX) return "pan";
    var w = ev.wheelDeltaY;
    var d = Math.abs(ev.deltaY);
    if (w) {
      if (w % 120 === 0) return "wheel";
      if (Math.abs(w + 3 * ev.deltaY) < 1e-6 && d < 50) return "pan";
    }
    return d >= 50 && Math.abs(d - Math.round(d)) < 1e-9 ? "wheel" : "pan";
  }

  /** When a swipe ends: a glide velocity (px/ms, the way the deltas point) if the stream stopped
      abruptly, or null while it continues or when the system already slowed it (its own momentum). */
  function swipeRelease(samples, now) {
    if (!samples.length || now - samples[samples.length - 1].t < RELEASE_GAP_MS) return null;
    var tail = samples.slice(-5), mags = tail.map(function (s) { return Math.hypot(s.dx, s.dy); });
    if (mags[mags.length - 1] < DECAYED * Math.max.apply(null, mags)) return null;
    var span = tail[tail.length - 1].t - tail[0].t + 16, sx = 0, sy = 0;
    tail.forEach(function (s) { sx += s.dx; sy += s.dy; });
    var v = { x: sx / span, y: sy / span };
    return Math.hypot(v.x, v.y) < MIN_GLIDE ? null : v;
  }

  /** One frame of a swipe: how far to move now (px) and what is left. Reduced motion moves at once. */
  function panStep(left, dt, reduced) {
    var f = reduced ? 1 : 1 - Math.exp(-dt / PAN_TAU), x = left.x * f, y = left.y * f;
    return { x: x, y: y, left: { x: left.x - x, y: left.y - y } };
  }

  /* -------------------------------------------------------- spotlight */
  /** Where the camera goes to spotlight company c with its neighbours (world points by id).
      opt: read (the lowest zoom where labels are readable), max, pad (px), and right/top/bottom
      (px the card and controls cover). Fit every neighbour if that zoom is readable. Otherwise
      stay readable and send the ones that do not fit to the ring. */
  function spotlightPlan(c, nbrs, view, opt) {
    var right = opt.right || 0, top = opt.top || 0, bottom = opt.bottom || 0;
    var hw = (view.w - right) / 2 - opt.pad, hh = (view.h - top - bottom) / 2 - opt.pad;
    var ids = Object.keys(nbrs).sort(), fit = Infinity;
    ids.forEach(function (id) {
      var dx = Math.abs(nbrs[id].x - c.x), dy = Math.abs(nbrs[id].y - c.y);
      if (dx > 1e-9) fit = Math.min(fit, hw / dx);
      if (dy > 1e-9) fit = Math.min(fit, hh / dy);
    });
    var k = fit >= opt.read ? Math.min(fit, opt.max) : opt.read, inPlace = [], ring = [];
    ids.forEach(function (id) {
      var ok = Math.abs(nbrs[id].x - c.x) * k <= hw + 1e-6 && Math.abs(nbrs[id].y - c.y) * k <= hh + 1e-6;
      (ok ? inPlace : ring).push(id);
    });
    var sx = (view.w - right) / 2, sy = top + (view.h - top - bottom) / 2;
    return { cam: { x: c.x - (sx - view.w / 2) / k, y: c.y - (sy - view.h / 2) / k, k: k }, inPlace: inPlace, ring: ring,
             centre: { x: sx, y: sy } };
  }

  /* ------------------------------------------------------- deep links */
  /** What an address hash asks for: the map at a company or sector, the list, or nothing. */
  function parseHash(hash, companies, sectors, teams) {
    var h = (hash || "").replace(/^#/, "");
    if (h.indexOf("sector-") === 0) return { view: "list" };
    if (h.indexOf("c-") === 0) {
      var id = h.slice(2);
      if (companies.has(id)) return { view: "map", company: id };
      return id.indexOf("-") > -1 ? { view: "list" } : { view: null };
    }
    if (h.indexOf("s-") === 0 && sectors.has(h.slice(2))) return { view: "map", sector: h.slice(2) };
    if (h.indexOf("t-") === 0 && teams && teams.has(h.slice(2))) return { view: "map", team: h.slice(2) };
    return { view: null };
  }
  function hashFor(state) {
    if (state.level === "company" && state.selected) return "#c-" + state.selected;
    if (state.level === "sector" && state.sector) return "#s-" + state.sector;
    if (state.team) return "#t-" + state.team;
    return "";
  }

  /* ---------------------------------------------------- card and nodes */
  /** Six spoke points for the radar, first one straight up; unrated sits at the floor. */
  function radar(values, r) {
    return values.map(function (v, i) {
      var f = v === null || v === undefined ? RADAR_FLOOR : RADAR_FLOOR + (1 - RADAR_FLOOR) * (clamp(v, 40, 99) - 40) / 59;
      var a = -Math.PI / 2 + i * Math.PI / 3;
      return { x: Math.cos(a) * r * f, y: Math.sin(a) * r * f };
    });
  }

  function tier(ovr, tiers) {
    if (ovr === null || ovr === undefined) return null;
    for (var i = 0; i < tiers.length; i++) if (ovr >= tiers[i].min) return tiers[i].label;
    return null;
  }

  function nodeRadius(ovr) {
    if (ovr === null || ovr === undefined) return R_UNRATED;
    return R_MIN + (clamp(ovr, 40, 99) - 40) / 59 * (R_MAX - R_MIN);
  }

  function initials(name) {
    var words = name.replace(/\(.*?\)/g, " ").split(/[\s&]+/).filter(Boolean);
    var s = words.length > 1 ? words[0][0] + words[1][0] : words[0].slice(0, 2);
    return s.toUpperCase();
  }

  /** n stars in the unit square, the same every time for the same seed (mulberry32). */
  function stars(n, seed) {
    var a = seed >>> 0, out = [];
    function rnd() {
      a = (a + 0x6D2B79F5) >>> 0;
      var t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    }
    for (var i = 0; i < n; i++) out.push({ x: rnd(), y: rnd(), m: rnd(), a: rnd() });
    return out;
  }

  return {
    toScreen: toScreen, toWorld: toWorld, fitCam: fitCam, zoomAround: zoomAround, clampCam: clampCam,
    approach: approach, glide: glide, flight: flight, flightMs: flightMs, easeInOut: easeInOut, detail: detail,
    collide: collide, splitTitle: splitTitle, sectorSummary: sectorSummary, relayout: relayout, galaxyFit: galaxyFit, blocksClear: blocksClear, arc: arc, onCurve: onCurve, bundles: bundles, bundleText: bundleText, focusRing: focusRing, ellipseRing: ellipseRing,
    wheelKind: wheelKind, swipeRelease: swipeRelease, panStep: panStep, spotlightPlan: spotlightPlan,
    GESTURE_REST_MS: GESTURE_REST_MS,
    parseHash: parseHash, hashFor: hashFor, radar: radar, tier: tier, nodeRadius: nodeRadius, initials: initials,
    stars: stars, R_UNRATED: R_UNRATED, RADAR_FLOOR: RADAR_FLOOR, SHOW: SHOW
  };
});
