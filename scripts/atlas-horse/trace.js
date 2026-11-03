// Trace the homepage horse (assets/images/horse-light.png, the site's own art) into
// line-work: the silhouette outline, the shards, and the engraved grooves (ribs,
// spine strap, leg edges). Writes JSON of polylines in a 0..W x 0..H box.
const fs = require("fs"), zlib = require("zlib");
const [src, out, gt] = process.argv.slice(2);
const GT = +(gt || 0.15), SD = +(process.argv[5] || 0.08);

function decodePNG(buf) {
  let p = 8, w, h, idat = [];
  while (p < buf.length) {
    const len = buf.readUInt32BE(p), type = buf.toString("ascii", p + 4, p + 8), data = buf.subarray(p + 8, p + 8 + len);
    if (type === "IHDR") { w = data.readUInt32BE(0); h = data.readUInt32BE(4); if (data[8] !== 8 || data[9] !== 6 || data[12]) throw new Error("need 8-bit RGBA, no interlace"); }
    if (type === "IDAT") idat.push(data);
    p += 12 + len;
  }
  const raw = zlib.inflateSync(Buffer.concat(idat)), bpp = 4, stride = w * bpp, px = Buffer.alloc(h * stride);
  for (let y = 0; y < h; y++) {
    const f = raw[y * (stride + 1)], row = raw.subarray(y * (stride + 1) + 1, (y + 1) * (stride + 1));
    for (let x = 0; x < stride; x++) {
      const a = x >= bpp ? px[y * stride + x - bpp] : 0, b = y ? px[(y - 1) * stride + x] : 0, c = x >= bpp && y ? px[(y - 1) * stride + x - bpp] : 0;
      let v = row[x];
      if (f === 1) v += a; else if (f === 2) v += b; else if (f === 3) v += (a + b) >> 1;
      else if (f === 4) { const pp = a + b - c, pa = Math.abs(pp - a), pb = Math.abs(pp - b), pc = Math.abs(pp - c); v += pa <= pb && pa <= pc ? a : pb <= pc ? b : c; }
      px[y * stride + x] = v & 255;
    }
  }
  return { w, h, px };
}

const img = decodePNG(fs.readFileSync(src));
const S = 2;                                  // work at half resolution
const W = Math.floor(img.w / S), H = Math.floor(img.h / S);
const A = new Float32Array(W * H);
for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
  let s = 0;
  for (let j = 0; j < S; j++) for (let i = 0; i < S; i++) s += img.px[((y * S + j) * img.w + x * S + i) * 4 + 3];
  A[y * W + x] = s / (S * S) / 255;
}
function boxMean(src, r) {
  const I = new Float64Array((W + 1) * (H + 1)), o = new Float32Array(W * H);
  for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) I[(y + 1) * (W + 1) + x + 1] = src[y * W + x] + I[y * (W + 1) + x + 1] + I[(y + 1) * (W + 1) + x] - I[y * (W + 1) + x];
  for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
    const x0 = Math.max(0, x - r), x1 = Math.min(W, x + r + 1), y0 = Math.max(0, y - r), y1 = Math.min(H, y + r + 1);
    o[y * W + x] = (I[y1 * (W + 1) + x1] - I[y0 * (W + 1) + x1] - I[y1 * (W + 1) + x0] + I[y0 * (W + 1) + x0]) / ((x1 - x0) * (y1 - y0));
  }
  return o;
}

// ---- silhouette: a lightly blurred mask, so engraving gaps do not split the body
const B = boxMean(A, 2), M = new Uint8Array(W * H);
for (let i = 0; i < W * H; i++) M[i] = B[i] > 0.28 ? 1 : 0;

// marching squares, one closed loop per component boundary
function contours(mask) {
  const seen = new Set(), loops = [];
  const at = (x, y) => (x >= 0 && y >= 0 && x < W && y < H ? mask[y * W + x] : 0);
  const code = (x, y) => (at(x, y) << 3) | (at(x + 1, y) << 2) | (at(x + 1, y + 1) << 1) | at(x, y + 1);
  // edge midpoints for each cell case, walked as directed segments
  const E = { t: [0.5, 0], r: [1, 0.5], b: [0.5, 1], l: [0, 0.5] };
  const SEG = { 1: [["l", "b"]], 2: [["b", "r"]], 3: [["l", "r"]], 4: [["r", "t"]], 5: [["l", "t"], ["r", "b"]], 6: [["b", "t"]], 7: [["l", "t"]],
                8: [["t", "l"]], 9: [["t", "b"]], 10: [["t", "r"], ["b", "l"]], 11: [["t", "r"]], 12: [["r", "l"]], 13: [["r", "b"]], 14: [["b", "l"]] };
  const next = new Map();
  for (let y = -1; y < H; y++) for (let x = -1; x < W; x++) {
    const c = code(x, y);
    (SEG[c] || []).forEach(([a, b]) => {
      const k = (p) => `${(x + E[p][0]).toFixed(1)},${(y + E[p][1]).toFixed(1)}`;
      next.set(k(a), k(b));
    });
  }
  for (const start of next.keys()) {
    if (seen.has(start)) continue;
    const loop = []; let k = start;
    while (k && !seen.has(k)) { seen.add(k); const [x, y] = k.split(",").map(Number); loop.push([x, y]); k = next.get(k); }
    if (loop.length > 6) loops.push(loop);
  }
  return loops;
}
function area(l) { let a = 0; for (let i = 0; i < l.length; i++) { const p = l[i], q = l[(i + 1) % l.length]; a += p[0] * q[1] - q[0] * p[1]; } return a / 2; }
function simplify(pts, tol, closed) {
  if (pts.length < 3) return pts;
  if (closed) {
    // split a loop at its farthest point from the start, then simplify each half
    let far = 0, fd = 0;
    pts.forEach((p, i) => { const d = Math.hypot(p[0] - pts[0][0], p[1] - pts[0][1]); if (d > fd) { fd = d; far = i; } });
    const a = simplify(pts.slice(0, far + 1), tol, false), b = simplify(pts.slice(far), tol, false);
    return a.concat(b.slice(1));
  }
  const keep = new Uint8Array(pts.length); keep[0] = keep[pts.length - 1] = 1;
  const st = [[0, pts.length - 1]];
  while (st.length) {
    const [a, b] = st.pop(); let md = 0, mi = -1;
    const [ax, ay] = pts[a], [bx, by] = pts[b], dx = bx - ax, dy = by - ay, L = Math.hypot(dx, dy) || 1;
    for (let i = a + 1; i < b; i++) { const d = Math.abs((pts[i][0] - ax) * dy - (pts[i][1] - ay) * dx) / L; if (d > md) { md = d; mi = i; } }
    if (md > tol) { keep[mi] = 1; st.push([a, mi], [mi, b]); }
  }
  return pts.filter((_, i) => keep[i]);
}
const loops = contours(M).map((l) => ({ pts: l, a: Math.abs(area(l)) })).sort((p, q) => q.a - p.a);
const body = loops[0];
const outline = [simplify(body.pts.concat([body.pts[0]]), 1.1, true)];
const holes = loops.slice(1).filter((l) => l.a > 40 && l.a < body.a * 0.02 && insideBody(l.pts[0]));
const shards = loops.slice(1).filter((l) => l.a > 6 && !insideBody(l.pts[0])).map((l) => simplify(l.pts.concat([l.pts[0]]), 0.9, true));
function insideBody(p) {
  let c = false; const P = body.pts;
  for (let i = 0, j = P.length - 1; i < P.length; j = i++) {
    if ((P[i][1] > p[1]) !== (P[j][1] > p[1]) && p[0] < (P[j][0] - P[i][0]) * (p[1] - P[i][1]) / (P[j][1] - P[i][1]) + P[i][0]) c = !c;
  }
  return c;
}

// ---- grooves: ink much fainter than its surroundings, deep inside the silhouette
const Mb = boxMean(Float32Array.from(M), 3), L6 = boxMean(A, 5), G = new Uint8Array(W * H);
for (let i = 0; i < W * H; i++) G[i] = Mb[i] > 0.9 && L6[i] - A[i] > GT ? 1 : 0;
// Zhang-Suen thinning to one-pixel lines
(function thin() {
  let changed = true;
  const g = (x, y) => (x >= 0 && y >= 0 && x < W && y < H ? G[y * W + x] : 0);
  while (changed) {
    changed = false;
    for (let pass = 0; pass < 2; pass++) {
      const del = [];
      for (let y = 1; y < H - 1; y++) for (let x = 1; x < W - 1; x++) {
        if (!G[y * W + x]) continue;
        const n = [g(x, y - 1), g(x + 1, y - 1), g(x + 1, y), g(x + 1, y + 1), g(x, y + 1), g(x - 1, y + 1), g(x - 1, y), g(x - 1, y - 1)];
        const b = n.reduce((s, v) => s + v, 0); if (b < 2 || b > 6) continue;
        let a = 0; for (let i = 0; i < 8; i++) if (!n[i] && n[(i + 1) % 8]) a++;
        if (a !== 1) continue;
        if (pass === 0 ? n[0] * n[2] * n[4] || n[2] * n[4] * n[6] : n[0] * n[2] * n[6] || n[0] * n[4] * n[6]) continue;
        del.push(y * W + x);
      }
      del.forEach((i) => { G[i] = 0; }); if (del.length) changed = true;
    }
  }
})();
// walk the thinned pixels into polylines
const used = new Uint8Array(W * H), lines = [];
const nb = (i) => { const x = i % W, y = (i / W) | 0, o = []; for (let dy = -1; dy <= 1; dy++) for (let dx = -1; dx <= 1; dx++) { if (!dx && !dy) continue; const xx = x + dx, yy = y + dy; if (xx >= 0 && yy >= 0 && xx < W && yy < H && G[yy * W + xx]) o.push(yy * W + xx); } return o; };
const ends = []; for (let i = 0; i < W * H; i++) if (G[i] && nb(i).length === 1) ends.push(i);
function walk(s) {
  const path = [s]; used[s] = 1; let cur = s;
  for (;;) { const n = nb(cur).filter((j) => !used[j]); if (!n.length) break; cur = n[0]; used[cur] = 1; path.push(cur); }
  return path.map((i) => [i % W, (i / W) | 0]);
}
ends.forEach((s) => { if (!used[s]) { const p = walk(s); if (p.length > 14) lines.push(simplify(p, 1.2, false)); } });

// ---- slats: in each column, dips in ink between bright bands, linked across columns
const HB = new Float32Array(W * H);
for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
  let s = 0, n = 0; for (let dx = -3; dx <= 3; dx++) { const xx = x + dx; if (xx >= 0 && xx < W) { s += A[y * W + xx]; n++; } } HB[y * W + x] = s / n;
}
const pts = [];
for (let x = 0; x < W; x += 2) for (let y = 4; y < H - 4; y++) {
  const i = y * W + x; if (Mb[i] < 0.95) continue;
  const v = HB[i]; let lo = true, up = 0, dn = 0;
  for (let k = 1; k <= 4; k++) { if (HB[i - k * W] < v || HB[i + k * W] < v) lo = false; up = Math.max(up, HB[i - k * W]); dn = Math.max(dn, HB[i + k * W]); }
  if (lo && Math.min(up, dn) - v > SD) pts.push([x, y]);
}
const byX = new Map(); pts.forEach((p) => { if (!byX.has(p[0])) byX.set(p[0], []); byX.get(p[0]).push(p); });
const chains = [], open = [];
[...byX.keys()].sort((a, b) => a - b).forEach((x) => {
  const col = byX.get(x), taken = new Set();
  open.forEach((c) => {
    const last = c[c.length - 1]; if (x - last[0] > 4) { c.done = true; return; }
    let best = null; col.forEach((p, j) => { if (!taken.has(j) && Math.abs(p[1] - last[1]) <= 2 && (!best || Math.abs(p[1] - last[1]) < Math.abs(best[0][1] - last[1]))) best = [p, j]; });
    if (best) { c.push(best[0]); taken.add(best[1]); }
  });
  for (let i = open.length - 1; i >= 0; i--) if (open[i].done) { chains.push(open.splice(i, 1)[0]); }
  col.forEach((p, j) => { if (!taken.has(j)) open.push([p]); });
});
chains.push(...open);
const slats = chains.filter((c) => c.length >= 9).map((c) => simplify(c, 1, false));

const scale = (l) => l.map(([x, y]) => [+(x * S).toFixed(1), +(y * S).toFixed(1)]);
fs.writeFileSync(out, JSON.stringify({ w: img.w, h: img.h, outline: outline.map(scale), shards: shards.map(scale),
  holes: holes.map((l) => scale(simplify(l.pts.concat([l.pts[0]]), 0.9, true))), grooves: lines.map(scale), slats: slats.map(scale) }));
console.log("outline pts", outline[0].length, "shards", shards.length, "holes", holes.length, "grooves", lines.length,
            "groove pts", lines.reduce((s, l) => s + l.length, 0), "slats", slats.length);
