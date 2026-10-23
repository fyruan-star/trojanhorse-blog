"""Background. Five explanations the Ten Years entries rely on.

Each one states what it claims first, explains the mechanism that supports the
claim, names the qualification that limits it, and says what a reader should
check when the subject comes up in a deal. Sources are linked beside the
claims they support. The word list at the foot of each piece is a glossary.

No em dashes, no semicolons.
"""

PRIMERS = [

 dict(
  slug="what-a-chip-is", roman="I",
  lead="What", line1="A Chip", line2="Is",
  sub="Design, licensing and manufacturing are three separate businesses",
  lede=("A chip is designed, licensed and manufactured by different "
        "companies, and the manufacturing step is concentrated in so few "
        "places that governments treat it as a matter of national capability. "
        "That concentration is why regulators appear in several of the "
        "semiconductor entries in Ten Years, and it is the background a reader "
        "needs to see what each of those buyers was acquiring."),
  sections=[
   ("Three businesses", [
    "A semiconductor is a piece of silicon with a very small circuit printed "
    "on it. Billions of switches, each on or off, are arranged so that "
    "setting them in the right order performs arithmetic. Three kinds of "
    "company are involved in making one.",
    "The first owns the architecture, which is the instruction set, the basic "
    "vocabulary a processor understands. Arm licenses this and manufactures "
    "nothing, and it receives a royalty on each chip built with its design. "
    "The second does the design, which is the specific layout of the chip. "
    "Nvidia, Apple and Qualcomm do this work and own no factories. The "
    "industry calls such a company fabless, and it is a business model and "
    "not a criticism. The third does the manufacturing, in a fabrication "
    "plant called a fab. A plant able to make the smallest features costs "
    "upward of twenty billion dollars and takes years to build.",
   ]),
   ("Why manufacturing concentrates", [
    "Each generation of equipment costs more than the last, until only a "
    "handful of firms can afford to remain at the leading edge. The machines "
    "that print the smallest circuits use extreme ultraviolet light, and one "
    "company, ASML in the Netherlands, makes them. Each machine costs on the "
    "order of hundreds of millions of dollars, and the figure depends on the "
    "generation "
    "(<a href=\"https://www.cnbc.com/2022/03/23/inside-asml-the-company-advanced-chipmakers-use-for-euv-lithography.html\">CNBC</a>).",
    "The largest manufacturer by a considerable margin is TSMC, in Taiwan. "
    "Estimates of its share of the most advanced logic chips cluster around "
    "90 percent, although sources define “most advanced” differently and the "
    "figure moves with the definition "
    "(<a href=\"https://eetasia.com/inside-taiwans-semiconductor-supremacy\">EE Times Asia</a>). "
    "A large share of the world's most advanced chips is therefore made in "
    "one place, and that place is the subject of an unresolved territorial "
    "dispute.",
   ]),
   ("Why governments became parties to deals", [
    "The policy question is not whether chips are useful. It is whether a "
    "country can obtain them if relations deteriorate. That question explains "
    "why a committee reviewing foreign investment was able to stop a takeover "
    "in 2018, why export controls now cover equipment most people could not "
    "identify, and why several governments have committed large sums to "
    "building manufacturing capacity at home. The United States, for example, "
    "passed the CHIPS and Science Act in 2022 to fund domestic fabs.",
    "The qualification is that concentration at manufacturing does not apply "
    "equally to every chip. Many chips used in cars and appliances are made "
    "on older equipment by many producers. The national capability argument "
    "is strongest for the leading edge, and weaker for the rest.",
   ]),
   ("What a reader should take from it", [
    "When a semiconductor deal is announced, identify which of the three "
    "businesses is being bought, then check where the manufacturing happens "
    "and who owns the equipment. A design company, an architecture licensor "
    "and a manufacturer face different regulators, different customers and "
    "different risks. The development that would change this picture is a "
    "second or third source of leading-edge manufacturing in a different "
    "country, which would reduce the concentration the rest of this "
    "reasoning depends on.",
   ]),
  ],
  takeaway="",
  words=[
   ("Semiconductor", "A chip. Silicon with a circuit printed on it."),
   ("Architecture", "The instruction set a processor is built around. Arm licenses this."),
   ("Fabless", "A company that designs chips and owns no factory."),
   ("Foundry", "A company that manufactures chips it did not design. TSMC is the largest."),
   ("Fab", "A fabrication plant. A leading-edge one costs tens of billions."),
   ("Node", "The size of the features being printed. Smaller is faster and harder to produce."),
  ]),

 dict(
  slug="what-the-cloud-is", roman="II",
  lead="What", line1="The Cloud", line2="Is",
  sub="Renting computing created lock-in, and lock-in is the asset",
  lede=("The cloud is computing that a company rents by the hour from a "
        "provider that owns the machines. I think the most valuable result of "
        "that arrangement for the providers is lock-in, the cost a customer "
        "would face to leave, and that it explains why buyers pay large "
        "premiums for software that works across all of the providers. IBM's "
        "purchase of Red Hat and Google's purchase of Wiz are two examples."),
  sections=[
   ("What changed in 2006", [
    "Before the cloud, a company that needed computing bought computers, "
    "housed them, employed people to maintain them and paid up front for "
    "capacity it would mostly not use. Amazon, which had built a large amount "
    "of capacity for its retail business, began renting storage in March 2006 "
    "and computing capacity a few months later "
    "(<a href=\"https://aws.amazon.com/blogs/aws/eight-years-and-counting-of-cloud-computing/\">AWS</a>). "
    "Microsoft and Google followed.",
    "In accounting terms a large one-off purchase became a monthly expense. "
    "That changed who could start a software company. Two founders could "
    "rent the same capacity as a bank and pay only for what they used, and a "
    "great many software companies founded afterward exist in a form that "
    "would not have been affordable before.",
   ]),
   ("Why customers stay", [
    "Amazon arrived first and remains the largest. Microsoft came second and "
    "already sold software to most large organizations. Google has been third "
    "for most of the period the timeline covers. Once a company's systems and "
    "data are established with one provider, moving them is a project and not "
    "a decision. It takes a long time, costs a great deal and visibly "
    "improves little when it is finished.",
    "The term for this is lock-in. A hypothetical customer with five hundred "
    "applications built for one provider's services would have to rewrite or "
    "retest each one to move. The provider's most valuable asset is the size "
    "of that bill.",
   ]),
   ("Multicloud and the neutral supplier", [
    "Larger customers recognized their position and began keeping systems with "
    "more than one provider deliberately, so that no single supplier could "
    "raise prices without a credible response. The practice is called "
    "multicloud. It creates a position worth having for a software supplier "
    "whose product works across all three providers, because that supplier "
    "earns revenue regardless of which one a customer chooses.",
    "IBM paid about $34 billion for a company in that position in 2018, and "
    "Google agreed to pay about $32 billion for another in 2025. Both "
    "purchases are about owning a neutral layer, and both carry the same risk, "
    "which is that the buyer is also a cloud provider and may weaken the "
    "neutrality it paid for.",
   ]),
   ("The qualification", [
    "Lock-in is eroding at the edges. Google announced in January 2024 that "
    "it would waive data transfer fees for customers leaving its cloud, and "
    "Amazon and Microsoft followed within about two months. Reporting links "
    "the moves to new European Union rules, and the waivers carry conditions, "
    "so the change is partial "
    "(<a href=\"https://www.theregister.com/2024/01/11/google_cloud_egress_fees/\">The Register</a>, "
    "<a href=\"https://www.lightreading.com/cloud/aws-follows-google-cloud-in-ending-cloud-switching-costs\">Light Reading</a>).",
   ]),
   ("What a reader should take from it", [
    "When a software company is sold, check whether its product works across "
    "the providers and whether the buyer owns one. If both are true, the "
    "price depends on the buyer preserving neutrality, and the useful evidence "
    "is how the product's support on competing clouds changes over the next "
    "several years.",
   ]),
  ],
  takeaway="",
  words=[
   ("Hyperscaler", "One of the very large cloud providers. Amazon, Microsoft, Google."),
   ("Capex", "Money spent acquiring an asset the company keeps."),
   ("Opex", "Money spent running the business period to period."),
   ("Lock-in", "What it would cost a customer to leave. Often the real asset."),
   ("Multicloud", "Using more than one provider deliberately, to preserve leverage."),
  ]),

 dict(
  slug="what-ai-needs", roman="III",
  lead="What", line1="Training", conn="", line2="Requires",
  sub="A software advance became a question about electricity",
  lede=("The part of the AI boom that mattered commercially to the companies "
        "in Ten Years was less the software than the computing it required. "
        "Training a large model is a physical activity that uses thousands of "
        "processors, buildings and large amounts of electricity, and the "
        "scarcest input moved step by step from processors to buildings to "
        "power. That sequence explains why storage, networking and "
        "construction attracted capital."),
  sections=[
   ("Training and inference", [
    "Training is building the model. A system is shown a very large "
    "quantity of text or images and adjusts billions of internal values "
    "until it predicts well. This runs on thousands of processors for weeks "
    "or months and is expensive. Inference is using the result. A question "
    "goes in and an answer comes out. Each instance is cheap and the total is "
    "not, because there are a great many questions.",
    "Training resembles a construction project, and inference resembles a "
    "utility bill. Most of the spending described in the timeline between "
    "2023 and 2025 is the first kind.",
   ]),
   ("Why thousands of chips and not one fast one", [
    "A conventional processor performs operations one after another very "
    "quickly. A graphics processor performs thousands of simple operations at "
    "the same time. Nvidia began as a maker of graphics chips for games, "
    "where the color of millions of pixels has to be worked out at once and "
    "the order does not matter. Training a model has a similar shape, which "
    "is how a company whose products were first sold for video games came to "
    "supply much of the hardware used for AI.",
    "One processor is not enough. A large training run uses thousands working "
    "together, so the connections between them determine how much of that "
    "hardware is in use at any moment. That is the reasoning behind Nvidia's "
    "purchase of Mellanox, which sold those connections, and behind the "
    "storage company DDN's valuation, since data has to reach the processors "
    "fast enough to keep them working.",
   ]),
   ("Where the constraint ends up", [
    "Thousands of processors in one building draw a great deal of "
    "electricity and turn nearly all of it into heat, so the building needs "
    "power delivered and heat removed. Both are problems of civil and "
    "electrical engineering and not of software. The International Energy "
    "Agency projects global data center electricity use to reach about 945 "
    "terawatt-hours by 2030, roughly the current consumption of Japan, and "
    "expects data centers to account for nearly half of US electricity "
    "demand growth through 2030 "
    "(<a href=\"https://www.iea.org/reports/energy-and-ai/executive-summary\">IEA, Energy and AI</a>).",
    "By 2026 the constraint most often described by operators was electrical "
    "capacity and the time needed to obtain a grid connection. In several "
    "markets hardware can be bought considerably faster than power can be "
    "connected.",
   ]),
   ("The qualification", [
    "Projections of this kind depend on assumptions about how efficient "
    "models and chips become. If training needs substantially less computing "
    "for the same result, the constraint would ease and some of the spending "
    "in the timeline would look excessive in hindsight. Published IEA "
    "scenarios vary widely after 2030 for that reason.",
   ]),
   ("What a reader should take from it", [
    "When a company on this subject announces a purchase or an investment, "
    "find which part of the chain it addresses, processors, connections, "
    "storage, buildings or power, and whether that part is the current "
    "constraint. The evidence that would change the picture is a sustained "
    "fall in the computing needed per model, which would weaken the case for "
    "paying a premium for any part of the chain.",
   ]),
  ],
  takeaway="",
  words=[
   ("Model", "The result of training. Billions of values encoding patterns in data."),
   ("Training", "Building the model. Thousands of processors, running for weeks."),
   ("Inference", "Using the model. Cheap individually, expensive in aggregate."),
   ("GPU", "A processor that performs many simple operations at once."),
   ("Parameters", "The internal values a model adjusts during training."),
  ]),

 dict(
  slug="the-building", roman="IV",
  lead="Inside", line1="A Data", line2="Centre",
  sub="A property with an electricity contract, measured in megawatts",
  lede=("A data center is a building full of computers, and describing it "
        "that way understates how unusual the business has become. The scarce "
        "input is not the computers. It is the power and the land to put them "
        "on, so I think the operators that secured power early hold an "
        "advantage that is difficult to copy."),
  sections=[
   ("What is in the building", [
    "Rows of metal racks hold servers, and each server holds processors. "
    "Above them runs electrical distribution, and alongside them runs cooling, "
    "because nearly every watt delivered comes out as heat and processors fail "
    "when they get too hot. Most of the engineering difficulty is in moving "
    "electricity in and heat out, which is why the people building these "
    "facilities increasingly come from industrial construction and not from "
    "software.",
   ]),
   ("Why these are measured in megawatts", [
    "Data centers are not usually described in square feet or in numbers of "
    "servers. They are described in megawatts. A megawatt is roughly the "
    "draw of eight hundred homes, and a large facility built for AI training "
    "may want several hundred of them. That is comparable to the demand of a "
    "small town, concentrated in one place and running close to full load "
    "through the night.",
    "Water is a consideration as well, because a good deal of cooling works "
    "by evaporation. That has made siting a local political matter in regions "
    "where water is limited.",
   ]),
   ("Why spending moved this way", [
    "The sequence is straightforward. A model needs many processors, many "
    "processors need a building, and the building needs power. Power requires "
    "a grid connection, and utilities grant connections on timescales "
    "measured in years. The constraint moved step by step toward the "
    "physical end of that chain and spending followed it. A growing share of "
    "capital that would once have gone to software development went to "
    "construction, electrical equipment and cooling.",
   ]),
   ("Who benefits, and the qualification", [
    "An operator with a grid connection already in place can add computing "
    "faster than one that has to wait for a utility, and the position can be "
    "worth more than the buildings. A hypothetical buyer comparing two "
    "identical sites would pay more for the one with the connection already "
    "granted.",
    "The qualification is that the advantage lasts only while connections "
    "are scarce. If utilities, regulators and equipment makers expand "
    "capacity faster than demand grows, the position loses value. The "
    "evidence to watch is the typical wait for a connection in the largest "
    "data center markets.",
   ]),
   ("What a reader should take from it", [
    "Value a data center as a property with an electricity contract and not "
    "as a technology asset. The questions that matter are how many megawatts "
    "are contracted, on what terms and by when, and these are more "
    "informative than the number of servers.",
   ]),
  ],
  takeaway="",
  words=[
   ("Data centre", "A building of computers. Measured in megawatts of power draw."),
   ("Rack", "The frame servers are mounted in."),
   ("Megawatt", "A million watts, roughly the draw of eight hundred homes."),
   ("Capex cycle", "A period in which an industry spends heavily on physical assets."),
  ]),

 dict(
  slug="what-a-bank-does", roman="V",
  lead="What", line1="A Bank", conn="Actually", line2="Does",
  sub="Advice and money are two businesses with different incentives",
  lede=("An investment bank does two things that are often described as "
        "one. It advises on transactions, and it arranges money. The "
        "incentives differ between them, and I think a reader who keeps the "
        "two apart can read an announcement's list of advisers as evidence "
        "about how a deal was framed and financed."),
  sections=[
   ("Advice means running a process", [
    "When a company is sold, somebody has to run the sale. That means "
    "deciding which buyers to approach and in what order, preparing the "
    "information they receive, setting a timetable and building the analysis "
    "that supports a view on what the business is worth. There is also a "
    "room of people to manage, each wanting a somewhat different outcome.",
    "This is the sell-side. The adviser is paid a percentage on completion "
    "and very little if the sale does not happen, which is relevant when "
    "reading any adviser's view on whether a sale should proceed. The "
    "buy-side is the other position. The adviser represents the acquirer, on "
    "what to offer, how to structure it and how to avoid paying more than "
    "necessary in a process designed to encourage exactly that.",
   ]),
   ("Arranging money", [
    "A company that needs capital can sell shares, which means giving up a "
    "portion of its ownership permanently, or borrow, which means committing "
    "to repay. Banks arrange both, and the choice between them says "
    "something about how a company views its own prospects.",
    "Equity is ownership, and an initial public offering is the first sale "
    "of it to the public. Debt is a loan, repaid before shareholders receive "
    "anything. A convertible note is a loan the holder may exchange for "
    "shares on agreed terms, which lets the borrower pay a lower interest "
    "rate in return for possible dilution. A term loan B is a large "
    "floating-rate loan sold to investment funds and not held by banks, and "
    "the B describes where it ranks if the borrower gets into trouble.",
   ]),
   ("Coverage", [
    "Banks organize themselves by industry. A coverage group is the team "
    "responsible for the relationship with companies in one industry. A "
    "technology coverage team follows the companies, reads the filings and is "
    "in contact well before there is a transaction to discuss. A company "
    "deciding whether to sell does not usually run a search for an adviser, "
    "and the relationships that determine who receives the call are built "
    "over years. This is why senior moves between banks are followed closely "
    "and why the value of such a hire is usually described in terms of the "
    "relationships it brings.",
   ]),
   ("What the fee is for", [
    "The fee is a percentage, and the percentage falls as transactions get "
    "larger. On a very large deal it may be a fraction of one percent, which "
    "still amounts to tens of millions of dollars. Whether that is "
    "proportionate is negotiated on every transaction. What can be said is "
    "that errors are expensive in ways that are hard to see from outside. A "
    "company sold at the wrong time, to the wrong buyer, or on terms that "
    "fail in a regulatory review costs its owners far more than any fee.",
   ]),
   ("What a reader should take from it", [
    "The work comes down to two questions: what the business is worth to a "
    "particular buyer, and where the money will come from. When reading an "
    "announcement, look at which banks advised each side and which arranged "
    "the financing, and ask whether the same institution did both. The "
    "separate piece on how banks win the mandate takes that question up.",
   ]),
  ],
  takeaway="",
  words=[
   ("Sell-side", "Representing the company being sold. Paid on completion."),
   ("Buy-side", "Representing the acquirer."),
   ("Coverage", "The team responsible for one industry's relationships."),
   ("Equity", "Ownership. Shares."),
   ("Debt", "A loan. Repaid ahead of shareholders."),
   ("Convertible note", "A loan the holder may exchange for shares."),
   ("Term loan B", "A large floating-rate loan sold to funds rather than banks."),
   ("EBITDA", "Earnings before interest, tax, depreciation and amortisation. A rough proxy for cash generation, and a choice about what to exclude."),
  ]),
]
