"""Tech Atlas, Phase 2, sector 13: Robotics."""

ENT = {
 "china_robots": ("Chinese industrial robot makers", "Supply about 55% of the robots installed in China."),
 "china_humanoids": ("Unitree, UBTech and AgiBot", "Chinese humanoid makers that shipped most of the world's units in H1 2026."),
 "figure": ("Figure AI", "US humanoid robot startup."),
 "agility": ("Agility Robotics", "Maker of the Digit warehouse robot."),
 "apptronik": ("Apptronik", "US humanoid startup."),
 "onex": ("1X", "Maker of the NEO home humanoid."),
 "skild": ("Skild AI", "Robot foundation model startup, valued above $14bn."),
 "physical_intel": ("Physical Intelligence", "Startup building general-purpose robot models."),
}

SECTOR = dict(
 id="robotics", name="Robotics", band="industries",
 blurb="The factory robots that already work, and the humanoids and robot models still arriving.",
 positions=[

  dict(id="industrial", name="Industrial and warehouse robots",
   metric=("The IFR counted 603,000 industrial robots installed worldwide in 2025, up 11%, and a global stock of 5 million. China installed 354,000, or 59%. The US passed Japan to become the second-largest market with about 38,500 units, up 12%. Amazon runs more than 1 million warehouse robots, a figure last announced in July 2025."),
   metric_src="https://thenextweb.com/news/industrial-robots-world-robotics-2026-china-59-eu-falls",
   players=[
    dict(e="china_robots", t="starter", conf="reported",
     stat="Domestic suppliers held about 55% of China's market in 2025, down from 57% (one source). China installed 354,000 robots.",
     why="Their home market is more than half of the world, and buyers there prefer local suppliers.",
     cond="Sources differ on growth rates for China's installs, from 15% to 20%.",
     src="https://thenextweb.com/news/industrial-robots-world-robotics-2026-china-59-eu-falls"),
    dict(e="amazon", t="starter", conf="reported",
     stat="More than 1 million warehouse robots, announced on 1 July 2025 and not updated since. It also employs more than 1.5 million people.",
     why="Runs the largest fleet of robots in one company.", cond="The count is a floor and a year old.",
     src="https://wisevoter.com/world/us/2026/10/20/amazon-reaches-millionth-warehouse-robot"),
   ]),

  dict(id="humanoids", name="Humanoid robots",
   metric=("Chinese makers accounted for over 97% of about 19,100 humanoids shipped globally in H1 2026 (one report, roughly triple the prior year's first half). Tesla's Optimus output is reported far below its target. Counts of units deployed are secondary and conflict."),
   metric_src="https://startupfortune.com/chinas-humanoid-robot-shipments-hit-97-of-the-world-as-tesla-stalls/",
   players=[
    dict(e="china_humanoids", t="starter", conf="reported",
     stat="Unitree, UBTech and AgiBot shipped most of about 19,100 humanoids in H1 2026. One report says Unitree is pursuing a $6.2bn IPO, which was not confirmed.",
     why="Scale manufacturing and low prices at home.", cond="Single-source shipment count.",
     src="https://startupfortune.com/chinas-humanoid-robot-shipments-hit-97-of-the-world-as-tesla-stalls/"),
    dict(e="tesla", t="second", conf="reported",
     stat="Reports conflict between over 1,000 Optimus Gen 3 units in its own factories and a few hundred against a 5,000 target. Management's target is 20,000 a week within about a year, with deliveries not before late 2027 by one account.",
     why="Could use its own factories and vehicle supply chain.", cond="Timelines keep moving.",
     src="https://www.kucoin.com/news/flash/tesla-q3-earnings-fsd-drives-demand-robotaxi-and-optimus-timelines-delayed"),
    dict(e="figure", t="rookie", conf="reported",
     stat="Reported to have deployed 40 Figure 03 units at BMW's Spartanburg plant in January 2026, billed at about $25 per robot-hour. A recent $1bn raise is mentioned without a confirmed valuation.",
     why="Has the strongest commercial deployment evidence among US startups.", cond="Single-source figures.",
     src="https://www.aimagicx.com/blog/humanoid-robots-workplace-tesla-optimus-atlas-2026"),
    dict(e="agility", t="rookie", conf="reported",
     stat="About 250 Digit units in logistics (market tracker).", why="Built for a narrow warehouse task.", cond="No funding figure was verified.",
     src="https://presenc.ai/research/humanoid-robot-market-tracker-2026"),
    dict(e="apptronik", t="rookie", conf="reported",
     stat="About 80 Apollo units deployed (market tracker).", why="Partnered with industrial customers.", cond="No funding figure was verified.",
     src="https://presenc.ai/research/humanoid-robot-market-tracker-2026"),
    dict(e="onex", t="rookie", conf="reported",
     stat="Over 10,000 pre-orders for the NEO home robot, with deliveries expected by the end of 2026 (one source).",
     why="Aims at the home and not the factory.", cond="Single source, and no funding figure was verified.",
     src="https://lumichats.com/blog/humanoid-robots-2026-tesla-optimus-figure-ai-unitree-complete-guide"),
   ]),

  dict(id="models", name="Robot foundation models",
   metric=("No starter was verified in this row. Skild AI raised close to $1.4bn led by SoftBank, with Nvidia's venture arm participating, at a valuation above $14bn in January 2026. Physical Intelligence was last reported at $5.6bn in November 2025."),
   metric_src="https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B",
   players=[
    dict(e="skild", t="rookie", badge="changes the premise",
     stat="Close to $1.4bn raised in January 2026, led by SoftBank with NVentures, at a valuation above $14bn, more than triple its $4.5bn mark seven months earlier.",
     why="Builds one model that controls many kinds of robots.", cond="A later round and an acquisition of a Zebra division are reported in single sources.",
     src="https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B"),
    dict(e="physical_intel", t="rookie", conf="reported",
     stat="Valued at $5.6bn in new funding reported in November 2025. A $1bn round that would value it above $11bn was reported in talks and not confirmed.",
     why="Works on a general-purpose model that robots from different makers can use.", cond="Round status unconfirmed.",
     src="https://en.wikipedia.org/wiki/Physical_Intelligence_Inc."),
   ]),
 ])

EDGES = [
 dict(a="softbank", b="skild", type="investment", text="Led the roughly $1.4bn round in January 2026.", src="https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B", date="2026-01", conf="primary"),
 dict(a="nvidia", b="skild", type="investment", text="Nvidia's venture arm, NVentures, took part in the round.", src="https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B", date="2026-01", conf="primary"),
 dict(a="tesla", b="china_humanoids", type="rivalry", text="Chinese makers shipped over 97% of humanoids in H1 2026 while Optimus output trails its target.", src="https://startupfortune.com/chinas-humanoid-robot-shipments-hit-97-of-the-world-as-tesla-stalls/", date="2026-H1", conf="reported"),
 dict(a="figure", b="tesla", type="rivalry", text="US humanoid makers competing for factory deployments.", src="https://newmarketpitch.com/blogs/news/humanoid-robotics-figure-vs-tesla", date="2026", conf="inferred"),
 dict(a="skild", b="physical_intel", type="rivalry", text="Both build general-purpose robot models.", src="https://sacra.com/c/skild-ai/", date="2026", conf="inferred"),
 dict(a="skild", b="figure", type="dependency", text="Robot makers need models to run on their hardware, which Skild and Physical Intelligence sell.", src="https://sacra.com/c/skild-ai/", date="2026", conf="inferred"),
 dict(a="china_robots", b="amazon", type="rivalry", text="China installs 59% of the world's industrial robots, while Amazon runs the largest single warehouse fleet.", src="https://thenextweb.com/news/industrial-robots-world-robotics-2026-china-59-eu-falls", date="2026", conf="inferred"),
]
