"""Tech Atlas teams and sector standings.

A team is an ecosystem: companies tied together by ownership, backing and
major partnerships, usually across sectors. The rules are written out in
docs/ratings-rubric.md. In short, in this order:

1. Each team in atlas.json names its captains. A captain leads its team.
2. A company's own `team` field, with `team_reason`, overrides everything.
   "independent" keeps it off every team.
3. A company owned by a captain joins that captain's team.
4. Otherwise each direct tie to a captain scores (TIE_WEIGHT) and the
   highest-scoring team wins. An even score is a tie, left for an override.
5. A company owned by a member placed by steps 1 to 4 joins that member's team.
6. Anyone else is independent.

Nothing here changes the data it is given.
"""

TIE_WEIGHT = {"investment": 10, "supply": 3, "alliance": 3, "license": 2, "dependency": 2}
CAPITAL = ("ownership", "investment")
INDEPENDENT = "independent"
MIN_MEMBERS = 3
STARTING_FIVE = (0.30, 0.25, 0.20, 0.15, 0.10)

# what a member is to the captain or member that placed it, by kind and direction
_ROLE = {("supply", "from"): "supplier", ("supply", "to"): "customer",
         ("license", "from"): "licensee", ("license", "to"): "licensor",
         ("dependency", "from"): "dependent", ("dependency", "to"): "relied-on",
         ("alliance", "from"): "partner", ("alliance", "to"): "partner",
         ("investment", "to"): "backed", ("ownership", "to"): "owned"}


def _captains(data):
    out = {}
    for t in data.get("teams", []):
        for i, cid in enumerate(t["captains"]):
            out[cid] = (t["id"], "captain" if i == 0 else "co-captain")
    return out


def _owners(data, cid):
    return [r["from"] for r in data["relationships"] if r["type"] == "ownership" and r["to"] == cid]


def _scores(data, cid, captains):
    """Points per team from cid's direct ties to captains, and the heaviest tie behind each."""
    points, best = {}, {}
    for r in data["relationships"]:
        kind = r["type"]
        if kind not in TIE_WEIGHT:
            continue
        if r["to"] == cid and r["from"] in captains:
            other, end = r["from"], "to"
        elif r["from"] == cid and r["to"] in captains and kind not in CAPITAL:
            other, end = r["to"], "from"
        else:
            continue
        team, w = captains[other][0], TIE_WEIGHT[kind]
        points[team] = points.get(team, 0) + w
        if w > best.get(team, (0,))[0]:
            best[team] = (w, _ROLE[(kind, end)], other)
    return points, best


def assign(data):
    """{"members": {cid: {team, role, via}}, "ties": {cid: [team ids]}}. Independents are left out."""
    captains = _captains(data)
    members, ties = {}, {}
    for cid, (team, role) in captains.items():
        members[cid] = {"team": team, "role": role, "via": None}
    for cid, c in data["companies"].items():
        if cid in members:
            continue
        if c.get("team"):
            if c["team"] != INDEPENDENT:
                members[cid] = {"team": c["team"], "role": "override", "via": None}
            continue
        owners = [o for o in _owners(data, cid) if o in captains]
        teams = sorted({captains[o][0] for o in owners})
        if len(teams) == 1:
            members[cid] = {"team": teams[0], "role": "owned", "via": owners[0]}
            continue
        if len(teams) > 1:
            ties[cid] = teams
            continue
        points, best = _scores(data, cid, captains)
        if not points:
            continue
        top = max(points.values())
        leaders = sorted(t for t, p in points.items() if p == top)
        if len(leaders) > 1:
            ties[cid] = leaders
            continue
        _, role, via = best[leaders[0]]
        members[cid] = {"team": leaders[0], "role": role, "via": via}
    # one step further: owned by a member placed above
    placed = dict(members)
    for cid, c in data["companies"].items():
        if cid in placed or cid in ties or c.get("team"):
            continue
        owners = [o for o in _owners(data, cid) if o in placed]
        teams = sorted({placed[o]["team"] for o in owners})
        if len(teams) == 1:
            members[cid] = {"team": teams[0], "role": "owned", "via": owners[0]}
        elif len(teams) > 1:
            ties[cid] = teams
    return {"members": members, "ties": ties}


def team_ovr(ovrs):
    """The starting five: the best five OVRs weighted 30, 25, 20, 15 and 10, rescaled when fewer."""
    top = sorted((v for v in ovrs if v is not None), reverse=True)[:len(STARTING_FIVE)]
    if not top:
        return None
    w = STARTING_FIVE[:len(top)]
    return round(sum(a * b for a, b in zip(top, w)) / sum(w))


def rosters(data, ovr_of, status_of=lambda cid: None):
    """Each team with its members (captains first, then by OVR), its OVR and how many members it rests on."""
    members = assign(data)["members"]
    out = []
    for t in data.get("teams", []):
        ids = [k for k, m in members.items() if m["team"] == t["id"]]
        rank = {"captain": 0, "co-captain": 1}
        ids.sort(key=lambda k: (rank.get(members[k]["role"], 2), -(ovr_of(k) or 0), data["companies"][k]["name"]))
        five = sorted((k for k in ids if ovr_of(k) is not None), key=lambda k: -ovr_of(k))[:len(STARTING_FIVE)]
        scored = [ovr_of(k) for k in five]
        draft = any(status_of(k) == "draft" for k in five)
        out.append({**t, "members": [{"company": k, **members[k]} for k in ids], "ovr": team_ovr(scored),
                    "ovr_from": len(scored), "ovr_status": "draft" if draft else ("reviewed" if scored else None)})
    return out


def standings(data, sector, ovr_of):
    """Companies placed in one sector: ranked by OVR (ties share a rank, then by name), and the unrated."""
    depth = {"starter": 0, "second_string": 1, "practice_squad": 2}
    best = {}
    # a company in two rows of one sector is listed once, at its best depth
    for p in data["placements"]:
        if p["sector"] == sector and (p["company"] not in best or depth[p["rank"]] < depth[best[p["company"]]["rank"]]):
            best[p["company"]] = p
    rows = []
    for p in best.values():
        c = data["companies"][p["company"]]
        hist = c.get("ovr_history") or []
        now = ovr_of(p["company"])
        change = now - hist[-1]["ovr"] if hist and now is not None else None
        rows.append({"company": p["company"], "row": p["row"], "depth": p["rank"], "ovr": now, "change": change})
    ranked = sorted((r for r in rows if r["ovr"] is not None),
                    key=lambda r: (-r["ovr"], data["companies"][r["company"]]["name"]))
    for i, r in enumerate(ranked):
        r["rank"] = ranked[i - 1]["rank"] if i and ranked[i - 1]["ovr"] == r["ovr"] else i + 1
    unrated = sorted((r for r in rows if r["ovr"] is None), key=lambda r: data["companies"][r["company"]]["name"])
    return {"ranked": ranked, "unrated": unrated}
