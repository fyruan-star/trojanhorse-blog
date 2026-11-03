"""Tests for content/atlas/atlas_ratings.py: OVR, Leverage, badges and the draft switch."""
import copy, json, pathlib, sys, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "content" / "atlas"))
import atlas_ratings as R

REAL = json.loads((HERE / "content/atlas/atlas.json").read_text(encoding="utf-8"))
EV = [{"url": "https://example.com/a", "trust": "sourced"}]


def attr(value, status="draft"):
    return {"value": value, "reason": "A fact.", "evidence": EV if value is not None else [], "status": status}


def lev(adjust, status="draft"):
    return {"adjust": adjust, "reason": "A fact.", "evidence": EV if adjust is not None else [], "status": status}


def world(attrs=None, badges=None, cid="nvidia"):
    """The real data with one company's ratings replaced, on a copy."""
    d = copy.deepcopy(REAL)
    for c in d["companies"].values():
        c.pop("attributes", None)
        c.pop("badges", None)
    if attrs is not None:
        d["companies"][cid]["attributes"] = attrs
    if badges is not None:
        d["companies"][cid]["badges"] = badges
    return d


class Ovr(unittest.TestCase):
    def test_all_six_at_the_same_value_give_that_value(self):
        self.assertEqual(R.ovr(dict.fromkeys(R.ATTRS, 80)), 80)

    def test_weights_and_peak(self):
        v = {"dominance": 99, "leverage": 99, "momentum": 70, "durability": 80, "firepower": 90, "deal_heat": 40}
        mean = (99 * .30 + 99 * .25 + 70 * .15 + 80 * .15 + 90 * .15) / 1.0
        self.assertEqual(R.ovr(v), round(0.8 * mean + 0.2 * 99))

    def test_deal_heat_does_not_move_ovr(self):
        base = {"dominance": 85, "leverage": 70, "momentum": 75, "durability": 80, "firepower": 60}
        self.assertEqual(R.ovr({**base, "deal_heat": 99}), R.ovr({**base, "deal_heat": 40}))

    def test_unrated_attributes_are_left_out_and_weights_rescaled(self):
        v = {"dominance": 90, "leverage": 70, "durability": 80, "momentum": None, "firepower": None, "deal_heat": None}
        mean = (90 * .30 + 70 * .25 + 80 * .15) / (.30 + .25 + .15)
        self.assertEqual(R.ovr(v), round(0.8 * mean + 0.2 * 90))

    def test_needs_dominance_leverage_and_durability(self):
        for missing in R.REQUIRED:
            with self.subTest(missing=missing):
                v = dict.fromkeys(R.ATTRS, 80)
                v[missing] = None
                self.assertIsNone(R.ovr(v))

    def test_held_between_40_and_99(self):
        self.assertEqual(R.ovr(dict.fromkeys(R.ATTRS, 99)), 99)
        self.assertEqual(R.ovr(dict.fromkeys(R.ATTRS, 40)), 40)


class Leverage(unittest.TestCase):
    def test_base_grows_by_eight_per_dependent_and_caps(self):
        self.assertEqual([R.leverage_base(n) for n in (0, 1, 2, 4, 9)], [50, 58, 66, 82, 82])

    def test_value_is_base_plus_adjust_held_in_range(self):
        self.assertEqual(R.leverage_value(66, 20), 86)
        self.assertEqual(R.leverage_value(82, 25), 99)
        self.assertEqual(R.leverage_value(50, -15), 40)

    def test_dependents_follow_each_relationship_type(self):
        deps = R.dependents(REAL)
        self.assertIn("nvidia", deps["tsmc"])        # supply: buyer depends on supplier
        self.assertIn("qualcomm", deps["arm"])       # license: licensee depends on licensor
        self.assertIn("coreweave", deps["microsoft"])  # dependency: from depends on to
        self.assertIn("cursor", deps["anthropic"])

    def test_alliances_rivalries_and_capital_do_not_count(self):
        deps = R.dependents(REAL)
        self.assertNotIn("amd", deps.get("intel", set()))       # rivalry
        self.assertNotIn("openai", deps.get("broadcom", set()))  # alliance
        self.assertNotIn("arm", deps.get("softbank", set()))     # ownership

    def test_the_backers_island_is_left_out(self):
        deps = R.dependents(REAL)
        backers = {k for k, c in REAL["companies"].items() if c["sector"] == "backers"}
        self.assertFalse(backers & set(deps))
        self.assertFalse(any(backers & s for s in deps.values()))


class Badges(unittest.TestCase):
    def test_kingmaker_goes_to_companies_backing_three_or_more(self):
        out = R.resolve(world(), show_drafts=True)
        kings = sorted(k for k, r in out.items() if any(b["id"] == "kingmaker" for b in r["badges"]))
        self.assertEqual(kings, ["blackstone", "mgx", "nvidia"])

    def test_chokepoint_from_leverage_of_92_or_more(self):
        n = R.leverage_base(len(R.dependents(REAL).get("nvidia", ())))
        hi = R.resolve(world({"leverage": lev(92 - n)}), show_drafts=True)["nvidia"]
        lo = R.resolve(world({"leverage": lev(91 - n)}), show_drafts=True)["nvidia"]
        self.assertIn("chokepoint", [b["id"] for b in hi["badges"]])
        self.assertNotIn("chokepoint", [b["id"] for b in lo["badges"]])

    def test_stored_badges_are_published_with_their_reason(self):
        b = [{"id": "in_play", "reason": "Reported talks.", "evidence": EV, "status": "reviewed"}]
        out = R.resolve(world(badges=b), show_drafts=False)["nvidia"]
        self.assertEqual([x["id"] for x in out["badges"] if x["id"] == "in_play"], ["in_play"])
        self.assertEqual(next(x for x in out["badges"] if x["id"] == "in_play")["label"], "In Play")


class DraftSwitch(unittest.TestCase):
    ATTRS = {"dominance": attr(90), "leverage": lev(10), "durability": attr(80), "momentum": attr(85, "reviewed"),
             "firepower": attr(None), "deal_heat": attr(None)}
    BADGES = [{"id": "single_customer_risk", "reason": "One customer.", "evidence": EV, "status": "draft"}]

    def test_drafts_show_when_switched_on(self):
        r = R.resolve(world(self.ATTRS, self.BADGES), show_drafts=True)["nvidia"]
        self.assertIsNotNone(r["ovr"])
        self.assertEqual(r["ovr_status"], "draft")
        self.assertIn("single_customer_risk", [b["id"] for b in r["badges"]])

    def test_switching_off_hides_draft_attributes_badges_and_ovr(self):
        r = R.resolve(world(self.ATTRS, self.BADGES), show_drafts=False)["nvidia"]
        self.assertEqual(sorted(r["attributes"]), ["momentum"])
        self.assertIsNone(r["ovr"])
        self.assertNotIn("single_customer_risk", [b["id"] for b in r["badges"]])

    def test_reviewed_attributes_stay_when_switched_off(self):
        reviewed = {k: {**v, "status": "reviewed"} for k, v in self.ATTRS.items()}
        r = R.resolve(world(reviewed), show_drafts=False)["nvidia"]
        self.assertEqual(r["ovr_status"], "reviewed")
        self.assertEqual(r["attributes"]["leverage"]["value"],
                         R.leverage_value(R.leverage_base(len(R.dependents(REAL).get("nvidia", ()))), 10))

    def test_ovr_from_counts_the_attributes_used(self):
        r = R.resolve(world(self.ATTRS), show_drafts=True)["nvidia"]
        self.assertEqual(r["ovr_from"], 4)

    def test_unrated_attributes_are_published_as_unrated(self):
        r = R.resolve(world(self.ATTRS), show_drafts=True)["nvidia"]
        self.assertIsNone(r["attributes"]["firepower"]["value"])


if __name__ == "__main__":
    unittest.main()
