"""Hand-drawn line art, generated as inline SVG.

Stroke-only and set in currentColor, so a drawing takes the ink of whatever
page it sits on: navy on the cream plates, silver on the navy cover. The
repetitive marks, meaning the sea and the rock hatching, come from a fixed
seed, so the drawing is identical on every build.

No raster images, nothing to download, about five kilobytes of path data.
"""

import random

W, H = 1200, 330


def _sea(rng, y0=124, y1=252, x0=8, x1=686, rows=18):
    """Horizontal strokes standing in for water. They lengthen and thin out as
    they come toward the viewer, the way a pencil lays in a flat sea."""
    out = []
    for i in range(rows):
        t = i / (rows - 1)
        y = y0 + (y1 - y0) * (t ** 1.45)
        n = rng.randint(2, 4) if t > .3 else rng.randint(1, 2)
        for _ in range(n):
            w = (x1 - x0) * (0.05 + 0.19 * t) * rng.uniform(.5, 1.45)
            x = rng.uniform(x0, max(x0 + 1, x1 - w))
            out.append(f'<path d="M{x:.0f} {y:.0f}h{w:.0f}" '
                       f'opacity="{0.48 - 0.25 * t:.2f}"/>')
    return "".join(out)


def _hatch(rng, x0, y0, x1, y1, n, length, dx, op):
    """Short strokes dropped along a line, for rock."""
    out = []
    for i in range(n):
        t = i / (n - 1)
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t + rng.uniform(-4, 4)
        L = length * rng.uniform(.45, 1.3)
        out.append(f'<path d="M{x:.0f} {y:.0f}l{dx * L:.0f} {L:.0f}" '
                   f'opacity="{op:.2f}"/>')
    return "".join(out)


def _dome(cx, spring, r):
    """A half dome on its drum, with the cross above it and two arcs of shade
    inside. The shade sits inside the dome rather than on the finial, which is
    what made an earlier version read as a fountain."""
    apex = spring - r
    return (f'<path d="M{cx-r} {spring}a{r} {r} 0 0 1 {2*r} 0"/>'
            f'<path d="M{cx-r*.66:.0f} {spring}a{r*.66:.0f} {r*.66:.0f} 0 0 1 '
            f'{r*1.32:.0f} 0" opacity=".3"/>'
            f'<path d="M{cx+r*.3:.0f} {spring}a{r*.3:.0f} {r*.3:.0f} 0 0 1 '
            f'{r*.6:.0f} 0" opacity=".22"/>'
            f'<path d="M{cx} {apex}V{apex-r*.42:.0f}"/>'
            f'<path d="M{cx-r*.17:.0f} {apex-r*.26:.0f}h{r*.34:.0f}"/>')


def _arch(x, base, w, h):
    r = w / 2
    return (f'<path d="M{x} {base}v{-(h-r):.0f}q0 {-r:.0f} {r:.0f} {-r:.0f}'
            f't{r:.0f} {r:.0f}v{h-r:.0f}"/>')


def _cypress(x, base, h, w):
    top = base - h
    return (f'<path d="M{x} {top}c{w} {h*.34:.0f} {w*.92:.0f} {h*.7:.0f} '
            f'{w*.36:.0f} {h:.0f}"/>'
            f'<path d="M{x} {top}c{-w} {h*.34:.0f} {-w*.92:.0f} {h*.7:.0f} '
            f'{-w*.36:.0f} {h:.0f}"/>'
            f'<path d="M{x} {top + h*.3:.0f}V{base}" opacity=".4"/>')


def coast():
    """A church above the sea. The Aegean, and also the oldest picture there is
    of somebody waiting on a deal to come back over the water."""
    rng = random.Random(7)

    sea = ('<path d="M6 118h684" opacity=".5"/>'
           '<path d="M92 118q38-19 80-10q28 6 48 10" opacity=".4"/>'
           '<path d="M262 118q24-11 53-7q20 3 33 7" opacity=".28"/>'
           + _sea(rng))

    # the headland, rising to the right, with its face dropping out of frame
    cliff = ('<path d="M694 246c54-6 106-18 168-36c60-18 148-16 338-20"/>'
             '<path d="M694 246c-26 16-44 40-54 84" opacity=".62"/>'
             + _hatch(rng, 706, 252, 1190, 196, 34, 11, -.35, .2)
             + _hatch(rng, 688, 252, 648, 322, 11, 17, -.3, .26))

    church = ('<path d="M910 200v-58h160v58"/>'
              '<path d="M940 142v-26h100v26"/>'
              + _dome(990, 116, 50)
              + _arch(955, 142, 14, 17) + _arch(1017, 142, 14, 17)
              + _arch(925, 200, 28, 43) + _arch(976, 200, 28, 43)
              + _arch(1027, 200, 28, 43)
              + '<path d="M900 200h180" opacity=".72"/>')

    chapel = ('<path d="M822 206v-36h72v36"/>'
              + _dome(858, 170, 32)
              + _arch(844, 206, 28, 35)
              + '<path d="M814 206h88" opacity=".72"/>')

    tower = ('<path d="M734 228v-42h52v42"/>'
             + _dome(760, 186, 22)
             + _arch(748, 228, 24, 34)
             + '<path d="M728 228h64" opacity=".72"/>')

    trees = (_cypress(1108, 196, 86, 15) + _cypress(1146, 194, 112, 18)
             + _cypress(1182, 192, 74, 13))

    return ('<svg class="sk__art" viewBox="0 0 1200 330" fill="none" '
            'preserveAspectRatio="xMidYMax meet" aria-hidden="true" '
            'focusable="false"><g stroke="currentColor" stroke-width="1.15" '
            'stroke-linecap="round" stroke-linejoin="round">'
            + sea + cliff + church + chapel + tower + trees + '</g></svg>')


def wave(n=11, w=58, h=7):
    """A line of water, used where a page changes subject."""
    d = [f"M0 {h+1}"]
    for i in range(n):
        up = -h if i % 2 == 0 else h
        d.append(f"q{w//4} {up} {w//2} 0t{w//2} 0")
    return (f'<svg class="wv__art" viewBox="0 0 {n*w} {h*2+2}" fill="none" '
            'preserveAspectRatio="xMidYMid meet" aria-hidden="true" '
            f'focusable="false"><path d="{"".join(d)}" stroke="currentColor" '
            'stroke-width="1.15" stroke-linecap="round"/></svg>')
