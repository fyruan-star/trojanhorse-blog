"""Deals From Palo Alto: a sub journal to Ten Years.

Three transactions from the BofA Securities Palo Alto software team's list,
told as stories. Each one has the same five questions under it (what the bank
did, why the price, what the company does, whether it holds, who it fights) and
a turn in the first third that asks what the industry stopped optimizing.

Where a public source does not name the adviser, the entry says so and
describes the work in general. No em dashes, no semicolons.
"""

DESK_INTRO = ("Transactions from the Palo Alto software team at BofA Securities, "
              "told as stories. Each one asks the same questions: what the bank "
              "did, why the company is priced as it is, what it actually does, "
              "whether it holds, and who it fights. Where a public source does "
              "not name the adviser, the entry says so.")

DESK = [

 dict(slug="desk-ddn", roman="I",
  lead="DDN takes $300m from", line1="Blackstone", line2="",
  sub="A STORAGE COMPANY THAT STOPPED SELLING CAPACITY<br>AND STARTED SELLING UTILIZATION",
  party="DDN / Blackstone", value="$300m at a $5bn valuation", dated="January 2025",
  lede=("For twenty-six years two founders owned a storage company outright. "
        "Alex Bouzari and Paul Bloch started DDN in 1998, built it into a "
        "profitable business and took no outside money. In January 2025 "
        "Blackstone Tactical Opportunities put in $300 million at a $5 billion "
        "valuation. It was the first outside capital DDN had accepted."),
  sections=[
   ("A company that never needed anyone", [
    "A company that has never needed a bank is the hardest kind to advise. "
    "There is no failing business to repair and no deadline forcing a "
    "decision. The only question is the one founders dislike most, which is "
    "why now, and why this investor.",
   ]),
   ("What the bank did", [
    "Several outlets reported that BofA Securities advised DDN. What follows "
    "describes how an assignment like this generally runs and is not a record "
    "of the room.",
    "The work begins with a story the founders had never needed to tell. "
    "Twenty-six years of quiet, profitable growth has to be turned into a case "
    "an investor can underwrite in a few weeks. Then the bank decides whom to "
    "call. A strategic buyer would want control, and these founders did not "
    "want to sell. A growth fund might want a board seat and a decade-long "
    "hold. A group like Blackstone Tactical Opportunities can write a large "
    "cheque, accept a minority position and move quickly.",
    "The part that decides the outcome is the price and what the founders keep "
    "in exchange for it. Here they kept the company. They sold a slice of a "
    "business they still run. Most of an adviser&rsquo;s work in that "
    "position is translation. Founders talk about customers and product. "
    "Investors talk about growth, margin and what year five looks like. The "
    "bank holds both conversations and makes them meet at a number.",
   ]),
   ("Why $5 billion", [
    "The announcement did not publish a revenue figure. Forbes has reported "
    "roughly $400 million of revenue in 2024, about $500 million in 2025 and a "
    "projection near $1 billion for 2026. Those are reported figures and not "
    "audited ones.",
    "On those numbers $5 billion is about ten times this year&rsquo;s revenue "
    "and about five times next year&rsquo;s if the projection holds. That is a "
    "fair price for a business growing at that pace and an unusual one for "
    "this part of the market, where most companies selling into AI "
    "infrastructure spend more than they earn. DDN has been profitable for "
    "decades.",
    "The rest of the price is proximity. DDN says its systems support more "
    "than 500,000 NVIDIA GPUs, including xAI&rsquo;s Colossus cluster, and "
    "that is a company claim and not a measured market share. A company "
    "sitting next to that much spending gets valued as part of it. Blackstone "
    "already owns data centres through QTS, so a storage business inside the "
    "same flow of capital is a natural second position.",
   ]),
   ("What it does, twice", [
    "In technical terms, DDN builds high-performance parallel storage. Its "
    "systems let thousands of compute nodes read and write the same dataset at "
    "once, using file systems such as Lustre. Its newer Infinia platform is a "
    "software-defined data layer aimed at AI workloads, where the job is "
    "keeping processors fed and organizing the data for training and "
    "inference.",
    "In plain terms, picture a kitchen with a thousand chefs, each costing "
    "tens of thousands of dollars. If the groceries arrive through one narrow "
    "door, most of the chefs stand around. The kitchen is not the problem. The "
    "door is. DDN builds the door.",
   ]),
   ("However", [
    "However, the interesting thing about DDN is what it stopped optimizing.",
    "For forty years the storage industry asked one question, which was how to "
    "hold more bytes more cheaply. Disk gave way to flash and flash got denser. "
    "Every improvement was a faster horse.",
    "Elon Musk&rsquo;s habit of walking into an industry and scratching its "
    "premise is the right lens. Cars did not beat horses by being better "
    "horses, and planes did not beat cars by being better cars. They changed "
    "what the machine was for. AI infrastructure did that to storage. The new "
    "question is not how much it can hold. It is how many dollars of processor "
    "time are idle while it waits for data. Once that is the measure, a "
    "storage company is not selling capacity. It is selling utilization on the "
    "most expensive chips ever built.",
    "There is a small irony in the customer list. The most famous practitioner "
    "of scratching the premise runs a supercomputer on a system built for the "
    "new one. That reframing is also why $300 million at $5 billion is not a "
    "storage multiple. It is priced as a piece of the GPU economy. The shorter "
    "note on this deal, which covers the economics, is "
    "<a href=\"fetching.html\">in the Ten Years series</a>.",
   ]),
   ("Whether it holds", [
    "There are three reasons it might. DDN has decades of profit, so it can "
    "fund its own product cycle, and it now has fresh capital for Infinia. It "
    "has deep roots in high-performance computing, where a storage failure "
    "costs weeks of training and buyers do not switch vendors lightly. And "
    "data has gravity. Once petabytes live in a system, moving them is slow "
    "and risky.",
    "There are three reasons it might not. Customer concentration, because a "
    "few very large AI buyers drive the growth. The GPU spending cycle, "
    "because if it slows storage orders slow with it. And the possibility that "
    "hyperscalers or NVIDIA&rsquo;s own reference designs pull storage in-house "
    "or toward a short list of approved vendors.",
   ]),
   ("Who it fights", [
    "From my own reading and not from the press coverage, the competitors are "
    "VAST Data, which is the most aggressive private rival, along with WEKA, "
    "Pure Storage, NetApp, Dell&rsquo;s PowerScale line, IBM Storage Scale, "
    "HPE&rsquo;s Cray storage line and Hammerspace. DDN&rsquo;s edge is a long "
    "record inside the largest and most demanding clusters.",
   ]),
   ("What the record does not show", [
    "The revenue and ownership figures above come from Forbes by way of "
    "secondary outlets, and I could not open the primary page. BofA&rsquo;s "
    "exact role is reported but not detailed, so the account of the work is "
    "mine.",
   ]),
  ],
  takeaway=("What a storage company is worth depends on how much idle "
            "processor time it removes, and much less on how many bytes it "
            "holds."),
  srcs=["Blackstone, press release, January 2025. $300m investment in DDN at a $5bn valuation, via Blackstone Tactical Opportunities. "
        "<a href=\"https://www.blackstone.com/news/press/blackstone-invests-300-million-at-a-5-billion-valuation-in-ddn-ai-and-data-intelligence-solutions-leader-to-fuel-further-rapid-growth/\">blackstone.com</a>",
        "BusinessWire release of the same announcement, and Pulse 2.0 coverage naming BofA Securities as DDN&rsquo;s adviser. "
        "<a href=\"https://pulse2.com/ddn-ai-and-data-intelligence-solutions-company-raises-300-million-at-5-billion-valuation/amp/\">pulse2.com</a>",
        "Revenue figures for 2024, 2025 and the 2026 projection are from Forbes as relayed by AI Weekly. "
        "<a href=\"https://aiweekly.co/alerts/ddn-projects-revenue-doubling-to-1b-in-2026-on-ai-storage-boom\">aiweekly.co</a>",
        "The GPU count and the xAI customer claim are DDN&rsquo;s own and are not independently verified."]),

 dict(slug="desk-wolfspeed", roman="II",
  lead="Wolfspeed and the", line1="$2bn Deposit", line2="",
  sub="WHAT HAPPENS WHEN A CUSTOMER PREPAYS A SUPPLIER<br>AND THE SUPPLIER CANNOT DELIVER THE FUTURE",
  party="Renesas / Wolfspeed", value="$2.062bn deposit restructured", dated="June 2025",
  lede=("In July 2023 the Japanese chipmaker Renesas gave a supplier $2 billion "
        "in advance. The money was a deposit tied to a ten-year agreement for "
        "silicon carbide wafers, and it later grew to $2.062 billion. By June "
        "2025 the supplier, Wolfspeed, was in Chapter 11, and Renesas was "
        "negotiating to turn the deposit into a piece of the company."),
  sections=[
   ("The prepayment", [
    "The logic was clean. Wolfspeed needed cash to build factories before "
    "demand arrived. Renesas needed guaranteed wafers for its own power chips. "
    "A deposit solved both problems at once. It was a loan dressed as a "
    "purchase order.",
    "Then the demand curve bent. Electric vehicle growth slowed and Wolfspeed"
    "&rsquo;s debt piled up. In May 2025 the company warned of going-concern "
    "doubt and said it might restructure in court. Renesas&rsquo;s deposit was "
    "suddenly the largest claim on a company that might not survive.",
   ]),
   ("What the bank did", [
    "A banker on BofA Securities&rsquo; Palo Alto software team lists this "
    "transaction among their work. Renesas&rsquo;s announcement names no "
    "advisers, so what follows describes this kind of assignment and not the "
    "record of this one.",
    "A customer deposit inside a bankruptcy is an awkward thing. It is not a "
    "bond, not a loan and not equity. Is it a creditor claim, a prepayment for "
    "goods never delivered or something else? An adviser&rsquo;s first job is "
    "to work out what the claim is worth, who stands ahead of and behind it, "
    "and which instruments could hold its value after the company comes out "
    "the other side.",
    "Renesas negotiated a Restructuring Support Agreement with Wolfspeed and "
    "its principal creditors in June 2025. The deposit would convert into "
    "three things. The first was $204 million of convertible notes due 2031. "
    "The second was common stock equal to 38.7 percent of Wolfspeed&rsquo;s "
    "shares at completion, or 17.9 percent fully diluted before warrants. The "
    "third was warrants for another 5 percent fully diluted. If regulatory "
    "approvals ran late, Renesas would hold instruments of equal economic "
    "value until they arrived.",
   ]),
   ("Why this price", [
    "There was no price tag here in the usual sense. The valuation was a "
    "haircut.",
    "Renesas said it expected a loss of roughly 250 billion yen on a deposit of "
    "about 301 billion yen, by its own internal estimate. That implies "
    "recovering about seventeen cents on the dollar through the new "
    "instruments. A number that stark is the market&rsquo;s verdict on a "
    "customer-funded bet that went wrong. The real question was never what "
    "Wolfspeed was worth. It was how much Renesas could take without "
    "destroying a supplier it still needed.",
   ]),
   ("What the companies do, twice", [
    "In technical terms, silicon carbide is a compound semiconductor. Power "
    "chips made from it switch higher voltages at higher temperatures and "
    "waste much less energy as heat than silicon chips do. That matters in an "
    "electric vehicle inverter, which turns battery power into motor power, "
    "and in solar and grid equipment. The material is hard to make. The "
    "crystals grow slowly in furnaces above 2,000 degrees Celsius and the "
    "finished wafers are close to diamond in hardness. Wolfspeed, formerly "
    "Cree, grew these crystals and built the Mohawk Valley fab in New York, "
    "which it describes as the first 200mm silicon carbide fab.",
    "In plain terms, power chips are the valves that control electricity. "
    "Silicon valves leak some energy as heat and silicon carbide valves leak "
    "far less. Wolfspeed makes the plate the valves are cut from. Renesas "
    "turns the plates into valves.",
   ]),
   ("However", [
    "However, this story starts with a premise somebody scratched.",
    "For sixty years power electronics improved silicon, with smaller "
    "transistors, cleaner processes and better packaging. That was a faster "
    "horse. Silicon carbide asked a different question. Instead of shrinking "
    "the same material, change the material. The physics of the new one "
    "supports higher voltages and temperatures in the same space, and that "
    "opened a different product, an electric car that goes further on the "
    "same battery.",
    "Elon Musk&rsquo;s approach to the car is the comparison. Do not ask how to "
    "make the combustion engine better. Ask what the vehicle looks like if the "
    "engine is not the starting point. Silicon carbide is that logic applied "
    "to the chip inside the car.",
    "The same idea has a cost. A new material does not only replace a part. It "
    "changes who has to spend first. Silicon carbide needed whole new "
    "factories before the cars that used it were selling in volume, so the "
    "people building the future ended up pre-funding it. Renesas&rsquo;s "
    "deposit was a customer paying for the new horse to be born. When the "
    "timing slipped, the customer took the loss.",
   ]),
   ("Whether it holds", [
    "The plan of reorganization became effective on 29 September 2025. One "
    "condition remained, which was regulatory clearance. On 30 January 2026 "
    "Wolfspeed announced the final step, the issue of about 16.9 million "
    "shares to Renesas in a company of roughly 45 million shares, and Renesas "
    "took a board seat. The largest customer is now also a shareholder, and "
    "that aligns the two of them.",
    "Long-term demand for silicon carbide is not really in doubt. Electric "
    "vehicles, charging and grid equipment need it, and a 200mm fab is a "
    "scarce asset. The risks are those that caused the filing in the first "
    "place. Vehicle demand swings quickly and capacity was built ahead of it. "
    "Chinese wafer makers are pushing prices down. A fab running below "
    "capacity loses money.",
   ]),
   ("Who they fight", [
    "From my own reading, in silicon carbide the competitors are Infineon, "
    "STMicroelectronics, onsemi, ROHM, Coherent in wafers and a fast-growing "
    "group of Chinese suppliers. Renesas competes in power and automotive "
    "chips with Infineon, STMicroelectronics, NXP and Texas Instruments.",
   ]),
   ("What the record does not show", [
    "I found no public source tying BofA to a particular side of this "
    "transaction. The profile abbreviates the deposit as a CRD and I treated "
    "that as the customer deposit without confirming the term. The loss "
    "figure is Renesas&rsquo;s own estimate from June 2025 and the final "
    "accounting may differ.",
   ]),
  ],
  takeaway=("A customer who prepays a supplier has become a lender without "
            "the protections a lender would have asked for."),
  srcs=["Renesas, announcement of the Restructuring Support Agreement with Wolfspeed, June 2025. Deposit history, conversion terms and expected loss. "
        "<a href=\"https://www.renesas.com/en/about/newsroom/renesas-announces-expected-loss-resulting-signing-restructuring-support-agreement-wolfspeed\">renesas.com</a>",
        "Wolfspeed and Renesas, ten-year silicon carbide wafer supply agreement, July 2023. "
        "<a href=\"https://www.wolfspeed.com/company/news-events/news/renesas-wolfspeed-10-year-wafer-supply-agreement\">wolfspeed.com</a>",
        "Wolfspeed, CFIUS clearance and completion of the equity issuance to Renesas, 30 January 2026, which also records the 29 September 2025 effective date. "
        "<a href=\"https://investor.wolfspeed.com/news/news-details/2026/Wolfspeed-Announces-CFIUS-Clearance-and-Completion-of-Equity-Issuance-to-Renesas-as-Part-of-Court-Approved-Restructuring/default.aspx\">investor.wolfspeed.com</a>",
        "Competitor lists are the author&rsquo;s own knowledge and not from the filings."]),

 dict(slug="desk-wasabi", roman="III",
  lead="Wasabi and the", line1="Exit Fee", line2="",
  sub="A STORAGE VENDOR THAT COMPETED ON THE METER<br>RATHER THAN THE PRICE PER TERABYTE",
  party="Wasabi", value="$70m at about $1.8bn", dated="January 2026",
  lede=("In January 2026 Wasabi Technologies announced a $70 million equity "
        "round led by L2 Point Management, with Pure Storage and existing "
        "investors including Fidelity taking part. The round valued the company "
        "at about $1.8 billion and brought its total funding past $600 million."),
  sections=[
   ("The bill", [
    "Every company that stores data in the cloud eventually meets the same "
    "surprise. Putting data in is cheap. Taking it out is not. Cloud providers "
    "charge for egress, which is the cost of moving your own data out of their "
    "system, and they also charge for the requests you make along the way. "
    "Storage looks cheap until you try to use it or leave.",
    "David Friend and Jeff Flowers knew that bill well. They had co-founded "
    "Carbonite, the online backup company, and paid cloud storage fees for "
    "years. In 2015 they started Wasabi on a simple claim, which was that the "
    "pricing model is the problem.",
   ]),
   ("What the bank did", [
    "A banker on BofA Securities&rsquo; Palo Alto software team lists a $70 "
    "million Series D1 for Wasabi among their transactions. I could not find "
    "that label in public coverage, which calls the January 2026 round an "
    "equity round. Foley &amp; Lardner is named as Wasabi&rsquo;s legal "
    "adviser and I found no public source naming BofA, so what follows "
    "describes the typical work.",
    "A follow-on round for a private infrastructure company is a positioning "
    "exercise. By then Wasabi had a record, including a $250 million package "
    "in 2022 made of about $125 million of Series D equity and a debt "
    "facility, which Barclays placed. The adviser&rsquo;s task is to answer "
    "one question for investors, which is what is different now. In 2026 the "
    "answer was AI. Data lakes, training sets and model checkpoints all need "
    "somewhere cheap and always available to live, and nobody wants an exit "
    "fee on a petabyte.",
    "The adviser also shapes who is in the room. L2 Point led this round as it "
    "did in 2022. A strategic investor like Pure Storage tells the market that "
    "this is not only a financial bet.",
   ]),
   ("Why $1.8 billion", [
    "I could not find Wasabi&rsquo;s revenue in the sources I checked, so I "
    "will not offer a multiple. The case for the price is structural.",
    "Storage is sticky, because data does not move casually, so revenue "
    "compounds. The pricing is flat and simple, which shortens sales cycles. AI "
    "workloads are raising demand for cheap, always-available data. A "
    "strategic investor in the round gives the valuation a second source of "
    "support beyond the financial funds.",
   ]),
   ("What it does, twice", [
    "In technical terms, Wasabi sells S3-compatible object storage, which "
    "means software written for Amazon&rsquo;s storage works with Wasabi "
    "unchanged. It is hot storage. Every object is available at the same "
    "speed, with no cold archive tier to wait on. Pricing is a flat rate per "
    "terabyte per month with no egress fees and no per-request fees.",
    "In plain terms, imagine a storage unit that charges only for the space "
    "and never for opening the door or taking your things out. Every other "
    "unit charges each time you open it.",
   ]),
   ("However", [
    "However, the industry spent a decade competing on the wrong number.",
    "Amazon, Microsoft and Google each tried to win storage by lowering the "
    "price per gigabyte and then adding tiers, discounts and special classes "
    "to optimize the bill. Every improvement worked inside the same model, "
    "which was cheap to store and costly to move. It was a faster horse.",
    "The Musk move is to scratch the premise. Cars did not win by being a "
    "better horse. Wasabi did not try to be a cheaper S3. It asked what "
    "storage looks like if the meter on leaving does not exist. Remove egress "
    "fees and the product becomes something else, a place data can live "
    "without a toll, and a promise the incumbents&rsquo; own business models "
    "make hard to match.",
    "That is the Trojan Horse in this deal. It looks like a cheaper storage "
    "vendor. It is actually an attack on the way the incumbents make money, "
    "because the egress fee is a lock-in tool as much as a revenue line. "
    "Wasabi walked it in as a pricing difference, and the real change was to "
    "the customer&rsquo;s freedom to leave.",
   ]),
   ("Whether it holds", [
    "The hardest test is that a horse can be copied. Google announced in "
    "January 2024 that it would waive data transfer fees for customers "
    "leaving its cloud, AWS followed in March, and Microsoft after that. "
    "Reporting links all three moves to new European Union rules. The waivers "
    "come with conditions, since they apply to customers who leave entirely "
    "and not to those who stay, so the advantage is narrower and not gone. "
    "What remains is the price, the simplicity and the focus. Those are real, "
    "but they are less structural than a gap in how the business model works.",
    "In its favor are predictable pricing that buyers like, S3 compatibility "
    "that makes switching in easy, a strategic backer in Pure Storage and "
    "demand from AI. Against it, the hyperscalers can cut prices and have far "
    "deeper pockets, storage is a scale business that favors the giants, and "
    "pure-play storage vendors have historically earned thin margins.",
   ]),
   ("Who it fights", [
    "From my own reading, AWS S3, Microsoft Azure Blob Storage and Google "
    "Cloud Storage, along with Backblaze B2, Cloudflare R2 and the "
    "object-storage lines of Dell, NetApp and Pure Storage.",
   ]),
   ("What the record does not show", [
    "BofA&rsquo;s role, the Series D1 label and Wasabi&rsquo;s revenue are "
    "all absent from the public sources I found. The company is reported to "
    "have secured a $250 million credit facility in April 2026, which I have "
    "not tied to this round.",
   ]),
  ],
  takeaway=("Competing on a rival&rsquo;s pricing model works until the rival "
            "changes it, and then what is left is everything else."),
  srcs=["Foley &amp; Lardner, note on advising Wasabi on its $70m equity round, January 2026. "
        "<a href=\"https://www.foley.com/news/2026/01/foley-guides-wasabi-technologies-in-70m-equity-funding-round/\">foley.com</a>",
        "Wasabi, $250m in new funding announcement, September 2022, which names Barclays as sole placement agent. "
        "<a href=\"https://www.businesswire.com/news/home/20220927005211/en/Wasabi-Technologies-Closes-%24250-Million-in-New-Funding-to-Usher-In-the-Future-of-Cloud-Storage\">businesswire.com</a>",
        "Founders, founding date and product from Wikipedia&rsquo;s entry on Wasabi. "
        "<a href=\"https://en.wikipedia.org/wiki/Wasabi_Technologies\">wikipedia.org</a>",
        "Egress waivers by Google, AWS and Microsoft, 2024, as reported by The Register, Light Reading and Petri. "
        "<a href=\"https://www.theregister.com/2024/01/11/google_cloud_egress_fees/\">theregister.com</a>",
        "Competitor lists are the author&rsquo;s own knowledge and not from the filings."]),
]
