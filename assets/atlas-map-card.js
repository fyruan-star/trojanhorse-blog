/* Tech Atlas map: the player card beside the map (a sheet on phones).

   Three tabs: Ratings (OVR, six attribute bars, a hexagon radar, badges),
   Profile (the Atlas card text) and Connections (allies, rivals, backers).
   The header carries the company's logo and a link to its full profile page.
   Everything is built with textContent, never parsed HTML. */
(function () {
  "use strict";
  var C = window.AtlasMapCore;
  var SVG = "http://www.w3.org/2000/svg";
  var RANK = { starter: { name: "Starter", why: "Why it leads" }, second: { name: "Second string", why: "Why it may rise" },
               rookie: { name: "Practice squad", why: "Why it matters" } };
  var GROUP_LABEL = { allies: "Allies and partners", rivals: "Rivals", backers: "Owners and backers" };
  var VERB = { ownership: ["owns", "owned by"], investment: ["funds", "funded by"] };
  var SHORT = { dominance: "DOM", momentum: "MOM", leverage: "LEV", durability: "DUR", firepower: "FIR", deal_heat: "DEAL" };
  var TABS = [["ratings", "Ratings"], ["profile", "Profile"], ["connections", "Connections"]];

  function h(tag, attrs, kids) {
    var n = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      if (k === "text") n.textContent = attrs[k];
      else if (k === "cls") n.className = attrs[k];
      else n.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) { if (c) n.appendChild(typeof c === "string" ? document.createTextNode(c) : c); });
    return n;
  }
  function s(tag, attrs, parent) {
    var n = document.createElementNS(SVG, tag);
    Object.keys(attrs).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    if (parent) parent.appendChild(n);
    return n;
  }
  /** The company's official mark on a round ground, or its initials when the Atlas has none. */
  function mark(e) {
    if (!e.logo) return h("span", { cls: "pc__mono", "aria-hidden": "true", text: e.initials || C.initials(e.name) });
    return h("span", { cls: "pc__logo" + (e.logo.ground === "dark" ? " pc__logo--dark" : ""), "aria-hidden": "true" },
             [h("img", { src: e.logo.file, alt: "", decoding: "async" })]);
  }
  function host(u) { try { return new URL(u).hostname.replace(/^www\./, ""); } catch (e) { return "source"; } }
  function source(url, trust) {
    return h("span", { cls: "pc__src" }, [h("span", { cls: "conf conf--" + trust, text: trust }), " ",
      h("a", { href: url, target: "_blank", rel: "noopener noreferrer", text: host(url) })]);
  }

  /** Build the card for company id into panel. ctx: {data, sectorName, rowName, cardsOf, tab, onTab, onGo}. */
  function render(panel, id, ctx) {
    var data = ctx.data, e = data.entities[id], tab = ctx.tab || "ratings";
    var cards = ctx.cardsOf[id] || [], home = cards.filter(function (c) { return c.sector === e.home; })[0] || cards[0];
    var tierName = e.ovr != null ? C.tier(e.ovr, data.ovr_tiers) : "Unrated";
    panel.textContent = "";
    panel.className = "pcard c-" + (e.home || "backers");

    var name = h("h2", { cls: "pc__name", id: "pc-name", tabindex: "-1", text: e.name });
    var meta = (e.home ? ctx.sectorName[e.home] : "Owners and backers") + (home ? " · " + ctx.rowName[home.sector + "/" + home.row] : "");
    var ovr = h("div", { cls: "pc__ovr", "data-tier": tierName }, [
      h("span", { cls: "pc__num", text: e.ovr != null ? String(e.ovr) : "NR" }),
      h("span", { cls: "pc__k", text: e.ovr != null ? "OVR" : "Not rated" }),
      h("span", { cls: "pc__tier", text: tierName }),
      e.ovr_status === "draft" ? h("span", { cls: "pc__draft", text: "Draft" }) : null
    ]);
    var rankBits = home ? [h("span", { cls: "badge", text: RANK[home.pl.t].name }),
      home.pl.badge ? h("span", { cls: "badge badge--label", text: home.pl.badge }) : null] : [];
    panel.appendChild(h("button", { type: "button", cls: "pc__close", "aria-label": "Close card", text: "×" }));
    panel.appendChild(h("header", { cls: "pc__head" }, [ovr, h("div", { cls: "pc__id" }, [
      mark(e),
      h("div", {}, [name, h("p", { cls: "pc__meta", text: meta }), h("p", { cls: "pc__rank" }, rankBits),
        e.profile ? h("a", { cls: "pc__profile", href: e.profile, text: "Open full profile \u2192" }) : null,
        e.page ? h("a", { cls: "pc__page", href: e.page, text: "Stats page \u2192" }) : null])])]));

    var list = h("div", { cls: "pc__tabs", role: "tablist", "aria-label": "Card sections" });
    TABS.forEach(function (t) {
      list.appendChild(h("button", { type: "button", role: "tab", id: "pc-tab-" + t[0], cls: "pc__tab",
        "aria-selected": t[0] === tab ? "true" : "false", "aria-controls": "pc-panel", tabindex: t[0] === tab ? "0" : "-1",
        "data-tab": t[0], text: t[1] }));
    });
    panel.appendChild(list);
    var body = h("div", { cls: "pc__body", role: "tabpanel", id: "pc-panel", "aria-labelledby": "pc-tab-" + tab, tabindex: "0" });
    (tab === "profile" ? profile(e, home, cards, ctx) : tab === "connections" ? connections(id, ctx) : ratings(e, data))
      .forEach(function (n) { if (n) body.appendChild(n); });
    panel.appendChild(body);
    return name;
  }

  function ratings(e, data) {
    var attrs = e.attributes || {}, out = [];
    if (e.ovr_reason) out.push(h("p", { cls: "pc__lede", text: e.ovr_reason }));
    if (e.ovr != null) out.push(h("p", { cls: "pc__note", text: "OVR from " + e.ovr_from + " of 6 attributes" +
      (e.ovr_status === "draft" ? ", drafted from the Atlas data and not yet reviewed." : ".") }));
    if (!Object.keys(attrs).length && e.ovr == null) out.push(h("p", { cls: "pc__note", text: "No published ratings for this company yet." }));
    var bars = h("ul", { cls: "pc__bars" });
    data.attributes.forEach(function (a) {
      var v = attrs[a.id] ? attrs[a.id].value : null, x = attrs[a.id];
      var tier = v != null ? C.tier(v, data.ovr_tiers) : "Unrated";
      var head = h("button", { type: "button", cls: "pc__bar", "aria-expanded": "false", "data-tier": tier }, [
        h("span", { cls: "pc__bn", text: a.label }),
        h("span", { cls: "pc__bt", "aria-hidden": "true" }, [h("span", { cls: "pc__bf", style: "width:" + (v != null ? Math.round((v - 30) / 69 * 100) : 0) + "%" })]),
        h("span", { cls: "pc__bv", text: v != null ? String(v) : "unrated" }),
        x && x.status === "draft" && v != null ? h("span", { cls: "pc__bd", text: "draft" }) : null
      ]);
      var more = h("div", { cls: "pc__why", hidden: "" }, [h("p", { text: x ? x.reason : "Not rated yet." })]
        .concat(x ? (x.evidence || []).map(function (ev) { return source(ev.url, ev.trust); }) : [])
        .concat(a.id === "leverage" && x && x.value != null ? [h("p", { cls: "pc__note", text: "Network base " + x.base + ", judgment " + (x.adjust >= 0 ? "+" : "") + x.adjust + "." })] : [])
        .concat([h("p", { cls: "pc__note", text: "Weight in OVR: " + Math.round(a.weight * 100) + "%." })]));
      bars.appendChild(h("li", {}, [head, more]));
    });
    out.push(bars);
    out.push(radarSvg(data.attributes.map(function (a) { return attrs[a.id] ? attrs[a.id].value : null; }),
                      data.attributes.map(function (a) { return a.label; })));
    if ((e.badges || []).length) {
      out.push(h("h3", { cls: "pc__h", text: "Badges" }));
      out.push(h("ul", { cls: "pc__badges" }, e.badges.map(function (b) {
        return h("li", { cls: "pc__badge pc__badge--" + b.id }, [h("span", { cls: "pc__bname", text: b.label }),
          b.status === "draft" ? h("span", { cls: "pc__bd", text: "draft" }) : null, h("p", { text: b.reason })]
          .concat((b.evidence || []).map(function (ev) { return source(ev.url, ev.trust); })));
      })));
    }
    return out;
  }

  function radarSvg(values, labels) {
    var R = 74, pad = 46, size = 2 * (R + pad);
    var svg = s("svg", { viewBox: [-R - pad, -R - pad, size, size].join(" "), role: "img",
      "aria-label": "Attribute radar: " + labels.map(function (l, i) { return l + " " + (values[i] != null ? values[i] : "unrated"); }).join(", ") });
    svg.setAttribute("class", "pc__radar");
    [1, 0.66, 0.33].forEach(function (f) {
      s("polygon", { points: C.radar([99, 99, 99, 99, 99, 99], R * f).map(function (p) { return p.x + "," + p.y; }).join(" "), "class": "pc__grid" }, svg);
    });
    C.radar([99, 99, 99, 99, 99, 99], R).forEach(function (p, i) {
      s("line", { x1: 0, y1: 0, x2: p.x, y2: p.y, "class": "pc__grid" }, svg);
      var t = s("text", { x: p.x * 1.32, y: p.y * 1.24 + 4, "text-anchor": Math.abs(p.x) < 1 ? "middle" : p.x > 0 ? "start" : "end", "class": "pc__rl" }, svg);
      t.textContent = SHORT[["dominance", "momentum", "leverage", "durability", "firepower", "deal_heat"][i]] + " " + (values[i] != null ? values[i] : "–");
    });
    s("polygon", { points: C.radar(values, R).map(function (p) { return p.x + "," + p.y; }).join(" "), "class": "pc__shape" }, svg);
    C.radar(values, R).forEach(function (p, i) {
      s("circle", { cx: p.x, cy: p.y, r: values[i] != null ? 3 : 2.2, "class": values[i] != null ? "pc__dot" : "pc__dot pc__dot--none" }, svg);
    });
    return h("figure", { cls: "pc__fig" }, [svg]);
  }

  function profile(e, home, cards, ctx) {
    var out = [h("p", { cls: "pc__desc", text: e.description })];
    if (!home) return out.concat([h("p", { cls: "pc__note", text: "An owner or investor that appears in the Atlas only through its relationships." })]);
    var pl = home.pl;
    out.push(fact("Key figure", pl.stat), fact(RANK[pl.t].why, pl.why), fact("What could change it", pl.cond), source(pl.src, pl.conf || "sourced"));
    var also = cards.filter(function (c) { return c !== home; });
    if (also.length) out.push(h("p", { cls: "pc__also", text: "Also plays in " + also.map(function (c) {
      return ctx.sectorName[c.sector] + ", " + ctx.rowName[c.sector + "/" + c.row] + " (" + RANK[c.pl.t].name.toLowerCase() + ")";
    }).join(" and ") + "." }));
    return out;
  }
  function fact(label, txt) { return h("div", { cls: "pc__fact" }, [h("h3", { cls: "pc__h", text: label }), h("p", { text: txt })]); }

  function connections(id, ctx) {
    var data = ctx.data, groups = { allies: [], rivals: [], backers: [] };
    data.edges.forEach(function (e) {
      if (e.a !== id && e.b !== id) return;
      var other = e.a === id ? e.b : e.a, oe = data.entities[other];
      var verb = VERB[e.type] ? (e.a === id ? VERB[e.type][0] : VERB[e.type][1]) + " " : "";
      groups[e.group].push(h("li", {}, [
        h("button", { type: "button", cls: "pc__go", "data-go": other }, [verb ? h("span", { cls: "pc__verb", text: verb }) : null, oe.name,
          oe.ovr != null ? h("span", { cls: "pc__govr", text: " " + oe.ovr }) : null]),
        oe.home && oe.home !== data.entities[id].home ? h("span", { cls: "pc__in", text: " in " + ctx.sectorName[oe.home] }) : null,
        h("p", { cls: "pc__x", text: e.text }), source(e.src, e.conf)]));
    });
    var out = ["allies", "rivals", "backers"].filter(function (g) { return groups[g].length; }).map(function (g) {
      return h("section", { cls: "pc__rel pc__rel--" + g }, [h("h3", { cls: "pc__h", text: GROUP_LABEL[g] }), h("ul", {}, groups[g])]);
    });
    return out.length ? out : [h("p", { cls: "pc__note", text: "The Atlas draws no relationships for this company yet." })];
  }

  window.AtlasMapCard = { render: render, TABS: TABS.map(function (t) { return t[0]; }) };
})();
