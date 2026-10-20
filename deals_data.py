"""Ten deal notes hanging off the Katabasis spine.

Every one runs the same move: what it looked like, what it actually was, and
what was in the belly. The explanation comes before the judgement, because a
reader who does not yet understand the mechanism cannot tell a good argument
from a confident one.

No em dashes. Figures are as announced unless the note says otherwise.
"""

DEALS = [

 dict(slug="the-blueprint", year="2016", roman="I",
  lead="The", line1="Blueprint", line2="",
  sub="SOFTBANK PAYS $32BN FOR A COMPANY<br>THAT HAS NEVER MADE A CHIP",
  party="SoftBank / ARM", value="$32bn", dated="July 2016",
  lede=("Masayoshi Son bought ARM Holdings in July 2016 for about $32 billion, "
        "a 43 percent premium, in cash, having apparently decided on it over a "
        "fortnight. The reaction was broadly that he had overpaid for a British "
        "company whose chips were in phones, at the exact moment phones stopped "
        "growing."),
  sections=[
   ("What ARM actually sells", [
    "ARM has never manufactured a chip and does not intend to. It designs the "
    "instruction set, the basic grammar a processor understands, and licenses it "
    "to everybody else. Apple, Qualcomm, Samsung and several hundred others take "
    "the design, build their own chip around it, and pay ARM a royalty on every "
    "single one.",
    "The royalty is small. Often cents. The volume is roughly thirty billion "
    "chips a year, which is how cents become a business.",
    "This is an unusual thing to own. ARM does not compete with its customers, "
    "which is why its customers were willing to standardise on it. It has no "
    "factories, so it has no capital cycle and no exposure to whether any "
    "particular phone sells. It sits underneath the industry and takes a toll.",
   ]),
   ("Which is why the phone framing missed it", [
    "Everyone priced ARM as a mobile company because in 2016 almost all its "
    "royalties came from mobile. That was a description of the present read as a "
    "forecast.",
    "What ARM actually had was a design that was radically more power efficient "
    "than the alternative, in a decade about to discover that power was the "
    "binding constraint on everything. A chip that uses less electricity is "
    "merely nice in a phone. In a building containing a hundred thousand of them, "
    "it is the entire economics."]),
   ("Here is what was in the horse", [
    "Within a few years ARM designs were in the data centre, which had been "
    "Intel&rsquo;s uncontested territory for twenty years. Amazon designed its "
    "own ARM-based server chips. Apple moved its laptops onto ARM and the "
    "comparison was not close. Nearly every AI accelerator built since has ARM "
    "somewhere in it.",
    "SoftBank did not buy a mobile company. It bought the position underneath "
    "whatever came next, and it was able to buy that position cheaply precisely "
    "because everyone was busy pricing what had already happened.",
    "ARM listed publicly again in 2023 at a valuation several times what SoftBank "
    "paid, with SoftBank keeping most of it. Whatever you think of the man, that "
    "one was read correctly."]),
   ("What I take from it", [
    "The useful habit here is not about chips. It is that a business which "
    "charges a very small amount for something everybody has to use is almost "
    "always underpriced, because the market prices the current volume and not the "
    "position.",
    "My read is that this is the single most repeated mistake in technology "
    "valuation, and it is repeated because the correct answer always looks "
    "expensive at the time."]),
  ],
  takeaway=("Everybody valued what ARM was being paid for. One buyer valued "
            "where it was standing."),
  srcs=["SoftBank Group, recommended cash acquisition of ARM Holdings plc, announced 18 July 2016. Approximately GBP 24.3bn, 1,700 pence per share, a premium of about 43 percent to the prior close.",
        "ARM's licensing and royalty model, and its annual chip shipment volumes, from the company's own disclosures and subsequent listing documents.",
        "ARM Holdings plc returned to public markets on Nasdaq in September 2023, with SoftBank retaining a substantial majority."]),

 dict(slug="the-blocked-bid", year="2018", roman="II",
  lead="The", line1="Blocked", line2="Bid",
  sub="A PRESIDENTIAL ORDER ENDS THE LARGEST<br>TECHNOLOGY TAKEOVER EVER ATTEMPTED",
  party="Broadcom / Qualcomm", value="$117bn, blocked", dated="March 2018",
  lede=("Broadcom went hostile for Qualcomm in November 2017 and raised its offer "
        "to around $117 billion, which would have been the largest technology "
        "acquisition in history by a distance. In March 2018 it was stopped by "
        "an executive order, on the recommendation of a committee most people in "
        "the industry could not have named a month earlier."),
  sections=[
   ("What was being bought", [
    "Qualcomm owns a great deal of the intellectual property underneath mobile "
    "communications. Not just chips: the patents on how a phone talks to a tower. "
    "Anybody building a modern handset pays Qualcomm something, which is a "
    "position roughly as good as ARM&rsquo;s and considerably more litigated.",
    "At the time, Qualcomm was deep in the work on 5G, the next generation of "
    "those standards. Standards are written in committees over years, and the "
    "companies with the most engineers in the room end up with the most patents "
    "in the result.",
   ]),
   ("What Broadcom was going to do with it", [
    "Broadcom under Hock Tan runs a specific and very effective model. Buy "
    "something established, cut the research spending hard, keep the parts "
    "customers cannot leave, and return the cash. It works. It has made an "
    "enormous amount of money for shareholders over two decades.",
    "Apply that to Qualcomm and you get a cost-efficient company with a smaller "
    "research budget, at the precise moment the 5G standards were being written.",
   ]),
   ("Here is what was in the horse", [
    "The Committee on Foreign Investment in the United States looked at that "
    "sequence and reached a conclusion nobody in the deal had priced. If "
    "Qualcomm&rsquo;s research spending fell, the companies filling the gap in "
    "those standards committees would be Chinese, principally Huawei. The "
    "acquisition would not transfer technology to a rival. It would create a "
    "vacancy.",
    "Broadcom was then domiciled in Singapore, which gave the committee "
    "jurisdiction. On 12 March 2018 a presidential order prohibited the "
    "transaction. Not on antitrust grounds. On national security grounds.",
    "This is the moment chips stopped being a product and became territory. "
    "Everything that followed, the export controls, the entity lists, the "
    "subsidies, the fabs under construction in Arizona and Dresden and Kumamoto, "
    "was already inside that decision.",
   ]),
   ("My read", [
    "Dealmakers took a narrow lesson from this, which was to check the "
    "jurisdiction early. I think the wider lesson is more uncomfortable.",
    "For thirty years the industry operated on the assumption that capital was "
    "the senior party and governments administered the paperwork. That assumption "
    "ended on a Monday in March 2018, and a great many of the deals further down "
    "this spine died for the same reason, in the same chair, with much better "
    "lawyers."]),
  ],
  takeaway=("A hundred and seventeen billion dollars was stopped by an argument "
            "about who would be sitting in a standards committee in five "
            "years. Nobody in the room had modelled that line."),
  srcs=["Broadcom Limited's unsolicited proposal for Qualcomm Incorporated, November 2017, raised to approximately $121bn including debt in February 2018 and subsequently reduced.",
        "Presidential Order of 12 March 2018 prohibiting the proposed takeover, issued on the recommendation of the Committee on Foreign Investment in the United States.",
        "The reasoning about 5G standards participation is drawn from CFIUS correspondence reported at the time and from the order itself. The specific forecast about Huawei is the committee's, not mine."]),

 dict(slug="the-layer-above", year="2018", roman="III",
  lead="The", line1="Layer", line2="Above",
  sub="IBM PAYS $34BN FOR A COMPANY<br>THAT GIVES ITS SOFTWARE AWAY",
  party="IBM / Red Hat", value="$34bn", dated="October 2018",
  lede=("IBM agreed to buy Red Hat in October 2018 for $190 a share in cash, "
        "about $34 billion, a premium north of 60 percent and the largest "
        "software acquisition anybody had made. Red Hat&rsquo;s core product is "
        "free. You can download it this afternoon."),
  sections=[
   ("How you sell something free", [
    "Red Hat&rsquo;s business was built on Linux, which is open source. Anybody "
    "can use it, change it, and redistribute it, without paying.",
    "What Red Hat sold was not the software. It sold a version somebody would "
    "stand behind: tested, patched, supported, and certified to work with the "
    "other things a bank or a hospital runs. Large institutions do not buy "
    "software. They buy somebody to be responsible when it breaks at two in the "
    "morning.",
    "Once a bank has standardised on your distribution, changing it means "
    "recertifying every application it runs. That is a multi-year project with no "
    "visible benefit. So nobody does it.",
   ]),
   ("Why IBM, specifically, and why then", [
    "IBM had been losing for a decade. It had missed the cloud, badly, and "
    "watched Amazon and Microsoft take a market it had every structural "
    "advantage in. Buying its way to a fourth-place cloud would have been "
    "expensive and pointless.",
    "So it did not. It bought the position above the clouds instead.",
   ]),
   ("Here is what was in the horse", [
    "Red Hat&rsquo;s actual bet, which IBM paid $34 billion to own, was that no "
    "serious enterprise would put everything in one cloud. They would keep some "
    "workloads in Amazon, some in Microsoft, some in their own buildings, for "
    "reasons of price, regulation and plain negotiating leverage.",
    "If that is true, there is enormous value in the layer that makes all of "
    "those look the same to the software running on top. You get paid regardless "
    "of who wins the cloud war, and you are the only party in the room with no "
    "preference about the outcome.",
    "That bet was correct. It is also, and I do not think this gets said enough, "
    "exactly the move Google made seven years later when it paid $32 billion for "
    "Wiz, security instead of operating systems, the same structural position, "
    "within two billion dollars of the same price."]),
   ("Where I would push back on myself", [
    "The obvious objection is that IBM paid a 60 percent premium and its share "
    "price has not obviously rewarded it, which is fair and is the number people "
    "point at.",
    "My concern is different. The position was right. What I am less sure about "
    "is whether a company with IBM&rsquo;s reflexes could hold it, because the "
    "value of being the neutral layer depends entirely on remaining neutral, and "
    "neutrality is not a thing large organisations are naturally good at."]),
  ],
  takeaway=("When you cannot win the market, the next best thing is to own the "
            "part everyone has to cross regardless of who does."),
  srcs=["IBM and Red Hat joint announcement, 28 October 2018. $190.00 per share in cash, approximately $34bn including assumed debt. Closed July 2019.",
        "Red Hat's subscription and support model, and its enterprise certification position, from the company's own filings prior to acquisition.",
        "The comparison to Google and Wiz is my argument, not a claim about either company's reasoning."]),

 dict(slug="the-wiring", year="2019", roman="IV",
  lead="The", line1="Wiring", line2="",
  sub="NVIDIA BUYS A NETWORKING COMPANY<br>THREE YEARS BEFORE ANYBODY NEEDS IT",
  party="NVIDIA / Mellanox", value="$6.9bn", dated="March 2019",
  lede=("Mellanox made networking gear. Cables and switches, the equipment that "
        "lets one computer talk to another computer, which sits somewhere below "
        "the paper clip on any list of thrilling technologies. NVIDIA paid $6.9 "
        "billion for it in March 2019 and the coverage was polite and short."),
  sections=[
   ("Why ten thousand chips is a different problem", [
    "Training a large model does not run on one chip. It runs on thousands, and "
    "the work has to be divided between them.",
    "The difficulty is that they cannot work independently. Every so often all of "
    "them have to stop, share what they have learned, agree, and continue. This "
    "happens constantly. If the sharing is slow, every chip in the building waits "
    "for the slowest connection, and you have bought a warehouse of the most "
    "expensive processors ever manufactured in order to watch them sit in the "
    "dark.",
    "The industry phrase for the useful fraction is utilisation. At scale, "
    "utilisation is set by the network, not by the chips.",
   ]),
   ("What Mellanox had", [
    "Mellanox built InfiniBand, a networking standard designed for exactly this. "
    "Not for the general internet, where a little delay is fine, but for "
    "machines in one building that need to behave as one machine.",
    "It was a small market with few customers, mostly scientific computing. "
    "Supercomputers for weather and physics and genomics. Serious, unglamorous, "
    "and not large.",
    "Intel wanted it too. Microsoft reportedly looked. NVIDIA paid up.",
   ]),
   ("Here is what was in the horse", [
    "Three years later every company on earth wanted to build the thing Mellanox "
    "had spent twenty years making possible, and the only alternatives were "
    "immature.",
    "NVIDIA did not just sell the chips for the AI buildout. It sold the chips, "
    "the wiring between them, and increasingly the whole rack as one product. A "
    "competitor making a faster chip in 2024 found that the chip was not the "
    "thing it needed to beat.",
    "Six point nine billion dollars was, by 2024, less than NVIDIA cleared in a "
    "good quarter."]),
   ("The habit I am trying to point at", [
    "What interests me here is that nothing about this required predicting "
    "ChatGPT. It only required noticing that NVIDIA&rsquo;s own customers kept "
    "hitting the same wall, and that the wall was not made of silicon.",
    "My read is that the best acquisitions in this decade were almost all of this "
    "shape. Not a bet on what the future would be, but a purchase of the "
    "bottleneck that was already visible to anybody who asked the engineers "
    "instead of the analysts."]),
  ],
  takeaway=("The constraint was never how fast a chip thinks. It was how quickly "
            "ten thousand of them can agree."),
  srcs=["NVIDIA and Mellanox Technologies, announced 11 March 2019, approximately $6.9bn in cash at $125 per share. Completed April 2020 following regulatory review.",
        "InfiniBand's role in high performance computing, and the utilisation argument, from NVIDIA's own subsequent technical disclosures and from contemporaneous reporting on the auction.",
        "Competing interest from other bidders was reported at the time and is not confirmed by the parties."]),

 dict(slug="paid-in-paper", year="2020", roman="V",
  lead="Paid in", line1="Paper", line2="",
  sub="THE MOST USEFUL THING TO UNDERSTAND<br>ABOUT A NUMBER ON A PRESS RELEASE",
  party="AMD / Xilinx", value="$35bn announced", dated="October 2020",
  lede=("AMD agreed to buy Xilinx in October 2020 in an all-stock transaction "
        "valued at about $35 billion. A few years earlier AMD had been close "
        "enough to failure that its survival was a live question. Understanding "
        "how it could possibly afford this is the most useful lesson on the "
        "whole timeline."),
  sections=[
   ("All-stock means nobody wrote a cheque", [
    "AMD did not pay $35 billion. It printed shares and handed them over. Xilinx "
    "shareholders stopped owning Xilinx and started owning a slice of the "
    "combined company.",
    "AMD&rsquo;s share price had risen roughly tenfold in the preceding few "
    "years. Its own paper had become extremely valuable, so it could buy a very "
    "large company without touching a bank, a loan, or a dollar it had earned.",
    "This is not a trick. It is the ordinary mechanics of a bull market, and it "
    "is why acquisitions cluster at the top. The currency is strongest exactly "
    "when everything is most expensive.",
   ]),
   ("So the headline number is a photograph", [
    "Here is the part that should change how you read every future "
    "announcement. In an all-stock deal, the value quoted on the day is a "
    "photograph of one day&rsquo;s share price, multiplied by an exchange ratio.",
    "The ratio is fixed. The share price is not. AMD and Xilinx announced at "
    "about $35 billion and closed in February 2022 at closer to $49 billion, "
    "because AMD stock had kept rising in between. Nothing about Xilinx changed. "
    "The price did, by fourteen billion dollars, for reasons entirely external to "
    "the asset being bought.",
    "Anybody who drops a headline number like that into a comparison of what "
    "companies in a sector are worth is quoting a stale share price for the "
    "buyer and calling it a valuation of the target. It is the cheapest error in "
    "the business and it is in print most weeks.",
   ]),
   ("Here is what was in the horse", [
    "The asset itself was an odd one. Xilinx made FPGAs, chips you can "
    "reconfigure after you have bought them. Slower than a purpose-built chip, "
    "far more flexible, useful when the thing you need to compute keeps changing.",
    "In 2020 the obvious read was telecoms equipment, where Xilinx was strong. "
    "What was in the belly was that the AI buildout would want adaptable silicon "
    "in the network and at the edges, and would want a credible second source to "
    "NVIDIA badly enough to pay for it.",
    "AMD became that second source. The acquisition it paid for in inflated paper "
    "turned out to be the base of a data centre business."]),
  ],
  takeaway=("The number in the headline is not a price. It is one day's share "
            "price wearing a price's clothes, and in a bull market it is "
            "flattering everybody involved."),
  srcs=["AMD and Xilinx, announced 27 October 2020, all-stock transaction valued at approximately $35bn at announcement, 1.7234 AMD shares per Xilinx share.",
        "Completed 14 February 2022. The higher closing value reflects AMD share price appreciation between announcement and completion and is widely reported at around $49bn.",
        "The characterisation of FPGA use cases is general industry description, not a claim from either company."]),

 dict(slug="too-central", year="2022", roman="VI",
  lead="Too", line1="Central", line2="",
  sub="THE DEAL THAT DIED BECAUSE<br>ITS CUSTOMERS WERE THE BUYER&rsquo;S RIVALS",
  party="NVIDIA / ARM, abandoned", value="$40bn", dated="February 2022",
  lede=("NVIDIA agreed to buy ARM from SoftBank in September 2020 for about $40 "
        "billion in cash and stock. Seventeen months later it was abandoned, with "
        "NVIDIA forfeiting a $1.25 billion prepayment it had already handed over. "
        "It is the most instructive failure on this spine."),
  sections=[
   ("Why it made obvious sense", [
    "NVIDIA was becoming the most important chip company in the world. ARM owned "
    "the design language most chips are built from. Putting them together would "
    "have created something with a position in nearly every category of computing "
    "at once.",
    "SoftBank wanted to sell, the price was large, and both boards agreed. On "
    "paper it is a clean transaction.",
   ]),
   ("Why it was dead on arrival", [
    "ARM&rsquo;s entire value rests on a single property: it is neutral. Its "
    "customers compete ferociously with each other and all of them are willing to "
    "build on ARM precisely because ARM does not build chips itself.",
    "NVIDIA builds chips. It competes with substantially everybody on "
    "ARM&rsquo;s customer list.",
    "So the moment the deal was announced, every one of those customers had to "
    "consider the possibility that their foundation was now owned by a rival who "
    "could see their roadmaps and set their costs. Qualcomm objected publicly. "
    "Others did so privately and at length to regulators in the United States, "
    "the United Kingdom and the European Union.",
   ]),
   ("Here is what was in the horse", [
    "The thing nobody in the announcement priced was that the asset could not "
    "survive being owned by that particular buyer. Not a regulatory risk in the "
    "ordinary sense, where you argue about market share. A structural one: the "
    "value of ARM was its independence, so a sale to any chipmaker destroyed some "
    "of what was being bought.",
    "ARM listed separately in 2023 instead and has traded at a multiple of the "
    "$40 billion NVIDIA offered, which is the most expensive compliment ever paid "
    "to an antitrust lawyer.",
    "SoftBank kept the $1.25 billion."]),
   ("My read", [
    "There is a question worth carrying out of this and it almost never appears "
    "in a model, because it has no number attached.",
    "Is any part of what you are buying made of the fact that you do not own it "
    "yet. Standards, platforms, benchmarks and marketplaces all have this "
    "property. They are valuable because they are trusted to be disinterested, "
    "and a disinterested asset held by an interested party is a smaller asset "
    "than it was the day before."]),
  ],
  takeaway=("Some assets are worth less the moment you own them, and no "
            "spreadsheet has a row for that."),
  srcs=["NVIDIA, SoftBank and Arm Limited, announced 13 September 2020, up to $40bn in stock and cash. Terminated 8 February 2022.",
        "NVIDIA retained no claim to the $1.25bn prepaid to SoftBank, which SoftBank recognised in its own results.",
        "Regulatory opposition in the US, UK and EU, and public objections from ARM licensees, were reported throughout 2021.",
        "Arm Holdings plc listed on Nasdaq in September 2023."]),

 dict(slug="the-price-machine", year="2022", roman="VII",
  lead="The", line1="Price", line2="Machine",
  sub="$61BN FOR A BUSINESS THAT IS NOT<br>GOING TO GROW, WHICH IS THE POINT",
  party="Broadcom / VMware", value="$61bn", dated="Announced May 2022",
  lede=("Broadcom agreed to buy VMware in May 2022 for about $61 billion in cash "
        "and stock, into a market that was falling apart around it. Rates were "
        "climbing, the Nasdaq was in the process of losing a third of its value, "
        "and financing anything was becoming difficult. It closed in November "
        "2023 after eighteen months of regulators."),
  sections=[
   ("What VMware does, briefly", [
    "VMware&rsquo;s core product lets one physical server behave as many "
    "separate computers. That sounds like a technicality and it is the reason "
    "corporate computing has looked the way it has for twenty years.",
    "It sits underneath an enormous amount of the software large companies run. "
    "Not visible, not exciting, and essentially impossible to remove without a "
    "project that would consume several years and somebody&rsquo;s career.",
   ]),
   ("The model, stated plainly", [
    "Broadcom is not a growth company and does not pretend to be. Its approach is "
    "consistent and it has worked for two decades.",
    "Buy infrastructure software that large customers cannot realistically leave. "
    "Cut the research spending and the smaller product lines hard. Move customers "
    "onto larger, longer, more expensive contracts. Return the cash.",
    "The industry is slightly squeamish about saying this out loud because it "
    "sounds like asset stripping. It is more precise than that. It is the "
    "observation that a product with genuine lock-in has been underpriced "
    "relative to what it is worth to the customer, and that nobody was going to "
    "fix that except an owner willing to be unpopular.",
   ]),
   ("Here is what was in the horse", [
    "Everyone read the deal as an enormous bet made at a terrible moment. The "
    "thing in the belly was that the moment did not matter very much, because the "
    "return was not coming from growth or from the cycle. It was coming from "
    "raising the price of something customers had already decided they could not "
    "leave.",
    "That is a return you can calculate before you sign. It is also why Broadcom "
    "could keep writing the cheque while the window shut on everybody else: it was "
    "not underwriting a forecast.",
    "Within a year of closing, VMware customers were describing very large "
    "increases in what they paid. Some left. Most did the arithmetic on leaving "
    "and stayed, which was always the number that mattered."]),
   ("My concern, and it is a real one", [
    "I want to be careful to separate what is observed from what I suspect.",
    "Observed: the model is legal, repeatable and extremely profitable, and "
    "shareholders have done exceptionally well out of it.",
    "My concern is narrower. A strategy that extracts from lock-in works until "
    "the memory of it changes behaviour, and enterprise buyers have very long "
    "memories. The cost of this does not appear in a quarterly number. It appears "
    "years later, in the deals a company is not invited to bid for."]),
  ],
  takeaway=("Most acquirers buy a forecast. This one buys the distance between "
            "what a customer pays and what leaving would cost them."),
  srcs=["Broadcom Inc. and VMware, Inc., announced 26 May 2022, approximately $61bn in cash and stock plus assumed debt. Completed 22 November 2023 following reviews in several jurisdictions.",
        "Broadcom's acquisition approach is described here from its public record across CA Technologies, Symantec's enterprise business and VMware, and from its own investor materials.",
        "Reported customer pricing increases following completion come from trade coverage and customer accounts rather than from company disclosure, and are characterised accordingly."]),

 dict(slug="reading-the-record", year="2023", roman="VIII",
  lead="Reading the", line1="Record", line2="",
  sub="IN THE QUIETEST YEAR FOR DEALS SINCE 2009,<br>CISCO PAID $28BN FOR LOG FILES",
  party="Cisco / Splunk", value="$28bn", dated="September 2023",
  lede=("Cisco agreed to buy Splunk in September 2023 for $157 a share in cash, "
        "about $28 billion. It was the largest acquisition Cisco had ever made, "
        "announced into the quietest year for technology dealmaking since the "
        "financial crisis, for a company whose product reads log files."),
  sections=[
   ("What a log file is", [
    "Every piece of software writes down what it just did. A user signed in here. "
    "This request failed. This server restarted at 4.12am. These notes are called "
    "logs and a large organisation produces an almost unimaginable quantity of "
    "them, nearly all of which nobody will ever read.",
    "Splunk collects all of it and makes it searchable. That is the product. It "
    "is the least glamorous sentence on this page.",
   ]),
   ("Why that is worth twenty-eight billion dollars", [
    "Two reasons, and the second is the interesting one.",
    "The first is security. When somebody breaks into a company, the evidence is "
    "in the logs, scattered across thousands of systems. Finding it means "
    "searching all of them at once. This category is called SIEM, security "
    "information and event management, and Splunk largely defined it.",
    "The second is that modern software is assembled from hundreds of small "
    "services written by different teams, and when something breaks, no single "
    "person understands the whole thing any more. The only way to know what "
    "happened is to read the record. The industry calls this observability, which "
    "is a long word for knowing what your own systems are doing.",
   ]),
   ("Here is what was in the horse", [
    "Cisco sells the network. The network sees every packet that moves. Splunk "
    "reads every record that is written. Put them together and you have a view of "
    "an organisation&rsquo;s actual behaviour that nobody else can assemble.",
    "The timing is the part worth noticing. This was announced in the first full "
    "year of the AI boom, when companies were connecting systems they did not "
    "fully understand to models they understood less. The amount nobody could "
    "account for went up sharply, and the company that reads the record quietly "
    "became strategic.",
    "Cisco paid cash in a year when cash was expensive and almost nobody else was "
    "buying anything."]),
   ("What I would watch", [
    "Whether Cisco can sell a software subscription to a customer base that has "
    "bought hardware from it for thirty years. That is a different motion and the "
    "graveyard of hardware companies attempting it is well populated.",
    "My read is that the asset was correctly identified and the integration is "
    "the open question, which is true of most large software acquisitions and is "
    "almost never what the announcement is argued about."]),
  ],
  takeaway=("In a year when nobody could say what their own systems were doing, "
            "the company that keeps the record turned out to be infrastructure."),
  srcs=["Cisco Systems, Inc. and Splunk Inc., announced 21 September 2023. $157.00 per share in cash, approximately $28bn in equity value. Completed March 2024.",
        "Splunk's position in security information and event management, and in observability, from the company's own filings and category coverage.",
        "The characterisation of 2023 as the weakest year for technology dealmaking since the financial crisis reflects reported league table volumes."]),

 dict(slug="third-in-line", year="2025", roman="IX",
  lead="Third in", line1="Line", line2="",
  sub="GOOGLE PAYS $32BN FOR SECURITY THAT<br>RUNS BEST ON ITS COMPETITORS",
  party="Google / Wiz", value="$32bn", dated="March 2025",
  lede=("In July 2024 Wiz walked away from a $23 billion offer from Google, "
        "citing antitrust and investor concerns, with annual recurring revenue "
        "above $500 million and a plan to go public. Eight months later it sold "
        "to the same buyer, facing the same antitrust problem, for $32 billion. "
        "Thirty-nine percent more money."),
  sections=[
   ("What Wiz does, in plain terms", [
    "When a company moves into the cloud, it creates thousands of small settings. "
    "Who can reach this database. Which machines can talk to which. What is "
    "exposed to the open internet, usually by accident.",
    "Wiz scans all of it and tells you which combinations are actually dangerous. "
    "Not a list of ten thousand warnings, which is what the previous generation "
    "of tools produced and which nobody reads. A short list of the paths an "
    "attacker could really walk.",
    "The reason people liked it is unglamorous and decisive: it worked in an "
    "afternoon rather than a quarter.",
   ]),
   ("Why Google wanted it so badly", [
    "Google Cloud has been a durable third behind Amazon and Microsoft for years, "
    "and third place in infrastructure is a specific kind of problem. You rarely "
    "win on price and you almost never win on features. You win when something "
    "forces a company to reopen a decision it made eight years ago.",
    "In practice the thing that forces that reconsideration is security.",
   ]),
   ("Here is what was in the horse", [
    "Wiz is deliberately multicloud, and Google committed publicly to keeping it "
    "working on Amazon, Microsoft and Oracle.",
    "Read that as strategy rather than good manners. Google did not buy a feature "
    "for its own cloud. It bought the security layer sitting above everybody&rsquo;s "
    "cloud, which means it now gets paid on the Amazon estate it was never going "
    "to win, and it holds the relationship with the security team, which is the "
    "team that gets consulted when workloads move.",
    "It is the same structural position IBM bought with Red Hat seven years "
    "earlier, for within two billion dollars of the same money."]),
   ("What the nine billion bought", [
    "The gap between the 2024 refusal and the 2025 agreement is the most "
    "instructive number here. Nothing about Wiz changed enough in eight months to "
    "justify $9 billion of additional value.",
    "My read is that the increase was not a revaluation of the asset. It was the "
    "price of removing an alternative. Wiz had a real one, an IPO, and a business "
    "growing fast enough to make it credible, and a seller with somewhere else to "
    "go is the only seller who gets paid properly.",
    "Whatever deal protections made an eighteen-month antitrust wait survivable "
    "for a company that had already said no once are in there too, and they are "
    "not public."]),
  ],
  takeaway=("The premium was not paid for the company. It was paid for the fact "
            "that the company did not have to sell."),
  srcs=["Google and Wiz, Inc., announced 18 March 2025, approximately $32bn in cash. Completed 2026 following regulatory review.",
        "Wiz ended earlier acquisition discussions with Google in July 2024 at a reported $23bn, citing antitrust and investor considerations, with reported ARR above $500m against $350m a year earlier.",
        "Google's public commitment to maintaining Wiz across other cloud providers is from the announcement.",
        "Wiz was private, so adviser roles and deal terms here rest on trade coverage rather than filings."]),

 dict(slug="fetching", year="2025", roman="X",
  lead="", line1="Fetching", line2="",
  sub="THE MOST EXPENSIVE PROCESSOR EVER BUILT<br>SPENDS A GREAT DEAL OF ITS LIFE WAITING",
  party="DDN / Blackstone", value="$300m at $5bn", dated="January 2025",
  lede=("Blackstone put $300 million into DataDirect Networks in January 2025 at "
        "a $5 billion valuation. DDN is not a startup. It was founded in 1998 "
        "and has spent a quarter of a century selling storage into supercomputing "
        "centres, in a market so unfashionable that almost nobody outside it "
        "could name a competitor."),
  sections=[
   ("The thing nobody says about a GPU", [
    "A GPU does not think slowly. It waits.",
    "Picture the most expensive processor ever manufactured at scale, sitting "
    "idle, because the data it needs to look at next has not arrived from storage "
    "yet. That is the constraint. Not intelligence. Not even electricity, though "
    "that is coming. Fetching.",
    "The bottleneck in artificial intelligence turns out to be the same one a "
    "library has, which is that it does not matter how many books you own if it "
    "takes forty minutes to find one.",
   ]),
   ("So the money went to the corridor", [
    "When Blackstone writes a cheque for the company that shortens the walk to "
    "the shelf, it is not investing in artificial intelligence. It is investing "
    "in the corridor.",
    "Corridors are historically where the durable money is. Nobody remembers who "
    "wrote the songs. Everybody remembers who owned the radio station.",
   ]),
   ("Here is what was in the horse", [
    "DDN was founded in 1998. So was Google.",
    "One of them became a verb. The other spent twenty-seven years quietly "
    "selling fast storage to national laboratories and weather modellers and "
    "genomics institutes. No keynote. No documentary.",
    "Then the machines got hungry, the unfashionable thing turned out to be the "
    "constraint, and a twenty-seven-year-old company woke up worth five billion "
    "dollars.",
    "I find this the best argument available against the idea that you have to be "
    "early. You have to be correct, and then you have to still be standing there "
    "when the world finally needs the thing you have been quietly good at the "
    "whole time. Patience is a strategy. It has terrible marketing."]),
   ("And the rest of the pattern", [
    "Once you see it you cannot unsee it. Cheap object storage raising at scale. "
    "Data protection being bought. Seagate, which makes the spinning platters "
    "everybody declared obsolete a decade ago, raising money on terms usually "
    "offered to growth companies.",
    "Hard drives were supposed to be dead. Flash was faster, had no moving parts, "
    "and that was meant to be the end of it. Then machines that read everything "
    "needed somewhere enormous and cheap to keep what they might want later, and "
    "slow but vast became a category again.",
    "Rust is back. Nobody put that on a slide in 2015."]),
  ],
  takeaway=("The capital markets have just told us, in the most expensive "
            "language available to them, what they think intelligence is made "
            "of. Not cleverness. The speed of the walk to the shelf."),
  srcs=["Blackstone, press release, 8 January 2025. $300m investment in DataDirect Networks at a $5bn valuation, via Blackstone Tactical Opportunities.",
        "DDN founding date, customer base and revenue ambition from Blackstone, DDN and contemporaneous trade coverage.",
        "Seagate's exchangeable note activity is confirmed in its own filings. Aggregate figures circulating on deal lists did not reconcile against those filings when I checked them, so this note describes the pattern rather than restating totals."]),
]
