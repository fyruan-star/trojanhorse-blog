"""Ten years of technology transactions, 2016 to 2026.

The page argues one thesis and uses each entry as evidence for or against it.
Entries state what the company sells, who pays for it, what the buyer paid and
in what form, and what the case shows. Quotations are kept to the ten longer
deal notes, where each is linked to its source. Values are announced values
unless an entry says final. No em dashes, no semicolons.

`width` is the spine's thickness for that year. It traces the broad shape of
the transaction cycle and is not plotted from a dataset.
"""

INTRO = (
 "Announcements of technology acquisitions usually explain the price as a bet "
 "on growth. IBM described its purchase of Red Hat as helping businesses begin "
 "<a href=\"the-layer-above.html\">“the next chapter of their digital reinventions.”</a> On that reading a deal's "
 "value follows how fast the target is expected to grow, and the buyer that "
 "paid well was the one that saw the future first. The entries below, which "
 "cover 2016 to 2026, support a different reading. The businesses that held "
 "their value sold something customers found costly to leave. The deals that "
 "failed were stopped because of what an asset's independence or location "
 "meant to competitors and governments. And the money that moved after 2023 "
 "went toward physical capacity, such as power, buildings and storage, more "
 "than toward software.")

INTRO_2 = (
 "The difference matters to anyone reading a deal announcement, because the "
 "growth forecast and the strategic rationale are the two parts of it least "
 "likely to predict the result. Four checks apply to every entry: what the "
 "company sells, who pays for it and from which budget, what a customer would "
 "have to do to replace it, and what the buyer paid and in what form.")

CLOSE_HEAD = "What the entries support"
CLOSE = [
 "The first finding is that the businesses which held their value tend to "
 "sell something a customer would find expensive to replace, where the "
 "expense is measured in time and risk and not in price. Red Hat, VMware and "
 "Arm are each an example. A bank that has certified a thousand applications "
 "against one vendor's software is not deciding whether a competitor is "
 "better. It is deciding whether to spend three years finding out. This "
 "finding explains why buyers could pay large premiums for businesses that "
 "were not growing fastest, and why Broadcom's strategy of raising prices "
 "after acquisition has been profitable.",

 "The second is that governments became a party to large semiconductor "
 "transactions in a way they had not been before 2018. Two of the three "
 "abandoned deals on this page ended in a regulator's office and not in a "
 "boardroom, and in both the objection was about who would hold a position in "
 "future and not about prices today. A deal whose value rests on independence, "
 "as Arm's did, fails if the buyer is a competitor of the asset's customers. A "
 "deal whose value rests on a standards position, as Qualcomm's did, can "
 "fail on a forecast of national capability.",

 "The third is that a growing share of spending went toward physical "
 "capacity. The Blackstone investment in DDN, the data center construction "
 "of 2024 and after, and Seagate's return to the debt markets all show it. "
 "Software still mattered, and two of the largest transactions of the final "
 "two years were software companies. The shift is in where the scarcest input "
 "sat, which moved from ideas and processors toward electricity and the time "
 "needed to obtain it.",

 "The strongest objection is that ten years and a few dozen deals are too "
 "few to establish a pattern. Cheap money explains much of 2020 and 2021 "
 "independently of customer lock-in, and Intel's purchase of Mobileye, "
 "priced at more than forty times revenue, is a case where the price did "
 "rest on growth. The entries are a selection, and I chose deals that "
 "illustrate each mechanism, so they cannot show how common each one is.",

 "Three developments would test the thesis. Documented customer migration "
 "away from VMware, or a rise in the share of new chip designs that choose "
 "RISC-V over Arm, would show that switching costs were weaker than they "
 "looked. Evidence that Red Hat keeps its neutrality under IBM, or that "
 "Cisco retains Splunk's customers, would show that buyers can hold what "
 "they bought. Until those arrive, the practical implication is that a "
 "reader should treat the announced price and growth rationale as the "
 "starting point and ask the four checks above before concluding that a "
 "buyer saw something the market missed.",
]

# kind: seal (completed or pending deal), column (abandoned), stone (not a deal)
# each node: (kind, tag, title, [paragraphs], note_or_empty)
YEARS = [

 ("2016", 20, [
  ("stone", "", "Smartphone growth slows", [
   "Smartphone shipments grew about three percent in 2016, against roughly "
   "ten percent in 2015, and the first annual decline came in 2017. A company "
   "whose main market doubles every few years can fund its growth from that "
   "market. A slower market leaves large technology companies choosing "
   "between buying their way into adjacent ones and accepting lower growth. "
   "The first two acquisitions below were made in that setting.",
  ], ""),

  ("seal", "Acquisition &middot; $32bn &middot; announced July 2016", "SoftBank / Arm", [
   "Arm designs the instruction set that processors are built around and "
   "licenses it. It manufactures nothing. Apple, Qualcomm, Samsung and others "
   "take the design, build a chip around it and pay Arm a royalty on each one "
   "sold, a few cents a chip, on more than fifteen billion chips a year.",
   "SoftBank paid about $32 billion in cash, a premium of roughly 43 "
   "percent, for a company whose royalties came mostly from a market that "
   "was flattening. Because Arm owns no factories it carries none of the "
   "capital spending of the rest of the industry, and because it makes no "
   "chips it does not compete with its licensees.",
  ],
   "The price was a bet on the licensing structure more than on mobile. Arm's "
   "designs were later used in server processors from Amazon and Nvidia, and "
   "SoftBank listed Arm again in 2023 at about $54.5 billion."),
 ]),

 ("2017", 17, [
  ("seal", "Acquisition &middot; $15.3bn &middot; announced March 2017", "Intel / Mobileye", [
   "Mobileye made the camera systems and software that let a car recognize "
   "a lane, a pedestrian or a vehicle ahead. It sold to carmakers, who "
   "designed it into models years before they reached showrooms, which made "
   "its revenue predictable once a design win was secured.",
   "Intel paid about $15.3 billion against Mobileye revenue of around $358 "
   "million the previous year, more than forty times. A buyer paying that "
   "multiple is assuming either that revenue grows by a large multiple or that "
   "the asset has value beyond its sales. Intel said publicly that it saw the "
   "car as a future computing platform, and it had missed mobile almost "
   "entirely.",
  ],
   "This is the clearest case on the page of a price resting on growth that "
   "had not yet occurred, and it is the objection to the thesis that the "
   "closing section addresses."),

  ("seal", "Carve-out &middot; ~$18bn &middot; signed September 2017", "Toshiba Memory", [
   "Toshiba sold its memory chip business to a consortium led by Bain Capital "
   "after losses in its nuclear division left it short of cash. The business "
   "made NAND flash, the storage in phones, laptops and data centers.",
   "The sale took close to a year to complete because several governments "
   "took an interest in who would own it.",
  ],
   "Government interest in who owns a chip business, which shows up here "
   "before it does in the larger cases, became routine over the decade."),
 ]),

 ("2018", 26, [
  ("column", "Prohibited &middot; ~$117bn &middot; March 2018", "Broadcom / Qualcomm", [
   "Broadcom pursued Qualcomm without its board's agreement and raised its "
   "offer to around $117 billion. Qualcomm holds a large body of patents "
   "covering how mobile devices communicate with networks and was heavily "
   "involved in writing the 5G standards.",
   "A presidential order prohibited the transaction in March 2018 after a "
   "review by the Committee on Foreign Investment in the United States. The "
   "committee's concern was that Broadcom's practice of cutting research "
   "spending at companies it buys would weaken American participation in "
   "those standards.",
  ],
   "Approval risk shifted from a market share question a bidder could model "
   "to a forecast of national capability it could not."),

  ("column", "Abandoned &middot; $44bn &middot; July 2018", "Qualcomm / NXP", [
   "Qualcomm agreed to buy NXP Semiconductors in 2016 and spent close to two "
   "years collecting approvals. All arrived except Chinese approval, and in "
   "July 2018 Qualcomm let the agreement lapse and paid NXP a $2 billion "
   "termination fee.",
   "A fee of that size is agreed in advance because approval is uncertain. "
   "It compensates the seller for the time spent waiting and for being "
   "publicly in play.",
  ],
   "The second abandoned deal of the year also ended in a regulator's office. "
   "Both failures were about positions in the supply chain."),

  ("seal", "Acquisition &middot; $34bn &middot; announced October 2018", "IBM / Red Hat", [
   "Red Hat's main product is a version of Linux, which is free software. "
   "What it sold was a version somebody would stand behind: tested, patched, "
   "supported and certified to work with the other systems a bank or a "
   "hospital runs.",
   "That is a subscription business, and its strength comes from what a "
   "customer would have to do to leave. An institution that has certified "
   "several hundred applications against one distribution would have to test "
   "all of them again. IBM paid $190 a share in cash, about $34 billion, a "
   "premium above 60 percent, for software that enterprises use across more "
   "than one cloud provider.",
  ],
   "The case for the price is the customer's cost of leaving. The risk is "
   "whether software valued for working equally well with every cloud can be "
   "owned by a company that sells one."),
 ]),

 ("2019", 19, [
  ("seal", "Acquisition &middot; $6.9bn &middot; announced March 2019", "Nvidia / Mellanox", [
   "Mellanox made high speed networking equipment, mainly a technology called "
   "InfiniBand, designed for connecting computers inside a single facility. "
   "Its customers were mostly scientific computing centers running weather "
   "models, physics simulations and genomics work.",
   "A large job split across many machines requires them to stop "
   "periodically and exchange results. If the connection is slow the "
   "processors spend their time waiting, so networking sets how much of a "
   "facility's equipment is in use. Nvidia paid $6.9 billion in cash, its "
   "largest acquisition to that point.",
  ],
   "The purchase is explained by what Nvidia's customers were already doing "
   "in 2019. The AI training demand that followed made the capability far "
   "more valuable, and the announcement does not claim to have forecast it."),

  ("seal", "Acquisition &middot; $15.7bn &middot; announced June 2019", "Salesforce / Tableau", [
   "Tableau made software for turning company data into charts that "
   "non-specialists could build themselves. Salesforce paid about $15.7 "
   "billion in its own shares.",
   "Analysis software tends to be sticky because an organization that has "
   "built hundreds of reports finance and sales rely on weekly would have to "
   "rebuild all of them and retrain its staff to move to a competitor. The "
   "switching cost sits in the work already done.",
  ],
   "Another instance of the cost-of-leaving test, here applied to software "
   "that is used by employees and not run by engineers."),
 ]),

 ("2020", 24, [
  ("stone", "", "Borrowing becomes very cheap", [
   "Central banks cut interest rates to near zero in response to the "
   "pandemic and held them there. Cheap borrowing raises what buyers can "
   "afford and raises the price of assets whose value depends on earnings "
   "far in the future. Most of the transactions in the next two years were "
   "negotiated under those conditions.",
  ],
   "Cheap money is a competing explanation for the high prices of 2020 and "
   "2021, and the closing section treats it as an objection."),

  ("seal", "Acquisition &middot; $35bn at announcement &middot; October 2020", "AMD / Xilinx", [
   "Xilinx made field programmable gate arrays, chips that can be "
   "reconfigured after manufacture. They are slower than a chip built for "
   "one purpose and more flexible, which suits applications where the task "
   "changes, such as telecommunications equipment.",
   "AMD paid entirely in its own shares at a fixed ratio of 1.7234 AMD shares "
   "for each Xilinx share, giving Xilinx holders about 26 percent of the "
   "combined company. Because the ratio was fixed, the value of the "
   "consideration moved. The deal was described as about $35 billion at "
   "announcement and closed in February 2022 at a figure widely reported near "
   "$49 billion.",
  ],
   "The announced value of an all-stock deal is the buyer's share price on one "
   "day multiplied by a ratio. The ratio and the ownership split are the "
   "terms, and comparisons that use the announced dollar value mislead."),
 ]),

 ("2021", 40, [
  ("stone", "", "The busiest year on record", [
   "Global deal volumes reached their highest level on record in 2021, "
   "helped by cheap debt, high equity prices and a large number of blank "
   "check vehicles raised to buy companies. Several transactions agreed "
   "that year were renegotiated or abandoned once conditions changed.",
  ], ""),

  ("seal", "Acquisition &middot; $19.7bn &middot; announced April 2021", "Microsoft / Nuance", [
   "Nuance sold speech recognition software, with its strongest position in "
   "hospitals, where it turns a clinician's dictation into a patient record. "
   "Microsoft paid $56 a share in cash, about $19.7 billion including debt.",
   "The attraction was less the software than the access. Health systems are "
   "slow and cautious about who they allow near patient data, for sound "
   "regulatory reasons, and a supplier that is already installed and "
   "approved holds a position that is difficult to buy any other way.",
  ],
   "The asset was an approved position inside a regulated customer, which is "
   "a switching cost created by the customer's own rules."),
 ]),

 ("2022", 20, [
  ("stone", "", "Rates rise and the market for new listings closes", [
   "Interest rates rose quickly through 2022. The Nasdaq composite fell by "
   "roughly a third over the year, debt became more expensive and the "
   "market for initial public offerings effectively shut. Companies that had "
   "expected to list stayed private, which is where a growing share of large "
   "technology businesses has remained.",
  ], ""),

  ("column", "Abandoned &middot; $40bn &middot; February 2022", "Nvidia / Arm", [
   "Nvidia agreed in September 2020 to buy Arm from SoftBank for up to $40 "
   "billion in cash and stock. Seventeen months later the parties abandoned "
   "it, and SoftBank kept a $1.25 billion payment Nvidia had made in "
   "advance.",
   "Arm's licensees include most of Nvidia's competitors, and they license "
   "from Arm partly because Arm does not build chips. Several objected to "
   "regulators in the United States, the United Kingdom and the European "
   "Union, and the US Federal Trade Commission sued to block the deal. "
   "SoftBank listed Arm on Nasdaq in September 2023 instead, at a valuation "
   "above what Nvidia had offered.",
  ],
   "Where part of an asset's value comes from its independence, a sale to an "
   "interested party reduces what is being bought."),

  ("seal", "Acquisition &middot; $61bn &middot; announced May 2022", "Broadcom / VMware", [
   "VMware's core product lets one physical server run as several separate "
   "machines. It sits underneath a large amount of corporate computing and "
   "is difficult to remove without a long migration project.",
   "Broadcom has bought established infrastructure software repeatedly, "
   "including CA Technologies and Symantec's enterprise business. It reduces "
   "research spending and smaller product lines, concentrates on the largest "
   "customers and raises prices, so its return does not depend on the "
   "acquired business growing. The VMware transaction was announced as rates "
   "rose, took eighteen months of review and completed in November 2023. "
   "Customers and cloud providers have since complained about large price "
   "increases.",
  ],
   "The price is a purchase of customers who cannot leave cheaply. Whether "
   "that approach carries a delayed cost with customers is not yet "
   "established."),
 ]),

 ("2023", 8, [
  ("stone", "", "A change in what customers were asking for", [
   "ChatGPT was released in late 2022 and reached wide use through 2023. "
   "The consequence that mattered most to the companies on this page was the "
   "computing it required. Training a large model uses thousands of "
   "processors running for weeks, and demand for that capacity grew faster "
   "than the infrastructure to supply it.",
  ], ""),

  ("stone", "", "And almost no transactions", [
   "Technology deal volumes in 2023 were the weakest in more than a decade. "
   "High rates made debt expensive, valuations agreed in 2021 had not yet "
   "adjusted, and buyers and sellers disagreed about price. Periods like "
   "this are common after a sharp change in the cost of money and usually end "
   "when one side gives way.",
  ], ""),

  ("seal", "Acquisition &middot; $28bn &middot; announced September 2023", "Cisco / Splunk", [
   "Software records what it does, and a large organization produces "
   "enormous volumes of these records, called logs. Splunk collected them "
   "and made them searchable. Security teams pay for that because the "
   "evidence of an intrusion is scattered across thousands of systems, and "
   "engineering teams pay because modern applications are assembled from "
   "many services and diagnosing a failure means reading the record.",
   "Cisco paid $157 a share in cash, about $28 billion, a premium of roughly "
   "31 percent and its largest acquisition. It was announced in a year when "
   "very few large transactions were, and paid for in cash when cash was "
   "expensive.",
  ],
   "Splunk is paid for from two budgets. The open question is Cisco's "
   "ability to sell and run subscription software after decades of "
   "selling hardware."),
 ]),

 ("2024", 14, [
  ("stone", "", "Spending moves toward buildings and power", [
   "Capital spending by the largest cloud providers rose sharply from 2024, "
   "and a growing share of it went to data center construction, electrical "
   "capacity and cooling and not to software development. Facilities of "
   "this kind are measured in megawatts of power draw, and in several markets "
   "the limiting factor became how long a utility took to provide a grid "
   "connection.",
  ],
   "This is the third part of the thesis. The scarce input moved from ideas "
   "and processors toward electricity."),

  ("seal", "Acquisition &middot; ~$1.46bn &middot; announced March 2024", "Keysight / Spirent", [
   "Spirent made equipment for testing networks, which generates realistic "
   "traffic so an operator can find out how a network behaves under load "
   "before customers do.",
   "It is an ordinary industrial business. Its customers are equipment makers "
   "and network operators, it sells into long product development cycles and "
   "its position rests on having been validated against standards that "
   "change slowly. Keysight prevailed over a competing offer from Viavi "
   "Solutions and completed the purchase in October 2025, nineteen months "
   "after announcing it.",
  ],
   "A validated position in a slow-changing standard is another form of "
   "switching cost, and a modest one, which is consistent with the modest "
   "price."),
 ]),

 ("2025", 26, [
  ("seal", "Investment &middot; $300m at a $5bn valuation &middot; January 2025",
   "DDN / Blackstone", [
   "DataDirect Networks sells storage systems to organizations running very "
   "large computing jobs. It was founded in 1998 and spent most of its "
   "history selling to national laboratories and research institutions.",
   "A facility full of expensive processors is productive only while those "
   "processors have data to work on, so the customer is buying utilization of "
   "equipment it has already paid for. Blackstone Tactical Opportunities "
   "invested $300 million at a $5 billion valuation, and DDN said the money "
   "was for getting data to processors faster inside enterprise AI clusters.",
  ],
   "A $5 billion valuation on a private company is an expectation. Whether "
   "DDN reaches the revenue it has described is what to watch."),

  ("seal", "Acquisition &middot; $32bn announced &middot; March 2025", "Google / Wiz", [
   "Wiz sells software that scans a company's cloud infrastructure and "
   "identifies which combinations of settings create a real risk. Earlier "
   "tools produced long lists of warnings that were mostly ignored, and Wiz "
   "produced short lists and could be returning results within hours.",
   "Wiz ended discussions with Google in July 2024 at a reported $23 "
   "billion and stated an intention to go public. Eight months later it "
   "agreed to sell to the same buyer for $32 billion.",
  ],
   "Little about the business changed in that time. What Wiz gained was a "
   "credible alternative, and a seller with somewhere else to go negotiates "
   "from a stronger position."),

  ("seal", "Acquisition &middot; $31 per share &middot; announced December 2025",
   "IBM / Confluent", [
   "Confluent sells a commercial version of Apache Kafka, software that "
   "moves data between systems continuously and not in overnight batches. "
   "IBM agreed to pay $31 a share in cash, an enterprise value of roughly $11 "
   "billion.",
   "IBM's public case concerned AI systems that take actions and not only "
   "answer questions. Software of that kind needs current information, so the "
   "difference between data that is up to date and data that is a day old "
   "becomes operationally significant.",
  ], ""),

  ("stone", "", "How the construction was financed", [
   "Much of the 2025 activity on these balance sheets was financing and not "
   "acquisition. Datadog issued convertible notes, Seagate issued "
   "exchangeable notes and LendingTree arranged a term loan. These "
   "transactions rarely make headlines and they paid for the spending "
   "described above.",
   "A convertible note is a loan that the holder can exchange for shares on "
   "agreed terms. The borrower accepts possible dilution in return for a "
   "lower interest rate, and the lender accepts the lower rate in return for "
   "taking part if the shares rise. It suits companies whose shares are highly "
   "valued and whose cash flows are not yet large.",
  ], ""),
 ]),

 ("2026", 36, [
  ("stone", "", "Two large deals complete, at different prices than announced", [
   "Google completed the Wiz acquisition on 11 March 2026. Alphabet's "
   "quarterly filing puts the purchase price at approximately $29.5 billion "
   "after adjustments, against the $32 billion described at announcement a "
   "year earlier. IBM completed Confluent on 17 March 2026.",
   "The gap between an announced figure and a final one is routine and is "
   "reported much less prominently than the announcement. Announced values "
   "are a starting point and not a record of what changed hands.",
  ], ""),

  ("stone", "", "Storage returns to favor", [
   "Hard drives were widely expected to be displaced by flash memory, which "
   "is faster and has no moving parts. Demand for very large and cheap "
   "capacity, driven by the volume of data retained for AI training, "
   "improved the position of the remaining manufacturers, and Seagate raised "
   "money on terms more often associated with growth companies.",
   "Storage is a cyclical industry and current conditions are unusually "
   "favorable, so the entry describes a change in conditions and not a "
   "permanent reversal.",
  ], ""),

  ("stone", "", "Where this leaves things", [
   "As of October 2026 the constraint most often described by the companies on "
   "this page is electrical capacity and the time required to obtain it, and "
   "not ideas or access to processors. Whether that remains true depends on "
   "how quickly utilities and regulators respond, which is not a technology "
   "question.",
  ], ""),
 ]),
]
