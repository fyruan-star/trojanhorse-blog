"""Ten years of technology transactions, 2016 to 2026.

Written for a reader with no background in finance or engineering. Each entry
gets the explanation its facts deserve and no more. Some of these deals show an
attractive business. Others show an expensive response to a threat, a financing
decision, or a bet that did not pay.

Rules this file is held to. No recurring template. No punchline endings. No
claim that a buyer foresaw an outcome unless the record at announcement says
so. Values are identified as announced or final. No em dashes, no semicolons.

`width` is the spine's thickness for that year. It traces the broad shape of
the transaction cycle and is not plotted from a dataset, and the page says so.
"""

INTRO = (
 "This page records technology transactions announced between 2016 and 2026, "
 "with enough explanation to follow them without a background in finance or "
 "engineering. Some of these deals worked. Two were stopped by governments. "
 "One was abandoned because the asset would have been damaged by the sale.")

INTRO_2 = (
 "They are collected here because a small set of questions explains a "
 "surprising amount of what happened. What does this company sell. Who pays "
 "it, and why. What would a customer have to do in order to replace it. What "
 "did the buyer pay, and in what form. You can carry those four questions "
 "through the whole decade.")

CLOSE_HEAD = "What ten years of this actually shows"
CLOSE = [
 "Three patterns recur in these entries. None of them is a law, and each has "
 "exceptions on this same page.",

 "The first is that the businesses which held their value tend to sell "
 "something a customer would find expensive to replace, where the expense is "
 "measured in time and risk rather than in price. Red Hat, VMware and Arm are "
 "each a version of this. A bank that has certified a thousand applications "
 "against one vendor's software is not deciding whether a competitor is "
 "better. It is deciding whether to spend three years finding out.",

 "The second is that governments became a party to large semiconductor "
 "transactions in a way they had not been before 2018. Two of the three "
 "abandoned deals here ended in a regulator's office rather than a boardroom, "
 "and in both cases the objection was about who would hold a position in "
 "future rather than about prices today.",

 "The third is that a growing share of spending went toward physical "
 "capacity. That is visible in the Blackstone investment in DDN, in the data "
 "centre construction of 2024 and after, and in Seagate's return to the debt "
 "markets. It does not follow that software stopped mattering. Two of the "
 "largest transactions of the final two years were software companies.",

 "One more thing is worth saying because it is less comfortable. Several of "
 "these buyers have since been described as having seen what was coming. In "
 "most cases the record at announcement does not support that. It shows "
 "companies solving the problem in front of them, and the problem in front of "
 "them turning out to matter more than anyone said at the time. That is a "
 "different and more useful observation, because the first kind of foresight "
 "cannot be copied and the second kind can.",
]

# kind: seal (completed or pending deal), column (abandoned), stone (not a deal)
# each node: (kind, tag, title, [paragraphs], note_or_empty)
YEARS = [

 ("2016", 20, [
  ("stone", "", "A slower market", [
   "Smartphone shipments grew about three percent in 2016, against roughly ten "
   "percent the year before. Growth did not stop, and the first annual decline "
   "came in 2017, but the slowdown was enough to change what large technology "
   "companies spent money on. A business built around a market that doubles "
   "every few years makes different decisions from one built around a market "
   "that grows slightly.",
  ], ""),

  ("seal", "Acquisition &middot; $32bn &middot; announced July 2016", "SoftBank / Arm", [
   "Arm designs the instruction set that processors are built around, and "
   "licenses it. It does not manufacture anything. Companies including Apple, "
   "Qualcomm and Samsung take the design, build a chip around it, and pay Arm a "
   "royalty on each one sold. The royalty is a few cents. The volume at the "
   "time was over fifteen billion chips a year.",
   "Two features of that arrangement are worth noticing. Arm does not compete "
   "with the companies that license from it, which is part of why they were "
   "willing to standardise on its designs. And because it owns no factories, it "
   "has none of the capital spending or inventory risk that the rest of the "
   "industry carries.",
   "SoftBank paid about $32 billion in cash, a premium of roughly 43 percent. "
   "At the time most of Arm's royalties came from mobile devices, and the "
   "common criticism was that SoftBank had paid a high price for exposure to a "
   "market that was flattening.",
  ],
   "Arm's designs were later used well outside mobile, in server processors "
   "from Amazon and Nvidia among others. By 2026 Arm-based machines accounted "
   "for a large share of data centre server revenue, though a much smaller "
   "share of unit shipments, and the gap between those two figures is worth "
   "holding onto. SoftBank listed Arm publicly again in 2023 at a considerably "
   "higher valuation and kept most of it."),
 ]),

 ("2017", 17, [
  ("seal", "Acquisition &middot; $15.3bn &middot; announced March 2017", "Intel / Mobileye", [
   "Mobileye made the camera systems and software that let a car recognise a "
   "lane, a pedestrian or a vehicle ahead. It sold to carmakers, who designed "
   "it into models years before those models reached showrooms, which made the "
   "revenue unusually predictable once a design win was secured.",
   "Intel paid about $15.3 billion. Mobileye's revenue the previous year was "
   "around $358 million. A buyer paying more than forty times revenue is "
   "assuming either that revenue grows by a large multiple or that the asset "
   "has value beyond its current sales, and Intel said publicly that it saw "
   "the car as a future computing platform.",
   "Intel had missed mobile almost entirely and was explicit that it did not "
   "intend to miss the next category. Whether that is good reasoning or an "
   "expensive way of managing a previous mistake depends on what you think the "
   "alternative was.",
  ], ""),

  ("seal", "Carve-out &middot; ~$18bn &middot; signed September 2017", "Toshiba Memory", [
   "Toshiba sold its memory chip business to a consortium led by Bain Capital, "
   "after losses in its nuclear division left it needing cash. The business "
   "made NAND flash, the storage in phones, laptops and data centres.",
   "The sale took close to a year to complete because several governments took "
   "an interest in who would end up owning it. That was an early example of "
   "something which became routine later in the decade.",
  ], ""),
 ]),

 ("2018", 26, [
  ("column", "Prohibited &middot; ~$117bn &middot; March 2018", "Broadcom / Qualcomm", [
   "Broadcom pursued Qualcomm without its board's agreement and raised its "
   "offer to around $117 billion. Qualcomm holds a large body of patents "
   "covering how mobile devices communicate with networks, and was then "
   "heavily involved in the committee work that produced the 5G standards.",
   "In March 2018 a presidential order prohibited the transaction, following a "
   "review by the Committee on Foreign Investment in the United States. "
   "Broadcom was domiciled in Singapore at the time, which gave the committee "
   "jurisdiction. The stated concern was that Broadcom's approach of reducing "
   "research spending at companies it acquired would weaken American "
   "participation in those standards committees.",
  ],
   "This was the first time a technology transaction of that size was stopped "
   "on national security grounds rather than competition grounds. The reasoning "
   "about standards participation is the committee's, and it was contested by "
   "Broadcom at the time."),

  ("column", "Abandoned &middot; $44bn &middot; July 2018", "Qualcomm / NXP", [
   "Qualcomm agreed to buy NXP Semiconductors in 2016 and spent close to two "
   "years collecting regulatory approvals. All of them arrived except one. "
   "Chinese approval did not come, and in July 2018 Qualcomm let the agreement "
   "lapse and paid NXP a $2 billion termination fee.",
   "A termination fee of that size is agreed in advance precisely because "
   "approval is uncertain. It compensates the seller for the time spent waiting "
   "and for the disruption of being publicly in play.",
  ], ""),

  ("seal", "Acquisition &middot; $34bn &middot; announced October 2018", "IBM / Red Hat", [
   "Red Hat's main product is a version of Linux, which is free software. "
   "Anyone can download it. What Red Hat sold was a version somebody would "
   "stand behind: tested, patched, supported, and certified to work alongside "
   "the other systems a bank or a hospital runs.",
   "That is a subscription business, and its strength comes from what a "
   "customer would have to do in order to leave. A large institution that has "
   "certified several hundred applications against one distribution would have "
   "to test all of them again. The cost is measured in years of work and in the "
   "risk of something breaking, not in the price of the alternative.",
   "IBM paid $190 a share in cash, around $34 billion including assumed debt, a "
   "premium above 60 percent. It had been losing ground in cloud computing to "
   "Amazon and Microsoft for several years. Rather than compete with them "
   "directly, it bought software that enterprises use across more than one "
   "cloud provider.",
  ],
   "IBM's share price has not obviously rewarded the purchase, which is the "
   "usual objection. The more specific question is whether software whose value "
   "rests on working equally well with every cloud can be owned by a company "
   "that also sells one."),
 ]),

 ("2019", 19, [
  ("seal", "Acquisition &middot; $6.9bn &middot; announced March 2019", "Nvidia / Mellanox", [
   "Mellanox made high speed networking equipment, principally a technology "
   "called InfiniBand, designed for connecting computers inside a single "
   "facility rather than across the internet. Its customers were mostly "
   "scientific computing centres running weather models, physics simulations "
   "and genomics work.",
   "The reason that market exists is worth understanding. A large computing job "
   "split across many machines requires those machines to stop periodically and "
   "exchange results. If the connection between them is slow, the processors "
   "spend their time waiting rather than working, and a facility full of "
   "expensive equipment produces less than it could. Networking determines how "
   "much of that equipment is actually in use.",
   "Nvidia paid $6.9 billion in cash, its largest acquisition to that point. "
   "Intel was reported to have bid as well. The stated rationale at announcement "
   "concerned data centre computing, which was already a growing part of "
   "Nvidia's business.",
  ],
   "The demand for training large AI models arrived some years later and made "
   "this capability far more valuable than it was in 2019. I would separate "
   "those two facts. The purchase is explicable on what Nvidia's customers were "
   "already doing. It does not require, and the announcement does not claim, "
   "that anyone anticipated 2023."),

  ("seal", "Acquisition &middot; $15.7bn &middot; announced June 2019", "Salesforce / Tableau", [
   "Tableau made software for turning company data into charts that "
   "non-specialists could build themselves. Salesforce paid about $15.7 billion "
   "in its own shares.",
   "Analysis software tends to be sticky for a practical reason. Once an "
   "organisation has built hundreds of reports that finance and sales rely on "
   "weekly, moving to a competitor means rebuilding all of them and retraining "
   "the people who use them. The switching cost sits in the work already done.",
  ], ""),
 ]),

 ("2020", 24, [
  ("stone", "", "Borrowing becomes very cheap", [
   "Central banks cut interest rates to near zero in response to the pandemic "
   "and held them there. Cheap borrowing raises what buyers can afford to pay "
   "and raises the price of assets whose value depends on earnings far in the "
   "future. Most of the transactions in the next two years were negotiated "
   "under those conditions, and several of them look different once that is "
   "taken into account.",
  ], ""),

  ("seal", "Acquisition &middot; $35bn at announcement &middot; October 2020", "AMD / Xilinx", [
   "Xilinx made field programmable gate arrays, chips that can be reconfigured "
   "after manufacture. They are slower than a chip built for one purpose and "
   "more flexible, which suits applications where the task changes, such as "
   "telecommunications equipment.",
   "AMD paid entirely in its own shares at a fixed exchange ratio of 1.7234 AMD "
   "shares for each Xilinx share. It is worth being clear about what that "
   "means. No cash left AMD. Xilinx shareholders gave up their shares and "
   "received an ownership interest in the combined company, so they continue to "
   "bear the results. AMD's share price had risen sharply over the preceding "
   "years, which is what made a purchase of this size possible for a company "
   "that had been in difficulty a few years earlier.",
   "Because the ratio was fixed and the share price was not, the value of the "
   "consideration moved between announcement and completion. The deal was "
   "described as about $35 billion in October 2020 and closed in February 2022 "
   "at a figure widely reported near $49 billion. Nothing about Xilinx changed "
   "to account for the difference.",
  ],
   "This is the most useful mechanical point on the page. A headline value for "
   "an all-stock transaction is the buyer's share price on one day multiplied "
   "by a ratio. Using it as though it were a price paid will mislead you, and "
   "it is a common error in published comparisons."),
 ]),

 ("2021", 40, [
  ("stone", "", "The busiest year on record", [
   "Global deal volumes reached their highest level ever recorded in 2021, "
   "helped by cheap debt, high equity prices and a large number of blank cheque "
   "vehicles raised to buy companies. Several transactions agreed that year "
   "were renegotiated or abandoned once conditions changed.",
  ], ""),

  ("seal", "Acquisition &middot; $19.7bn &middot; announced April 2021", "Microsoft / Nuance", [
   "Nuance sold speech recognition software, with its strongest position in "
   "hospitals, where it is used to turn a clinician's dictation into a patient "
   "record. Microsoft paid $56 a share in cash, about $19.7 billion including "
   "debt.",
   "The attraction of the business was less the software than the access. "
   "Health systems are slow and cautious about who they let near patient data, "
   "for sound regulatory reasons, and a supplier already installed and approved "
   "is in a position that is difficult to buy any other way.",
  ], ""),
 ]),

 ("2022", 20, [
  ("stone", "", "Rates rise and the market for new listings closes", [
   "Interest rates rose quickly through 2022. The Nasdaq composite fell by "
   "roughly a third over the year, debt became more expensive, and the market "
   "for initial public offerings effectively shut. Companies that had expected "
   "to list stayed private, which is where a growing share of large technology "
   "businesses has remained.",
  ], ""),

  ("column", "Abandoned &middot; $40bn &middot; February 2022", "Nvidia / Arm", [
   "Nvidia agreed in September 2020 to buy Arm from SoftBank for up to $40 "
   "billion in cash and stock. Seventeen months later the parties abandoned it, "
   "and SoftBank kept a $1.25 billion payment Nvidia had made in advance.",
   "The difficulty was structural rather than ordinary competition law. Arm's "
   "licensees include most of Nvidia's competitors, and they license from Arm "
   "partly because Arm does not build chips itself. Several of them objected, "
   "publicly and to regulators in the United States, the United Kingdom and the "
   "European Union. Qualcomm was among the most vocal.",
   "SoftBank listed Arm on Nasdaq in September 2023 instead, at a valuation "
   "well above what Nvidia had offered.",
  ],
   "The question this raises is worth carrying. Where part of an asset's value "
   "comes from its independence, a sale to an interested party reduces what is "
   "being bought. Standards, marketplaces and benchmarks all have some of this "
   "property. Arm itself announced its own server processor in March 2026, "
   "which places it in a version of the same tension with its licensees."),

  ("seal", "Acquisition &middot; $61bn &middot; announced May 2022", "Broadcom / VMware", [
   "VMware's core product allows one physical server to run as several separate "
   "machines. It sits underneath a large amount of corporate computing and is "
   "difficult to remove without a long migration project.",
   "Broadcom's approach to acquisitions is consistent and publicly visible "
   "across CA Technologies, Symantec's enterprise business and now VMware. It "
   "buys established infrastructure software, reduces research spending and "
   "smaller product lines, concentrates on the largest customers, and raises "
   "prices. The return does not depend on the acquired business growing.",
   "The transaction was announced into deteriorating conditions and took "
   "eighteen months of regulatory review in several jurisdictions before "
   "completing in November 2023. Customers subsequently reported substantial "
   "increases in what they pay, and some moved to alternatives.",
  ],
   "I would separate two things here. That the approach is profitable is "
   "observable in Broadcom's results over two decades. Whether it has a cost "
   "that arrives later, in customers who avoid the company when they have a "
   "choice, is a reasonable concern and not something the record yet settles."),
 ]),

 ("2023", 8, [
  ("stone", "", "A change in what customers were asking for", [
   "ChatGPT was released in late 2022 and reached wide use through 2023. The "
   "commercial consequence that mattered most to the companies on this page was "
   "not the software itself but the computing it required. Training a large "
   "model uses thousands of processors running for weeks, and the demand for "
   "that capacity grew faster than the infrastructure to supply it.",
  ], ""),

  ("stone", "", "And almost no transactions", [
   "Technology deal volumes in 2023 were the weakest in more than a decade. "
   "High rates made debt financing expensive, valuations agreed in 2021 had not "
   "yet adjusted, and buyers and sellers disagreed about price. Periods like "
   "this are common after a sharp change in the cost of money and they usually "
   "end when one side gives way.",
  ], ""),

  ("seal", "Acquisition &middot; $28bn &middot; announced September 2023", "Cisco / Splunk", [
   "Software records what it does. A failed request, a login, a server "
   "restarting at four in the morning. These records are called logs, and a "
   "large organisation generates an enormous volume of them. Splunk collected "
   "them and made them searchable.",
   "Two groups pay for that. Security teams, because the evidence of an "
   "intrusion is scattered across thousands of systems and has to be found "
   "quickly. And engineering teams, because modern applications are assembled "
   "from many separate services and no individual understands the whole, so "
   "diagnosing a failure means reading the record.",
   "Cisco paid $157 a share in cash, around $28 billion, its largest "
   "acquisition. It was announced in a year when very few large transactions "
   "were, and paid for in cash when cash was expensive.",
  ],
   "The open question is execution rather than price. Cisco has sold hardware "
   "to these customers for decades and selling software subscriptions is a "
   "different business. Hardware companies have attempted this before with "
   "mixed results."),
 ]),

 ("2024", 14, [
  ("stone", "", "Spending moves toward buildings and power", [
   "Capital spending by the largest cloud providers rose sharply from 2024 "
   "onward, and a growing share of it went to data centre construction, "
   "electrical capacity and cooling rather than to software development. "
   "Facilities of this kind are measured in megawatts of power draw, and in "
   "several markets the limiting factor became how long a utility took to "
   "provide a grid connection.",
  ], ""),

  ("seal", "Acquisition &middot; ~$1.46bn &middot; announced March 2024", "Keysight / Spirent", [
   "Spirent made equipment for testing networks: hardware and software that "
   "generates realistic traffic so an operator can find out how a network "
   "behaves under load before customers do.",
   "This is an ordinary industrial business and worth understanding on those "
   "terms. Its customers are equipment makers and network operators, it sells "
   "into long product development cycles, and its competitive position rests on "
   "having been validated against standards that change slowly. Keysight "
   "prevailed over a competing offer from Viavi Solutions and completed the "
   "purchase in October 2025, nineteen months after announcing it.",
  ], ""),
 ]),

 ("2025", 26, [
  ("seal", "Investment &middot; $300m at a $5bn valuation &middot; January 2025",
   "DDN / Blackstone", [
   "DataDirect Networks sells storage systems to organisations running very "
   "large computing jobs. It was founded in 1998 and spent most of its history "
   "selling to national laboratories, research institutions and other "
   "scientific computing customers.",
   "The economics are easier to follow than the category suggests. A facility "
   "full of expensive processors is only productive while those processors have "
   "data to work on. If the storage system cannot supply data quickly enough, "
   "the processors idle. The customer is therefore buying utilisation of "
   "equipment it has already paid for, which is why this kind of supplier can "
   "charge well despite selling what sounds like a commodity.",
   "Blackstone Tactical Opportunities invested $300 million at a $5 billion "
   "valuation. DDN said the money was for getting data to processors faster "
   "inside enterprise AI clusters and that it was aiming at a billion dollars "
   "of revenue.",
  ],
   "A $5 billion valuation on a private company is an expectation rather than a "
   "result. Whether DDN reaches the revenue it has described is the thing to "
   "watch, and it has not yet."),

  ("seal", "Acquisition &middot; $32bn announced &middot; March 2025", "Google / Wiz", [
   "Wiz sells software that scans a company's cloud infrastructure and "
   "identifies which combinations of settings actually create a risk. Earlier "
   "tools in this category produced long lists of warnings that were mostly "
   "ignored. Wiz produced short lists, and could be connected and returning "
   "results in hours rather than months, which is most of why it grew quickly.",
   "Wiz had ended earlier discussions with Google in July 2024, at a reported "
   "$23 billion, citing antitrust and investor concerns and stating an "
   "intention to go public. Its annual recurring revenue was reported above "
   "$500 million at that point, against $350 million a year earlier.",
   "Eight months later it agreed to sell to the same buyer for $32 billion. The "
   "difference is instructive. Little about the business changed in that time. "
   "What Wiz had was a credible alternative, in the form of a listing, and a "
   "seller with somewhere else to go is in a materially stronger position than "
   "one without.",
  ],
   "Google committed publicly to keeping Wiz working on Amazon's and "
   "Microsoft's cloud services as well as its own. Google Cloud has been third "
   "in that market for years, and software that customers use regardless of "
   "which provider they chose is a way of earning revenue from estates it has "
   "not won."),

  ("seal", "Acquisition &middot; $31 per share &middot; announced December 2025",
   "IBM / Confluent", [
   "Confluent sells a commercial version of Apache Kafka, software that moves "
   "data between systems continuously rather than in overnight batches. IBM "
   "agreed to pay $31 a share in cash, an enterprise value of roughly $11 "
   "billion.",
   "The case IBM made publicly concerned AI systems that take actions rather "
   "than answer questions. Software of that kind needs current information, so "
   "the difference between data that is up to date and data that is a day old "
   "becomes operationally significant.",
  ], ""),

  ("stone", "", "How the construction was financed", [
   "Much of the 2025 activity on these balance sheets was not acquisition but "
   "financing. Datadog issued convertible notes. Seagate issued exchangeable "
   "notes. LendingTree arranged a term loan. None of this makes headlines and "
   "it is how the spending described above was paid for.",
   "A convertible note is a loan that the holder can exchange for shares on "
   "agreed terms. The borrower accepts that possible dilution in return for a "
   "lower interest rate, and the lender accepts the lower rate in return for "
   "participating if the shares rise. It suits companies whose shares are "
   "highly valued and whose cash flows are not yet large.",
  ], ""),
 ]),

 ("2026", 36, [
  ("stone", "", "Two large deals complete, at different prices than announced", [
   "Google completed the Wiz acquisition on 11 March 2026. Alphabet's quarterly "
   "filing puts the purchase price at approximately $29.5 billion after "
   "adjustments, against the $32 billion described at announcement a year "
   "earlier. IBM completed Confluent on 17 March 2026.",
   "The gap between an announced figure and a final one is routine and is "
   "rarely reported with the same prominence. It is one reason to treat "
   "announcement values as a starting point rather than a record of what "
   "changed hands.",
  ], ""),

  ("stone", "", "Storage returns to favour", [
   "Hard drives were widely expected to be displaced by flash memory, which is "
   "faster and has no moving parts. Demand for very large and comparatively "
   "cheap capacity, driven by the volume of data being retained for AI "
   "training, improved the position of the remaining manufacturers. Seagate "
   "raised money on terms more often associated with growth companies.",
   "I would be careful about reading this as a permanent reversal. It is a "
   "cyclical industry and the current conditions are unusually favourable.",
  ], ""),

  ("stone", "", "Where this leaves things", [
   "As of October 2026 the constraint most often described by the companies on "
   "this page is not ideas, and not access to processors. It is electrical "
   "capacity and the time required to obtain it. Whether that remains true "
   "depends on how quickly utilities and regulators respond, which is not a "
   "technology question.",
  ], ""),
 ]),
]
