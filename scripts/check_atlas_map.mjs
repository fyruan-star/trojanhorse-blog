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
  await page.waitForFunction(() => window.AtlasMap && window.AtlasMap.api() && window.AtlasMap.api().scene.debug().horses > 0, null, { timeout: 15000 });
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
  check(engine, vp.name, "nine horses drawn", dbg.horses === 9, `horses ${dbg.horses}`);
  await page.screenshot({ path: `${OUT}/${tag}-galaxy.png` });

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
    await page.evaluate(() => AtlasMap.api().goGalaxy()); await settle(page);
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

  // sector close-up: nodes and their labels readable over the horse
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

  // full screen and back
  if (vp.name === "desktop") {
    await page.evaluate(() => AtlasMap.api().goGalaxy());
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

// headless Chromium draws WebGL in software unless told to use the GPU, which would skew frame times
const LAUNCH = { chromium: { args: ["--use-angle=metal", "--ignore-gpu-blocklist"] }, webkit: {} };
for (const [engine, type] of [["chromium", chromium], ["webkit", webkit]]) {
  const browser = await type.launch(LAUNCH[engine]);
  for (const vp of VIEWPORTS) {
    try { await mapChecks(browser, engine, vp); } catch (e) { check(engine, vp.name, "map checks ran", false, String(e).slice(0, 300)); }
    try { await pageChecks(browser, engine, vp); } catch (e) { check(engine, vp.name, "page checks ran", false, String(e).slice(0, 300)); }
  }
  await browser.close();
}
for (const r of results) console.log(`${r.ok ? "PASS" : "FAIL"}  ${r.engine.padEnd(8)} ${r.vp.padEnd(7)} ${r.name}${r.detail ? "  " + r.detail : ""}`);
const failed = results.filter((r) => !r.ok).length;
console.log(`\n${results.length - failed} passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
