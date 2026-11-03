"""Tests for content/atlas/atlas_pages.py: profiles, sector standings, team pages and logos."""
import html, pathlib, re, sys, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "content" / "atlas"))
import atlas_data as AD
import atlas_pages as P

HEAD = "<!doctype html><html><head><title>{title}</title><meta name=\"description\" content=\"{desc}\">" \
       "<link rel=\"stylesheet\" href=\"site.css\"></head><body>"
FOOT = "</body></html>"
CTX = P.context(AD, HEAD, FOOT)


def text_of(page):
    return html.unescape(re.sub(r"<[^>]+>", " ", page))


class Logos(unittest.TestCase):
    def test_initials_match_the_map(self):
        cases = {"Oracle": "OR", "Palo Alto Networks": "PA", "Cursor (Anysphere)": "CU", "Foxconn, Quanta, Wistron": "FQ",
                 "AT&T": "AT", "SK hynix": "SH"}
        for name, want in cases.items():
            with self.subTest(name=name):
                self.assertEqual(P.initials(name), want)

    def test_a_company_with_a_logo_shows_the_file(self):
        out = P.logo_html(CTX, "nvidia", "md")
        self.assertIn('src="../logos/nvidia.svg"', out)
        self.assertNotIn("lg--mono", out)

    def test_a_company_without_a_logo_gets_a_monogram_in_its_sector_colour(self):
        self.assertNotIn("logo", AD.DATA["companies"]["broadcom"])
        out = P.logo_html(CTX, "broadcom", "md")
        self.assertIn("lg--mono", out)
        self.assertIn("c-silicon", out)
        self.assertIn(">BR<", out)
        self.assertNotIn("<img", out)

    def test_a_dark_logo_sits_on_a_dark_ground(self):
        self.assertIn("lg--dark", P.logo_html(CTX, "blue_owl", "md"))


class HeadlineStats(unittest.TestCase):
    def test_every_value_comes_from_the_key_figure(self):
        for p in AD.DATA["placements"]:
            for s in P.headline_stats(p):
                with self.subTest(company=p["company"], value=s["value"]):
                    self.assertIn(s["value"].lstrip("+-−").lstrip("$").replace("$", ""), p["key_figure"])

    def test_at_most_four(self):
        self.assertTrue(all(len(P.headline_stats(p)) <= 4 for p in AD.DATA["placements"]))

    def test_written_stats_win_over_derived_ones(self):
        p = {"key_figure": "Revenue $5bn, up 10%.", "stats": [{"label": "Growth", "value": "+10%"}]}
        self.assertEqual(P.headline_stats(p), [{"label": "Growth", "value": "+10%"}])

    def test_derived_stats_take_the_first_amount_of_each_sentence(self):
        p = {"key_figure": "Data Center $89.0bn, quarter to 26 Jul 2026. Total revenue $96.2bn. No figure here."}
        self.assertEqual([s["value"] for s in P.headline_stats(p)], ["$89.0bn", "$96.2bn"])
        self.assertEqual(P.headline_stats(p)[0]["label"], "Data Center, quarter to 26 Jul 2026")


class Profile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.oracle = P.profile_page(CTX, "oracle")

    def test_sections_in_order_with_ratings_directly_below_the_hero(self):
        ids = re.findall(r'<section class="pf__[a-z]+" id="([a-z-]+)"', self.oracle)
        self.assertEqual(ids[:2], ["hero", "ratings"])
        self.assertEqual([i for i in ids if i in ("figures", "profile", "connections", "standing")],
                         ["figures", "profile", "connections", "standing"])

    def test_hero_has_name_sector_rank_team_and_ovr(self):
        hero = self.oracle[self.oracle.index('id="hero"'):self.oracle.index('id="ratings"')]
        t = text_of(hero)
        for want in ("Oracle", "Cloud and compute", "Second string", "Microsoft and OpenAI", "74", "Role player"):
            with self.subTest(want=want):
                self.assertIn(want, t)

    def test_six_attributes_and_a_radar(self):
        ratings = self.oracle[self.oracle.index('id="ratings"'):]
        for label in ("Dominance", "Momentum", "Leverage", "Durability", "Firepower", "Deal Heat"):
            self.assertIn(label, ratings)
        self.assertIn('class="pf__radar"', ratings)

    def test_connections_link_to_profiles_and_the_map(self):
        self.assertIn('href="openai.html"', self.oracle)
        self.assertIn('href="../tech-atlas.html#c-openai"', self.oracle)

    def test_bio_cells_show_only_filled_fields(self):
        CTX.companies["oracle"] = {**AD.DATA["companies"]["oracle"],
                                   "bio": {"hq": "Somewhere", "sources": {"hq": "https://example.com/hq"}}}
        try:
            page = P.profile_page(CTX, "oracle")
        finally:
            CTX.companies["oracle"] = AD.DATA["companies"]["oracle"]
        cells = re.findall(r'<div class="pf__cell"><span>([^<]+)</span>', page)
        self.assertEqual(cells, ["HQ"])

    def test_no_bio_means_no_bio_section(self):
        self.assertNotIn('id="bio"', P.profile_page(CTX, "groq") if "bio" not in AD.DATA["companies"]["groq"] else "")

    def test_page_is_found_and_indexed(self):
        self.assertIn('<link rel="canonical" href="https://trojanhorse.blog/atlas/oracle.html">', self.oracle)
        self.assertIn('href="../site.css"', self.oracle)
        self.assertIn("<title>Oracle", self.oracle)

    def test_no_braces_leak(self):
        self.assertNotRegex(text_of(self.oracle), r"[{}]")

    def test_every_company_has_a_page(self):
        for cid in AD.DATA["companies"]:
            with self.subTest(cid=cid):
                self.assertIn("<h1", P.profile_page(CTX, cid))

    def test_a_backer_without_a_card_still_gets_a_page(self):
        page = P.profile_page(CTX, "softbank")
        self.assertIn("SoftBank", page)
        self.assertNotIn('id="standing"', page)


class StandingsPage(unittest.TestCase):
    def test_rows_follow_ovr(self):
        page = P.standings_page(CTX, "silicon")
        names = re.findall(r'<td class="st__co"><a href="([a-z0-9_]+)\.html"', page)
        ovrs = [AD.RATINGS[n]["ovr"] for n in names]
        self.assertEqual(ovrs, sorted(ovrs, reverse=True))
        self.assertEqual(names[0], "asml")

    def test_columns_for_the_six_attributes(self):
        page = P.standings_page(CTX, "silicon")
        for short in ("DOM", "MOM", "LEV", "DUR", "FIRE", "HEAT"):
            self.assertIn(f">{short}<", page)

    def test_rows_carry_logos_and_teams(self):
        page = P.standings_page(CTX, "silicon")
        self.assertIn('src="../logos/nvidia.svg"', page)
        self.assertIn("Microsoft and OpenAI", page)


class TeamPage(unittest.TestCase):
    def test_roster_and_team_ovr(self):
        team = next(t for t in CTX.rosters if t["id"] == "nvidia")
        page = P.team_page(CTX, team)
        self.assertIn("Nvidia", page)
        self.assertIn(str(team["ovr"]), page)
        for m in team["members"]:
            self.assertIn(f'href="{m["company"]}.html"', page)
        self.assertIn('href="../tech-atlas.html#t-nvidia"', page)

    def test_index_lists_every_team(self):
        page = P.teams_page(CTX)
        for t in CTX.rosters:
            self.assertIn(f'href="team-{t["id"]}.html"', page)


if __name__ == "__main__":
    unittest.main()
