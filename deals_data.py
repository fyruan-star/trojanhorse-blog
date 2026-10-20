"""Ten longer notes on transactions from the timeline.

Each one is organised around what the facts of that deal require. The headings
differ because the deals differ. There is no recurring reveal, no closing
flourish, and no claim that a buyer anticipated an outcome unless the record at
announcement supports it.

Values are identified as announced or final. No em dashes, no semicolons.
"""

DEALS = [

 dict(slug="the-blueprint", year="2016", roman="I",
  lead="SoftBank and", line1="Arm", line2="",
  sub="WHAT A COMPANY THAT MAKES NOTHING SELLS,<br>AND WHY IT IS DIFFICULT TO DISPLACE",
  party="SoftBank / Arm", value="$32bn, announced", dated="July 2016",
  lede=("SoftBank agreed to acquire Arm Holdings in July 2016 for about GBP "
        "24.3 billion, roughly $32 billion, at 1,700 pence a share in cash. "
        "That was a premium of approximately 43 percent to the previous close. "
        "Arm has never manufactured a chip."),
  sections=[
   ("The business", [
    "Arm designs the instruction set a processor is built around, which is the "
    "basic vocabulary the chip understands, along with reference designs for "
    "the processor cores themselves. It licenses both to other companies.",
    "A licensee such as Apple or Qualcomm pays an upfront fee for access to the "
    "design, then a royalty on each chip it ships. The royalty is typically a "
    "few cents. At the time of the acquisition the industry was shipping well "
    "over fifteen billion Arm-based chips a year.",
    "Two things make that position durable. Software compiled for one "
    "instruction set does not run on another without being rebuilt and "
    "retested, so an industry that has standardised on a design carries a real "
    "cost to move away from it. And because Arm does not manufacture chips, it "
    "does not compete with the companies licensing from it, which mattered to "
    "licensees competing fiercely with each other.",
   ]),
   ("The price, and what it required", [
    "A 43 percent premium paid in cash is a considerable commitment. At the "
    "time the large majority of Arm's royalty revenue came from mobile devices, "
    "and smartphone shipment growth had slowed to around three percent that "
    "year from roughly ten percent the year before.",
    "The criticism at announcement was straightforward. SoftBank had paid a "
    "high price for a business whose main end market was maturing. On the "
    "information available, that was a reasonable thing to say.",
   ]),
   ("What happened afterward", [
    "Arm designs were subsequently adopted well outside mobile devices. Amazon "
    "built server processors on them for its own cloud, and Nvidia used an "
    "Arm-based design for the processor paired with its accelerators. By 2026, "
    "industry figures put Arm-based machines at a substantial share of data "
    "centre server revenue, although at a much lower share of unit shipments. "
    "Those two measures differ enough that it is worth knowing which one you "
    "are being shown.",
    "SoftBank listed Arm on Nasdaq again in September 2023 at a valuation "
    "considerably above what it had paid, retaining most of the company.",
    "I would not read this as evidence that SoftBank anticipated demand for AI "
    "infrastructure. The public case made in 2016 concerned connected devices "
    "generally. What the purchase did require was a judgement that the "
    "licensing position was more durable than the end market it then served, "
    "and that judgement was correct.",
   ]),
  ],
  takeaway=("A licensing business can be worth more than its current end market "
            "suggests, because the royalty follows the design wherever the "
            "design is adopted next."),
  srcs=["SoftBank Group, recommended cash acquisition of ARM Holdings plc, announced 18 July 2016. GBP 24.3bn, 1,700 pence per share, premium of approximately 43 percent.",
        "Arm licensing and royalty structure, and annual shipment volumes, from the company's own disclosures and its 2023 listing documents.",
        "Smartphone shipment growth of approximately three percent in 2016 against roughly ten percent in 2015, per IDC estimates reported at the time. The first annual decline came in 2017.",
        "Arm Holdings plc listed on Nasdaq in September 2023. Data centre share figures for 2026 vary considerably by measure and are described here as reported ranges rather than a single number."]),

 dict(slug="the-blocked-bid", year="2018", roman="II",
  lead="Broadcom and", line1="Qualcomm", line2="",
  sub="A TAKEOVER PROHIBITED ON NATIONAL SECURITY<br>GROUNDS RATHER THAN COMPETITION GROUNDS",
  party="Broadcom / Qualcomm", value="~$117bn, prohibited", dated="March 2018",
  lede=("Broadcom pursued Qualcomm from November 2017 without the agreement of "
        "its board, raising its offer to around $117 billion. In March 2018 a "
        "presidential order prohibited the transaction, following a review by "
        "the Committee on Foreign Investment in the United States."),
  sections=[
   ("What Qualcomm owns", [
    "Qualcomm sells mobile processors, and it also holds a large body of "
    "patents covering how a handset communicates with a network. Manufacturers "
    "pay licence fees on those patents, a business that has been both "
    "consistently profitable and frequently litigated.",
    "In 2017 and 2018 Qualcomm was among the most active participants in the "
    "committee work producing the 5G standards. Standards are negotiated over "
    "years, and companies contributing more engineers tend to hold more of the "
    "patents that end up essential to the result.",
   ]),
   ("Why the review reached the conclusion it did", [
    "Broadcom's record with companies it acquires is public. It reduces "
    "research spending, concentrates on the most profitable product lines, and "
    "returns cash to shareholders. Applied to Qualcomm, the committee's view "
    "was that this would reduce American participation in the standards process "
    "and that other participants, principally Huawei, would fill the gap.",
    "Broadcom was domiciled in Singapore at the time, which gave the committee "
    "jurisdiction. Broadcom disputed the analysis and offered commitments on "
    "research spending. The order was issued regardless.",
   ]),
   ("What changed as a result", [
    "Before this, large technology acquisitions were reviewed principally for "
    "their effect on competition. Afterward, the relevant question for "
    "semiconductor transactions included who would hold a position in a future "
    "standard, and that question is answered by governments rather than by "
    "markets.",
    "Subsequent export controls, entity listings and manufacturing subsidies "
    "followed similar reasoning. I would be careful about treating the 2018 "
    "order as their cause. It is better described as the first occasion on "
    "which that reasoning was applied at this scale, in public.",
   ]),
   ("The practical consequence for a buyer", [
    "Approval risk in deals of this size is no longer confined to an antitrust "
    "analysis a bidder can model. It now includes a national interest "
    "assessment that may turn on a forecast of industrial capability several "
    "years out. That is difficult to price, and it is one reason large "
    "semiconductor agreements carry substantial termination fees and long "
    "outside dates.",
   ]),
  ],
  takeaway=("Approval risk in semiconductors stopped being a question about "
            "market share and became a question about national capability, "
            "which a bidder cannot model in the same way."),
  srcs=["Broadcom Limited's unsolicited proposals for Qualcomm Incorporated from November 2017, raised to approximately $121bn including assumed debt in February 2018 and subsequently reduced to around $117bn.",
        "Presidential Order of 12 March 2018 prohibiting the proposed takeover, on the recommendation of the Committee on Foreign Investment in the United States.",
        "The reasoning concerning 5G standards participation is the committee's, as set out in its correspondence and the order. Broadcom disputed it publicly at the time."]),

 dict(slug="the-layer-above", year="2018", roman="III",
  lead="IBM and", line1="Red Hat", line2="",
  sub="A SUBSCRIPTION BUSINESS BUILT ON SOFTWARE<br>THAT ANYONE CAN DOWNLOAD FOR NOTHING",
  party="IBM / Red Hat", value="$34bn", dated="Announced October 2018",
  lede=("IBM agreed to acquire Red Hat in October 2018 at $190 a share in cash, "
        "approximately $34 billion including assumed debt and a premium above "
        "60 percent. It completed in July 2019. Red Hat's principal product is "
        "free software."),
  sections=[
   ("What customers are paying for", [
    "Red Hat Enterprise Linux is a distribution of Linux, which is open source. "
    "The code is available at no charge and can be downloaded, modified and "
    "redistributed by anyone.",
    "What Red Hat sold was a supported version. Tested across a defined set of "
    "hardware, patched on a published schedule for a long support window, and "
    "certified to work with the commercial applications a bank or hospital "
    "runs. The subscription buys accountability and a maintenance commitment "
    "rather than access to the software.",
    "The strength of that position comes from work the customer has already "
    "done. An institution that has certified several hundred applications "
    "against one distribution would have to repeat that testing to move. The "
    "cost is counted in engineering years and in the risk of an outage, not in "
    "the licence fee of an alternative.",
   ]),
   ("Why IBM was the buyer", [
    "IBM had lost ground in cloud computing to Amazon and Microsoft over the "
    "preceding years and had no realistic path to catching them by building. "
    "Buying a fourth-place cloud provider would have been expensive and would "
    "not have addressed the problem.",
    "Red Hat offered something different. Its software is used by enterprises "
    "across more than one cloud provider and in their own facilities, so its "
    "revenue does not depend on which provider wins.",
   ]),
   ("The open question", [
    "IBM's share price has not clearly reflected the purchase in the years "
    "since, which is the objection usually raised. A more specific question is "
    "more useful.",
    "The value of software whose selling point is that it works equally well "
    "everywhere depends on customers believing it will continue to. IBM also "
    "sells a cloud service. Whether an owner in that position can maintain the "
    "neutrality the asset relies on is a question about organisational "
    "behaviour, and no single year of results settles it.",
   ]),
  ],
  takeaway=("Where a customer has spent years certifying against one supplier, "
            "the supplier's pricing power comes from that work rather than "
            "from the product being better."),
  srcs=["IBM and Red Hat, announced 28 October 2018. $190.00 per share in cash, approximately $34bn including assumed debt. Completed 9 July 2019.",
        "Red Hat's subscription, support and certification model from the company's filings prior to acquisition.",
        "IBM's cloud market position relative to Amazon Web Services and Microsoft Azure from contemporaneous market share estimates, which vary by source."]),

 dict(slug="the-wiring", year="2019", roman="IV",
  lead="Nvidia and", line1="Mellanox", line2="",
  sub="WHY THE CONNECTIONS BETWEEN MACHINES<br>DETERMINE THE VALUE OF THE MACHINES",
  party="Nvidia / Mellanox", value="$6.9bn", dated="Announced March 2019",
  lede=("Nvidia agreed to acquire Mellanox Technologies in March 2019 at $125 a "
        "share in cash, about $6.9 billion. It was Nvidia's largest acquisition "
        "to that point and completed in April 2020 after regulatory review."),
  sections=[
   ("What Mellanox sold", [
    "Mellanox made high speed networking hardware, principally for a technology "
    "called InfiniBand. This is not internet networking. It is designed for "
    "connecting machines inside a single facility, where delay is measured in "
    "microseconds and consistency matters more than distance.",
    "Its customers were largely scientific computing centres. National "
    "laboratories, weather services, genomics institutes. The market was "
    "specialised and not large.",
   ]),
   ("Why that equipment determines the value of other equipment", [
    "A computing job too large for one machine is divided across many. Those "
    "machines cannot work entirely independently, because each periodically "
    "needs results the others have produced. So they stop, exchange, and "
    "continue.",
    "If the connection between them is slow or inconsistent, every machine "
    "waits for the slowest exchange. The practical effect is that an operator "
    "who has bought a facility full of expensive processors gets less work out "
    "of them. The industry measures this as utilisation, and at large scale the "
    "network often sets it.",
    "This is why a networking supplier can charge well for what looks like "
    "commodity hardware. The customer is not comparing it against other cables. "
    "It is comparing the cost against idle time on equipment it has already "
    "bought.",
   ]),
   ("Separating the purchase from what followed", [
    "Nvidia's stated rationale at announcement concerned data centre computing, "
    "already a growing part of its business. Intel was reported to have bid for "
    "the same asset.",
    "Demand for training large AI models arrived several years later and made "
    "this capability far more valuable than it was in 2019. I would keep those "
    "two facts apart. The acquisition is adequately explained by what Nvidia's "
    "existing customers were already doing, and nothing in the announcement "
    "claims anticipation of what came after. Describing it as foresight makes "
    "it sound less repeatable than it was.",
   ]),
  ],
  takeaway=("The supplier whose product determines how much use a customer gets "
            "from equipment it has already bought is in a stronger position "
            "than the category description suggests."),
  srcs=["NVIDIA Corporation and Mellanox Technologies, announced 11 March 2019, $125.00 per share in cash, approximately $6.9bn. Completed April 2020.",
        "InfiniBand's role in high performance computing from Nvidia's and Mellanox's own technical documentation.",
        "Competing interest from other bidders was reported at the time and has not been confirmed by the parties."]),

 dict(slug="paid-in-paper", year="2020", roman="V",
  lead="AMD and", line1="Xilinx", line2="",
  sub="WHAT AN ALL-STOCK TRANSACTION ACTUALLY IS,<br>AND WHY ITS HEADLINE VALUE MOVES",
  party="AMD / Xilinx", value="$35bn announced, ~$49bn at close", dated="October 2020",
  lede=("AMD agreed to acquire Xilinx in October 2020 in an all-stock "
        "transaction valued at approximately $35 billion at announcement. It "
        "completed in February 2022 at a figure widely reported near $49 "
        "billion. Xilinx's business had not changed to account for the "
        "difference."),
  sections=[
   ("What all-stock means", [
    "No cash left AMD. Xilinx shareholders gave up their shares and received "
    "newly issued AMD shares at a fixed ratio of 1.7234 AMD shares for each "
    "Xilinx share.",
    "The important consequence is that the seller does not exit. Xilinx "
    "shareholders became owners of the combined company and continue to bear "
    "its results, good or bad. That is a different arrangement from a cash sale "
    "and it changes how both sides think about price, because a seller taking "
    "stock is accepting a view on the buyer as well as on its own business.",
    "AMD's share price had risen very substantially over the preceding years. "
    "That is what made a purchase of this size available to a company which had "
    "been in serious difficulty not long before.",
   ]),
   ("Why the number moved", [
    "The exchange ratio was fixed in October 2020. AMD's share price was not. "
    "Between announcement and completion in February 2022 AMD stock rose, and "
    "the value of the consideration rose with it.",
    "So the $35 billion reported at announcement was AMD's share price on one "
    "day multiplied by the number of shares to be issued. Treating it as a "
    "price paid will mislead you, and published comparisons of what companies "
    "in a sector are worth frequently make exactly this error.",
   ]),
   ("The business acquired", [
    "Xilinx made field programmable gate arrays, chips whose logic can be "
    "reconfigured after manufacture. They are slower and more expensive per "
    "unit of work than a chip designed for one fixed purpose, and they suit "
    "applications where the task changes or the volume does not justify a "
    "custom design. Telecommunications equipment was the largest market.",
    "AMD's stated case concerned a broader data centre product range. The "
    "business has since been reported within AMD's embedded segment, and I "
    "would treat claims about its contribution to AMD's AI revenue carefully, "
    "because the company does not break it out in a way that settles the "
    "question.",
   ]),
  ],
  takeaway=("In an all-stock deal the announced value is the buyer's share "
            "price on a single day, and the seller has taken an ownership "
            "position rather than been paid."),
  srcs=["Advanced Micro Devices, Inc. and Xilinx, Inc., announced 27 October 2020. All-stock, 1.7234 AMD shares per Xilinx share, approximately $35bn at announcement.",
        "Completed 14 February 2022. The higher figure at completion reflects AMD share price appreciation and is widely reported at around $49bn.",
        "AMD does not separately disclose Xilinx-derived revenue in a form permitting precise attribution, and this note does not attempt one."]),

 dict(slug="too-central", year="2022", roman="VI",
  lead="Nvidia and", line1="Arm", line2="",
  sub="AN ASSET WHOSE VALUE DEPENDED<br>ON NOT BEING OWNED BY A COMPETITOR",
  party="Nvidia / Arm, abandoned", value="$40bn", dated="Announced September 2020",
  lede=("Nvidia agreed in September 2020 to acquire Arm from SoftBank for up to "
        "$40 billion in cash and stock. In February 2022 the parties abandoned "
        "the transaction. SoftBank retained $1.25 billion that Nvidia had paid "
        "in advance."),
  sections=[
   ("The case for it", [
    "Nvidia was becoming the most commercially important designer of processors "
    "for data centre computing. Arm owned the instruction set most processors "
    "outside the personal computer market are built around. A combination would "
    "have given one company a position across a very wide range of computing.",
    "SoftBank wanted to sell, the price was high, and both boards agreed terms.",
   ]),
   ("Why it could not complete", [
    "Arm licenses its designs to companies that compete intensely with one "
    "another. Part of why they were willing to build on a common foundation is "
    "that Arm builds no chips and therefore has no stake in which of them wins.",
    "Nvidia does build chips and competes with a significant number of Arm "
    "licensees. Several objected, publicly and in submissions to regulators in "
    "the United States, the United Kingdom and the European Union. Qualcomm was "
    "among the more vocal. The objection was not that the combined company "
    "would hold too large a share of a defined market. It was that an "
    "interested owner would have visibility into competitors' plans and "
    "influence over their costs.",
    "SoftBank listed Arm on Nasdaq in September 2023 instead, at a valuation "
    "well above the $40 billion Nvidia had offered.",
   ]),
   ("The general point, with a complication", [
    "Where part of an asset's value rests on its independence, selling it to an "
    "interested party reduces the thing being bought. Standards bodies, "
    "marketplaces, benchmarks and ratings all share some of this property, and "
    "it does not appear in a financial model because there is no line for it.",
    "The complication is worth stating. In March 2026 Arm announced a server "
    "processor of its own, which puts it in some tension with licensees "
    "building their own Arm-based chips. The independence that made the Nvidia "
    "sale impossible is a position Arm is now testing itself, and how its "
    "customers respond will say more about the strength of that argument than "
    "the 2022 outcome did.",
   ]),
  ],
  takeaway=("Some assets are worth less once an interested party owns them, "
            "and the reduction does not appear anywhere in the valuation."),
  srcs=["NVIDIA Corporation, SoftBank Group and Arm Limited, announced 13 September 2020, up to $40bn in stock and cash. Terminated 8 February 2022.",
        "SoftBank retained the $1.25bn prepayment, which it recognised in its own results.",
        "Regulatory opposition in the United States, United Kingdom and European Union, and objections from Arm licensees, were reported through 2021.",
        "Arm Holdings plc listed on Nasdaq in September 2023. Arm announced its own server processor in March 2026. Coverage of availability and timing varies, and it is treated here as directional."]),

 dict(slug="the-price-machine", year="2022", roman="VII",
  lead="Broadcom and", line1="VMware", line2="",
  sub="A PURCHASE WHOSE RETURN DOES NOT DEPEND<br>ON THE ACQUIRED BUSINESS GROWING",
  party="Broadcom / VMware", value="$61bn", dated="Announced May 2022",
  lede=("Broadcom agreed to acquire VMware in May 2022 for approximately $61 "
        "billion in cash and stock plus assumed debt. It was announced as "
        "interest rates were rising sharply and completed in November 2023 "
        "after review in several jurisdictions."),
  sections=[
   ("What VMware sells", [
    "VMware's core product allows one physical server to run as several "
    "independent machines. That sounds like a technical detail and it is the "
    "basis on which a great deal of corporate computing has been organised for "
    "two decades.",
    "It sits beneath the applications a company runs rather than beside them. "
    "Replacing it means moving every workload that depends on it, testing each "
    "one, and accepting the risk of the migration. Most organisations conclude "
    "the project would cost more than the licences.",
   ]),
   ("The acquirer's method", [
    "Broadcom's approach is consistent and visible across CA Technologies, "
    "Symantec's enterprise business and now VMware. It acquires established "
    "infrastructure software, reduces research spending and discontinues "
    "smaller product lines, focuses commercial effort on the largest customers, "
    "and raises prices.",
    "The significant feature is that the return does not require the acquired "
    "business to grow. It requires existing customers to stay, which the "
    "previous section explains. That is a calculation a buyer can make with "
    "more confidence than a growth forecast, and it is part of why Broadcom "
    "could proceed while financing conditions deteriorated for others.",
    "After completion, customers reported substantial increases in what they "
    "pay and some moved to alternatives. Both outcomes were anticipated in the "
    "model. The question was always the ratio between them.",
   ]),
   ("What I would hold open", [
    "That the approach is profitable is observable across twenty years of "
    "Broadcom's results, and I would not argue with it.",
    "What is not yet settled is whether it carries a delayed cost. Enterprise "
    "buyers have long memories and considerable discretion about who they "
    "invite to bid next time. Such a cost, if it exists, would not appear in a "
    "quarterly figure. It would appear years later in processes the company is "
    "not part of, and by then it is difficult to attribute.",
   ]),
  ],
  takeaway=("Where customers cannot leave cheaply, a buyer can underwrite price "
            "increases with more confidence than it can underwrite growth."),
  srcs=["Broadcom Inc. and VMware, Inc., announced 26 May 2022, approximately $61bn in cash and stock plus assumed debt. Completed 22 November 2023.",
        "Broadcom's acquisition approach is described from its public record across CA Technologies, Symantec's enterprise business and VMware, and from its own investor materials.",
        "Reported customer pricing increases following completion come from trade coverage and customer accounts rather than from company disclosure."]),

 dict(slug="reading-the-record", year="2023", roman="VIII",
  lead="Cisco and", line1="Splunk", line2="",
  sub="TWO DIFFERENT BUYERS FOR THE SAME DATA,<br>AND A HARDWARE COMPANY SELLING SOFTWARE",
  party="Cisco / Splunk", value="$28bn", dated="Announced September 2023",
  lede=("Cisco agreed to acquire Splunk in September 2023 at $157 a share in "
        "cash, around $28 billion. It was Cisco's largest acquisition, "
        "announced in the weakest year for technology transactions in more than "
        "a decade, and completed in March 2024."),
  sections=[
   ("The product", [
    "Software records what it does. A user signed in. A request failed. A "
    "server restarted at four in the morning. These records are called logs, "
    "and a large organisation produces them in volumes no person could read.",
    "Splunk collected logs from across an organisation's systems and made them "
    "searchable quickly. That is the product.",
   ]),
   ("Who pays for it", [
    "Two groups, for different reasons, which is part of why the business held "
    "up.",
    "Security teams pay because the evidence of an intrusion is distributed "
    "across many systems and the useful question is what happened in sequence. "
    "The category is known as security information and event management.",
    "Engineering teams pay because applications are now assembled from many "
    "separate services, often maintained by different teams, so when something "
    "fails no individual holds the whole picture. Reading the record is the "
    "practical way to find out. That category is called observability.",
    "A product serving two budgets within the same customer is harder to remove "
    "than one serving a single budget, because a cost reduction in one "
    "department does not by itself end the relationship.",
   ]),
   ("The question this raises", [
    "Cisco paid cash at a time when cash was comparatively expensive, which "
    "indicates conviction, and bought when competition for assets was unusually "
    "low, which is a reasonable thing for a buyer to do.",
    "The open issue is execution rather than price. Cisco has sold network "
    "hardware to these customers for decades on a purchasing cycle measured in "
    "years. Selling a software subscription is a different commercial motion "
    "with different staff, different renewal dynamics and different measures. "
    "Hardware companies have attempted this transition before with varied "
    "results, and the outcome here is not yet clear.",
   ]),
  ],
  takeaway=("A product paid for out of two separate budgets inside the same "
            "customer is harder to displace than its category suggests."),
  srcs=["Cisco Systems, Inc. and Splunk Inc., announced 21 September 2023. $157.00 per share in cash, approximately $28bn in equity value. Completed 18 March 2024.",
        "Splunk's position in security information and event management and in observability from the company's filings and category coverage.",
        "2023 as the weakest year for technology deal volumes in over a decade reflects reported league table data, which varies by provider and by sector definition."]),

 dict(slug="third-in-line", year="2025", roman="IX",
  lead="Google and", line1="Wiz", line2="",
  sub="WHAT A SELLER WITH AN ALTERNATIVE IS WORTH,<br>AND WHAT THE FINAL FIGURE TURNED OUT TO BE",
  party="Google / Wiz", value="$32bn announced, ~$29.5bn final", dated="March 2025",
  lede=("Wiz ended acquisition discussions with Google in July 2024 at a "
        "reported $23 billion, citing antitrust and investor concerns and "
        "stating an intention to go public. Eight months later it agreed to "
        "sell to the same buyer for $32 billion. The transaction completed on "
        "11 March 2026, and Alphabet's quarterly filing puts the purchase price "
        "at approximately $29.5 billion after adjustments."),
  sections=[
   ("The product", [
    "When a company runs infrastructure in a cloud provider, it creates "
    "thousands of configuration settings. Which systems can reach which "
    "databases, what is accessible from the open internet, which credentials "
    "carry which permissions.",
    "Wiz examines all of it and reports which combinations create a usable path "
    "for an attacker. Earlier tools in the category produced very long lists of "
    "individual warnings, which teams largely stopped reading. Wiz produced "
    "shorter lists, and could be connected and returning results within hours "
    "rather than over a deployment project. That is most of the reason it grew "
    "quickly.",
   ]),
   ("Why Google was willing to pay", [
    "Google Cloud has been third behind Amazon and Microsoft for a number of "
    "years. A provider in that position rarely wins on price and seldom on "
    "features alone, because what holds a customer in place is the cost of "
    "moving rather than satisfaction.",
    "Wiz works across Amazon, Microsoft and Oracle as well as Google, and "
    "Google committed publicly to keeping it that way. Software used regardless "
    "of which provider a customer chose produces revenue from estates Google "
    "has not won, and puts it in contact with the security teams consulted when "
    "a company considers moving workloads.",
   ]),
   ("What the increase actually bought", [
    "The gap between $23 billion refused and $32 billion agreed is the most "
    "instructive figure here. Wiz's reported annual recurring revenue was above "
    "$500 million in mid-2024, against $350 million a year earlier, and it kept "
    "growing. That growth does not on its own account for the difference.",
    "What Wiz had was a credible alternative. A company able to list publicly "
    "does not have to accept an offer, and a seller with somewhere else to go "
    "negotiates from a materially different position than one without. Deal "
    "terms addressing the regulatory wait are likely to form part of the "
    "explanation as well, and those are not public.",
   ]),
   ("A note on the final figure", [
    "The $32 billion reported at announcement and the approximately $29.5 "
    "billion recorded on completion differ for ordinary reasons, including "
    "adjustments and the treatment of equity awards. The first figure was "
    "reported widely and the second much less so. It is a useful reminder to "
    "check whether a number describes an announcement or a conclusion.",
   ]),
  ],
  takeaway=("A seller able to walk away is in a different negotiation from one "
            "that cannot, and the difference is visible in the price."),
  srcs=["Google and Wiz, Inc., announced 18 March 2025, approximately $32bn in cash. Completed 11 March 2026.",
        "Alphabet Inc. Form 10-Q for the quarter ended 31 March 2026 records a purchase price of approximately $29.5bn after adjustments, with Wiz reported within the Google Cloud segment.",
        "Wiz ended earlier discussions in July 2024 at a reported $23bn, with reported ARR above $500m against $350m a year earlier. Those revenue figures come from trade reporting rather than filings.",
        "Google's commitment to maintaining Wiz across other cloud providers is from the announcement."]),

 dict(slug="fetching", year="2025", roman="X",
  lead="DDN and", line1="Blackstone", line2="",
  sub="WHY A STORAGE SUPPLIER CAN CHARGE WELL<br>FOR WHAT SOUNDS LIKE A COMMODITY",
  party="DDN / Blackstone", value="$300m at a $5bn valuation", dated="January 2025",
  lede=("Blackstone Tactical Opportunities invested $300 million in DataDirect "
        "Networks in January 2025 at a $5 billion valuation. DDN was founded in "
        "1998 and has sold storage into scientific and high performance "
        "computing for most of its history."),
  sections=[
   ("The economics of the product", [
    "A processor working on a large job needs the next portion of data before "
    "it can continue. If the storage system cannot deliver it quickly enough, "
    "the processor waits.",
    "That is the commercial case for this category, and it is worth stating "
    "plainly because the equipment itself sounds unremarkable. An operator with "
    "a facility full of expensive processors is buying storage in order to get "
    "more work out of hardware it has already paid for. The comparison is not "
    "against cheaper storage. It is against idle time on a much larger "
    "investment.",
    "Suppliers whose product governs the productivity of a customer's existing "
    "capital tend to have better pricing than their category implies. That is "
    "true here and it was equally true of the networking business discussed in "
    "the Mellanox note.",
   ]),
   ("The company and the terms", [
    "DDN sold for twenty-seven years into national laboratories, weather "
    "services and genomics institutes. The market was specialised and the "
    "company not widely known outside it.",
    "Blackstone's investment was a minority one at a $5 billion valuation. DDN "
    "said the capital was directed at moving data to processors faster inside "
    "enterprise AI clusters, and that it was working toward a billion dollars "
    "of revenue.",
   ]),
   ("What would have to be true", [
    "A $5 billion valuation on a private company is an expectation rather than "
    "a result. It implies both that enterprise demand for this kind of system "
    "grows substantially and that DDN holds its position as larger storage "
    "vendors and the cloud providers themselves address the same requirement.",
    "The revenue figure DDN described is the checkable part and it has not yet "
    "been reached. I would watch that before concluding anything about the "
    "valuation.",
   ]),
   ("The wider pattern, stated carefully", [
    "Related businesses attracted capital over the same period. Object storage "
    "providers raised money, data protection companies were acquired, and "
    "Seagate raised on terms more commonly offered to growth companies after a "
    "decade in which hard drives were widely expected to be displaced by flash.",
    "The common factor is demand for large and comparatively cheap capacity "
    "alongside the fast storage. I would not describe this as a permanent "
    "change in the industry. Storage is cyclical, current conditions are "
    "unusually favourable, and the previous consensus about hard drives was "
    "also held confidently.",
   ]),
  ],
  takeaway=("The supplier whose product determines how much work a customer "
            "gets from its existing equipment is in a better position than the "
            "word commodity suggests."),
  srcs=["Blackstone, press release, 8 January 2025. $300m investment in DataDirect Networks at a $5bn valuation, via Blackstone Tactical Opportunities.",
        "DDN founding date, customer base and stated revenue ambition from Blackstone, DDN and contemporaneous trade coverage.",
        "Seagate's exchangeable note activity is confirmed in its own filings. Aggregate figures circulating on deal lists did not reconcile against those filings when checked, so this note describes the pattern rather than restating totals."]),
]
