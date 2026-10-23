/* Tech Atlas. Everything on the page works without this file. The script adds
   one sector at a time, and when a card is opened it marks that company's
   allies, rivals and owners or backers on the cards around it. */
(function () {
  var data;
  try { data = JSON.parse(document.getElementById("atlas-data").textContent); } catch (e) { return; }
  document.body.classList.add("js");

  var STYLE = {
    allies:  { stroke: "#8FD0B0", dash: "",    w: 2.2, tag: "ally" },
    rivals:  { stroke: "#E2A58F", dash: "7 5", w: 2.2, tag: "rival" },
    backers: { stroke: "#E0CB8E", dash: "",    w: 2.2, tag: "backer" }
  };
  var PRIORITY = ["rivals", "backers", "allies"];
  var NS = "http://www.w3.org/2000/svg";
  var sectors = [].slice.call(document.querySelectorAll(".sector"));
  var chips = [].slice.call(document.querySelectorAll(".chip[data-sector]"));
  var enabled = {};
  [].forEach.call(document.querySelectorAll(".toggles input[data-group]"), function (i) { enabled[i.dataset.group] = i.checked; });

  function el(name, attrs) {
    var n = document.createElementNS(NS, name);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    return n;
  }
  function activeSector() { return sectors.filter(function (s) { return s.classList.contains("is-on"); })[0]; }
  function cardsFor(sector, ent) {
    return [].slice.call(sector.querySelectorAll('.card[data-e="' + ent + '"]'));
  }

  function showSector(id, quiet) {
    sectors.forEach(function (s) { s.classList.toggle("is-on", s.dataset.sector === id); });
    chips.forEach(function (c) { c.setAttribute("aria-pressed", c.dataset.sector === id ? "true" : "false"); });
    [].forEach.call(document.querySelectorAll(".tile"), function (t) { t.classList.toggle("is-on", t.dataset.sector === id); });
    [].forEach.call(document.querySelectorAll(".card[open]"), function (o) { o.open = false; });
    clearMarks();
    if (!quiet) {
      var s = document.getElementById("sector-" + id);
      if (s) s.scrollIntoView({ behavior: "smooth", block: "start" });
      history.replaceState(null, "", "#sector-" + id);
    }
  }

  function clearMarks() {
    [].forEach.call(document.querySelectorAll(".board svg.lines"), function (s) { s.innerHTML = ""; });
    [].forEach.call(document.querySelectorAll(".card"), function (c) {
      c.classList.remove("is-dim");
      c.removeAttribute("data-rel");
      c.removeAttribute("data-tag");
    });
  }

  // Mark the open company's relationships. Lines run behind the opaque cards, so
  // they only show in the gaps between them and never cross any text.
  function mark(ent) {
    var sector = activeSector();
    if (!sector) return;
    clearMarks();
    var board = sector.querySelector(".board");
    var svg = board.querySelector("svg.lines");
    var br = board.getBoundingClientRect();
    var me = cardsFor(sector, ent)[0];
    if (!me) return;
    var rel = {};
    data.edges.forEach(function (e) {
      if (!enabled[e.g]) return;
      var other = e.a === ent ? e.b : (e.b === ent ? e.a : null);
      if (!other || other === ent) return;
      var cur = rel[other];
      if (!cur || PRIORITY.indexOf(e.g) < PRIORITY.indexOf(cur)) rel[other] = e.g;
    });
    var a = me.getBoundingClientRect();
    var ax = a.left + a.width / 2 - br.left, ay = a.top + 24 - br.top;
    [].forEach.call(sector.querySelectorAll(".card"), function (c) {
      var g = rel[c.dataset.e];
      if (c === me) return;
      if (!g) { c.classList.add("is-dim"); return; }
      c.setAttribute("data-rel", g);
      c.setAttribute("data-tag", STYLE[g].tag);
      var b = c.getBoundingClientRect();
      var bx = b.left + b.width / 2 - br.left, by = b.top + 24 - br.top;
      var s = STYLE[g];
      var p = el("path", {
        d: "M" + ax + " " + ay + " L" + bx + " " + by,
        fill: "none", stroke: s.stroke, "stroke-width": s.w, "stroke-linecap": "round"
      });
      if (s.dash) p.setAttribute("stroke-dasharray", s.dash);
      svg.appendChild(p);
    });
  }

  // a card is selected by opening it
  document.addEventListener("toggle", function (ev) {
    var c = ev.target;
    if (!c.classList || !c.classList.contains("card")) return;
    if (c.open) {
      [].forEach.call(document.querySelectorAll(".card[open]"), function (o) { if (o !== c) o.open = false; });
      mark(c.dataset.e);
    } else if (!document.querySelector(".card[open]")) clearMarks();
  }, true);

  // tabs, chips and tiles
  chips.forEach(function (c) { c.addEventListener("click", function () { showSector(c.dataset.sector); }); });
  [].forEach.call(document.querySelectorAll(".tile"), function (t) {
    t.addEventListener("click", function (e) { e.preventDefault(); showSector(t.dataset.sector); });
  });

  // relationship toggles
  [].forEach.call(document.querySelectorAll(".toggles input[data-group]"), function (i) {
    i.addEventListener("change", function () {
      enabled[i.dataset.group] = i.checked;
      document.body.classList.toggle("hide-" + i.dataset.group, !i.checked);
      var o = document.querySelector(".card[open]");
      if (o) mark(o.dataset.e);
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
    var run = function () {
      var q = search.value.trim().toLowerCase();
      if (!q) return;
      var k = byName[q];
      if (!k) {
        var m = Object.keys(byName).filter(function (n) { return n.indexOf(q) > -1; });
        if (m.length) k = byName[m[0]];
      }
      if (k) goTo(k);
    };
    search.addEventListener("change", run);
    search.addEventListener("keydown", function (e) { if (e.key === "Enter") run(); });
  }

  // start on the sector in the address, a company, or silicon
  function start() {
    var h = location.hash.replace("#", "");
    var id = "silicon";
    if (h.indexOf("sector-") === 0) id = h.slice(7);
    else if (h.indexOf("c-") === 0) { var c = document.getElementById(h); if (c) id = c.closest(".sector").dataset.sector; }
    showSector(id, true);
    if (h.indexOf("c-") === 0) { var cc = document.getElementById(h); if (cc) cc.open = true; }
  }
  window.addEventListener("resize", function () {
    var o = document.querySelector(".card[open]");
    if (o) mark(o.dataset.e); else clearMarks();
  });
  start();
})();
