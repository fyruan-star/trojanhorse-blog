// Browser checks for the Atlas map and its pages, in Chromium and WebKit.
//
//   python3 build.py && python3 -m http.server -d _site 8731 &
//   node scripts/check_atlas_map.mjs [screenshot folder]
//
// Needs the playwright package (npm i playwright) with its browsers installed.
// It is not part of the build, which stays standard library only.
import { createRequire } from "node:module";
import { mkdirSync } from "node:fs";

const require = createRequire(import.meta.url);
const { chromium, webkit } = require(process.env.PLAYWRIGHT_PATH || "playwright");
const BASE = process.env.ATLAS_BASE || "http://localhost:8731";
const OUT = process.argv[2] || "atlas-shots";
mkdirSync(OUT, { recursive: true });

const VIEWPORTS = [{ name: "desktop", width: 1280, height: 900 }, { name: "phone", width: 375, height: 812 }];
const SPOTLIGHTS = ["oracle", "nvidia", "anthropic"];
// GPU driver notes printed when a screenshot reads the canvas back are not page errors
const IGNORE = /GL Driver Message|GPU stall|ReadPixels/;
const results = [];
const check = (engine, vp, name, ok, detail) => results.push({ engine, vp, name, ok: !!ok, detail: detail || "" });

async function openMap(page, hash = "") {
  await page.goto(`${BASE}/tech-atlas.html?check=${Date.now()}${hash}`);
  await page.evaluate(() => window.AtlasMap && window.AtlasMap.ready());
  await page.waitForFunction(() => window.AtlasMap && window.AtlasMap.api() && window.AtlasMap.api().scene.debug().helmets > 0, null, { timeout: 15000 });
  await page.evaluate(() => document.getElementById("atlas-map").scrollIntoView({ block: "center" }));
  await page.waitForTimeout(900);
}
const cam = (page) => page.evaluate(() => AtlasMap.api().scene.cam());
const settle = (page) => page.waitForFunction(() => !AtlasMap.api().scene.busy(), null, { timeout: 8000 }).catch(() => {});

async function centre(page) {
  const r = await page.evaluate(() => { const b = document.querySelector(".amap__canvas").getBoundingClientRect(); return { x: b.left + b.width / 2, y: b.top + b.height / 2 }; });
  await page.mouse.move(r.x, r.y);
  return r;
}

async function frameTimes(page, run) {
  // one sampler at a time: each run has its own token, and the previous loop stops when the token changes
  await page.evaluate(() => {
    const token = (window.__ftToken || 0) + 1, dts = [];
    window.__ftToken = token; window.__dts = dts;
    let last = performance.now();
    const tick = (t) => { if (window.__ftToken !== token) return; dts.push(t - last); last = t; requestAnimationFrame(tick); };
    requestAnimationFrame(tick);
  });
  await run();
  const dts = await page.evaluate(() => { const d = window.__dts.slice(2); window.__ftToken++; return d; });
  const sorted = dts.slice().sort((a, b) => a - b);
  const avg = dts.reduce((a, b) => a + b, 0) / Math.max(1, dts.length);
  return { frames: dts.length, avgMs: +avg.toFixed(1), p95Ms: +(sorted[Math.floor(sorted.length * 0.95)] || 0).toFixed(1),
           maxMs: +(sorted[sorted.length - 1] || 0).toFixed(1), fps: +(1000 / avg).toFixed(0) };
}

async function mapChecks(browser, engine, vp) {
  const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
  const errors = [];
  page.on("pageerror", (e) => errors.push(String(e)));
  page.on("console", (m) => { if (m.type() === "error" && !IGNORE.test(m.text())) errors.push(m.text()); });
  await openMap(page);
  const tag = `${engine}-${vp.name}`;

  // the frame: margins on desktop, edge to edge on phones
  const fr = await page.evaluate(() => { const r = document.querySelector(".amap__stage").getBoundingClientRect(); return { l: r.left, r: innerWidth - r.right, w: r.width, h: r.height, vw: innerWidth, vh: innerHeight }; });
  if (vp.name === "desktop") check(engine, vp.name, "frame leaves margins", fr.l >= 40 && fr.r >= 40 && fr.h <= fr.vh * 0.75, JSON.stringify(fr));
  else check(engine, vp.name, "frame goes edge to edge", fr.l === 0 && fr.r === 0 && fr.h >= 400, JSON.stringify(fr));

  const dbg = await page.evaluate(() => AtlasMap.api().scene.debug());
  check(engine, vp.name, "ten helmets drawn", dbg.helmets === 10, `helmets ${dbg.helmets}`);
  await page.screenshot({ path: `${OUT}/${tag}-galaxy.png` });

  // the galaxy's labels: all ten complete, one title style, clear of each other and of the controls
  const gal = await page.evaluate(() => {
    const s = AtlasMap.api().scene, frame = document.querySelector(".amap__canvas").getBoundingClientRect();
    const keepOut = [...document.querySelectorAll(".amap__legend, .amap__mini, .amap__tools, .amap__hint")].map((el) => {
      const r = el.getBoundingClientRect();
      return { name: el.className, x: r.left - frame.left, y: r.top - frame.top, w: r.width, h: r.height };
    }).filter((r) => r.w && r.h);
    return { labels: s.galaxyLabels(), view: s.view(), keepOut };
  });
  const hits = (a, b) => a.x < b.x + b.w && b.x < a.x + a.w && a.y < b.y + b.h && b.y < a.y + a.h;
  const complete = gal.labels.filter((l) => {
    const lines = (l.stats || "").split("\n");
    return l.title && lines.length === 4 && (l.sid === "backers" ? /^12 owners and backers$/.test(lines[0]) && lines.slice(1).every((x) => / · \d+ backed$/.test(x)) : /^\d+ compan(y|ies)$/.test(lines[0]) && lines.slice(1).every((x) => /\s\d+$/.test(x)));
  });
  check(engine, vp.name, "ten sectors show a title, count and top 3", complete.length === 10, gal.labels.filter((l) => !complete.includes(l)).map((l) => l.sid).join(","));
  check(engine, vp.name, "all sector titles share one size", new Set(gal.labels.map((l) => l.titleSize)).size === 1, [...new Set(gal.labels.map((l) => l.titleSize))].join(","));
  const boxes = gal.labels.map((l) => l.box).filter(Boolean);
  const crossing = boxes.filter((a, i) => boxes.some((b, j) => j > i && hits(a, b))).length;
  check(engine, vp.name, "sector label blocks do not overlap", boxes.length === 10 && crossing === 0, `${boxes.length} blocks, ${crossing} crossing`);
  const clipped = gal.labels.filter((l) => l.box && (l.box.x < 0 || l.box.y < 0 || l.box.x + l.box.w > gal.view.w || l.box.y + l.box.h > gal.view.h)).map((l) => l.sid);
  check(engine, vp.name, "sector labels are not clipped", clipped.length === 0, clipped.join(","));
  const blocked = gal.labels.flatMap((l) => l.box ? gal.keepOut.filter((k) => hits(l.box, k)).map((k) => `${l.sid}/${k.name}`) : []);
  check(engine, vp.name, "sector labels clear the controls, legend, hint and minimap", blocked.length === 0, blocked.join(" "));
  const onLabel = await page.evaluate(() => { const s = AtlasMap.api().scene, b = s.galaxyLabels()[0].box; return s.pick({ x: b.x + b.w / 2, y: b.y + b.h / 2 }); });
  check(engine, vp.name, "a label belongs to its sector for hover", onLabel && onLabel.kind === "sector" && onLabel.id === "silicon", JSON.stringify(onLabel));

  // trackpad swipe: small deltas in both axes pan, the page does not scroll, and a dead stop glides on
  if (vp.name === "desktop") {
    // the galaxy view is held centred, so swipe once zoomed into a sector
    await page.evaluate(() => AtlasMap.api().goSector("silicon")); await settle(page); await page.waitForTimeout(400);
    await centre(page);
    const y0 = await page.evaluate(() => scrollY);
    const c0 = await cam(page);
    const swipeFt = await frameTimes(page, async () => {
      for (let i = 0; i < 14; i++) { await page.mouse.wheel(14, 9); await page.waitForTimeout(16); }
      await page.waitForTimeout(40);
    });
    const c1 = await cam(page);
    await page.waitForTimeout(700);
    const c2 = await cam(page);
    check(engine, vp.name, "swipe pans right and down", c1.x > c0.x && c1.y > c0.y, `dx ${(c1.x - c0.x).toFixed(1)} dy ${(c1.y - c0.y).toFixed(1)}`);
    check(engine, vp.name, "swipe glides after release", Math.hypot(c2.x - c1.x, c2.y - c1.y) > 1, `glide ${Math.hypot(c2.x - c1.x, c2.y - c1.y).toFixed(1)}`);
    check(engine, vp.name, "page does not scroll under a swipe", (await page.evaluate(() => scrollY)) === y0);
    for (let i = 0; i < 10; i++) { await page.mouse.wheel(-12, -8); await page.waitForTimeout(16); }
    await page.waitForTimeout(400);
    const c3 = await cam(page);
    check(engine, vp.name, "swipe pans left and up", c3.x < c2.x && c3.y < c2.y);
    results.push({ engine, vp: vp.name, name: "frame times during swipe", ok: true, detail: JSON.stringify(swipeFt) });

    // pinch (ctrlKey) and mouse wheel both zoom toward the cursor
    await page.evaluate(() => { AtlasMap.api().goGalaxy(); }); await settle(page);
    const p = await centre(page);
    const k0 = (await cam(page)).k;
    const zoomFt = await frameTimes(page, async () => {
      for (let i = 0; i < 8; i++) {
        await page.evaluate(({ x, y }) => document.querySelector(".amap__canvas").dispatchEvent(new WheelEvent("wheel", { deltaY: -8, ctrlKey: true, clientX: x, clientY: y, bubbles: true, cancelable: true })), p);
        await page.waitForTimeout(16);
      }
      await page.waitForTimeout(500);
    });
    const k1 = (await cam(page)).k;
    check(engine, vp.name, "pinch zooms in", k1 > k0 * 1.2, `k ${k0.toFixed(3)} -> ${k1.toFixed(3)}`);
    await page.waitForTimeout(200);
    await page.mouse.wheel(0, 100); await page.waitForTimeout(600);
    const k2 = (await cam(page)).k;
    check(engine, vp.name, "mouse wheel zooms out", k2 < k1, `k ${k1.toFixed(3)} -> ${k2.toFixed(3)}`);
    results.push({ engine, vp: vp.name, name: "frame times during zoom", ok: true, detail: JSON.stringify(zoomFt) });
  }

  // sector close-up: nodes and their labels readable over the helmet
  await page.evaluate(() => AtlasMap.api().goSector("silicon")); await settle(page); await page.waitForTimeout(500);
  const labels = await page.evaluate(() => AtlasMap.api().scene.labelBoxes());
  const overlaps = labels.filter((a, i) => labels.some((b, j) => j > i && a.x < b.x + b.w && b.x < a.x + a.w && a.y < b.y + b.h && b.y < a.y + a.h)).length;
  check(engine, vp.name, "sector labels do not overlap", overlaps === 0 && labels.length > 8, `${labels.length} labels, ${overlaps} overlaps`);
  await page.screenshot({ path: `${OUT}/${tag}-silicon.png` });

  // spotlight: the company and every connection inside the frame
  for (const id of SPOTLIGHTS) {
    const flightFt = await frameTimes(page, async () => {
      await page.evaluate((cid) => AtlasMap.api().goCompany(cid), id);
      await settle(page); await page.waitForTimeout(1000);
    });
    const res = await page.evaluate(() => {
      const s = AtlasMap.api().scene, v = s.view(), sp = s.spotlight(), boxes = s.proxyBoxes();
      const card = document.querySelector(".pcard"), cr = card.hidden ? null : card.getBoundingClientRect(), hr = document.querySelector(".amap__canvas").getBoundingClientRect();
      const free = innerWidth > 900 && cr ? cr.left - hr.left : v.w;
      const out = boxes.filter((b) => b.x - b.r < 0 || b.y - b.r < 0 || b.x + b.r > free || b.y + b.r > v.h);
      return { n: boxes.length, want: 1 + sp.inPlace.length + sp.ring.length, ring: sp.ring.length, out: out.map((b) => b.id) };
    });
    check(engine, vp.name, `spotlight fits ${id}`, res.n === res.want && res.out.length === 0, JSON.stringify(res));
    if (vp.name === "desktop") results.push({ engine, vp: vp.name, name: `frame times during ${id} flight`, ok: true, detail: JSON.stringify(flightFt) });
    if (id === "oracle") await page.screenshot({ path: `${OUT}/${tag}-spotlight-oracle.png` });
  }

  // a team lights up its members
  await page.evaluate(() => AtlasMap.api().goTeam("nvidia")); await settle(page); await page.waitForTimeout(700);
  check(engine, vp.name, "team highlight", (await page.evaluate(() => AtlasMap.api().scene.debug().team)) === "nvidia" && /#t-nvidia$/.test(await page.url()));
  await page.screenshot({ path: `${OUT}/${tag}-team-nvidia.png` });

  // the galaxy's labels at common window sizes, and the map's places surviving a change of arrangement
  if (vp.name === "desktop") {
    const hit = (a, b) => a.x < b.x + b.w && b.x < a.x + a.w && a.y < b.y + b.h && b.y < a.y + a.h;
    await page.evaluate(() => { AtlasMap.api().goGalaxy(); }); await settle(page);
    // the fit depends on the label widths, so read it with the site's own font in place
    await page.waitForFunction(() => [...document.fonts].some((f) => f.status === "loaded" && f.weight === "600"), null, { timeout: 15000 }).catch(() => {});
    await page.waitForTimeout(400);
    for (const [width, height, wantFull] of [[1280, 720, true], [1366, 650, true], [1536, 730, true], [1440, 900, true], [1024, 768, true], [820, 1100, true], [390, 844, true], [360, 740, true], [844, 390, false], [667, 375, false]]) {
      await page.setViewportSize({ width, height });
      // the map stops drawing while it is out of sight, so bring it back into view before reading it
      await page.evaluate(() => { document.getElementById("atlas-map").scrollIntoView({ block: "center" }); });
      await page.waitForTimeout(700);
      const g = await page.evaluate(() => {
        const s = AtlasMap.api().scene, frame = document.querySelector(".amap__canvas").getBoundingClientRect();
        const keepOut = [...document.querySelectorAll(".amap__legend, .amap__mini, .amap__tools")].map((el) => { const r = el.getBoundingClientRect(); return { name: el.className, x: r.left - frame.left, y: r.top - frame.top, w: r.width, h: r.height }; }).filter((r) => r.w && r.h);
        return { labels: s.galaxyLabels(), view: s.view(), keepOut, font: [...document.fonts].some((f) => f.status === "loaded" && f.weight === "600") };
      });
      const b = g.labels.map((l) => l.box).filter(Boolean), size = `${width}x${height}`;
      const crossed = b.filter((x, i) => b.some((y, j) => j > i && hit(x, y))).length;
      const lines = new Set(g.labels.map((l) => (l.stats || "").split("\n").length));
      const blocked = g.labels.flatMap((l) => l.box ? g.keepOut.filter((k) => hit(l.box, k)).map((k) => `${l.sid}/${k.name}`) : []);
      const off = g.labels.filter((l) => l.box && (l.box.x < 0 || l.box.y < 0 || l.box.x + l.box.w > g.view.w || l.box.y + l.box.h > g.view.h)).map((l) => l.sid);
      check(engine, vp.name, `${size}: ten labels, none crossing`, b.length === 10 && crossed === 0, `${b.length} blocks, ${crossed} crossing`);
      check(engine, vp.name, `${size}: labels ${wantFull ? "show the top 3" : "all match"}`, lines.size === 1 && (!wantFull || lines.has(4)), `${[...lines].join()} lines in ${Math.round(g.view.w)}x${Math.round(g.view.h)}, ${g.font ? "site font" : "fallback font"}`);
      check(engine, vp.name, `${size}: labels unclipped and clear of the controls`, off.length === 0 && blocked.length === 0, [...off, ...blocked].join(" "));
    }
    // moving between the wide and narrow arrangements while somewhere on the map
    const onScreen = () => page.evaluate(() => { const s = AtlasMap.api().scene, v = s.view(), p = s.proxyBoxes(); return { n: p.length, inside: p.filter((b) => b.x >= 0 && b.y >= 0 && b.x <= v.w && b.y <= v.h).length }; });
    await page.setViewportSize({ width: vp.width, height: vp.height }); await page.waitForTimeout(450);
    await page.evaluate(() => { document.getElementById("atlas-map").scrollIntoView({ block: "center" }); });
    await page.evaluate(() => { AtlasMap.api().goCompany("nvidia"); }); await settle(page); await page.waitForTimeout(900);
    await page.setViewportSize({ width: 700, height: 900 }); await page.waitForTimeout(900);
    const narrowSpot = await onScreen();
    check(engine, vp.name, "spotlight stays on screen entering the narrow layout", narrowSpot.n > 1 && narrowSpot.inside === narrowSpot.n, JSON.stringify(narrowSpot));
    await page.setViewportSize({ width: vp.width, height: vp.height }); await page.waitForTimeout(900);
    const wideSpot = await onScreen();
    check(engine, vp.name, "spotlight stays on screen leaving the narrow layout", wideSpot.n > 1 && wideSpot.inside === wideSpot.n, JSON.stringify(wideSpot));
    await page.evaluate(() => { AtlasMap.api().goSector("cloud"); }); await settle(page); await page.waitForTimeout(400);
    await page.setViewportSize({ width: 700, height: 900 }); await page.waitForTimeout(700);
    const sectorView = await page.evaluate(() => { const s = AtlasMap.api().scene, c = s.cam(), t = s.sectorCam("cloud"); return Math.hypot(c.x - t.x, c.y - t.y); });
    check(engine, vp.name, "sector view follows the sector into the narrow layout", sectorView < 1, `off by ${sectorView.toFixed(1)}`);
    await page.setViewportSize({ width: vp.width, height: vp.height }); await page.waitForTimeout(500);
    await page.evaluate(() => { AtlasMap.api().goGalaxy(); }); await settle(page);
  }

  // full screen and back
  if (vp.name === "desktop") {
    await page.evaluate(() => { AtlasMap.api().goGalaxy(); });
    await page.click(".amap__full"); await page.waitForTimeout(600);
    const full = await page.evaluate(() => { const r = document.querySelector(".amap__stage").getBoundingClientRect(); return r.width >= innerWidth - 1 && r.height >= innerHeight - 1; });
    await page.click(".amap__full"); await page.waitForTimeout(600);
    const back = await page.evaluate(() => document.querySelector(".amap__stage").getBoundingClientRect().width < innerWidth * 0.9);
    check(engine, vp.name, "full screen opens and closes", full && back);
  }

  // the List still works, and the Map comes back from a deep link
  await page.click('.view__b[data-view="list"]'); await page.waitForTimeout(300);
  check(engine, vp.name, "list view shows", await page.evaluate(() => !document.getElementById("atlas-list").hidden && document.getElementById("atlas-map").hidden));
  check(engine, vp.name, "no console errors", errors.length === 0, errors.slice(0, 3).join(" | "));
  await page.close();
}

async function pageChecks(browser, engine, vp) {
  const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
  const errors = [];
  page.on("pageerror", (e) => errors.push(String(e)));
  page.on("console", (m) => { if (m.type() === "error") errors.push(m.text()); });
  const tag = `${engine}-${vp.name}`;
  await page.goto(`${BASE}/atlas/oracle.html`);
  const order = await page.evaluate(() => [...document.querySelectorAll(".pf > section")].map((s) => s.id));
  check(engine, vp.name, "profile: ratings directly below the hero", order[0] === "hero" && order[1] === "ratings", order.join(","));
  const wide = await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1);
  check(engine, vp.name, "profile: no sideways scroll", wide);
  await page.screenshot({ path: `${OUT}/${tag}-profile-oracle.png`, fullPage: true });
  await page.goto(`${BASE}/atlas/sector-silicon.html`);
  const rows = await page.evaluate(() => document.querySelectorAll(".st tbody tr").length);
  check(engine, vp.name, "standings: Silicon table", rows > 20, `${rows} rows`);
  await page.screenshot({ path: `${OUT}/${tag}-standings-silicon.png`, fullPage: true });
  await page.goto(`${BASE}/atlas/team-microsoft_openai.html`);
  const members = await page.evaluate(() => document.querySelectorAll(".st tbody tr").length);
  check(engine, vp.name, "team page: roster", members >= 3, `${members} members`);
  await page.screenshot({ path: `${OUT}/${tag}-team-page.png`, fullPage: true });
  check(engine, vp.name, "pages: no console errors", errors.length === 0, errors.slice(0, 3).join(" | "));
  await page.close();
}

// the homepage, Articles, Prologue and Atlas: the nav, the current page, and what each must still show
const NAV_PAGES = [["index.html", null], ["articles.html", "Articles"], ["ten-years.html", "Prologue"], ["tech-atlas.html", "Atlas"]];
async function siteChecks(browser, engine, vp) {
  const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
  const errors = [];
  page.on("pageerror", (e) => errors.push(String(e)));
  page.on("console", (m) => { if (m.type() === "error" && !IGNORE.test(m.text())) errors.push(m.text()); });
  const tag = `${engine}-${vp.name}`;
  for (const [file, current] of NAV_PAGES) {
    await page.goto(`${BASE}/${file}?check=${Date.now()}`);
    await page.waitForTimeout(500);
    const n = await page.evaluate(() => {
      const links = [...document.querySelectorAll(".sitenav__a")], box = (el) => el.getBoundingClientRect();
      const words = links.map((a) => a.querySelector(".sitenav__w").textContent);
      const marked = links.filter((a) => a.getAttribute("aria-current") === "page").map((a) => a.querySelector(".sitenav__w").textContent);
      const line = marked.length ? getComputedStyle(links.find((a) => a.getAttribute("aria-current")).querySelector(".sitenav__w")).borderBottomColor : "";
      const nav = box(document.querySelector(".sitenav")), back = document.querySelector(".back");
      const backHit = back ? (() => { const b = box(back); return b.left < nav.right && nav.left < b.right && links.some((a) => { const r = box(a); return r.left < b.right && b.left < r.right && r.top < b.bottom && b.top < r.bottom; }); })() : false;
      const head = document.querySelector(".atlas-head__k, .silohead__kicker, .articles .th__k");
      return { words, marked, line, tops: new Set(links.map((a) => Math.round(box(a).top))).size, backHit, gap: head ? box(head).top - nav.bottom : null,
               wide: document.documentElement.scrollWidth <= innerWidth, width: nav.width };
    });
    const name = file.replace(".html", "");
    check(engine, vp.name, `${name}: nav in order`, n.words.join() === "Prologue,Articles,Atlas", n.words.join());
    check(engine, vp.name, `${name}: current page marked`, current ? n.marked.join() === current && n.line !== "rgba(0, 0, 0, 0)" : n.marked.length === 0, `${n.marked} ${n.line}`);
    check(engine, vp.name, `${name}: nav stays on one line`, n.tops === 1);
    check(engine, vp.name, `${name}: nav clears the back link and heading`, !n.backHit && (n.gap === null || n.gap >= 0), `gap ${n.gap}`);
    check(engine, vp.name, `${name}: no sideways scroll`, n.wide);
    await page.screenshot({ path: `${OUT}/${tag}-${name}.png`, fullPage: file === "articles.html" });
    // WebKit on a Mac only tabs through links with Option held, as Safari does by default
    const tab = engine === "webkit" ? "Alt+Tab" : "Tab";
    await page.keyboard.press(tab); await page.keyboard.press(tab);
    const focus = await page.evaluate(() => document.activeElement.className);
    check(engine, vp.name, `${name}: nav reached by keyboard`, /sitenav__a/.test(focus), focus);
    if (file === "index.html") {
      const h = await page.evaluate(() => ({ sign: !!document.querySelector(".essay .tale__sign") && getComputedStyle(document.querySelector(".essay .tale__sign")).display !== "none",
        cards: document.querySelectorAll(".th__c").length, label: document.querySelector(".th__k").textContent, title: document.querySelector(".th__t").textContent, all: !!document.querySelector('a[href="articles.html"].th__all'), pod: document.querySelector(".spot__name").textContent }));
      check(engine, vp.name, "homepage: Francis's story is there", h.sign);
      check(engine, vp.name, "homepage: one featured Trojan Horse, the latest", h.cards === 1 && h.label === "Trojan Horse of the Week" && h.title === "Trading Copper for Light" && h.all, JSON.stringify(h));
      check(engine, vp.name, "homepage: podcast named", h.pod === "In The Belly");
      await page.evaluate(() => document.querySelector(".th").scrollIntoView()); await page.waitForTimeout(500);
      await page.screenshot({ path: `${OUT}/${tag}-home-featured.png` });
    }
  }
  check(engine, vp.name, "nav pages: no console errors", errors.length === 0, errors.slice(0, 3).join(" | "));
  await page.close();
}

// headless Chromium draws WebGL in software unless told to use the GPU, which would skew frame times
const LAUNCH = { chromium: { args: ["--use-angle=metal", "--ignore-gpu-blocklist"] }, webkit: {} };
for (const [engine, type] of [["chromium", chromium], ["webkit", webkit]]) {
  const browser = await type.launch(LAUNCH[engine]);
  for (const vp of VIEWPORTS) {
    try { await mapChecks(browser, engine, vp); } catch (e) { check(engine, vp.name, "map checks ran", false, String(e).slice(0, 300)); }
    try { await pageChecks(browser, engine, vp); } catch (e) { check(engine, vp.name, "page checks ran", false, String(e).slice(0, 300)); }
    try { await siteChecks(browser, engine, vp); } catch (e) { check(engine, vp.name, "site checks ran", false, String(e).slice(0, 300)); }
  }
  await browser.close();
}
for (const r of results) console.log(`${r.ok ? "PASS" : "FAIL"}  ${r.engine.padEnd(8)} ${r.vp.padEnd(7)} ${r.name}${r.detail ? "  " + r.detail : ""}`);
const failed = results.filter((r) => !r.ok).length;
console.log(`\n${results.length - failed} passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
