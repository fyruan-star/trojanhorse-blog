"""Tests for the draft-rating switch and OVR tiers in content/atlas/atlas_data.py."""
import pathlib, sys, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "content" / "atlas"))
import atlas_data as AD

class Wiring(unittest.TestCase):
    def test_every_company_is_resolved(self):
        self.assertEqual(set(AD.RESOLVED), set(AD.DATA["companies"]))

    def test_ratings_holds_only_companies_with_a_published_ovr(self):
        self.assertTrue(all(r["ovr"] is not None for r in AD.RATINGS.values()))

    def test_switch_is_passed_through(self):
        hidden = AD.atlas_ratings.resolve(AD.DATA, show_drafts=False)
        self.assertFalse(any(a["status"] == "draft" for r in hidden.values() for a in r["attributes"].values()))
        self.assertFalse(any(b["status"] == "draft" for r in hidden.values() for b in r["badges"]))


class Tiers(unittest.TestCase):
    def test_tier_edges(self):
        cases = {99: "Generational", 95: "Generational", 94: "Superstar", 85: "All-Star", 84: "Starter",
                 75: "Rotation", 70: "Role player", 69: "Bench", 60: "Bench", 59: "Prospect", 40: "Prospect"}
        for ovr, label in cases.items():
            with self.subTest(ovr=ovr):
                self.assertEqual(AD.ovr_tier(ovr), label)


class Shapes(unittest.TestCase):
    def test_every_card_company_has_a_home(self):
        self.assertEqual(set(AD.APPEARS), set(AD.HOME))

    def test_backers_are_the_companies_with_no_card(self):
        self.assertEqual(len(AD.BACKERS), 12)
        self.assertFalse(set(AD.BACKERS) & set(AD.HOME))


if __name__ == "__main__":
    unittest.main()
