"""Tests for the Biotech sector: Ryan's sector, its rows and companies, its
sourcing, its links to the rest of the Atlas, and where the map puts it."""
import copy, json, pathlib, sys, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "scripts"))
sys.path.insert(0, str(HERE / "content" / "atlas"))
import validate_atlas as V
import atlas_data as AD
import atlas_layout as L

DATA = json.loads((HERE / "content/atlas/atlas.json").read_text(encoding="utf-8"))
SECTOR = next((s for s in DATA["sectors"] if s["id"] == "biotech"), None)
CARDS = [p for p in DATA["placements"] if p["sector"] == "biotech"]
HOMED = {cid for cid, c in DATA["companies"].items() if c["sector"] == "biotech"}
ROWS = {"Large-cap biotech and pharma": {"lilly", "novo_nordisk", "regeneron", "moderna"},
        "Tools and sequencing": {"thermo_fisher", "illumina", "tenx_genomics"},
        "AI drug discovery": {"isomorphic", "recursion", "insilico", "xaira"},
        "Gene editing and cell therapy": {"vertex", "crispr_tx"}}


class Sector(unittest.TestCase):
    def test_biotech_exists_and_is_ryans(self):
        self.assertIsNotNone(SECTOR)
        self.assertEqual(SECTOR["name"], "Biotech")
        self.assertEqual(SECTOR["owner"], "Ryan")

    def test_it_has_the_four_approved_rows(self):
        self.assertEqual([r["name"] for r in SECTOR["rows"]], list(ROWS))
        for r in SECTOR["rows"]:
            with self.subTest(row=r["id"]):
                self.assertTrue(r["metric_source"].startswith("https://"))

    def test_the_approved_companies_sit_in_their_rows(self):
        row_name = {r["id"]: r["name"] for r in SECTOR["rows"]}
        got = {}
        for p in CARDS:
            got.setdefault(row_name[p["row"]], set()).add(p["company"])
        self.assertEqual(got, ROWS)
        self.assertEqual(HOMED, set().union(*ROWS.values()))

    def test_between_ten_and_fifteen_companies(self):
        self.assertTrue(10 <= len(HOMED) <= 15, len(HOMED))

    def test_each_row_has_a_starter(self):
        for r in SECTOR["rows"]:
            with self.subTest(row=r["id"]):
                self.assertIn("starter", {p["rank"] for p in CARDS if p["row"] == r["id"]})


class Sourcing(unittest.TestCase):
    def test_every_card_has_a_sourced_key_figure(self):
        for p in CARDS:
            with self.subTest(company=p["company"]):
                self.assertTrue(p["key_figure"].strip())
                self.assertTrue(p["source"].startswith("https://"))
                self.assertIn(p["trust"], V.CARD_TRUST)

    def test_every_company_is_described_and_rated_as_a_draft(self):
        for cid in HOMED:
            c = DATA["companies"][cid]
            with self.subTest(company=cid):
                self.assertTrue(c["description"].strip())
                self.assertEqual(c["ovr_by"], "Claude (draft)")
                for a in c["attributes"].values():
                    self.assertEqual(a["status"], "draft")

    def test_it_is_linked_to_the_rest_of_the_atlas(self):
        outside = [r for r in DATA["relationships"]
                   if (r["from"] in HOMED) != (r["to"] in HOMED)]
        self.assertGreaterEqual(len(outside), 3)
        for r in outside:
            with self.subTest(link=(r["from"], r["to"])):
                self.assertTrue(r["source"].startswith("https://"))


class Owner(unittest.TestCase):
    def errors(self, owner):
        d = copy.deepcopy(DATA)
        next(s for s in d["sectors"] if s["id"] == "biotech")["owner"] = owner
        return V.validate(d)[0]

    def test_an_owner_must_be_one_of_the_three_authors(self):
        self.assertEqual(self.errors("Ryan"), [])
        self.assertTrue(any("owner" in e for e in self.errors("Someone")))


class MapPlacement(unittest.TestCase):
    LAY = L.layout(AD.DATA)

    def test_biotech_is_on_the_map_with_a_helmet_slot(self):
        self.assertIn("biotech", self.LAY["sectors"])

    def test_wide_rows_run_four_four_three(self):
        ys = {}
        for sid, t in self.LAY["sectors"].items():
            ys.setdefault(t["y"], []).append(t["x"])
        self.assertEqual(sorted(len(v) for v in ys.values()), [3, 4, 4])
        for xs in ys.values():
            xs = sorted(xs)
            gaps = {round(b - a) for a, b in zip(xs, xs[1:])}
            self.assertLessEqual(len(gaps), 1, "even spacing within a row")

    def test_narrow_is_two_columns_of_six(self):
        centres = self.LAY["narrow"]["centres"]
        self.assertEqual(len(centres), 11)
        cols = {}
        for x, y in centres.values():
            cols.setdefault(x, []).append(y)
        self.assertEqual(sorted(len(v) for v in cols.values()), [5, 6])


if __name__ == "__main__":
    unittest.main()
