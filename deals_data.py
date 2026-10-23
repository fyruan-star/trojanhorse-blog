"""Ten notes on transactions from the Ten Years timeline.

Each note is an argument. It states the thesis first, gives the interpretation
it disagrees with and whose it is, builds the case in order, answers the
strongest objection and ends with what a reader should do differently.
Quotations are short, attributed and linked to a primary document where one is
available. Where a figure comes from press reporting and not a filing, the text
says so.

No em dashes, no semicolons.
"""

DEALS = [

 dict(slug="the-blueprint", year="2016", roman="I",
  lead="SoftBank and", line1="Arm", line2="",
  sub="A royalty business that did not depend on its end market",
  party="SoftBank / Arm", value="$32bn, announced", dated="July 2016",
  lede=("SoftBank agreed in July 2016 to buy Arm Holdings for about GBP 24.3 "
        "billion, roughly $32 billion, at 1,700 pence a share in cash, a "
        "premium of about 43 percent. I think the price is explained by how Arm "
        "earns money and not by the smartphone market it then served. Arm "
        "collects a royalty on every chip built on its designs, and the cost to "
        "its customers of leaving that arrangement is high enough that the "
        "royalty follows the design into whatever market adopts it next."),
  sections=[
   ("The explanations offered at the time", [
    "SoftBank gave a growth explanation. Its chief executive, Masayoshi Son, "
    "said that “ARM will be an excellent strategic fit within the SoftBank "
    "group as we invest to capture the very significant opportunities provided "
    "by the ‘Internet of Things’” "
    "(<a href=\"https://electronicdesign.com/technologies/test-measurement/article/21206621/softbank-reaches-agreement-to-acquire-arm\">SoftBank announcement</a>).",
    "Investors did not object to the strategy so much as to the buyer's "
    "position. SoftBank's shares fell about 10 percent in Tokyo on the first "
    "trading day, and fund manager Mitsushige Akino said that “a fresh "
    "acquisition is not what the market wants from SoftBank,” which was still "
    "carrying a large debt load "
    "(<a href=\"https://www.fierce-network.com/wireless/softbank-s-son-challenges-investors-as-shares-slide-following-news-arm-deal\">Fierce Network, citing Reuters</a>). "
    "Both views treat the price as a bet on how fast Arm's markets would grow.",
   ]),
   ("How Arm earns money", [
    "Arm designs the instruction set a processor is built around, which is the "
    "basic vocabulary the chip understands, together with reference designs for "
    "the processor cores. It licenses both. A licensee such as Apple or "
    "Qualcomm pays an upfront fee for access, then a royalty on each chip it "
    "ships. The royalty is a few cents a chip, and the industry was shipping "
    "more than fifteen billion Arm-based chips a year at the time of the "
    "acquisition.",
    "Two features make that income durable. Software compiled for one "
    "instruction set does not run on another until it is rebuilt and retested, "
    "so every licensee and every customer of a licensee carries a cost to "
    "moving away. And Arm does not manufacture chips, so it does not compete "
    "with the companies licensing from it. That mattered to licensees who "
    "competed fiercely with one another and were willing to share a common "
    "foundation only because its owner had no product of its own to favor.",
    "Both features describe the licensing position and neither depends on "
    "smartphones. Consider a hypothetical licensee building a processor for a "
    "server. If it starts from an Arm design, its operating system, compilers "
    "and customer software all already exist. Choosing something else means "
    "paying for all of that again, so Arm's royalty follows the design into "
    "the new market.",
   ]),
   ("What happened afterward", [
    "The record is consistent with that reading. Amazon built server "
    "processors on Arm designs for its own cloud, and Nvidia used an "
    "Arm-based processor alongside its accelerators. By 2026 industry figures "
    "put Arm-based machines at a substantial share of data centre server "
    "revenue, though a much smaller share of unit shipments, and the two "
    "measures differ enough that a reader should check which one is being "
    "quoted. SoftBank listed Arm on Nasdaq in September 2023 at $51 a share, a "
    "valuation of about $54.5 billion "
    "(<a href=\"https://www.eenewseurope.com/en/arm-to-hit-nasdaq-with-us54-5-billion-valuation/\">eeNews Europe</a>), "
    "and kept most of the company.",
    "What this shows is limited. Growth outside mobile occurred, and the "
    "royalty structure was in place when it did. It does not show that "
    "SoftBank foresaw data centre demand. The public case in 2016 concerned "
    "connected devices, and nothing in the announcement mentions servers. What "
    "I infer is that the licensing position was a better asset than the end "
    "market that then supplied most of its revenue, and that a buyer who "
    "understood the position did not need the end market to grow quickly.",
   ]),
   ("The strongest objection", [
    "The objection is that Arm's position is less secure than a royalty "
    "stream suggests, because an open instruction set called RISC-V gives "
    "licensees a way to build chips without paying Arm. If licensees can "
    "leave at an acceptable cost, the royalty is a price and not a position.",
    "Two facts would decide the question. One is the share of new chip "
    "designs that choose RISC-V over Arm in each market. The other is how "
    "licensees behave when Arm's interests diverge from theirs, which became "
    "a live question when Arm announced a server processor of its own in "
    "March 2026. Rising RISC-V share in designs for phones or servers would "
    "weaken this note's argument.",
   ]),
   ("What a reader should take from it", [
    "When a licensing or royalty business is sold, the useful questions are "
    "how costly it is for licensees to leave and whether the licensor "
    "competes with them. The current end market matters less than both. A "
    "buyer paying a high premium for a business whose end market is slowing "
    "is not necessarily mistaken, and a reader who wants to check the price "
    "should look at licensee behavior and not at unit growth.",
   ]),
  ],
  takeaway="",
  srcs=["SoftBank Group, recommended cash acquisition of ARM Holdings plc, announced 18 July 2016. GBP 24.3bn, 1,700 pence per share, premium of approximately 43 percent. Son's statement as carried in "
        "<a href=\"https://electronicdesign.com/technologies/test-measurement/article/21206621/softbank-reaches-agreement-to-acquire-arm\">Electronic Design</a>.",
        "Market reaction and investor comments, as reported at the time. "
        "<a href=\"https://www.fierce-network.com/wireless/softbank-s-son-challenges-investors-as-shares-slide-following-news-arm-deal\">Fierce Network</a>.",
        "Arm Holdings plc, Nasdaq listing, September 2023, priced at $51 a share. "
        "<a href=\"https://www.eenewseurope.com/en/arm-to-hit-nasdaq-with-us54-5-billion-valuation/\">eeNews Europe</a>.",
        "Royalty rates, shipment volumes and smartphone growth (about 3 percent in 2016 against roughly 10 percent in 2015, per IDC estimates reported at the time) are from Arm's disclosures and contemporaneous coverage. Data centre share figures for 2026 vary by measure and are described as ranges."]),

 dict(slug="the-blocked-bid", year="2018", roman="II",
  lead="Broadcom and", line1="Qualcomm", line2="",
  sub="Approval risk became a question about national capability",
  party="Broadcom / Qualcomm", value="~$117bn, prohibited", dated="March 2018",
  lede=("Broadcom pursued Qualcomm from November 2017 without the agreement of "
        "its board and raised its offer to around $117 billion. In March 2018 "
        "a presidential order prohibited the transaction. I think the order "
        "changed what a bidder for a semiconductor company has to predict. "
        "Merger review in the United States is ordinarily a test of competition "
        "in a defined market. This order rested on a forecast about who would "
        "hold a position in a future standard, which a bidder cannot model in "
        "the same way."),
  sections=[
   ("The ordinary test", [
    "Antitrust review asks whether a combined company would raise prices or "
    "reduce choice for customers. A bidder can estimate that. It knows its own "
    "products and its rival's, it can compare their market shares, and it can "
    "propose divestitures. Most large technology transactions are priced on "
    "the assumption that this is the test.",
    "Broadcom and Qualcomm were largely complementary. Broadcom's strengths "
    "were in connectivity and networking chips, and Qualcomm's were in mobile "
    "processors and in the patents covering how handsets communicate with "
    "networks. Under the ordinary test the overlap was modest.",
   ]),
   ("What the committee examined instead", [
    "The Committee on Foreign Investment in the United States reviewed the "
    "bid because Broadcom was domiciled in Singapore, which gave it "
    "jurisdiction. Its concern, as reported from its March 2018 letter to the "
    "companies, was that Broadcom would reduce Qualcomm's research spending, "
    "that this would weaken American participation in the committees that "
    "write the 5G standards, and that Huawei and other Chinese companies "
    "would fill the gap "
    "(<a href=\"https://www.eweek.com/de/mobile/u-s-5g-leadership-at-core-of-broadcom-qualcomm-bid-regulatory-review/\">eWeek</a>). "
    "Standards are negotiated over years, and the companies that contribute "
    "the most engineers tend to hold the patents that become essential to the "
    "result.",
    "Hock Tan, Broadcom's chief executive, told Congress that any notion that "
    "the combined company would cut 5G funding or cede leadership was "
    "“completely unfounded.” Broadcom also offered commitments on research "
    "spending. The president's order, issued on 12 March 2018, rested on a "
    "different kind of finding: “There is credible evidence that leads me to "
    "believe that Broadcom Limited” might “take action that threatens to "
    "impair the national security of the United States.” It added that "
    "Broadcom and Qualcomm “shall immediately and permanently abandon the "
    "proposed takeover” "
    "(<a href=\"https://trumpwhitehouse.archives.gov/presidential-actions/presidential-order-regarding-proposed-takeover-qualcomm-incorporated-broadcom-limited\">presidential order</a>).",
    "The word that matters is “might.” The order does not find that Broadcom "
    "would harm the United States. It finds credible evidence that it could. "
    "That is a lower standard than the evidence a competition case would "
    "require, and it turns on a prediction of industrial capability several "
    "years out, which Broadcom disputed and which no market share table can "
    "answer.",
   ]),
   ("What changed for bidders", [
    "Before the order, a bidder's regulatory risk was mostly a competition "
    "analysis it could price. After it, the risk for a semiconductor deal "
    "included a national interest assessment that could stop a transaction on "
    "a forecast. That is hard to price, and it explains features that are now "
    "routine in large chip agreements: long outside dates for completion and "
    "termination fees large enough to compensate a seller for waiting.",
    "Subsequent export controls, restrictions on named companies and "
    "manufacturing subsidies follow similar reasoning. The 2018 order did not "
    "cause them. It was an early public application of that reasoning to a "
    "transaction this large.",
   ]),
   ("The strongest objection", [
    "The order may reflect unusual facts and not a general rule. Broadcom was "
    "a foreign acquirer of a company at the center of a standards fight with a "
    "named competitor, and it had a publicly known practice of cutting "
    "research spending at companies it bought. A different buyer with a "
    "different record might have been cleared.",
    "That is a reasonable reading, and later transactions test it. If "
    "large semiconductor deals involving US-domiciled buyers continue to face "
    "reviews that turn on capability and not on market share, the 2018 order "
    "was an early instance of a general change. If they clear on competition "
    "analysis alone, it was an exception.",
   ]),
   ("What a reader should take from it", [
    "When a semiconductor deal is announced, read the domicile of the buyer "
    "and the seller's position in standards and supply chains alongside the "
    "market shares. The termination fee and the outside date show how much "
    "approval risk the parties believe they carry.",
   ]),
  ],
  takeaway="",
  srcs=["Broadcom Limited's unsolicited proposals for Qualcomm Incorporated from November 2017, raised to approximately $121bn including assumed debt in February 2018 and later reduced to around $117bn.",
        "Order Regarding the Proposed Takeover of Qualcomm Incorporated by Broadcom Limited, 12 March 2018. "
        "<a href=\"https://trumpwhitehouse.archives.gov/presidential-actions/presidential-order-regarding-proposed-takeover-qualcomm-incorporated-broadcom-limited\">whitehouse.gov archive</a>.",
        "CFIUS letter of 5 March 2018 as described in contemporaneous coverage, including Hock Tan's response to Congress. "
        "<a href=\"https://www.eweek.com/de/mobile/u-s-5g-leadership-at-core-of-broadcom-qualcomm-bid-regulatory-review/\">eWeek</a>.",
        "The description of Broadcom and Qualcomm as largely complementary is the author's reading of their product lines and is not a finding by any regulator."]),

 dict(slug="the-layer-above", year="2018", roman="III",
  lead="IBM and", line1="Red Hat", line2="",
  sub="Customers pay for work they have already done",
  party="IBM / Red Hat", value="$34bn", dated="Announced October 2018",
  lede=("IBM agreed in October 2018 to buy Red Hat at $190 a share in cash, "
        "about $34 billion, a premium of roughly 63 percent. Red Hat's main "
        "product is free software. I think the price is explained by what a "
        "customer would have to redo to leave, and that the main risk to the "
        "purchase is IBM's own ownership, because the asset is worth most "
        "while it stays neutral across the cloud providers that IBM competes "
        "with."),
  sections=[
   ("The skeptical reading", [
    "Investors and analysts questioned the purchase. IBM's shares fell about 4 "
    "percent on the announcement because the all-cash structure would halt "
    "buybacks and add debt, and Red Hat's shares closed at $169.63, below the "
    "$190 offer, which Fortune read as a sign of Wall Street's doubts "
    "(<a href=\"https://fortune.com/2018/10/29/ibm-red-hat-cloud-data\">Fortune</a>). "
    "Moody's put IBM's rating under review and called the deal “a departure "
    "from IBM's historical acquisition philosophy of making small, tuck-in "
    "acquisitions.” Citigroup's Jim Suva said the purchase could suggest IBM "
    "was less well placed in cloud than it had claimed. Others disagreed. "
    "Bernstein's Toni Sacconaghi argued that Red Hat already had a strong "
    "foothold in the cloud.",
   ]),
   ("What customers pay for", [
    "Red Hat Enterprise Linux is a distribution of Linux, which is open "
    "source. Anyone can download the code at no charge. What Red Hat sold was "
    "a supported version: tested across a defined set of hardware, patched on "
    "a published schedule for a long support window, and certified to work "
    "with the commercial applications a bank or hospital runs. The "
    "subscription buys accountability and a maintenance commitment.",
    "That position is strong because of work the customer has already done. "
    "Consider a hypothetical bank that has certified three hundred "
    "applications against one distribution. To move, it would have to repeat "
    "that testing for all of them. The cost is counted in engineering years "
    "and in the risk of an outage, and it has little to do with the price of "
    "an alternative. A supplier whose customers face that cost can sustain a "
    "subscription price that the free product alone could not support.",
   ]),
   ("Why IBM bought it", [
    "IBM had lost ground in cloud computing to Amazon and Microsoft and had "
    "no realistic way to catch them by building. Buying a smaller cloud "
    "provider would have been costly without solving the problem. Red Hat's "
    "software runs in more than one cloud and in customers' own data centers, "
    "so its revenue does not depend on which provider wins.",
    "IBM's chief executive, Ginni Rometty, put it this way in the "
    "announcement: “Businesses are starting the next chapter of their digital "
    "reinventions,” and “they need open, flexible technology to manage these "
    "hybrid multicloud environments.” The release also stated that “IBM "
    "preserves Red Hat's independence and neutrality” "
    "(<a href=\"https://www.sec.gov/Archives/edgar/data/51143/000095014219001515/eh1900893_ex9901.htm\">joint press release</a>). "
    "That commitment is the central one. A buyer paying a 63 percent premium "
    "for neutrality is promising to preserve something that its own ownership "
    "puts at risk.",
   ]),
   ("The risk the structure creates", [
    "Red Hat's neutrality is an asset that IBM can reduce by its own "
    "decisions. IBM sells a cloud service. If Red Hat's engineers favor IBM's "
    "cloud, or if customers on other clouds believe they do, the reason to "
    "choose Red Hat everywhere weakens. The same dynamic ended the Nvidia and "
    "Arm transaction in 2022, where licensees objected to an owner with a "
    "competing product.",
    "The two cases differ in how the risk shows up. Arm's licensees had a "
    "regulator to appeal to. Red Hat's customers have only their own purchasing "
    "decisions. What would show whether IBM preserved neutrality is whether "
    "Red Hat's products stay fully supported on Amazon's, Microsoft's and "
    "Google's clouds, and whether Red Hat's revenue growth, which IBM reports "
    "each quarter, holds up among customers that run on those clouds.",
   ]),
   ("What a reader should take from it", [
    "The skeptics addressed the cost, and IBM's shares did fall on the "
    "announcement. They did not address the mechanism. A buyer of this kind of "
    "business should be judged on whether it kept the property that made the "
    "asset valuable, and for IBM that means the evidence of neutrality over "
    "years and not a single year of results.",
   ]),
  ],
  takeaway="",
  srcs=["IBM and Red Hat, joint press release, 28 October 2018. $190.00 per share in cash, approximately $34bn in equity value, including the statements by Ginni Rometty and the commitment to Red Hat's independence and neutrality. "
        "<a href=\"https://www.sec.gov/Archives/edgar/data/51143/000095014219001515/eh1900893_ex9901.htm\">sec.gov</a>. Completed 9 July 2019.",
        "Market and analyst reaction, including the share price moves, the Moody's review and the Citigroup and Bernstein comments. "
        "<a href=\"https://fortune.com/2018/10/29/ibm-red-hat-cloud-data\">Fortune</a>.",
        "The 63 percent premium is as reported by Fortune against Red Hat's closing price on the preceding Friday.",
        "Red Hat's subscription, support and certification model is from the company's filings prior to the acquisition."]),

 dict(slug="the-wiring", year="2019", roman="IV",
  lead="Nvidia and", line1="Mellanox", line2="",
  sub="A network sets how much a data center's processors can do",
  party="Nvidia / Mellanox", value="$6.9bn", dated="Announced March 2019",
  lede=("Nvidia agreed in March 2019 to buy Mellanox Technologies at $125 a "
        "share in cash, about $6.9 billion. It later looked prescient, because "
        "demand for AI training arrived and the networking Mellanox sold became "
        "essential. I think the purchase is better explained by a constraint "
        "Nvidia's customers already faced in 2019 than by a forecast of "
        "generative AI. That makes it a more repeatable kind of judgment."),
  sections=[
   ("The inference from hindsight", [
    "The common inference from what happened next is that Nvidia foresaw the "
    "AI boom. The announcement supports a narrower claim. Jensen Huang, "
    "Nvidia's chief executive, said that “addressing this demand will require "
    "holistic architectures that connect vast numbers of fast computing "
    "nodes.” The demand he referred to was the one created by AI and data "
    "science, which were already growing in 2019. The release describes the "
    "deal as one that “will unite two of the world's leading companies in "
    "high performance computing” "
    "(<a href=\"https://www.sec.gov/Archives/edgar/data/1045810/000104581019000031/ex991jointpr.htm\">joint press release</a>). "
    "Nothing in it predicts a particular application or a particular scale.",
   ]),
   ("What Mellanox sold", [
    "Mellanox made high speed networking hardware, mainly for a technology "
    "called InfiniBand. It is not internet networking. It connects machines "
    "inside one facility, where delay is measured in microseconds and "
    "consistency matters more than distance. Its customers were largely "
    "scientific computing centers, such as national laboratories, weather "
    "services and genomics institutes.",
   ]),
   ("Why that equipment sets the value of other equipment", [
    "A computing job too large for one machine is divided across many. Those "
    "machines cannot work entirely alone, because each periodically needs "
    "results the others have produced, so they stop, exchange data and "
    "continue. If the connection is slow or inconsistent, every machine waits "
    "for the slowest exchange.",
    "A hypothetical example shows the size of the effect. Suppose a facility "
    "has a thousand processors and the network keeps each of them waiting for "
    "ten percent of the time. The operator is paying for a thousand processors "
    "and getting the output of nine hundred. A faster network that removes the "
    "waiting adds the equivalent of a hundred processors without buying one. "
    "The customer therefore compares the network's price with the cost of idle "
    "processors, not with the price of other cables, and that comparison is "
    "why a supplier of what looks like commodity hardware can charge well.",
   ]),
   ("Why buy and not partner", [
    "The strongest objection is that the two companies already worked "
    "together. Mellanox's chief executive, Eyal Waldman, referred in the "
    "announcement to “our longstanding partnership.” If the partnership "
    "worked, a purchase paid a premium for something Nvidia already had.",
    "Ownership gave Nvidia something a partnership did not, which was control "
    "of the roadmap for a component that determined how its own products "
    "performed in the largest installations, and protection against a "
    "competitor owning that component. The evidence that would decide the "
    "matter is how Nvidia sold the combination afterward. Selling networking "
    "and accelerators together as one system, which Nvidia later did, is "
    "consistent with the ownership argument. It does not prove the premium "
    "was necessary.",
   ]),
   ("What a reader should take from it", [
    "Separate what an acquirer said it was buying from what happened after. "
    "The announcement is adequately explained by what Nvidia's customers were "
    "doing in 2019, and attributing the result to foresight makes the "
    "decision look less repeatable than it was. The repeatable version is to "
    "ask what determines how much use a customer gets from equipment it has "
    "already bought, and to look for suppliers of that component.",
   ]),
  ],
  takeaway="",
  srcs=["NVIDIA Corporation and Mellanox Technologies, joint press release, 11 March 2019. $125.00 per share in cash, approximately $6.9bn enterprise value, with the statements by Jensen Huang and Eyal Waldman. "
        "<a href=\"https://www.sec.gov/Archives/edgar/data/1045810/000104581019000031/ex991jointpr.htm\">sec.gov</a>. Completed April 2020.",
        "InfiniBand's role in high performance computing is from Nvidia's and Mellanox's technical documentation.",
        "The thousand-processor example is hypothetical and uses round numbers."]),

 dict(slug="paid-in-paper", year="2020", roman="V",
  lead="AMD and", line1="Xilinx", line2="",
  sub="In an all-stock deal the dollar value is not the price",
  party="AMD / Xilinx", value="$35bn announced, ~$49bn at close", dated="October 2020",
  lede=("AMD agreed in October 2020 to buy Xilinx in an all-stock transaction "
        "that it described as valued at $35 billion. It completed in February "
        "2022 at a figure widely reported near $49 billion, and the business "
        "acquired had not changed to account for the difference. I think the "
        "announced dollar value of an all-stock deal should not be read as a "
        "price paid. The exchange ratio and the ownership split are the "
        "terms."),
  sections=[
   ("The convention being challenged", [
    "Press coverage and published comparisons of deal values usually report "
    "the figure in the announcement. AMD's own release gave one, and Xilinx "
    "shareholders were told they would receive about $143 a share, based on "
    "the average of AMD's price over the ten trading days through 8 October "
    "2020 "
    "(<a href=\"https://www.sec.gov/Archives/edgar/data/743988/000110465920118358/tm2034313d1_ex99-1.htm\">joint press release</a>). "
    "The convention is reasonable for a cash deal, where the figure is what "
    "changes hands.",
   ]),
   ("What all-stock means", [
    "No cash left AMD. The release set a fixed ratio of 1.7234 AMD shares for "
    "each Xilinx share, and the completion announcement repeats that the "
    "ratio was unchanged "
    "(<a href=\"https://www.sec.gov/Archives/edgar/data/2488/000000248822000031/xilinxacquisitionclosepres.htm\">AMD completion release</a>). "
    "Xilinx shareholders did not exit. They became owners of the combined "
    "company and continue to bear its results. The release stated that, on a "
    "fully diluted basis, AMD stockholders would own about 74 percent and "
    "Xilinx stockholders about 26 percent.",
    "That is the price, in the sense that matters to each side. AMD agreed to "
    "give up 26 percent of itself. Xilinx's owners agreed to take 26 percent "
    "of a larger company. What each portion was worth in dollars depended on "
    "AMD's share price, which moved.",
   ]),
   ("Why the dollar value moved", [
    "The ratio was set in October 2020 and the share price was not. AMD's stock "
    "rose between announcement and completion in February 2022, and the "
    "value of the consideration rose with it, to a figure reported near $49 "
    "billion. The completion release itself gives the ratio and no dollar "
    "value, which is consistent with the point that the ratio is the term "
    "and the dollar figure is a snapshot.",
    "A hypothetical shows how the snapshot misleads. If AMD's stock had fallen "
    "by half instead, the same deal would have been reported as a $17 billion "
    "purchase, and nothing about what AMD gave or Xilinx received in "
    "ownership would have changed.",
   ]),
   ("The business acquired", [
    "Xilinx made field programmable gate arrays, chips whose logic can be "
    "reconfigured after manufacture. They are slower and costlier per unit "
    "of work than a chip designed for one purpose, and they suit applications "
    "where the task changes or the volume does not justify a custom design. "
    "Telecommunications equipment was the largest market. Victor Peng, "
    "Xilinx's chief executive, said that “together, we will lead the new era "
    "of high performance and adaptive computing.” AMD has since reported the "
    "business within its embedded segment and does not break out its "
    "contribution to AI revenue in a way that settles any claim about it.",
   ]),
   ("The strongest objection", [
    "The objection is that the announced value was a fair description at "
    "the time it was made, and that a deal agreed at $35 billion was a $35 "
    "billion deal. For the purpose of recording what the market valued, that "
    "is correct.",
    "It is incomplete for any purpose that compares one transaction with "
    "another or asks what a buyer paid. The test is whether the comparison "
    "changes when the buyer's share price changes. If it does, the dollar "
    "figure was not a price.",
   ]),
   ("What a reader should take from it", [
    "For an all-stock deal, look at the exchange ratio and the ownership "
    "split first, then at the value on the signing date and on the closing "
    "date. A sector comparison that mixes cash deals and stock deals at "
    "announcement values is mixing two different measures.",
   ]),
  ],
  takeaway="",
  srcs=["Advanced Micro Devices, Inc. and Xilinx, Inc., joint press release, 27 October 2020. All-stock, 1.7234 AMD shares per Xilinx share, approximately $35bn, about $143 per Xilinx share, 74 percent and 26 percent ownership. "
        "<a href=\"https://www.sec.gov/Archives/edgar/data/743988/000110465920118358/tm2034313d1_ex99-1.htm\">sec.gov</a>.",
        "AMD, completion release, 14 February 2022, which gives the ratio and no dollar value. "
        "<a href=\"https://www.sec.gov/Archives/edgar/data/2488/000000248822000031/xilinxacquisitionclosepres.htm\">sec.gov</a>.",
        "The figure of about $49bn at completion is widely reported and is not stated in either release. The $17bn example is hypothetical."]),

 dict(slug="too-central", year="2022", roman="VI",
  lead="Nvidia and", line1="Arm", line2="",
  sub="Part of Arm's value was that no competitor owned it",
  party="Nvidia / Arm, abandoned", value="$40bn", dated="Announced September 2020",
  lede=("Nvidia agreed in September 2020 to buy Arm from SoftBank for up to "
        "$40 billion in cash and stock. In February 2022 the parties "
        "abandoned the transaction, and SoftBank kept a $1.25 billion payment "
        "Nvidia had made in advance. I think the deal failed because the asset "
        "was worth less to the market once an interested party owned it. Arm's "
        "licensees accept a common foundation because its owner has no chip "
        "of its own to favor."),
  sections=[
   ("What each side argued", [
    "Nvidia argued that it would keep Arm's open licensing model. A "
    "spokesperson said regulators and customers would see the benefits of "
    "that plan, and the company's position was that the purchase price alone "
    "gave it no incentive to damage the asset "
    "(<a href=\"https://www.cnbc.com/amp/2021/02/12/qualcomm-objects-to-nvidias-40-billion-arm-acquisition.html\">CNBC</a>).",
    "Licensees disagreed. Qualcomm, according to reporting from February "
    "2021, told regulators in several jurisdictions that it feared Nvidia "
    "would restrict Arm's licensing, and Microsoft and Google also raised "
    "concerns "
    "(<a href=\"https://fortune.com/2021/02/12/google-microsoft-qualcomm-protest-nvidia-arm-acquisition\">Fortune</a>). "
    "In December 2021 the US Federal Trade Commission sued to block the "
    "transaction, alleging that the combined firm would have the means and "
    "incentive to “stifle innovative next-generation technologies” "
    "(<a href=\"https://ftc.gov/news-events/press-releases/2021/12/ftc-sues-block-40-billion-semiconductor-chip-merger\">FTC</a>).",
   ]),
   ("Why independence is an asset", [
    "Arm licenses its designs to companies that compete with one another. "
    "Part of why they build on a common foundation is that Arm makes no chips "
    "and has no stake in which of them wins. That neutrality is a property of "
    "the asset. It does not appear in Arm's financial statements, and a "
    "valuation model has no line for it.",
    "Nvidia builds chips and competes with many of Arm's licensees. Arm "
    "would have shown those licensees' designs and plans to a competitor "
    "while controlling the terms of their licenses. A hypothetical licensee "
    "planning a server processor would have had to ask whether its roadmap "
    "was safe with Nvidia as its supplier. Even a sincere promise of fair "
    "treatment leaves the licensee exposed, which is why the objection did not "
    "depend on Nvidia misusing the position. It depended on the position "
    "existing.",
   ]),
   ("How it ended", [
    "The termination announcement cited “significant regulatory challenges "
    "preventing the consummation of the transaction, despite good faith "
    "efforts by the parties.” Huang said that “though we won't be one company, "
    "we will partner closely with Arm,” and Son said that SoftBank would "
    "“start preparing to take Arm public” "
    "(<a href=\"https://nvidianews.nvidia.com/news/nvidia-and-softbank-group-announce-termination-of-nvidias-acquisition-of-arm-limited\">Nvidia and SoftBank announcement</a>). "
    "SoftBank listed Arm on Nasdaq in September 2023 at a valuation of "
    "about $54.5 billion, above the $40 billion Nvidia had offered.",
   ]),
   ("The strongest objection", [
    "The objection comes from Arm's own behavior. In March 2026 Arm announced "
    "a server processor of its own, which places it in competition with "
    "licensees building Arm-based chips. If neutrality were as valuable as "
    "this note claims, an independent Arm would not weaken it, and the "
    "licensees' objection to Nvidia would be a matter of degree and not of "
    "kind.",
    "That is a fair challenge. The difference between the two cases is that "
    "Arm's licensees can still choose whether to keep building on its designs "
    "when it competes with them, while a sale to Nvidia would have removed "
    "that choice by changing who held the licensing terms. How those "
    "licensees respond to Arm's server processor, in the designs they choose "
    "over the next several years, will show how much of the original "
    "argument survives.",
   ]),
   ("What a reader should take from it", [
    "Where part of an asset's value comes from its independence, a sale to "
    "an interested party reduces what is being bought. Standards bodies, "
    "marketplaces, benchmarks and ratings share the property. A reader "
    "evaluating a deal for any of them should ask whether the buyer competes "
    "with the asset's customers, because the answer changes the value in a "
    "way a price cannot show.",
   ]),
  ],
  takeaway="",
  srcs=["NVIDIA Corporation, SoftBank Group and Arm Limited, announced 13 September 2020, up to $40bn in stock and cash. Terminated 8 February 2022. The termination statement and the quotations from Jensen Huang and Masayoshi Son are in "
        "<a href=\"https://nvidianews.nvidia.com/news/nvidia-and-softbank-group-announce-termination-of-nvidias-acquisition-of-arm-limited\">the joint announcement</a>.",
        "SoftBank retained the $1.25bn prepayment, which it recognized in its own results.",
        "Objections by Qualcomm, Microsoft and Google are as reported by CNBC and Fortune in February 2021. Qualcomm's own submissions to regulators were not published. "
        "The FTC's complaint was announced on 2 December 2021.",
        "Arm announced its own server processor in March 2026. Coverage of its availability and timing varies, and it is treated here as directional."]),

 dict(slug="the-price-machine", year="2022", roman="VII",
  lead="Broadcom and", line1="VMware", line2="",
  sub="A return that depends on customers staying, not on growth",
  party="Broadcom / VMware", value="$61bn", dated="Announced May 2022",
  lede=("Broadcom agreed in May 2022 to buy VMware for about $61 billion in "
        "cash and stock plus about $8 billion of net debt, a premium of 44 "
        "percent. I think the transaction is best read as a purchase of "
        "customers who cannot leave cheaply and not as a purchase of a growing "
        "business. The return depends on keeping those customers while "
        "raising what they pay, which is a calculation a buyer can make with "
        "more confidence than a growth forecast."),
  sections=[
   ("The stated rationale", [
    "The announcement described a combination of strengths. Hock Tan, "
    "Broadcom's chief executive, said that “this transaction combines our "
    "leading semiconductor and infrastructure software businesses.” VMware's "
    "chief executive, Raghu Raghuram, said that “collectively, we will "
    "deliver even more choice, value and innovation to customers” "
    "(<a href=\"https://www.sec.gov/Archives/edgar/data/1730168/000119312522160371/d323890dex991.htm\">joint press release</a>). "
    "On that account the deal adds product breadth and the customers "
    "benefit.",
   ]),
   ("What VMware sells and what Broadcom does with such assets", [
    "VMware's core product allows one physical server to run as several "
    "independent machines. It is the basis on which much corporate computing "
    "has been organized for two decades. It sits beneath the applications a "
    "company runs and not beside them. Replacing it means moving every "
    "workload that depends on it, testing each one and accepting the risk "
    "of the move. Most organizations conclude that the project would cost "
    "more than the licenses.",
    "The release's own headline describes Broadcom's method: the purchase "
    "“advances Broadcom's strategy to build the world's leading "
    "infrastructure technology company, with track record of acquiring "
    "established, mission-critical platforms.” The record includes CA "
    "Technologies and the enterprise business of Symantec. In each, Broadcom "
    "reduced research spending and smaller product lines, focused commercial "
    "effort on its largest customers and raised prices. The return in that "
    "model does not require the acquired business to grow. It requires "
    "existing customers to stay, and the cost of replacing the product is what "
    "keeps them.",
   ]),
   ("What the record shows", [
    "The transaction closed on 22 November 2023 after review in several "
    "jurisdictions. Since then, complaints have centered on price. CISPE, "
    "the association of European cloud providers, challenged the European "
    "Commission's approval in court and later filed a competition complaint "
    "that put the cumulative increase for European providers above 1,000 "
    "percent once price rises, bundling and minimum purchase terms are "
    "counted. Other reporting has put increases for some customers between "
    "800 and 1,500 percent "
    "(<a href=\"https://www.computing.co.uk/news/2025/cloud/european-customers-rail-against-broadcom-vmware-price-hikes\">Computing</a>, "
    "<a href=\"https://heise.de/-11220013\">heise</a>). "
    "Broadcom disputes the complaint and describes CISPE as funded by large "
    "cloud providers.",
    "These sources show that prices rose and that some customers objected "
    "loudly. They do not show how many customers left or what share of "
    "revenue was lost, and that is the number the thesis turns on.",
   ]),
   ("The strongest objection", [
    "The objection is that the price increases are not evidence of a "
    "problem. If Broadcom's customers could leave, many would have, and the "
    "fact that revenue is retained after the increases shows the product is "
    "worth the new price. Broadcom's twenty-year record of profitable "
    "acquisitions supports that view.",
    "I agree that the approach is profitable. The question is whether it has "
    "a delayed cost. Enterprise buyers have long memories and wide discretion "
    "over whom they invite to bid next time. Such a cost would not appear in "
    "a quarterly figure. It would appear in processes Broadcom is not asked to "
    "join, years later, and would be hard to attribute. The evidence that "
    "would decide it is documented migration away from VMware, the outcome of "
    "the European complaint and court case, and how customers describe "
    "Broadcom as a vendor in later purchasing decisions.",
   ]),
   ("What a reader should take from it", [
    "When a buyer pays a large premium for infrastructure software, ask "
    "whether the underwriting depends on growth or on retention. A deal "
    "underwritten on retention can proceed in conditions that stop other "
    "buyers, because its return depends on a switching cost and not on a "
    "forecast. The same feature is what makes the later customer "
    "relationship adversarial.",
   ]),
  ],
  takeaway="",
  srcs=["Broadcom Inc. and VMware, Inc., joint press release, 26 May 2022. Approximately $61bn in cash and stock plus about $8bn of net debt, 44 percent premium, with the statements by Hock Tan and Raghu Raghuram. "
        "<a href=\"https://www.sec.gov/Archives/edgar/data/1730168/000119312522160371/d323890dex991.htm\">sec.gov</a>. Completed 22 November 2023.",
        "CISPE's complaint and court challenge, and Broadcom's response, as reported by "
        "<a href=\"https://www.computing.co.uk/news/2025/cloud/european-customers-rail-against-broadcom-vmware-price-hikes\">Computing</a> and "
        "<a href=\"https://heise.de/-11220013\">heise</a>. The percentage figures are the complainants' and are disputed by Broadcom.",
        "Broadcom's acquisition record at CA Technologies and Symantec's enterprise business is from its public disclosures."]),

 dict(slug="reading-the-record", year="2023", roman="VIII",
  lead="Cisco and", line1="Splunk", line2="",
  sub="Two budgets pay for the product, and execution is the open question",
  party="Cisco / Splunk", value="$28bn", dated="Announced September 2023",
  lede=("Cisco agreed in September 2023 to buy Splunk at $157 a share in "
        "cash, about $28 billion, a premium of about 31 percent. I think the "
        "price is supported by the fact that Splunk is paid for out of two "
        "separate budgets inside the same customer, which makes it harder to "
        "remove. The open question is Cisco's ability to run it, and analysts "
        "at the time pointed to the same risk."),
  sections=[
   ("What Splunk sells", [
    "Software records what it does. A user signed in, a request failed, a "
    "server restarted at four in the morning. These records are called logs, "
    "and a large organization produces them in volumes no person could read. "
    "Splunk collected logs from across an organization's systems and made "
    "them searchable quickly.",
   ]),
   ("Why two budgets matter", [
    "Two groups pay for that capability, for different reasons. Security "
    "teams pay because the evidence of an intrusion is spread across many "
    "systems, and the useful question is what happened in sequence. That "
    "category is called security information and event management. "
    "Engineering teams pay because applications are assembled from many "
    "separate services maintained by different teams, so when something fails "
    "no individual holds the whole picture. Reading the record is the "
    "practical way to find out, and that category is called observability.",
    "A product that serves two budgets in the same customer is harder to "
    "remove than one serving a single budget, because a cost reduction in one "
    "department does not end the relationship. Cisco described the combination "
    "in these terms. Its chief executive, Chuck Robbins, said that “our "
    "combined capabilities will drive the next generation of AI-enabled "
    "security and observability” "
    "(<a href=\"https://www.sec.gov/Archives/edgar/data/1353283/000110465923102594/tm2326347d1_ex99-1.htm\">joint press release</a>).",
   ]),
   ("What analysts questioned", [
    "The reservations were about execution and not about the product. "
    "Jefferies' George Notter stressed the need for seamless integration, "
    "which he said had been mixed at Cisco historically. Barclays called "
    "Cisco's record in security and observability mixed. BMO noted near-term "
    "integration risk because Cisco's own AppDynamics and ThousandEyes "
    "overlap with Splunk's observability products, and Needham's Alex "
    "Henderson pointed to Cisco's record of realizing less than expected "
    "from earlier acquisitions "
    "(<a href=\"https://drupal-cloudfront.benzinga.com/analyst-ratings/analyst-color/23/09/34826014/is-splunk-a-good-investment-after-cisco-deal-announcement-7-analysts-weigh-in\">Benzinga</a>, "
    "<a href=\"https://www.tipranks.com/news/the-fly/barclays-mixed-on-cisco-acquisition-of-splunk\">TipRanks</a>).",
    "That risk is real, and it follows from the difference between the two "
    "businesses. Cisco has sold network hardware for decades on a purchasing "
    "cycle measured in years. A software subscription is a different "
    "commercial motion, with different staff, different renewal dynamics and "
    "different measures of success. Hardware companies have attempted the "
    "transition before with varied results.",
   ]),
   ("What the sale record shows", [
    "Splunk's proxy statement records how the price was reached "
    "(<a href=\"https://www.sec.gov/Archives/edgar/data/1353283/000114036123050211/ny20011269x2_defm14a.htm\">Splunk proxy statement</a>). "
    "Cisco first made an unsolicited indication of $165 to $175 a share in "
    "December 2021 and raised it to $193 in February 2022. Splunk's chair "
    "countered at $212, and Cisco withdrew the same day. When Cisco returned in "
    "2023 its first indication was $130, which the board's transaction "
    "committee judged not compelling. The committee decided not to run a "
    "market check, because it judged no other party likely to be interested. "
    "A series of offers and counteroffers in the last week of August ended at "
    "$157, a dollar below the $158 Splunk had said it would accept.",
    "Two things follow. The $157 was a negotiated price with a single buyer and "
    "not the result of competition, so the premium measures what Cisco "
    "was willing to pay and not what the market would have paid. And it was "
    "lower than Cisco's own indication eighteen months earlier, which "
    "supports the view that Cisco was not paying for exceptional growth and "
    "that Splunk's own situation had changed.",
   ]),
   ("The strongest objection", [
    "A skeptic can say that the two-budget argument is a justification found "
    "after the fact, and that Cisco simply paid cash for a large software "
    "business at a time when few large deals were being agreed. The 31 percent "
    "premium was lower than the 44 percent paid for VMware and the 63 percent "
    "paid for Red Hat, which supports the view that Cisco was not paying for "
    "exceptional growth.",
    "The evidence that would decide between the readings is Cisco's reported "
    "annual recurring revenue and its disclosures on Splunk renewals. If "
    "renewal rates among customers that use Splunk for both security and "
    "observability exceed those that use it for one, the two-budget argument "
    "has support.",
   ]),
   ("What a reader should take from it", [
    "For a software purchase, count how many separate budgets in the "
    "customer pay for the product, and check whether the buyer has run "
    "subscription software before. The first predicts how hard the product is "
    "to remove, and the second predicts whether the buyer can keep it.",
   ]),
  ],
  takeaway="",
  srcs=["Cisco Systems, Inc. and Splunk Inc., joint press release, 21 September 2023. $157.00 per share in cash, approximately $28bn in equity value, with the statements by Chuck Robbins and Gary Steele. "
        "<a href=\"https://www.sec.gov/Archives/edgar/data/1353283/000110465923102594/tm2326347d1_ex99-1.htm\">sec.gov</a>. Completed 18 March 2024.",
        "The 31 percent premium is as reported against Splunk's prior closing price of $119.59.",
        "Analyst comments from "
        "<a href=\"https://drupal-cloudfront.benzinga.com/analyst-ratings/analyst-color/23/09/34826014/is-splunk-a-good-investment-after-cisco-deal-announcement-7-analysts-weigh-in\">Benzinga</a> and "
        "<a href=\"https://www.tipranks.com/news/the-fly/barclays-mixed-on-cisco-acquisition-of-splunk\">TipRanks</a>. The categories security information and event management and observability are described from Splunk's filings."]),

 dict(slug="third-in-line", year="2025", roman="IX",
  lead="Google and", line1="Wiz", line2="",
  sub="A seller with an alternative commanded a higher price",
  party="Google / Wiz", value="$32bn announced, ~$29.5bn final", dated="March 2025",
  lede=("Wiz ended acquisition talks with Google in July 2024 at a reported "
        "$23 billion. Eight months later it agreed to sell to the same buyer "
        "for $32 billion, and the transaction completed on 11 March 2026 at a "
        "purchase price that Alphabet's filing puts near $29.5 billion. I think "
        "most of the difference is explained by Wiz having shown that it could "
        "say no, and that a seller with an alternative negotiates from a "
        "different position than one without."),
  sections=[
   ("What Wiz sells", [
    "A company that runs infrastructure in a cloud provider creates "
    "thousands of configuration settings, such as which systems can reach "
    "which databases, what is open to the internet and which credentials "
    "carry which permissions. Wiz examines all of it and reports which "
    "combinations create a usable path for an attacker. Earlier tools in the "
    "category produced long lists of individual warnings that teams stopped "
    "reading. Wiz produced short lists and could be connected and returning "
    "results within hours, which is most of why it grew quickly. Its "
    "reported annual recurring revenue was above $500 million in mid-2024, "
    "against $350 million a year earlier, figures that come from trade "
    "reporting and not from filings.",
   ]),
   ("The refusal", [
    "In July 2024 Wiz's chief executive, Assaf Rappaport, wrote to employees "
    "that “saying no to such humbling offers is tough” and that “while we "
    "are flattered by offers we have received, we have chosen to continue on "
    "our path to building Wiz.” Reporting on the memo said it set an initial "
    "public offering and $1 billion in annual recurring revenue as the "
    "goals "
    "(<a href=\"https://en.globes.co.il/en/article-wiz-turns-down-googles-23b-acquisition-offer-1001484935\">Globes</a>).",
    "A refusal of that kind has two effects. It tells the buyer that the "
    "seller does not need the sale, and it gives the seller a visible "
    "alternative, a public listing, to which the buyer's price will be "
    "compared. The buyer's next offer has to beat a listing and not merely "
    "match its previous number.",
   ]),
   ("Why the increase is not only growth", [
    "The offer rose by about 39 percent in eight months. Wiz kept growing "
    "over that period, and growth explains part of the increase. I infer that "
    "it does not explain all of it, because a refusal followed by a higher "
    "offer is the pattern a change in bargaining position produces. Terms "
    "covering the regulatory wait may also account for some of the gap. Those "
    "terms are not public, so the inference rests on the timing and on the "
    "seller's own statement and not on a disclosed breakdown of the price.",
    "Google's reasons for paying are easier to state. Google Cloud has been "
    "third behind Amazon and Microsoft for several years. A provider in that "
    "position rarely wins on price and seldom on features alone, because what "
    "holds a customer in place is the cost of moving. Wiz works across "
    "Amazon, Microsoft and Oracle as well as Google, and Google committed "
    "publicly to keeping it that way. Software used regardless of which cloud "
    "a customer chose produces revenue from estates Google has not won.",
   ]),
   ("The final figure", [
    "The $32 billion reported at announcement and the approximately $29.5 "
    "billion in Alphabet's quarterly filing for the period ended 31 March "
    "2026 differ for ordinary reasons, including adjustments and the treatment "
    "of equity awards. The first figure was reported widely and the second "
    "much less so, so a reader comparing deals should check which of the two "
    "a number describes.",
   ]),
   ("The strongest objection", [
    "The objection is that the increase reflects Google's own priorities and "
    "not Wiz's leverage. Google wanted a strong security product in a "
    "market where it trails, and a buyer in that position pays more for a "
    "strategic fit regardless of what the seller says.",
    "The evidence that would separate the readings is whether other buyers "
    "were involved or were reported to be, and whether Wiz's price would "
    "have held without the refusal. The record I found does not answer "
    "either, and the claim here is limited to the timing and to Wiz's own "
    "statement.",
   ]),
   ("What a reader should take from it", [
    "When a seller turns down an offer and later accepts a higher one, "
    "check what alternative it created in between. A listing, a competing "
    "bidder or a financing source all change the price, and they show up in "
    "the result before they show up in the company's performance.",
   ]),
  ],
  takeaway="",
  srcs=["Google and Wiz, Inc., announced 18 March 2025, approximately $32bn in cash. Completed 11 March 2026.",
        "Alphabet Inc. Form 10-Q for the quarter ended 31 March 2026 records a purchase price of approximately $29.5bn after adjustments, with Wiz reported within the Google Cloud segment.",
        "Rappaport's memo to employees, July 2024, as reported by "
        "<a href=\"https://en.globes.co.il/en/article-wiz-turns-down-googles-23b-acquisition-offer-1001484935\">Globes</a>. The $23bn figure and the ARR figures are from trade reporting and not from filings.",
        "Google's commitment to maintaining Wiz across other cloud providers is from the announcement."]),

 dict(slug="fetching", year="2025", roman="X",
  lead="DDN and", line1="Blackstone", line2="",
  sub="A storage supplier priced by the processor time it saves",
  party="DDN / Blackstone", value="$300m at a $5bn valuation", dated="January 2025",
  lede=("Blackstone Tactical Opportunities invested $300 million in "
        "DataDirect Networks in January 2025 at a $5 billion valuation. DDN "
        "was founded in 1998 and sold for most of its history into scientific "
        "computing. I think the valuation is explained by what DDN's product "
        "saves its customers and not by the volume of data it stores. A "
        "storage supplier that raises the utilization of very expensive "
        "processors can be priced against the cost of those processors."),
  sections=[
   ("The usual way to price storage", [
    "Storage is conventionally treated as a commodity. Capacity is measured "
    "in bytes, prices fall as flash and disk improve, and suppliers compete "
    "on cost per terabyte. On that view a $5 billion valuation for a "
    "private storage company needs an unusual explanation.",
   ]),
   ("What DDN's customers are buying", [
    "A processor working on a large job needs the next portion of data "
    "before it can continue. If the storage system cannot deliver it fast "
    "enough, the processor waits. A hypothetical operator with a facility of "
    "ten thousand accelerators, each costing tens of thousands of dollars, "
    "is paying for a very large amount of capital that earns nothing while "
    "it waits. If a better storage system recovers five percent of that "
    "time, the gain is the output of five hundred accelerators, which is "
    "worth far more than the storage system costs.",
    "The comparison customers make is therefore against idle time on a much "
    "larger investment, not against cheaper storage. Suppliers whose product "
    "governs the productivity of a customer's existing capital tend to be "
    "priced better than their category implies. The networking business "
    "described in the Mellanox note is a similar case.",
   ]),
   ("The company and the terms", [
    "DDN's chief executive, Alex Bouzari, said that “Blackstone's support "
    "accelerates our mission to redefine the enterprise AI infrastructure "
    "category,” and Blackstone's Jas Khaira said that “we are thrilled to be "
    "the first institutional investor in DDN.” The release said the "
    "investment would “help fund DDN's continued rapid growth,” and it named "
    "BofA Securities as DDN's exclusive financial adviser "
    "(<a href=\"https://pulse2.com/ddn-ai-and-data-intelligence-solutions-company-raises-300-million-at-5-billion-valuation/amp/\">Pulse 2.0, reproducing the release</a>). "
    "The release gave no revenue figure. Forbes has reported revenue near "
    "$400 million in 2024, about $500 million in 2025 and a projection near $1 "
    "billion for 2026 "
    "(<a href=\"https://aiweekly.co/alerts/ddn-projects-revenue-doubling-to-1b-in-2026-on-ai-storage-boom\">AI Weekly</a>). "
    "On those figures $5 billion is about ten times 2025 revenue and five times "
    "the 2026 projection.",
   ]),
   ("What would have to be true", [
    "A valuation on a private company is an expectation and not a result. "
    "This one implies that enterprise demand for this kind of system grows "
    "substantially, and that DDN holds its position as larger storage "
    "vendors and the cloud providers address the same requirement. The "
    "revenue projection is the checkable part, and it had not been reached "
    "when this was written.",
   ]),
   ("The strongest objection", [
    "The objection is that the valuation reflects the market for anything "
    "adjacent to AI spending. In that case it would fall with the sector, "
    "whatever DDN's storage does. The evidence for that view is the number "
    "of related businesses that raised capital on favorable terms over the "
    "same period.",
    "The two readings predict different results. If the valuation tracks "
    "sector sentiment, DDN's revenue growth should look like everyone else's "
    "and its valuation should move with theirs. If it tracks utilization, "
    "DDN should keep winning in the largest installations, where idle "
    "processors cost the most, even if sentiment weakens.",
   ]),
   ("What a reader should take from it", [
    "When a supplier of a component sounds like a commodity, ask what the "
    "customer would lose if the component underperformed. The answer sets the "
    "price the supplier can defend. The separate account of what the bank did "
    "in this transaction is in "
    "<a href=\"desk-ddn.html\">Deals From Palo Alto</a>.",
   ]),
  ],
  takeaway="",
  srcs=["Blackstone, press release, January 2025. $300m investment in DataDirect Networks at a $5bn valuation, via Blackstone Tactical Opportunities. The statements by Alex Bouzari and Jas Khaira and the adviser are as reproduced by "
        "<a href=\"https://pulse2.com/ddn-ai-and-data-intelligence-solutions-company-raises-300-million-at-5-billion-valuation/amp/\">Pulse 2.0</a>.",
        "Revenue figures are Forbes's, as relayed by "
        "<a href=\"https://aiweekly.co/alerts/ddn-projects-revenue-doubling-to-1b-in-2026-on-ai-storage-boom\">AI Weekly</a>, and are not audited.",
        "The ten thousand accelerator example is hypothetical and uses round numbers."]),
]
