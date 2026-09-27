"""Deal notes, written in Francis's voice.

Structure every piece is held to. The opening names the received reading and
then states one thesis. Every section after that advances the same thesis:
the evidence for it, the implication nobody draws from it, the strongest
argument against it. The call is the thesis converted into something
checkable. Nothing appears because it is interesting on its own.

No em dashes anywhere. Personal detail only where it is documented on his own
site (the supplement shelf, the bloodwork, the training, the AI for Business
degree). Nothing about his life is invented to warm the prose up.
"""

STORIES = [

dict(
 slug="buying-the-standard",
 lead="", line1="Buying", conn="the", line2="Standard",
 sub=("A STANDARD IS THE ONLY ASSET", "THAT COMPOUNDS WITHOUT A PRODUCT"),
 party="Databricks / Tabular", value="~$2B", dated="June 2024",
 opening="Every write up of this deal reached for the same joke. Two billion dollars, roughly forty people, do the division, marvel at the price per head. I ran it too, and then I decided the headcount is the least informative fact in the transaction. My thesis is simple: Databricks did not buy a company here, it bought the end of a standards war, and a standard is the only asset in enterprise software that compounds without anybody shipping a product.",
 sections=[
  ("The asset was never the forty people",
   ["Tabular was founded by the engineers who created Apache Iceberg while they were at Netflix. Iceberg is an open table format, the unglamorous plumbing deciding how enormous piles of data get organised so that different tools can read them.",
    "Databricks maintains Delta Lake, which was Iceberg's principal rival. So this was not a capability Databricks lacked and it was not forty engineers it could have hired one at a time for far less. It was the other side of a format war, bought together with the specific people whose names are the reason anybody trusts that format. Call it a talent deal and you have described the receipt instead of the purchase."]),
  ("Why a standard outruns a product",
   ["A product competes every year. A standard competes once, and then it collects. If the industry settles on Iceberg and Databricks sits outside it, every enterprise data decision for the next decade begins with a format Databricks does not influence. That is not a competitive disadvantage you can engineer your way out of, because you cannot out build a default.",
    "Which is why I think two billion is the cheap end of the range rather than the absurd one. You are not paying for revenue or headcount, you are paying to stop competing against your own standard and to put both formats under one roof. Notice too that Databricks has only ever confirmed a floor, that consideration exceeded one billion. A company thrilled with a price tends to name it. A company that would rather you discussed the strategy gives you a floor and lets the number find its own level, and I read that as consistent with a purchase that was never really about the money."]),
  ("The argument against my own thesis",
   ["If standards are the asset, then the value depends entirely on Iceberg staying a standard rather than becoming a product. Open formats are trusted precisely because no single commercial party steers them, and the largest commercial party in the category now employs the creators.",
    "I have seen no evidence of capture and I do not think it was the intent. But my thesis only holds while the format stays genuinely communal, which means the thing I am claiming is valuable is also the thing the acquisition puts at risk."]),
  ("My call",
   ["Cheap if Iceberg remains everybody's, expensive the moment it starts to look like Databricks'. The checkable version is whether the contributor base stays broad over the next few years or quietly narrows to one company, and that is something you can go and count rather than argue about."]),
 ],
 takeaway="A product competes every year. A standard competes once, and then it collects.",
 srcs=["Databricks announcement, Data and AI Summit, 4 June 2024. Databricks has publicly confirmed consideration above one billion dollars; the approximately two billion figure is from subsequent reporting and is not company confirmed.",
       "Tabular founding team and the origin of Apache Iceberg at Netflix, per the companies' own materials."]),

dict(
 slug="bought-then-freed",
 lead="", line1="Bought", conn="then", line2="Freed",
 sub=("YOU BUY THE LAYER ABOVE", "YOUR MOAT IN ORDER TO GIVE IT AWAY"),
 party="NVIDIA / Run:ai", value="~$700M", dated="December 2024",
 opening="The tidy version is that NVIDIA is buying up the AI stack layer by layer and Run:ai is one more brick in the wall. That framing is popular and I think it is backwards. NVIDIA released the software as open source almost immediately after closing, which is a strange way to hoard anything. This was never an accumulation. It was a purchase made in order to give the thing away, because a complement you control is a complement nobody else can turn into a weapon.",
 sections=[
  ("Orchestration sits above the moat, not inside it",
   ["NVIDIA agreed to buy Run:ai in April 2024 and closed that December after review by the Department of Justice and the European Commission. Reported price is around seven hundred million dollars, unconfirmed by either side.",
    "Run:ai orchestrates GPU workloads across Kubernetes clusters. It decides which job gets which slice of which chip and lets one physical GPU be shared rather than handed whole to a single task. GPUs are the most expensive objects in the building and they idle an embarrassing amount of the time, so orchestration is what turns a pile of hardware into a utility. Crucially it is a layer above the thing NVIDIA sells. It is a complement, not a product."]),
  ("Which is why free is the aggressive move",
   ["The correct play with a complement has been the same since Rockefeller was selling kerosene and giving away lamps. Make it free, abundant and excellent, because every gram of friction removed from the layer above arrives as demand in the layer you own.",
    "Free orchestration that runs anywhere still has to schedule onto something. So seven hundred million buys two things at once: certainty that the scheduling layer never becomes a rival's beachhead, and the removal of any commercial reason for anyone to build an alternative. Against that balance sheet the price is close to a rounding error, and I think it is the cheapest defensive purchase on my list. The accumulation story misses the strategy entirely, because the strategy is in the giving away."]),
  ("The argument against my own thesis",
   ["Commoditising your complement only works while the complement points back at you. Software that orchestrates GPUs generically also makes it easier to orchestrate somebody else's GPUs, and open source is not a one way door.",
    "My concern is that the openness protecting the moat today lowers switching costs tomorrow, and the parties most motivated to extend an open orchestrator are precisely those selling alternative silicon. I do not think that makes it a mistake. I think it is a price NVIDIA looked at and decided it could carry."]),
  ("My call",
   ["A good trade, and a clearer statement of strategy than the announcement managed. What I would watch is not adoption, which is guaranteed the moment a useful thing becomes free. It is who is contributing in three years, and what hardware those contributors happen to sell."]),
 ],
 takeaway="The strategy was never the buying. It was that they could afford to give it away.",
 srcs=["NVIDIA announcement of the agreement, April 2024; completion December 2024 following US and EU review.",
       "The approximately seven hundred million figure is from reporting and was not confirmed by either party; some accounts place it nearer eight hundred million."]),

dict(
 slug="the-missing-fifth",
 lead="The", line1="Missing", conn="", line2="Fifth",
 sub=("UNILEVER BOUGHT AN OPERATOR,", "NOT A BRAND. THE FIFTH PROVES IT"),
 party="Unilever / Gr&uuml;ns", value="~$1.2B", dated="June 2026",
 opening="I am not a neutral reader here and would rather say so first. I take around fifteen things every day, I read the mechanism on each before it goes in, and I get bloodwork drawn to check whether any of it does what it claims. So when Unilever completed its acquisition of Gr&uuml;ns on the first of June, another shelf in my own bathroom changed owner. I do not think Unilever bought a brand at all. It bought an operator, and the one fifth it deliberately left behind is the evidence.",
 sections=[
  ("The denominator nobody checked",
   ["Gr&uuml;ns was founded in 2023 by Chad Janis, sells a daily greens supplement in gummy form almost entirely by subscription, reached roughly three hundred million dollars of annual revenue in under four years, and was reported profitable inside about fourteen months. The deal came out around one point two billion dollars.",
    "Then nearly everyone ran the same sum. One point two over three hundred, four times sales, sensible bolt on, move along. Trade reporting places that consideration against eighty percent of the shares rather than all of them. If that holds, the whole company is nearer one and a half billion and the multiple is closer to five than four. I could not confirm the split in Unilever's own half year filing, which records completion and says nothing about terms, so I flag it rather than bank it. But the number is not the interesting part. The structure is."]),
  ("You do not leave a fifth behind by accident",
   ["A full turn of revenue is the distance between a bolt on price and a growth price. What explains paying a growth price and still not taking the whole thing?",
    "My read is that the retained fifth is a retention device, and that tells you what the asset actually was. Gr&uuml;ns is three years old, founder run, and the whole business is a subscription machine somebody has been operating with unusual discipline for a very short time. You do not buy that outright when what you need is for the operator to stay in the building. Unilever bought execution, and execution walks out of the door unless you give it a reason to stay."]),
  ("Which is exactly why I am watching the label",
   ["If the thesis is right, then everything I care about as a customer rests on the same fifth. A greens gummy is a formulation, and formulations get revisited. Under a founder the reason to change one is usually efficacy. Under a large consumer owner with a cost line to manage, the reason can be margin.",
    "So the retention device is not just a deal term, it is the thing standing between the product I buy and the ordinary gravity of a large portfolio. I have no evidence that anything has changed or is planned, and I want that stated plainly rather than implied. But my concern is specific and it has a date attached: not what happens now, but what happens when that fifth is finally bought and the founder has no remaining reason to defend the formula."]),
  ("My call",
   ["A good price for Unilever while the operator stays, which is a narrower dependency than four times revenue implies and narrower still at five. I would not watch revenue. I would watch for the announcement that the remaining stake has been acquired, because that is the moment the protection expires."]),
 ],
 takeaway="They bought execution, and execution walks out of the door unless you give it a reason to stay.",
 srcs=["Unilever Form 6-K, half year results to 30 June 2026, confirming completion in June 2026 and not stating terms.",
       "Consideration, revenue scale and the eighty percent stake are from trade reporting rather than the filing, and are treated here as reported rather than confirmed."]),

dict(
 slug="premium-without-profit",
 lead="", line1="Premium", conn="without", line2="Profit",
 sub=("THE PREMIUM MEASURES THE MARKET,", "NOT THE BUYER"),
 party="Mars / Hotel Chocolat", value="&pound;534M", dated="November 2023",
 opening="A hundred and seventy percent premium ends most arguments before they start. Half the coverage read it as Mars losing its mind and half as a triumph for shareholders, and both are lazy in the same way. A premium is not a measurement of the buyer. It is the distance between a price and a value, and when that distance gets this large the interesting party is usually the one who was wrong beforehand.",
 sections=[
  ("Start with the number you cannot use",
   ["Mars offered five hundred and thirty four million pounds in November 2023, three hundred and seventy five pence a share in cash, completing that January. In the financial year to July 2023 Hotel Chocolat had gone from a pre tax profit of twenty one point seven million pounds to a loss of eight hundred thousand.",
    "So earnings cannot value this, because at the moment of the offer there effectively were not any. That is the whole puzzle rather than a footnote. Any read starting from the premium is measuring out from a price the public market had already given up on, which makes the premium a statement about the starting point and not about Mars."]),
  ("What the market could not price",
   ["Look at what does exist. Hotel Chocolat was founded in 2004, sells through its own stores and its own website, and owns a hundred and forty acre cocoa estate and the Rabot Hotel in Saint Lucia. That is a business controlling its product from the tree to the till.",
    "Public markets are good at pricing earnings and poor at pricing structure, and vertical integration is almost pure structure. It shows up as cost while it is being built and as resilience only much later, so a loss making year makes it look like an expensive habit rather than an asset. Mars could price it because Mars knows exactly what it does not have: it is exceptional at moving volume through other people's shelves and has no premium brand with its own estate, its own retail and a direct line to the person eating the thing. You cannot assemble that in pieces. You buy somebody who already spent twenty years on it."]),
  ("The argument against my own thesis",
   ["If the structure is the asset, then the risk is that owning it changes it. The quality making Hotel Chocolat worth a premium is that it is small enough to control end to end, and every move to scale it, more stores, more countries, more volume through a finite estate, works against the thing that justified the price.",
    "My concern is not deliberate damage. It is that the instinct which makes Mars excellent is precisely the instinct that dissolves a vertically integrated premium business, and I have no evidence either way yet."]),
  ("My call",
   ["Defensible, and more interesting than the premium makes it sound. The metric is not sales growth, it is the share of sales still moving through Hotel Chocolat's own channels. If that falls while total sales climb, Mars bought the structure and then spent it."]),
 ],
 takeaway="Public markets price earnings well and structure badly, and this company was almost entirely structure.",
 srcs=["Mars offer announced 16 November 2023 at 375p per share; transaction completed 25 January 2024.",
       "Hotel Chocolat financial year to July 2023, pre tax result moving from a 21.7m profit to a 0.8m loss, per contemporaneous coverage of the company's results."]),

dict(
 slug="the-margin-gap",
 lead="The", line1="Margin", conn="", line2="Gap",
 sub=("A CUSTOMER ACQUISITION BUSINESS", "WEARING A FOOD LABEL"),
 party="Danone / Huel", value="~&pound;860M", dated="March 2026",
 opening="Direct to consumer brands love quoting gross margin and I have started reading that as a small act of misdirection. Huel's is fifty nine percent, which sounds like a software company wearing an apron. Its adjusted EBITDA margin the same year was about eight. Huel is not a food business. It is a customer acquisition business with a product attached, and what Danone bought is the right to stop paying for the acquisition.",
 sections=[
  ("Where the fifty one points go",
   ["I train for a half Ironman and race HYROX, so complete nutrition is a category I watch as a person and not only as somebody reading filings. Danone announced in March 2026 at around eight hundred and sixty million pounds and the CMA cleared it that August.",
    "In the year to 2024 Huel recorded two hundred and fourteen million pounds of revenue at a fifty nine percent gross margin and eighteen point two million of adjusted EBITDA. Revenue reached two hundred and fifty million the following year, up sixteen percent. Fifty nine percent of two hundred and fourteen is about a hundred and twenty six million of gross profit against eighteen of EBITDA, so roughly a hundred and eight million pounds, close to half of all revenue, leaves below the gross line. In a subscription business selling direct, the overwhelming share of that is the cost of finding the next customer. Huel is not expensive to make. Huel is expensive to sell."]),
  ("Which makes the synergy mechanical rather than cultural",
   ["I am ordinarily sceptical of synergy arguments because they are the easiest slide in any deck and the hardest line to find afterwards. This one is different for a structural reason. If the cost sitting between fifty nine and eight is distribution, then shelf space is a direct substitute for paid acquisition, and Danone happens to own shelf space in quantity.",
    "You are not hoping two organisations learn to collaborate. You are swapping a cost line for an asset the buyer already holds, which is the only kind of synergy I take seriously. And it gives a test needing no model at all: EBITDA margin should climb from eight toward the gross margin over three years. If it does, the thesis was right. If it has not moved, Danone bought revenue at a food multiple and inherited the advertising budget with it."]),
  ("The argument against my own thesis",
   ["The gap only closes if the loyalty survives the move. A brand built on a subscription relationship does not always hold up on a shelf beside eleven alternatives, and some of what looks like brand strength in those numbers may be a function of the format rather than the formula.",
    "If that is true then the acquisition cost was never really waste, it was the price of a relationship, and removing it removes the thing being bought. That is a hypothesis rather than a finding, and it is why I would watch subscriber retention as closely as the margin."]),
  ("My call",
   ["The best articulated thesis on my list and the easiest to grade, which are related virtues. Fifty nine into eight is the entire deal. Either Danone closes that gap or it did not need to own the company to find out."]),
 ],
 takeaway="Huel is not expensive to make. Huel is expensive to sell, and that is what changed hands.",
 srcs=["Danone announcement March 2026; CMA clearance August 2026; consideration of approximately 860m from reporting.",
       "Huel FY2024 revenue, gross margin and adjusted EBITDA, and FY2025 revenue, per company figures reported in trade coverage."]),

dict(
 slug="two-versus-six",
 lead="", line1="Two", conn="versus", line2="Six",
 sub=("THE MULTIPLE PRICES COPYABILITY,", "NOT GROWTH AND NOT CATEGORY"),
 party="L Catterton / Good Culture", value="&gt;$500M", dated="January 2026",
 opening="People discuss the wellness trade as though it were one thing you could be long or short, and this year handed me the cleanest disproof I am likely to get. One sponsor, one calendar year, two health brands riding the same demand, priced at roughly two times revenue going in and roughly six times coming out. The multiple in this category is not pricing growth, and it is not pricing the category. It is pricing whether somebody else can make the same thing.",
 sections=[
  ("A natural experiment I did not have to construct",
   ["In January 2026 L Catterton took a majority stake in Good Culture, the cottage cheese brand, at a reported value above five hundred million dollars. Good Culture did about a hundred million of revenue in 2023, close to double that in 2024, and was tracking near two hundred and fifty million in 2025, so roughly two times sales. Semcap Food and Nutrition added fifty five million that February.",
    "In August the same firm sold Thorne to Procter and Gamble at a reported three point eight billion against roughly six hundred and fifty million of forward revenue, about five point eight times. Same investor, same year, same broad bet that people are buying health. Four turns of difference."]),
  ("Two explanations that do not survive",
   ["Growth was my first instinct and it fails immediately. Good Culture roughly doubled. That is not a business being marked down for stalling.",
    "Category was my second and it fails too. Both are things people put in their body deliberately, sold on a health claim, riding the same protein and longevity demand, and if anything cottage cheese has had the louder cultural moment. So whatever produces a four turn spread is not the thing the category label names, which is my central objection to talking about a wellness trade at all."]),
  ("What is left is copyability",
   ["Cottage cheese is a refrigerated commodity with a cold chain, a short shelf life and a private label version on the same shelf at a lower price. A competitor can match the product. The brand is real and the execution is plainly excellent, but the moat is thin by construction and no amount of growth thickens it.",
    "Thorne's moat was a practitioner willing to say the name out loud to a patient who was frightened. You cannot private label that and you cannot rebuild it once spent. Four turns of revenue is the price of that difference, and it is a far more useful number than anything in the category commentary."]),
  ("The argument against my own thesis",
   ["I may be reading a sponsor's portfolio timing as a market judgement. L Catterton bought one asset and exited another, and exit timing owes as much to fund cycles and a closed IPO window as to anything I am claiming about moats.",
    "I would rather raise that than have it raised for me. It does not fully defeat the read, because a fund cycle explains when you choose to sell and not what somebody is willing to pay when you do, but it is the strongest thing anyone could say against me."]),
  ("My call",
   ["Two was right for Good Culture and six was right for Thorne. If you want to know what a consumer health brand is worth, do not ask how fast it is growing. Ask whether somebody could make it for less, and whether anyone would notice."]),
 ],
 takeaway="Ask whether somebody could make it for less, and whether anyone would notice. That is the multiple.",
 srcs=["L Catterton majority investment in Good Culture announced January 2026, reported above 500m; Semcap Food and Nutrition investment of 55m, February 2026.",
       "Good Culture revenue scale from trade coverage. Thorne figures as set out in my separate note on that transaction."]),

dict(
 slug="owning-the-clock",
 lead="", line1="Owning", conn="the", line2="Clock",
 sub=("A BENCHMARK OWNED BY THE VENDOR", "STOPS BEING EVIDENCE"),
 party="Infinite Epigenetics / Tally Health", value="Undisclosed", dated="April 2026",
 opening="When terms are not disclosed the reflex is to assume the deal was small and move on, and I have stopped doing that, because undisclosed is a decision somebody made rather than an absence of information. On the twenty ninth of April 2026 Infinite Epigenetics acquired Tally Health in an asset purchase. The asset here was never the supplements, or even the brand. It was the benchmark, and a benchmark owned by the vendor quietly stops functioning as evidence.",
 sections=[
  ("Read what actually changed hands",
   ["I get bloodwork drawn specifically to check whether the things I take do what they claim, which makes me the customer this deal is about, so I read the announcement twice.",
    "Tally Health was co founded in 2023 by the Harvard geneticist David Sinclair and sells an epigenetic biological age test alongside a supplement line. The buyer also owns TruDiagnostic and states it holds among the largest private datasets of adult DNA methylation. Tally continues as a standalone brand under Melanie Goldey. The obvious description is that a longevity company bought a longevity company. My read is that what moved was a methylation dataset and a competing clock, and the supplements came along attached to them."]),
  ("A clock is a model, so owning it means defining the year",
   ["Biological age is not a measurement the way height is a measurement. It is a model. Somebody decides what counts as a year, which markers matter, and what the reference population looks like. Two clocks can read the same blood and disagree, and neither is lying.",
    "This is where I would push back on how the field talks about itself, because a biological age result is handed to consumers with the confidence of a bathroom scale and is nothing of the kind. If you already hold the largest reference dataset and then buy the most consumer visible rival clock, you have not added a product to a catalogue. You have consolidated the definition, and every longevity intervention hoping to claim it works eventually validates against somebody's clock. There is now one fewer somebody."]),
  ("Which is precisely the problem with my own bloodwork",
   ["Follow the thesis to where it lands on me. If the benchmark is the asset, then the company selling the intervention now owns the instrument grading whether the intervention worked, and the number I am paying for stops being independent evidence and becomes a number with an interest in the answer.",
    "I want to be careful and precise. I have no evidence of manipulation, nothing in the announcement suggests any such intent, and vertical structures like this are ordinary in diagnostics and not improper in themselves. But independence is not a bonus feature of a benchmark. It is the entire reason a benchmark means anything, and it is a strange thing to own both sides of."]),
  ("My call",
   ["The most strategically interesting deal on my list and the one carrying the least public information, which I do not think is unrelated. The test is narrow and checkable. Does Tally's test keep reporting on its own clock, or does it quietly migrate onto TruDiagnostic's? That single answer separates a portfolio addition from a consolidation of the definition, and I know which way I am leaning."]),
 ],
 takeaway="Independence is not a feature of a benchmark. It is the entire reason a benchmark means anything.",
 srcs=["Infinite Epigenetics announcement of the Tally Health asset purchase, 29 April 2026. Terms not disclosed by either party.",
       "Tally Health founding, leadership and product scope, and Infinite Epigenetics' ownership of TruDiagnostic, per the announcement."]),

]
