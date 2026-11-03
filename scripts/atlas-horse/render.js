// Turn the traced polylines into the Atlas horse: constellation line-work in white
// (the map tints it per sector). Writes one SVG.
const fs = require("fs");
const [src, out] = process.argv.slice(2);
const d = JSON.parse(fs.readFileSync(src));
const f = (v) => +v.toFixed(1);

function smooth(pts, closed) {
  const p = closed ? [pts[pts.length - 2], ...pts, pts[1]] : [pts[0], ...pts, pts[pts.length - 1]];
  let s = `M${f(p[1][0])} ${f(p[1][1])}`;
  for (let i = 1; i < p.length - 2; i++) {
    const [a, b, c, e] = [p[i - 1], p[i], p[i + 1], p[i + 2]];
    s += ` C${f(b[0] + (c[0] - a[0]) / 6)} ${f(b[1] + (c[1] - a[1]) / 6)} ${f(c[0] - (e[0] - b[0]) / 6)} ${f(c[1] - (e[1] - b[1]) / 6)} ${f(c[0])} ${f(c[1])}`;
  }
  return s;
}
function turn(a, b, c) {
  const u = Math.atan2(b[1] - a[1], b[0] - a[0]), v = Math.atan2(c[1] - b[1], c[0] - b[0]);
  let t = Math.abs(v - u); if (t > Math.PI) t = 2 * Math.PI - t; return t;
}
function len(l) { let s = 0; for (let i = 1; i < l.length; i++) s += Math.hypot(l[i][0] - l[i - 1][0], l[i][1] - l[i - 1][1]); return s; }

// a slat gap becomes the rib line through its middle: its long axis, bent with the gap
function centreline(poly) {
  const n = poly.length, cx = poly.reduce((s, p) => s + p[0], 0) / n, cy = poly.reduce((s, p) => s + p[1], 0) / n;
  let sxx = 0, syy = 0, sxy = 0;
  poly.forEach(([x, y]) => { sxx += (x - cx) ** 2; syy += (y - cy) ** 2; sxy += (x - cx) * (y - cy); });
  const ang = 0.5 * Math.atan2(2 * sxy, sxx - syy), ux = Math.cos(ang), uy = Math.sin(ang);
  const proj = poly.map(([x, y]) => ({ t: (x - cx) * ux + (y - cy) * uy, s: -(x - cx) * uy + (y - cy) * ux }));
  const t0 = Math.min(...proj.map((p) => p.t)), t1 = Math.max(...proj.map((p) => p.t));
  const width = Math.max(...proj.map((p) => Math.abs(p.s))) * 2;
  if (t1 - t0 < 2.2 * width || t1 - t0 < 24) return null;
  const k = 6, line = [];
  for (let i = 0; i <= k; i++) {
    const t = t0 + (t1 - t0) * (0.04 + 0.92 * i / k), near = proj.filter((p) => Math.abs(p.t - t) < (t1 - t0) / k);
    const s = near.length ? near.reduce((a, p) => a + p.s, 0) / near.length : 0;
    line.push([cx + t * ux - s * uy, cy + t * uy + s * ux]);
  }
  return line;
}

const body = [];
// the outline, drawn twice: a fine line and a soft wide one under it, like an engraved edge
const outline = d.outline[0];
body.push(`<path d="${smooth(outline, true)}" stroke-width="7" opacity=".12"/>`);
body.push(`<path d="${smooth(outline, true)}" stroke-width="2.2" opacity=".92"/>`);
const ribs = d.holes.map(centreline).filter(Boolean);
ribs.forEach((r) => body.push(`<path d="${smooth(r, false)}" stroke-width="2" opacity=".7"/>`));
(d.slats || []).forEach((g) => body.push(`<path d="${smooth(g, false)}" stroke-width="1.6" opacity=".62"/>`));
d.grooves.filter((g) => len(g) > 36).forEach((g) => body.push(`<path d="${smooth(g, false)}" stroke-width="1.4" opacity=".45"/>`));
d.shards.forEach((s) => body.push(`<path d="${smooth(s, true)}" stroke-width="1.6" opacity=".75"/>`));

// stars where the outline turns sharply, spaced out, plus one in each larger shard
const stars = [];
for (let i = 1; i < outline.length - 1; i++) {
  const t = turn(outline[i - 1], outline[i], outline[i + 1]);
  if (t > 0.75 && stars.every((s) => Math.hypot(s[0] - outline[i][0], s[1] - outline[i][1]) > 46)) stars.push([...outline[i], t]);
}
ribs.forEach((r) => [r[0], r[r.length - 1]].forEach((p) => { if (stars.every((s) => Math.hypot(s[0] - p[0], s[1] - p[1]) > 30)) stars.push([...p, 0.5]); }));
const dots = stars.map(([x, y, t]) => {
  const r = t > 1.4 ? 4.6 : t > 1 ? 3.6 : 2.8;
  return `<circle cx="${f(x)}" cy="${f(y)}" r="${r * 2.6}" opacity=".14"/><circle cx="${f(x)}" cy="${f(y)}" r="${r}"/>`;
});
d.shards.forEach((s) => {
  if (len(s) < 40) return;
  const cx = s.reduce((a, p) => a + p[0], 0) / s.length, cy = s.reduce((a, p) => a + p[1], 0) / s.length;
  dots.push(`<circle cx="${f(cx)}" cy="${f(cy)}" r="2.2" opacity=".8"/>`);
});

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${d.w} ${d.h}" width="${d.w}" height="${d.h}">` +
  `<g fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round">${body.join("")}</g>` +
  `<g fill="#FFFFFF" stroke="none">${dots.join("")}</g></svg>\n`;
fs.writeFileSync(out, svg);
console.log("ribs", ribs.length, "stars", stars.length, "bytes", svg.length);
