/* Tech Atlas map: the WebGL scene, drawn with PixiJS.

   One camera moves over the galaxy. Far out, each sector is a helmet drawn in
   its own colour over a nebula wash, and sectors are joined by bundled lines.
   Closer in, the sectors open into their companies, shown by their logos on
   the orbits of their rows. Selecting a company puts it in a spotlight: the
   camera fits it and its connections in the frame, and pulls any that are too
   far to read into a ring around it. A team can be lit up the same way.
   atlas-map.js turns input into calls on the object create() returns, the
   arithmetic is in atlas-map-core.js and the textures in atlas-map-art.js. */
(function () {
  "use strict";
  var C = window.AtlasMapCore, ART = window.AtlasMapArt;

  var SECTOR_COLOR = { silicon: 0xA6DB8C, infra: 0xE9B47E, cloud: 0x84D2E3, models: 0xBCA6F4, software: 0x93B2F6,
                       security: 0xEDA3DA, internet: 0xF4A9A0, devices: 0xE6DB8C, fintech: 0x8EDCC4, backers: 0xC9D2DF };
  var LINE = { allies: 0x8FD0B0, rivals: 0xEE8B7C, backers: 0x8DB4F2 };
  var SPACE = 0x151C2A, SILVER = 0xE2E9F3, DIM = 0xC3CCDA;
  var SERIF = '"Cormorant Garamond", Georgia, serif';
  var SANS = 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif';
  // a logo badge never shrinks below a readable size on screen, nor grows past a tidy one
  var BADGE_MIN_PX = 12, BADGE_MAX_PX = 24;
  var ZOOM_TAU = 90, GLIDE_TAU = 325, FOCUS_MS = 760, TEAM_MS = 600, MAX_ZOOM = 14;
  // what a neighbour is to the company in the spotlight, by kind and by which end it is
  var KIND_WORD = { supply: ["supplier", "customer"], license: ["licensee", "licensor"], dependency: ["depends on it", "relied on"],
                    ownership: ["owner", "owned"], investment: ["backer", "backed"], alliance: ["ally", "ally"], rivalry: ["rival", "rival"] };
  var TIERS = [{ id: "end" }, { id: "platform" }, { id: "stack" }];
  var RANK_CODE = { starter: "starter", second_string: "second", practice_squad: "rookie" };
  // at or below this canvas width the sectors stand in two columns of five
  var NARROW_W = 780;
  // the strips the galaxy's labels keep clear of: the controls above, the legend and first-visit hint below
  var GAL_SAFE = { wide: { top: 54, bottom: 92, side: 8 }, narrow: { top: 52, bottom: 46, side: 6 } };
  var HELMET_MAX = 1250;   // tallest a helmet may be, in map units
  var BLOCK_GAP = 3;   // between a sector's title and the lines under it

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
    // the soft dark ground behind a sector's label: solid in the middle, fading out at the edge
    function plateTexture() {
      var c = document.createElement("canvas"), x = c.getContext("2d");
      c.width = c.height = 128;
      var g = x.createRadialGradient(64, 64, 0, 64, 64, 64);
      g.addColorStop(0, "rgba(255,255,255,1)"); g.addColorStop(0.6, "rgba(255,255,255,.9)"); g.addColorStop(1, "rgba(255,255,255,0)");
      x.fillStyle = g; x.fillRect(0, 0, 128, 128);
      return PIXI.Texture.from(c);
    }
    var GLOW = glowTexture(), PLATE = plateTexture();

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
    var bundleG = new PIXI.Graphics(), hoverG = new PIXI.Graphics(), focusLayer = new PIXI.Container(), plateLayer = new PIXI.Container(), labelLayer = new PIXI.Container();
    var focusLines = new PIXI.Graphics(), focusDots = new PIXI.Graphics();
    focusLayer.addChild(focusLines, focusDots);
    var teamG = new PIXI.Graphics(), spotLight = new PIXI.Sprite(GLOW);
    spotLight.anchor.set(0.5); spotLight.visible = false;
    under.addChild(bundleG);
    overlay.addChild(spotLight, hoverG, teamG, focusLayer, plateLayer, labelLayer);
    var star = ART.shootingStar(PIXI, bg, reduced);

    /* --------------------------------------------- sectors (planets) */
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
      // a soft nebula wash in the sector colour, the helmet over it, then the orbits of its rows
      var glow = new PIXI.Sprite(GLOW);
      glow.anchor.set(0.5); glow.tint = color; glow.width = glow.height = t.r * 3.1; glow.alpha = 0.22;
      var helmet = new PIXI.Sprite(PIXI.Texture.EMPTY);
      helmet.anchor.set(0.5); helmet.tint = color; helmet.visible = false;
      var bands = new PIXI.Graphics();
      t.rings.forEach(function (r) { bands.circle(0, 0, r); });
      bands.stroke({ width: 1, color: color, alpha: 0.13 });
      t.bands.forEach(function (b) {
        bands.moveTo(t.outer * Math.cos(b.a0), t.outer * Math.sin(b.a0)).arc(0, 0, t.outer, b.a0, b.a1);
      });
      bands.stroke({ width: 1.4, color: color, alpha: 0.42 });
      t.bands.forEach(function (b) {
        var c = Math.cos(b.a0), sn = Math.sin(b.a0);
        bands.moveTo((t.outer - 9) * c, (t.outer - 9) * sn).lineTo((t.outer + 9) * c, (t.outer + 9) * sn);
      });
      bands.stroke({ width: 1, color: color, alpha: 0.35 });
      var nodesC = new PIXI.Container();
      sc.addChild(glow, helmet, bands, nodesC);
      world.addChild(sc);
      // sectors sit at slightly different depths, so they slide against each other as the camera moves
      sectors[sid] = { id: sid, t: t, c: sc, glow: glow, helmet: helmet, bands: bands, nodes: nodesC, color: color,
                       depth: [-0.03, 0.02, -0.012, 0.034, -0.024, 0.012, 0.028, -0.034, 0.006, -0.018][i % 10] };
    });
    ART.helmets(PIXI, sectorIds).then(function (all) {
      sectorIds.forEach(function (sid) {
        var s = sectors[sid], h = all[sid];
        if (!h) return;
        s.helmet.texture = h.texture;
        // the two largest sectors are capped so they do not run into the row above
        s.helmet.height = Math.min(s.t.r * 2.5, HELMET_MAX); s.helmet.width = s.helmet.height * h.ratio;
        s.helmet.visible = true;
      });
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
      var badge = new PIXI.Sprite(PIXI.Texture.EMPTY);
      badge.anchor.set(0.5); badge.visible = false;
      nc.addChild(glow, g, ring, badge);
      s.nodes.addChild(nc);
      return { i: i, id: c.company, sector: c.sector, row: c.row, rank: rank, main: c.main, x: c.x, y: c.y, r: r,
               home: home, color: color, c: nc, glow: glow, dot: g, badge: badge, phase: i * 1.731, off: false };
    });
    var mainOf = {};
    nodes.forEach(function (n) { if (n.main) mainOf[n.id] = n; });
    // logo badges load once, the first time companies come into view
    var badgeTex = {}, badgesAsked = false;
    function loadBadges() {
      if (badgesAsked) return;
      badgesAsked = true;
      Object.keys(mainOf).forEach(function (id) {
        var n = mainOf[id];
        ART.badge(PIXI, ent[id], n.color).then(function (b) {
          badgeTex[id] = b.texture;
          n.badge.texture = b.texture;
          n.badge.width = n.badge.height = 2 * (n.r + 2);
          n.hasBadge = true;
          if (focus && focus.proxies[id]) focus.proxies[id].setBadge(b.texture);
        });
      });
    }

    /* ------------------------------------------------------ labels */
    function text(str, style) {
      var t = new PIXI.Text({ text: str, style: Object.assign({ fill: SILVER, stroke: { color: SPACE, width: 4, join: "round" } }, style) });
      t.visible = false;
      labelLayer.addChild(t);
      return t;
    }
    var labels = [], statsOf = {}, plates = {};
    // every sector's title has one style: texts[0] for wide canvases, texts[1] for narrow ones
    // weight 700 draws the site's boldest face (600); WebKit left a canvas asking for 600 in the fallback font
    var TITLE_STYLE = [{ fontFamily: SERIF, fontSize: 16, fontWeight: "700", letterSpacing: 2.6, align: "center", lineHeight: 18 },
                       { fontFamily: SERIF, fontSize: 13, fontWeight: "700", letterSpacing: 1, align: "center", lineHeight: 14 }];
    var STATS_STYLE = [{ fontFamily: SANS, fontSize: 12, fill: DIM, align: "center", lineHeight: 16 },
                       { fontFamily: SANS, fontSize: 11, fill: DIM, align: "center", lineHeight: 13 }];
    sectorIds.forEach(function (sid) {
      var s = sectors[sid], col = s.color, nm = names[sid];
      var mains = nodes.filter(function (n) { return n.sector === sid && n.main; }).map(function (n) { return n.id; });
      var sum = C.sectorSummary(sid, mains, ent, data.edges);
      var title = C.splitTitle(nm).join("\n").toUpperCase();
      labels.push({ kind: "title", sid: sid, texts: TITLE_STYLE.map(function (st) { return text(title, Object.assign({ fill: col }, st)); }) });
      // full lines, then the count alone for a window too short to hold them, in each of the two sizes
      var full = [sum.count].concat(sum.top).join("\n"), stats = { kind: "stats", sid: sid, count: sum.count, top: sum.top,
        texts: [text(full, STATS_STYLE[0]), text(sum.count, STATS_STYLE[0]), text(full, STATS_STYLE[1]), text(sum.count, STATS_STYLE[1])] };
      labels.push(stats);
      statsOf[sid] = stats;
      var plate = new PIXI.Sprite(PLATE);
      plate.anchor.set(0.5); plate.tint = SPACE; plate.visible = false;
      plateLayer.addChild(plate);
      plates[sid] = plate;
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
    var cam = { x: 0, y: 0, k: 1 }, kGal = 1, zoomTo = null, vel = null, fl = null, tilt = 0, panLeft = null;
    var state = { detail: 0, focus: null, hover: null, keyFocus: null, sector: null, filters: null, t: 0 };
    // the part of the view the card and the controls cover, so the spotlight centres in what is left
    var inset = { right: 0, top: 0, bottom: 0 };
    var team = null;    // {id, members: Set, t0, leaving}
    function limits() { return { min: kGal, max: kGal * MAX_ZOOM }; }
    var narrow = false, galaxy = { x: 0, y: 0, k: 1 }, brief = false;
    // every sector's label size, with the top three lines or (brief) with the count alone
    function blockSizes(short) {
      var v = narrow ? 1 : 0, s = (narrow ? 2 : 0) + (short ? 1 : 0);
      return labels.filter(function (l) { return l.kind === "title"; }).map(function (l) {
        var st = statsOf[l.sid].texts[s], t = l.texts[v];
        return { sid: l.sid, w: Math.max(t.width, st.width), h: t.height + BLOCK_GAP + st.height };
      });
    }
    function fitBlocks(sizes) {
      var centres = sectorIds.map(function (sid) { return lay.sectors[sid]; });
      var most = { w: Math.max.apply(null, sizes.map(function (b) { return b.w; })), h: Math.max.apply(null, sizes.map(function (b) { return b.h; })) };
      return C.galaxyFit(centres, most, view, narrow ? GAL_SAFE.narrow : GAL_SAFE.wide);
    }
    function blocksFit(fit, sizes) {
      return C.blocksClear(sizes.map(function (b) {
        var c = C.toScreen(fit, view, lay.sectors[b.sid]);
        return { x: c.x - b.w / 2, y: c.y - b.h / 2, w: b.w, h: b.h };
      }), 3);
    }
    // the full labels if they all clear each other; if the window is too small, every sector drops to title and count together
    function measureGalaxy() {
      var full = blockSizes(false), fit = fitBlocks(full);
      brief = !blocksFit(fit, full);
      galaxy = brief ? fitBlocks(blockSizes(true)) : fit;
    }
    function galaxyCam() { return { x: galaxy.x, y: galaxy.y, k: galaxy.k }; }
    function sectorCam(sid) {
      var t = lay.sectors[sid];
      return C.fitCam([t.x - t.r, t.y - t.r, t.x + t.r, t.y + t.r], view, 28, limits());
    }
    function companyCam(id) { return spotPlan(id).cam; }
    function teamCam(members) {
      var xs = [], ys = [];
      members.forEach(function (id) { if (mainOf[id]) { xs.push(mainOf[id].x); ys.push(mainOf[id].y); } });
      if (!xs.length) return galaxyCam();
      var m = 160, box = [Math.min.apply(null, xs) - m, Math.min.apply(null, ys) - m, Math.max.apply(null, xs) + m, Math.max.apply(null, ys) + m];
      return C.fitCam(box, view, 40, limits());
    }
    function clampNow() {
      var m = 0.5 * Math.max(view.w, view.h) / cam.k;
      cam = C.clampCam(cam, [lay.bounds[0] + m * 0.2, lay.bounds[1] + m * 0.2, lay.bounds[2] - m * 0.2, lay.bounds[3] - m * 0.2], limits());
      var b = lay.bounds;
      // with the whole map in view it rests where the labels clear the controls
      if (view.w / cam.k >= b[2] - b[0]) cam.x = galaxy.x;
      if (view.h / cam.k >= b[3] - b[1]) cam.y = galaxy.y;
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
      star.step(now, view);
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
      // a trackpad swipe, eased in over a few frames so it moves at the display's rate
      if (panLeft) {
        var ps = C.panStep(panLeft, dt, reduced());
        cam = { x: cam.x - ps.x / cam.k, y: cam.y - ps.y / cam.k, k: cam.k };
        panLeft = Math.hypot(ps.left.x, ps.left.y) < 0.05 ? null : ps.left;
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
      if (d > 0.3) loadBadges();
      var fp = focusProgress(now), tp = teamProgress(now);
      // the helmet is clearest far out and fades back once its companies are in view; it stays faint enough to read a label over
      sectorIds.forEach(function (sid) {
        var s = sectors[sid], t = s.t, off = state.filters && !state.filters.sectors.has(sid);
        // the depth drift only starts once zoomed in, so the galaxy's rows of labels stay evenly spaced
        var dep = still ? 0 : s.depth * Math.min(1, Math.max(0, (z - 1) / 0.4));
        s.c.position.set(t.x + (cam.x - t.x) * dep, t.y + (cam.y - t.y) * dep);
        s.c.alpha = off ? 0.18 : 1;
        var quiet = (1 - 0.55 * fp) * (1 - 0.55 * tp);
        s.helmet.alpha = (0.26 - 0.16 * d) * quiet;
        s.glow.alpha = 0.22 * (1 - 0.35 * d) * quiet;
        s.bands.alpha = d * (1 - 0.6 * fp);
        s.nodes.alpha = Math.max(d, tp);
        s.nodes.visible = d > 0.01 || tp > 0.01;
      });
      var tsec = now / 1000, bd = Math.max(0, Math.min(1, (d - 0.45) / 0.3)), lit = focus && !focus.leaving ? focus.ids : null;
      nodes.forEach(function (n) {
        var dx = 0, dy = 0;
        if (!still && d > 0.01) { dx = Math.sin(tsec * 0.6 + n.phase) * 1.6; dy = Math.cos(tsec * 0.47 + n.phase * 1.3) * 1.6; }
        n.c.position.set(n.x - lay.sectors[n.sector].x + dx, n.y - lay.sectors[n.sector].y + dy);
        var a = n.off ? 0.08 : 1;
        // in the spotlight its proxy stands in for the node, and everyone else steps back
        if (lit) a *= lit[n.id] && n.main ? 1 - fp : 1 - 0.86 * fp;
        if (team) {
          var member = team.members.has(n.id) && n.main;
          a = a * (1 - tp) + tp * (member ? 1 : d > 0.35 ? 0.14 : 0);
        }
        n.c.alpha = a;
        n.sr = n.r * cam.k;
        // a team's members show their logos even far out
        var nb = team && n.main && team.members.has(n.id) ? Math.max(bd, tp) : bd;
        if (n.main && n.hasBadge) {
          n.badge.visible = nb > 0.01; n.badge.alpha = nb; n.dot.alpha = 1 - nb;
          var want = Math.max(BADGE_MIN_PX, Math.min(BADGE_MAX_PX, (n.r + 2) * cam.k * 1.5));
          n.badge.width = n.badge.height = 2 * want / cam.k;
          n.sr = n.sr + (want - n.sr) * nb;
        }
        var hot = n.main && (n.id === state.hover || n.id === state.keyFocus || (team && tp > 0 && team.members.has(n.id)));
        var pulse = team && hot && !still ? 1 + 0.18 * Math.sin(tsec * 2.4 + n.phase) : 1;
        n.glow.alpha = n.main ? (hot ? 0.95 : 0.42) : 0;
        n.glow.scale.set((hot ? 7.5 : 5) * pulse * n.r / 128);
      });
      bg.alpha = 1 - 0.25 * fp;
      drawBundles(d, Math.max(fp, tp));
      drawHover(d, fp);
      drawTeam(tp);
      drawFocus(now);
      drawSpot(fp);
      placeLabels(d, fp, tp);
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
        // faint at rest so the labels read first; a sector under the pointer or keyboard lights up its own lines
        var lit = hot || state.hover === "sector:" + b.a || state.hover === "sector:" + b.b || state.keyFocus === "sector:" + b.a || state.keyFocus === "sector:" + b.b;
        bundleG.moveTo(c.start.x, c.start.y).quadraticCurveTo(c.ctrl.x, c.ctrl.y, c.end.x, c.end.y)
          .stroke({ width: 0.8 + 0.9 * Math.sqrt(b.count), color: lit ? 0xFFFFFF : SILVER, alpha: a * (hot ? 0.7 : lit ? 0.5 : 0.07), cap: "round" });
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
      var id = state.hover && !/^(bundle|sector):/.test(state.hover) ? state.hover : state.keyFocus;
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

    /* ------------------------------------------------- the spotlight */
    var focus = null;   // {id, t0, proxies: {id: proxy}, plan, ids, leavers, leaving}
    function focusProgress(now) {
      if (!focus) return 0;
      if (reduced()) return focus.leaving ? 0 : 1;
      var p = C.easeInOut(Math.min(1, (now - focus.t0) / FOCUS_MS));
      return focus.leaving ? 1 - p : p;
    }
    function compact() { return Math.min(view.w, view.h) < 520; }
    function neighbours(id) {
      var pos = {}, links = {};
      edgesOf(id).forEach(function (e) {
        var o = e.a === id ? e.b : e.a;
        if (mainOf[o].off) return;
        pos[o] = { x: mainOf[o].x, y: mainOf[o].y };
        (links[o] = links[o] || []).push(e);
      });
      return { pos: pos, links: links };
    }
    /** The spotlight's camera, and which neighbours stay where they are and which join the ring. */
    function spotPlan(id) {
      var n = mainOf[id], nb = neighbours(id), sk = sectorCam(n.sector).k;
      var plan = C.spotlightPlan({ x: n.x, y: n.y }, nb.pos, view, {
        read: kGal * C.SHOW.sectorsFrom, max: Math.max(kGal * C.SHOW.sectorsFrom, sk * 2.2), pad: compact() ? 54 : 78,
        right: inset.right, top: inset.top, bottom: inset.bottom });
      plan.links = nb.links;
      return plan;
    }
    function makeProxy(id, centre) {
      var e = ent[id], home = e.home || "backers", color = SECTOR_COLOR[home] || SILVER, small = compact();
      var r = centre ? (small ? 25 : 31) : (small ? 15 : 19);
      var c = new PIXI.Container();
      var glow = new PIXI.Sprite(GLOW);
      glow.anchor.set(0.5); glow.tint = color; glow.width = glow.height = r * 5.2; glow.alpha = centre ? 0.75 : 0.4;
      var disc = new PIXI.Graphics().circle(0, 0, r).fill({ color: color }).circle(0, 0, r + 4).stroke({ width: 1.5, color: color, alpha: 0.75 });
      var ini = new PIXI.Text({ text: C.initials(e.name), style: { fontFamily: SANS, fontSize: centre ? (small ? 15 : 18) : (small ? 11 : 13), fontWeight: "700", fill: SPACE } });
      ini.anchor.set(0.5);
      var badge = new PIXI.Sprite(PIXI.Texture.EMPTY);
      badge.anchor.set(0.5); badge.visible = false;
      c.addChild(glow, disc, ini, badge);
      focusLayer.addChild(c);
      var name = text(e.name, { fontFamily: SANS, fontSize: centre ? (small ? 14 : 16) : (small ? 12 : 13), fontWeight: centre ? "600" : "500" });
      var score = e.ovr != null ? text(String(e.ovr), { fontFamily: SANS, fontSize: small ? 11.5 : 12.5, fontWeight: "700", fill: tierColor(e.ovr) }) : null;
      var px = { id: id, c: c, r: r, centre: centre, name: name, score: score, kind: null, pos: null, from: null, mode: null, ringAt: null,
                 alpha: 0, trail: [] };
      px.setBadge = function (tex) {
        badge.texture = tex; badge.width = badge.height = 2 * (r + 3); badge.visible = true; ini.visible = false;
        disc.clear().circle(0, 0, r + 4).stroke({ width: 1.5, color: color, alpha: 0.85 });
      };
      if (badgeTex[id]) px.setBadge(badgeTex[id]);
      return px;
    }
    function tierColor(ovr) {
      return ovr >= 95 ? 0xF2D98D : ovr >= 90 ? 0xD4B6FF : ovr >= 85 ? 0x94CFF7 : ovr >= 80 ? 0xE2E9F3 : 0xB7C0CE;
    }
    function dropProxy(p) {
      focusLayer.removeChild(p.c); p.c.destroy({ children: true });
      [p.name, p.score, p.kind].forEach(function (t) { if (t) { labelLayer.removeChild(t); t.destroy(); } });
    }
    function sideOf(id, e) {
      if (e.group === "rivals") return "right";
      if (e.group === "backers") return e.a === id ? "bottom" : "top";
      return "left";
    }
    function kindWord(id, e) {
      var w = KIND_WORD[e.type] || [e.type, e.type];
      return e.a === id ? w[1] : w[0];
    }
    var SIDE_RANK = { top: 0, bottom: 1, right: 2, left: 3 };
    /** Ring positions (relative to the company on screen) for the neighbours too far to show in place. */
    function ringLayout(id, plan) {
      var groups = { left: [], right: [], top: [], bottom: [] }, sideFor = {};
      plan.ring.forEach(function (o) {
        plan.links[o].forEach(function (e) {
          var side = sideOf(id, e);
          if (!sideFor[o] || SIDE_RANK[side] < SIDE_RANK[sideFor[o]]) sideFor[o] = side;
        });
      });
      Object.keys(sideFor).sort(function (a, b) { return (ent[b].ovr || 0) - (ent[a].ovr || 0); })
        .forEach(function (o) { groups[sideFor[o]].push(o); });
      var fw = view.w - inset.right, fh = view.h - inset.top - inset.bottom;
      if (compact()) return C.ellipseRing(groups, Math.max(60, fw / 2 - 52), Math.max(60, fh / 2 - 60));
      var ring = C.focusRing(groups, Math.max(140, Math.min(fw, fh) * 0.34), 112), ext = 1;
      Object.keys(ring).forEach(function (o) {
        ext = Math.max(ext, Math.abs(ring[o].x) / (fw / 2 - 74), Math.abs(ring[o].y) / (fh / 2 - 52));
      });
      Object.keys(ring).forEach(function (o) { ring[o] = { x: ring[o].x / ext, y: ring[o].y / ext }; });
      return ring;
    }
    function homeScreen(id) {
      var n = mainOf[id], s = screenOfNode(n);
      return { x: s.x - view.w / 2, y: s.y - view.h / 2 };
    }
    function setFocus(id) {
      var now = performance.now(), old = focus && !focus.leaving ? focus.proxies : {}, keep = {};
      if (focus && focus.leaving && id) {
        Object.keys(focus.proxies).forEach(function (k) { dropProxy(focus.proxies[k]); });
        (focus.leavers || []).forEach(dropProxy);
        focus = null;
      }
      if (!id) {
        if (!focus) return;
        Object.keys(focus.proxies).forEach(function (k) { var p = focus.proxies[k]; p.from = p.pos; p.mode = null; });
        focus.leaving = true; focus.t0 = now;
        return;
      }
      loadBadges();
      var plan = spotPlan(id), ring = ringLayout(id, plan), ids = {};
      [id].concat(plan.inPlace, plan.ring).forEach(function (k) {
        var p = old[k] || makeProxy(k, k === id);
        if (old[k] && p.centre !== (k === id)) { var pos = p.pos; dropProxy(p); p = makeProxy(k, k === id); p.pos = pos; }
        p.from = p.pos || homeScreen(k);
        p.mode = k === id ? "centre" : ring[k] ? "ring" : "place";
        p.ringAt = ring[k] || null;
        if (p.kind) { labelLayer.removeChild(p.kind); p.kind.destroy(); p.kind = null; }
        if (k !== id) {
          var e0 = plan.links[k][0];
          p.kind = text(plan.links[k].map(function (e) { return kindWord(id, e); }).join(" · "),
                        { fontFamily: SANS, fontSize: 11, fontWeight: "600", letterSpacing: 0.6, fill: LINE[e0.group], stroke: { color: SPACE, width: 3.5, join: "round" } });
        }
        keep[k] = p; ids[k] = true;
      });
      var leaving = [];
      Object.keys(old).forEach(function (k) { if (!keep[k]) { old[k].from = old[k].pos; old[k].mode = null; leaving.push(old[k]); } });
      if (focus && focus.leavers) focus.leavers.forEach(dropProxy);
      focus = { id: id, t0: now, proxies: keep, plan: plan, ids: ids, leavers: leaving, leaving: false };
    }
    function target(px) {
      if (px.mode === "ring") { var c = homeScreen(focus.id); return { x: c.x + px.ringAt.x, y: c.y + px.ringAt.y }; }
      return homeScreen(px.id);
    }
    function drawFocus(now) {
      focusLines.clear(); focusDots.clear();
      if (!focus) return;
      var still = reduced(), raw = still ? 1 : Math.min(1, (now - focus.t0) / FOCUS_MS), p = C.easeInOut(raw), cx = view.w / 2, cy = view.h / 2;
      function move(px) {
        var to = px.mode ? target(px) : homeScreen(px.id), from = px.from || to;
        px.pos = raw >= 1 ? to : { x: from.x + (to.x - from.x) * p, y: from.y + (to.y - from.y) * p };
        var pulse = px.centre && !still && !focus.leaving ? 1 + 0.04 * Math.sin(now / 380) : 1;
        px.c.position.set(cx + px.pos.x, cy + px.pos.y);
        px.c.scale.set(pulse);
        px.alpha = px.mode ? Math.min(1, 0.25 + p) : 1 - p;
        px.c.alpha = px.alpha;
        // a comet's tail while it travels
        if (!still && raw < 1) { px.trail.push({ x: cx + px.pos.x, y: cy + px.pos.y }); if (px.trail.length > 9) px.trail.shift(); }
        else px.trail = [];
        for (var i = 1; i < px.trail.length; i++) {
          focusLines.moveTo(px.trail[i - 1].x, px.trail[i - 1].y).lineTo(px.trail[i].x, px.trail[i].y)
            .stroke({ width: 1 + i * 0.35, color: SILVER, alpha: 0.05 * i * px.alpha, cap: "round" });
        }
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
          strokeLine(focusLines, s2, t2, e.group, hot ? 2.6 : 1.8, la * (hot ? 1 : 0.88));
          if (e.group === "backers" && !still) {
            var from = e.a === focus.id ? s2 : t2, to = e.a === focus.id ? t2 : s2;
            for (var q = 0; q < 3; q++) {
              var f = ((now / 1300) + q / 3) % 1;
              focusDots.circle(from.x + (to.x - from.x) * f, from.y + (to.y - from.y) * f, 2.4).fill({ color: LINE.backers, alpha: la });
            }
          }
          if (e.group === "backers" && still) {
            var tip = e.a === focus.id ? t2 : s2, back = e.a === focus.id ? s2 : t2;
            var bx = tip.x - back.x, by = tip.y - back.y, bl = Math.hypot(bx, by) || 1;
            bx /= bl; by /= bl;
            focusDots.poly([tip.x, tip.y, tip.x - bx * 9 - by * 4.5, tip.y - by * 9 + bx * 4.5, tip.x - bx * 9 + by * 4.5, tip.y - by * 9 - bx * 4.5])
              .fill({ color: LINE.backers, alpha: la });
          }
        });
        px.mid = { x: (s.x + t.x) / 2, y: (s.y + t.y) / 2, ux: ux, uy: uy };
      });
    }
    /** A soft light on the company in the spotlight, and the vignette over everything else (HTML, via hooks). */
    function drawSpot(fp) {
      var c = focus && focus.proxies[focus.id];
      if (!c || !c.pos || fp < 0.01) { spotLight.visible = false; if (hooks.onSpot) hooks.onSpot(null); return; }
      var x = view.w / 2 + c.pos.x, y = view.h / 2 + c.pos.y, r = Math.min(view.w - inset.right, view.h) * 0.62;
      spotLight.visible = true; spotLight.position.set(x, y); spotLight.width = spotLight.height = r * 2; spotLight.alpha = 0.13 * fp;
      if (hooks.onSpot) hooks.onSpot({ x: x, y: y, r: r, a: fp });
    }

    /* ---------------------------------------------------------- teams */
    function teamProgress(now) {
      if (!team) return 0;
      if (reduced()) return team.leaving ? 0 : 1;
      var p = C.easeInOut(Math.min(1, (now - team.t0) / TEAM_MS));
      if (team.leaving && p >= 1) { team = null; return 0; }
      return team.leaving ? 1 - p : p;
    }
    function setTeam(id, members) {
      if (!id) { if (team && !team.leaving) { team.leaving = true; team.t0 = performance.now(); } return; }
      loadBadges();
      team = { id: id, members: new Set(members), t0: performance.now(), leaving: false };
    }
    function drawTeam(tp) {
      teamG.clear();
      if (!team || tp < 0.02) return;
      var k = screenScale();
      enabledEdges().forEach(function (e) {
        if (!team.members.has(e.a) || !team.members.has(e.b) || !mainOf[e.a] || !mainOf[e.b]) return;
        var a = screenOfNode(mainOf[e.a]), b = screenOfNode(mainOf[e.b]);
        var c = C.arc(a, b, mainOf[e.a].r * k + 5, mainOf[e.b].r * k + 5, 0.12, 2, e.a, e.b), pts = [c.start];
        for (var i = 1; i <= 14; i++) pts.push(C.onCurve(c, i / 14));
        for (i = 0; i < pts.length - 1; i++) strokeLine(teamG, pts[i], pts[i + 1], e.group, 1.4, 0.7 * tp);
      });
    }

    /* ------------------------------------------------- label placing */
    var NODE_POS = [[0, 1], [1, 0], [-1, 0], [0, -1]];
    function nodeAlts(n, s, w, h, k) {
      var r = (n.sr || n.r * k) + 4;
      return NODE_POS.map(function (p) {
        var x = p[0] === 0 ? s.x - w / 2 : p[0] > 0 ? s.x + r + 2 : s.x - r - 2 - w;
        var y = p[1] === 0 ? s.y - h / 2 : p[1] > 0 ? s.y + r : s.y - r - h;
        return { x: x, y: y, w: w, h: h };
      });
    }
    function placeLabels(d, fp, tp) {
      var k = screenScale(), items = [], blocks = [], ids = 0, v = narrow ? 1 : 0, sv = narrow ? 2 : 0;
      var lview = { w: view.w, h: view.h, top: hooks.reserveTop || 0, bottom: hooks.reserveBottom || 0 };
      // far out, each sector shows one block: title, count and top three, centred on the sector
      var blockMode = d < 0.5 && tp <= 0.05;
      state.blocks = {};
      labels.forEach(function (l) { l.texts.forEach(function (t) { t.visible = false; }); l.pick = null; });
      sectorIds.forEach(function (sid) { plates[sid].visible = false; });
      if (fp < 1) {
        if (d > 0.35) nodes.forEach(function (n) {
          if (n.off) return;
          var s = screenOfNode(n), r = (n.sr || n.r * k) + 4 * k;
          if (s.x + r < 0 || s.y + r < 0 || s.x - r > view.w || s.y - r > view.h) return;
          blocks.push({ x: s.x - r, y: s.y - r, w: 2 * r, h: 2 * r });
        });
        labels.forEach(function (l, i) {
          var alts, p = 0, t0 = l.texts[0];
          if (l.kind === "title") {
            var c = screenOfSector(l.sid), R = lay.sectors[l.sid].r * k;
            if (c.x + R < 0 || c.x - R > view.w || c.y + R < 0 || c.y - R > view.h) return;
            var tx = l.texts[v];
            if (blockMode) {
              if (c.x < 0 || c.x > view.w || c.y < 0 || c.y > view.h) return;
              // zoomed in a little, a label near the frame slides inside it, and gives up its lines before its title
              alts = [statsOf[l.sid].texts[sv + (brief ? 1 : 0)], null].map(function (st) {
                var w = Math.max(tx.width, st ? st.width : 0), h = tx.height + (st ? BLOCK_GAP + st.height : 0);
                return { x: Math.max(2, Math.min(view.w - 2 - w, c.x - w / 2)), y: Math.max(lview.top, Math.min(view.h - lview.bottom - h, c.y - h / 2)), w: w, h: h, stats: st };
              });
              items.push({ id: i, p: 6000, force: true, alts: alts });
              return;
            }
            var cy = d < 0.5 ? c.y : c.y - R * 0.98, shift = d < 0.5 ? Math.max(18, R * 0.55) : 0;
            alts = [];
            [[0, 0], [0, shift], [0, -shift], [-shift, 0], [shift, 0]].forEach(function (o, pass) {
              if (pass && !shift) return;
              alts.push({ x: c.x + o[0] - tx.width / 2, y: cy + o[1] - tx.height / 2, w: tx.width, h: tx.height });
            });
            items.push({ id: i, p: 6000 - tx.width, force: true, alts: alts });
            return;
          }
          if (l.kind === "stats") return;   // placed with its title
          if (l.kind === "band") {
            if (d < 0.6 || !state.filters || !state.filters.sectors.has(l.sid)) return;
            tmp.set(l.wx - lay.sectors[l.sid].x, l.wy - lay.sectors[l.sid].y);
            var sb = sectors[l.sid].c.toGlobal(tmp);
            var bx = l.anchor === "end" ? sb.x - t0.width : l.anchor === "middle" ? sb.x - t0.width / 2 : sb.x;
            items.push({ id: i, p: 300, avoid: true, alts: [{ x: bx, y: sb.y - t0.height / 2, w: t0.width, h: t0.height }] });
            return;
          }
          var n = l.n, member = team && tp > 0.3 && n.main && team.members.has(n.id);
          if ((d < 0.35 && !member) || n.off || (team && tp > 0.3 && !member)) return;
          var special = n.main && (n.id === state.hover || n.id === state.keyFocus || member);
          var sn = screenOfNode(n);
          if (sn.x < -40 || sn.y < -40 || sn.x > view.w + 40 || sn.y > view.h + 40) return;
          p = special ? 4000 : (n.main ? 100 : 0) + (ent[n.id].ovr || 30) + (n.sector === state.sector ? 60 : 0);
          // the best-rated names may sit over a neighbour's badge, never over another name
          var top = n.main && (ent[n.id].ovr || 0) >= 85;
          items.push({ id: i, p: p, avoid: !special && !top, force: special, alts: nodeAlts(n, sn, t0.width, t0.height, k) });
        });
      }
      var shown = C.collide(items, lview, 3, blocks), byId = {};
      items.forEach(function (x) { byId[x.id] = x; });
      shown.forEach(function (alt, i) {
        var l = labels[i], kind = l.kind, t = kind === "title" ? l.texts[v] : l.texts[0];
        var box = byId[i].alts[alt];
        t.visible = true;
        var fade = kind === "title" ? 1 - 0.45 * (tp || 0) :
          kind === "node" && team && team.members.has(l.n.id) ? Math.max(tp, Math.min(1, (d - 0.35) / 0.3)) : Math.min(1, (d - 0.35) / 0.3);
        t.alpha = fade * (1 - fp);
        ids++;
        if (kind === "title" && blockMode) {
          t.position.set(box.x + (box.w - t.width) / 2, box.y);
          var st = box.stats, show = (1 - d / 0.5) * (1 - fp), plate = plates[l.sid];
          if (st) {
            st.visible = true;
            st.position.set(box.x + (box.w - st.width) / 2, box.y + t.height + BLOCK_GAP);
            st.alpha = show;
            ids++;
          }
          plate.visible = true;
          plate.position.set(box.x + box.w / 2, box.y + box.h / 2);
          plate.width = box.w * 1.25 + 20; plate.height = box.h * 1.3 + 16;
          plate.alpha = (narrow ? 0.18 : 0.3) * show;
          state.blocks[l.sid] = box;
          return;
        }
        t.position.set(box.x, box.y);
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
        if (px.kind) px.kind.visible = false;
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
      // what each neighbour is to the company, at the middle of its line, where it fits
      var kinds = [];
      all.forEach(function (px, i) {
        if (!px.kind || !px.mid || px.alpha < 0.3 || px.mode === null) return;
        var w = px.kind.width, h = px.kind.height, m = px.mid, nx = -m.uy * (h * 0.9), ny = m.ux * (h * 0.9);
        kinds.push({ id: "k" + i, px: px, p: 1, avoid: true, alts: [
          { x: m.x - w / 2, y: m.y - h / 2, w: w, h: h }, { x: m.x + nx - w / 2, y: m.y + ny - h / 2, w: w, h: h },
          { x: m.x - nx - w / 2, y: m.y - ny - h / 2, w: w, h: h }] });
      });
      var shown = C.collide(items.concat(kinds), { w: view.w, h: view.h, top: hooks.reserveTop || 0, bottom: 0 }, 3, blocks);
      kinds.forEach(function (it) {
        if (!shown.has(it.id)) return;
        var b = it.alts[shown.get(it.id)];
        it.px.kind.position.set(b.x, b.y); it.px.kind.visible = true; it.px.kind.alpha = it.px.alpha;
      });
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
        if (best) return best;
        var kk = screenScale(), hitN = null, bd = Infinity;
        nodes.forEach(function (n) {
          if (n.off || !n.main || focus.ids[n.id]) return;
          var sn = screenOfNode(n), dd = Math.hypot(sn.x - s.x, sn.y - s.y);
          if (dd <= Math.max(n.r * kk + 6, 12) && dd < bd) { bd = dd; hitN = { kind: "node", id: n.id, main: true, sector: n.sector }; }
        });
        return hitN || { kind: "focus-bg" };
      }
      var k = screenScale(), d = state.detail, hit = null, bestD = Infinity;
      if (d > 0.35) nodes.forEach(function (n) {
        if (n.off) return;
        var sn = screenOfNode(n), dd = Math.hypot(sn.x - s.x, sn.y - s.y);
        if (dd <= Math.max((n.sr || n.r * k) + 6, 12) && dd < bestD) { bestD = dd; hit = { kind: "node", id: n.id, main: n.main, sector: n.sector }; }
      });
      if (hit) return hit;
      // a label is its sector, so a line passing behind the words does not take the pointer
      Object.keys(state.blocks || {}).forEach(function (sid) {
        var b = state.blocks[sid];
        if (!hit && s.x >= b.x && s.x <= b.x + b.w && s.y >= b.y && s.y <= b.y + b.h) hit = { kind: "sector", id: sid };
      });
      if (hit) return hit;
      if (d < 0.6 && !team) bundleList.forEach(function (b) {
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
        return [focus.id].concat(focus.plan.inPlace, focus.plan.ring).map(function (k) {
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
      var wantNarrow = view.w <= NARROW_W, flipped = wantNarrow !== narrow;
      if (flipped) {
        narrow = wantNarrow;
        var moved = C.relayout(lay, narrow);
        nodes.forEach(function (n) { n.x += moved[n.sector].x; n.y += moved[n.sector].y; });
        labels.forEach(function (l) { if (l.kind === "band") { l.wx += moved[l.sid].x; l.wy += moved[l.sid].y; } });
      }
      measureGalaxy();
      kGal = galaxy.k;
      clampNow();
      return flipped;
    }
    function setFilters(f) {
      state.filters = f;
      nodes.forEach(function (n) { n.off = !f.sectors.has(n.sector) || !!(n.rank && !f.ranks.has(n.rank)); });
      rebuildBundles();
      if (focus && !focus.leaving) setFocus(focus.id);
    }
    resize(view.w, view.h);
    cam = galaxyCam();
    // a web font that arrives late changes every label's size, so draw and measure them again
    if (document.fonts && document.fonts.addEventListener) document.fonts.addEventListener("loadingdone", function () {
      var home = Math.abs(cam.k / kGal - 1) < 1e-3 && !focus && !team && !fl;
      labels.forEach(function (l) { l.texts.forEach(function (t) { t.style.update(); }); });
      measureGalaxy();
      kGal = galaxy.k;
      if (home) cam = galaxyCam(); else clampNow();
    });
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
      galaxyCam: galaxyCam, sectorCam: sectorCam, companyCam: companyCam, teamCam: teamCam, setTeam: setTeam,
      team: function () { return team && !team.leaving ? team.id : null; },
      setInset: function (v) { inset = { right: v.right || 0, top: v.top || 0, bottom: v.bottom || 0 }; },
      spotlight: function () { return focus && !focus.leaving ? { id: focus.id, inPlace: focus.plan.inPlace.slice(), ring: focus.plan.ring.slice() } : null; },
      // set the camera exactly, without the edge limits a spotlight is allowed to go past
      place: function (c) { fl = null; zoomTo = null; vel = null; panLeft = null; cam = { x: c.x, y: c.y, k: c.k }; },
      fly: fly, jump: jump, resize: resize, pick: pick, targets: targets, setFilters: setFilters,
      focus: setFocus, focused: function () { return focus && !focus.leaving ? focus.id : null; },
      linkText: function (o) { return focus && focus.plan.links[o] ? focus.plan.links[o] : []; },
      setHover: function (h) { state.hover = h; },
      setKeyFocus: function (id) { state.keyFocus = id; },
      setSector: function (sid) { state.sector = sid; },
      busy: function () { return !!(fl || zoomTo || vel || panLeft); },
      panBy: function (dx, dy) {
        fl = null; vel = null;
        panLeft = { x: (panLeft ? panLeft.x : 0) + dx, y: (panLeft ? panLeft.y : 0) + dy };
      },
      // the render loop stops while the map is out of sight
      pause: function () { app.ticker.stop(); },
      resume: function () { if (!app.ticker.started) { last = performance.now(); app.ticker.start(); } },
      labelsShown: function () { return state.labelsShown; },
      dragStart: function () { fl = null; zoomTo = null; vel = null; panLeft = null; },
      dragBy: function (dx, dy) { cam = { x: cam.x - dx / cam.k, y: cam.y - dy / cam.k, k: cam.k }; clampNow(); },
      release: function (v) { vel = reduced() || !v ? null : v; },
      zoomBy: function (factor, s) {
        fl = null; vel = null;
        var base = zoomTo ? zoomTo.k : cam.k, L = limits();
        var k = Math.max(L.min, Math.min(L.max, base * factor));
        if (reduced()) { cam = C.zoomAround(cam, view, s, k); clampNow(); zoomTo = null; return; }
        zoomTo = { k: k, s: s, w: C.toWorld(cam, view, s) };
      },
      debug: function () {
        return { cam: cam, kGal: kGal, detail: state.detail, focus: focus && focus.id, badges: Object.keys(badgeTex).length,
                 helmets: sectorIds.filter(function (sid) { return sectors[sid].helmet.visible; }).length, team: team && team.id };
      },
      // for the browser checks: where each spotlight proxy is on screen
      proxyBoxes: function () {
        if (!focus) return [];
        return Object.keys(focus.proxies).map(function (k) {
          var p = focus.proxies[k];
          return p.pos ? { id: k, x: view.w / 2 + p.pos.x, y: view.h / 2 + p.pos.y, r: p.r, mode: p.mode } : null;
        }).filter(Boolean);
      },
      narrow: function () { return narrow; },
      // for the browser checks: each sector's label block as it stands on screen
      galaxyLabels: function () {
        return sectorIds.map(function (sid) {
          var st = statsOf[sid], title = labels.filter(function (l) { return l.kind === "title" && l.sid === sid; })[0];
          var t = title.texts.filter(function (x) { return x.visible; })[0], s = st.texts.filter(function (x) { return x.visible; })[0];
          var b = (state.blocks || {})[sid];
          return { sid: sid, brief: brief, title: t ? t.text : null, titleSize: t ? t.style.fontSize : null, stats: s ? s.text : null, box: b ? { x: b.x, y: b.y, w: b.w, h: b.h } : null };
        });
      },
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
