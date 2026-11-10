// The Atlas helmets: the traditional Greek helmet seen from the front, one solid
// piece shared by every sector, with a crest that says what the sector does.
// Drawn in white so the map can tint each one. Writes one SVG per sector.
//
//   node scripts/atlas-helmets/draw.js
const fs = require("fs"), path = require("path");
const OUT = path.join(__dirname, "..", "..", "assets", "images", "helmets");
const W = 800, H = 840, CX = 400;
const f = (v) => +v.toFixed(1);
const mirror = (p) => [2 * CX - p[0], p[1]];
const poly = (pts) => pts.map((p, i) => `${i ? "L" : "M"}${f(p[0])} ${f(p[1])}`).join(" ") + " Z";
const dot = (x, y, r) => `M${f(x - r)} ${f(y)} A${r} ${r} 0 1 0 ${f(x + r)} ${f(y)} A${r} ${r} 0 1 0 ${f(x - r)} ${f(y)} Z`;
const bar = (p, q, w) => {
  const dx = q[0] - p[0], dy = q[1] - p[1], l = Math.hypot(dx, dy), nx = (-dy / l) * (w / 2), ny = (dx / l) * (w / 2);
  return poly([[p[0] + nx, p[1] + ny], [q[0] + nx, q[1] + ny], [q[0] - nx, q[1] - ny], [p[0] - nx, p[1] - ny]]);
};

const DOME = { x: CX, y: 436, r: 200 };
const GAP = { x: CX, y: 436, r: 218 };   // every crest stands this far off the dome
const RIGHT = [[600, 640], [488, 800], [456, 600], [456, 566], [572, 520], [572, 462], [426, 496], [422, 590]];
const NOSE_TIP = [CX, 634];
function shell() {
  const pts = [...RIGHT, NOSE_TIP, ...RIGHT.slice().reverse().map(mirror)];
  let d = `M${2 * CX - (DOME.x + DOME.r)} ${DOME.y} A${DOME.r} ${DOME.r} 0 0 1 ${DOME.x + DOME.r} ${DOME.y}`;
  pts.forEach((p) => { d += ` L${f(p[0])} ${f(p[1])}`; });
  return d + " Z";
}

function hitCircles(a, b, pick) {
  const dx = b.x - a.x, dy = b.y - a.y, d = Math.hypot(dx, dy);
  const m = (a.r * a.r - b.r * b.r + d * d) / (2 * d), h = Math.sqrt(Math.max(0, a.r * a.r - m * m));
  const mx = a.x + (dx * m) / d, my = a.y + (dy * m) / d;
  return pick([mx + (h * dy) / d, my - (h * dx) / d], [mx - (h * dy) / d, my + (h * dx) / d]);
}
const upper = (p, q) => (p[1] < q[1] ? p : q), lefter = (p, q) => (p[0] < q[0] ? p : q), righter = (p, q) => (p[0] > q[0] ? p : q);
const onGap = (x) => GAP.y - Math.sqrt(GAP.r ** 2 - (x - CX) ** 2);
const foot = (half) => [[CX - half, onGap(CX - half)], [CX + half, onGap(CX + half)]];
const backTo = (p) => `A${GAP.r} ${GAP.r} 0 0 0 ${f(p[0])} ${f(p[1])} Z`;

// a crest whose base follows the dome: right is its right side from the foot up, mirrored for the left
function onDome(half, right, apex) {
  const [L, R] = foot(half);
  const pts = [L, ...right.map(mirror), ...(apex ? [apex] : []), ...right.slice().reverse(), R];
  return pts.map((p, i) => `${i ? "L" : "M"}${f(p[0])} ${f(p[1])}`).join(" ") + " " + backTo(L);
}

const TOP = { x: CX, y: 300, r: 256 }, FANX = 188, FOOT = 112;
const fanY = (x) => TOP.y - Math.sqrt(TOP.r ** 2 - (x - CX) ** 2);
const fanL = [CX - FANX, fanY(CX - FANX)], fanR = [CX + FANX, fanY(CX + FANX)];

function channel(line, w) {
  const a = [], b = [], n = line.length;
  const norm = (p, q) => { const dx = q[0] - p[0], dy = q[1] - p[1], l = Math.hypot(dx, dy); return [-dy / l, dx / l]; };
  for (let i = 0; i < n; i++) {
    const n0 = i ? norm(line[i - 1], line[i]) : norm(line[0], line[1]);
    const n1 = i < n - 1 ? norm(line[i], line[i + 1]) : n0;
    let mx = n0[0] + n1[0], my = n0[1] + n1[1]; const ml = Math.hypot(mx, my); mx /= ml; my /= ml;
    const k = (w / 2) / (mx * n0[0] + my * n0[1]);
    a.push([line[i][0] - mx * k, line[i][1] - my * k]);
    b.push([line[i][0] + mx * k, line[i][1] + my * k]);
  }
  return { a, b };
}

const CRESTS = {
  // circuit traces cut in from the top edge, each ending in a round via
  silicon() {
    const VIA = 18, [footL, footR] = foot(FOOT);
    const routes = [[[-146, 46], [-122, 70], [-122, 92]], [[-74, 66], [-74, 92], [-48, 118], [-48, 142]], [[0, 0], [0, 150]]];
    const lines = routes.map((r) => {
      const x0 = CX + r[0][0], y0 = fanY(x0);
      return [[x0, y0 - 2], ...r.map(([dx, dy]) => [CX + dx, y0 + dy])].filter((p, i, l) => !(i && p[0] === l[i - 1][0] && p[1] === l[i - 1][1]));
    });
    const all = [...lines];
    lines.slice(0, 2).reverse().forEach((l) => all.push(l.map(mirror)));
    let d = `M${f(footL[0])} ${f(footL[1])} L${f(fanL[0])} ${f(fanL[1])}`;
    all.forEach((line) => {
      const c = channel(line, 20), left = c.a[0][0] < c.b[0][0] ? c.a : c.b, right = left === c.a ? c.b : c.a;
      d += ` A${TOP.r} ${TOP.r} 0 0 1 ${f(left[0][0])} ${f(fanY(left[0][0]))}`;
      left.slice(1).forEach((p) => { d += ` L${f(p[0])} ${f(p[1])}`; });
      const e = right[right.length - 1];
      d += ` A${VIA} ${VIA} 0 1 0 ${f(e[0])} ${f(e[1])}`;
      right.slice(1, -1).reverse().forEach((p) => { d += ` L${f(p[0])} ${f(p[1])}`; });
      d += ` L${f(right[0][0])} ${f(fanY(right[0][0]))}`;
    });
    return [d + ` A${TOP.r} ${TOP.r} 0 0 1 ${f(fanR[0])} ${f(fanR[1])} L${f(footR[0])} ${f(footR[1])} ${backTo(footL)}`];
  },

  // a transmission tower with two crossarms and lattice windows
  infra() {
    const body = onDome(96, [[446, 152], [524, 152], [524, 130], [438, 130], [430, 92], [488, 92], [488, 74], [424, 74]], [CX, 30]);
    const windows = poly([[CX, 160], [430, 188], [CX, 208], [370, 188]]) + " " + poly([[CX, 96], [416, 114], [CX, 126], [384, 114]]);
    return [body + " " + windows];
  },

  // a billow of five circles resting on the dome
  cloud() {
    const c = [{ x: 236, y: 222, r: 56 }, { x: 302, y: 150, r: 68 }, { x: CX, y: 122, r: 80 }, { x: 498, y: 150, r: 68 }, { x: 564, y: 222, r: 56 }];
    const s = hitCircles(c[0], GAP, lefter), e = hitCircles(c[4], GAP, righter);
    let d = `M${f(s[0])} ${f(s[1])}`, from = s;
    c.forEach((k, i) => {
      const to = i < c.length - 1 ? hitCircles(k, c[i + 1], upper) : e;
      const ang = (p) => Math.atan2(p[1] - k.y, p[0] - k.x);
      let turn = ang(to) - ang(from); while (turn < 0) turn += 2 * Math.PI;
      d += ` A${k.r} ${k.r} 0 ${turn > Math.PI ? 1 : 0} 1 ${f(to[0])} ${f(to[1])}`;
      from = to;
    });
    return [d + " " + backTo(s)];
  },

  // a low fan carrying a chain of linked nodes
  models() {
    const [L, R] = foot(FOOT);
    const body = `M${f(L[0])} ${f(L[1])} L262 168 A300 300 0 0 1 538 168 L${f(R[0])} ${f(R[1])} ${backTo(L)}`;
    const nodes = [[226, 128, 18], [300, 82, 20], [CX, 56, 22], [500, 82, 20], [574, 128, 18]];
    const stems = [[[300, 82], [300, 150]], [[CX, 56], [CX, 140]], [[500, 82], [500, 150]], [[226, 128], [272, 165]], [[574, 128], [528, 165]]];
    const links = nodes.slice(1).map((n, i) => [[nodes[i][0], nodes[i][1]], [n[0], n[1]]]);
    return [body, ...[...stems, ...links].map(([p, q]) => bar(p, q, 11)), ...nodes.map(([x, y, r]) => dot(x, y, r))];
  },

  // code brackets around a slash
  software() {
    const left = [[216, 128], [300, 46], [344, 46], [262, 128], [344, 210], [300, 210]];
    return [poly(left), poly(left.map(mirror)), poly([[420, 46], [458, 46], [380, 210], [342, 210]])];
  },

  // a heater shield with a keyhole cut through it
  security() {
    const shield = `M${CX} 38 L548 66 L548 128 Q540 180 ${CX} 208 Q260 180 252 128 L252 66 Z`;
    const keyhole = dot(CX, 104, 24) + " " + poly([[388, 112], [412, 112], [420, 166], [380, 166]]);
    return [shield + " " + keyhole];
  },

  // signal arcs broadcast from a point
  internet() {
    const C = [CX, 190], a0 = -2.6, a1 = -0.54;
    const pt = (a, r) => [C[0] + r * Math.cos(a), C[1] + r * Math.sin(a)];
    const band = (ri, ro) => {
      const [p, q, u, v] = [pt(a0, ro), pt(a1, ro), pt(a1, ri), pt(a0, ri)];
      return `M${f(p[0])} ${f(p[1])} A${ro} ${ro} 0 0 1 ${f(q[0])} ${f(q[1])} L${f(u[0])} ${f(u[1])} A${ri} ${ri} 0 0 0 ${f(v[0])} ${f(v[1])} Z`;
    };
    return [dot(C[0], C[1], 24), band(52, 72), band(94, 114), band(136, 156)];
  },

  // a rounded device frame with its screen cut out
  devices() {
    const rect = (x0, y0, x1, y1, r) => `M${x0 + r} ${y0} H${x1 - r} A${r} ${r} 0 0 1 ${x1} ${y0 + r} V${y1 - r} A${r} ${r} 0 0 1 ${x1 - r} ${y1} H${x0 + r} A${r} ${r} 0 0 1 ${x0} ${y1 - r} V${y0 + r} A${r} ${r} 0 0 1 ${x0 + r} ${y0} Z`;
    return [rect(256, 52, 544, 200, 34) + " " + rect(280, 76, 520, 176, 14)];
  },

  // half a coin behind the dome, its edge milled, one inner ring
  fintech() {
    const C = { x: CX, y: 236, r: 196 }, T = 9, N = 38;
    const s = hitCircles(C, GAP, lefter), e = hitCircles(C, GAP, righter);
    const a0 = Math.atan2(s[1] - C.y, s[0] - C.x), a1 = Math.atan2(e[1] - C.y, e[0] - C.x) + 2 * Math.PI, step = (a1 - a0) / (2 * N + 1);
    const pt = (a, r) => [C.x + r * Math.cos(a), C.y + r * Math.sin(a)];
    let d = `M${f(s[0])} ${f(s[1])}`;
    for (let i = 0; i <= 2 * N; i++) {
      const r = i % 2 ? C.r - T : C.r, a = a0 + step * (i + 1), end = pt(a, r);
      d += ` A${r} ${r} 0 0 1 ${f(end[0])} ${f(end[1])}`;
      if (i < 2 * N) { const next = pt(a, i % 2 ? C.r : C.r - T); d += ` L${f(next[0])} ${f(next[1])}`; }
    }
    d += " " + backTo(s);
    const ro = 150, ri = 136, ring = [a0 + 0.42, a1 - 0.42];
    const [p, q] = [pt(ring[0], ro), pt(ring[1], ro)], [u, v] = [pt(ring[1], ri), pt(ring[0], ri)];
    return [d + ` M${f(p[0])} ${f(p[1])} A${ro} ${ro} 0 0 1 ${f(q[0])} ${f(q[1])} L${f(u[0])} ${f(u[1])} A${ri} ${ri} 0 0 0 ${f(v[0])} ${f(v[1])} Z`];
  },

  // a crown of three points, each tipped with a ball
  backers() {
    const body = onDome(140, [[568, 84], [482, 150]], [CX, 44]);
    return [body, dot(232, 74, 14), dot(CX, 34, 14), dot(568, 74, 14)];
  },
};

fs.mkdirSync(OUT, { recursive: true });
Object.entries(CRESTS).forEach(([id, crest]) => {
  const body = [shell(), ...crest()].map((d) => `<path d="${d}" fill-rule="evenodd"/>`).join("");
  fs.writeFileSync(path.join(OUT, `${id}.svg`), `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}"><g fill="#FFFFFF">${body}</g></svg>\n`);
});
console.log(Object.keys(CRESTS).length, "helmets written");
