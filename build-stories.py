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
STORIES = [
 dict(
  slug="buying-the-standard",
  lead="", line1="Buying", conn="the", line2="Standard",
  sub=("HOW A FORTY-PERSON COMPANY", "CHANGED HANDS FOR TWO BILLION"),
  intro=(
    "Databricks announced its acquisition of Tabular on 4 June 2024, at its own "
    "Data and AI Summit. Tabular was founded by Ryan Blue, Daniel Weeks and Jason "
    "Reid, the engineers who created Apache Iceberg while at Netflix, and it sold a "
    "managed storage platform built on that format. The company employed roughly "
    "forty people at the time of sale. Databricks has confirmed publicly only that "
    "the consideration exceeded one billion dollars; reporting in August 2024 put "
    "the figure closer to two billion. Iceberg is an open table format, and its "
    "principal rival in the market at the time was Delta Lake, which Databricks "
    "itself maintains."),
  takeaway="Databricks has confirmed only that the price exceeded one billion dollars.",
  sector="Enterprise Data", party="Databricks / Tabular", value="~$2B", dated="June 2024"),

 dict(
  slug="bought-then-freed",
  lead="", line1="Bought", conn="then", line2="Freed",
  sub=("HOW SEVEN HUNDRED MILLION DOLLARS", "BECAME AN OPEN SOURCE RELEASE"),
  intro=(
    "NVIDIA agreed to acquire Run:ai in April 2024 and closed the transaction in "
    "December of that year, following review by the United States Department of "
    "Justice and the European Commission. Run:ai was an Israeli company whose "
    "software orchestrated GPU workloads across Kubernetes clusters, scheduling and "
    "virtualising access to hardware that is otherwise allocated whole. The price "
    "was widely reported at approximately seven hundred million dollars, with some "
    "accounts putting it nearer eight hundred million. Neither party published a "
    "figure. On closing, NVIDIA stated that it would release the software as open "
    "source."),
  takeaway="NVIDIA open-sourced the software after the acquisition had closed.",
  sector="AI Infrastructure", party="NVIDIA / Run:ai", value="~$700M", dated="December 2024"),

 dict(
  slug="the-missing-fifth",
  lead="The", line1="Missing", conn="", line2="Fifth",
  sub=("HOW A THREE-YEAR-OLD BRAND", "REACHED A BILLION IN VALUE"),
  intro=(
    "Unilever completed its acquisition of Gr&uuml;ns on 1 June 2026. Gr&uuml;ns was "
    "founded in 2023 by Chad Janis and sells a daily greens supplement in gummy "
    "form, almost entirely by subscription and direct to the consumer. It reached "
    "roughly three hundred million dollars of annual revenue in under four years and "
    "was reported profitable within about fourteen months of launch. The transaction "
    "was reported at approximately one point two billion dollars, or seven hundred "
    "and sixty-seven million euro, and trade press placed that consideration against "
    "eighty percent of the shares rather than the whole. Unilever's half-year Form "
    "6-K records the completion and does not state the terms."),
  takeaway="Unilever's own filing confirms the completion and not the terms.",
  sector="Consumer Health", party="Unilever / Gr&uuml;ns", value="~$1.2B", dated="June 2026"),

 dict(
  slug="premium-without-profit",
  lead="", line1="Premium", conn="without", line2="Profit",
  sub=("HOW A LOSS-MAKING CHOCOLATIER", "DREW A HUNDRED AND SEVENTY PERCENT"),
  intro=(
    "Mars announced its offer for Hotel Chocolat on 16 November 2023 at five hundred "
    "and thirty-four million pounds, or three hundred and seventy-five pence per "
    "share in cash. The price represented a premium of approximately one hundred and "
    "seventy percent to the previous close. The transaction completed on 25 January "
    "2024. Hotel Chocolat was founded in 2004, sells through its own stores and "
    "online, and owns a hundred and forty acre cocoa estate and the Rabot Hotel in "
    "Saint Lucia. In the financial year to July 2023 the company moved from a pre-tax "
    "profit of twenty-one point seven million pounds to a loss of eight hundred "
    "thousand."),
  takeaway="The company had just posted a loss when the premium was agreed.",
  sector="Premium Consumer", party="Mars / Hotel Chocolat", value="&pound;534M", dated="November 2023"),

 dict(
  slug="the-margin-gap",
  lead="The", line1="Margin", conn="", line2="Gap",
  sub=("HOW A MEAL REPLACEMENT BRAND", "CROSSED INTO BIG FOOD"),
  intro=(
    "Danone announced its acquisition of Huel in March 2026 at approximately eight "
    "hundred and sixty million pounds. The Competition and Markets Authority cleared "
    "the transaction in August 2026. Huel sells complete-nutrition powders, ready to "
    "drink formats and bars, built first on a direct-to-consumer subscription and "
    "more recently through retail. In the financial year to 2024 the company recorded "
    "two hundred and fourteen million pounds of revenue at a fifty-nine percent gross "
    "margin, and eighteen point two million pounds of adjusted EBITDA. Revenue "
    "reached two hundred and fifty million pounds in the following year, a rise of "
    "sixteen percent."),
  takeaway="Fifty-nine percent at the gross line arrived as eight at EBITDA.",
  sector="Functional Nutrition", party="Danone / Huel", value="~&pound;860M", dated="March 2026"),

 dict(
  slug="two-versus-six",
  lead="", line1="Two", conn="versus", line2="Six",
  sub=("HOW ONE SPONSOR BOUGHT AND SOLD", "INSIDE A SINGLE YEAR"),
  intro=(
    "L Catterton took a majority stake in Good Culture in January 2026, in a "
    "transaction reported to value the business above five hundred million dollars. "
    "Good Culture sells cottage cheese and related cultured dairy. Revenue was "
    "approximately one hundred million dollars in 2023, close to double that in 2024, "
    "and tracking near two hundred and fifty million in 2025. Semcap Food and "
    "Nutrition invested a further fifty-five million dollars in February 2026. "
    "Separately, in August 2026, L Catterton sold Thorne to Procter and Gamble in a "
    "transaction reported at three point eight billion dollars, against forward "
    "revenue of roughly six hundred and fifty million."),
  takeaway="The same sponsor bought here and sold Thorne inside one year.",
  sector="Sponsor Strategy", party="L Catterton / Good Culture", value="&gt;$500M", dated="January 2026"),

 dict(
  slug="owning-the-clock",
  lead="", line1="Owning", conn="the", line2="Clock",
  sub=("HOW A LONGEVITY TEST CHANGED HANDS", "FOR AN UNDISCLOSED SUM"),
  intro=(
    "Infinite Epigenetics announced the acquisition of Tally Health on 29 April 2026 "
    "as an asset purchase. Terms were not disclosed by either party. Tally Health was "
    "co-founded in 2023 by the Harvard geneticist David Sinclair and sells an "
    "epigenetic biological age test alongside a line of supplements. The buyer also "
    "owns TruDiagnostic and states that it holds among the largest private datasets "
    "of adult DNA methylation. Tally Health continues to operate as a standalone "
    "consumer brand under Melanie Goldey, and Matthew Dawson remains chief executive "
    "of Infinite Epigenetics."),
  takeaway="No consideration was disclosed by either party.",
  sector="Longevity Tech", party="Infinite Epigenetics / Tally Health", value="Undisclosed", dated="April 2026"),
]

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
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="stylesheet" href="story.css">
</head>
<body>

<a class="back" href="index.html">&larr; The Trojan Horse</a>

<article class="sheet">

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
  <div class="opening"><p>{intro}</p></div>

  <!-- 05 KEY TAKEAWAY -->
  <p class="takeaway">{takeaway}</p>

  <!-- 06 FIXED BRAND MARK -->
  <figure class="mark"><img src="images/horse.png" alt="The Trojan Horse engraving"></figure>

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
    for i, s in enumerate(STORIES):
        lead = f'<span class="tt__lead">{s["lead"]}</span>' if s["lead"] else ""
        conn = f'<span class="tt__conn">{s["conn"]}</span>' if s["conn"] else ""
        plain = " ".join(x for x in (s["lead"], s["line1"], s["conn"], s["line2"]) if x)
        html = PAGE.format(
            plain=plain, lead=lead, conn=conn,
            line1=s["line1"], line2=s["line2"],
            sub1=s["sub"][0], sub2=s["sub"][1],
            intro=s["intro"], takeaway=s["takeaway"],
            party=s["party"], value=s["value"], dated=s["dated"],
            roman=ROMAN[i])
        (ROOT / f'{s["slug"]}.html').write_text(html, encoding="utf-8")
        print(f'{s["slug"]}.html')

    # point each book on the index at its own sheet
    idx = ROOT / "index.html"
    t = idx.read_text(encoding="utf-8")
    parts = t.split('<a class="story" href="#">')
    if len(parts) == len(STORIES) + 1:
        out = parts[0]
        for s, blk in zip(STORIES, parts[1:]):
            out += f'<a class="story" href="{s["slug"]}.html">' + blk
        idx.write_text(out, encoding="utf-8")
        print("index.html links wired")
    else:
        print(f"index links already wired ({len(parts)-1} placeholders found)")

if __name__ == "__main__":
    build()
