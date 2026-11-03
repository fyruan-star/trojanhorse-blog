"""Tests for content/atlas/atlas_teams.py: team rules, team OVR and sector standings."""
import copy, json, pathlib, sys, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "content" / "atlas"))
import atlas_teams as T

REAL = json.loads((HERE / "content/atlas/atlas.json").read_text(encoding="utf-8"))


def line(a, b, kind):
    return {"from": a, "to": b, "type": kind}


def small(lines, teams=None, overrides=None):
    """A tiny world: two teams, captains a (team A) and b with co-captain c (team B), and companies x, y, z, w."""
    companies = {k: {"name": k.upper(), "sector": "silicon"} for k in "abcxyzw"}
    for cid, (team, reason) in (overrides or {}).items():
        companies[cid].update(team=team, team_reason=reason)
    return {"companies": companies, "relationships": lines,
            "teams": teams or [{"id": "ta", "name": "A", "captains": ["a"]}, {"id": "tb", "name": "B", "captains": ["b", "c"]}]}


class Assign(unittest.TestCase):
    def test_captains_lead_their_teams(self):
        out = T.assign(small([]))
        self.assertEqual(out["members"]["a"], {"team": "ta", "role": "captain", "via": None})
        self.assertEqual(out["members"]["c"]["role"], "co-captain")

    def test_a_company_with_no_tie_is_independent(self):
        self.assertNotIn("x", T.assign(small([]))["members"])

    def test_the_heaviest_tie_to_a_captain_wins(self):
        out = T.assign(small([line("x", "a", "supply"), line("b", "x", "investment")]))
        self.assertEqual(out["members"]["x"], {"team": "tb", "role": "backed", "via": "b"})

    def test_ties_to_co_captains_add_up(self):
        out = T.assign(small([line("x", "a", "supply"), line("x", "b", "alliance"), line("x", "c", "license")]))
        self.assertEqual(out["members"]["x"]["team"], "tb")

    def test_ownership_beats_every_other_tie(self):
        lines = [line("b", "x", "investment"), line("c", "x", "investment"), line("a", "x", "ownership")]
        self.assertEqual(T.assign(small(lines))["members"]["x"], {"team": "ta", "role": "owned", "via": "a"})

    def test_rivalry_counts_for_nothing(self):
        self.assertNotIn("x", T.assign(small([line("x", "a", "rivalry")]))["members"])

    def test_capital_only_pulls_the_company_that_receives_it(self):
        self.assertNotIn("x", T.assign(small([line("x", "a", "investment")]))["members"])

    def test_an_even_score_is_a_tie_left_unassigned(self):
        out = T.assign(small([line("x", "a", "supply"), line("x", "b", "supply")]))
        self.assertNotIn("x", out["members"])
        self.assertEqual(out["ties"], {"x": ["ta", "tb"]})

    def test_an_override_settles_a_tie(self):
        d = small([line("x", "a", "supply"), line("x", "b", "supply")], overrides={"x": ("tb", "Larger contract.")})
        out = T.assign(d)
        self.assertEqual(out["members"]["x"], {"team": "tb", "role": "override", "via": None})
        self.assertEqual(out["ties"], {})

    def test_an_override_can_make_a_company_independent(self):
        d = small([line("a", "x", "ownership")], overrides={"x": ("independent", "Largest owner is on no team.")})
        self.assertNotIn("x", T.assign(d)["members"])

    def test_a_company_owned_by_a_member_joins_once_removed(self):
        lines = [line("a", "x", "ownership"), line("x", "y", "ownership"), line("y", "z", "ownership")]
        out = T.assign(small(lines))
        self.assertEqual(out["members"]["y"], {"team": "ta", "role": "owned", "via": "x"})
        self.assertNotIn("z", out["members"])

    def test_the_role_names_the_direction_of_supply(self):
        self.assertEqual(T.assign(small([line("x", "a", "supply")]))["members"]["x"]["role"], "supplier")
        self.assertEqual(T.assign(small([line("a", "x", "supply")]))["members"]["x"]["role"], "customer")

    def test_assign_never_changes_its_input(self):
        d = small([line("x", "a", "supply")])
        before = copy.deepcopy(d)
        T.assign(d)
        self.assertEqual(d, before)


class TeamOvr(unittest.TestCase):
    def test_starting_five_weights(self):
        self.assertEqual(T.team_ovr([90, 80, 70, 60, 50]), round(.3 * 90 + .25 * 80 + .2 * 70 + .15 * 60 + .1 * 50))

    def test_only_the_best_five_count(self):
        self.assertEqual(T.team_ovr([90, 80, 70, 60, 50, 99]), T.team_ovr([99, 90, 80, 70, 60]))

    def test_fewer_than_five_rescale_the_weights(self):
        self.assertEqual(T.team_ovr([90, 60]), round((.3 * 90 + .25 * 60) / .55))

    def test_no_rated_member_means_no_team_ovr(self):
        self.assertIsNone(T.team_ovr([]))


class RealTeams(unittest.TestCase):
    """The rosters the rules and the overrides in atlas.json give today."""
    @classmethod
    def setUpClass(cls):
        cls.members = T.assign(REAL)["members"]

    def team_of(self, cid):
        return self.members.get(cid, {}).get("team")

    def test_settled_ties(self):
        self.assertEqual(self.team_of("amd"), "microsoft_openai")
        self.assertEqual(self.team_of("broadcom"), "google")
        self.assertEqual(self.team_of("nebius"), "microsoft_openai")

    def test_tsmc_follows_its_larger_customer(self):
        self.assertEqual(self.team_of("tsmc"), "nvidia")

    def test_tiktok_is_independent(self):
        self.assertIsNone(self.team_of("tiktok"))

    def test_no_tie_is_left_open(self):
        self.assertEqual(T.assign(REAL)["ties"], {})

    def test_every_team_has_at_least_three_members(self):
        for t in REAL["teams"]:
            with self.subTest(team=t["id"]):
                self.assertGreaterEqual(sum(1 for m in self.members.values() if m["team"] == t["id"]), T.MIN_MEMBERS)


class Standings(unittest.TestCase):
    def setUp(self):
        self.data = {"companies": {"a": {"name": "Alpha"}, "b": {"name": "Beta"}, "c": {"name": "Gamma"}, "d": {"name": "Delta"}},
                     "placements": [{"company": k, "sector": "s", "row": "r", "rank": "starter"} for k in "abcd"]
                                   + [{"company": "a", "sector": "other", "row": "r", "rank": "starter"}]}
        self.ovr = {"a": 80, "b": 90, "c": 80, "d": None}

    def test_ranked_by_ovr_then_name(self):
        out = T.standings(self.data, "s", lambda k: self.ovr[k])
        self.assertEqual([r["company"] for r in out["ranked"]], ["b", "a", "c"])
        self.assertEqual([r["rank"] for r in out["ranked"]], [1, 2, 2])

    def test_unrated_companies_are_listed_apart(self):
        self.assertEqual([r["company"] for r in T.standings(self.data, "s", lambda k: self.ovr[k])["unrated"]], ["d"])

    def test_only_the_sector_asked_for(self):
        self.assertEqual([r["company"] for r in T.standings(self.data, "other", lambda k: self.ovr[k])["ranked"]], ["a"])

    def test_a_company_in_two_rows_of_a_sector_is_listed_once_at_its_best_depth(self):
        self.data["placements"].append({"company": "b", "sector": "s", "row": "r2", "rank": "practice_squad"})
        self.data["placements"].insert(0, {"company": "c", "sector": "s", "row": "r0", "rank": "second_string"})
        out = T.standings(self.data, "s", lambda k: self.ovr[k])
        names = [r["company"] for r in out["ranked"]]
        self.assertEqual(names, ["b", "a", "c"])
        rows = {r["company"]: r for r in out["ranked"]}
        self.assertEqual((rows["b"]["row"], rows["c"]["row"], rows["c"]["depth"]), ("r", "r", "starter"))

    def test_change_from_the_last_recorded_rating(self):
        self.data["companies"]["b"]["ovr_history"] = [{"ovr": 85, "date": "2026-10-01", "by": "x", "note": "y"}]
        self.data["companies"]["a"]["ovr_history"] = [{"ovr": 82, "date": "2026-10-01", "by": "x", "note": "y"}]
        rows = {r["company"]: r for r in T.standings(self.data, "s", lambda k: self.ovr[k])["ranked"]}
        self.assertEqual((rows["b"]["change"], rows["a"]["change"], rows["c"]["change"]), (5, -2, None))


if __name__ == "__main__":
    unittest.main()
