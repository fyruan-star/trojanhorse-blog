"""Tests for Atlas logos: every company shows its official mark, or sits on the
monogram list with a reason, and the mark appears wherever the company does.

The page tests read the built site, so setUpModule builds it first."""
import copy, json, pathlib, re, subprocess, sys, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "scripts"))
import validate_atlas as V

DATA = json.loads((HERE / "content/atlas/atlas.json").read_text(encoding="utf-8"))
SITE = HERE / "_site"
MONO = DATA.get("monograms", {})
HOMED = {cid for cid, c in DATA["companies"].items() if c["sector"] != "backers"}


def setUpModule():
    subprocess.run([sys.executable, "build.py"], cwd=HERE, check=True, capture_output=True)


def read(name):
    return (SITE / name).read_text(encoding="utf-8")


class FallbackList(unittest.TestCase):
    def test_every_company_has_a_logo_or_a_listed_reason(self):
        missing = [cid for cid, c in DATA["companies"].items() if not c.get("logo") and cid not in MONO]
        self.assertEqual(missing, [])

    def test_no_company_is_both(self):
        both = [cid for cid in MONO if DATA["companies"].get(cid, {}).get("logo")]
        self.assertEqual(both, [])

    def test_every_reason_names_the_search(self):
        for cid, reason in MONO.items():
            with self.subTest(company=cid):
                self.assertIn(cid, DATA["companies"])
                self.assertGreater(len(reason.split()), 5)
                self.assertTrue(reason.rstrip().endswith("."))

    def test_monograms_are_the_minority(self):
        self.assertLess(len(MONO), len(DATA["companies"]) / 4)


class Validator(unittest.TestCase):
    def errors(self, fn):
        d = copy.deepcopy(DATA)
        fn(d)
        return V.validate(d)[0]

    def test_a_company_with_no_logo_and_no_reason_is_caught(self):
        def drop(d):
            cid = next(c for c in d["companies"] if d["companies"][c].get("logo"))
            del d["companies"][cid]["logo"]
        self.assertTrue(any("monogram" in e for e in self.errors(drop)))

    def test_a_reason_for_a_company_with_a_logo_is_caught(self):
        def both(d):
            cid = next(c for c in d["companies"] if d["companies"][c].get("logo"))
            d.setdefault("monograms", {})[cid] = "Searched Simple Icons and the press kit, found nothing usable."
        self.assertTrue(any("monogram" in e for e in self.errors(both)))

    def test_a_reason_for_an_unknown_company_is_caught(self):
        def ghost(d):
            d.setdefault("monograms", {})["no_such_co"] = "Searched Simple Icons and the press kit, found nothing."
        self.assertTrue(any("no_such_co" in e for e in self.errors(ghost)))


class Pages(unittest.TestCase):
    def test_every_logo_file_exists(self):
        for cid, c in DATA["companies"].items():
            if c.get("logo"):
                with self.subTest(company=cid):
                    self.assertTrue((HERE / "assets" / "logos" / c["logo"]["file"]).is_file())

    def test_profiles_show_the_logo(self):
        for cid, c in DATA["companies"].items():
            if c.get("logo"):
                with self.subTest(company=cid):
                    self.assertIn(f'src="../logos/{c["logo"]["file"]}"', read(f"atlas/{cid}.html"))

    def test_standings_show_each_logo(self):
        for s in DATA["sectors"]:
            page = read(f"atlas/sector-{s['id']}.html")
            for p in DATA["placements"]:
                c = DATA["companies"][p["company"]]
                if p["sector"] == s["id"] and c.get("logo"):
                    with self.subTest(sector=s["id"], company=p["company"]):
                        self.assertIn(f'../logos/{c["logo"]["file"]}', page)

    def test_list_cards_show_the_logo_or_the_monogram(self):
        page = read("tech-atlas.html")
        cards = re.findall(r'<details class="card card--[^"]*"[^>]*>(.*?)</details>', page, re.S)
        self.assertEqual(len(cards), len(DATA["placements"]))
        for card in cards:
            with self.subTest(card=card[:80]):
                self.assertRegex(card, r'class="card__logo[^"]*"><img src="logos/[a-z0-9_]+\.svg"|class="card__mono"')

    def test_the_map_data_carries_every_logo(self):
        built = json.loads(read("tech-atlas.json"))
        text = json.dumps(built)
        for cid, c in DATA["companies"].items():
            if c.get("logo"):
                with self.subTest(company=cid):
                    self.assertIn("logos/" + c["logo"]["file"], text)


if __name__ == "__main__":
    unittest.main()
