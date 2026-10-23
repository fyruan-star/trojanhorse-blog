/* Tech Atlas. Everything on the page works without this file. The script adds
   one sector at a time, lines between companies, search and edge filters. */
(function () {
  var data;
  try { data = JSON.parse(document.getElementById("atlas-data").textContent); } catch (e) { return; }
  document.body.classList.add("js");

  var STYLE = {
    alliance:   { stroke: "#E2E9F3", dash: "",     w: 1.6, arrow: false },
    supply:     { stroke: "#E2E9F3", dash: "",     w: 1.6, arrow: false },
    license:    { stroke: "#E2E9F3", dash: "2 3",  w: 1.6, arrow: false },
    rivalry:    { stroke: "#E2A58F", dash: "6 5",  w: 1.6, arrow: false },
    ownership:  { stroke: "#E0CB8E", dash: "",     w: 2.2, arrow: true },
    investment: { stroke: "#E0CB8E", dash: "",     w: 2.2, arrow: true },
    dependency: { stroke: "#93B6DB", dash: "1 4",  w: 1.4, arrow: true }
  };
  var NS = "http://www.w3.org/2000/svg";
  var sectors = [].slice.call(document.querySelectorAll(".sector"));
  var chips = [].slice.call(document.querySelectorAll(".chip[data-sector]"));
  var enabled = {};
  [].forEach.call(document.querySelectorAll(".toggles input[data-edge]"), function (i) { enabled[i.dataset.edge] = i.checked; });

  function el(name, attrs) {
    var n = document.createElementNS(NS, name);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    return n;
  }
  function ensureDefs(svg) {
    if (svg.querySelector("defs")) return;
    var d = el("defs", {});
    ["E0CB8E", "93B6DB"].forEach(function (c) {
      var m = el("marker", { id: "ah-" + c, viewBox: "0 0 10 10", refX: "9", refY: "5", markerWidth: "7", markerHeight: "7", orient: "auto-start-reverse" });
      m.appendChild(el("path", { d: "M0 0 L10 5 L0 10 z", fill: "#" + c }));
      d.appendChild(m);
    });
    svg.appendChild(d);
  }

  function activeSector() { return sectors.filter(function (s) { return s.classList.contains("is-on"); })[0]; }

  function showSector(id, quiet) {
    sectors.forEach(function (s) { s.classList.toggle("is-on", s.dataset.sector === id); });
    chips.forEach(function (c) { c.setAttribute("aria-pressed", c.dataset.sector === id ? "true" : "false"); });
    [].forEach.call(document.querySelectorAll(".tile"), function (t) { t.classList.toggle("is-on", t.dataset.sector === id); });
    clearLines();
    if (!quiet) {
      var s = document.getElementById("sector-" + id);
      if (s) s.scrollIntoView({ behavior: "smooth", block: "start" });
      history.replaceState(null, "", "#sector-" + id);
    }
  }

  function cardsFor(sector, ent) {
    return [].slice.call(sector.querySelectorAll('.card[data-e="' + ent + '"]'));
  }

  function clearLines() {
    [].forEach.call(document.querySelectorAll(".board svg.lines"), function (s) { s.innerHTML = ""; });
    [].forEach.call(document.querySelectorAll(".card"), function (c) { c.classList.remove("is-dim", "is-hit"); });
  }

  function drawFor(ent) {
    var sector = activeSector();
    if (!sector) return;
    var board = sector.querySelector(".board");
    var svg = board.querySelector("svg.lines");
    svg.innerHTML = "";
    ensureDefs(svg);
    var br = board.getBoundingClientRect();
    var me = cardsFor(sector, ent)[0];
    if (!me) return;
    var hits = {};
    hits[ent] = true;
    data.edges.forEach(function (e) {
      if (!enabled[e.type]) return;
      var other = e.a === ent ? e.b : (e.b === ent ? e.a : null);
      if (!other) return;
      var oc = cardsFor(sector, other)[0];
      if (!oc) return;
      hits[other] = true;
      var s = STYLE[e.type] || STYLE.supply;
      var a = me.getBoundingClientRect(), b = oc.getBoundingClientRect();
      var ax = a.left + a.width / 2 - br.left, ay = a.top + a.height / 2 - br.top;
      var bx = b.left + b.width / 2 - br.left, by = b.top + b.height / 2 - br.top;
      var mx = (ax + bx) / 2, my = (ay + by) / 2;
      var dx = bx - ax, dy = by - ay, len = Math.sqrt(dx * dx + dy * dy) || 1;
      var cx = mx - dy / len * Math.min(60, len / 5), cy = my + dx / len * Math.min(60, len / 5);
      var from = e.a === ent ? [ax, ay] : [bx, by], to = e.a === ent ? [bx, by] : [ax, ay];
      var p = el("path", {
        d: "M" + from[0] + " " + from[1] + " Q" + cx + " " + cy + " " + to[0] + " " + to[1],
        fill: "none", stroke: s.stroke, "stroke-width": s.w, opacity: ".9"
      });
      if (s.dash) p.setAttribute("stroke-dasharray", s.dash);
      if (s.arrow) p.setAttribute("marker-end", "url(#ah-" + s.stroke.slice(1) + ")");
      svg.appendChild(p);
    });
    [].forEach.call(sector.querySelectorAll(".card"), function (c) {
      var on = hits[c.dataset.e];
      c.classList.toggle("is-dim", !on);
      c.classList.toggle("is-hit", !!on && c.dataset.e !== ent);
    });
  }

  // lines appear on hover and when a card is opened
  document.addEventListener("mouseover", function (ev) {
    var c = ev.target.closest && ev.target.closest(".card");
    if (c) drawFor(c.dataset.e);
  });
  document.addEventListener("mouseout", function (ev) {
    var c = ev.target.closest && ev.target.closest(".card");
    if (c && !document.querySelector(".card[open]")) clearLines();
    else if (c) { var o = document.querySelector(".card[open]"); if (o) drawFor(o.dataset.e); }
  });
  document.addEventListener("toggle", function (ev) {
    var c = ev.target;
    if (!c.classList || !c.classList.contains("card")) return;
    if (c.open) { [].forEach.call(document.querySelectorAll(".card[open]"), function (o) { if (o !== c) o.open = false; }); drawFor(c.dataset.e); }
    else clearLines();
  }, true);

  // tabs, chips and tiles
  chips.forEach(function (c) { c.addEventListener("click", function () { showSector(c.dataset.sector); }); });
  [].forEach.call(document.querySelectorAll(".tile"), function (t) {
    t.addEventListener("click", function (e) { e.preventDefault(); showSector(t.dataset.sector); });
  });

  // edge type toggles
  [].forEach.call(document.querySelectorAll(".toggles input[data-edge]"), function (i) {
    i.addEventListener("change", function () {
      enabled[i.dataset.edge] = i.checked;
      document.body.classList.toggle("hide-" + i.dataset.edge, !i.checked);
      var o = document.querySelector(".card[open]");
      if (o) drawFor(o.dataset.e); else drawOverview();
    });
  });

  // jump to a company, from search or a connection link
  function goTo(ent) {
    var id = data.home[ent];
    if (!id) return false;
    showSector(id, true);
    var sector = document.getElementById("sector-" + id);
    var c = cardsFor(sector, ent)[0];
    if (!c) return false;
    c.open = true;
    c.scrollIntoView({ behavior: "smooth", block: "center" });
    c.classList.remove("flash"); void c.offsetWidth; c.classList.add("flash");
    return true;
  }
  document.addEventListener("click", function (ev) {
    var a = ev.target.closest && ev.target.closest("a[data-go]");
    if (!a) return;
    ev.preventDefault();
    goTo(a.dataset.go);
  });
  var search = document.getElementById("atlas-search");
  if (search) {
    var byName = {};
    Object.keys(data.names).forEach(function (k) { byName[data.names[k].toLowerCase()] = k; });
    function run() {
      var q = search.value.trim().toLowerCase();
      if (!q) return;
      var k = byName[q];
      if (!k) {
        var m = Object.keys(byName).filter(function (n) { return n.indexOf(q) === 0 || n.indexOf(q) > -1; });
        if (m.length) k = byName[m[0]];
      }
      if (k) goTo(k);
    }
    search.addEventListener("change", run);
    search.addEventListener("keydown", function (e) { if (e.key === "Enter") run(); });
  }

  // overview: one line per pair of sectors that share relationships
  function drawOverview() {
    var ov = document.getElementById("overview");
    var svg = ov.querySelector("svg.links");
    if (!svg) return;
    svg.innerHTML = "";
    if (window.innerWidth <= 900) return;
    var r = ov.getBoundingClientRect();
    var pts = {};
    [].forEach.call(ov.querySelectorAll(".tile"), function (t) {
      var b = t.getBoundingClientRect();
      pts[t.dataset.sector] = [b.left + b.width / 2 - r.left, b.top + b.height / 2 - r.top, b];
    });
    data.pairs.forEach(function (p) {
      var kinds = p.types.filter(function (t) { return enabled[t]; });
      if (!kinds.length) return;
      var a = pts[p.a], b = pts[p.b];
      if (!a || !b) return;
      var kind = kinds.indexOf("ownership") > -1 || kinds.indexOf("investment") > -1 ? "investment" : (kinds.indexOf("rivalry") > -1 ? "rivalry" : kinds[0]);
      var s = STYLE[kind];
      var mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2;
      var dx = b[0] - a[0], dy = b[1] - a[1], len = Math.sqrt(dx * dx + dy * dy) || 1;
      var off = Math.min(70, len / 4);
      var path = el("path", {
        d: "M" + a[0] + " " + a[1] + " Q" + (mx - dy / len * off) + " " + (my + dx / len * off) + " " + b[0] + " " + b[1],
        fill: "none", stroke: s.stroke, "stroke-width": Math.min(1 + p.n * 0.35, 4), opacity: ".38"
      });
      if (s.dash) path.setAttribute("stroke-dasharray", s.dash);
      svg.appendChild(path);
    });
  }

  // start on the sector in the address, a company, or silicon
  function start() {
    var h = location.hash.replace("#", "");
    var id = "silicon";
    if (h.indexOf("sector-") === 0) id = h.slice(7);
    else if (h.indexOf("c-") === 0) { var c = document.getElementById(h); if (c) id = c.closest(".sector").dataset.sector; }
    showSector(id, true);
    drawOverview();
    if (h.indexOf("c-") === 0) { var cc = document.getElementById(h); if (cc) { cc.open = true; } }
  }
  window.addEventListener("resize", function () { drawOverview(); clearLines(); });
  window.addEventListener("load", drawOverview);
  start();
})();
