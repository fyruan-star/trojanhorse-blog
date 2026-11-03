"""Nvidia's stats page, company-nvidia.html, laid out like an NBA player page.

The financial table comes from nvidia.json, written by
scripts/fetch_company.py from Nvidia's SEC filings. This file holds only the
words and the bio facts, each with its source.
"""

SLUG = "nvidia"
ATLAS = "nvidia"                 # the company's id in content/atlas/atlas.json
NAME = ["Nvidia"]                # one line per row of the big name
POSITION = "AI accelerators"     # the Atlas row it starts in
LOGO = {"file": "nvidia.svg", "w": 630.2, "h": 118.2}
TEAM = "#141414"                 # the hero colour
ACCENT = "#76B900"               # Nvidia green

WIKI = "https://en.wikipedia.org/wiki/Nvidia"
BIO = [
    ("Headquarters", "Santa Clara, Calif.", None),
    ("CEO", "Jensen Huang", WIKI),
    ("Ticker", "Nasdaq: NVDA", None),
    ("Employees", "42,000 (FY2026)", WIKI),
    ("Age", "33 years", None),
    ("Founded", "April 5, 1993", WIKI),
    ("IPO", "January 22, 1999", WIKI),
    ("Experience", "27 years public", None),
]
FOUNDED = 1993
IPO = 1999

LINKS = [
    ("Investor relations", "https://investor.nvidia.com/"),
    ("SEC filings", "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001045810&type=10-&dateb=&owner=include&count=40"),
]

ABOUT = [
    "Nvidia sells AI chips, the networking that joins them and the software "
    "that runs them, increasingly as complete racks. Its fiscal year ends in "
    "late January, so FY2026 is mostly calendar 2025.",
    "Read the table the way you would read a scoring line. Revenue went from "
    "$27.0 billion in FY2023 to $215.9 billion in FY2026, and the first half "
    "of FY2027 alone brought $177.8 billion. The YTD row is the season in "
    "progress.",
]
