// The Atlas helmet: the traditional Greek helmet seen from the front, with no
// crest or plume. One design is shared by every sector. It is drawn in white and
// greys, so when the map tints it the shading becomes darker shades of the
// sector's colour: a lit dome, an engraved brow band, riveted edges and shaded
// cheek guards. Writes assets/images/helmets/helmet.svg.
//
//   node scripts/atlas-helmets/draw.js
const fs = require("fs"), path = require("path");
const OUT = path.join(__dirname, "..", "..", "assets", "images", "helmets");
const CX = 400;
const VIEW = { x: 184, y: 220, w: 432, h: 596 };   // the helmet's own bounds, plus a margin for the rim
const f = (v) => +v.toFixed(1);
const mirror = (p) => [2 * CX - p[0], p[1]];
const poly = (pts) => pts.map((p, i) => `${i ? "L" : "M"}${f(p[0])} ${f(p[1])}`).join(" ") + " Z";
const dot = (x, y, r) => `M${f(x - r)} ${f(y)} A${r} ${r} 0 1 0 ${f(x + r)} ${f(y)} A${r} ${r} 0 1 0 ${f(x - r)} ${f(y)} Z`;

// the outline: a dome, cheek guards that close to a T-shaped opening, and a nose guard
const DOME = { y: 436, r: 200 };
const RIGHT = [[600, 640], [488, 800], [456, 600], [456, 566], [572, 520], [572, 462], [426, 496], [422, 590]];
const NOSE_TIP = [CX, 634];
function shell() {
  const pts = [...RIGHT, NOSE_TIP, ...RIGHT.slice().reverse().map(mirror)];
  let d = `M${CX - DOME.r} ${DOME.y} A${DOME.r} ${DOME.r} 0 0 1 ${CX + DOME.r} ${DOME.y}`;
  pts.forEach((p) => { d += ` L${f(p[0])} ${f(p[1])}`; });
  return d + " Z";
}

// the brow band: a curved strip above the eyes, its edges two quadratic curves
const BAND = { top: [[200, 404], [CX, 450], [600, 404]], bottom: [[600, 444], [CX, 490], [200, 444]] };
const quad = (q, t) => [0, 1].map((k) => (1 - t) ** 2 * q[0][k] + 2 * t * (1 - t) * q[1][k] + t * t * q[2][k]);
const curve = (q) => `Q${q[1][0]} ${q[1][1]} ${q[2][0]} ${q[2][1]}`;
const band = () => `M${BAND.top[0][0]} ${BAND.top[0][1]} ${curve(BAND.top)} L${BAND.bottom[0][0]} ${BAND.bottom[0][1]} ${curve(BAND.bottom)} Z`;
const mid = (t) => { const a = quad(BAND.top, t), b = quad(BAND.bottom, 1 - t); return [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]; };

// the engraving: a running row of diamonds along the middle of the band, with a fine line at each edge
function engraving() {
  const n = 15, out = [];
  for (let i = 1; i < n; i++) {
    const t = i / n, [x, y] = mid(t), w = 9, h = 8;
    out.push(poly([[x, y - h], [x + w, y], [x, y + h], [x - w, y]]));
  }
  return out.join(" ");
}
const edgeLine = (q, dy) => `M${q[0][0]} ${q[0][1] + dy} Q${q[1][0]} ${q[1][1] + dy} ${q[2][0]} ${q[2][1] + dy}`;

// rivets: one at each end of the band, then down both edges of each cheek guard
function rivetPoints() {
  const pts = [];
  pts.push(mid(0.035), mid(0.965));
  const cheek = [[584, 470], [584, 520], [584, 572], [580, 624], [548, 690], [516, 740]];
  cheek.forEach((p) => { pts.push(p, mirror(p)); });
  [[470, 590], [476, 660], [494, 730]].forEach((p) => { pts.push(p, mirror(p)); });
  return pts;
}

// a crest-free ridge: a shallow keel line from the crown down to the band
const ridge = () => `M${CX} 240 Q${CX + 2} 330 ${CX} 446`;

function svg() {
  const rivets = rivetPoints();
  const rim = (w, c) => `<path d="${shell()}" fill="none" stroke="${c}" stroke-width="${w}" stroke-linejoin="round" clip-path="url(#in)"/>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${VIEW.x} ${VIEW.y} ${VIEW.w} ${VIEW.h}" width="${VIEW.w}" height="${VIEW.h}">
<defs>
<clipPath id="in"><path d="${shell()}"/></clipPath>
<linearGradient id="body" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="0.55" stop-color="#E4E4E4"/><stop offset="1" stop-color="#9C9C9C"/></linearGradient>
<radialGradient id="lit" cx="0.38" cy="0.3" r="0.45"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.95"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>
<linearGradient id="cheekR" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#7A7A7A" stop-opacity="0.7"/><stop offset="1" stop-color="#7A7A7A" stop-opacity="0"/></linearGradient>
<linearGradient id="cheekL" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7A7A7A" stop-opacity="0.7"/><stop offset="1" stop-color="#7A7A7A" stop-opacity="0"/></linearGradient>
<linearGradient id="band" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#D2D2D2"/></linearGradient>
</defs>
<path d="${shell()}" fill="url(#body)"/>
<g clip-path="url(#in)">
<ellipse cx="${CX}" cy="360" rx="190" ry="170" fill="url(#lit)"/>
<rect x="470" y="440" width="140" height="380" fill="url(#cheekR)"/>
<rect x="190" y="440" width="140" height="380" fill="url(#cheekL)"/>
<path d="${ridge()}" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round"/>
<path d="${ridge()}" fill="none" stroke="#8C8C8C" stroke-width="2.5" stroke-linecap="round" transform="translate(5 0)"/>
<path d="${band()}" fill="url(#band)"/>
<path d="${edgeLine(BAND.top, 6)}" fill="none" stroke="#6E6E6E" stroke-width="2.5"/>
<path d="${edgeLine(BAND.bottom.slice().reverse(), -6)}" fill="none" stroke="#6E6E6E" stroke-width="2.5"/>
<path d="${engraving()}" fill="#7C7C7C"/>
</g>
${rim(16, "#8A8A8A")}${rim(5, "#FFFFFF")}
<g>${rivets.map(([x, y]) => `<circle cx="${f(x)}" cy="${f(y)}" r="8.5" fill="#6E6E6E"/><circle cx="${f(x - 2)}" cy="${f(y - 2)}" r="4.5" fill="#FFFFFF"/>`).join("")}</g>
</svg>
`;
}

fs.mkdirSync(OUT, { recursive: true });
fs.writeFileSync(path.join(OUT, "helmet.svg"), svg());
console.log("helmet written");
