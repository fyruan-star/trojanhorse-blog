"""Tech Atlas, Phase 2, sector 10: Foundation. The inputs under the chip."""

ENT = {
 "ase": ("ASE Technology", "Largest outsourced chip assembly and test company."),
 "amkor": ("Amkor", "US-based outsourced chip packaging company."),
 "abf_trio": ("Unimicron, Ibiden and Shinko", "Make the substrates that advanced AI chips sit on."),
 "shin_sumco": ("Shin-Etsu and SUMCO", "The two largest suppliers of 300mm silicon wafers."),
 "china_ree": ("China's rare earth sector", "Processes most rare earths and decides who gets licences to export them."),
 "mp": ("MP Materials", "The US rare earth miner and magnet maker."),
}

SECTOR = dict(
 id="foundation", name="Foundation", band="foundation",
 blurb="The packaging, wafers and magnets that sit under every chip and motor.",
 positions=[

  dict(id="packaging", name="Advanced packaging and substrates",
   metric=("TSMC's CoWoS capacity is estimated to reach 115,000 to 140,000 wafers a month by the end of 2026, and TSMC does not disclose it. Nvidia is estimated at about 60% of capacity and Nvidia, Broadcom and AMD together at 85% or more. TrendForce reports the supply gap narrowing from 20% to 10% by the end of 2026. Three companies make about 75% of ABF substrates."),
   metric_src="https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/",
   players=[
    dict(e="tsmc", t="starter", conf="reported",
     stat="Ramping CoWoS packaging from about 75,000 to 80,000 wafers a month toward 120,000 to 130,000 by the end of 2026 (estimates).",
     why="Packages the chips it makes, so the customer buys the whole stack from one place.",
     cond="Capacity expansion. TrendForce expects the squeeze to ease from 2027.",
     src="https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/"),
    dict(e="abf_trio", t="starter", conf="reported",
     stat="Unimicron, Ibiden and Shinko control about 75% of the ABF substrate market. New lines take 18 to 24 months.",
     why="Few companies can make the substrates, and adding capacity is slow.",
     cond="No shortage-specific capacity data was found.",
     src="https://eu.36kr.com/en/p/3892020701149697"),
    dict(e="ase", t="second", conf="reported",
     stat="Q1 2026 revenue NT$173.7bn, up 17%. Its assembly, test and materials unit grew nearly 30%. CoWoS-type output is projected at 20,000 to 25,000 wafers a month by year end (brokerage estimate).",
     why="Takes the overflow when TSMC's own lines are full.",
     cond="Whether it wins the flagship customers' volume.",
     src="https://insights.munich-startup.de/news/feed/ase-technology-beats-amkor-with-30-revenue-surge-as-ai-drives-chip-packaging-demand"),
    dict(e="amkor", t="second", conf="reported",
     stat="Record Q1 2026 revenue of $1.68bn, up 27%. 2026 capital spending $2.5bn to $3bn. A 10-year CoWoS agreement with TSMC (June 2026) and a $1.5bn advanced-packaging deal with Nvidia (July) are reported by one commentary source.",
     why="Gives US customers a US packaging option, with an Arizona campus.",
     cond="The two agreements are single-sourced.",
     src="https://www.yolegroup.com/product/quarterly-monitor/advanced-packaging-market-monitor/"),
   ]),

  dict(id="wafers", name="Silicon wafers",
   metric=("Shin-Etsu and SUMCO together hold over 50% of 300mm wafer supply (Future Market Insights, a secondary estimate). No 2026 SEMI shipment data and no GlobalWafers share was found."),
   metric_src="https://www.futuremarketinsights.com/reports/semiconductor-wafers-market",
   players=[
    dict(e="shin_sumco", t="starter", conf="reported",
     stat="Over 50% of global 300mm supply between them. SUMCO plans to end 200mm production at Miyazaki by late 2026 to focus on 300mm AI-grade wafers.",
     why="Wafer making is a slow, specialist craft that the chip makers buy from two suppliers.",
     cond="Share is a secondary estimate, and the data here is thin.",
     src="https://www.futuremarketinsights.com/reports/semiconductor-wafers-market"),
   ]),

  dict(id="minerals", name="Rare earths and magnets",
   metric=("China's April 2025 export licensing for seven medium and heavy rare earths remains in force. A second wave of controls is suspended until 10 November 2026. China's rare earth and magnet exports in January and February 2026 were under one third of the same months in 2024 and 2025. A US defense procurement ban on Chinese magnets takes full effect on 1 January 2027."),
   metric_src="https://www.techtimes.com/articles/328392/20261002/rare-earth-magnets-chinas-november-10-deadline-us-gap-money-cant-close.htm",
   players=[
    dict(e="china_ree", t="starter", conf="reported",
     stat="Controls licensing for exports of rare earths and the magnets that contain them. Beijing had not ruled out the most expansive version of its controls as of May 2026.",
     why="Processes most of the world's rare earths, so a licence decides who builds motors.",
     cond="The suspension of the second wave expires on 10 November 2026.",
     src="https://epthinktank.eu/2025/11/24/chinas-rare-earth-export-restrictions/"),
    dict(e="mp", t="second",
     stat="Q2 2026 NdPr production 840 tonnes, up 41%. Revenue $108.5m, up 89%. Magnetics revenue $16.5m, with capital spending of $230.3m, over 60% on magnets. Signed an offtake for separated gadolinium with a US aerospace and defense customer.",
     why="The only scaled US producer, with price protection income that supports it.",
     cond="US magnet capacity is not expected to be meaningful until 2028 (one source).",
     src="https://investors.mpmaterials.com/investor-news/news-details/2026/MP-Materials-Reports-Second-Quarter-2026-Results/default.aspx"),
   ]),
 ])

EDGES = [
 dict(a="nvidia", b="tsmc", type="dependency", text="Nvidia is estimated to hold about 60% of TSMC's CoWoS packaging capacity.", src="https://eu.36kr.com/en/p/3892020701149697", date="2026", conf="reported"),
 dict(a="amkor", b="tsmc", type="supply", text="Reported 10-year CoWoS packaging agreement signed in June 2026.", src="https://www.yolegroup.com/product/quarterly-monitor/advanced-packaging-market-monitor/", date="2026-06", conf="reported"),
 dict(a="amkor", b="nvidia", type="supply", text="Reported $1.5bn advanced-packaging deal in July 2026.", src="https://www.yolegroup.com/product/quarterly-monitor/advanced-packaging-market-monitor/", date="2026-07", conf="reported"),
 dict(a="ase", b="tsmc", type="supply", text="Takes packaging spillover, about 40,000 wafers a month by one estimate, when TSMC's lines are full.", src="https://eu.36kr.com/en/p/3892020701149697", date="2026", conf="reported"),
 dict(a="broadcom", b="tsmc", type="dependency", text="Nvidia, Broadcom and AMD together are estimated at 85% or more of CoWoS capacity.", src="https://eu.36kr.com/en/p/3892020701149697", date="2026", conf="reported"),
 dict(a="china_ree", b="mp", type="rivalry", text="MP is building a US supply chain for materials China currently licenses.", src="https://investors.mpmaterials.com/investor-news/news-details/2026/MP-Materials-Reports-Second-Quarter-2026-Results/default.aspx", date="2026-08", conf="inferred"),
 dict(a="china_ree", b="tesla", type="dependency", text="Rare earth magnets go into electric motors, and China licenses their export.", src="https://epthinktank.eu/2025/11/24/chinas-rare-earth-export-restrictions/", date="2025", conf="inferred"),
]
