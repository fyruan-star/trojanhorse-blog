"""Tech Atlas, sector 9: Telecom and connectivity."""

ENT = {
 "att": ("AT&T", "US wireless and fiber carrier."),
 "verizon": ("Verizon", "US wireless carrier."),
 "tmobile": ("T-Mobile US", "US wireless carrier."),
 "ericsson": ("Ericsson", "Mobile network equipment."),
 "nokia": ("Nokia", "Mobile and fixed network equipment."),
 "zte": ("ZTE", "Chinese network equipment maker."),
 "starlink": ("Starlink (SpaceX)", "Low-orbit satellite broadband."),
 "cloudflare": ("Cloudflare", "Network and security services that sit between users and websites."),
 "akamai": ("Akamai", "Content delivery and security."),
}

SECTOR = dict(
 id="telecom", name="Telecom and connectivity", band="end",
 blurb="The carriers, the equipment makers, the satellites and the networks that carry everything else.",
 positions=[

  dict(id="carriers", name="US carriers",
   metric=("AT&T's Q3 2026: 379,000 postpaid phone net adds at 0.92% churn, 442,000 fiber net adds and 327,000 fixed wireless adds. Debt of $159.6bn. Verizon guided to the upper half of 750,000 to 1 million postpaid phone net adds for 2026."),
   metric_src="https://about.att.com/story/2026/3q-earnings.html",
   players=[
    dict(e="att", t="starter", stat="Q3 2026: 379,000 postpaid phone net adds, churn 0.92%, 442,000 fiber adds. Plans over 60 million fiber locations by 2030.",
     why="Sells wireless and fiber together.", cond="Total debt of $159.6bn, which it attributes partly to spectrum purchases.",
     src="https://about.att.com/story/2026/3q-earnings.html"),
    dict(e="verizon", t="starter", conf="reported", stat="Raised 2026 guidance twice. First positive first-quarter postpaid phone net adds since 2013. Q3 results due 26 October 2026.",
     why="Turnaround after years of subscriber losses.", cond="Q3 results had not been reported when this was compiled.",
     src="https://www.hudson-labs.com/research/verizon-q3-2026-earnings-preview-vz-guidance-estimates-key"),
    dict(e="tmobile", t="starter", conf="reported", stat="No 2026 results were verified in this research. A report says Deutsche Telekom is weighing a full takeover (unverified).",
     why="Largest 5G network by coverage claims.", cond="Figures not checked here.",
     src="https://about.att.com/story/2026/3q-earnings.html"),
   ]),

  dict(id="ran", name="Mobile network equipment",
   metric=("Dell'Oro's 1H26 ranking: Huawei, Ericsson, Nokia, ZTE and Samsung hold 96% of the RAN market. Huawei and Ericsson together held nearly two-thirds in late 2025. The market was flat in 2Q 2026, with Huawei strong and Ericsson softer than expected."),
   metric_src="https://www.delloro.com/news/ran-market-growth-continues-in-2q-2026/",
   players=[
    dict(e="huawei", t="starter", stat="Number one globally by RAN revenue and gained share outside China (Dell'Oro).",
     why="Competitive on price and technology where it is allowed to sell.", cond="Western restrictions.",
     src="https://www.delloro.com/news/ran-market-growth-continues-in-2q-2026/"),
    dict(e="ericsson", t="starter", stat="Clear number two. Q2 2026 performance softer than expected (Dell'Oro).",
     why="Largest Western supplier.", cond="Huawei's share gains.",
     src="https://www.delloro.com/news/ran-market-growth-continues-in-2q-2026/"),
    dict(e="nokia", t="second", stat="Third in 1H26. Lost ground between 2019 and 2025 (Dell'Oro).",
     why="Western alternative with a broad portfolio.", cond="Winning share with AI-focused radio products.",
     src="https://www.delloro.com/news/ran-market-growth-continues-in-2q-2026/"),
    dict(e="zte", t="second", stat="Fourth in 1H26 (Dell'Oro).", why="Chinese domestic demand.", cond="Western restrictions.",
     src="https://www.delloro.com/news/ran-market-growth-continues-in-2q-2026/"),
    dict(e="samsung", t="second", stat="Fifth in 1H26 (Dell'Oro).", why="Sells mainly in the US, Japan and Korea.", cond="Small share against the top two.",
     src="https://www.delloro.com/news/ran-market-growth-continues-in-2q-2026/"),
   ]),

  dict(id="satellite", name="Satellite connectivity",
   metric=("Starlink reached 13.6 million subscribers in Q3 2026, up from 12 million in Q2 and 10.3 million in Q1, with average revenue of $69 a user. Connectivity revenue was $5.25bn in the quarter."),
   metric_src="https://broadbandbreakfast.com/starlink-reaches-13-6-million-subscribers-globally-as-spacex-revenue-jumps-161/",
   players=[
    dict(e="starlink", t="starter",
     stat="13.6 million subscribers across 174 markets, with 1.6 million added in Q3 2026. SpaceX's total revenue was $14.6bn in the quarter, up 161%, with AI the largest business at $7.56bn (reported).",
     why="Launches its own satellites at a cost no rival matches.", cond="SpaceX counts service lines, so a household with two plans counts twice.",
     src="https://broadbandbreakfast.com/starlink-reaches-13-6-million-subscribers-globally-as-spacex-revenue-jumps-161/"),
   ]),

  dict(id="edge", name="Network edge and delivery",
   metric=("Cloudflare's Q2 2026 revenue was $696.1m, up 36%, with 4,698 customers above $100,000 a year, up 27%. Gross margin fell 3.2 points to 73.1% on higher network costs."),
   metric_src="https://www.sec.gov/Archives/edgar/data/0001477333/000147733326000053/q226exhibit991.htm",
   players=[
    dict(e="cloudflare", t="starter", stat="Revenue $696.1m, up 36%. Non-GAAP operating income $96.1m. Raised full-year guidance.",
     why="Sells security and delivery from one global network, and is building for AI agents.", cond="Gross margin down as paid traffic grows.",
     src="https://www.sec.gov/Archives/edgar/data/0001477333/000147733326000053/q226exhibit991.htm"),
    dict(e="akamai", t="second", conf="reported", stat="No 2026 figure was verified in this research.",
     why="Long-standing delivery and security customer base.", cond="Unchecked.",
     src="https://www.alpha-sense.com/earnings/net/"),
   ]),
 ])

EDGES = [
 dict(a="spacex", b="starlink", type="ownership", text="Starlink is SpaceX's connectivity business and its main source of profit.", src="https://broadbandbreakfast.com/starlink-reaches-13-6-million-subscribers-globally-as-spacex-revenue-jumps-161/", date="2026-Q3", conf="reported"),
 dict(a="huawei", b="ericsson", type="rivalry", text="Number one and two in RAN, with nearly two-thirds of the market between them.", src="https://www.delloro.com/news/ran-market-growth-continues-in-2q-2026/", date="2026", conf="primary"),
 dict(a="nokia", b="huawei", type="rivalry", text="Nokia lost ground to Huawei outside China between 2019 and 2025.", src="https://www.delloro.com/news/ran-market-growth-continues-in-2q-2026/", date="2025", conf="primary"),
 dict(a="att", b="verizon", type="rivalry", text="AT&T added 379,000 postpaid phones in Q3 2026. Verizon is guided to 750,000 to 1 million for the year.", src="https://about.att.com/story/2026/3q-earnings.html", date="2026-Q3", conf="reported"),
 dict(a="starlink", b="att", type="rivalry", text="Satellite broadband competes with fixed wireless and fiber for rural customers.", src="https://about.att.com/story/2026/3q-earnings.html", date="2026", conf="inferred"),
 dict(a="cloudflare", b="amazon", type="rivalry", text="Delivery and security at the network edge competes with cloud providers' own services.", src="https://www.sec.gov/Archives/edgar/data/0001477333/000147733326000053/q226exhibit991.htm", date="2026", conf="inferred"),
 dict(a="cloudflare", b="akamai", type="rivalry", text="Content delivery and security.", src="https://www.sec.gov/Archives/edgar/data/0001477333/000147733326000053/q226exhibit991.htm", date="2026", conf="inferred"),
 dict(a="spacex", b="xai", type="ownership", text="SpaceX's AI division was its largest business by revenue in Q3 2026 at $7.56bn (reported).", src="https://www.kucoin.com/blog/spacex-q3-2026-earnings-revenue-profit-ai-starlink", date="2026-Q3", conf="reported"),
]
