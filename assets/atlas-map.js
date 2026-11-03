/* Tech Atlas: the Map view and the Map/List switch.

   The List works without this file. With it, the page opens on a galaxy of
   sectors: click a territory to fly in, click a company to open its card, and
   press Esc or Back to fly out a level. d3 (zoom and smooth flights) and the
   data (tech-atlas.json) load only when the Map is first shown. The arithmetic
   lives in atlas-map-core.js. */
(function () {
  "use strict";
  var C = window.AtlasMapCore;
  var root = document.getElementById("atlas-map");
  if (!root || !C) return;
  document.body.classList.add("js");

  var D3_URL = "https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js";
  var D3_SRI = "sha512-vc58qvvBdrDR4etbxMdlTt4GBQk1qjvyORR2nrsPsFPyrs+/u5c3+1Ct6upOgdZoIl7eq6k3a1UPDSNAQi/32A==";
  var VIEW_KEY = "atlas-view";
  var NS = "http://www.w3.org/2000/svg";
  var LABEL_EVERY_MS = 110;
  var RANK = {
    starter: { name: "Starter", why: "Why it leads" },
    second: { name: "Second string", why: "Why it may rise" },
    rookie: { name: "Practice squad", why: "Why it matters" }
  };
  var GROUP_LABEL = { allies: "Allies and partners", rivals: "Rivals", backers: "Owners and backers" };
  var VERB = { ownership: ["owns", "owned by"], investment: ["funds", "funded by"] };
  // where the layout's long rank names map to the renderer's short ones
  var RANK_CODE = { starter: "starter", second_string: "second", practice_squad: "rookie" };

  var stage = root.querySelector(".amap__stage");
  var svg = root.querySelector(".amap__svg");
  var canvas = root.querySelector(".amap__stars");
  var panel = root.querySelector(".pcard");
  var msg = root.querySelector(".amap__msg");
  var backBtn = root.querySelector(".amap__back");
  var where = root.querySelector(".amap__where");
  var filtersBtn = root.querySelector('[aria-controls="amap-filters"]');
  var filtersBox = document.getElementById("amap-filters");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* ------------------------------------------------------- the switch */
  function readView() { try { return localStorage.getItem(VIEW_KEY); } catch (e) { return null; } }
  function saveView(v) { try { localStorage.setItem(VIEW_KEY, v); } catch (e) { /* private mode: not remembered */ } }

  var loading = null, M = null, escHandler = null;

  function setView(v, remember) {
    var isMap = v === "map";
    document.body.classList.toggle("view-map", isMap);
    root.hidden = !isMap;
    [].forEach.call(document.querySelectorAll(".view__b"), function (b) {
      b.setAttribute("aria-pressed", b.dataset.view === v ? "true" : "false");
    });
    [].forEach.call(document.querySelectorAll("#atlas-names option[data-backer]"), function (o) { o.disabled = !isMap; });
    if (remember) saveView(v);
    if (isMap) ensureMap();
  }
  [].forEach.call(document.querySelectorAll(".view__b"), function (b) {
    b.addEventListener("click", function () {
      setView(b.dataset.view, true);
      if (b.dataset.view === "map") stage.scrollIntoView({ behavior: reduce.matches ? "auto" : "smooth", block: "nearest" });
    });
  });

  function loadD3() {
    if (window.d3) return Promise.resolve(window.d3);
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = D3_URL; s.integrity = D3_SRI; s.crossOrigin = "anonymous";
      s.onload = function () { window.d3 ? resolve(window.d3) : reject(new Error("d3 missing")); };
      s.onerror = function () { s.remove(); reject(new Error("d3 failed to load")); };
      document.head.appendChild(s);
    });
  }
  function loadData() {
    return fetch("tech-atlas.json").then(function (r) {
      if (!r.ok) throw new Error("tech-atlas.json " + r.status);
      return r.json();
    });
  }
  function ensureMap() {
    if (loading) return loading;
    msg.hidden = false;
    loading = Promise.all([loadD3(), loadData()]).then(function (res) {
      M = createMap(res[0], res[1]);
      msg.hidden = true;
    }).catch(function () {
      msg.textContent = "The map could not load, so the List is showing instead.";
      loading = null;
      setView("list", false);
      msg.hidden = false;
      root.hidden = false;
      root.classList.add("is-failed");
    });
    return loading;
  }

  /* ------------------------------------------------------- the map */
  function el(name, attrs, parent) {
    var n = document.createElementNS(NS, name);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }
  function h(tag, attrs, kids) {
    var n = document.createElement(tag);
    for (var k in attrs || {}) {
      if (k === "text") n.textContent = attrs[k];
      else if (k === "cls") n.className = attrs[k];
      else n.setAttribute(k, attrs[k]);
    }
    (kids || []).forEach(function (c) { if (c) n.appendChild(typeof c === "string" ? document.createTextNode(c) : c); });
    return n;
  }
  function host(u) {
    try { return new URL(u).hostname.replace(/^www\./, ""); } catch (e) { return "source"; }
  }

  function createMap(d3, data) {
    var lay = data.map;
    var sectorName = { backers: "Owners and backers" }, rowName = {}, cardsOf = {};
    data.sectors.forEach(function (s) {
      sectorName[s.id] = s.name;
      s.positions.forEach(function (p) {
        rowName[s.id + "/" + p.id] = p.name;
        p.players.forEach(function (pl) {
          (cardsOf[pl.e] = cardsOf[pl.e] || []).push({ sector: s.id, row: p.id, pl: pl });
        });
      });
    });
    var ent = data.entities, edgesOf = {};
    data.edges.forEach(function (e) {
      (edgesOf[e.a] = edgesOf[e.a] || []).push(e);
      (edgesOf[e.b] = edgesOf[e.b] || []).push(e);
    });

    var nodes = lay.cards.map(function (c, i) {
      var e = ent[c.company];
      return { i: i, id: c.company, sector: c.sector, row: c.row, rank: RANK_CODE[c.rank] || null,
               main: c.main, x: c.x, y: c.y, r: c.main ? C.nodeRadius(e.ovr) : C.R_UNRATED + 1,
               home: e.home || "backers" };
    });
    var mainOf = {};
    nodes.forEach(function (n) { if (n.main) mainOf[n.id] = n; });

    var state = { level: "galaxy", sector: null, selected: null, hover: null, focus: null,
                  t: d3.zoomIdentity, kGal: 1, view: { w: 0, h: 0 } };
    var filters = { sectors: new Set(Object.keys(sectorName)), ranks: new Set(["starter", "second", "rookie"]), groups: {} };
    [].forEach.call(document.querySelectorAll(".toggles input[data-group]"), function (i) { filters.groups[i.dataset.group] = i.checked; });

    /* ---- drawing, once */
    svg.textContent = "";
    var defs = el("defs", {}, svg);
    Object.keys(lay.sectors).forEach(function (sid) {
      var g = el("radialGradient", { id: "amg-" + sid }, defs);
      el("stop", { offset: "0", "class": "glow0 c-" + sid }, g);
      el("stop", { offset: ".55", "class": "glow1 c-" + sid }, g);
      el("stop", { offset: "1", "class": "glow2 c-" + sid }, g);
    });
    var scene = el("g", { "class": "scene" }, svg);
    var gTiers = el("g", { "class": "tiers" }, scene);
    var gTerr = el("g", { "class": "terrs" }, scene);
    var gEdges = el("g", { "class": "edges", "aria-hidden": "true" }, scene);
    var gNodes = el("g", { "class": "nodes" }, scene);

    var labels = []; // {el, kind, ref, anchor, wx, wy, w, h}
    lay.tiers.forEach(function (t) {
      var tx = el("text", { "class": "tier-label", x: t.x, y: t.y, "text-anchor": "end", "aria-hidden": "true" }, gTiers);
      tx.textContent = t.label;
      labels.push({ el: tx, kind: "tier", wx: t.x, wy: t.y });
    });

    var terrEls = {};
    Object.keys(lay.sectors).forEach(function (sid) {
      var t = lay.sectors[sid];
      var n = nodes.filter(function (x) { return x.sector === sid; }).length;
      var g = el("g", { "class": "terr c-" + sid, "data-sector": sid, role: "button", tabindex: "0",
                        "aria-label": t.name + ", " + n + " companies. Press Enter to fly in." }, gTerr);
      el("circle", { "class": "terr__glow", cx: t.x, cy: t.y, r: t.r * 1.08, fill: "url(#amg-" + sid + ")" }, g);
      var tr = "translate(" + t.x + " " + t.y + ")";
      el("path", { "class": "terr__halo", d: t.outline, transform: tr }, g);
      el("path", { "class": "terr__line", d: t.outline, transform: tr }, g);
      el("path", { "class": "terr__line2", d: t.outline2, transform: tr }, g);
      t.spokes.forEach(function (s) { el("line", { "class": "terr__div", x1: s[0], y1: s[1], x2: s[2], y2: s[3] }, g); });
      t.rings.forEach(function (r) { el("circle", { "class": "terr__div", cx: t.x, cy: t.y, r: r }, g); });
      // the name sits across the territory, like a country on a map
      var title = el("text", { "class": "terr__title", x: t.x, y: t.y, "text-anchor": "middle" }, g);
      splitName(t.name).forEach(function (line, i, all) {
        var ts = el("tspan", { x: t.x, dy: i ? "1.2em" : (all.length > 1 ? "-0.25em" : "0.35em") }, title);
        ts.textContent = line;
      });
      labels.push({ el: title, kind: "sector", ref: sid, wx: t.x, wy: t.y });
      t.rows.forEach(function (r) {
        var rl = el("text", { "class": "row-label", x: r.x, y: r.y, "text-anchor": r.anchor, dy: ".35em" }, g);
        rl.textContent = r.name;
        labels.push({ el: rl, kind: "row", ref: sid, wx: r.x, wy: r.y });
      });
      terrEls[sid] = g;
    });

    nodes.forEach(function (n) {
      var e = ent[n.id];
      var g = el("g", { "class": "node c-" + n.home + (n.main ? "" : " node--echo") + (n.rank ? " rank--" + n.rank : ""),
                        transform: "translate(" + n.x + " " + n.y + ")", role: "button", tabindex: "-1",
                        "data-id": n.id, "aria-label": nodeLabel(n, e) }, gNodes);
      if (n.main) el("circle", { "class": "node__glow", r: n.r * 2, fill: "url(#amg-" + n.home + ")" }, g);
      el("circle", { "class": "node__core", r: n.r }, g);
      el("circle", { "class": "node__ring", r: n.r + 3.5 }, g);
      var tx = el("text", { "class": "node__label", y: n.r, dy: "1.2em", "text-anchor": "middle" }, g);
      tx.textContent = e.name;
      n.el = g;
      labels.push({ el: tx, kind: "company", ref: n, wx: n.x, wy: n.y });
    });

    // long sector names break into two lines at the word nearest the middle
    function splitName(name) {
      if (name.length < 15) return [name];
      var words = name.split(" "), best = 1, gap = Infinity;
      for (var i = 1; i < words.length; i++) {
        var d = Math.abs(words.slice(0, i).join(" ").length - words.slice(i).join(" ").length);
        if (d < gap) { gap = d; best = i; }
      }
      return [words.slice(0, best).join(" "), words.slice(best).join(" ")];
    }

    function nodeLabel(n, e) {
      var bits = [e.name + (n.main ? "" : ", also plays here"), sectorName[n.sector]];
      if (n.rank) bits.push(rowName[n.sector + "/" + n.row] + ", " + RANK[n.rank].name);
      if (e.ovr != null) bits.push("OVR " + e.ovr + ", " + C.tier(e.ovr, data.ovr_tiers) + (e.ovr_status === "draft" ? ", draft" : ""));
      return bits.join(". ") + ".";
    }

    /* ---- measure labels at screen size, once fonts are in */
    function measure() {
      var keep = scene.getAttribute("transform");
      scene.removeAttribute("transform");
      scene.style.setProperty("--s", 1);
      // offsets of each label's box from its anchor, in screen pixels: labels keep their size as the map zooms
      labels.forEach(function (l) {
        if (l.kind === "company") { l.pos = -1; placeAt(l, 0); }
        var b = l.el.getBBox();
        l.w = b.width; l.h = b.height;
        l.ox = b.x - l.wx; l.oy = b.y - l.wy;
        if (l.kind === "company") {
          // font size and the baseline's drop below the box top, for the other positions
          l.fs = parseFloat(getComputedStyle(l.el).fontSize) || 12.5;
          l.asc = l.ref.r + 1.2 * l.fs - b.y;
        }
      });
      if (keep) scene.setAttribute("transform", keep);
      scene.style.setProperty("--s", 1 / state.t.k);
    }

    /* ---- camera */
    var zoom = d3.zoom().clickDistance(6).on("zoom", onZoom).on("end", function () { updateLabels(); });
    var sel = d3.select(svg).call(zoom).on("dblclick.zoom", null);

    function inset() {
      var open = !panel.hidden;
      if (!open) return { top: 54, right: 0, bottom: 40, left: 0 };
      if (state.view.w > 900) return { top: 54, right: panel.offsetWidth + 12, bottom: 40, left: 0 };
      return { top: 54, right: 0, bottom: panel.offsetHeight + 8, left: 0 };
    }
    // narrow screens drop the tier names, so the galaxy can use their margin
    var terrBounds = Object.keys(lay.sectors).reduce(function (b, sid) {
      var t = lay.sectors[sid];
      return [Math.min(b[0], t.x - t.r), Math.min(b[1], t.y - t.r), Math.max(b[2], t.x + t.r), Math.max(b[3], t.y + t.r)];
    }, [Infinity, Infinity, -Infinity, -Infinity]);
    function galaxyT() {
      var narrow = state.view.w <= 600;
      return C.fit(narrow ? terrBounds : lay.bounds, state.view, { top: 54, right: 0, bottom: 40, left: 0 }, narrow ? 12 : 8, { min: 1e-3, max: 1e3 });
    }
    function sectorT(sid) {
      var t = lay.sectors[sid];
      return C.fit([t.x - t.r, t.y - t.r - 40, t.x + t.r, t.y + t.r], state.view, inset(), 16, { min: state.kGal * 0.7, max: state.kGal * 14 });
    }
    function companyT(n) {
      var k = Math.min(sectorT(n.sector).k * 1.4, state.kGal * 14);
      return C.centre(n, k, state.view, inset());
    }
    function fly(t) {
      var target = d3.zoomIdentity.translate(t.x, t.y).scale(t.k);
      var cur = state.t, w = state.view.w, hh = state.view.h;
      var raw = d3.interpolateZoom([(w / 2 - cur.x) / cur.k, (hh / 2 - cur.y) / cur.k, w / cur.k],
                                   [(w / 2 - t.x) / t.k, (hh / 2 - t.y) / t.k, w / t.k]).duration;
      var ms = C.flightMs(raw, reduce.matches);
      sel.interrupt();
      if (!ms) { sel.call(zoom.transform, target); updateLabels(); return; }
      root.classList.add("is-flying");
      sel.transition().duration(ms).ease(C.easeInOut).call(zoom.transform, target)
        .on("end interrupt", function () { root.classList.remove("is-flying"); updateLabels(); });
    }

    var lastLabels = 0, starFrame = 0;
    function onZoom(ev) {
      state.t = ev.transform;
      scene.setAttribute("transform", ev.transform.toString());
      scene.style.setProperty("--s", 1 / ev.transform.k);
      restyleEdges();
      if (!starFrame) starFrame = requestAnimationFrame(function () { starFrame = 0; drawStars(); });
      var now = performance.now();
      if (now - lastLabels > LABEL_EVERY_MS) { lastLabels = now; updateLabels(); }
    }

    /* ---- stars: three layers that drift at different speeds */
    var LAYERS = [{ n: 260, f: 0.025, size: 0.8, alpha: 0.42, seed: 11 },
                  { n: 120, f: 0.07, size: 1.15, alpha: 0.6, seed: 23 },
                  { n: 46, f: 0.16, size: 1.6, alpha: 0.8, seed: 37 }];
    LAYERS.forEach(function (l) { l.stars = C.stars(l.n, l.seed); });
    var ctx = canvas.getContext("2d");
    function drawStars() {
      var w = state.view.w, hh = state.view.h, dpr = window.devicePixelRatio || 1;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, w, hh);
      var still = reduce.matches, t = state.t, z0 = state.kGal || 1;
      LAYERS.forEach(function (l) {
        var f = still ? 0 : l.f;
        var z = still ? 1 : Math.pow(t.k / z0, f * 1.6);
        var ox = t.x * f, oy = t.y * f;
        l.stars.forEach(function (s) {
          var x = (((s.x - 0.5) * w * z + w / 2 + ox) % w + w) % w;
          var y = (((s.y - 0.5) * hh * z + hh / 2 + oy) % hh + hh) % hh;
          var r = l.size * (0.55 + s.m * 0.7);
          ctx.globalAlpha = l.alpha * (0.45 + s.a * 0.55);
          ctx.fillStyle = s.m > 0.86 ? "#C9DBFF" : "#EEF2F8";
          ctx.beginPath(); ctx.arc(x, y, r, 0, 6.2832); ctx.fill();
        });
      });
      ctx.globalAlpha = 1;
    }

    /* ---- labels: by zoom, by priority, never overlapping */
    // A company's name can sit below, right, left or above its node. Offsets are
    // in ems, so they stay the same on screen at every zoom.
    var POS = [
      { x: 0, y: 1, dx: "0", dy: "1.2em", anchor: "middle" },
      { x: 1, y: 0, dx: "0.5em", dy: "0.35em", anchor: "start" },
      { x: -1, y: 0, dx: "-0.5em", dy: "0.35em", anchor: "end" },
      { x: 0, y: -1, dx: "0", dy: "-0.5em", anchor: "middle" }
    ];
    function placeAt(l, i) {
      if (l.pos === i) return;
      var p = POS[i], r = l.ref.r;
      l.el.setAttribute("x", p.x * r); l.el.setAttribute("y", p.y * r);
      l.el.setAttribute("dx", p.dx); l.el.setAttribute("dy", p.dy);
      l.el.setAttribute("text-anchor", p.anchor);
      l.pos = i;
    }
    function companyBoxes(l) {
      var t = state.t, sx = t.applyX(l.wx), sy = t.applyY(l.wy), rk = l.ref.r * t.k, f = l.fs, a = l.asc;
      return [
        { x: sx - l.w / 2, y: sy + rk + 1.2 * f - a, w: l.w, h: l.h },
        { x: sx + rk + 0.5 * f, y: sy + 0.35 * f - a, w: l.w, h: l.h },
        { x: sx - rk - 0.5 * f - l.w, y: sy + 0.35 * f - a, w: l.w, h: l.h },
        { x: sx - l.w / 2, y: sy - rk - 0.5 * f - a, w: l.w, h: l.h }
      ];
    }
    function screenBox(l) {
      var t = state.t;
      return { x: t.applyX(l.wx) + l.ox, y: t.applyY(l.wy) + l.oy, w: l.w, h: l.h };
    }
    // the screen boxes of the visible nodes, which company and row labels must not cover
    function nodeBoxes() {
      var t = state.t, out = [];
      nodes.forEach(function (n) {
        if (n.el.classList.contains("is-off")) return;
        var x = t.applyX(n.x), y = t.applyY(n.y), r = (n.r + 4) * t.k;
        if (x + r < 0 || y + r < 0 || x - r > state.view.w || y - r > state.view.h) return;
        out.push({ x: x - r, y: y - r, w: 2 * r, h: 2 * r });
      });
      return out;
    }
    function companyPriority(n) {
      if (n.id === state.focus && n.main) return 1000;
      if (n.id === state.selected && n.main) return 950;
      if (n.id === state.hover && n.main) return 900;
      if (n.el.classList.contains("is-lit")) return 400;
      var e = ent[n.id];
      return (n.main ? 100 : 0) + (e.ovr || 30) + (n.sector === state.sector ? 50 : 0);
    }
    function updateLabels() {
      if (!state.view.w) return;
      var z = state.t.k / state.kGal, want = C.labelsAt(z), items = [];
      labels.forEach(function (l, i) {
        var p, special = false;
        if (l.kind === "tier") p = want.tiers && state.view.w > 600 ? 2000 : -1;
        else if (l.kind === "sector") p = want.sectors && filters.sectors.has(l.ref) ? 1500 : -1;
        else if (l.kind === "row") p = want.rows && filters.sectors.has(l.ref) ? 300 : -1;
        else {
          var n = l.ref;
          special = n.main && (n.id === state.focus || n.id === state.selected || n.id === state.hover);
          if (n.el.classList.contains("is-off")) p = -1;
          else if (want.companies || special) p = companyPriority(n);
          else p = -1;
          if (n.el.classList.contains("is-dim") && !special) p = -1;
        }
        if (p < 0) return;
        var lit = l.kind === "company" && l.ref.el.classList.contains("is-lit");
        items.push({ id: i, p: p, avoid: (l.kind === "company" && !special && !lit) || l.kind === "row", force: special,
                     alts: l.kind === "company" ? companyBoxes(l) : [screenBox(l)] });
      });
      var blockers = want.companies || want.rows || state.selected ? nodeBoxes() : [];
      var view = { w: state.view.w, h: state.view.h, top: 50, bottom: state.view.w > 600 ? 30 : 46 };
      var shown = C.collide(items, view, 3, blockers);
      labels.forEach(function (l, i) {
        var at = shown.get(i);
        if (at !== undefined && l.kind === "company") placeAt(l, at);
        l.el.classList.toggle("is-shown", at !== undefined);
      });
    }

    /* ---- relationships */
    var drawn = [];
    function enabledEdges(id) {
      return (edgesOf[id] || []).filter(function (e) {
        var other = e.a === id ? e.b : e.a;
        return filters.groups[e.group] && mainOf[other] && !mainOf[other].el.classList.contains("is-off");
      });
    }
    function drawEdges(id) {
      gEdges.textContent = "";
      drawn = [];
      if (!id || !mainOf[id]) return;
      enabledEdges(id).forEach(function (e) {
        var a = mainOf[e.a], b = mainOf[e.b];
        var bend = a.sector === b.sector ? 0.14 : 0.24;
        var path = el("path", { "class": "edge edge--" + e.group }, gEdges);
        var arrow = e.group === "backers" ? el("path", { "class": "edge__arrow" }, gEdges) : null;
        drawn.push({ a: a, b: b, bend: bend, path: path, arrow: arrow, group: e.group });
      });
      restyleEdges();
    }
    function restyleEdges() {
      var s = 1 / state.t.k;
      drawn.forEach(function (d) {
        var g = d.arrow ? 9 * s : 4 * s;
        var arc = C.arc(d.a, d.b, d.a.r + 3, d.b.r + 3, d.bend, g, d.a.id, d.b.id);
        d.path.setAttribute("d", arc.d);
        d.path.setAttribute("stroke-width", 1.7 * s);
        if (d.group === "rivals") d.path.setAttribute("stroke-dasharray", 7 * s + " " + 5 * s);
        if (d.arrow) {
          var L = 9 * s, W = 4.5 * s, ex = arc.end.x + arc.dir.x * L, ey = arc.end.y + arc.dir.y * L;
          d.arrow.setAttribute("d", "M" + ex + " " + ey + " L" + (arc.end.x - arc.dir.y * W) + " " + (arc.end.y + arc.dir.x * W) +
                               " L" + (arc.end.x + arc.dir.y * W) + " " + (arc.end.y - arc.dir.x * W) + " Z");
        }
      });
    }

    /* ---- selection, dimming and filters */
    function neighbours(id) {
      var out = {};
      enabledEdges(id).forEach(function (e) { out[e.a === id ? e.b : e.a] = e.group; });
      return out;
    }
    function applyState() {
      var near = state.selected ? neighbours(state.selected) : {};
      nodes.forEach(function (n) {
        var off = !filters.sectors.has(n.sector) || (n.rank && !filters.ranks.has(n.rank));
        n.el.classList.toggle("is-off", off);
        n.el.classList.toggle("is-sel", n.id === state.selected);
        var rel = n.main && near[n.id];
        n.el.classList.toggle("is-lit", !!rel);
        if (rel) n.el.setAttribute("data-rel", rel); else n.el.removeAttribute("data-rel");
        n.el.classList.toggle("is-dim", !!state.selected && n.id !== state.selected && !rel);
        var tabbable = !off && state.level !== "galaxy" && n.sector === state.sector;
        n.el.setAttribute("tabindex", tabbable ? "0" : "-1");
      });
      Object.keys(terrEls).forEach(function (sid) {
        terrEls[sid].classList.toggle("is-off", !filters.sectors.has(sid));
        terrEls[sid].classList.toggle("is-here", sid === state.sector);
        terrEls[sid].setAttribute("tabindex", state.level === "galaxy" && filters.sectors.has(sid) ? "0" : "-1");
      });
      drawEdges(state.hover || state.focus || state.selected);
      backBtn.hidden = state.level === "galaxy";
      where.textContent = state.level === "galaxy" ? "All sectors" :
        sectorName[state.sector] + (state.selected ? " · " + ent[state.selected].name : "");
      [].forEach.call(document.querySelectorAll(".chip[data-sector]"), function (c) {
        c.setAttribute("aria-pressed", c.dataset.sector === state.sector ? "true" : "false");
      });
      updateLabels();
    }

    function goGalaxy(keepFocus) {
      var prev = state.sector;
      state.level = "galaxy"; state.sector = null; state.selected = null;
      var lost = closePanel(); applyState(); fly(galaxyT());
      if (lost || keepFocus) refocus(null, prev);
    }
    function goSector(sid, keepFocus) {
      var prevSel = state.selected;
      state.level = "sector"; state.sector = sid; state.selected = null;
      var lost = closePanel(); applyState(); fly(sectorT(sid));
      if (lost || keepFocus) refocus(prevSel, sid);
    }
    function goCompany(id, focusCard) {
      var n = mainOf[id];
      if (!n) return;
      // a company in a filtered-out sector or rank is switched back on
      if (!filters.sectors.has(n.sector) || (n.rank && !filters.ranks.has(n.rank))) {
        filters.sectors.add(n.sector);
        if (n.rank) filters.ranks.add(n.rank);
        var boxes = filtersBox.querySelectorAll('[data-fsector="' + n.sector + '"], [data-frank="' + n.rank + '"]');
        [].forEach.call(boxes, function (b) { b.checked = true; });
      }
      state.level = "company"; state.sector = n.sector; state.selected = id;
      openPanel(id, focusCard); applyState(); fly(companyT(n));
    }
    function back(keepFocus) {
      if (state.level === "company") goSector(state.sector, keepFocus);
      else if (state.level === "sector") goGalaxy(keepFocus);
    }

    /* ---- the player card */
    function closePanel() {
      var hadFocus = panel.contains(document.activeElement);
      panel.hidden = true; panel.textContent = ""; root.classList.remove("has-card");
      return hadFocus;
    }
    // after the card closes or the camera steps out, keep keyboard focus on the map
    function refocus(prevSelected, prevSector) {
      var t = state.level === "sector" && prevSelected && mainOf[prevSelected] ? mainOf[prevSelected].el : terrEls[prevSector];
      if (t) t.focus({ preventScroll: true });
    }
    function trustLink(url, trust) {
      return h("span", { cls: "pc__src" }, [h("span", { cls: "conf conf--" + trust, text: trust }), " ",
        h("a", { href: url, target: "_blank", rel: "noopener noreferrer", text: host(url) })]);
    }
    function ratingBlock(e) {
      var rated = e.ovr != null, tierName = rated ? C.tier(e.ovr, data.ovr_tiers) : "Unrated";
      return h("div", { cls: "pc__ovr", "data-tier": tierName }, [
        h("span", { cls: "pc__num", text: rated ? String(e.ovr) : "NR" }),
        h("span", { cls: "pc__k", text: rated ? "OVR" : "Not rated" }),
        h("span", { cls: "pc__tier", text: tierName }),
        rated && e.ovr_status === "draft" ? h("span", { cls: "pc__draft", text: "Draft" }) : null
      ]);
    }
    function relations(id) {
      var groups = { allies: [], rivals: [], backers: [] };
      (edgesOf[id] || []).forEach(function (e) {
        var other = e.a === id ? e.b : e.a, oe = ent[other];
        var verb = VERB[e.type] ? (e.a === id ? VERB[e.type][0] : VERB[e.type][1]) + " " : "";
        var elsewhere = oe.home && oe.home !== ent[id].home ? h("span", { cls: "pc__in", text: " in " + sectorName[oe.home] }) : null;
        var go = h("button", { type: "button", cls: "pc__go", "data-go": other }, [
          verb ? h("span", { cls: "pc__verb", text: verb }) : null, oe.name]);
        groups[e.group].push(h("li", {}, [go, elsewhere, h("p", { cls: "pc__x", text: e.text }), trustLink(e.src, e.conf)]));
      });
      return ["allies", "rivals", "backers"].filter(function (g) { return groups[g].length; }).map(function (g) {
        return h("section", { cls: "pc__rel pc__rel--" + g }, [h("h3", { cls: "pc__h", text: GROUP_LABEL[g] }), h("ul", {}, groups[g])]);
      });
    }
    function cardFacts(id) {
      var n = mainOf[id], cards = cardsOf[id] || [];
      var home = cards.filter(function (c) { return c.sector === n.sector && c.row === n.row; })[0];
      if (!home) return [];
      var pl = home.pl, also = cards.filter(function (c) { return c !== home; });
      return [
        h("div", { cls: "pc__fact" }, [h("h3", { cls: "pc__h", text: "Key figure" }), h("p", { text: pl.stat })]),
        h("div", { cls: "pc__fact" }, [h("h3", { cls: "pc__h", text: RANK[pl.t].why }), h("p", { text: pl.why })]),
        h("div", { cls: "pc__fact" }, [h("h3", { cls: "pc__h", text: "What could change it" }), h("p", { text: pl.cond })]),
        trustLink(pl.src, pl.conf || "sourced"),
        also.length ? h("p", { cls: "pc__also", text: "Also plays in " + also.map(function (c) {
          return sectorName[c.sector] + ", " + rowName[c.sector + "/" + c.row] + " (" + RANK[c.pl.t].name.toLowerCase() + ")";
        }).join(" and ") + "." }) : null
      ];
    }
    function openPanel(id, fromPanel) {
      var e = ent[id], n = mainOf[id];
      var card = (cardsOf[id] || []).filter(function (c) { return c.sector === n.sector && c.row === n.row; })[0];
      var rankBits = card ? [h("span", { cls: "badge", text: RANK[card.pl.t].name }),
        card.pl.badge ? h("span", { cls: "badge badge--label", text: card.pl.badge }) : null] : [];
      var name = h("h2", { cls: "pc__name", tabindex: "-1", text: e.name });
      panel.textContent = "";
      panel.className = "pcard c-" + n.home;
      [
        h("button", { type: "button", cls: "pc__close", "aria-label": "Close card", text: "×" }),
        h("header", { cls: "pc__head" }, [
          ratingBlock(e),
          h("div", { cls: "pc__id" }, [
            h("span", { cls: "pc__mono", "aria-hidden": "true", text: C.initials(e.name) }),
            h("div", {}, [name,
              h("p", { cls: "pc__meta", text: sectorName[n.sector] + (card ? " · " + rowName[n.sector + "/" + n.row] : "") }),
              h("p", { cls: "pc__rank" }, rankBits)])
          ])
        ]),
        e.ovr != null ? h("section", { cls: "pc__why" }, [h("h3", { cls: "pc__h", text: "Why this rating" }),
          h("p", { text: e.ovr_reason })].concat((e.ovr_evidence || []).map(function (v) { return trustLink(v.url, v.trust); }))) : null,
        h("p", { cls: "pc__desc", text: e.description })
      ].concat(cardFacts(id), relations(id)).forEach(function (c) { if (c) panel.appendChild(c); });
      panel.hidden = false;
      root.classList.add("has-card");
      panel.scrollTop = 0;
      if (fromPanel) name.focus({ preventScroll: true });
    }
    panel.addEventListener("click", function (ev) {
      var go = ev.target.closest(".pc__go");
      if (go) { goCompany(go.dataset.go, true); return; }
      if (ev.target.closest(".pc__close")) goSector(state.sector, true);
    });

    /* ---- input */
    function nodeFrom(t) { var g = t.closest && t.closest(".node"); return g ? nodes[[].indexOf.call(gNodes.children, g)] : null; }
    function activate(target, byKey) {
      var n = nodeFrom(target);
      if (n) { if (!n.el.classList.contains("is-off")) goCompany(n.id, byKey); return true; }
      var terr = target.closest && target.closest(".terr");
      if (terr) {
        var sid = terr.dataset.sector;
        if (state.level === "galaxy" || sid !== state.sector) goSector(sid);
        else if (state.level === "company") goSector(sid);
        return true;
      }
      return false;
    }
    svg.addEventListener("click", function (ev) { activate(ev.target); });
    svg.addEventListener("keydown", function (ev) {
      if ((ev.key === "Enter" || ev.key === " ") && activate(ev.target, true)) ev.preventDefault();
    });
    svg.addEventListener("pointerover", function (ev) {
      if (ev.pointerType !== "mouse") return;
      var n = nodeFrom(ev.target);
      var id = n && n.main && !n.el.classList.contains("is-off") ? n.id : null;
      if (id !== state.hover) { state.hover = id; drawEdges(id || state.focus || state.selected); updateLabels(); }
    });
    svg.addEventListener("pointerleave", function () {
      if (state.hover) { state.hover = null; drawEdges(state.focus || state.selected); updateLabels(); }
    });
    svg.addEventListener("focusin", function (ev) {
      var n = nodeFrom(ev.target);
      state.focus = n && n.main ? n.id : null;
      drawEdges(state.hover || state.focus || state.selected); updateLabels();
    });
    svg.addEventListener("focusout", function () {
      state.focus = null; drawEdges(state.hover || state.selected); updateLabels();
    });
    if (escHandler) document.removeEventListener("keydown", escHandler);
    escHandler = function (ev) {
      if (ev.key !== "Escape" || !document.body.classList.contains("view-map")) return;
      if (ev.target.closest && ev.target.closest("input, textarea, select")) return;
      if (!filtersBox.hidden) { toggleFilters(false); filtersBtn.focus(); return; }
      back(root.contains(document.activeElement));
    };
    document.addEventListener("keydown", escHandler);
    backBtn.addEventListener("click", function () { back(false); });
    root.querySelector('[data-zoom="home"]').addEventListener("click", function () { goGalaxy(false); });
    [].forEach.call(root.querySelectorAll('[data-zoom="in"], [data-zoom="out"]'), function (b) {
      b.addEventListener("click", function () {
        sel.interrupt().transition().duration(reduce.matches ? 0 : 320).ease(C.easeInOut)
          .call(zoom.scaleBy, b.dataset.zoom === "in" ? 1.6 : 1 / 1.6);
      });
    });
    function toggleFilters(open) {
      filtersBox.hidden = !open;
      filtersBtn.setAttribute("aria-expanded", open ? "true" : "false");
    }
    filtersBtn.addEventListener("click", function () { toggleFilters(filtersBox.hidden); });
    filtersBox.addEventListener("change", function (ev) {
      var i = ev.target;
      if (i.dataset.fsector) filters.sectors[i.checked ? "add" : "delete"](i.dataset.fsector);
      if (i.dataset.frank) filters.ranks[i.checked ? "add" : "delete"](i.dataset.frank);
      applyState();
    });
    [].forEach.call(document.querySelectorAll(".toggles input[data-group]"), function (i) {
      i.addEventListener("change", function () { filters.groups[i.dataset.group] = i.checked; applyState(); });
    });
    [].forEach.call(document.querySelectorAll(".chip[data-sector]"), function (c) {
      c.addEventListener("click", function () { if (document.body.classList.contains("view-map")) goSector(c.dataset.sector); });
    });

    var byName = {};
    Object.keys(ent).forEach(function (k) { if (mainOf[k]) byName[ent[k].name.toLowerCase()] = k; });
    var search = document.getElementById("atlas-search"), lastQ = "", lastAt = 0;
    function runSearch() {
      if (!document.body.classList.contains("view-map")) return;
      var q = search.value.trim().toLowerCase();
      // Enter and the change event both fire for one search
      if (!q || (q === lastQ && performance.now() - lastAt < 400)) return;
      lastQ = q; lastAt = performance.now();
      var k = byName[q] || byName[Object.keys(byName).filter(function (n) { return n.indexOf(q) > -1; }).sort()[0]];
      if (k) goCompany(k); else where.textContent = "No company matches “" + search.value.trim() + "”";
    }
    search.addEventListener("change", runSearch);
    search.addEventListener("keydown", function (e) { if (e.key === "Enter") runSearch(); });

    /* ---- size */
    function resize() {
      var r = stage.getBoundingClientRect(), dpr = window.devicePixelRatio || 1;
      if (!r.width || !r.height) return;
      state.view = { w: r.width, h: r.height };
      canvas.width = Math.round(r.width * dpr); canvas.height = Math.round(r.height * dpr);
      state.kGal = galaxyT().k;
      zoom.scaleExtent([state.kGal * 0.6, state.kGal * 16]).extent([[0, 0], [r.width, r.height]])
        .translateExtent([[lay.bounds[0] - 1200, lay.bounds[1] - 1200], [lay.bounds[2] + 1200, lay.bounds[3] + 1200]]);
      var t = state.level === "company" ? companyT(mainOf[state.selected]) :
              state.level === "sector" ? sectorT(state.sector) : galaxyT();
      sel.interrupt().call(zoom.transform, d3.zoomIdentity.translate(t.x, t.y).scale(t.k));
      measure(); drawStars(); updateLabels();
    }
    if (window.ResizeObserver) new ResizeObserver(resize).observe(stage);
    else window.addEventListener("resize", resize);
    reduce.addEventListener && reduce.addEventListener("change", drawStars);

    resize();
    applyState();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { measure(); updateLabels(); });

    var list = document.getElementById("atlas-names");
    Object.keys(ent).forEach(function (k) {
      if (!mainOf[k] || ent[k].home) return;
      list.appendChild(h("option", { value: ent[k].name, "data-backer": "" }));
    });

    return { goCompany: goCompany, goSector: goSector, goGalaxy: goGalaxy, state: state };
  }

  // the sticky control bar's height, so the map fits under it
  var bar = document.querySelector(".atlas-bar");
  function barHeight() { if (bar) document.documentElement.style.setProperty("--atlas-bar", bar.offsetHeight + "px"); }
  if (bar && window.ResizeObserver) new ResizeObserver(barHeight).observe(bar);
  barHeight();

  /* ------------------------------------------------------- start */
  var hash = location.hash.replace("#", "");
  var forced = hash.indexOf("sector-") === 0 || hash.indexOf("c-") === 0;
  setView(forced ? "list" : (readView() === "list" ? "list" : "map"), false);
  // for checks in the browser console and tests
  window.AtlasMap = { ready: function () { return loading; }, api: function () { return M; } };
})();
