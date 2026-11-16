"""Tests for the Atlas helmet in assets/images/helmets/: one shared design with
no crest or plume, which the map tints per sector."""
import pathlib, re, unittest
import xml.etree.ElementTree as ET

HERE = pathlib.Path(__file__).resolve().parent.parent
FOLDER = HERE / "assets" / "images" / "helmets"
HELMET = FOLDER / "helmet.svg"
ART = (HERE / "assets" / "atlas-map-art.js").read_text(encoding="utf-8")
NS = "{http://www.w3.org/2000/svg}"


class Helmet(unittest.TestCase):
    def test_one_shared_helmet_file(self):
        self.assertEqual([p.name for p in FOLDER.glob("*.svg")], ["helmet.svg"])
        self.assertIn('"images/helmets/helmet.svg"', ART)
        self.assertNotIn('"images/helmets/" + sid', ART)

    def test_no_crest_above_the_dome(self):
        # the dome's crown is at y=236 and the view starts just above it, so nothing can stand on top
        root = ET.parse(HELMET).getroot()
        x, y, w, h = (float(v) for v in root.get("viewBox").split())
        self.assertGreaterEqual(y, 216)
        self.assertLess(h / w, 1.5)

    def test_detail_is_drawn(self):
        root = ET.parse(HELMET).getroot()
        rivets = [c for c in root.iter(f"{NS}circle") if c.get("r") == "8.5"]
        self.assertGreaterEqual(len(rivets), 16, "rivets along the edges")
        self.assertGreaterEqual(len(list(root.iter(f"{NS}linearGradient"))), 3, "shaded body, band and cheeks")

    def test_white_and_grey_only_so_the_tint_carries_the_colour(self):
        text = HELMET.read_text(encoding="utf-8")
        for hexcol in re.findall(r"#([0-9A-Fa-f]{6})", text):
            with self.subTest(colour=hexcol):
                self.assertTrue(hexcol[0:2] == hexcol[2:4] == hexcol[4:6], f"#{hexcol} is not a grey")

    def test_plain_shapes_only(self):
        text = HELMET.read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"<(script|image|foreignObject)|\son\w+=|href=|url\(http", text))


if __name__ == "__main__":
    unittest.main()
