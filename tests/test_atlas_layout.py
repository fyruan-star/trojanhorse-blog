"""Tests for the map layout in content/atlas/atlas_layout.py."""
import math, pathlib, sys, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "content" / "atlas"))
import atlas_data as AD
import atlas_layout as L

LAYOUT = L.layout(AD.DATA)


def dist(a, b):
    return math.hypot(a["x"] - b["x"], a["y"] - b["y"])


class Coverage(unittest.TestCase):
    def test_every_card_is_placed(self):
        placed = {(c["company"], c["sector"], c["row"]) for c in LAYOUT["cards"] if c["sector"] != "backers"}
        wanted = {(p["company"], p["sector"], p["row"]) for p in AD.DATA["placements"]}
        self.assertEqual(placed, wanted)

    def test_each_company_has_exactly_one_main_node(self):
        mains = [c["company"] for c in LAYOUT["cards"] if c["main"]]
        self.assertEqual(len(mains), len(set(mains)))
        self.assertEqual(set(mains), set(AD.HOME) | set(AD.BACKERS))

    def test_main_node_sits_in_the_home_sector(self):
        for c in LAYOUT["cards"]:
            if c["main"] and c["company"] in AD.HOME:
                self.assertEqual(c["sector"], AD.HOME[c["company"]], c["company"])

    def test_all_nine_sectors_and_the_backers_island_exist(self):
        self.assertEqual(set(LAYOUT["sectors"]), {s["id"] for s in AD.SECTORS} | {"backers"})


class Geometry(unittest.TestCase):
    def test_nodes_keep_their_distance(self):
        cards = LAYOUT["cards"]
        worst = min(dist(a, b) for i, a in enumerate(cards) for b in cards[i + 1:])
        self.assertGreaterEqual(worst, L.MIN_GAP * 0.95)

    def test_nodes_stay_inside_their_territory(self):
        for c in LAYOUT["cards"]:
            t = LAYOUT["sectors"][c["sector"]]
            self.assertLess(dist(c, t), t["r"], c["company"])

    def test_territories_do_not_overlap(self):
        ts = list(LAYOUT["sectors"].values())
        for i, a in enumerate(ts):
            for b in ts[i + 1:]:
                self.assertGreater(dist(a, b), a["r"] + b["r"], (a["id"], b["id"]))

    def test_starters_sit_nearer_the_centre_than_the_practice_squad(self):
        for sid in AD.HOME.values():
            t = LAYOUT["sectors"][sid]
            by_rank = {}
            for c in LAYOUT["cards"]:
                if c["sector"] == sid:
                    by_rank.setdefault(c["rank"], []).append(dist(c, t))
            means = [sum(v) / len(v) for k, v in sorted(by_rank.items(), key=lambda kv: L.RANKS.index(kv[0]))]
            self.assertEqual(means, sorted(means), sid)

    def test_tiers_run_end_markets_over_platforms_over_the_stack(self):
        y = {t["id"]: t["y"] for t in LAYOUT["tiers"]}
        self.assertLess(y["end"], y["platform"])
        self.assertLess(y["platform"], y["stack"])

    def test_row_labels_sit_inside_their_territory(self):
        for t in LAYOUT["sectors"].values():
            for r in t["rows"]:
                self.assertLess(dist(r, t), t["r"], (t["id"], r["id"]))

    def test_dividers_and_rings_stay_inside_their_territory(self):
        for t in LAYOUT["sectors"].values():
            for x1, y1, x2, y2 in t["spokes"]:
                self.assertLess(dist({"x": x2, "y": y2}, t), t["r"])
            for ring in t["rings"]:
                self.assertLess(ring, t["r"])

    def test_a_sector_with_one_row_has_no_dividers(self):
        one_row = [s["id"] for s in AD.SECTORS if len(s["positions"]) == 1]
        for sid in one_row:
            self.assertEqual(LAYOUT["sectors"][sid]["spokes"], [])

    def test_bands_cover_each_row_once_and_sit_inside(self):
        for sid in AD.HOME.values():
            t = LAYOUT["sectors"][sid]
            self.assertEqual([b["id"] for b in t["bands"]], [r["id"] for r in t["rows"]])
            self.assertLess(t["outer"], t["r"])
            for a, b in zip(t["bands"], t["bands"][1:]):
                self.assertLessEqual(a["a1"], b["a0"])

    def test_outline_is_a_closed_path(self):
        for t in LAYOUT["sectors"].values():
            self.assertTrue(t["outline"].startswith("M") and t["outline"].endswith("Z"))

    def test_bounds_hold_every_territory(self):
        x0, y0, x1, y1 = LAYOUT["bounds"]
        for t in LAYOUT["sectors"].values():
            self.assertTrue(x0 <= t["x"] - t["r"] and t["x"] + t["r"] <= x1)
            self.assertTrue(y0 <= t["y"] - t["r"] and t["y"] + t["r"] <= y1)


class NarrowLayout(unittest.TestCase):
    def setUp(self):
        self.narrow = LAYOUT["narrow"]
        self.centres = self.narrow["centres"]

    def test_every_sector_has_a_narrow_place(self):
        self.assertEqual(set(self.centres), set(LAYOUT["sectors"]))

    def test_two_columns_of_five(self):
        columns = {}
        for x, y in self.centres.values():
            columns.setdefault(x, []).append(y)
        self.assertEqual(sorted(len(v) for v in columns.values()), [5, 5])
        self.assertEqual(len({y for ys in columns.values() for y in ys}), 5)

    def test_territories_do_not_overlap(self):
        ids = list(self.centres)
        for i, a in enumerate(ids):
            for b in ids[i + 1:]:
                d = math.hypot(self.centres[a][0] - self.centres[b][0], self.centres[a][1] - self.centres[b][1])
                self.assertGreater(d, LAYOUT["sectors"][a]["r"] + LAYOUT["sectors"][b]["r"], (a, b))

    def test_bounds_hold_every_territory(self):
        x0, y0, x1, y1 = self.narrow["bounds"]
        for sid, (x, y) in self.centres.items():
            r = LAYOUT["sectors"][sid]["r"]
            self.assertTrue(x0 <= x - r and x + r <= x1 and y0 <= y - r and y + r <= y1, sid)


class SectorLabels(unittest.TestCase):
    """What the galaxy view prints under each title has to exist in the data."""

    def test_every_sector_has_three_rated_companies_to_list(self):
        for sid, t in LAYOUT["sectors"].items():
            if sid == "backers":
                continue
            mains = [c["company"] for c in LAYOUT["cards"] if c["sector"] == sid and c["main"]]
            rated = [m for m in mains if AD.RATINGS.get(m, {}).get("ovr") is not None]
            self.assertGreaterEqual(len(rated), 3, sid)

    def test_owners_and_backers_are_twelve_and_three_have_backed_companies(self):
        mains = {c["company"] for c in LAYOUT["cards"] if c["sector"] == "backers" and c["main"]}
        self.assertEqual(len(mains), 12)
        backing = {e["a"] for e in AD.EDGES if AD.GROUP[e["type"]] == "backers" and e["a"] in mains}
        self.assertGreaterEqual(len(backing), 3)


class Determinism(unittest.TestCase):
    def test_same_data_gives_the_same_map(self):
        self.assertEqual(L.layout(AD.DATA), LAYOUT)


if __name__ == "__main__":
    unittest.main()
