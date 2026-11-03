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


def rated(d, cid="nvidia", **over):
    rating = {"ovr": 90, "ovr_status": "draft", "ovr_reason": "Leads its row on revenue.",
              "ovr_evidence": [{"url": "https://example.com/a", "trust": "sourced"}],
              "ovr_updated": "2026-11-02", "ovr_by": "Claude (draft)"}
    rating.update(over)
    d["companies"][cid].update(rating)


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
        d = changed(lambda d: d["companies"]["nvidia"].update(
            {"attributes": {"scale": 99}, "badges": ["chokepoint"], "ovr_history": []}))
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
    def test_valid_draft_passes(self):
        self.assertEqual(errors_of(changed(rated)), [])

    def test_out_of_range_ovr_is_caught(self):
        for bad in (39, 100, 85.5, "90"):
            with self.subTest(bad=bad):
                self.assertTrue(any("ovr" in e for e in errors_of(changed(lambda d: rated(d, ovr=bad)))))

    def test_rating_needs_reason_evidence_and_status(self):
        cases = [dict(ovr_reason=""), dict(ovr_evidence=[]), dict(ovr_status="final"),
                 dict(ovr_evidence=[{"url": "https://x.com", "trust": "vibes"}]), dict(ovr_updated="Nov 2")]
        for over in cases:
            with self.subTest(over=over):
                self.assertNotEqual(errors_of(changed(lambda d: rated(d, **over))), [])

    def test_reason_follows_house_punctuation(self):
        for reason in ("Leads its row—by far.", "Leads; and grows.", "Leads its row?",
                       "Leads its row. It also grows."):
            with self.subTest(reason=reason):
                self.assertNotEqual(errors_of(changed(lambda d: rated(d, ovr_reason=reason))), [])

    def test_reason_may_contain_decimal_figures(self):
        d = changed(lambda d: rated(d, ovr_reason="Data Center revenue of $89.0bn, up 117%."))
        self.assertEqual(errors_of(d), [])

    def test_unrated_company_carries_no_rating_fields(self):
        d = changed(lambda d: rated(d, ovr=None))
        self.assertTrue(any("unrated" in e for e in errors_of(d)))


class Prose(unittest.TestCase):
    def test_semicolon_in_card_text_is_caught(self):
        d = changed(lambda d: d["placements"][0].update({"why": "Sells chips; and racks."}))
        self.assertTrue(any("semicolon" in e for e in errors_of(d)))


if __name__ == "__main__":
    unittest.main()
