"""Tests for the optional author line under a Trojan Horse story's title."""
import pathlib
import sys
import types
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402


def story(**extra):
    return types.SimpleNamespace(**extra)


class Byline(unittest.TestCase):
    def test_a_story_with_an_author_shows_the_name(self):
        out = build._byline(story(AUTHOR="Ryan Chian"))
        self.assertEqual(out, '<p class="plate__by">Ryan Chian</p>')

    def test_a_story_without_an_author_shows_nothing(self):
        self.assertEqual(build._byline(story()), "")

    def test_an_empty_author_shows_nothing(self):
        self.assertEqual(build._byline(story(AUTHOR="  ")), "")

    def test_the_marvell_story_page_carries_the_byline_under_the_title(self):
        page = (HERE / "_site" / "marvell-lumentum.html")
        if not page.exists():
            self.skipTest("run python3 build.py first")
        text = page.read_text(encoding="utf-8")
        title_at = text.index('<h1 class="plate__t">')
        by_at = text.index('<p class="plate__by">Ryan Chian</p>')
        self.assertGreater(by_at, title_at)
        self.assertLess(by_at, text.index("</header>"))

    def test_other_stories_carry_no_byline(self):
        page = (HERE / "_site" / "thorne-loyalty.html")
        if not page.exists():
            self.skipTest("run python3 build.py first")
        self.assertNotIn("plate__by", page.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
