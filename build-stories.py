#!/usr/bin/env python3
"""Emit one story page per deal from a single template.

Every page is the same sheet: the seven mapped fields from the opening
template and nothing else. The brand mark is fixed. Facts only at this stage,
no argument, so the slots below carry specifics and dates and no reading of
them.
"""
import pathlib, re

ROOT = pathlib.Path(__file__).parent
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII"]

# 01 title is split the way the template splits it: a small italic lead, a
# large line, an optional small italic connector, a second large line.
from stories_data import STORIES

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{plain} | The Trojan Horse</title>
<meta name="description" content="{party} &middot; {value} &middot; {dated}.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&display=swap" rel="stylesheet">
<link rel="icon" href="/favicon.ico?v=2" sizes="any">
<link rel="icon" type="image/png" href="/favicon.png?v=2">
<link rel="apple-touch-icon" href="/apple-touch-icon.png?v=2">
<link rel="stylesheet" href="story.css">
</head>
<body>

<a class="back" href="strategemata.html">&larr; Strategemata</a>

<article class="sheet sheet--long">

  <!-- 01 TITLE -->
  <h1 class="tt">
    {lead}<span class="tt__big">{line1}</span>
    <span class="tt__row">{conn}<span class="tt__big">{line2}</span></span>
  </h1>

  <!-- 02 SUBTITLE -->
  <p class="sub">{sub1}<br>{sub2}</p>

  <!-- 03 BYLINE -->
  <p class="byline">Francis Ruan</p>

  <!-- 04 OPENING TEXT -->
  <div class="opening"><p class="lede">{opening}</p></div>

  <div class="body">
{sections}
  </div>

  <!-- 05 KEY TAKEAWAY -->
  <p class="takeaway">{takeaway}</p>

  <!-- 06 FIXED BRAND MARK -->
  <figure class="mark"><img src="images/horse.png" alt="The Trojan Horse engraving"></figure>

  <div class="srcs">
    <h3>Sources</h3>
    <ol>
{srcs}
    </ol>
  </div>

  <!-- 07 PUBLICATION FOOTER -->
  <footer class="colophon">
    <p class="colophon__loc">At Los Angeles</p>
    <p>Published by <em>The Trojan Horse</em></p>
    <p>No. {roman} &middot; {dated}</p>
    <p class="colophon__last">{party} &middot; {value}</p>
  </footer>

</article>

</body>
</html>
"""

def build():
    for i, st in enumerate(STORIES):
        lead = f'<span class="tt__lead">{st["lead"]}</span>' if st["lead"] else ""
        conn = f'<span class="tt__conn">{st["conn"]}</span>' if st["conn"] else ""
        plain = " ".join(x for x in (st["lead"], st["line1"], st["conn"], st["line2"]) if x)

        secs = []
        for head, paras in st["sections"]:
            secs.append(f'    <h2 class="h2">{head}</h2>')
            secs.extend(f"    <p>{para}</p>" for para in paras)
        srcs = "\n".join(f"      <li>{x}</li>" for x in st["srcs"])

        html = PAGE.format(
            plain=plain, lead=lead, conn=conn,
            line1=st["line1"], line2=st["line2"],
            sub1=st["sub"][0], sub2=st["sub"][1],
            opening=st["opening"], sections="\n".join(secs),
            takeaway=st["takeaway"], srcs=srcs,
            party=st["party"], value=st["value"], dated=st["dated"],
            roman=ROMAN[i])
        (ROOT / f'{st["slug"]}.html').write_text(html, encoding="utf-8")
        print(f'{st["slug"]}.html')


if __name__ == "__main__":
    build()
