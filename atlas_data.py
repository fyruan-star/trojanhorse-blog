"""Tech Atlas: the whole landscape, assembled from one module per sector.

Phase 1 covers nine sectors. Entities are shared across sectors, so a company
has one record and appears wherever it plays. Sector order follows the stack,
from the physical foundation at the bottom to the end markets at the top.
"""
import importlib

ASOF = "23 October 2026"

_MODULES = ["silicon", "infra", "cloud", "models", "software", "security",
            "internet", "devices", "telecom"]

ENT, SECTORS, EDGES = {}, [], []
for m in _MODULES:
    mod = importlib.import_module(f"atlas_{m}")
    for k, v in mod.ENT.items():
        ENT.setdefault(k, v)
    SECTORS.append(mod.SECTOR)
    EDGES.extend(mod.EDGES)

# which sector is each company's home, by first appearance as a player
HOME = {}
APPEARS = {}
for s in SECTORS:
    for p in s["positions"]:
        for pl in p["players"]:
            HOME.setdefault(pl["e"], s["id"])
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

# Overview map. Edges worth drawing between sectors, chosen by hand from EDGES.
def check():
    problems = []
    for ed in EDGES:
        for e in (ed["a"], ed["b"]):
            if e not in ENT:
                problems.append(f"edge endpoint missing: {e}")
        if ed["type"] not in EDGE_LABEL:
            problems.append(f"bad edge type {ed['type']}")
    for s in SECTORS:
        for p in s["positions"]:
            for pl in p["players"]:
                if pl["e"] not in ENT:
                    problems.append(f"player missing: {pl['e']} in {s['id']}/{p['id']}")
                if pl["t"] not in TIER_LABEL:
                    problems.append(f"bad tier {pl['t']}")
    return problems

if __name__ == "__main__":
    pr = check()
    print("problems:", pr or "none")
    n = sum(len(p["players"]) for s in SECTORS for p in s["positions"])
    print(len(SECTORS), "sectors,", sum(len(s["positions"]) for s in SECTORS), "positions,", n, "cards,",
          len(HOME), "companies with a home,", len(BACKERS), "backers,", len(EDGES), "edges")
