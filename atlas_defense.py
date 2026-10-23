"""Tech Atlas, Phase 2, sector 15: Defense and space."""

ENT = {
 "blue_origin": ("Blue Origin", "Builds the New Glenn rocket."),
 "ula": ("United Launch Alliance", "Maker of the Vulcan rocket."),
 "rocket_lab": ("Rocket Lab", "Small launch company building the Neutron rocket."),
 "ast": ("AST SpaceMobile", "Satellite-to-phone broadband company."),
 "anduril": ("Anduril", "Defense technology company building autonomous systems."),
 "thrive": ("Thrive Capital", "Venture investor that led Anduril's May 2026 round."),
 "a16z": ("Andreessen Horowitz", "Venture investor that led Anduril's May 2026 round."),
 "rtx": ("RTX", "Aerospace and defense prime contractor."),
 "lockheed": ("Lockheed Martin", "The largest US defense prime."),
}

SECTOR = dict(
 id="defense", name="Defense and space", band="industries",
 blurb="The rockets that reach orbit, the startups taking defense work and the primes with the backlogs.",
 positions=[

  dict(id="launch", name="Launch",
   metric=("Since early March 2026 the only US heavy rocket able to fly several national security missions has been SpaceX's Falcon 9. ULA's Vulcan last flew on 12 February and has been paused since. Blue Origin's New Glenn exploded during a static-fire test on 28 May and had not returned to flight as of the latest report. No 2026 SpaceX launch count was found."),
   metric_src="https://thespaceatlas.org/read/new-glenn-vulcan/",
   players=[
    dict(e="spacex", t="starter", conf="reported",
     stat="Falcon 9 is the only vehicle flying the missions Vulcan paused. Starship's 2026 flight history conflicts across sources.",
     why="The only operator with a rocket that flies often and reuses its boosters.", cond="Starship has to reach orbit reliably and carry payloads.",
     src="https://thespaceatlas.org/read/new-glenn-vulcan/"),
    dict(e="blue_origin", t="second", conf="reported",
     stat="New Glenn's third flight on 19 April left AST SpaceMobile's BlueBird 7 in the wrong orbit. It exploded in a static-fire test on 28 May.",
     why="Backed by deep funding and an Amazon Leo contract.", cond="Return to flight.",
     src="https://en.wikipedia.org/wiki/List_of_New_Glenn_launches"),
    dict(e="ula", t="second", conf="reported",
     stat="Vulcan's last flight, USSF-87 on 12 February, reached its orbits despite a solid rocket motor anomaly. No launches since.",
     why="Holds long-standing national security contracts.", cond="Return to flight.",
     src="https://thespaceatlas.org/read/new-glenn-vulcan/"),
    dict(e="rocket_lab", t="rookie", conf="reported",
     stat="The Neutron rocket's debut reportedly slipped into 2027 after a dome technical issue (one source). No Q2 2026 results were found.",
     why="A mid-size rocket would fill the gap between small launchers and heavy ones.", cond="Date is single-sourced.",
     src="https://newspaceeconomy.ca/2026/06/06/how-does-starship-compare-to-falcon-9-falcon-heavy-new-glenn-vulcan-nova-and-neutron/"),
   ]),

  dict(id="deftech", name="Defense technology",
   metric=("Anduril raised $5bn in a Series H at a $61bn valuation in May 2026, more than double its valuation a year earlier, and reported $2.2bn of 2025 revenue. A round near $100bn was reported in talks in July, unconfirmed."),
   metric_src="https://techcrunch.com/2026/05/13/anduril-raises-5b-doubles-valuation-to-61b/",
   players=[
    dict(e="anduril", t="rookie", badge="late stage",
     stat="$5bn Series H at $61bn, May 2026, led by Thrive Capital and Andreessen Horowitz. 2025 revenue $2.2bn. New capital is expected to support its Arsenal-1 factory in Ohio. No IPO filing.",
     why="Builds weapons and autonomous systems as products and sells them to the Pentagon.", cond="Reported talks at about $100bn are unconfirmed.",
     src="https://techcrunch.com/2026/05/13/anduril-raises-5b-doubles-valuation-to-61b/"),
    dict(e="palantir", t="second", conf="reported",
     stat="Q2 2026 revenue $1.935bn, up 92.8%. Its defense mix was not researched here.", why="Sells deployed software to governments.", cond="Concentration in government buyers.",
     src="https://finance.yahoo.com/markets/stocks/articles/palantir-vs-snowflake-growth-stock-153045683.html"),
   ]),

  dict(id="primes", name="Defense primes",
   metric=("RTX's total backlog was $289bn at the end of Q2 2026, up 22%, split between $170bn commercial and $119bn defense. Lockheed's backlog was $230.4bn at 28 June, up from $193.6bn at the end of 2025. The House advanced a $1.15tn FY2027 defense bill (reported), and the 2027 defense authorization had not been enacted."),
   metric_src="https://www.nasdaq.com/articles/rtx-and-lockheed-earnings-can-strong-guidance-reset-defense-trade",
   players=[
    dict(e="rtx", t="starter", stat="Q2 2026 revenue $24.71bn, up 14%. Sales guidance raised to $95bn to $96bn.",
     why="Sells engines and defense systems to commercial and military buyers.", cond="Defense budgets and authorization timing.",
     src="https://www.nasdaq.com/articles/rtx-and-lockheed-earnings-can-strong-guidance-reset-defense-trade"),
    dict(e="lockheed", t="starter", stat="Adjusted EPS of $7.94 in Q2 2026. 2026 revenue guide $79.75bn to $81.75bn.",
     why="Prime on the largest fighter, missile and space programs.", cond="If the authorization act is not signed by 1 October, multiyear procurement contracts cannot go out.",
     src="https://www.nasdaq.com/articles/lockheed-q2-earnings-beat-estimates-sales-increase-year-over-year"),
   ]),
 ])

EDGES = [
 dict(a="ula", b="spacex", type="dependency", text="Since early March 2026 the only vehicle able to fly the missions Vulcan paused has been Falcon 9.", src="https://thespaceatlas.org/read/new-glenn-vulcan/", date="2026-03", conf="reported"),
 dict(a="ast", b="blue_origin", type="supply", text="New Glenn's April flight carried AST SpaceMobile's BlueBird 7 and left it in the wrong orbit.", src="https://en.wikipedia.org/wiki/List_of_New_Glenn_launches", date="2026-04", conf="reported"),
 dict(a="amazon", b="blue_origin", type="supply", text="Amazon's first Leo satellite mission on New Glenn was planned for June and did not fly after the vehicle exploded.", src="https://thespaceatlas.org/read/new-glenn-vulcan/", date="2026-06", conf="reported"),
 dict(a="spacex", b="amazon", type="rivalry", text="Starlink has 13.6 million subscribers. No Amazon Leo deployment totals were found.", src="https://broadbandbreakfast.com/starlink-reaches-13-6-million-subscribers-globally-as-spacex-revenue-jumps-161/", date="2026", conf="inferred"),
 dict(a="thrive", b="anduril", type="investment", text="Co-led the $5bn Series H with Andreessen Horowitz.", src="https://techcrunch.com/2026/05/13/anduril-raises-5b-doubles-valuation-to-61b/", date="2026-05", conf="primary"),
 dict(a="a16z", b="anduril", type="investment", text="Co-led the $5bn Series H with Thrive Capital.", src="https://techcrunch.com/2026/05/13/anduril-raises-5b-doubles-valuation-to-61b/", date="2026-05", conf="primary"),
 dict(a="anduril", b="lockheed", type="rivalry", text="A venture-backed contractor taking work that primes have held.", src="https://www.cnbc.com/2026/05/13/anduril-valuation-defense-tech-funding-boom.html", date="2026", conf="inferred"),
 dict(a="rtx", b="lockheed", type="rivalry", text="Backlogs of $289bn and $230.4bn.", src="https://www.nasdaq.com/articles/rtx-and-lockheed-earnings-can-strong-guidance-reset-defense-trade", date="2026-Q2", conf="reported"),
 dict(a="spacex", b="rocket_lab", type="rivalry", text="Neutron would compete with Falcon 9 for mid-size payloads, and its debut reportedly slipped to 2027.", src="https://newspaceeconomy.ca/2026/06/06/how-does-starship-compare-to-falcon-9-falcon-heavy-new-glenn-vulcan-nova-and-neutron/", date="2026", conf="reported"),
]
