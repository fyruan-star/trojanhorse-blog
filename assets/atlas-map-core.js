/* Tech Atlas map: the arithmetic, with no page or library behind it, so it can
   be tested on its own (node --test). atlas-map.js does the drawing. */
(function (root, factory) {
  var api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.AtlasMapCore = api;
})(this, function () {
  "use strict";

  var FLIGHT_MIN = 800, FLIGHT_MAX = 1200;
  var R_UNRATED = 5, R_MIN = 7, R_MAX = 19;
  // zoom, as a multiple of the zoom that fits the whole galaxy, at which each kind of label appears
  var SHOW = { tiersBelow: 1.6, sectorsBelow: 2.1, rowsFrom: 1.9, companiesFrom: 1.7 };

  function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }

  /** Zoom transform {k, x, y} that fits box [x0, y0, x1, y1] inside the view, clear of the insets. */
  function fit(box, view, inset, pad, limits) {
    var fw = view.w - inset.left - inset.right - 2 * pad;
    var fh = view.h - inset.top - inset.bottom - 2 * pad;
    var k = clamp(Math.min(fw / (box[2] - box[0]), fh / (box[3] - box[1])), limits.min, limits.max);
    return centre({ x: (box[0] + box[2]) / 2, y: (box[1] + box[3]) / 2 }, k, view, inset);
  }

  /** Zoom transform at scale k that puts point p in the middle of the view's free area. */
  function centre(p, k, view, inset) {
    var cx = inset.left + (view.w - inset.left - inset.right) / 2;
    var cy = inset.top + (view.h - inset.top - inset.bottom) / 2;
    return { k: k, x: cx - k * p.x, y: cy - k * p.y };
  }

  /** How long a camera flight lasts, from the library's suggested duration. */
  function flightMs(suggested, reduced) {
    return reduced ? 0 : clamp(Math.round(suggested), FLIGHT_MIN, FLIGHT_MAX);
  }

  /** Cubic ease-in-out: slow away, fast in the middle, slow to land. */
  function easeInOut(t) {
    return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
  }

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

  /** A curved line from a to b that stops short of both nodes, with the direction it arrives in. */
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

  /** The tier label for an OVR, from tiers sorted highest first. */
  function tier(ovr, tiers) {
    if (ovr === null || ovr === undefined) return null;
    for (var i = 0; i < tiers.length; i++) if (ovr >= tiers[i].min) return tiers[i].label;
    return null;
  }

  /** Node radius in map units: bigger for a higher OVR. */
  function nodeRadius(ovr) {
    if (ovr === null || ovr === undefined) return R_UNRATED;
    return R_MIN + (clamp(ovr, 40, 99) - 40) / 59 * (R_MAX - R_MIN);
  }

  /** Two letters for the card's monogram. */
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

  /** Which kinds of label are candidates at zoom z (a multiple of the galaxy-fit zoom). */
  function labelsAt(z) {
    return { tiers: z < SHOW.tiersBelow, sectors: z < SHOW.sectorsBelow, rows: z >= SHOW.rowsFrom, companies: z >= SHOW.companiesFrom };
  }

  return {
    fit: fit, centre: centre, flightMs: flightMs, easeInOut: easeInOut, collide: collide, arc: arc,
    tier: tier, nodeRadius: nodeRadius, initials: initials, stars: stars, labelsAt: labelsAt,
    R_UNRATED: R_UNRATED, SHOW: SHOW
  };
});
