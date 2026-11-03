"""Tech Atlas: the whole landscape, read from atlas.json.

atlas.json is the one source of truth for the List view (tech-atlas.html), the
Map view and the published tech-atlas.json. Edit it, then run
python3 scripts/validate_atlas.py. This module turns it back into the shapes
build.py renders: ENT, SECTORS and EDGES.

Every card carries a one line key figure with a period and a link. `why` is
the mechanism in one sentence and `could_change` is the named condition that
would change the order. Both are the author's reading of the evidence and are
marked as inference on the page. Trust on cards is sourced or reported. Trust
on relationships is primary (a filing, release or regulator document),
reported (credible press without the document) or inferred.

Sector order follows the stack, from the physical foundation at the bottom to
the end markets at the top. The telecom, foundation, mobility, robotics,
health, defense, quantum and energy modules stay on disk but are not loaded.
"""
import json, pathlib, sys

# False removes every draft rating from the published pages and JSON, so only
# ratings marked "reviewed" go live. True publishes drafts, labelled DRAFT.
SHOW_DRAFT_RATINGS = True

DATA = json.loads((pathlib.Path(__file__).parent / "atlas.json").read_text(encoding="utf-8"))
ASOF = DATA["asof"]

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent / "scripts"))
import validate_atlas
ERRORS, WARNINGS = validate_atlas.validate(DATA)

# atlas.json spells the ranks out. The renderer uses the short codes.
RANK_CODE = {"starter": "starter", "second_string": "second", "practice_squad": "rookie"}

ENT = {k: (v["name"], v["description"]) for k, v in DATA["companies"].items()}

def _player(pl):
    out = {"e": pl["company"], "t": RANK_CODE[pl["rank"]]}
    if pl.get("label"):
        out["badge"] = pl["label"]
    if pl["trust"] != "sourced":
        out["conf"] = pl["trust"]
    out.update(stat=pl["key_figure"], why=pl["why"], cond=pl["could_change"], src=pl["source"])
    return out

SECTORS = [dict(id=s["id"], name=s["name"], band=s["tier"], blurb=s["blurb"], positions=[
    dict(id=r["id"], name=r["name"], metric=r["metric"], metric_src=r["metric_source"],
         players=[_player(pl) for pl in DATA["placements"] if pl["sector"] == s["id"] and pl["row"] == r["id"]])
    for r in s["rows"]]) for s in DATA["sectors"]]

# Only lines a source states are in atlas.json. scripts/validate_atlas.py keeps
# out the ones a review rejected.
EDGES = [dict(a=r["from"], b=r["to"], type=r["type"], text=r["text"], src=r["source"],
              date=r["date"], conf=r["trust"]) for r in DATA["relationships"]]

# Three kinds of line are drawn. The seven source types fold into them.
GROUP = {"alliance": "allies", "supply": "allies", "license": "allies", "dependency": "allies",
         "rivalry": "rivals", "ownership": "backers", "investment": "backers"}
GROUP_LABEL = {"allies": "Allies and partners", "rivals": "Rivals", "backers": "Owners and backers"}

# each company's home sector, where the map draws it. Companies with no card
# have the sector "backers" and are left out of HOME.
HOME = {k: v["sector"] for k, v in DATA["companies"].items() if v["sector"] != validate_atlas.BACKERS}
APPEARS = {}
for s in SECTORS:
    for p in s["positions"]:
        for pl in p["players"]:
            APPEARS.setdefault(pl["e"], []).append((s["id"], p["id"], pl["t"]))

# the companies that appear only in relationships (investors, owners, funds)
BACKERS = sorted(set(e for ed in EDGES for e in (ed["a"], ed["b"])) - set(HOME))

TIER_LABEL = {"starter": "Starters", "second": "Second string", "rookie": "Practice squad"}
EDGE_LABEL = {
    "alliance": "Alliance", "supply": "Supply", "license": "Licence",
    "rivalry": "Rivalry", "ownership": "Ownership", "investment": "Investment",
    "dependency": "Dependency",
}
BAND_LABEL = {"end": "End markets", "platform": "Platforms and software", "stack": "The compute stack"}

import atlas_ratings

# What each company publishes about its ratings (attributes, calculated OVR,
# badges), with drafts already removed when SHOW_DRAFT_RATINGS is False.
RESOLVED = atlas_ratings.resolve(DATA, SHOW_DRAFT_RATINGS) if not ERRORS else {}
# the companies with a published OVR
RATINGS = {k: r for k, r in RESOLVED.items() if r["ovr"] is not None}

# OVR tiers, highest first, as in docs/ratings-rubric.md
OVR_TIERS = [(95, "Generational"), (90, "Superstar"), (85, "All-Star"), (80, "Starter"),
             (75, "Rotation"), (70, "Role player"), (60, "Bench"), (40, "Prospect")]

def ovr_tier(ovr):
    return next(label for floor, label in OVR_TIERS if ovr >= floor)

if __name__ == "__main__":
    for w in WARNINGS:
        print("warning:", w)
    print("problems:", ERRORS or "none")
    n = sum(len(p["players"]) for s in SECTORS for p in s["positions"])
    print(len(SECTORS), "sectors,", sum(len(s["positions"]) for s in SECTORS), "positions,", n, "cards,",
          len(HOME), "companies with a home,", len(BACKERS), "backers,", len(EDGES), "edges,",
          len(RATINGS), "ratings published")
