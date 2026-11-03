// Tests for assets/atlas-map-core.js. Run: node --test
import { test } from "node:test";
import assert from "node:assert/strict";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const C = require("../assets/atlas-map-core.js");

const VIEW = { w: 1000, h: 600 };
const NO_INSET = { top: 0, right: 0, bottom: 0, left: 0 };

test("flight time is held between 0.8 and 1.2 seconds, and is instant for reduced motion", () => {
  assert.equal(C.flightMs(100, false), 800);
  assert.equal(C.flightMs(5000, false), 1200);
  assert.equal(C.flightMs(1000, false), 1000);
  assert.equal(C.flightMs(1000, true), 0);
});

test("easing starts slow, ends slow and passes the middle", () => {
  assert.equal(C.easeInOut(0), 0);
  assert.equal(C.easeInOut(1), 1);
  assert.equal(C.easeInOut(0.5), 0.5);
  assert.ok(C.easeInOut(0.1) < 0.1 && C.easeInOut(0.9) > 0.9);
});

const box = (id, x, y, w, h, p, extra) => Object.assign({ id, p, alts: [{ x, y, w, h }] }, extra || {});

test("collide keeps higher priority labels and drops overlapping ones", () => {
  const shown = C.collide([box("a", 0, 0, 50, 10, 1), box("b", 20, 2, 50, 10, 5), box("c", 200, 0, 50, 10, 0)], VIEW, 2);
  assert.deepEqual([...shown.keys()].sort(), ["b", "c"]);
});

test("collide drops labels outside the view", () => {
  assert.equal(C.collide([box("a", -100, 0, 50, 10, 1)], VIEW, 0).size, 0);
});

test("collide keeps labels out of the reserved strips", () => {
  const shown = C.collide([box("top", 10, 10, 40, 10, 1), box("mid", 10, 300, 40, 10, 1)], { w: 1000, h: 600, top: 50, bottom: 40 }, 0);
  assert.deepEqual([...shown.keys()], ["mid"]);
});

test("collide tries the next position when the first one is taken", () => {
  const items = [box("big", 0, 0, 100, 20, 9),
                 { id: "small", p: 1, alts: [{ x: 10, y: 5, w: 40, h: 10 }, { x: 10, y: 40, w: 40, h: 10 }] }];
  const shown = C.collide(items, VIEW, 2);
  assert.equal(shown.get("small"), 1);
});

test("labels that must avoid nodes do, and others ignore them", () => {
  const nodes = [{ x: 0, y: 0, w: 20, h: 20 }];
  const shown = C.collide([box("row", 5, 5, 30, 10, 1, { avoid: true }), box("title", 5, 5, 30, 10, 1)], VIEW, 0, nodes);
  assert.equal(shown.has("row"), false);
  assert.equal(shown.has("title"), true);
});

test("a forced label is kept even when every position is taken", () => {
  const nodes = [{ x: 0, y: 0, w: 500, h: 500 }];
  const shown = C.collide([box("sel", 5, 5, 30, 10, 99, { avoid: true, force: true })], VIEW, 0, nodes);
  assert.equal(shown.get("sel"), 0);
});

test("no two kept labels overlap", () => {
  const items = Array.from({ length: 60 }, (_, i) => box(String(i), (i * 37) % 900, (i * 53) % 560, 70, 14, i % 7));
  const shown = C.collide(items, VIEW, 2);
  const kept = items.filter((b) => shown.has(b.id)).map((b) => b.alts[shown.get(b.id)]);
  for (const a of kept) for (const b of kept) {
    if (a === b) continue;
    const apart = a.x + a.w + 2 <= b.x || b.x + b.w + 2 <= a.x || a.y + a.h + 2 <= b.y || b.y + b.h + 2 <= a.y;
    assert.ok(apart, "two kept labels overlap");
  }
});

test("arc stops short of both nodes and points its arrow at the target", () => {
  const a = { x: 0, y: 0 }, b = { x: 100, y: 0 };
  const arc = C.arc(a, b, 10, 20, 0.2, 4);
  assert.ok(Math.hypot(arc.end.x - b.x, arc.end.y - b.y) >= 20 + 4 - 1e-9);
  assert.ok(Math.hypot(arc.start.x - a.x, arc.start.y - a.y) >= 10 + 4 - 1e-9);
  assert.ok(arc.dir.x > 0); // heading towards b
  assert.match(arc.d, /^M[-\d.]+ [-\d.]+ Q/);
});

test("arc bends the same way whichever end is first", () => {
  const p = { x: 0, y: 0 }, q = { x: 100, y: 0 };
  assert.equal(C.arc(p, q, 0, 0, 0.3, 0, "p", "q").ctrl.y, C.arc(q, p, 0, 0, 0.3, 0, "q", "p").ctrl.y);
});

test("tier finds the band an OVR falls in", () => {
  const tiers = [{ min: 95, label: "Generational" }, { min: 80, label: "Starter" }, { min: 40, label: "Prospect" }];
  assert.equal(C.tier(97, tiers), "Generational");
  assert.equal(C.tier(80, tiers), "Starter");
  assert.equal(C.tier(41, tiers), "Prospect");
  assert.equal(C.tier(null, tiers), null);
});

test("node radius grows with OVR and unrated companies get the small default", () => {
  assert.equal(C.nodeRadius(null), C.R_UNRATED);
  assert.ok(C.nodeRadius(99) > C.nodeRadius(70));
  assert.ok(C.nodeRadius(40) > C.R_UNRATED);
});

test("initials take the first letters of up to two words", () => {
  assert.equal(C.initials("Nvidia"), "NV");
  assert.equal(C.initials("Palo Alto Networks"), "PA");
  assert.equal(C.initials("Everpure (Pure Storage)"), "EV");
  assert.equal(C.initials("xAI (SpaceXAI)"), "XA");
});

test("stars are the same every time for the same seed", () => {
  assert.deepEqual(C.stars(5, 7), C.stars(5, 7));
  assert.notDeepEqual(C.stars(5, 7), C.stars(5, 8));
  for (const s of C.stars(50, 1)) assert.ok(s.x >= 0 && s.x < 1 && s.y >= 0 && s.y < 1);
});

test("semantic zoom: planets far out, companies close in, a blend between", () => {
  assert.equal(C.detail(1), 0);
  assert.equal(C.detail(10), 1);
  const mid = C.detail((C.SHOW.planetsUntil + C.SHOW.sectorsFrom) / 2);
  assert.ok(mid > 0 && mid < 1);
});

/* ---------------------------------------------------------- camera */
const V = { w: 800, h: 600 };
const near = (a, b, e = 1e-6) => Math.abs(a - b) < e;

test("screen and world round-trip", () => {
  const cam = { x: 100, y: -50, k: 2.5 };
  const w = C.toWorld(cam, V, C.toScreen(cam, V, { x: 7, y: 9 }));
  assert.ok(near(w.x, 7) && near(w.y, 9));
});

test("zooming around a point keeps that point under the cursor", () => {
  const cam = { x: 0, y: 0, k: 1 }, s = { x: 650, y: 120 };
  const before = C.toWorld(cam, V, s);
  const after = C.toWorld(C.zoomAround(cam, V, s, 3.7), V, s);
  assert.ok(near(before.x, after.x) && near(before.y, after.y));
});

test("fitCam centres a box and fits its tighter side", () => {
  const cam = C.fitCam([0, 0, 200, 100], V, 0, { min: 0.01, max: 100 });
  assert.deepEqual([cam.x, cam.y, cam.k], [100, 50, 4]);
});

test("clampCam holds the zoom limits and keeps the centre near the map", () => {
  const c = C.clampCam({ x: 9999, y: -9999, k: 50 }, [0, 0, 100, 100], { min: 1, max: 4 });
  assert.equal(c.k, 4);
  assert.ok(c.x <= 100 && c.y >= 0);
});

test("eased approach closes most of the gap in a few frames and never overshoots", () => {
  let v = 0;
  for (let i = 0; i < 6; i++) v = C.approach(v, 100, 16.7, 60);
  assert.ok(v > 75 && v < 100);
});

test("inertia slows smoothly and stops", () => {
  let v = { x: 2, y: -1 }, steps = 0;
  const first = C.glide(v, 16.7, 325);
  assert.ok(Math.hypot(first.x, first.y) < Math.hypot(2, 1));
  while (v && steps < 1000) { v = C.glide(v, 16.7, 325); steps++; }
  assert.ok(steps > 20 && steps < 400);
});

test("a flight starts and ends on its cameras, zooms out mid-way on a long jump, and has a duration", () => {
  const a = { x: 0, y: 0, k: 1 }, b = { x: 5000, y: 0, k: 1 };
  const f = C.flight(a, b, V);
  const s = f.at(0), e = f.at(1), m = f.at(0.5);
  assert.ok(near(s.x, 0) && near(e.x, 5000, 1e-6) && near(e.k, 1, 1e-9));
  assert.ok(m.k < 1);
  assert.ok(f.duration > 0);
});

test("a flight that only zooms still works", () => {
  const f = C.flight({ x: 10, y: 10, k: 1 }, { x: 10, y: 10, k: 4 }, V);
  assert.ok(near(f.at(1).k, 4, 1e-9) && near(f.at(0.5).x, 10));
});

/* ------------------------------------------------------- focus ring */
test("focus ring puts allies left, rivals right, backers above and backed below", () => {
  const pos = C.focusRing({ left: ["a"], right: ["r"], top: ["b"], bottom: ["d"] }, 200, 120);
  assert.ok(pos.a.x < 0 && Math.abs(pos.a.y) < 1e-9);
  assert.ok(pos.r.x > 0);
  assert.ok(pos.b.y < 0 && pos.d.y > 0);
});

test("focus ring keeps neighbours apart, even when one side is crowded", () => {
  const left = Array.from({ length: 9 }, (_, i) => "l" + i);
  const pos = C.focusRing({ left, right: ["r1", "r2"], top: ["t"], bottom: [] }, 180, 110);
  const pts = Object.values(pos);
  for (const p of pts) for (const q of pts) if (p !== q) assert.ok(Math.hypot(p.x - q.x, p.y - q.y) >= 110 * 0.95);
  for (const id of left) assert.ok(pos[id].x < 0, id + " should be on the left");
});

/* ----------------------------------------------------------- bundles */
test("bundles count relationships between home sectors, by kind", () => {
  const home = { a: "s1", b: "s2", c: "s2", d: "s1" };
  const edges = [{ a: "a", b: "b", group: "allies" }, { a: "c", b: "a", group: "backers" }, { a: "a", b: "d", group: "rivals" },
                 { a: "d", b: "c", group: "allies" }];
  const out = C.bundles(edges, home);
  assert.equal(out.length, 1);
  assert.deepEqual([out[0].a, out[0].b, out[0].count], ["s1", "s2", 3]);
  assert.deepEqual(out[0].by, { allies: 2, rivals: 0, backers: 1 });
  assert.equal(C.bundleText(out[0], { s1: "Silicon", s2: "Cloud" }), "Silicon ↔ Cloud: 2 ally, 1 backer");
});

/* -------------------------------------------------------- deep links */
const COS = new Set(["oracle", "nvidia"]), SECS = new Set(["silicon", "cloud"]);
test("deep links: companies and sectors open the map, old card links open the list", () => {
  assert.deepEqual(C.parseHash("#c-oracle", COS, SECS), { view: "map", company: "oracle" });
  assert.deepEqual(C.parseHash("#s-cloud", COS, SECS), { view: "map", sector: "cloud" });
  assert.deepEqual(C.parseHash("#sector-cloud", COS, SECS), { view: "list" });
  assert.deepEqual(C.parseHash("#c-silicon-accelerators-nvidia", COS, SECS), { view: "list" });
  assert.deepEqual(C.parseHash("", COS, SECS), { view: null });
  assert.deepEqual(C.parseHash("#c-nobody", COS, SECS), { view: null });
});

test("deep links are written back for the current place", () => {
  assert.equal(C.hashFor({ level: "company", selected: "oracle" }), "#c-oracle");
  assert.equal(C.hashFor({ level: "sector", sector: "cloud" }), "#s-cloud");
  assert.equal(C.hashFor({ level: "galaxy" }), "");
});

/* ------------------------------------------------------------- radar */
test("radar puts each attribute on its own spoke, unrated at the floor", () => {
  const pts = C.radar([99, 40, null, 70, 70, 70], 100);
  assert.equal(pts.length, 6);
  assert.ok(near(Math.hypot(pts[0].x, pts[0].y), 100, 1e-9));
  assert.ok(near(Math.hypot(pts[1].x, pts[1].y), C.RADAR_FLOOR * 100, 1e-9));
  assert.ok(near(Math.hypot(pts[2].x, pts[2].y), C.RADAR_FLOOR * 100, 1e-9));
  assert.ok(pts[0].y < 0); // first spoke points up
});

test("on narrow screens the ring is one ellipse that keeps each side's place", () => {
  const groups = { top: ["b1"], right: ["r1", "r2"], bottom: ["d1", "d2", "d3", "d4"], left: ["a1", "a2", "a3"] };
  const pos = C.ellipseRing(groups, 110, 190);
  assert.equal(Object.keys(pos).length, 10);
  assert.ok(pos.b1.y < -150);
  for (const id of ["r1", "r2"]) assert.ok(pos[id].x > 0, id);
  for (const id of ["a1", "a2", "a3"]) assert.ok(pos[id].x < 0, id);
  for (const p of Object.values(pos)) assert.ok(Math.abs((p.x / 110) ** 2 + (p.y / 190) ** 2 - 1) < 1e-9);
});

test("ellipse ring spreads neighbours evenly", () => {
  const pos = C.ellipseRing({ top: [], right: ["a", "b", "c", "d"], bottom: [], left: [] }, 100, 100);
  const pts = Object.values(pos);
  for (const p of pts) for (const q of pts) if (p !== q) assert.ok(Math.hypot(p.x - q.x, p.y - q.y) > 100);
});

/* ---------------------------------------------------- round 3: input */
const ev = (o) => Object.assign({ deltaX: 0, deltaY: 0, deltaMode: 0, ctrlKey: false }, o);

test("a pinch arrives as a wheel event with ctrlKey and always zooms", () => {
  assert.equal(C.wheelKind(ev({ deltaY: 3.5, ctrlKey: true }), null, 0), "pinch");
  assert.equal(C.wheelKind(ev({ deltaY: 3.5, ctrlKey: true }), { kind: "pan", t: 0 }, 50), "pinch");
});

test("line or page deltas come from a mouse wheel", () => {
  assert.equal(C.wheelKind(ev({ deltaY: 3, deltaMode: 1 }), null, 0), "wheel");
  assert.equal(C.wheelKind(ev({ deltaY: 1, deltaMode: 2 }), null, 0), "wheel");
});

test("a sideways delta, or small fractional ones, come from a trackpad swipe", () => {
  assert.equal(C.wheelKind(ev({ deltaX: 4, deltaY: 1 }), null, 0), "pan");
  assert.equal(C.wheelKind(ev({ deltaY: 2.5 }), null, 0), "pan");
  assert.equal(C.wheelKind(ev({ deltaY: -12 }), null, 0), "pan");
});

test("large whole-number steps come from a mouse wheel", () => {
  assert.equal(C.wheelKind(ev({ deltaY: 100 }), null, 0), "wheel");
  assert.equal(C.wheelKind(ev({ deltaY: -120 }), null, 0), "wheel");
});

test("wheelDeltaY, where the browser sends it, tells a trackpad from a mouse", () => {
  assert.equal(C.wheelKind(ev({ deltaY: 12, wheelDeltaY: -36 }), null, 0), "pan");
  assert.equal(C.wheelKind(ev({ deltaY: 4.000244140625, wheelDeltaY: -120 }), null, 0), "wheel");
  // Safari gives every wheel event the trackpad ratio, so a full notch still reads as a wheel
  assert.equal(C.wheelKind(ev({ deltaY: 100, wheelDeltaY: -300 }), null, 0), "wheel");
});

test("one gesture keeps its kind until the input rests", () => {
  const prev = { kind: "pan", t: 1000 };
  assert.equal(C.wheelKind(ev({ deltaY: 100 }), prev, 1050), "pan");
  assert.equal(C.wheelKind(ev({ deltaY: 100 }), prev, 1000 + C.GESTURE_REST_MS + 1), "wheel");
});

test("a swipe that stops abruptly gets a glide, and one the system already slowed does not", () => {
  const steady = [0, 16, 32, 48, 64].map((t) => ({ t, dx: 0, dy: 24 }));
  const v = C.swipeRelease(steady, 64 + 80);
  assert.ok(v && v.y > 1 && Math.abs(v.x) < 1e-9);
  const decayed = [24, 16, 9, 4, 1.5, 0.4].map((dy, i) => ({ t: i * 16, dx: 0, dy }));
  assert.equal(C.swipeRelease(decayed, 5 * 16 + 80), null);
  assert.equal(C.swipeRelease(steady, 64 + 10), null, "still swiping");
});

test("panning follows the swipe per frame and arrives without overshoot", () => {
  let left = { x: 0, y: 100 }, moved = 0;
  for (let i = 0; i < 30; i++) { const s = C.panStep(left, 16.7, false); moved += s.y; left = s.left; }
  assert.ok(Math.abs(moved - 100) < 0.5 && moved <= 100.0001);
  const instant = C.panStep({ x: 5, y: 7 }, 16.7, true);
  assert.deepEqual([instant.x, instant.y, instant.left.x, instant.left.y], [5, 7, 0, 0]);
});

/* ------------------------------------------------ round 3: spotlight */
const FRAME = { w: 1000, h: 600 };

test("spotlight fits every connection when they are close enough to read", () => {
  const plan = C.spotlightPlan({ x: 0, y: 0 }, { a: { x: 100, y: 0 }, b: { x: -50, y: 80 } }, FRAME, { read: 1, max: 4, pad: 60 });
  assert.deepEqual(plan.ring, []);
  assert.deepEqual(plan.inPlace.sort(), ["a", "b"]);
  assert.equal(plan.cam.x, 0); assert.equal(plan.cam.y, 0);
  assert.ok(plan.cam.k >= 1 && plan.cam.k <= 4);
  // every connection lands inside the frame with the padding to spare
  ["a", "b"].forEach((id) => {
    const p = C.toScreen(plan.cam, FRAME, { a: { x: 100, y: 0 }, b: { x: -50, y: 80 } }[id]);
    assert.ok(p.x >= 60 && p.x <= 940 && p.y >= 60 && p.y <= 540);
  });
});

test("a connection too far to read is pulled into the ring, and the zoom stays readable", () => {
  const plan = C.spotlightPlan({ x: 0, y: 0 }, { near: { x: 100, y: 0 }, far: { x: 9000, y: 0 } }, FRAME, { read: 1, max: 4, pad: 60 });
  assert.deepEqual(plan.ring, ["far"]);
  assert.deepEqual(plan.inPlace, ["near"]);
  assert.ok(plan.cam.k >= 1);
});

test("the spotlight centres the company in the part of the frame the card leaves free", () => {
  const plan = C.spotlightPlan({ x: 0, y: 0 }, {}, FRAME, { read: 1, max: 2, pad: 60, right: 400 });
  const s = C.toScreen(plan.cam, FRAME, { x: 0, y: 0 });
  assert.ok(Math.abs(s.x - 300) < 1e-6 && Math.abs(s.y - 300) < 1e-6);
});

test("team addresses open the map with that team highlighted", () => {
  const r = C.parseHash("#t-nvidia", new Set(["nvidia"]), new Set(["silicon"]), new Set(["nvidia", "google"]));
  assert.deepEqual(r, { view: "map", team: "nvidia" });
  assert.equal(C.hashFor({ level: "galaxy", team: "google" }), "#t-google");
  assert.deepEqual(C.parseHash("#t-nope", new Set(), new Set(), new Set(["google"])), { view: null });
});
