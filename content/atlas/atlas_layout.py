"""Tech Atlas map: where every territory and company sits, in map units.

Computed at build time from atlas.json and published inside tech-atlas.json,
so the browser only draws. Deterministic: the same data gives the same map.

Each sector is a territory. Its sub-rows are wedges around the centre and its
ranks are rings: starters nearest the centre, the practice squad at the edge.
Territories are laid out in the Atlas's three tiers, end markets on top and
the compute stack at the bottom. Companies with no card (owners and backers)
form a small island at the end of the middle row.
"""
import math, random

MIN_GAP = 80.0       # the closest two company centres may sit
RANKS = ["starter", "second_string", "practice_squad"]
SUB = 66.0           # step between sub-rings inside one rank's band
BAND_STEP = 98.0     # from the last sub-ring of one rank to the first of the next
PAD = 70.0           # from the outermost company to the territory's edge
WEDGE_GAP = 0.12     # radians left empty between sub-row wedges
TERR_GAP = 170.0     # least space between two territories
RELAX_ROUNDS = 160
WOBBLE = ((3, 0.034), (5, 0.02), (7, 0.012))   # harmonics of the hand-drawn outline
TIER_ORDER = ["end", "platform", "stack"]
TIER_LABEL = {"end": "End markets", "platform": "Platforms and software", "stack": "The compute stack"}
BACKERS = "backers"


def _wedges(rows, counts):
    """Start angle and span for each sub-row, wider for fuller rows, first at the top."""
    weights = [counts.get(r["id"], 0) + 1 for r in rows]
    free = 2 * math.pi - WEDGE_GAP * len(rows)
    out, a = [], -math.pi / 2 + WEDGE_GAP / 2
    for w in weights:
        span = free * w / sum(weights)
        out.append((a, span))
        a += span + WEDGE_GAP
    return out


def _rings(group, a0, span, start):
    """Spread one sub-row's cards of one rank over as many sub-rings as they need."""
    out, ring, i = [], 0, 0
    while i < len(group):
        rad = start + ring * SUB
        cap = max(1, int(rad * span // MIN_GAP))
        take = group[i:i + cap]
        for j, card in enumerate(take):
            ang = a0 + span * (j + 0.5) / len(take)
            out.append({"card": card, "x": rad * math.cos(ang), "y": rad * math.sin(ang), "lo": start})
        i += len(take)
        ring += 1
    return out, ring


def _relax(nodes):
    """Push apart any two nodes closer than MIN_GAP, keeping each inside its rank's band."""
    for _ in range(RELAX_ROUNDS):
        moved = False
        for i, a in enumerate(nodes):
            for b in nodes[i + 1:]:
                dx, dy = b["x"] - a["x"], b["y"] - a["y"]
                d = math.hypot(dx, dy)
                if d >= MIN_GAP:
                    continue
                if d < 1e-6:
                    dx, dy, d = 1.0, 0.0, 1.0
                push = (MIN_GAP - d) / 2 + 0.5
                a["x"] -= dx / d * push; a["y"] -= dy / d * push
                b["x"] += dx / d * push; b["y"] += dy / d * push
                moved = True
        for n in nodes:
            r = math.hypot(n["x"], n["y"])
            lo, hi = n["lo"] - SUB * 0.45, n["hi"] + SUB * 0.45
            if r and not lo <= r <= hi:
                k = min(max(r, lo), hi) / r
                n["x"] *= k; n["y"] *= k
        if not moved:
            return


def _outline(rid, radius, scale=1.0):
    """A closed, slightly irregular path around the origin, seeded by the territory id."""
    rng = random.Random(f"{rid}:{scale}")
    phases = [rng.uniform(0, 2 * math.pi) for _ in WOBBLE]
    pts = []
    for i in range(96):
        t = 2 * math.pi * i / 96
        f = 1 + sum(amp * math.sin(h * t + p) for (h, amp), p in zip(WOBBLE, phases))
        pts.append(f"{radius * scale * f * math.cos(t):.1f} {radius * scale * f * math.sin(t):.1f}")
    return "M" + " L".join(pts) + " Z"


def _territory(rid, rows, cards):
    """Local layout of one territory: nodes around (0, 0), its radius and rim labels."""
    counts = {}
    for c in cards:
        counts[c["row"]] = counts.get(c["row"], 0) + 1
    wedges = _wedges(rows, counts)
    nodes, start = [], max(MIN_GAP * 1.3, MIN_GAP * len(rows) / (2 * math.pi) * 1.35)
    edges = []      # where one rank's band ends and the next begins
    for rank in RANKS:
        deepest = 0
        for row, (a0, span) in zip(rows, wedges):
            group = [c for c in cards if c["row"] == row["id"] and c["rank"] == rank]
            placed, depth = _rings(group, a0, span, start)
            for n in placed:
                n["hi"] = start + (depth - 1) * SUB
            nodes += placed
            deepest = max(deepest, depth)
        if deepest:
            start += (deepest - 1) * SUB + BAND_STEP
            edges.append(start - BAND_STEP / 2)
    _relax(nodes)
    floor = 1 - sum(amp for _, amp in WOBBLE)
    base = (max(math.hypot(n["x"], n["y"]) for n in nodes) + PAD) / floor
    reach = base * (1 + sum(amp for _, amp in WOBBLE))
    # each sub-row's name sits just beyond its own cluster, inside the outline
    rim = []
    for row, (a0, span) in zip(rows, wedges):
        mid = a0 + span / 2
        own = [math.hypot(n["x"], n["y"]) for n in nodes if n["card"]["row"] == row["id"]]
        at = min(max(own, default=start) + 40, base * floor * 0.97)
        rim.append({"id": row["id"], "name": row["name"],
                    "x": round(math.cos(mid) * at, 1), "y": round(math.sin(mid) * at, 1),
                    "anchor": "start" if math.cos(mid) > 0.3 else "end" if math.cos(mid) < -0.3 else "middle"})
    # faint dividers between sub-rows, and rings between ranks
    spokes = [] if len(rows) < 2 else [
        (math.cos(a0 - WEDGE_GAP / 2), math.sin(a0 - WEDGE_GAP / 2)) for a0, _ in wedges]
    spokes = [(c * MIN_GAP * 0.5, s * MIN_GAP * 0.5, c * base * floor * 0.94, s * base * floor * 0.94) for c, s in spokes]
    rings = [e for e in edges[:-1] if e < base * floor * 0.94]
    # each sub-row as a named band: its wedge, from the core to just inside the outline
    bands = [{"id": row["id"], "name": row["name"], "a0": round(a0, 4), "a1": round(a0 + span, 4)}
             for row, (a0, span) in zip(rows, wedges)]
    return nodes, base, reach, {"rows": rim, "spokes": spokes, "rings": rings, "bands": bands,
                                "inner": MIN_GAP * 0.5, "outer": base * floor * 0.94}


def _backer_cards(data):
    linked = []
    for r in data["relationships"]:
        for cid in (r["from"], r["to"]):
            if data["companies"][cid]["sector"] == BACKERS and cid not in linked:
                linked.append(cid)
    return [{"company": cid, "sector": BACKERS, "row": BACKERS, "rank": None} for cid in sorted(linked)]


def layout(data):
    """The whole map. Reads data, never changes it."""
    sectors = {s["id"]: s for s in data["sectors"]}
    local = {}
    for sid, s in sectors.items():
        local[sid] = _territory(sid, s["rows"], [p for p in data["placements"] if p["sector"] == sid])
    backers = _backer_cards(data)
    island = [{"card": c, "x": 0.0, "y": 0.0, "lo": 0.0, "hi": 0.0} for c in backers]
    ring = max(MIN_GAP, len(island) * MIN_GAP / (2 * math.pi) * 1.1)
    for i, n in enumerate(island):
        t = -math.pi / 2 + 2 * math.pi * i / len(island)
        n["x"], n["y"] = ring * math.cos(t), ring * math.sin(t)
    floor = 1 - sum(amp for _, amp in WOBBLE)
    island_base = (ring + PAD) / floor
    local[BACKERS] = (island, island_base, island_base * (2 - floor),
                      {"rows": [], "spokes": [], "rings": [], "bands": [], "inner": 0, "outer": island_base * floor * 0.94})

    rows_of = {t: [sid for sid, s in sectors.items() if s["tier"] == t] for t in TIER_ORDER}
    rows_of["platform"] = rows_of["platform"] + [BACKERS]

    # place each tier row left to right, centred, and stack the rows top to bottom
    placed, tiers, y = {}, [], 0.0
    for t in TIER_ORDER:
        ids = rows_of[t]
        reach = [local[sid][2] for sid in ids]
        tallest = max(reach)
        y += tallest
        width = sum(2 * r for r in reach) + TERR_GAP * (len(ids) - 1)
        x = -width / 2
        for sid, r in zip(ids, reach):
            rng = random.Random(sid)
            dy = rng.uniform(-0.5, 0.5) * (tallest - r)
            placed[sid] = (x + r, y + dy)
            x += 2 * r + TERR_GAP
        tiers.append({"id": t, "label": TIER_LABEL[t], "y": round(y, 1), "left": -width / 2})
        y += tallest + TERR_GAP

    left = min(t["left"] for t in tiers) - TERR_GAP * 0.6
    tiers = [{"id": t["id"], "label": t["label"], "x": round(left, 1), "y": t["y"]} for t in tiers]

    cards, out = [], {}
    mains = set()
    for sid, (nodes, base, reach, marks) in local.items():
        cx, cy = placed[sid]
        name = sectors[sid]["name"] if sid in sectors else "Owners and backers"
        out[sid] = {"id": sid, "name": name, "x": round(cx, 1), "y": round(cy, 1), "r": round(reach, 1),
                    "outline": _outline(sid, base), "outline2": _outline(sid, base, 1.012),
                    "rows": [{**r, "x": round(r["x"] + cx, 1), "y": round(r["y"] + cy, 1)} for r in marks["rows"]],
                    "spokes": [[round(x1 + cx, 1), round(y1 + cy, 1), round(x2 + cx, 1), round(y2 + cy, 1)]
                               for x1, y1, x2, y2 in marks["spokes"]],
                    "rings": [round(r, 1) for r in marks["rings"]], "bands": marks["bands"],
                    "inner": round(marks["inner"], 1), "outer": round(marks["outer"], 1)}
        for n in nodes:
            c = n["card"]
            home = data["companies"][c["company"]]["sector"]
            main = home == sid and c["company"] not in mains
            if main:
                mains.add(c["company"])
            cards.append({"company": c["company"], "sector": sid, "row": c["row"], "rank": c["rank"],
                          "main": main, "x": round(n["x"] + cx, 1), "y": round(n["y"] + cy, 1)})

    x0 = min(left - 60, min(t["x"] - t["r"] for t in out.values()))
    x1 = max(t["x"] + t["r"] for t in out.values())
    y0 = min(t["y"] - t["r"] for t in out.values()) - 90
    y1 = max(t["y"] + t["r"] for t in out.values()) + 40
    return {"bounds": [round(x0, 1), round(y0, 1), round(x1, 1), round(y1, 1)],
            "tiers": tiers, "sectors": out, "cards": cards}
