// Tests for assets/atlas-map-core.js. Run: node --test
import { test } from "node:test";
import assert from "node:assert/strict";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const C = require("../assets/atlas-map-core.js");

const VIEW = { w: 1000, h: 600 };
const NO_INSET = { top: 0, right: 0, bottom: 0, left: 0 };

test("fit centres a box and scales it to the tighter side", () => {
  const t = C.fit([0, 0, 200, 100], VIEW, NO_INSET, 0, { min: 0.01, max: 100 });
  assert.equal(t.k, 5); // 1000/200 = 5, 600/100 = 6
  assert.equal(t.x + t.k * 100, 500); // box centre lands on view centre
  assert.equal(t.y + t.k * 50, 300);
});

test("fit leaves room for the card panel", () => {
  const t = C.fit([0, 0, 100, 100], VIEW, { top: 0, right: 400, bottom: 0, left: 0 }, 0, { min: 0.01, max: 100 });
  assert.equal(t.x + t.k * 50, 300); // centre of the 600px left of the panel
});

test("fit respects the zoom limits", () => {
  assert.equal(C.fit([0, 0, 1, 1], VIEW, NO_INSET, 0, { min: 0.1, max: 4 }).k, 4);
});

test("centre puts a point in the middle of the free area", () => {
  const t = C.centre({ x: 10, y: 20 }, 2, VIEW, { top: 0, right: 0, bottom: 300, left: 0 });
  assert.deepEqual([t.x + 2 * 10, t.y + 2 * 20], [500, 150]);
});

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

test("labels show by zoom: sectors far out, companies close in", () => {
  assert.deepEqual(C.labelsAt(1), { tiers: true, sectors: true, rows: false, companies: false });
  assert.equal(C.labelsAt(3).companies, true);
  assert.equal(C.labelsAt(3).sectors, false);
});
