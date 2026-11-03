/* Tech Atlas map: the WebGL scene, drawn with PixiJS.

   One camera moves over the galaxy. Far out, each sector is a labelled planet
   and sectors are joined by bundled lines. Closer in, the planets open into
   their companies. Selecting a company pulls it and its neighbours into a
   constellation in front of everything else. atlas-map.js turns input into
   calls on the object create() returns, and the arithmetic is in
   atlas-map-core.js. */
(function () {
  "use strict";
  var C = window.AtlasMapCore;

  var SECTOR_COLOR = { silicon: 0xA6DB8C, infra: 0xE9B47E, cloud: 0x84D2E3, models: 0xBCA6F4, software: 0x93B2F6,
                       security: 0xEDA3DA, internet: 0xF4A9A0, devices: 0xE6DB8C, fintech: 0x8EDCC4, backers: 0xC9D2DF };
  var LINE = { allies: 0x8FD0B0, rivals: 0xEE8B7C, backers: 0x8DB4F2 };
  var SPACE = 0x151C2A, SILVER = 0xE2E9F3, DIM = 0xA9B3C4;
  var SERIF = '"Cormorant Garamond", Georgia, serif';
  var SANS = 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif';
  var ZOOM_TAU = 90, GLIDE_TAU = 325, FOCUS_MS = 720, MAX_ZOOM = 14;
  var TIERS = [{ id: "end" }, { id: "platform" }, { id: "stack" }];
  var RANK_CODE = { starter: "starter", second_string: "second", practice_squad: "rookie" };

  function create(PIXI, data, host, hooks) {
    var app = new PIXI.Application();
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var size = host.getBoundingClientRect();
    return app.init({ width: Math.max(1, size.width), height: Math.max(1, size.height), backgroundAlpha: 0,
                      antialias: true, resolution: dpr, autoDensity: true, preference: "webgl" })
      .then(function () {
        app.canvas.setAttribute("aria-hidden", "true");
        host.appendChild(app.canvas);
        return build(PIXI, app, data, hooks, { w: Math.max(1, size.width), h: Math.max(1, size.height) });
      })
      .catch(function (err) {
        // a half-built scene is taken down, so a retry starts clean
        try { app.destroy(true, { children: true }); } catch (e) { /* nothing was built */ }
        throw err;
      });
  }

  function build(PIXI, app, data, hooks, view) {
    var lay = data.map, ent = data.entities;
    var reduced = hooks.reduced;
    var names = {};
    Object.keys(lay.sectors).forEach(function (sid) { names[sid] = lay.sectors[sid].name; });

    /* ---------------------------------------------------- textures */
    function glowTexture() {
      var c = document.createElement("canvas"), x = c.getContext("2d");
      c.width = c.height = 128;
      var g = x.createRadialGradient(64, 64, 0, 64, 64, 64);
      g.addColorStop(0, "rgba(255,255,255,1)"); g.addColorStop(0.35, "rgba(255,255,255,.35)"); g.addColorStop(1, "rgba(255,255,255,0)");
      x.fillStyle = g; x.fillRect(0, 0, 128, 128);
      return PIXI.Texture.from(c);
    }
    function starTile(n, seed, size, alpha) {
      var c = document.createElement("canvas"), x = c.getContext("2d");
      c.width = c.height = 512;
      C.stars(n, seed).forEach(function (s) {
        x.globalAlpha = alpha * (0.45 + s.a * 0.55);
        x.fillStyle = s.m > 0.86 ? "#C9DBFF" : "#EEF2F8";
        x.beginPath(); x.arc(s.x * 512, s.y * 512, size * (0.55 + s.m * 0.7), 0, 6.2832); x.fill();
      });
      return PIXI.Texture.from(c);
    }
    var GLOW = glowTexture();

    /* ------------------------------------------------------ layers */
    var bg = new PIXI.Container(), under = new PIXI.Container(), rig = new PIXI.Container(), world = new PIXI.Container(), overlay = new PIXI.Container();
    // bundled lines run beneath the planets, everything else that is drawn on screen sits above them
    app.stage.addChild(bg, under, rig, overlay);
    rig.addChild(world);
    var STAR_LAYERS = [{ n: 150, seed: 11, size: 0.8, alpha: 0.42, f: 0.025 },
                       { n: 70, seed: 23, size: 1.15, alpha: 0.6, f: 0.07 },
                       { n: 26, seed: 37, size: 1.6, alpha: 0.8, f: 0.16 }].map(function (l) {
      var t = new PIXI.TilingSprite({ texture: starTile(l.n, l.seed, l.size, l.alpha), width: view.w, height: view.h });
      bg.addChild(t);
      return { sprite: t, f: l.f };
    });
    var bundleG = new PIXI.Graphics(), hoverG = new PIXI.Graphics(), focusLayer = new PIXI.Container(), labelLayer = new PIXI.Container();
    var focusLines = new PIXI.Graphics(), focusDots = new PIXI.Graphics();
    focusLayer.addChild(focusLines, focusDots);
    under.addChild(bundleG);
    overlay.addChild(hoverG, focusLayer, labelLayer);

    /* --------------------------------------------- sectors (planets) */
    function outlinePoints(d) {
      return d.replace(/[MZ]/g, "").trim().split(/\s*L\s*/).reduce(function (a, p) {
        var xy = p.trim().split(/\s+/); a.push(+xy[0], +xy[1]); return a;
      }, []);
    }
    function dashedCircle(g, r, dash, gap) {
      var n = Math.max(6, Math.floor(2 * Math.PI * r / (dash + gap)));
      for (var i = 0; i < n; i++) {
        var a = i * 2 * Math.PI / n, b = a + (dash / (dash + gap)) * 2 * Math.PI / n;
        g.moveTo(r * Math.cos(a), r * Math.sin(a)); g.arc(0, 0, r, a, b);
      }
    }
    var sectors = {}, sectorIds = Object.keys(lay.sectors);
    sectorIds.forEach(function (sid, i) {
      var t = lay.sectors[sid], color = SECTOR_COLOR[sid] || SILVER;
      var sc = new PIXI.Container();
      var glow = new PIXI.Sprite(GLOW);
      glow.anchor.set(0.5); glow.tint = color; glow.width = glow.height = t.r * 2.5; glow.alpha = 0.32;
      var pts = outlinePoints(t.outline), pts2 = outlinePoints(t.outline2);
      var disc = new PIXI.Graphics().poly(pts).fill({ color: color, alpha: 0.11 });
      var rim = new PIXI.Graphics().poly(pts).stroke({ width: 1.4, color: color, alpha: 0.75, pixelLine: false })
        .poly(pts2).stroke({ width: 0.8, color: color, alpha: 0.3 });
      var bands = new PIXI.Graphics();
      t.bands.forEach(function (b, j) {
        var steps = 18, poly = [];
        for (var s = 0; s <= steps; s++) { var a = b.a0 + (b.a1 - b.a0) * s / steps; poly.push(t.outer * Math.cos(a), t.outer * Math.sin(a)); }
        for (s = steps; s >= 0; s--) { a = b.a0 + (b.a1 - b.a0) * s / steps; poly.push(t.inner * Math.cos(a), t.inner * Math.sin(a)); }
        bands.poly(poly).fill({ color: color, alpha: j % 2 ? 0.035 : 0.075 });
      });
      t.rings.forEach(function (r) { dashedCircle(bands, r, 4, 9); });
      bands.stroke({ width: 1, color: color, alpha: 0.22 });
      var nodesC = new PIXI.Container();
      sc.addChild(glow, disc, bands, rim, nodesC);
      world.addChild(sc);
      // sectors sit at slightly different depths, so they slide against each other as the camera moves
      sectors[sid] = { id: sid, t: t, c: sc, glow: glow, disc: disc, bands: bands, rim: rim, nodes: nodesC, color: color,
                       depth: [-0.03, 0.02, -0.012, 0.034, -0.024, 0.012, 0.028, -0.034, 0.006, -0.018][i % 10] };
    });

    /* --------------------------------------------------- companies */
    var nodes = lay.cards.map(function (c, i) {
      var e = ent[c.company], home = e.home || "backers", color = SECTOR_COLOR[home] || SILVER;
      var r = c.main ? C.nodeRadius(e.ovr) : C.R_UNRATED + 1, rank = RANK_CODE[c.rank] || null;
      var s = sectors[c.sector], t = s.t;
      var nc = new PIXI.Container();
      nc.position.set(c.x - t.x, c.y - t.y);
      var glow = new PIXI.Sprite(GLOW);
      glow.anchor.set(0.5); glow.tint = color; glow.width = glow.height = r * 5; glow.alpha = c.main ? 0.42 : 0;
      var g = new PIXI.Graphics();
      if (c.main) g.circle(0, 0, r).fill({ color: color });
      else g.circle(0, 0, r).fill({ color: SPACE }).stroke({ width: 1.2, color: color });
      var ring = new PIXI.Graphics();
      if (rank === "second") dashedCircle(ring, r + 3.5, 4, 3);
      else if (rank === "rookie") dashedCircle(ring, r + 3.5, 0.6, 3.2);
      else ring.circle(0, 0, r + 3.5);
      ring.stroke({ width: rank === "rookie" ? 2 : 1.4, color: color, alpha: 0.9 });
      nc.addChild(glow, g, ring);
      s.nodes.addChild(nc);
      return { i: i, id: c.company, sector: c.sector, row: c.row, rank: rank, main: c.main, x: c.x, y: c.y, r: r,
               home: home, color: color, c: nc, glow: glow, phase: i * 1.731, off: false };
    });
    var mainOf = {};
    nodes.forEach(function (n) { if (n.main) mainOf[n.id] = n; });

    /* ------------------------------------------------------ labels */
    function text(str, style) {
      var t = new PIXI.Text({ text: str, style: Object.assign({ fill: SILVER, stroke: { color: SPACE, width: 4, join: "round" } }, style) });
      t.visible = false;
      labelLayer.addChild(t);
      return t;
    }
    function splitName(name) {
      if (name.length < 15) return [name];
      var w = name.split(" "), best = 1, gap = Infinity;
      for (var i = 1; i < w.length; i++) {
        var d = Math.abs(w.slice(0, i).join(" ").length - w.slice(i).join(" ").length);
        if (d < gap) { gap = d; best = i; }
      }
      return [w.slice(0, best).join(" "), w.slice(best).join(" ")];
    }
    var topOf = {};
    nodes.forEach(function (n) {
      if (!n.main || ent[n.id].ovr == null) return;
      (topOf[n.home] = topOf[n.home] || []).push(n.id);
    });
    var labels = [];
    sectorIds.forEach(function (sid) {
      var s = sectors[sid], col = s.color, nm = names[sid];
      var count = nodes.filter(function (n) { return n.sector === sid && n.main; }).length;
      var top = (topOf[sid] || []).sort(function (a, b) { return ent[b].ovr - ent[a].ovr; }).slice(0, 3);
      var titles = [
        text(nm.toUpperCase(), { fontFamily: SERIF, fontSize: 17, fontWeight: "600", letterSpacing: 3, fill: col, align: "center" }),
        text(splitName(nm).join("\n").toUpperCase(), { fontFamily: SERIF, fontSize: 15, fontWeight: "600", letterSpacing: 2.4, fill: col, align: "center", lineHeight: 17 }),
        text(splitName(nm).join("\n"), { fontFamily: SERIF, fontSize: 14.5, fontWeight: "700", fill: col, align: "center", lineHeight: 15 }),
        text(splitName(nm).join("\n"), { fontFamily: SERIF, fontSize: 12.5, fontWeight: "700", fill: col, align: "center", lineHeight: 13 })
      ];
      labels.push({ kind: "title", sid: sid, texts: titles });
      var noun = sid === "backers" ? (count === 1 ? " firm" : " firms") : (count === 1 ? " company" : " companies");
      var stats = [
        text(count + noun + (top.length ? "\n" + top.map(function (id) { return ent[id].name + "  " + ent[id].ovr; }).join("\n") : ""),
             { fontFamily: SANS, fontSize: 12, fill: DIM, align: "center", lineHeight: 16 }),
        text(count + noun, { fontFamily: SANS, fontSize: 12, fill: DIM, align: "center" })
      ];
      labels.push({ kind: "stats", sid: sid, texts: stats });
      s.t.rows.forEach(function (r, j) {
        var b = s.t.bands[j], mid = b ? (b.a0 + b.a1) / 2 : 0;
        labels.push({ kind: "band", sid: sid, wx: r.x, wy: r.y, anchor: r.anchor, mid: mid,
                      texts: [text(r.name, { fontFamily: SANS, fontSize: 11.5, fontStyle: "italic", fill: col, stroke: { color: SPACE, width: 3 } })] });
      });
    });
    nodes.forEach(function (n) {
      labels.push({ kind: "node", n: n, texts: [text(ent[n.id].name, { fontFamily: SANS, fontSize: 12.5, fill: n.main ? SILVER : DIM,
        fontStyle: n.main ? "normal" : "italic", stroke: { color: SPACE, width: 3.5, join: "round" } })] });
    });

    /* ------------------------------------------------------ camera */
    var cam = { x: 0, y: 0, k: 1 }, kGal = 1, zoomTo = null, vel = null, fl = null, tilt = 0;
    var state = { detail: 0, focus: null, hover: null, keyFocus: null, sector: null, filters: null, t: 0 };
    function limits() { return { min: kGal, max: kGal * MAX_ZOOM }; }
    function galaxyCam() { return C.fitCam(lay.bounds, view, 24, { min: 1e-4, max: 1e4 }); }
    function sectorCam(sid) {
      var t = lay.sectors[sid];
      return C.fitCam([t.x - t.r, t.y - t.r, t.x + t.r, t.y + t.r], view, 28, limits());
    }
    function companyCam(id) {
      var n = mainOf[id];
      return { x: n.x, y: n.y, k: Math.min(sectorCam(n.sector).k * 1.4, kGal * MAX_ZOOM) };
    }
    function clampNow() {
      var m = 0.5 * Math.max(view.w, view.h) / cam.k;
      cam = C.clampCam(cam, [lay.bounds[0] + m * 0.2, lay.bounds[1] + m * 0.2, lay.bounds[2] - m * 0.2, lay.bounds[3] - m * 0.2], limits());
      var b = lay.bounds;
      if (view.w / cam.k >= b[2] - b[0]) cam.x = (b[0] + b[2]) / 2;
      if (view.h / cam.k >= b[3] - b[1]) cam.y = (b[1] + b[3]) / 2;
    }
    function fly(target, done) {
      zoomTo = null; vel = null;
      var f = C.flight(cam, target, view), ms = C.flightMs(f.duration, reduced());
      if (!ms) { cam = { x: target.x, y: target.y, k: target.k }; fl = null; tilt = 0; if (done) done(); return; }
      var far = Math.min(1, Math.hypot(target.x - cam.x, target.y - cam.y) * cam.k / view.w);
      fl = { f: f, t0: performance.now(), ms: ms, to: target, done: done, tilt: 0.014 * far };
    }
    function jump(target) { fl = null; zoomTo = null; vel = null; cam = { x: target.x, y: target.y, k: target.k }; clampNow(); }

    /* -------------------------------------------------- per frame */
    var last = performance.now();
    app.ticker.add(function () {
      var now = performance.now(), dt = Math.min(64, now - last);
      last = now; state.t = now;
      step(now, dt);
      render(now);
      if (hooks.onFrame) hooks.onFrame(cam, view);
    });

    function step(now, dt) {
      if (fl) {
        var p = Math.min(1, (now - fl.t0) / fl.ms);
        cam = p >= 1 ? { x: fl.to.x, y: fl.to.y, k: fl.to.k } : fl.f.at(C.easeInOut(p));
        tilt = Math.sin(Math.PI * p) * fl.tilt;
        if (p >= 1) { var d = fl.done; fl = null; tilt = 0; if (d) d(); }
        return;
      }
      if (zoomTo) {
        var k = Math.exp(C.approach(Math.log(cam.k), Math.log(zoomTo.k), dt, ZOOM_TAU));
        if (Math.abs(Math.log(k / zoomTo.k)) < 0.002) k = zoomTo.k;
        cam = { x: zoomTo.w.x - (zoomTo.s.x - view.w / 2) / k, y: zoomTo.w.y - (zoomTo.s.y - view.h / 2) / k, k: k };
        if (k === zoomTo.k) zoomTo = null;
        clampNow();
      }
      if (vel) {
        cam = { x: cam.x - vel.x * dt / cam.k, y: cam.y - vel.y * dt / cam.k, k: cam.k };
        vel = C.glide(vel, dt, GLIDE_TAU);
        clampNow();
      }
    }

    function render(now) {
      var still = reduced();
      rig.position.set(view.w / 2, view.h / 2);
      rig.rotation = still ? 0 : tilt;
      world.scale.set(cam.k);
      world.position.set(-cam.x * cam.k, -cam.y * cam.k);
      var z = cam.k / kGal, d = C.detail(z);
      state.detail = d;
      STAR_LAYERS.forEach(function (l) {
        var f = still ? 0 : l.f;
        l.sprite.tilePosition.set(-cam.x * cam.k * f, -cam.y * cam.k * f);
        var sc = still ? 1 : Math.pow(z, l.f * 1.4);
        l.sprite.tileScale.set(sc);
      });
      sectorIds.forEach(function (sid) {
        var s = sectors[sid], t = s.t, off = state.filters && !state.filters.sectors.has(sid);
        var dep = still ? 0 : s.depth;
        s.c.position.set(t.x + (cam.x - t.x) * dep, t.y + (cam.y - t.y) * dep);
        s.c.alpha = off ? 0.18 : 1;
        s.disc.alpha = 1 - 0.55 * d;
        s.glow.alpha = 0.32 * (1 - 0.45 * d);
        s.bands.alpha = d;
        s.nodes.alpha = d;
        s.nodes.visible = d > 0.01;
      });
      var tsec = now / 1000;
      nodes.forEach(function (n) {
        var dx = 0, dy = 0;
        if (!still && d > 0.01) { dx = Math.sin(tsec * 0.6 + n.phase) * 1.6; dy = Math.cos(tsec * 0.47 + n.phase * 1.3) * 1.6; }
        n.c.position.set(n.x - lay.sectors[n.sector].x + dx, n.y - lay.sectors[n.sector].y + dy);
        n.c.alpha = n.off ? 0.08 : 1;
        var hot = n.main && (n.id === state.hover || n.id === state.keyFocus);
        n.glow.alpha = n.main ? (hot ? 0.95 : 0.42) : 0;
        n.glow.scale.set((hot ? 7.5 : 5) * n.r / 128);
      });
      // the galaxy recedes behind a constellation
      var fp = focusProgress(now);
      rig.scale.set(1 - 0.07 * fp);
      world.alpha = 1 - 0.8 * fp;
      bg.alpha = 1 - 0.35 * fp;
      drawBundles(d, fp);
      drawHover(d, fp);
      drawFocus(now);
      placeLabels(d, fp);
    }

    /* ---------------------------------------------- screen positions */
    var tmp = new PIXI.Point();
    function screenOfNode(n) {
      tmp.set(n.c.position.x, n.c.position.y);
      return sectors[n.sector].c.toGlobal(tmp);
    }
    function screenOfSector(sid) { tmp.set(0, 0); return sectors[sid].c.toGlobal(tmp); }
    function screenScale() { return cam.k * rig.scale.x; }

    /* ------------------------------------------------ bundled lines */
    var bundleList = [];
    function rebuildBundles() {
      var homeOf = {};
      Object.keys(ent).forEach(function (k) { if (ent[k].home || mainOf[k]) homeOf[k] = ent[k].home || "backers"; });
      bundleList = C.bundles(enabledEdges(), homeOf);
    }
    function bundleCurve(b) {
      var a = screenOfSector(b.a), c = screenOfSector(b.b), k = screenScale();
      return C.arc(a, c, lay.sectors[b.a].r * k * 0.82, lay.sectors[b.b].r * k * 0.82, 0.12, 4, b.a, b.b);
    }
    function drawBundles(d, fp) {
      bundleG.clear();
      var a = (1 - d) * (1 - fp);
      if (a < 0.02) return;
      bundleList.forEach(function (b) {
        var c = bundleCurve(b), hot = state.hover === "bundle:" + b.a + "|" + b.b;
        bundleG.moveTo(c.start.x, c.start.y).quadraticCurveTo(c.ctrl.x, c.ctrl.y, c.end.x, c.end.y)
          .stroke({ width: 1.2 + 1.3 * Math.sqrt(b.count), color: hot ? 0xFFFFFF : SILVER, alpha: a * (hot ? 0.75 : 0.28), cap: "round" });
      });
    }

    /* ----------------------------------------- hover lines (sector view) */
    function enabledEdges() {
      var g = state.filters ? state.filters.groups : null;
      return data.edges.filter(function (e) { return !g || g[e.group]; });
    }
    function edgesOf(id) {
      return enabledEdges().filter(function (e) { return (e.a === id || e.b === id) && mainOf[e.a === id ? e.b : e.a]; });
    }
    function strokeLine(g, a, b, group, width, alpha) {
      if (group === "rivals") {
        var len = Math.hypot(b.x - a.x, b.y - a.y), n = Math.max(1, Math.floor(len / 11));
        for (var i = 0; i < n; i++) {
          var t0 = i / n, t1 = Math.min(1, t0 + 0.6 / n);
          g.moveTo(a.x + (b.x - a.x) * t0, a.y + (b.y - a.y) * t0).lineTo(a.x + (b.x - a.x) * t1, a.y + (b.y - a.y) * t1);
        }
      } else g.moveTo(a.x, a.y).lineTo(b.x, b.y);
      g.stroke({ width: width, color: LINE[group], alpha: alpha, cap: "round" });
    }
    function drawHover(d, fp) {
      hoverG.clear();
      var id = state.hover && state.hover.indexOf("bundle:") !== 0 ? state.hover : state.keyFocus;
      if (!id || !mainOf[id] || d < 0.5 || fp > 0) return;
      var a = screenOfNode(mainOf[id]), k = screenScale();
      edgesOf(id).forEach(function (e) {
        var o = mainOf[e.a === id ? e.b : e.a], b = screenOfNode(o);
        var c = C.arc(a, b, mainOf[id].r * k + 4, o.r * k + 4, 0.14, 2);
        var pts = [c.start];
        for (var s = 1; s <= 12; s++) pts.push(C.onCurve(c, s / 12));
        for (s = 0; s < pts.length - 1; s++) strokeLine(hoverG, pts[s], pts[s + 1], e.group, 1.6, 0.8 * d);
      });
    }

    /* ---------------------------------------------- the constellation */
    var focus = null;   // {id, t0, proxies: {id: proxy}, links: [...]}
    function focusProgress(now) {
      if (!focus) return 0;
      if (reduced()) return focus.leaving ? 0 : 1;
      var p = C.easeInOut(Math.min(1, (now - focus.t0) / FOCUS_MS));
      return focus.leaving ? 1 - p : p;
    }
    function compact() { return Math.min(view.w, view.h) < 520; }
    function makeProxy(id, centre) {
      var e = ent[id], home = e.home || "backers", color = SECTOR_COLOR[home] || SILVER, small = compact();
      var r = centre ? (small ? 25 : 32) : (small ? 16 : 21);
      var c = new PIXI.Container();
      var glow = new PIXI.Sprite(GLOW);
      glow.anchor.set(0.5); glow.tint = color; glow.width = glow.height = r * 5; glow.alpha = centre ? 0.7 : 0.4;
      var disc = new PIXI.Graphics().circle(0, 0, r).fill({ color: color }).circle(0, 0, r + 4).stroke({ width: 1.5, color: color, alpha: 0.7 });
      var ini = new PIXI.Text({ text: C.initials(e.name), style: { fontFamily: SANS, fontSize: centre ? (small ? 15 : 18) : (small ? 11 : 13), fontWeight: "700", fill: SPACE } });
      ini.anchor.set(0.5);
      c.addChild(glow, disc, ini);
      focusLayer.addChild(c);
      var name = text(e.name, { fontFamily: SANS, fontSize: centre ? (small ? 13.5 : 15) : (small ? 11.5 : 12.5), fontWeight: centre ? "600" : "400" });
      var score = e.ovr != null ? text(String(e.ovr), { fontFamily: SANS, fontSize: small ? 11 : 12, fontWeight: "700", fill: tierColor(e.ovr) }) : null;
      return { id: id, c: c, r: r, centre: centre, name: name, score: score, pos: null, from: null, to: null, alpha: 0 };
    }
    function tierColor(ovr) {
      return ovr >= 95 ? 0xF2D98D : ovr >= 90 ? 0xD4B6FF : ovr >= 85 ? 0x94CFF7 : ovr >= 80 ? 0xE2E9F3 : 0xB7C0CE;
    }
    function dropProxy(p) {
      focusLayer.removeChild(p.c); p.c.destroy({ children: true });
      [p.name, p.score].forEach(function (t) { if (t) { labelLayer.removeChild(t); t.destroy(); } });
    }
    function sideOf(id, e) {
      if (e.group === "rivals") return "right";
      if (e.group === "backers") return e.a === id ? "bottom" : "top";
      return "left";
    }
    var SIDE_RANK = { top: 0, bottom: 1, right: 2, left: 3 };
    function constellation(id) {
      var groups = { left: [], right: [], top: [], bottom: [] }, links = {}, sideFor = {};
      edgesOf(id).forEach(function (e) {
        var other = e.a === id ? e.b : e.a;
        if (mainOf[other].off) return;
        var side = sideOf(id, e);
        (links[other] = links[other] || []).push(e);
        if (!sideFor[other] || SIDE_RANK[side] < SIDE_RANK[sideFor[other]]) sideFor[other] = side;
      });
      Object.keys(sideFor).sort(function (a, b) { return (ent[b].ovr || 0) - (ent[a].ovr || 0); })
        .forEach(function (o) { groups[sideFor[o]].push(o); });
      var small = compact(), radius = Math.max(140, Math.min(view.w, view.h) * 0.31), gap = 118;
      // a narrow screen gets one ellipse that fills the free map; a wide one gets arcs by side
      if (small) return { ring: C.ellipseRing(groups, Math.max(60, view.w / 2 - 58), Math.max(60, view.h / 2 - 66)), links: links, side: sideFor };
      var ring = C.focusRing(groups, radius, gap), ext = 1;
      Object.keys(ring).forEach(function (o) {
        ext = Math.max(ext, Math.abs(ring[o].x) / (view.w / 2 - 70), Math.abs(ring[o].y) / (view.h / 2 - 50));
      });
      Object.keys(ring).forEach(function (o) { ring[o] = { x: ring[o].x / ext, y: ring[o].y / ext }; });
      return { ring: ring, links: links, side: sideFor };
    }
    function homeScreen(id) {
      var n = mainOf[id], s = screenOfNode(n);
      return { x: s.x - view.w / 2, y: s.y - view.h / 2 };
    }
    function setFocus(id) {
      var now = performance.now(), old = focus && !focus.leaving ? focus.proxies : {}, keep = {};
      // a constellation still flying home is cleared before a new one forms
      if (focus && focus.leaving && id) {
        Object.keys(focus.proxies).forEach(function (k) { dropProxy(focus.proxies[k]); });
        (focus.leavers || []).forEach(dropProxy);
        focus = null;
      }
      if (!id) {
        if (!focus) return;
        Object.keys(focus.proxies).forEach(function (k) {
          var p = focus.proxies[k]; p.from = p.pos; p.to = null;
        });
        focus.leaving = true; focus.t0 = now;
        return;
      }
      var plan = constellation(id), ids = [id].concat(Object.keys(plan.ring));
      ids.forEach(function (k) {
        var p = old[k] || makeProxy(k, k === id);
        if (old[k] && p.centre !== (k === id)) { dropProxy(p); p = makeProxy(k, k === id); p.pos = old[k].pos; }
        p.from = p.pos || homeScreen(k);
        p.to = k === id ? { x: 0, y: 0 } : plan.ring[k];
        keep[k] = p;
      });
      // companies that are not in the new constellation go home
      var leaving = [];
      Object.keys(old).forEach(function (k) { if (!keep[k]) { old[k].from = old[k].pos; old[k].to = null; leaving.push(old[k]); } });
      if (focus && focus.leavers) focus.leavers.forEach(dropProxy);
      focus = { id: id, t0: now, proxies: keep, plan: plan, leavers: leaving, leaving: false };
    }
    function drawFocus(now) {
      focusLines.clear(); focusDots.clear();
      if (!focus) return;
      var raw = reduced() ? 1 : Math.min(1, (now - focus.t0) / FOCUS_MS), p = C.easeInOut(raw), cx = view.w / 2, cy = view.h / 2;
      function move(px) {
        var to = px.to || homeScreen(px.id), from = px.from || to;
        px.pos = { x: from.x + (to.x - from.x) * p, y: from.y + (to.y - from.y) * p };
        var pulse = px.centre && !reduced() && !focus.leaving ? 1 + 0.045 * Math.sin(now / 380) : 1;
        px.c.position.set(cx + px.pos.x, cy + px.pos.y);
        px.c.scale.set(pulse);
        px.alpha = px.to ? Math.min(1, 0.25 + p) : 1 - p;
        px.c.alpha = px.alpha;
      }
      Object.keys(focus.proxies).forEach(function (k) { move(focus.proxies[k]); });
      (focus.leavers || []).forEach(move);
      if (raw >= 1 && focus.leavers && focus.leavers.length) { focus.leavers.forEach(dropProxy); focus.leavers = []; }
      if (focus.leaving && raw >= 1) {
        Object.keys(focus.proxies).forEach(function (k) { dropProxy(focus.proxies[k]); });
        focus = null;
        return;
      }
      var centre = focus.proxies[focus.id], la = focus.leaving ? 1 - p : p;
      Object.keys(focus.plan.links).forEach(function (o) {
        var px = focus.proxies[o];
        if (!px || !px.pos) return;
        var a = { x: cx + centre.pos.x, y: cy + centre.pos.y }, b = { x: cx + px.pos.x, y: cy + px.pos.y };
        var dx = b.x - a.x, dy = b.y - a.y, len = Math.hypot(dx, dy) || 1, ux = dx / len, uy = dy / len;
        var s = { x: a.x + ux * (centre.r + 7), y: a.y + uy * (centre.r + 7) }, t = { x: b.x - ux * (px.r + 7), y: b.y - uy * (px.r + 7) };
        var hot = state.hover === "line:" + o || state.hover === "proxy:" + o || state.keyFocus === o;
        focus.plan.links[o].forEach(function (e, i) {
          var off = (i - (focus.plan.links[o].length - 1) / 2) * 5;
          var s2 = { x: s.x - uy * off, y: s.y + ux * off }, t2 = { x: t.x - uy * off, y: t.y + ux * off };
          strokeLine(focusLines, s2, t2, e.group, hot ? 2.6 : 1.8, la * (hot ? 1 : 0.85));
          if (e.group === "backers" && !reduced()) {
            var from = e.a === focus.id ? s2 : t2, to = e.a === focus.id ? t2 : s2;
            for (var q = 0; q < 3; q++) {
              var f = ((now / 1300) + q / 3) % 1;
              focusDots.circle(from.x + (to.x - from.x) * f, from.y + (to.y - from.y) * f, 2.4).fill({ color: LINE.backers, alpha: la });
            }
          }
          if (e.group === "backers" && reduced()) {
            var tip = e.a === focus.id ? t2 : s2, back = e.a === focus.id ? s2 : t2;
            var bx = tip.x - back.x, by = tip.y - back.y, bl = Math.hypot(bx, by) || 1;
            bx /= bl; by /= bl;
            focusDots.poly([tip.x, tip.y, tip.x - bx * 9 - by * 4.5, tip.y - by * 9 + bx * 4.5, tip.x - bx * 9 + by * 4.5, tip.y - by * 9 - bx * 4.5])
              .fill({ color: LINE.backers, alpha: la });
          }
        });
      });
    }

    /* ------------------------------------------------- label placing */
    var NODE_POS = [[0, 1], [1, 0], [-1, 0], [0, -1]];
    function nodeAlts(n, s, w, h, k) {
      var r = n.r * k + 4;
      return NODE_POS.map(function (p) {
        var x = p[0] === 0 ? s.x - w / 2 : p[0] > 0 ? s.x + r + 2 : s.x - r - 2 - w;
        var y = p[1] === 0 ? s.y - h / 2 : p[1] > 0 ? s.y + r : s.y - r - h;
        return { x: x, y: y, w: w, h: h };
      });
    }
    function placeLabels(d, fp) {
      var k = screenScale(), items = [], blocks = [], small = view.w < 600, ids = 0;
      var lview = { w: view.w, h: view.h, top: hooks.reserveTop || 0, bottom: hooks.reserveBottom || 0 };
      labels.forEach(function (l) { l.texts.forEach(function (t) { t.visible = false; }); l.pick = null; });
      if (fp < 1) {
        if (d > 0.35) nodes.forEach(function (n) {
          if (n.off) return;
          var s = screenOfNode(n), r = (n.r + 4) * k;
          if (s.x + r < 0 || s.y + r < 0 || s.x - r > view.w || s.y - r > view.h) return;
          blocks.push({ x: s.x - r, y: s.y - r, w: 2 * r, h: 2 * r });
        });
        labels.forEach(function (l, i) {
          var alts, p = 0, t0 = l.texts[0];
          if (l.kind === "title") {
            var c = screenOfSector(l.sid), R = lay.sectors[l.sid].r * k;
            if (c.x + R < 0 || c.x - R > view.w || c.y + R < 0 || c.y - R > view.h) return;
            var cy = d < 0.5 ? c.y - (fp ? 0 : 14) : c.y - R * 0.98;
            // each variant centred, then moved down or up inside the planet; on narrow screens the sentence-case ones first
            var order = small && d < 0.5 ? [2, 3, 0, 1] : [0, 1, 2, 3], shift = d < 0.5 ? Math.max(18, R * 0.55) : 0;
            alts = []; l.order = [];
            [[0, 0], [0, shift], [0, -shift], [-shift, 0], [shift, 0]].forEach(function (o, pass) {
              if (pass && !shift) return;
              order.forEach(function (v) {
                var tx = l.texts[v];
                alts.push({ x: c.x + o[0] - tx.width / 2, y: cy + o[1] - tx.height / 2, w: tx.width, h: tx.height });
                l.order.push(v);
              });
            });
            // shorter names place first, so a long name is the one that moves or wraps
            items.push({ id: i, p: 6000 - l.texts[order[0]].width, force: true, alts: alts });
            return;
          }
          if (l.kind === "stats") {
            if (d > 0.5) return;
            var cs = screenOfSector(l.sid);
            alts = l.texts.map(function (t) { return { x: cs.x - t.width / 2, y: cs.y + 6, w: t.width, h: t.height }; });
            items.push({ id: i, p: 3000, alts: alts });
            return;
          }
          if (l.kind === "band") {
            if (d < 0.6 || !state.filters || !state.filters.sectors.has(l.sid)) return;
            tmp.set(l.wx - lay.sectors[l.sid].x, l.wy - lay.sectors[l.sid].y);
            var sb = sectors[l.sid].c.toGlobal(tmp);
            var bx = l.anchor === "end" ? sb.x - t0.width : l.anchor === "middle" ? sb.x - t0.width / 2 : sb.x;
            items.push({ id: i, p: 300, avoid: true, alts: [{ x: bx, y: sb.y - t0.height / 2, w: t0.width, h: t0.height }] });
            return;
          }
          var n = l.n;
          if (d < 0.35 || n.off) return;
          var special = n.main && (n.id === state.hover || n.id === state.keyFocus);
          var sn = screenOfNode(n);
          if (sn.x < -40 || sn.y < -40 || sn.x > view.w + 40 || sn.y > view.h + 40) return;
          p = special ? 4000 : (n.main ? 100 : 0) + (ent[n.id].ovr || 30) + (n.sector === state.sector ? 60 : 0);
          items.push({ id: i, p: p, avoid: !special, force: special, alts: nodeAlts(n, sn, t0.width, t0.height, k) });
        });
      }
      var shown = C.collide(items, lview, 3, blocks), byId = {};
      items.forEach(function (x) { byId[x.id] = x; });
      shown.forEach(function (alt, i) {
        var l = labels[i], kind = l.kind, t = kind === "title" ? l.texts[l.order[alt]] : kind === "stats" ? l.texts[alt] : l.texts[0];
        var box = byId[i].alts[alt];
        t.visible = true;
        t.position.set(box.x, box.y);
        var fade = kind === "title" ? 1 : kind === "stats" ? (1 - d / 0.5) : Math.min(1, (d - 0.35) / 0.3);
        t.alpha = fade * (1 - fp);
        ids++;
      });
      if (focus) placeFocusLabels();
      state.labelsShown = ids;
    }
    function placeFocusLabels() {
      var cx = view.w / 2, cy = view.h / 2, all = [], items = [], blocks = [];
      Object.keys(focus.proxies).forEach(function (k) { all.push(focus.proxies[k]); });
      (focus.leavers || []).forEach(function (p) { all.push(p); });
      all.forEach(function (px) {
        px.name.visible = false;
        if (px.score) px.score.visible = false;
        if (!px.pos || px.alpha < 0.05) return;
        var x = cx + px.pos.x, y = cy + px.pos.y, r = px.r + 5;
        blocks.push({ x: x - r, y: y - r, w: 2 * r, h: 2 * r });
      });
      // a name and its OVR travel together, below, beside or above the disc, never over another disc
      all.forEach(function (px, i) {
        if (!px.pos || px.alpha < 0.05) return;
        var x = cx + px.pos.x, y = cy + px.pos.y, r = px.r + 6, h = px.name.height;
        var w = px.name.width + (px.score ? px.score.width + 5 : 0), out = px.pos.x >= 0 ? 1 : -1;
        var below = { x: x - w / 2, y: y + r, w: w, h: h }, above = { x: x - w / 2, y: y - r - h, w: w, h: h };
        var outward = { x: out > 0 ? x + r : x - r - w, y: y - h / 2, w: w, h: h };
        var inward = { x: out > 0 ? x - r - w : x + r, y: y - h / 2, w: w, h: h };
        var alts = px.centre ? [below, above, outward, inward] : px.pos.y < -10 ? [above, outward, below, inward] : [below, outward, above, inward];
        items.push({ id: i, p: px.centre ? 100 : 10 + (ent[px.id].ovr || 0) / 100, avoid: true, force: true, alts: alts });
      });
      var shown = C.collide(items, { w: view.w, h: view.h, top: hooks.reserveTop || 0, bottom: 0 }, 3, blocks);
      items.forEach(function (it) {
        var px = all[it.id], b = it.alts[shown.has(it.id) ? shown.get(it.id) : 0];
        px.name.position.set(b.x, b.y);
        px.name.visible = true; px.name.alpha = px.alpha;
        if (px.score) {
          px.score.position.set(b.x + px.name.width + 5, b.y + (px.name.height - px.score.height) / 2);
          px.score.visible = true; px.score.alpha = px.alpha;
        }
      });
    }

    /* ------------------------------------------------------ picking */
    function pick(s) {
      if (focus && !focus.leaving) {
        var cx = view.w / 2, cy = view.h / 2, best = null;
        Object.keys(focus.proxies).forEach(function (k) {
          var p = focus.proxies[k];
          if (p.pos && Math.hypot(s.x - cx - p.pos.x, s.y - cy - p.pos.y) <= p.r + 8) best = { kind: "proxy", id: k };
        });
        if (best) return best;
        var c = focus.proxies[focus.id];
        Object.keys(focus.plan.links).forEach(function (o) {
          var p = focus.proxies[o];
          if (!best && p && p.pos && distToSeg(s, { x: cx + c.pos.x, y: cy + c.pos.y }, { x: cx + p.pos.x, y: cy + p.pos.y }) < 9) best = { kind: "line", id: o };
        });
        return best || { kind: "focus-bg" };
      }
      var k = screenScale(), d = state.detail, hit = null, bestD = Infinity;
      if (d > 0.35) nodes.forEach(function (n) {
        if (n.off) return;
        var sn = screenOfNode(n), dd = Math.hypot(sn.x - s.x, sn.y - s.y);
        if (dd <= Math.max(n.r * k + 6, 12) && dd < bestD) { bestD = dd; hit = { kind: "node", id: n.id, main: n.main, sector: n.sector }; }
      });
      if (hit) return hit;
      if (d < 0.6) bundleList.forEach(function (b) {
        if (hit) return;
        var c = bundleCurve(b);
        for (var t = 0; t <= 1; t += 1 / 24) {
          var q = C.onCurve(c, t);
          if (Math.hypot(q.x - s.x, q.y - s.y) < 8) { hit = { kind: "bundle", id: b.a + "|" + b.b, text: C.bundleText(b, names) }; break; }
        }
      });
      if (hit) return hit;
      sectorIds.forEach(function (sid) {
        var c = screenOfSector(sid), dd = Math.hypot(c.x - s.x, c.y - s.y);
        if (dd <= lay.sectors[sid].r * k * 0.95 && dd < bestD) { bestD = dd; hit = { kind: "sector", id: sid }; }
      });
      return hit;
    }
    function distToSeg(p, a, b) {
      var dx = b.x - a.x, dy = b.y - a.y, l2 = dx * dx + dy * dy || 1;
      var t = Math.max(0, Math.min(1, ((p.x - a.x) * dx + (p.y - a.y) * dy) / l2));
      return Math.hypot(p.x - a.x - t * dx, p.y - a.y - t * dy);
    }

    /* ------------------------------------------- keyboard targets */
    function targets(level, sector) {
      if (focus && !focus.leaving) {
        var cx = view.w / 2, cy = view.h / 2;
        return [focus.id].concat(Object.keys(focus.plan.ring)).map(function (k) {
          var p = focus.proxies[k];
          return p && p.pos ? { kind: "proxy", id: k, x: cx + p.pos.x, y: cy + p.pos.y, r: p.r + 6 } : null;
        }).filter(Boolean);
      }
      var k = screenScale();
      if (level === "galaxy") return sectorIds.map(function (sid) {
        var c = screenOfSector(sid);
        return { kind: "sector", id: sid, x: c.x, y: c.y, r: Math.min(60, lay.sectors[sid].r * k * 0.5) };
      });
      return nodes.filter(function (n) { return n.main && n.sector === sector && !n.off; }).map(function (n) {
        var s = screenOfNode(n);
        return { kind: "node", id: n.id, x: s.x, y: s.y, r: Math.max(10, n.r * k + 5), wx: n.x, wy: n.y };
      });
    }

    /* --------------------------------------------------------- api */
    function resize(w, h) {
      view = { w: Math.max(1, w), h: Math.max(1, h) };
      app.renderer.resize(view.w, view.h);
      STAR_LAYERS.forEach(function (l) { l.sprite.width = view.w; l.sprite.height = view.h; });
      kGal = galaxyCam().k;
      clampNow();
    }
    function setFilters(f) {
      state.filters = f;
      nodes.forEach(function (n) { n.off = !f.sectors.has(n.sector) || !!(n.rank && !f.ranks.has(n.rank)); });
      rebuildBundles();
      if (focus && !focus.leaving) setFocus(focus.id);
    }
    resize(view.w, view.h);
    cam = galaxyCam();
    // the first constellation pays for building its text; do that once while nothing is moving
    setTimeout(function () {
      var first = Object.keys(mainOf)[0];
      if (!focus && first) { dropProxy(makeProxy(first, true)); dropProxy(makeProxy(first, false)); }
    }, 400);

    return {
      view: function () { return view; },
      cam: function () { return cam; },
      kGal: function () { return kGal; },
      detail: function () { return state.detail; },
      galaxyCam: galaxyCam, sectorCam: sectorCam, companyCam: companyCam,
      fly: fly, jump: jump, resize: resize, pick: pick, targets: targets, setFilters: setFilters,
      focus: setFocus, focused: function () { return focus && !focus.leaving ? focus.id : null; },
      linkText: function (o) { return focus && focus.plan.links[o] ? focus.plan.links[o] : []; },
      setHover: function (h) { state.hover = h; },
      setKeyFocus: function (id) { state.keyFocus = id; },
      setSector: function (sid) { state.sector = sid; },
      busy: function () { return !!(fl || zoomTo || vel); },
      // the render loop stops while the map is out of sight
      pause: function () { app.ticker.stop(); },
      resume: function () { if (!app.ticker.started) { last = performance.now(); app.ticker.start(); } },
      labelsShown: function () { return state.labelsShown; },
      dragStart: function () { fl = null; zoomTo = null; vel = null; },
      dragBy: function (dx, dy) { cam = { x: cam.x - dx / cam.k, y: cam.y - dy / cam.k, k: cam.k }; clampNow(); },
      release: function (v) { vel = reduced() || !v ? null : v; },
      zoomBy: function (factor, s) {
        fl = null; vel = null;
        var base = zoomTo ? zoomTo.k : cam.k, L = limits();
        var k = Math.max(L.min, Math.min(L.max, base * factor));
        if (reduced()) { cam = C.zoomAround(cam, view, s, k); clampNow(); zoomTo = null; return; }
        zoomTo = { k: k, s: s, w: C.toWorld(cam, view, s) };
      },
      debug: function () { return { cam: cam, kGal: kGal, detail: state.detail, focus: focus && focus.id }; },
      // for the browser checks: which sector names show, and every visible label's box on screen
      visibleTitles: function () {
        return labels.filter(function (l) { return l.kind === "title" && l.texts.some(function (x) { return x.visible && x.alpha > 0.5; }); })
          .map(function (l) { return l.sid; });
      },
      labelBoxes: function () {
        return labelLayer.children.filter(function (x) { return x.visible && x.alpha > 0.3; })
          .map(function (x) { return { text: x.text, x: x.x, y: x.y, w: x.width, h: x.height }; });
      }
    };
  }

  window.AtlasMapScene = { create: create };
})();
