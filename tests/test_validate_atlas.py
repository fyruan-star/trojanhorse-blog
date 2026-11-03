"""Tests for scripts/validate_atlas.py. Run: python3 -m unittest discover tests"""
import copy, json, pathlib, sys, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "scripts"))
import validate_atlas as V

REAL = json.loads((HERE / "content/atlas/atlas.json").read_text(encoding="utf-8"))


def changed(fn):
    """A deep copy of the real data with one change applied to the copy."""
    d = copy.deepcopy(REAL)
    fn(d)
    return d


def errors_of(d):
    return V.validate(d)[0]


EV = [{"url": "https://example.com/a", "trust": "sourced"}]


def rated(d, cid="nvidia", key="dominance", **over):
    """Give one company one attribute, on the copy."""
    a = {"value": 90, "reason": "Leads its row on revenue.", "evidence": EV, "status": "draft"}
    if key == "leverage":
        a = {"adjust": 20, "reason": "Sole supplier of its part.", "evidence": EV, "status": "draft"}
    a.update(over)
    d["companies"][cid].setdefault("attributes", {})[key] = a


def badged(d, cid="nvidia", **over):
    b = {"id": "in_play", "reason": "Reported to be in talks.", "evidence": EV, "status": "draft"}
    b.update(over)
    d["companies"][cid].setdefault("badges", []).append(b)


class RealData(unittest.TestCase):
    def test_real_atlas_has_no_errors(self):
        errors, _ = V.validate(REAL)
        self.assertEqual(errors, [])

    def test_counts_match_the_old_atlas(self):
        self.assertEqual(len(REAL["sectors"]), 9)
        self.assertEqual(len(REAL["placements"]), 159)
        self.assertEqual(len(REAL["relationships"]), 89)


class Relationships(unittest.TestCase):
    def test_unknown_endpoint_is_caught(self):
        d = changed(lambda d: d["relationships"][0].update({"to": "no_such_co"}))
        self.assertTrue(any("no_such_co" in e for e in errors_of(d)))

    def test_exact_duplicate_is_caught(self):
        d = changed(lambda d: d["relationships"].append(dict(d["relationships"][0])))
        self.assertTrue(any("duplicate relationship" in e for e in errors_of(d)))

    def test_reversed_symmetric_duplicate_is_caught(self):
        def rev(d):
            r = next(x for x in d["relationships"] if x["type"] == "rivalry")
            d["relationships"].append({**r, "from": r["to"], "to": r["from"]})
        self.assertTrue(any("duplicate relationship" in e for e in errors_of(changed(rev))))

    def test_same_pair_with_a_different_type_is_allowed(self):
        def both(d):
            r = next(x for x in d["relationships"] if x["type"] == "rivalry")
            d["relationships"].append({**r, "type": "alliance"})
        self.assertEqual(errors_of(changed(both)), [])

    def test_rejected_line_cannot_come_back(self):
        def back(d):
            d["relationships"].append({**d["relationships"][0], "from": "stripe", "to": "paypal", "type": "rivalry"})
        self.assertTrue(any("rejected" in e for e in errors_of(changed(back))))

    def test_bad_type_trust_and_dates_are_caught(self):
        d = changed(lambda d: d["relationships"][0].update(
            {"type": "friendship", "trust": "primary", "added": "23 Oct"}))
        errs = errors_of(d)
        self.assertTrue(any("type" in e for e in errs))
        self.assertTrue(any("trust" in e for e in errs))
        self.assertTrue(any("added" in e for e in errs))

    def test_inferred_line_must_be_ownership(self):
        def inf(d):
            r = next(x for x in d["relationships"] if x["type"] == "rivalry")
            r["trust"] = "inferred"
        self.assertTrue(any("inferred" in e for e in errors_of(changed(inf))))


class Companies(unittest.TestCase):
    def test_company_without_sector_is_caught(self):
        d = changed(lambda d: d["companies"]["nvidia"].pop("sector"))
        self.assertTrue(any("nvidia" in e and "sector" in e for e in errors_of(d)))

    def test_home_sector_must_be_one_it_plays_in(self):
        d = changed(lambda d: d["companies"]["nvidia"].update({"sector": "fintech"}))
        self.assertTrue(any("nvidia" in e for e in errors_of(d)))

    def test_misspelt_field_is_caught(self):
        d = changed(lambda d: d["companies"]["nvidia"].update({"descripton": "x"}))
        self.assertTrue(any("descripton" in e for e in errors_of(d)))

    def test_reserved_extension_fields_are_allowed(self):
        d = changed(lambda d: d["companies"]["nvidia"].update({"ovr_history": []}))
        self.assertEqual(errors_of(d), [])


class Placements(unittest.TestCase):
    def test_unknown_row_and_rank_are_caught(self):
        d = changed(lambda d: d["placements"][0].update({"row": "nope", "rank": "bench"}))
        errs = errors_of(d)
        self.assertTrue(any("row" in e for e in errs))
        self.assertTrue(any("rank" in e for e in errs))

    def test_duplicate_card_is_caught(self):
        d = changed(lambda d: d["placements"].append(dict(d["placements"][0])))
        self.assertTrue(any("duplicate card" in e for e in errors_of(d)))

    def test_plain_http_source_is_caught(self):
        d = changed(lambda d: d["placements"][0].update({"source": "http://example.com"}))
        self.assertTrue(any("https" in e for e in errors_of(d)))


class Ratings(unittest.TestCase):
    def test_valid_draft_attribute_passes(self):
        self.assertEqual(errors_of(changed(rated)), [])

    def test_out_of_range_value_is_caught(self):
        for bad in (39, 100, 85.5, "90"):
            with self.subTest(bad=bad):
                self.assertTrue(any("value" in e for e in errors_of(changed(lambda d: rated(d, value=bad)))))

    def test_unrated_attribute_needs_no_evidence(self):
        self.assertEqual(errors_of(changed(lambda d: rated(d, value=None, evidence=[], reason="No growth figure is stated."))), [])

    def test_rated_attribute_needs_reason_evidence_and_status(self):
        cases = [dict(reason=""), dict(evidence=[]), dict(status="final"),
                 dict(evidence=[{"url": "https://x.com", "trust": "vibes"}])]
        for over in cases:
            with self.subTest(over=over):
                self.assertNotEqual(errors_of(changed(lambda d: rated(d, **over))), [])

    def test_leverage_stores_adjust_not_value(self):
        self.assertEqual(errors_of(changed(lambda d: rated(d, key="leverage"))), [])
        self.assertTrue(any("adjust" in e for e in errors_of(changed(lambda d: rated(d, key="leverage", value=80)))))
        self.assertTrue(any("adjust" in e for e in errors_of(changed(lambda d: rated(d, key="leverage", adjust=60)))))

    def test_unknown_attribute_is_caught(self):
        self.assertTrue(any("unknown attribute" in e for e in errors_of(changed(lambda d: rated(d, key="speed")))))

    def test_stored_ovr_is_rejected(self):
        d = changed(lambda d: d["companies"]["nvidia"].update({"ovr": 90}))
        self.assertTrue(any("calculated" in e for e in errors_of(d)))

    def test_companies_without_a_card_are_not_rated(self):
        self.assertTrue(any("card" in e for e in errors_of(changed(lambda d: rated(d, cid="softbank")))))

    def test_badges(self):
        self.assertEqual(errors_of(changed(badged)), [])
        self.assertTrue(any("calculated" in e for e in errors_of(changed(lambda d: badged(d, id="chokepoint")))))
        self.assertTrue(any("twice" in e for e in errors_of(changed(lambda d: (badged(d), badged(d))))))
        self.assertTrue(any("evidence" in e for e in errors_of(changed(lambda d: badged(d, evidence=[])))))

    def test_reason_follows_house_punctuation(self):
        for reason in ("Leads its row\u2014by far.", "Leads; and grows.", "Leads its row?",
                       "Leads its row. It also grows."):
            with self.subTest(reason=reason):
                self.assertNotEqual(errors_of(changed(lambda d: rated(d, reason=reason))), [])

    def test_reason_may_contain_decimal_figures(self):
        self.assertEqual(errors_of(changed(lambda d: rated(d, reason="Data Center revenue of $89.0bn, up 117%."))), [])


class Prose(unittest.TestCase):
    def test_semicolon_in_card_text_is_caught(self):
        d = changed(lambda d: d["placements"][0].update({"why": "Sells chips; and racks."}))
        self.assertTrue(any("semicolon" in e for e in errors_of(d)))


if __name__ == "__main__":
    unittest.main()
