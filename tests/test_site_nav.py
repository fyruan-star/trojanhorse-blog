"""Tests for the Prologue, Articles and Atlas navigation, the homepage and the Articles page.

They read the real pages, so setUpModule builds the site first."""
import datetime, hashlib, pathlib, re, subprocess, sys, types, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "content"))
sys.path.insert(0, str(HERE / "content" / "stories"))
import build  # noqa: E402
from home import ESSAY, STORIES, MORE_FROM_JOURNAL  # noqa: E402

SITE = HERE / "_site"
ESSAY_SHA256 = "7fb031df8b848c9ba296cf92c75472e73a870099a2255141bd946b54059b3c7a"
ORDER = [("ten-years.html", "Prologue"), ("articles.html", "Articles"), ("tech-atlas.html", "Atlas")]
CURRENT = {"ten-years.html": "ten-years.html", "articles.html": "articles.html", "tech-atlas.html": "tech-atlas.html", "index.html": None}


def setUpModule():
    subprocess.run([sys.executable, "build.py"], cwd=HERE, check=True, capture_output=True)


def read(name):
    return (SITE / name).read_text(encoding="utf-8")


def nav_of(page):
    return re.search(r'<nav class="sitenav[^>]*>(.*?)</nav>', page, re.S).group(1)


def internal_links(page):
    return {h.split("#")[0].split("?")[0] for h in re.findall(r'href="([^":]+\.html[^"]*)"', page)}


class Navigation(unittest.TestCase):
    def test_the_nav_is_on_all_four_pages_in_order(self):
        for name in CURRENT:
            with self.subTest(page=name):
                nav = nav_of(read(name))
                self.assertEqual(re.findall(r'href="([^"]+)"', nav), [h for h, _ in ORDER])
                self.assertEqual(re.findall(r'sitenav__w">([^<]+)<', nav), [w for _, w in ORDER])

    def test_every_nav_link_resolves(self):
        for href, _ in ORDER:
            self.assertTrue((SITE / href).exists(), href)

    def test_the_current_page_and_only_that_page_is_marked(self):
        for name, current in CURRENT.items():
            with self.subTest(page=name):
                marked = re.findall(r'href="([^"]+)" aria-current="page"', nav_of(read(name)))
                self.assertEqual(marked, [current] if current else [])

    def test_the_prologue_link_carries_its_dates(self):
        self.assertIn("2016 to 2026", nav_of(read("index.html")))


class Homepage(unittest.TestCase):
    def setUp(self):
        self.page = read("index.html")

    def test_francis_story_is_unchanged(self):
        # the hash of the essay as it stood before the navigation was added
        self.assertEqual(hashlib.sha256(ESSAY.encode()).hexdigest(), ESSAY_SHA256)
        self.assertIn(ESSAY, self.page)

    def test_only_the_latest_trojan_horse_is_featured(self):
        latest = build.stories_newest_first()[0]
        self.assertEqual(latest.SLUG, "marvell-lumentum")
        self.assertEqual(self.page.count('class="th__c"'), 1)
        self.assertIn("Trojan Horse of the Week", self.page)
        self.assertIn(f'<a href="{latest.SLUG}.html">{latest.TITLE}</a>', self.page)
        self.assertIn(latest.HOOK, self.page)
        self.assertIn("Continue reading", self.page)

    def test_the_rest_of_the_list_has_moved_off_the_homepage(self):
        for m in build.stories_newest_first()[1:]:
            self.assertNotIn(f'href="{m.SLUG}.html"', self.page, m.SLUG)

    def test_see_all_articles_follows_the_featured_story(self):
        self.assertRegex(self.page, r'href="articles\.html">See all articles')
        self.assertLess(self.page.index('class="th__c"'), self.page.index("See all articles"))

    def test_there_is_one_prologue_link_and_one_atlas_link(self):
        self.assertEqual(self.page.count('href="ten-years.html"'), 1)
        self.assertEqual(self.page.count('href="tech-atlas.html"'), 1)

    def test_the_podcast_is_visible_and_named(self):
        self.assertRegex(self.page, r'href="podcast\.html"[^>]*>.*?In The Belly</span>\s*</a>'.replace(".*?", "(?s:.*?)"))

    def test_the_byline_names_all_three(self):
        foot = re.search(r'<footer class="foot">(.*?)</footer>', self.page, re.S).group(1)
        for name in ("Francis Ruan", "Ryan Chian", "Timothy Zhang"):
            self.assertIn(name, foot)


class ArticlesPage(unittest.TestCase):
    def setUp(self):
        self.page = read("articles.html")
        self.stories = [__import__(n) for n in STORIES]

    def test_every_story_that_was_on_the_homepage_is_listed(self):
        self.assertEqual(len(self.stories), 7)
        self.assertEqual(self.page.count('class="th__c"'), 7)
        for m in self.stories:
            with self.subTest(slug=m.SLUG):
                self.assertIn(f'<a href="{m.SLUG}.html">{m.TITLE}</a>', self.page)
                self.assertIn(m.HOOK, self.page)
                self.assertIn(m.WEEK, self.page)
                self.assertTrue((SITE / f"{m.SLUG}.html").exists())

    def test_the_list_runs_newest_first(self):
        slugs = re.findall(r'<h2 class="th__t"><a href="([^"]+)\.html"', self.page)
        by_slug = {m.SLUG: build.story_date(m) for m in self.stories}
        dates = [by_slug[s] for s in slugs]
        self.assertEqual(dates, sorted(dates, reverse=True))
        self.assertEqual(slugs[0], "marvell-lumentum")

    def test_more_from_the_journal_comes_after_the_stories(self):
        self.assertLess(self.page.rindex('class="th__c"'), self.page.index("More from the journal"))
        for href, title, _ in MORE_FROM_JOURNAL:
            with self.subTest(href=href):
                self.assertIn(title, self.page)
                self.assertIn(f'<a href="{href}">', self.page)
                self.assertTrue((SITE / href).exists())


class Links(unittest.TestCase):
    def test_no_page_with_the_nav_has_a_broken_internal_link(self):
        for name in CURRENT:
            for link in internal_links(read(name)):
                with self.subTest(page=name, link=link):
                    self.assertTrue((SITE / link).exists())


class StoryDates(unittest.TestCase):
    def test_both_date_styles_are_read(self):
        self.assertEqual(build.story_date(types.SimpleNamespace(WEEK="Week of 9 November 2026")), datetime.date(2026, 11, 9))
        self.assertEqual(build.story_date(types.SimpleNamespace(WEEK="31 October 2026")), datetime.date(2026, 10, 31))


if __name__ == "__main__":
    unittest.main()
