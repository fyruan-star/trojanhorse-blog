"""Tests for the draft-rating switch and OVR tiers in content/atlas/atlas_data.py."""
import pathlib, sys, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "content" / "atlas"))
import atlas_data as AD

DRAFT = {"name": "X", "ovr": 88, "ovr_status": "draft", "ovr_reason": "r.", "ovr_by": "Claude (draft)"}
REVIEWED = {**DRAFT, "ovr_status": "reviewed", "ovr_by": "Ryan"}


class DraftSwitch(unittest.TestCase):
    def test_drafts_hidden_when_switched_off(self):
        self.assertIsNone(AD.public_rating(DRAFT, show_drafts=False))

    def test_drafts_shown_when_switched_on(self):
        self.assertEqual(AD.public_rating(DRAFT, show_drafts=True)["ovr"], 88)

    def test_reviewed_always_shown(self):
        self.assertEqual(AD.public_rating(REVIEWED, show_drafts=False)["ovr_status"], "reviewed")

    def test_unrated_never_shown(self):
        self.assertIsNone(AD.public_rating({"name": "X", "ovr": None}, show_drafts=True))

    def test_published_rating_carries_no_other_fields(self):
        self.assertNotIn("name", AD.public_rating(REVIEWED, show_drafts=False))


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
