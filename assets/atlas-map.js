/* Tech Atlas: the Map view and the Map/List switch.

   The List works without this file. With it, the page opens on a galaxy of
   sector planets: click one to fly in, click a company to bring it and its
   neighbours forward, and press Esc or Back to step out. PixiJS (the WebGL
   renderer) and the data (tech-atlas.json) load only when the Map is first
   shown. The scene is atlas-map-scene.js, the card atlas-map-card.js, and the
   arithmetic atlas-map-core.js. Addresses: #c-<company> and #s-<sector>. */
(function () {
  "use strict";
  var C = window.AtlasMapCore;
  var root = document.getElementById("atlas-map");
  if (!root || !C || !window.AtlasMapScene || !window.AtlasMapCard) return;
  document.body.classList.add("js");

  var PIXI_URL = "https://cdn.jsdelivr.net/npm/pixi.js@8.22.0/dist/pixi.min.js";
  var PIXI_SRI = "sha384-sQhAUuZTvdanRcBHbVCTasnEWH28GGEK87FJGPj/JaqwL/15KWQwKe7whTHdCkwm";
  var VIEW_KEY = "atlas-view", HINT_KEY = "atlas-map-hint";
  var DRAG_SLOP = 6, VELOCITY_WINDOW = 90, LOAD_TIMEOUT_MS = 12000;

  var host = root.querySelector(".amap__canvas");
  var keys = root.querySelector(".amap__keys");
  var panel = root.querySelector(".pcard");
  var msg = root.querySelector(".amap__msg");
  var backBtn = root.querySelector(".amap__back");
  var where = root.querySelector(".amap__where");
  var tip = root.querySelector(".amap__tip");
  var hint = root.querySelector(".amap__hint");
  var mini = root.querySelector(".amap__mini");
  var filtersBtn = root.querySelector('[aria-controls="amap-filters"]');
  var filtersBox = document.getElementById("amap-filters");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");

  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } return null; }
  function inMap() { return document.body.classList.contains("view-map"); }

  /* ------------------------------------------------------- the switch */
  var loading = null, M = null, pendingRoute = null;
  function setView(v, remember) {
    var isMap = v === "map";
    document.body.classList.toggle("view-map", isMap);
    root.hidden = !isMap;
    [].forEach.call(document.querySelectorAll(".view__b"), function (b) { b.setAttribute("aria-pressed", b.dataset.view === v ? "true" : "false"); });
    [].forEach.call(document.querySelectorAll("#atlas-names option[data-backer]"), function (o) { o.disabled = !isMap; });
    if (remember) store(VIEW_KEY, v);
    // a map address (#c-, #s-) would reopen the Map on reload, so the List drops it
    if (!isMap && /^#(c|s)-[a-z0-9_]+$/.test(location.hash)) history.replaceState(null, "", location.pathname + location.search);
    if (isMap) ensureMap();
    running();
  }
  // run the scene only while the Map is chosen, on screen and in a visible tab
  var onScreen = true;
  function running() {
    if (!M) return;
    if (inMap() && onScreen && !document.hidden) M.scene.resume(); else M.scene.pause();
  }
  if (window.IntersectionObserver) new IntersectionObserver(function (es) { onScreen = es[0].isIntersecting; running(); }).observe(root);
  document.addEventListener("visibilitychange", running);
  [].forEach.call(document.querySelectorAll(".view__b"), function (b) {
    b.addEventListener("click", function () {
      setView(b.dataset.view, true);
      if (b.dataset.view === "map") root.scrollIntoView({ behavior: reduce.matches ? "auto" : "smooth", block: "start" });
    });
  });

  function loadPixi() {
    if (window.PIXI) return Promise.resolve(window.PIXI);
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = PIXI_URL; s.integrity = PIXI_SRI; s.crossOrigin = "anonymous";
      s.onload = function () { window.PIXI ? resolve(window.PIXI) : reject(new Error("PixiJS missing")); };
      s.onerror = function () { s.remove(); reject(new Error("PixiJS failed to load")); };
      document.head.appendChild(s);
    });
  }
  function loadData() {
    return fetch("tech-atlas.json").then(function (r) {
      if (!r.ok) throw new Error("tech-atlas.json " + r.status);
      return r.json();
    });
  }
  function fontsReady() {
    if (!document.fonts || !document.fonts.load) return Promise.resolve();
    return Promise.all([document.fonts.load('600 17px "Cormorant Garamond"'), document.fonts.load('700 15px "Cormorant Garamond"')])
      .catch(function () { /* the map falls back to Georgia */ });
  }
  function timeout(ms) {
    return new Promise(function (_, reject) { setTimeout(function () { reject(new Error("map load timed out")); }, ms); });
  }
  function ensureMap() {
    if (loading) return loading;
    root.classList.remove("is-failed");
    msg.textContent = "Loading the map.";
    msg.hidden = false;
    var all = Promise.all([loadPixi(), loadData(), fontsReady()]);
    loading = Promise.race([all, timeout(LOAD_TIMEOUT_MS)]).then(function (res) {
      return createMap(res[0], res[1]);
    }).then(function (m) {
      M = m;
      msg.hidden = true;
      running();
    }).catch(function () {
      var stale = document.querySelector('script[src="' + PIXI_URL + '"]');
      if (stale && !window.PIXI) stale.remove();
      msg.textContent = "The map could not load, so the List is showing instead.";
      loading = null;
      setView("list", false);
      root.hidden = false;
      root.classList.add("is-failed");
    });
    return loading;
  }

  /* --------------------------------------------------------- the map */
  function createMap(PIXI, data) {
    var ent = data.entities, sectorName = { backers: "Owners and backers" }, rowName = {}, cardsOf = {};
    data.sectors.forEach(function (s) {
      sectorName[s.id] = s.name;
      s.positions.forEach(function (p) {
        rowName[s.id + "/" + p.id] = p.name;
        p.players.forEach(function (pl) { (cardsOf[pl.e] = cardsOf[pl.e] || []).push({ sector: s.id, row: p.id, pl: pl }); });
      });
    });
    var onMap = {};
    data.map.cards.forEach(function (c) { if (c.main) onMap[c.company] = c.sector; });
    var companies = new Set(Object.keys(onMap)), sectorSet = new Set(Object.keys(data.map.sectors));
    var nav = { level: "galaxy", sector: null, selected: null, tab: "ratings" };
    var filters = { sectors: new Set(Object.keys(data.map.sectors)), ranks: new Set(["starter", "second", "rookie"]), groups: {} };
    [].forEach.call(document.querySelectorAll(".toggles input[data-group]"), function (i) { filters.groups[i.dataset.group] = i.checked; });
    var frameHooks = [];

    return AtlasMapScene.create(PIXI, data, host, {
      reduced: function () { return reduce.matches; },
      reserveTop: 50, reserveBottom: 34,
      onFrame: function (cam, view) { frameHooks.forEach(function (f) { f(cam, view); }); }
    }).then(function (scene) {
      scene.setFilters(filters);

      /* ---- size: the map fills whatever the card leaves */
      function resize() {
        var r = host.getBoundingClientRect();
        if (!r.width || !r.height) return;
        var before = scene.view();
        if (Math.abs(before.w - r.width) < 1 && Math.abs(before.h - r.height) < 1) return;
        scene.resize(r.width, r.height);
        if (nav.level === "galaxy") scene.jump(scene.galaxyCam());
        else if (nav.level === "sector") scene.jump(scene.sectorCam(nav.sector));
        else if (nav.level === "company") scene.focus(nav.selected);
        drawMini(true);
      }
      if (window.ResizeObserver) new ResizeObserver(resize).observe(host);
      else window.addEventListener("resize", resize);

      /* ---- where we are */
      function sync() {
        backBtn.hidden = nav.level === "galaxy";
        where.textContent = nav.level === "galaxy" ? "All sectors" :
          sectorName[nav.sector] + (nav.selected ? " · " + ent[nav.selected].name : "");
        scene.setSector(nav.sector);
        var hash = C.hashFor(nav);
        if (location.hash !== hash) history.replaceState(null, "", hash || location.pathname + location.search);
        [].forEach.call(document.querySelectorAll(".chip[data-sector]"), function (c) {
          c.setAttribute("aria-pressed", c.dataset.sector === nav.sector ? "true" : "false");
        });
        keysDirty = true;
      }
      function goGalaxy() {
        nav = { level: "galaxy", sector: null, selected: null, tab: nav.tab };
        scene.focus(null); closeCard(); sync(); scene.fly(scene.galaxyCam());
      }
      function goSector(sid) {
        nav = { level: "sector", sector: sid, selected: null, tab: nav.tab };
        scene.focus(null); closeCard(); sync(); scene.fly(scene.sectorCam(sid));
      }
      function goCompany(id, focusCard) {
        if (!companies.has(id)) return;
        var sid = onMap[id];
        if (!filters.sectors.has(sid)) { filters.sectors.add(sid); tick("[data-fsector='" + sid + "']"); scene.setFilters(filters); }
        nav = { level: "company", sector: sid, selected: id, tab: nav.tab };
        openCard(id, focusCard);
        resize();
        scene.focus(id);
        sync();
        scene.fly(scene.companyCam(id));
      }
      function tick(sel) { var b = filtersBox.querySelector(sel); if (b) b.checked = true; }
      function back() {
        if (nav.level === "company") goSector(nav.sector);
        else if (nav.level === "sector") goGalaxy();
      }

      /* ---- the card */
      function openCard(id, focusCard) {
        var name = AtlasMapCard.render(panel, id, { data: data, sectorName: sectorName, rowName: rowName, cardsOf: cardsOf, tab: nav.tab });
        // on phones the card opens as a peek under the map, and this shows the rest
        var more = document.createElement("button"), open = root.classList.contains("card-open");
        more.type = "button"; more.className = "pc__more";
        more.setAttribute("aria-expanded", open ? "true" : "false");
        more.textContent = open ? "Show the map" : "Show the card";
        panel.insertBefore(more, panel.firstChild);
        panel.hidden = false;
        root.classList.add("has-card");
        panel.scrollTop = 0;
        if (focusCard) name.focus({ preventScroll: true });
      }
      function closeCard() {
        var had = panel.contains(document.activeElement);
        panel.hidden = true; panel.textContent = ""; root.classList.remove("has-card", "card-open");
        resize();
        return had;
      }
      panel.addEventListener("click", function (ev) {
        if (ev.target.closest(".pc__more")) {
          var open = !root.classList.contains("card-open");
          root.classList.toggle("card-open", open);
          ev.target.setAttribute("aria-expanded", open ? "true" : "false");
          ev.target.textContent = open ? "Show the map" : "Show the card";
          resize();
          return;
        }
        var go = ev.target.closest(".pc__go");
        if (go) { goCompany(go.dataset.go, true); return; }
        if (ev.target.closest(".pc__close")) { var prev = nav.selected; goSector(nav.sector); focusKey("node:" + prev); return; }
        var tabB = ev.target.closest(".pc__tab");
        if (tabB) { showTab(tabB.dataset.tab, true); return; }
        var bar = ev.target.closest(".pc__bar");
        if (bar) {
          var open = bar.getAttribute("aria-expanded") !== "true";
          bar.setAttribute("aria-expanded", open ? "true" : "false");
          bar.nextElementSibling.hidden = !open;
        }
      });
      panel.addEventListener("keydown", function (ev) {
        var tabB = ev.target.closest(".pc__tab");
        if (!tabB || (ev.key !== "ArrowRight" && ev.key !== "ArrowLeft")) return;
        var i = AtlasMapCard.TABS.indexOf(tabB.dataset.tab), n = AtlasMapCard.TABS.length;
        showTab(AtlasMapCard.TABS[(i + (ev.key === "ArrowRight" ? 1 : n - 1)) % n], true);
        ev.preventDefault();
      });
      function showTab(t, focusTab) {
        nav.tab = t;
        openCard(nav.selected);
        if (focusTab) { var b = panel.querySelector('[data-tab="' + t + '"]'); if (b) b.focus(); }
      }

      /* ---- keyboard: a button over each thing you can pick */
      var keysDirty = true, keyEls = {}, keyTarget = {};
      function keyLabel(t) {
        if (t.kind === "sector") return sectorName[t.id] + ". Press Enter to fly in.";
        var e = ent[t.id];
        return e.name + (e.ovr != null ? ", OVR " + e.ovr : "") + (t.kind === "proxy" && t.id === nav.selected ? ", selected" : "") + ".";
      }
      function placeKeys() {
        var list = scene.targets(nav.level, nav.sector), seen = {};
        list.forEach(function (t) {
          var key = t.kind + ":" + t.id, b = keyEls[key];
          if (!b) {
            b = document.createElement("button");
            b.type = "button"; b.className = "amap__key"; b.dataset.kind = t.kind; b.dataset.id = t.id;
            b.addEventListener("focus", function () {
              scene.setKeyFocus(t.kind === "sector" ? null : t.id);
              // a company tabbed to while zoomed in may be off screen, so the camera brings it into view
              var cur = keyTarget[key], v = scene.view();
              if (cur && cur.wx !== undefined && (cur.x < 30 || cur.y < 60 || cur.x > v.w - 30 || cur.y > v.h - 40)) {
                scene.fly({ x: cur.wx, y: cur.wy, k: scene.cam().k });
              }
            });
            b.addEventListener("blur", function () { scene.setKeyFocus(null); });
            keyEls[key] = b;
          }
          keyTarget[key] = t;
          b.setAttribute("aria-label", keyLabel(t));
          b.style.transform = "translate(" + (t.x - t.r) + "px," + (t.y - t.r) + "px)";
          b.style.width = b.style.height = 2 * t.r + "px";
          if (keysDirty) keys.appendChild(b);
          seen[key] = true;
        });
        Object.keys(keyEls).forEach(function (k) {
          if (!seen[k]) { if (keyEls[k] === document.activeElement) { keyEls[k].blur(); } keyEls[k].remove(); delete keyEls[k]; }
        });
        keysDirty = false;
      }
      function focusKey(key) {
        placeKeys();
        var b = keyEls[key];
        if (b) b.focus({ preventScroll: true });
      }
      keys.addEventListener("click", function (ev) {
        var b = ev.target.closest(".amap__key");
        if (!b) return;
        if (b.dataset.kind === "sector") { goSector(b.dataset.id); setTimeout(function () { focusFirst(); }, 0); }
        else if (b.dataset.id !== nav.selected) goCompany(b.dataset.id, true);
      });
      function focusFirst() { placeKeys(); var b = keys.querySelector(".amap__key"); if (b) b.focus({ preventScroll: true }); }
      var frameN = 0;
      frameHooks.push(function () { if (keysDirty || ++frameN % 3 === 0) placeKeys(); });

      /* ---- escape steps out one level */
      document.addEventListener("keydown", function (ev) {
        if (ev.key !== "Escape" || !inMap()) return;
        if (ev.target.closest && ev.target.closest("input, textarea, select")) return;
        dismissHint();
        if (!filtersBox.hidden) { toggleFilters(false); filtersBtn.focus(); return; }
        var inside = root.contains(document.activeElement), prev = { sel: nav.selected, sec: nav.sector };
        back();
        if (inside || document.activeElement === document.body) {
          if (nav.level === "sector" && prev.sel) focusKey("node:" + prev.sel);
          else if (nav.level === "galaxy" && prev.sec) focusKey("sector:" + prev.sec);
        }
      });
      backBtn.addEventListener("click", back);
      root.querySelector('[data-zoom="home"]').addEventListener("click", goGalaxy);
      [].forEach.call(root.querySelectorAll('[data-zoom="in"], [data-zoom="out"]'), function (b) {
        b.addEventListener("click", function () {
          var v = scene.view();
          scene.zoomBy(b.dataset.zoom === "in" ? 1.6 : 1 / 1.6, { x: v.w / 2, y: v.h / 2 });
        });
      });

      /* ---- pointer: drag with glide, pinch, wheel and trackpad zoom */
      var pts = new Map(), drag = null, samples = [], pinch = null;
      function local(ev) { var r = host.getBoundingClientRect(); return { x: ev.clientX - r.left, y: ev.clientY - r.top }; }
      host.addEventListener("pointerdown", function (ev) {
        dismissHint();
        try { host.setPointerCapture(ev.pointerId); } catch (e) { /* the pointer has already gone */ }
        pts.set(ev.pointerId, local(ev));
        scene.dragStart();
        if (pts.size === 2) {
          var p = Array.from(pts.values());
          pinch = { d: Math.hypot(p[0].x - p[1].x, p[0].y - p[1].y), m: { x: (p[0].x + p[1].x) / 2, y: (p[0].y + p[1].y) / 2 } };
          drag = null;
        } else drag = { start: local(ev), last: local(ev), moved: false };
        samples = [];
      });
      host.addEventListener("pointermove", function (ev) {
        var p = local(ev);
        if (!pts.has(ev.pointerId)) { hover(p, ev.pointerType); return; }
        pts.set(ev.pointerId, p);
        if (pinch && pts.size >= 2) {
          var q = Array.from(pts.values()), d = Math.hypot(q[0].x - q[1].x, q[0].y - q[1].y);
          var m = { x: (q[0].x + q[1].x) / 2, y: (q[0].y + q[1].y) / 2 };
          scene.dragBy(m.x - pinch.m.x, m.y - pinch.m.y);
          scene.zoomBy(d / pinch.d, m);
          pinch = { d: d, m: m };
          return;
        }
        if (!drag) return;
        if (!drag.moved && Math.hypot(p.x - drag.start.x, p.y - drag.start.y) > DRAG_SLOP) { drag.moved = true; host.classList.add("is-dragging"); }
        if (drag.moved) {
          scene.dragBy(p.x - drag.last.x, p.y - drag.last.y);
          var now = performance.now();
          samples.push({ t: now, x: p.x, y: p.y });
          while (samples.length && now - samples[0].t > VELOCITY_WINDOW) samples.shift();
        }
        drag.last = p;
      });
      function end(ev) {
        var p = local(ev);
        pts.delete(ev.pointerId);
        host.classList.remove("is-dragging");
        if (pinch) { if (pts.size < 2) pinch = null; drag = null; return; }
        if (!drag) return;
        if (!drag.moved && ev.type === "pointerup") click(p);
        else if (samples.length > 1) {
          var a = samples[0], b = samples[samples.length - 1], dt = Math.max(16, b.t - a.t);
          scene.release(performance.now() - b.t < 60 ? { x: (b.x - a.x) / dt, y: (b.y - a.y) / dt } : null);
        }
        drag = null;
      }
      host.addEventListener("pointerup", end);
      host.addEventListener("pointercancel", end);
      host.addEventListener("pointerleave", function () { scene.setHover(null); hideTip(); host.style.cursor = ""; });
      host.addEventListener("wheel", function (ev) {
        ev.preventDefault();
        dismissHint();
        var dy = ev.deltaY * (ev.deltaMode === 1 ? 16 : ev.deltaMode === 2 ? 400 : 1);
        // a trackpad pinch arrives as a wheel event with ctrlKey set
        scene.zoomBy(Math.exp(-dy * (ev.ctrlKey ? 0.011 : 0.0016)), local(ev));
      }, { passive: false });
      // Safari reports trackpad pinches as gesture events instead
      var gScale = 1;
      host.addEventListener("gesturestart", function (ev) { ev.preventDefault(); gScale = 1; });
      host.addEventListener("gesturechange", function (ev) {
        ev.preventDefault();
        scene.zoomBy(ev.scale / gScale, local(ev));
        gScale = ev.scale;
      });

      function click(p) {
        var hit = scene.pick(p);
        if (!hit) return;
        if (hit.kind === "proxy" || hit.kind === "line") { if (hit.id !== nav.selected) goCompany(hit.id); return; }
        if (hit.kind === "node") { goCompany(hit.id); return; }
        if (hit.kind === "sector") { if (nav.level !== "sector" || nav.sector !== hit.id) goSector(hit.id); return; }
        if (hit.kind === "bundle") showTip(hit.text, p);
      }
      function hover(p, type) {
        if (type !== "mouse") return;
        var hit = scene.pick(p);
        host.style.cursor = hit && hit.kind !== "focus-bg" ? "pointer" : "";
        if (!hit || hit.kind === "focus-bg") { scene.setHover(null); hideTip(); return; }
        if (hit.kind === "bundle") { scene.setHover("bundle:" + hit.id); showTip(hit.text, p); return; }
        if (hit.kind === "line" || hit.kind === "proxy") {
          scene.setHover(hit.kind + ":" + hit.id);
          var texts = scene.linkText(hit.id).map(function (e) { return e.text; });
          if (hit.id === nav.selected || !texts.length) hideTip(); else showTip(ent[hit.id].name + ": " + texts.join(" "), p);
          return;
        }
        if (hit.kind === "node") { scene.setHover(hit.id); hideTip(); return; }
        scene.setHover(null); hideTip();
      }
      function showTip(t, p) {
        tip.textContent = t;
        tip.hidden = false;
        var r = host.getBoundingClientRect(), w = tip.offsetWidth, hgt = tip.offsetHeight;
        tip.style.transform = "translate(" + Math.min(Math.max(8, p.x + 14), r.width - w - 8) + "px," + Math.min(Math.max(56, p.y + 14), r.height - hgt - 8) + "px)";
      }
      function hideTip() { tip.hidden = true; }

      /* ---- filters, chips and search */
      function toggleFilters(open) { filtersBox.hidden = !open; filtersBtn.setAttribute("aria-expanded", open ? "true" : "false"); }
      filtersBtn.addEventListener("click", function () { toggleFilters(filtersBox.hidden); });
      filtersBox.addEventListener("change", function (ev) {
        var i = ev.target;
        if (i.dataset.fsector) filters.sectors[i.checked ? "add" : "delete"](i.dataset.fsector);
        if (i.dataset.frank) filters.ranks[i.checked ? "add" : "delete"](i.dataset.frank);
        scene.setFilters(filters);
        keysDirty = true;
      });
      [].forEach.call(document.querySelectorAll(".toggles input[data-group]"), function (i) {
        i.addEventListener("change", function () { filters.groups[i.dataset.group] = i.checked; scene.setFilters(filters); });
      });
      [].forEach.call(document.querySelectorAll(".chip[data-sector]"), function (c) {
        c.addEventListener("click", function () { if (inMap()) goSector(c.dataset.sector); });
      });
      var byName = {};
      companies.forEach(function (k) { byName[ent[k].name.toLowerCase()] = k; });
      var search = document.getElementById("atlas-search"), lastQ = "", lastAt = 0;
      function runSearch() {
        if (!inMap()) return;
        var q = search.value.trim().toLowerCase();
        // Enter and the change event both fire for one search
        if (!q || (q === lastQ && performance.now() - lastAt < 400)) return;
        lastQ = q; lastAt = performance.now();
        var k = byName[q] || byName[Object.keys(byName).filter(function (n) { return n.indexOf(q) > -1; }).sort()[0]];
        if (k) goCompany(k); else where.textContent = "No company matches “" + search.value.trim() + "”";
      }
      search.addEventListener("change", runSearch);
      search.addEventListener("keydown", function (e) { if (e.key === "Enter") runSearch(); });
      var names = document.getElementById("atlas-names");
      companies.forEach(function (k) {
        if (ent[k].home) return;
        var o = document.createElement("option");
        o.value = ent[k].name; o.setAttribute("data-backer", "");
        names.appendChild(o);
      });

      /* ---- the minimap */
      var mctx = mini.getContext("2d"), miniKey = "";
      function miniFrame() {
        var b = data.map.bounds, w = mini.clientWidth, hh = mini.clientHeight;
        var s = Math.min(w / (b[2] - b[0]), hh / (b[3] - b[1]));
        return { s: s, ox: (w - s * (b[2] - b[0])) / 2 - s * b[0], oy: (hh - s * (b[3] - b[1])) / 2 - s * b[1], w: w, h: hh };
      }
      var MINI_COLOR = { silicon: "#A6DB8C", infra: "#E9B47E", cloud: "#84D2E3", models: "#BCA6F4", software: "#93B2F6",
                         security: "#EDA3DA", internet: "#F4A9A0", devices: "#E6DB8C", fintech: "#8EDCC4", backers: "#C9D2DF" };
      function drawMini(force) {
        var cam = scene.cam(), v = scene.view(), key = [cam.x | 0, cam.y | 0, cam.k.toFixed(4), v.w, v.h, nav.sector].join();
        if (!force && key === miniKey) return;
        miniKey = key;
        var dpr = window.devicePixelRatio || 1, f = miniFrame();
        if (!f.w) return;
        if (mini.width !== Math.round(f.w * dpr) || mini.height !== Math.round(f.h * dpr)) { mini.width = Math.round(f.w * dpr); mini.height = Math.round(f.h * dpr); }
        mctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        mctx.clearRect(0, 0, f.w, f.h);
        Object.keys(data.map.sectors).forEach(function (sid) {
          var t = data.map.sectors[sid];
          mctx.globalAlpha = filters.sectors.has(sid) ? (sid === nav.sector ? 0.95 : 0.6) : 0.15;
          mctx.fillStyle = MINI_COLOR[sid];
          mctx.beginPath(); mctx.arc(f.ox + f.s * t.x, f.oy + f.s * t.y, Math.max(2.5, f.s * t.r * 0.8), 0, 6.2832); mctx.fill();
        });
        mctx.globalAlpha = 1;
        mctx.strokeStyle = "#E2E9F3"; mctx.lineWidth = 1.2;
        var vw = v.w / cam.k, vh = v.h / cam.k;
        mctx.strokeRect(f.ox + f.s * (cam.x - vw / 2), f.oy + f.s * (cam.y - vh / 2), f.s * vw, f.s * vh);
      }
      frameHooks.push(function () { drawMini(false); });
      mini.addEventListener("click", function (ev) {
        dismissHint();
        var f = miniFrame(), r = mini.getBoundingClientRect();
        var wx = (ev.clientX - r.left - f.ox) / f.s, wy = (ev.clientY - r.top - f.oy) / f.s, inside = null;
        Object.keys(data.map.sectors).forEach(function (sid) {
          var t = data.map.sectors[sid];
          if (Math.hypot(wx - t.x, wy - t.y) < t.r) inside = sid;
        });
        if (inside && nav.level !== "company") goSector(inside);
        else scene.fly({ x: wx, y: wy, k: scene.cam().k });
      });
      mini.addEventListener("keydown", function (ev) { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); goGalaxy(); } });

      /* ---- first visit */
      if (window.matchMedia("(pointer: coarse)").matches) hint.textContent = "Pinch to zoom \u00b7 drag to move \u00b7 tap a company";
      if (!store(HINT_KEY)) hint.hidden = false;
      root.addEventListener("keydown", dismissHint);

      /* ---- addresses */
      function route(hash, quiet) {
        var r = C.parseHash(hash, companies, sectorSet);
        if (r.company) goCompany(r.company);
        else if (r.sector) goSector(r.sector);
        else if (!quiet) goGalaxy();
      }
      window.addEventListener("hashchange", function () {
        var r = C.parseHash(location.hash, companies, sectorSet);
        if (r.view === "list") { setView("list", false); return; }
        if (r.view === "map") { if (!inMap()) setView("map", false); route(location.hash, true); }
      });
      scene.jump(scene.galaxyCam());
      sync();
      if (pendingRoute) route(pendingRoute, true);

      return {
        goCompany: goCompany, goSector: goSector, goGalaxy: goGalaxy, back: back, scene: scene,
        state: function () { return { level: nav.level, sector: nav.sector, selected: nav.selected, tab: nav.tab }; }
      };
    });
  }

  function dismissHint() {
    if (hint.hidden) return;
    hint.hidden = true;
    store(HINT_KEY, "1");
  }

  /* ------------------------------------------------------- start */
  var bar = document.querySelector(".atlas-bar");
  function barHeight() { if (bar) document.documentElement.style.setProperty("--atlas-bar", bar.offsetHeight + "px"); }
  if (bar && window.ResizeObserver) new ResizeObserver(barHeight).observe(bar);
  barHeight();

  var h0 = location.hash.replace("#", "");
  var wantsList = h0.indexOf("sector-") === 0 || /^c-[a-z0-9_]+-/.test(h0);
  var wantsMap = /^(c|s)-[a-z0-9_]+$/.test(h0);
  if (wantsMap) pendingRoute = location.hash;
  setView(wantsList ? "list" : wantsMap ? "map" : (store(VIEW_KEY) === "list" ? "list" : "map"), false);
  // for checks in the browser console and tests
  window.AtlasMap = { ready: function () { return loading; }, api: function () { return M; } };
})();
