"""The written pieces that sit under the Tech Atlas chart.

One opening piece on how to read the board, then one per sector. Warm and
story-led, anchored in a decision someone had to make, using only facts that are
in the atlas data. Quotations are short, attributed and linked. No em dashes,
no semicolons, no rhetorical questions.
"""

INTRO = [
 "This is a depth chart for the whole technology industry. The idea comes from "
 "football, where a coach lists each position and ranks the players who could "
 "fill it. Here every row is a position in the stack, such as AI accelerators, "
 "foundries or customer service software. Each row has three tiers. The "
 "starters are the companies winning today, measured by a number with a date "
 "and a source. The second string holds credible challengers, with shipping "
 "product or named customers behind them. The practice squad holds startups "
 "that have raised real money.",
 "The lines are the part I enjoy most. A solid line joins companies that "
 "supply or ally with each other, a dashed line joins rivals, and an arrow "
 "runs from an owner or an investor to the company it holds. Click a card to "
 "see its lines, including the ones that cross into other sectors, because "
 "those usually explain the most. A chip supplier who invests in its own "
 "customer is telling you something, and so is a cloud that rents capacity to "
 "a rival.",
 "Every number carries its source, and a small tag says how far to trust it. "
 "Sourced means a company filing or release, or a named research firm. Reported "
 "means credible press coverage without the document in hand. Inferred means "
 "the line is my reading of the structure and no source states it. The figures "
 "are as of 23 October 2026, and markets in this industry move faster than "
 "that date suggests.",
]

SECTOR_PIECES = {

 "silicon": [
  "Start at the buyer's side of the table, because that is where the leverage "
  "moved. In October 2025 OpenAI, which has no chip factory, announced two "
  "supply deals in a week. AMD agreed to supply 6 gigawatts of GPUs and "
  "gave OpenAI a warrant for up to 160 million of its own shares, vesting as "
  "the purchases scale "
  "(<a href=\"https://ir.amd.com/news-events/press-releases/detail/1260/amd-and-openai-announce-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus\">AMD</a>). "
  "A week later OpenAI and Broadcom said they would deploy 10 gigawatts of "
  "accelerators that OpenAI had designed itself "
  "(<a href=\"https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/\">OpenAI</a>).",
  "Nvidia's own offer had come first, a letter of intent for 10 gigawatts and "
  "up to $100 billion of investment. Months later Nvidia's finance chief said "
  "“We still haven't completed a definitive agreement,” and Jensen Huang called "
  "the pledge “never a commitment” "
  "(<a href=\"https://fortune.com/2025/12/02/nvidia-openai-deal-not-signed-yet-100-billion-rally-colette-kress/\">Fortune</a>, "
  "<a href=\"https://fortune.com/2026/02/02/jensen-huang-nvidia-ceo-on-openai-investment-never-a-commitment/\">Fortune</a>). "
  "Put the three side by side and a buyer's strategy shows. A customer that "
  "can threaten to design its own chip gets suppliers to bid with equity. AMD "
  "welcomed a very large order and handed over a share of itself to win it, "
  "and the risk that came in with the order is a customer that now owns part "
  "of its supplier.",
  "Look down the rest of the chart for the bottlenecks. TSMC makes 72.5% of "
  "the top ten foundries' revenue. SK hynix holds about half of high-bandwidth "
  "memory, though Samsung's share is rising as its next generation ships. ASML "
  "is the only company that makes the extreme ultraviolet machines every "
  "leading-edge fab needs. Where the chart shows one name at a chokepoint, "
  "that company sets terms for everyone above it.",
  "The challengers worth watching change the premise of the row. Cerebras "
  "builds one chip from an entire wafer, and went public in May 2026. "
  "Substrate is trying to replace the light source in lithography with a "
  "particle accelerator that writes with X-rays, and it has money and no "
  "revenue. In China, Huawei already ships 28% of AI chips to Nvidia's 34% "
  "(IDC, as reported). The orders to watch are the 14A decisions at Intel "
  "Foundry in the next two quarters, the first racks of OpenAI's own chips, and "
  "the volume ramp of AMD's MI450.",
 ],

 "infra": [
  "Every part of this sector is a queue. GE Vernova has gas turbine slots "
  "reserved into 2030, with 56 gigawatts of reservations on its books. Dell "
  "ended its last fiscal year with a $43 billion backlog of AI servers, and "
  "IDC says supply, not demand, is what holds server shipments back. Equinix "
  "summed up its quarter with the line that “the vast majority of our largest "
  "deals were driven by AI workloads” "
  "(<a href=\"https://investor.equinix.com/news-events/press-releases/detail/1114/equinix-reports-second-quarter-results-raises-2026\">Equinix</a>). "
  "A queue is a good place to study strategy, because the ones in line are "
  "deciding who they are willing to pay to move up.",
  "Money is the clearest example. Meta needed a gigawatt-scale campus in "
  "Louisiana and agreed a joint venture in which Blue Owl funds hold 80% and "
  "Meta 20%. Meta leases the buildings and provided a guarantee for the first "
  "sixteen years "
  "(<a href=\"https://www.prnewswire.com/news-releases/meta-announces-joint-venture-with-funds-managed-by-blue-owl-capital-to-develop-hyperion-data-center-302590584.html\">Meta</a>). "
  "Meta welcomed that capital because it let the campus be built faster and "
  "kept most of the cost off its own balance sheet. The risk that rode in with "
  "it is a long guarantee that stays with Meta if demand disappoints. The "
  "<a href=\"horse-credit.html\">first horse on the Trojan Horses page</a> "
  "describes how private credit enters a bank's relationships in much the same "
  "way.",
  "Power gets bought the same way, years ahead. Meta signed three nuclear "
  "deals that support up to 6.6 gigawatts and prepaid Oklo, with a first phase "
  "targeted for 2030. Amazon's deal with X-energy could reach 5 gigawatts by 2039. A buyer "
  "that pays up front to get something built has taken on some of the "
  "builder's risk, which is the same arrangement as Renesas's deposit to "
  "Wolfspeed "
  "(<a href=\"desk-wolfspeed.html\">that case</a>).",
  "The networking row holds a quieter shift. Ethernet has moved from under a "
  "fifth of AI cluster switch sales to about two-thirds, and Celestica, which "
  "builds to the cloud buyers' own designs, led the second quarter ahead of "
  "Nvidia. The startup to watch is Ayar Labs, which wants to replace copper "
  "links between chips with light. In storage, VAST Data's $30 billion "
  "valuation beside DDN's $5 billion shows how far investors will pay for the "
  "fastest-growing name in a row with no audited share figure.",
 ],

 "cloud": [
  "On a September morning Oracle reported that its remaining performance "
  "obligations, the contracted revenue it has yet to deliver, had reached $664 "
  "billion. In the same release its free cash flow for the quarter was "
  "negative $5 billion "
  "(<a href=\"https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/\">Oracle</a>). "
  "A company long known for databases has signed the largest AI contracts in "
  "the industry and is paying for the buildings before the revenue arrives. Analysts estimate OpenAI is about half of that backlog, so "
  "Oracle has made a very large bet on one customer's ability to keep paying.",
  "Google took the opposite route. Its cloud grew 82% in the June quarter and "
  "carries a reported $514 billion backlog, and it sells its own chips and its "
  "own models alongside the rental. Amazon still leads on share at 28% and "
  "grew AWS 37%, its fastest in eighteen quarters. Microsoft's Azure grew 43% "
  "and its commercial backlog is reported at $678 billion. The three are "
  "growing at the same time, which is unusual, and it tells you the demand "
  "behind them is a shortage of capacity and not a contest for customers.",
  "That shortage built a new tier. CoreWeave rents Nvidia systems to the buyers "
  "who cannot build quickly enough, and its customers include Meta, OpenAI "
  "and Microsoft, which was about 67% of its 2025 revenue. Nebius holds long "
  "contracts from Microsoft and Meta. A landlord for the biggest tenants is a "
  "strong business while the shortage lasts, and the interest bills show the "
  "cost. CoreWeave paid $640 million of net interest in one quarter.",
  "The practice squad is full of companies selling inference, the "
  "serving of finished models to developers. Fireworks AI and Together AI both "
  "raised at valuations above $8 billion this summer, and Wasabi's no-exit-fee "
  "storage shows a different premise, selling the customer's freedom to leave "
  "(<a href=\"desk-wasabi.html\">that case</a>). The test for the whole sector "
  "is conversion. A backlog counts promises, and the quarters ahead show how "
  "many of them become revenue.",
 ],

 "models": [
  "February 2026 was the month the labs became public-company-sized. SpaceX "
  "bought xAI in an all-stock deal that closed on the 2nd. OpenAI's $122 "
  "billion round followed, at an $852 billion valuation, with Amazon "
  "committing $50 billion and Nvidia and SoftBank $30 billion each "
  "(<a href=\"https://news.bloomberglaw.com/tech-and-telecom-law/openai-valued-at-852-billion-after-closing-122-billion-round\">Bloomberg Law</a>). "
  "Then Anthropic raised $65 billion at $965 billion in May and told "
  "investors its annualized revenue had reached $65 billion by July "
  "(<a href=\"https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html\">CNBC</a>). "
  "These valuations are reported, and the point is the ordering underneath "
  "them. Menlo Ventures' survey put Anthropic first in enterprise spending at "
  "about 40%, ahead of OpenAI at 27% and Google at 21%, while Google's Gemini "
  "app passed 950 million monthly users.",
  "Anthropic's strategy is to be the neutral buyer. It can use up to a million "
  "Google TPUs, trains on Amazon's Trainium, has signed for up to two "
  "gigawatts of AMD's chips and still uses Nvidia. Each supplier welcomes the "
  "order, and none of them owns the customer. That position gives it a "
  "bargaining advantage the single-supplier labs lack, and it explains why "
  "chipmakers and clouds are also its investors.",
  "The companies building on the labs sit in a harder spot. Cursor's coding "
  "editor buys models from the labs that also sell coding tools, and Menlo "
  "estimated Anthropic at 54% of coding model spending. Perplexity competes "
  "with Google Search while depending on others' models. These businesses "
  "were welcomed by developers for what they add, and the risk inside them is "
  "that their suppliers can become their competitors.",
  "Two names are listed as practice squad that raise a different question. "
  "Safe Superintelligence is valued near $32 billion with no product revenue. "
  "Thinking Machines has a confirmed $12 billion seed valuation and several "
  "unconfirmed reports above it. Open-weight models from DeepSeek were "
  "reported to take 24.4% of text requests on one developer marketplace in a "
  "September week. The thing to watch is whether the frontier stays closed.",
 ],

 "software": [
  "In February the software industry was told, by the market, that it had a "
  "problem. Commentators put the selloff at about $285 billion, the fear being "
  "that AI agents would do the work that companies paid seats to do. A seat is "
  "a license for one human, and an agent is not a human. Vendors answered "
  "within months. Salesforce began selling agent actions at about ten cents "
  "each, according to commentary, and its Agentforce business reached more than $1.5 billion of annual "
  "recurring revenue, up over 240% "
  "(<a href=\"https://valueaddvc.com/pulse/salesforce-agentforce-1-5-billion-arr-benioff-2026\">reported</a>).",
  "The incumbents' strategy is to own the data and the workflow that agents "
  "need to act inside. ServiceNow's subscription revenue grew 24.5% in the "
  "June quarter. SAP's cloud backlog grew 27%. Microsoft says it has "
  "more than 30 million paid Microsoft 365 Copilot seats, up from 15 million in "
  "January "
  "(<a href=\"https://techcrunch.com/2026/01/29/satya-nadella-insists-people-are-using-microsofts-copilot-ai-a-lot\">TechCrunch</a>, "
  "reported). Each of these companies welcomed the "
  "agent because it is a new product line. The risk that came with it is that "
  "every agent that finishes a task is one less seat to bill.",
  "The startups sell the outcome and skip the seat. Sierra raised $950 "
  "million at a valuation above $15 billion to resolve customer-service "
  "issues, and Harvey, Decagon and Glean are doing the same in law, support "
  "and search. Meanwhile Databricks closed $5 billion at $190 billion in "
  "August, and Palantir is growing at 92.8%, which shows the money is "
  "following the platforms where data and models meet.",
  "Private equity is watching the same repricing. Silver Lake is reported in "
  "talks to take Workday private at a value above $51 billion, and Thoma Bravo "
  "completed Dayforce in February. The question for the second half of the "
  "year is whether agent revenue replaces seat revenue fast enough, and "
  "Workday's slowing total backlog is the number to keep an eye on.",
 ],

 "security": [
  "Security used to be a market of dozens of products and one overworked "
  "buyer. In 2026 the buyers are consolidating the sellers. Google closed its "
  "Wiz purchase on 11 March at about $29.5 billion after adjustments "
  "(<a href=\"https://abc.xyz/investor/news/news-details/2026/Google-Completes-Acquisition-of-Wiz-2026-ta7OaU2uA0/default.aspx\">Alphabet</a>). "
  "Palo Alto Networks completed CyberArk in February to “Secure the AI Era,” "
  "as its release put it. ServiceNow agreed to pay $7.75 billion for Armis and "
  "CrowdStrike reportedly paid $740 million for an identity startup.",
  "The thinking behind each purchase is the same. A chief security officer "
  "wants fewer vendors and one place to answer for a breach, so the vendor "
  "that sells the most modules to the same customer wins the renewal. Palo "
  "Alto's next-generation security ARR is $9.10 billion, up 63%, and part of "
  "that growth was bought. CrowdStrike sells flexible credits that a customer "
  "can spend across modules, and Falcon Flex accounts now exceed $2.29 billion "
  "of ARR.",
  "Identity is where the new fight is, because AI agents need identities and "
  "permissions as people do. Okta says more than 90% of its customers run "
  "agents in production and only 22% are confident the agents are controlled, "
  "which is a company-reported figure with an obvious interest behind it. "
  "CyberArk now sits inside Palo Alto, and CrowdStrike bought SGNL, so Okta "
  "is competing against platforms that treat identity as one module among "
  "many.",
  "The Wiz case shows a promise that does real work. Google committed to keep "
  "the product available on AWS, Azure and Oracle Cloud, and that is what "
  "keeps its value as a neutral layer "
  "(<a href=\"third-in-line.html\">the note on that deal</a>). The startups "
  "to watch are Island, valued at $6.4 billion, and Cyera, reported at $12 "
  "billion, both selling a control point that the platforms do not yet own.",
 ],

 "internet": [
  "Meta's second quarter is a good place to see how ads work now. Its "
  "advertising revenue rose 27% to $59.36 billion, on an audience that grew 3% "
  "to 3.60 billion daily people. Impressions rose 14% and the price of each ad "
  "rose 12%, so it earned far more from the same people by showing them "
  "better matches (secondary report). Google's near 90% of search referral "
  "traffic and Amazon's $19.8 billion of ads belong to the same story, the "
  "three companies sell access to attention at the moment of intent.",
  "Streaming shows what happens when the attention is already crowded. "
  "YouTube reached a record 14.2% of US television time in July, the largest "
  "single service, while Netflix held 7.9% in June. Netflix's operating margin "
  "was 34.6% in its latest quarter and it still cut its ad target to $2.7 "
  "billion and about 1,000 jobs "
  "(<a href=\"https://www.sec.gov/Archives/edgar/data/0001065280/000106528026000290/ex991_q326.htm\">Netflix</a>). "
  "On 6 October Paramount closed its $31 a share cash purchase of Warner "
  "Bros. Discovery, a scale answer to the same pressure.",
  "TikTok's US venture closed in January, with Oracle, Silver Lake and MGX "
  "holding 15% each and ByteDance keeping 19.9%. Daily US use held near 95% of "
  "earlier levels. Each new owner welcomed the user base, and the thing to "
  "watch is whether the recommendation system stays as good under their "
  "control.",
  "The sector's open question is what happens when the buyer is an AI agent. "
  "Shopify reported $115.6 billion of volume, up 32%, with AI-driven orders "
  "tripling from a small base. Google's AI Mode passed a billion monthly "
  "users. Roblox, at the other end, saw bookings slow to 8% as spending per "
  "hour fell. The chart's first row shows who earns the ad dollar today. The "
  "rows beneath it show who is trying to move where the question gets asked.",
 ],

 "devices": [
  "The most surprising line on this chart connects a phone to a memory chip. "
  "IDC counted 276.3 million smartphones shipped in the second quarter, down "
  "7.4%, and described a memory crisis that is disrupting the market with "
  "unprecedented costs and strained supply "
  "(<a href=\"https://www.biztechreports.com/news-archive/2026/8/6/global-smartphone-shipments-fall-67-in-q2-2026-as-the-memory-crisis-splits-the-market-in-two-idc-august-11-2026\">IDC, as reported</a>). "
  "It expects 2026 shipments to fall 16.7%, the steepest drop on record, as the "
  "average price rises 27.6% to $581. The DRAM that AI data centers are "
  "buying in bulk is the same DRAM that goes into the phone.",
  "In a shortage the strongest brand gets the supply. Samsung and Apple were "
  "the only top-five phone makers to grow, with Samsung up 8.1% and Apple up "
  "14.9%, while Xiaomi, OPPO and vivo fell between 17% and 26% in one "
  "IDC-based table. Samsung also "
  "makes memory, which gives it a second way to win. In PCs the same split "
  "appears. IDC counted 68.2 million shipments, down 4.9%, and Apple was the "
  "only major maker to grow, up about 10% with its new MacBook Neo.",
  "The category that is growing is the one nobody had to buy a new phone for. "
  "Smart glasses and headsets grew about 35% in the quarter, with glasses at "
  "nearly 85% of the category. Meta holds roughly 69% to 76% of smart "
  "glasses, depending on the source, and EssilorLuxottica sold more than 7 "
  "million of the Meta-branded pairs in 2025. Meta paused the international "
  "launch of its Ray-Ban Display glasses because United States demand was "
  "backlogged.",
  "Google and Samsung plan Android XR glasses for the fall, with no confirmed "
  "date. The row to watch is how long memory stays scarce. IDC expects the "
  "shortage to last into early 2028, which means the device makers' margins "
  "depend on suppliers in a different sector.",
 ],

 "telecom": [
  "SpaceX's third quarter holds a line worth rereading. Revenue was $14.6 "
  "billion, up 161%, and the largest business was AI at $7.56 billion, ahead of "
  "Starlink's $5.25 billion of connectivity revenue (reported). The company "
  "that began by landing rockets now sells more through its AI division than "
  "through the satellites it launched. Starlink itself reached 13.6 million "
  "subscribers across 174 markets, adding 1.6 million in the quarter.",
  "On the ground, the carriers are building fiber to keep customers. AT&T "
  "added 442,000 fiber customers and 379,000 postpaid phone customers in the "
  "third quarter, and plans more than 60 million fiber locations by 2030. Its "
  "debt reached $159.6 billion, which coverage ties partly to spectrum "
  "purchases "
  "(<a href=\"https://about.att.com/story/2026/3q-earnings.html\">AT&T</a>). "
  "Verizon, after years of losing subscribers, posted its first positive "
  "first-quarter postpaid phone net adds since 2013 and was due to report on "
  "26 October.",
  "In mobile network equipment, Huawei and Ericsson held nearly two-thirds "
  "of the market in late 2025, and the top five suppliers hold 96% "
  "(<a href=\"https://www.delloro.com/news/ran-market-growth-continues-in-2q-2026/\">Dell'Oro</a>). "
  "The market is flat, which turns every point of share into a fight, and "
  "Nokia lost ground to Huawei outside China between 2019 and 2025.",
  "At the network edge, Cloudflare grew revenue 36% to $696.1 million and "
  "raised its guidance, while its gross margin fell 3.2 points as paid traffic "
  "grew. The thing to watch is whether satellites, fiber and cloud edge "
  "networks end up as three suppliers to the same customer or three rivals "
  "for the same dollar. Telecom is the sector where this research found the "
  "least verified 2026 data, and the chart says so on the cards.",
 ],
}
