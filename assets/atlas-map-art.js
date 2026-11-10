/* Tech Atlas map: the art the scene draws with, made into WebGL textures.

   Each sector has one helmet (images/helmets/<sector>.svg, drawn by
   scripts/atlas-helmets/), in white so the map can tint it the sector's colour.
   Logo badges put a company's official mark on a round light
   or dark ground, or its initials in the sector colour when the Atlas has no
   official file. Logos are drawn as published: never recoloured or reshaped. */
(function () {
  "use strict";

  var HELMET_PX = 800;          // texture height: sharp at sector zoom without wasting memory on ten of them
  var BADGE_PX = 128;
  var SANS = 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif';

  function loadImage(url) {
    return new Promise(function (resolve, reject) {
      var img = new Image();
      img.decoding = "async";
      img.onload = function () { resolve(img); };
      img.onerror = function () { reject(new Error("could not load " + url)); };
      img.src = url;
    });
  }

  function canvas(w, h) {
    var c = document.createElement("canvas");
    c.width = w; c.height = h;
    return c;
  }

  /** Each sector's helmet as a white texture, {sid: {texture, ratio}}. One that cannot load is left out, and the map still works without it. */
  function helmets(PIXI, ids) {
    var out = {};
    return Promise.all(ids.map(function (sid) {
      return loadImage("images/helmets/" + sid + ".svg").then(function (img) {
        var ratio = (img.naturalWidth || 800) / (img.naturalHeight || 840);
        var c = canvas(Math.round(HELMET_PX * ratio), HELMET_PX);
        c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
        out[sid] = { texture: PIXI.Texture.from(c), ratio: ratio };
      }).catch(function () { /* this sector goes without */ });
    })).then(function () { return out; });
  }

  function monogram(x, text, color) {
    x.fillStyle = "#0F1522";
    x.beginPath(); x.arc(BADGE_PX / 2, BADGE_PX / 2, BADGE_PX / 2 - 3, 0, 6.2832); x.fill();
    x.lineWidth = 5; x.strokeStyle = color;
    x.beginPath(); x.arc(BADGE_PX / 2, BADGE_PX / 2, BADGE_PX / 2 - 5, 0, 6.2832); x.stroke();
    x.fillStyle = color;
    x.font = "600 " + Math.round(BADGE_PX * 0.36) + "px " + SANS;
    x.textAlign = "center"; x.textBaseline = "middle";
    x.fillText(text, BADGE_PX / 2, BADGE_PX / 2 + 2);
  }

  /** A round badge texture for one company: {texture, logo} where logo says whether it is the official mark. */
  function badge(PIXI, ent, color) {
    var c = canvas(BADGE_PX, BADGE_PX), x = c.getContext("2d");
    var css = "#" + ("000000" + color.toString(16)).slice(-6);
    function done(isLogo) { return { texture: PIXI.Texture.from(c), logo: isLogo }; }
    if (!ent.logo) { monogram(x, ent.initials || "", css); return Promise.resolve(done(false)); }
    return loadImage(ent.logo.file).then(function (img) {
      var dark = ent.logo.ground === "dark", r = BADGE_PX / 2;
      x.fillStyle = dark ? "#0F1522" : "#EEF2F7";
      x.beginPath(); x.arc(r, r, r - 2, 0, 6.2832); x.fill();
      x.lineWidth = 3; x.strokeStyle = "rgba(226,233,243,.55)";
      x.beginPath(); x.arc(r, r, r - 3, 0, 6.2832); x.stroke();
      // the mark is contained in a centred square, at its own proportions
      var box = BADGE_PX * 0.62, w = img.naturalWidth || box, h = img.naturalHeight || box, s = Math.min(box / w, box / h);
      x.drawImage(img, r - w * s / 2, r - h * s / 2, w * s, h * s);
      return done(true);
    }).catch(function () {
      x.clearRect(0, 0, BADGE_PX, BADGE_PX);
      monogram(x, ent.initials || "", css);
      return done(false);
    });
  }

  /** A slow shooting star now and then: call step(now, view) each frame. Off with reduced motion. */
  function shootingStar(PIXI, layer, reduced) {
    var g = new PIXI.Graphics(), next = performance.now() + 6000 + Math.random() * 14000, run = null;
    layer.addChild(g);
    function step(now, view) {
      g.clear();
      if (reduced()) { run = null; return; }
      if (!run && now > next) {
        var a = 0.35 + Math.random() * 0.5, len = Math.max(view.w, view.h) * (0.35 + Math.random() * 0.25);
        run = { t0: now, ms: 1400 + Math.random() * 900, x: view.w * (0.15 + Math.random() * 0.7), y: view.h * (0.05 + Math.random() * 0.35),
                dx: Math.cos(a) * len, dy: Math.sin(a) * len };
      }
      if (!run) return;
      var p = (now - run.t0) / run.ms;
      if (p >= 1) { run = null; next = now + 20000 + Math.random() * 20000; return; }
      var head = { x: run.x + run.dx * p, y: run.y + run.dy * p }, tail = Math.min(p, 0.22);
      var fade = Math.sin(Math.PI * p);
      for (var i = 0; i < 6; i++) {
        var t0 = p - tail * (i + 1) / 6, t1 = p - tail * i / 6;
        g.moveTo(run.x + run.dx * t0, run.y + run.dy * t0).lineTo(run.x + run.dx * t1, run.y + run.dy * t1)
          .stroke({ width: 1.6 - i * 0.2, color: 0xEEF2F8, alpha: fade * (0.75 - i * 0.12), cap: "round" });
      }
      g.circle(head.x, head.y, 1.6).fill({ color: 0xFFFFFF, alpha: fade });
    }
    return { step: step };
  }

  window.AtlasMapArt = { helmets: helmets, badge: badge, shootingStar: shootingStar };
})();
