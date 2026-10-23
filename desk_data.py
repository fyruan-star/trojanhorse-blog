"""Deals From Palo Alto: a sub journal to Ten Years.

Three transactions from the BofA Securities Palo Alto software team's list.
Each is an argument with a thesis, the view it challenges, the evidence and the
strongest objection. Where a public source does not name the adviser, the
entry says so and describes what the work involves in general terms.

No em dashes, no semicolons.
"""

DESK_INTRO = ("Three transactions from the BofA Securities Palo Alto software "
              "team's list, each examined as a case. Each states a thesis, "
              "gives the view it challenges and links its sources. Where a "
              "public source does not name the adviser, the entry says so.")

DESK = [

 dict(slug="desk-ddn", roman="I",
  lead="DDN takes $300m from", line1="Blackstone", line2="",
  sub="A founder-owned company sold about six percent of itself",
  party="DDN / Blackstone", value="$300m at a $5bn valuation", dated="January 2025",
  lede=("For twenty-six years two founders owned DDN outright. Alex Bouzari "
        "and Paul Bloch started the storage company in 1998 and built it into a "
        "profitable business without outside money. In January 2025 "
        "Blackstone Tactical Opportunities invested $300 million at a $5 "
        "billion valuation, the first outside capital DDN had accepted. I "
        "think a deal of this kind should be read as a decision about price "
        "and control and not mainly as a decision about funding, and that "
        "BofA Securities, which was reported to be DDN's exclusive adviser, "
        "was solving a problem the founders had not faced before."),
  sections=[
   ("The usual reading", [
    "A capital raise is normally read as a company getting money it needs to "
    "grow. DDN's announcement framed it that way. The release said the "
    "investment would “help fund DDN's continued rapid growth,” and "
    "Bouzari said that “Blackstone's support accelerates our mission to "
    "redefine the enterprise AI infrastructure category” "
    "(<a href=\"https://pulse2.com/ddn-ai-and-data-intelligence-solutions-company-raises-300-million-at-5-billion-valuation/amp/\">Pulse 2.0, reproducing the release</a>).",
    "That reading is incomplete for this company. DDN had been profitable for "
    "decades and had never needed outside capital, and $300 million at a $5 "
    "billion valuation is at most about six percent of the company. The "
    "founders sold a small slice and kept control.",
   ]),
   ("What the bank was reported to do", [
    "BofA Securities was named in the announcement as DDN's exclusive "
    "financial adviser, and the release names no adviser for Blackstone. The "
    "public record shows nothing further, so what follows is what the "
    "assignment involves in general terms and not a description of this "
    "one.",
    "A founder-owned company that has never sold equity has no price to "
    "anchor a negotiation. The adviser's work is to establish one, by "
    "turning twenty-six years of quiet, profitable growth into a case an "
    "investor can underwrite in a few weeks, deciding which investors to "
    "approach, and negotiating what the founders keep. A strategic buyer "
    "would want control, and the founders did not want to sell. A growth "
    "fund might want a board seat and a ten-year hold. A group that can write "
    "a large check, accept a minority position and move quickly was a "
    "workable match, and Blackstone's Jas Khaira said, “We are thrilled to "
    "be the first institutional investor in DDN.”",
   ]),
   ("Why $5 billion", [
    "The announcement gave no revenue figure. Forbes has reported revenue of "
    "roughly $400 million in 2024, about $500 million in 2025 and a "
    "projection near $1 billion for 2026 "
    "(<a href=\"https://aiweekly.co/alerts/ddn-projects-revenue-doubling-to-1b-in-2026-on-ai-storage-boom\">AI Weekly</a>), "
    "figures that are not audited. On those numbers $5 billion is about ten "
    "times 2025 revenue and five times the 2026 projection, which is a "
    "premium price for a business growing that quickly and an unusual one "
    "for this part of the market, where most companies selling into AI "
    "infrastructure spend more than they earn.",
    "The rest of the price reflects proximity to the scarce input. DDN says "
    "its systems support more than 500,000 NVIDIA GPUs, including xAI's "
    "Colossus cluster. That is a company claim and not a measured market "
    "share. The economics behind the price are in the "
    "<a href=\"fetching.html\">note on this deal in Ten Years</a>. In short, a "
    "storage supplier whose product keeps very expensive processors working "
    "can be priced against the cost of those processors.",
   ]),
   ("What I infer", [
    "The investment's main product may be the price itself. A $5 billion "
    "valuation set by a major investor gives DDN a reference point for "
    "hiring, for negotiating with customers and for any later financing or "
    "listing. I infer this from the structure, since a company that "
    "needed no money took a small amount at a high price, and no source "
    "states it as the purpose.",
   ]),
   ("The strongest objection", [
    "The objection is that the founders did want the money. Building a new "
    "product platform called Infinia and supplying clusters of this size is "
    "capital intensive, and a profitable company can still choose to raise "
    "capital to grow faster. The stated use of proceeds supports that.",
    "The two readings predict different behavior. If the capital was needed, "
    "DDN should raise more or deploy it visibly in capacity and product "
    "within a year or two. If the price was the aim, the next evidence would "
    "be a further financing or a listing at a higher valuation, with the "
    "$300 million largely unspent.",
   ]),
   ("Competition and durability", [
    "From my own reading and not from the announcement, DDN's competitors "
    "include VAST Data, the most aggressive private rival, along with WEKA, "
    "Pure Storage, NetApp, Dell's PowerScale line, IBM Storage Scale, HPE's "
    "Cray storage line and Hammerspace. DDN's edge is a long record inside "
    "the largest and most demanding clusters, where a storage failure costs "
    "weeks of training and buyers do not switch vendors lightly.",
    "Three risks bear on whether the valuation holds. A few very large AI "
    "buyers drive much of the growth, so customer concentration is high. The "
    "GPU spending cycle can slow, and storage orders slow with it. And "
    "hyperscalers or NVIDIA's own reference designs could pull storage "
    "in-house or toward a short list of approved vendors. DDN's decades of "
    "profit mean it can fund its own product cycle through a slowdown, which "
    "most of its younger rivals cannot.",
   ]),
   ("What a reader should take from it", [
    "When a founder-owned company takes a small minority investment at a high "
    "valuation, ask what the investment gives the company other than money. "
    "The adviser's role in establishing the price is part of what was "
    "bought.",
   ]),
  ],
  takeaway="",
  srcs=["Blackstone, press release, January 2025. $300m investment in DDN at a $5bn valuation, via Blackstone Tactical Opportunities, with the statements by Alex Bouzari and Jas Khaira and the naming of BofA Securities as DDN's exclusive financial adviser, as reproduced by "
        "<a href=\"https://pulse2.com/ddn-ai-and-data-intelligence-solutions-company-raises-300-million-at-5-billion-valuation/amp/\">Pulse 2.0</a>.",
        "Revenue figures for 2024, 2025 and the 2026 projection are from Forbes as relayed by "
        "<a href=\"https://aiweekly.co/alerts/ddn-projects-revenue-doubling-to-1b-in-2026-on-ai-storage-boom\">AI Weekly</a>.",
        "The GPU count and the xAI customer claim are DDN's own and are not independently verified. The description of what an adviser does is general and not specific to this transaction."]),

 dict(slug="desk-wolfspeed", roman="II",
  lead="Wolfspeed and the", line1="$2bn Deposit", line2="",
  sub="A customer's prepayment is a loan without a lender's protections",
  party="Renesas / Wolfspeed", value="$2.062bn deposit restructured", dated="June 2025",
  lede=("In July 2023 the Japanese chipmaker Renesas gave Wolfspeed $2 billion "
        "in advance, under a ten-year agreement for silicon carbide wafers. By "
        "June 2025 Wolfspeed was in Chapter 11 and Renesas was converting the "
        "deposit, by then $2.062 billion, into a stake in the company. I think "
        "a prepayment of that size is a loan, and that Renesas carried a "
        "lender's risk without a lender's protections."),
  sections=[
   ("How the arrangement was described", [
    "The 2023 agreement was presented as securing supply. Renesas needed "
    "guaranteed wafers for its own power chips, and Wolfspeed needed cash to "
    "build factories before demand arrived. The deposit solved both problems, "
    "and Renesas described it as support for Wolfspeed's capacity expansion "
    "(<a href=\"https://www.wolfspeed.com/company/news-events/news/renesas-wolfspeed-10-year-wafer-supply-agreement\">Wolfspeed</a>). "
    "On that reading the deposit was a purchase order paid early.",
   ]),
   ("Why it was closer to a loan", [
    "A deposit of $2 billion, against a supplier that was spending heavily and "
    "borrowing, has the economics of a loan. The money went to the supplier "
    "up front, repayment depended on the supplier's later performance, and "
    "the customer's remedy if the supplier failed was a claim in bankruptcy. "
    "A lender would normally have taken security, set covenants and ranked "
    "ahead of the supplier's owners. A customer holding a deposit usually has "
    "none of those.",
    "The test came when demand slowed. Electric vehicle growth eased, "
    "Wolfspeed's debt grew and in May 2025 the company warned of going-concern "
    "doubt and said it might restructure in court. Renesas then negotiated a "
    "Restructuring Support Agreement with Wolfspeed and its principal "
    "creditors in June 2025.",
   ]),
   ("What the conversion shows", [
    "Under the agreement Renesas converted the $2.062 billion deposit into "
    "$204 million of convertible notes due 2031, common stock equal to 38.7 "
    "percent of Wolfspeed's shares at completion, which is 17.9 percent fully "
    "diluted before warrants, and warrants for 5 percent more on a fully "
    "diluted basis. Renesas said it expected a loss of roughly 250 billion "
    "yen on a deposit of about 301 billion yen, by its own estimate "
    "(<a href=\"https://www.renesas.com/en/about/newsroom/renesas-announces-expected-loss-resulting-signing-restructuring-support-agreement-wolfspeed\">Renesas announcement</a>). "
    "That implies recovering about seventeen cents on the dollar.",
    "The plan became effective on 29 September 2025, with one regulatory "
    "condition outstanding. On 30 January 2026 Wolfspeed announced that the "
    "final clearance had been received and that it had issued about 16.9 "
    "million shares to Renesas, in a company of roughly 45 million shares. "
    "Renesas took a board seat "
    "(<a href=\"https://investor.wolfspeed.com/news/news-details/2026/Wolfspeed-Announces-CFIUS-Clearance-and-Completion-of-Equity-Issuance-to-Renesas-as-Part-of-Court-Approved-Restructuring/default.aspx\">Wolfspeed</a>). "
    "The largest customer is now also a shareholder, which aligns its "
    "interests with the supplier's and also ties more of its risk to it.",
   ]),
   ("What the companies do", [
    "Silicon carbide is a compound semiconductor. Power chips made from it "
    "switch higher voltages at higher temperatures and waste less energy as "
    "heat than silicon chips, which matters in an electric vehicle inverter, "
    "where battery power is converted to motor power, and in solar and grid "
    "equipment. The material is difficult to make. The crystals grow slowly "
    "in furnaces above 2,000 degrees Celsius and the finished wafers are "
    "close to diamond in hardness. Wolfspeed, formerly Cree, grew these "
    "crystals and built the Mohawk Valley fab in New York, which it describes "
    "as the first 200mm silicon carbide fab. Renesas turns the wafers into "
    "power chips.",
    "The case also shows why a customer would take the risk. A new material "
    "needs factories before the products that use it are selling in volume, "
    "so whoever depends on the supply may have to help pay for the capacity. "
    "Silicon carbide was a change in what power chips are made of and not an "
    "improvement to silicon, and that change moved the cost of building "
    "forward onto the customers.",
   ]),
   ("Competition", [
    "From my own reading, in silicon carbide Wolfspeed competes with "
    "Infineon, STMicroelectronics, onsemi, ROHM, Coherent in wafers and a "
    "fast-growing group of Chinese suppliers that are pushing prices down. "
    "Renesas competes in power and automotive chips with Infineon, "
    "STMicroelectronics, NXP and Texas Instruments. Wolfspeed's survival "
    "after the filing depends on whether a 200mm fab can run at enough of "
    "its capacity to cover its costs, because vehicle demand swings quickly "
    "and a plant running below capacity loses money.",
   ]),
   ("The strongest objection", [
    "The objection is that a prepayment secured something a loan could not, "
    "which was the supply itself. Renesas received wafers it could not "
    "otherwise get during the period when they were scarce, and a loss on "
    "the deposit does not mean the arrangement was unwise.",
    "That depends on how many wafers were delivered against the deposit, "
    "which the announcements do not state. The evidence that would decide "
    "the question is the quantity and price of wafers Renesas received "
    "relative to the cost of buying them in the open market. If it received "
    "substantial supply at a discount, the loss was partly the price of "
    "that supply.",
   ]),
   ("What a reader should take from it", [
    "When a customer prepays a supplier, treat the deposit as credit "
    "exposure and ask what protection the customer holds. The announcements "
    "name no advisers on this transaction. A BofA Securities banker lists it "
    "among their work, and what a bank does in a conversion of this kind is "
    "to work out what the claim is worth and which instruments can hold that "
    "value after the company emerges.",
   ]),
  ],
  takeaway="",
  srcs=["Renesas, announcement of the Restructuring Support Agreement with Wolfspeed, June 2025. Deposit history, conversion terms and expected loss. "
        "<a href=\"https://www.renesas.com/en/about/newsroom/renesas-announces-expected-loss-resulting-signing-restructuring-support-agreement-wolfspeed\">renesas.com</a>",
        "Wolfspeed and Renesas, ten-year silicon carbide wafer supply agreement, July 2023. "
        "<a href=\"https://www.wolfspeed.com/company/news-events/news/renesas-wolfspeed-10-year-wafer-supply-agreement\">wolfspeed.com</a>",
        "Wolfspeed, CFIUS clearance and completion of the equity issuance to Renesas, 30 January 2026, which records the 29 September 2025 effective date. "
        "<a href=\"https://investor.wolfspeed.com/news/news-details/2026/Wolfspeed-Announces-CFIUS-Clearance-and-Completion-of-Equity-Issuance-to-Renesas-as-Part-of-Court-Approved-Restructuring/default.aspx\">investor.wolfspeed.com</a>",
        "The loss figure is Renesas's own estimate from June 2025 and the final accounting may differ. The description of what a bank does in a conversion is general. Wolfspeed describes the Mohawk Valley fab as the first of its kind at 200mm."]),

 dict(slug="desk-wasabi", roman="III",
  lead="Wasabi and the", line1="Exit Fee", line2="",
  sub="A storage vendor that competed on the pricing model",
  party="Wasabi", value="$70m at about $1.8bn", dated="January 2026",
  lede=("In January 2026 Wasabi Technologies announced a $70 million equity "
        "round led by L2 Point Management, with Pure Storage and existing "
        "investors including Fidelity taking part. The round valued the company "
        "at about $1.8 billion and brought its total funding past $600 million. "
        "I think Wasabi's position rests on its pricing model more than on "
        "the price per terabyte, and that the large cloud providers' 2024 "
        "waivers of exit fees narrowed that position without removing it."),
  sections=[
   ("The usual way to compete in storage", [
    "Cloud storage is usually sold on the price per gigabyte, and the large "
    "providers have cut it repeatedly while adding tiers, discounts and "
    "special classes to optimize a customer's bill. Putting data in is cheap. "
    "Taking it out is not. Providers charge for egress, the cost of moving a "
    "customer's own data out of their system, and for the requests made "
    "along the way.",
   ]),
   ("What Wasabi did differently", [
    "David Friend and Jeff Flowers founded Wasabi in 2015. They had "
    "co-founded the online backup company Carbonite and had paid cloud "
    "storage fees for years "
    "(<a href=\"https://en.wikipedia.org/wiki/Wasabi_Technologies\">Wikipedia</a>). "
    "Wasabi sells S3-compatible object storage, which means software "
    "written for Amazon's storage works with Wasabi unchanged. It is hot "
    "storage, with every object available at the same speed and no cold "
    "archive tier to wait on. Its price is a flat rate per terabyte per "
    "month with no egress fees and no per-request fees.",
    "A storage unit that charged only for the space, and never for opening "
    "the door or taking things out, would be a different kind of product from "
    "one that charged for each access. Competing on the exit fee changes what "
    "the customer is buying, because the fee was also a way of keeping "
    "customers in place. A vendor built without it gives up that source of "
    "lock-in and sells the customer's freedom to leave.",
   ]),
   ("The adviser", [
    "A BofA Securities banker lists a $70 million Series D1 for Wasabi among "
    "their transactions. Public coverage calls the January 2026 round an "
    "equity round, I found no source using the D1 label, and the sources "
    "name Foley &amp; Lardner as Wasabi's legal adviser and no bank "
    "(<a href=\"https://www.foley.com/news/2026/01/foley-guides-wasabi-technologies-in-70m-equity-funding-round/\">Foley</a>). "
    "For the 2022 round of $250 million, which combined about $125 million of "
    "Series D equity with a debt facility, Barclays was the sole placement "
    "agent "
    "(<a href=\"https://www.businesswire.com/news/home/20220927005211/en/Wasabi-Technologies-Closes-%24250-Million-in-New-Funding-to-Usher-In-the-Future-of-Cloud-Storage\">BusinessWire</a>).",
    "What an adviser does in a follow-on round like this is position the "
    "company for investors by answering what has changed since the last one. "
    "In 2026 the available answer was AI, since data lakes, training sets and "
    "model checkpoints need somewhere cheap and always available to live, and "
    "nobody wants an exit fee on a petabyte. L2 Point led both rounds, and "
    "Pure Storage, a flash storage vendor, taking part signals that the "
    "backing is strategic as well as financial.",
   ]),
   ("Why $1.8 billion", [
    "I could not find Wasabi's revenue in the sources I checked, so I will "
    "not offer a multiple. The case for the price rests on how the business "
    "works. Storage is sticky, because data does not move casually, so "
    "revenue compounds. The flat pricing shortens sales cycles. AI workloads "
    "increase demand for cheap, always-available data, and a strategic "
    "investor in the round gives the valuation support beyond the financial "
    "funds.",
   ]),
   ("How the incumbents responded", [
    "Google announced in January 2024 that it would waive data transfer fees "
    "for customers leaving its cloud, AWS followed in March, and Microsoft "
    "after that. Reporting links all three moves to new European Union "
    "rules, and the waivers carry conditions. They apply to customers who "
    "leave entirely and not to those who stay "
    "(<a href=\"https://www.theregister.com/2024/01/11/google_cloud_egress_fees/\">The Register</a>, "
    "<a href=\"https://www.lightreading.com/cloud/aws-follows-google-cloud-in-ending-cloud-switching-costs\">Light Reading</a>).",
    "So the advantage is narrower and not gone. A customer who keeps data on "
    "Amazon's cloud and uses it actively still pays to move it. What "
    "remains for Wasabi is the price, the simplicity and its focus, which are "
    "real but less structural than a gap in how the business model works.",
   ]),
   ("Competition", [
    "From my own reading, Wasabi competes with AWS S3, Microsoft Azure Blob "
    "Storage and Google Cloud Storage, along with Backblaze B2, Cloudflare R2 "
    "and the object-storage lines of Dell, NetApp and Pure Storage.",
   ]),
   ("The strongest objection", [
    "The objection is that storage is a scale business and the hyperscalers "
    "have far more scale. They can cut prices below what a smaller vendor can "
    "sustain, and pure-play storage vendors have historically earned thin "
    "margins. On that view the $1.8 billion rewards a position that the "
    "incumbents can eventually erode.",
    "The evidence that would decide it is Wasabi's price and growth relative "
    "to the large providers over the next several quarters, and whether "
    "customers that stayed on Amazon despite the waivers still pay to move "
    "data to a cheaper store. The record I found does not yet answer either.",
   ]),
   ("What a reader should take from it", [
    "When a vendor competes on its pricing model, check whether the "
    "incumbents' own policies make the model costly to copy, because that "
    "determines how long the advantage lasts. The adviser, the round label "
    "and the revenue are not established by the sources I found.",
   ]),
  ],
  takeaway="",
  srcs=["Foley &amp; Lardner, note on advising Wasabi on its $70m equity round, January 2026. "
        "<a href=\"https://www.foley.com/news/2026/01/foley-guides-wasabi-technologies-in-70m-equity-funding-round/\">foley.com</a>",
        "Wasabi, $250m in new funding announcement, September 2022, which names Barclays as sole placement agent. "
        "<a href=\"https://www.businesswire.com/news/home/20220927005211/en/Wasabi-Technologies-Closes-%24250-Million-in-New-Funding-to-Usher-In-the-Future-of-Cloud-Storage\">businesswire.com</a>",
        "Founders, founding date and product from Wikipedia's entry on Wasabi. "
        "<a href=\"https://en.wikipedia.org/wiki/Wasabi_Technologies\">wikipedia.org</a>",
        "Egress waivers by Google, AWS and Microsoft, 2024. "
        "<a href=\"https://www.theregister.com/2024/01/11/google_cloud_egress_fees/\">The Register</a>, "
        "<a href=\"https://www.lightreading.com/cloud/aws-follows-google-cloud-in-ending-cloud-switching-costs\">Light Reading</a>. "
        "Competitor lists and the description of Pure Storage are the author's own knowledge."]),
]
