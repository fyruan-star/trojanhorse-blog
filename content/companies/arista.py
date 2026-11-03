"""Arista Networks' stats page, company-arista.html, laid out like an NBA
player page.

The financial table comes from arista.json, written by
scripts/fetch_company.py from Arista's SEC filings. This file holds only the
words and the bio facts, each with its source.
"""

SLUG = "arista"
ATLAS = "arista"                 # the company's id in content/atlas/atlas.json
NAME = ["Arista", "Networks"]    # one line per row of the big name
POSITION = "Networking"          # the Atlas row it starts in
LOGO = {"file": "arista.svg", "w": 1115, "h": 175}
TEAM = "#16325B"                 # Arista navy, from its logo
ACCENT = "#5AA9E6"

WIKI = "https://en.wikipedia.org/wiki/Arista_Networks"
BIO = [
    ("Headquarters", "Santa Clara, Calif.", None),
    ("CEO", "Jayshree Ullal", WIKI),
    ("Ticker", "NYSE: ANET", None),
    ("Employees", "5,115 (Dec 2025)", WIKI),
    ("Age", "22 years", None),
    ("Founded", "2004, as Arastra", WIKI),
    ("IPO", "June 2014", WIKI),
    ("Experience", "12 years public", None),
]
FOUNDED = 2004
IPO = 2014

LINKS = [
    ("Investor relations", "https://investors.arista.com/"),
    ("SEC filings", "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001596532&type=10-&dateb=&owner=include&count=40"),
]

ABOUT = [
    "Arista sells the high-speed Ethernet switches that connect servers inside "
    "cloud and AI data centers. It plays in the same row of the Atlas as Nvidia, "
    "which sells networking of its own.",
    "It runs a similar play at a smaller scale: revenue grew "
    "from $1.6 billion in FY2017 to $9.0 billion in FY2025, and the first half "
    "of 2026 brought $5.7 billion, up 36% on a year earlier by my arithmetic.",
]
