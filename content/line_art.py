"""Hand-drawn line art, generated as inline SVG.

The first version of this looked like CAD: perfect arcs, uniform stroke, every
line drawn exactly once. Pencil does none of those things. So every mark here
goes through the same treatment. It is sampled into points, each point is
nudged off true, the points are smoothed back into a curve, and most marks are
drawn twice at slightly different jitter and opacity, which is what over-draw
looks like when somebody goes round a line a second time.

Stroked in currentColor, so a drawing takes the ink of the page it sits on:
silver on the navy cover, navy on the cream plates. The randomness runs from a
fixed seed, so the drawing is byte-identical on every build.
"""

import math
import random


class Pen:
    def __init__(self, seed=5, amp=1.15):
        self.r = random.Random(seed)
        self.amp = amp
        self.out = []

    # ---- geometry ------------------------------------------------------
    def _smooth(self, pts):
        """Quadratic through the midpoints, so a jittered point list reads as
        a drawn curve rather than a polygon."""
        d = [f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"]
        for i in range(1, len(pts) - 1):
            mx = (pts[i][0] + pts[i + 1][0]) / 2
            my = (pts[i][1] + pts[i + 1][1]) / 2
            d.append(f"Q{pts[i][0]:.1f} {pts[i][1]:.1f} {mx:.1f} {my:.1f}")
        d.append(f"L{pts[-1][0]:.1f} {pts[-1][1]:.1f}")
        return "".join(d)

    def _jit(self, pts, amp=None):
        a = self.amp if amp is None else amp
        r = self.r
        return [(x + r.uniform(-a, a), y + r.uniform(-a, a)) for x, y in pts]

    # ---- marks ---------------------------------------------------------
    def draw(self, pts, op=.82, twice=True, amp=None, w=None):
        """One mark, usually gone over a second time."""
        passes = 2 if twice and self.r.random() < .75 else 1
        for k in range(passes):
            o = op if k == 0 else op * self.r.uniform(.34, .52)
            sw = w or self.r.uniform(.95, 1.25)
            self.out.append(
                f'<path d="{self._smooth(self._jit(pts, amp))}" '
                f'opacity="{o:.2f}" stroke-width="{sw:.2f}"/>')

    def seg(self, a, b, n=7, **kw):
        self.draw([(a[0] + (b[0] - a[0]) * i / (n - 1),
                    a[1] + (b[1] - a[1]) * i / (n - 1)) for i in range(n)], **kw)

    def arc(self, cx, cy, r, a0, a1, n=17, **kw):
        self.draw([(cx + r * math.cos(a0 + (a1 - a0) * i / (n - 1)),
                    cy + r * math.sin(a0 + (a1 - a0) * i / (n - 1)))
                   for i in range(n)], **kw)

    def box(self, x0, y0, x1, y1, top=True, **kw):
        self.seg((x0, y1), (x0, y0), **kw)
        self.seg((x1, y1), (x1, y0), **kw)
        if top:
            self.seg((x0, y0), (x1, y0), **kw)

    def arch(self, cx, base, r, h, **kw):
        """A doorway or window: two jambs and a half round over them."""
        self.seg((cx - r, base), (cx - r, base - h), **kw)
        self.seg((cx + r, base), (cx + r, base - h), **kw)
        self.arc(cx, base - h, r, math.pi, 2 * math.pi, n=11, **kw)

    def hatch(self, x0, y0, x1, y1, n, length, dx, op=.3):
        """Shading. Short strokes, never doubled."""
        for i in range(n):
            t = i / max(1, n - 1)
            x = x0 + (x1 - x0) * t + self.r.uniform(-3, 3)
            y = y0 + (y1 - y0) * t + self.r.uniform(-3, 3)
            L = length * self.r.uniform(.45, 1.25)
            self.seg((x, y), (x + dx * L, y + L), n=3,
                     op=op * self.r.uniform(.6, 1.15), twice=False, amp=.5)

    def svg(self, w, h, cls):
        return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" fill="none" '
                'preserveAspectRatio="xMidYMax meet" aria-hidden="true" '
                'focusable="false"><g stroke="currentColor" '
                'stroke-linecap="round" stroke-linejoin="round">'
                + "".join(self.out) + "</g></svg>")


W, H = 1200, 232


def coast():
    """A church above the sea. Short and wide on purpose, so it sits inside a
    column of text instead of interrupting it."""
    p = Pen(5)
    rnd = p.r

    # --- water -----------------------------------------------------------
    p.seg((8, 68), (648, 68), n=14, op=.5, amp=.7)
    p.draw([(104, 68), (124, 59), (152, 55), (184, 58), (208, 66), (218, 68)],
           op=.38, amp=.8)
    p.draw([(272, 68), (292, 61), (316, 59), (338, 64), (348, 68)],
           op=.28, amp=.7)
    for i in range(20):
        t = i / 19
        y = 76 + 96 * (t ** 1.4)
        for _ in range(rnd.randint(1, 3) if t < .3 else rnd.randint(2, 4)):
            w = 640 * (.05 + .2 * t) * rnd.uniform(.5, 1.4)
            x = rnd.uniform(6, max(8, 644 - w))
            p.seg((x, y), (x + w, y), n=5, op=.46 - .24 * t, twice=False, amp=.75)

    # --- the headland ----------------------------------------------------
    p.draw([(648, 182), (712, 176), (776, 166), (840, 150), (916, 140),
            (1012, 140), (1116, 137), (1194, 135)], op=.78, amp=1.3)
    p.draw([(648, 182), (628, 194), (612, 214), (604, 232)], op=.62, amp=1.3)
    p.hatch(660, 188, 1186, 142, 32, 9, -.35, .2)
    p.hatch(642, 188, 610, 230, 10, 13, -.3, .26)

    # --- the church ------------------------------------------------------
    p.box(930, 94, 1056, 142, top=False)          # body
    p.seg((930, 94), (1056, 94))
    p.box(954, 72, 1032, 94, top=False)           # drum
    p.arc(993, 72, 39, math.pi, 2 * math.pi)      # dome
    p.arc(993, 72, 27, math.pi * 1.08, math.pi * 1.6, n=9, op=.3, twice=False)
    p.arc(993, 72, 17, math.pi * 1.1, math.pi * 1.5, n=7, op=.22, twice=False)
    p.seg((993, 33), (993, 18), n=4)              # finial and cross
    p.seg((985, 24), (1001, 24), n=4)
    p.arch(972, 94, 6, 12, op=.55)                # drum windows
    p.arch(1014, 94, 6, 12, op=.55)
    for cx in (952, 993, 1034):                   # arcade
        p.arch(cx, 142, 11, 32)
    p.seg((922, 142), (1064, 142), n=9, op=.7)
    p.hatch(1038, 104, 1054, 138, 7, 7, -.3, .22)

    # --- the chapel ------------------------------------------------------
    p.box(862, 116, 914, 148, top=False)
    p.seg((862, 116), (914, 116))
    p.arc(888, 116, 26, math.pi, 2 * math.pi, n=13)
    p.arc(888, 116, 17, math.pi * 1.08, math.pi * 1.6, n=8, op=.28, twice=False)
    p.seg((888, 90), (888, 79), n=4)
    p.seg((881, 84), (895, 84), n=4)
    p.arch(888, 148, 10, 22)
    p.seg((856, 148), (920, 148), n=6, op=.7)

    # --- the bell tower --------------------------------------------------
    p.box(786, 134, 830, 166, top=False)
    p.seg((786, 134), (830, 134))
    p.arc(808, 134, 22, math.pi, 2 * math.pi, n=11)
    p.seg((808, 112), (808, 102), n=4)
    p.seg((802, 107), (814, 107), n=4)
    p.arch(808, 166, 9, 21)
    p.seg((780, 166), (836, 166), n=6, op=.7)

    # --- cypresses -------------------------------------------------------
    for x, h, w in ((1106, 62, 11), (1142, 82, 13), (1176, 54, 10)):
        base = 136
        p.draw([(x, base - h), (x + w * .9, base - h * .62),
                (x + w, base - h * .28), (x + w * .34, base)], amp=.9)
        p.draw([(x, base - h), (x - w * .9, base - h * .62),
                (x - w, base - h * .28), (x - w * .34, base)], amp=.9)
        p.seg((x, base - h * .66), (x, base), n=4, op=.4, twice=False)

    return p.svg(W, H, "sk__art")


def wave(n=10, w=46, h=5):
    """A line of water, where a page changes subject."""
    p = Pen(3, amp=.55)
    pts = [(i * w / 6, h + 1 + (-h if (i // 3) % 2 == 0 else h) *
            math.sin(i * math.pi / 3)) for i in range(n * 6 + 1)]
    p.draw(pts, op=.85, twice=False)
    return p.svg(n * w, h * 2 + 4, "wv__art")
