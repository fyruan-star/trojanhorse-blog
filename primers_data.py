"""Background. Five explanations the timeline keeps relying on.

Written for a reader with no technical knowledge. Each one explains the
mechanism before drawing any conclusion from it, and stops when the
explanation is complete. No em dashes, no semicolons, no closing flourishes.

Each ends with the words it has handed over, because being able to read the
sentence afterward is the point.
"""

PRIMERS = [

 dict(
  slug="what-a-chip-is", roman="I",
  lead="What", line1="A Chip", line2="Is",
  sub=("THE DIFFERENCE BETWEEN DESIGNING ONE<br>"
       "AND MANUFACTURING ONE, AND WHY IT MATTERS"),
  lede=("A semiconductor is a piece of silicon with a very small circuit "
        "printed on it. Billions of switches, each either on or off, arranged "
        "so that setting them in the right order performs arithmetic. "
        "Everything that follows is a consequence of how difficult that is to "
        "manufacture."),
  sections=[
   ("Three businesses, one chip", [
    "Designing a chip and making a chip are separate businesses, run by "
    "different companies in different countries. That separation explains a "
    "good deal of what appears in the timeline.",
    "<strong>The architecture</strong> is the instruction set, the basic "
    "vocabulary a processor understands. Arm licenses this and manufactures "
    "nothing. It receives a royalty on each chip built using its design, which "
    "across the industry runs to tens of billions of units a year.",
    "<strong>The design</strong> is the specific layout. Nvidia, Apple and "
    "Qualcomm do this work and own no factories. The industry calls such a "
    "company fabless, which sounds like a criticism and is a business model.",
    "<strong>The manufacture</strong> happens in a fabrication plant, known as "
    "a fab. A plant capable of the smallest feature sizes costs upward of "
    "twenty billion dollars and takes years to build. Very few companies "
    "operate one at the leading edge, and the largest by a considerable margin "
    "is TSMC, in Taiwan.",
   ]),
   ("Why governments became involved", [
    "The consequence is worth sitting with. A large share of the most advanced "
    "chips in the world are manufactured in one place, and that place is the "
    "subject of an unresolved territorial dispute.",
    "This is the background to several entries in the timeline. It is why a "
    "committee reviewing foreign investment was able to stop a takeover in "
    "2018, why export controls now cover equipment most people could not "
    "identify, and why several governments have committed large sums to "
    "building manufacturing capacity domestically. The policy question is not "
    "whether chips are useful. It is whether a country can obtain them if "
    "relations deteriorate.",
   ]),
   ("A single supplier for one critical machine", [
    "The machines that print the smallest circuits use extreme ultraviolet "
    "light, and one company makes them. ASML, in the Netherlands. Each machine "
    "costs a few hundred million dollars and is delivered in several aircraft.",
    "The result is a supply chain with very few alternatives at several steps. "
    "That concentration was not planned. It is what happens when each "
    "generation of equipment costs more than the last, until only a handful of "
    "firms can afford to remain at the leading edge.",
   ]),
  ],
  takeaway=("Designing a chip, licensing the instruction set it is built on, "
            "and manufacturing it are three separate businesses with different "
            "economics. Several disputes in this timeline are about which of "
            "them was worth owning."),
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
  sub="A BUILDING WITH AN ADDRESS, OWNED BY SOMEBODY ELSE,<br>RENTED BY THE HOUR",
  lede=("The cloud is somebody else's computer, in a building you will not "
        "visit, rented by the hour. That is not a simplification. Holding on "
        "to it will carry you through a good deal of what follows."),
  sections=[
   ("What changed around 2010", [
    "Before then, a company that needed computing bought computers. It put "
    "them in a room, employed people to maintain them, and paid up front for "
    "capacity it would mostly not use.",
    "Amazon, which had built a great deal of computing capacity for its retail "
    "business, began renting the spare capacity to others. Microsoft and "
    "Google followed.",
    "In accounting terms a large one-off purchase became a monthly expense. "
    "That sounds like a technicality and it changed who could start a software "
    "company. Two people now had access to the same computing capacity as a "
    "bank, and paid only for what they used. A great many software companies "
    "founded after 2010 exist in a form that would not have been affordable "
    "before it.",
   ]),
   ("Why there are three", [
    "Amazon arrived first and remains the largest. Microsoft was second and "
    "had an advantage, in that it was already selling software to most large "
    "organisations. Google has been third for most of the period covered here.",
    "Once a company's systems and data are established with one provider, "
    "moving them is a project rather than a decision. It takes a long time, it "
    "costs a great deal, and little visibly improves when it is finished. So "
    "customers tend to stay. The term for this is lock-in, and it is usually "
    "the most valuable thing a provider has.",
   ]),
   ("Multicloud, and why customers want it", [
    "Larger customers recognised the position they were in and began keeping "
    "systems with more than one provider deliberately, so that no single "
    "supplier could raise prices without a credible response. That practice is "
    "called multicloud.",
    "It also creates a position worth having. A supplier whose software works "
    "across all three providers earns revenue regardless of which one a "
    "customer chooses, and has no stake in the outcome.",
    "IBM paid about $34 billion for a company in that position in 2018, and "
    "Google agreed to pay about $32 billion for another in 2025. The "
    "resemblance between those two purchases is worth noticing when you reach "
    "them.",
   ]),
  ],
  takeaway=("Renting computing changed who could afford to start a software "
            "company. It also created a durable position for suppliers whose "
            "products work across all three major providers."),
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
  sub="HOW A SOFTWARE ADVANCE BECAME<br>A QUESTION ABOUT ELECTRICAL CAPACITY",
  lede=("Something clearly changed in late 2022. The part that mattered "
        "commercially to the companies in this timeline was less the software "
        "itself than the computing it required, and the consequences of that "
        "requirement ran a long way into the physical world."),
  sections=[
   ("Training and inference, which are different jobs", [
    "<strong>Training</strong> is building the model. A system is shown a very "
    "large quantity of text or images and adjusts billions of internal values "
    "until it predicts well. This runs on thousands of processors for weeks or "
    "months and is expensive.",
    "<strong>Inference</strong> is using the result. A question goes in and an "
    "answer comes out. Each instance is cheap and the total is not, because "
    "there are a great many questions.",
    "Training resembles a construction project. Inference resembles a utility "
    "bill. Most of the spending described in the timeline between 2023 and "
    "2025 is the first kind.",
   ]),
   ("Why thousands of chips rather than one fast one", [
    "A conventional processor is built to perform operations one after another "
    "very quickly. A graphics processor is built to perform thousands of "
    "simple operations at the same time. It was developed for video games, "
    "where the colour of two million pixels has to be worked out "
    "simultaneously and the order does not matter.",
    "Training a model has a similar shape. That is how a company whose "
    "products were originally sold for video games came to supply much of the "
    "hardware used for AI training.",
    "One processor is not sufficient. A large training run uses thousands "
    "working together, which means the connections between them affect how "
    "much of that hardware is actually in use. It is why the Mellanox purchase "
    "appears in the timeline.",
   ]),
   ("Where the constraint ends up", [
    "Thousands of processors in one building draw a great deal of electricity "
    "and convert nearly all of it into heat, so the building needs power "
    "delivered and heat removed. Both are matters of civil and electrical "
    "engineering rather than software.",
    "By 2026 the constraint most often described by operators was electrical "
    "capacity and the time needed to obtain a grid connection. In several "
    "markets hardware can be purchased considerably faster than power can be "
    "connected.",
   ]),
  ],
  takeaway=("Training large models turned a software advance into a demand for "
            "buildings, electrical capacity and cooling, on timescales set by "
            "utilities rather than by engineers."),
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
  sub="A PROPERTY WITH AN ELECTRICITY CONTRACT,<br>MEASURED IN MEGAWATTS",
  lede=("A data centre is a building full of computers. Describing it that way "
        "understates how unusual the business has become, because the scarce "
        "input is not the computers. It is the power and the land to put them "
        "on."),
  sections=[
   ("What is in the building", [
    "Rows of metal racks. Each rack holds servers, each server holds "
    "processors. Above them, electrical distribution. Alongside, cooling, "
    "because nearly every watt delivered emerges as heat and processors fail "
    "when they get too hot.",
    "Most of the engineering difficulty is in moving electricity in and heat "
    "out. That is why the people building these facilities increasingly come "
    "from industrial construction rather than from software.",
   ]),
   ("Why these are measured in megawatts", [
    "Data centres are not usually described in square feet or in numbers of "
    "servers. They are described in megawatts, a measure of electrical power.",
    "A megawatt is roughly the draw of eight hundred homes. A large facility "
    "built for AI training may want several hundred. That is comparable to the "
    "demand of a small town, concentrated in one place and running close to "
    "full load through the night.",
    "Water is a consideration as well, because a good deal of cooling works by "
    "evaporation. That has made siting a local political matter in regions "
    "where water is limited.",
   ]),
   ("Why spending moved this way", [
    "The sequence is straightforward. A model needs many processors. Many "
    "processors need a building. The building needs power. Power requires a "
    "grid connection, and grid connections are granted by utilities on "
    "timescales measured in years.",
    "The constraint moved step by step toward the physical end of that chain, "
    "and spending followed it. A growing share of capital that would once have "
    "gone to software development went instead to construction, electrical "
    "equipment and cooling. It is among the more consequential developments of "
    "the period and it is reported considerably less than the models are.",
   ]),
  ],
  takeaway=("A data centre is better understood as a property with an "
            "electricity contract than as a technology asset, and operators "
            "who secured power early held an advantage that was difficult to "
            "copy."),
  words=[
   ("Data centre", "A building of computers. Measured in megawatts of power draw."),
   ("Rack", "The frame servers are mounted in."),
   ("Megawatt", "A million watts, roughly the draw of eight hundred homes."),
   ("Capex cycle", "A period in which an industry spends heavily on physical assets."),
  ]),

 dict(
  slug="what-a-bank-does", roman="V",
  lead="What", line1="A Bank", conn="Actually", line2="Does",
  sub="ADVICE, MONEY, AND THE DIFFERENCE<br>BETWEEN THE TWO SIDES OF A TRANSACTION",
  lede=("An investment bank does two things that are often described as one. "
        "It advises on transactions, and it arranges money. Most writing about "
        "the industry concerns the hours rather than the work, so this is the "
        "work."),
  sections=[
   ("Advice, which means running a process", [
    "When a company is sold, somebody has to run the sale. Decide which buyers "
    "to approach and in what order, prepare the information they receive, set "
    "a timetable, and build the analysis that supports a view on what the "
    "business is worth. There is also a room of people to manage, each wanting "
    "a somewhat different outcome.",
    "That is the sell-side. The adviser is paid a percentage on completion and "
    "very little if the sale does not happen, which is worth knowing when "
    "reading any adviser's view on whether a sale should proceed.",
    "The buy-side is the other position. The adviser represents the acquirer: "
    "what to offer, how to structure it, and how to avoid paying more than "
    "necessary in a process designed to encourage exactly that.",
   ]),
   ("Arranging the money", [
    "The other business is arranging money, and in a decade with this much "
    "construction in it that half has mattered a great deal.",
    "A company that needs capital can sell shares, which means giving up a "
    "portion of its ownership permanently, or borrow, which means committing "
    "to repay. Banks arrange both, and the choice between them says something "
    "about how a company views its own prospects.",
    "<strong>Equity</strong> is ownership. An initial public offering is the "
    "first sale of it to the public. <strong>Debt</strong> is a loan, repaid "
    "before shareholders receive anything. A <strong>convertible note</strong> "
    "is a loan the holder may exchange for shares on agreed terms, which lets "
    "the borrower pay a lower interest rate in return for possible dilution. "
    "A <strong>term loan B</strong> is a large floating-rate loan sold to "
    "investment funds rather than held by banks. The B describes where it "
    "ranks if the borrower gets into trouble. There is also a term loan A, "
    "usually held by banks, which attracts less attention.",
   ]),
   ("Coverage, and why the word exists", [
    "Banks organise themselves by industry. A coverage group is the team "
    "responsible for the relationship with companies in one of them. A "
    "technology coverage team follows the companies, reads the filings, and is "
    "in contact well before there is a transaction to discuss.",
    "A good deal of the job is being known before there is anything to "
    "discuss. A company deciding whether to sell does not usually run a search "
    "for an adviser, and the relationships that determine who receives the "
    "call are built over years.",
    "This is why senior moves between banks are followed closely, and why the "
    "value of such a hire is usually described in terms of the relationships "
    "it brings rather than the work the person does.",
   ]),
   ("What the fee is for", [
    "The fee is a percentage, and the percentage falls as transactions get "
    "larger. On a very large deal it may be a fraction of one percent, which "
    "still amounts to tens of millions of dollars. Whether that is "
    "proportionate is a fair question and it is negotiated on every "
    "transaction.",
    "What can be said is that the errors are expensive in ways that are hard "
    "to see from outside. A company sold at the wrong time, to the wrong "
    "buyer, or on terms that fail during a regulatory review, costs its owners "
    "far more than any fee. Several of the abandoned transactions in this "
    "timeline are that kind of error, in public.",
   ]),
  ],
  takeaway=("The work comes down to two questions. What is this business worth "
            "to a particular buyer, and where will the money come from. The "
            "rest of the apparatus exists to answer those two reliably."),
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
