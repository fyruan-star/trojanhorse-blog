"""Tests for the sector helmets in assets/images/helmets/."""
import json, pathlib, re, sys, unittest
import xml.etree.ElementTree as ET

HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "content" / "atlas"))
import atlas_data as AD
import atlas_layout as L

FOLDER = HERE / "assets" / "images" / "helmets"
SECTORS = sorted(L.layout(AD.DATA)["sectors"])
NS = "{http://www.w3.org/2000/svg}"


def paths(sid):
    return [p.get("d") for p in ET.parse(FOLDER / f"{sid}.svg").getroot().iter(f"{NS}path")]


class Helmets(unittest.TestCase):
    def test_all_ten_sectors_have_a_helmet(self):
        self.assertEqual(len(SECTORS), 10)
        self.assertEqual(sorted(p.stem for p in FOLDER.glob("*.svg")), SECTORS)

    def test_every_helmet_is_the_same_helmet(self):
        self.assertEqual(len({paths(sid)[0] for sid in SECTORS}), 1)

    def test_every_sector_has_its_own_crest(self):
        crests = [tuple(paths(sid)[1:]) for sid in SECTORS]
        self.assertTrue(all(crests))
        self.assertEqual(len(set(crests)), 10)

    def test_files_are_plain_shapes_on_one_canvas(self):
        for sid in SECTORS:
            with self.subTest(sector=sid):
                text = (FOLDER / f"{sid}.svg").read_text(encoding="utf-8")
                self.assertIn('viewBox="0 0 800 840"', text)
                self.assertIsNone(re.search(r"<(script|image|foreignObject)|\\son\\w+=|href=", text))


if __name__ == "__main__":
    unittest.main()
