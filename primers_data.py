"""The Ground Floor. Five things you need before the timeline makes sense.

Rule for all five: explain the thing before being clever about it. Deflate the
jargon, never the reader. If a sentence would make somebody feel they should
already have known, it is cut.

Each one ends with the words it just handed over, because the satisfying part
of learning a field is noticing you can now read the sentence.
"""

PRIMERS = [

 dict(
  slug="what-a-chip-is", roman="I",
  lead="What", line1="A Chip", conn="", line2="Is",
  sub=("THE DIFFERENCE BETWEEN DRAWING ONE<br>"
       "AND BUILDING ONE, AND WHY IT IS A COUNTRY&rsquo;S PROBLEM"),
  lede=("A semiconductor is a slab of silicon with a very small city printed on "
        "it. Billions of switches, each one either on or off, arranged so that "
        "flicking them in the right order does arithmetic. That is the whole "
        "idea. Everything after this is logistics."),
  sections=[
   ("Three companies, one chip", [
    "Here is the thing almost nobody outside the industry knows, and it explains "
    "most of the last decade. Designing a chip and making a chip are completely "
    "different businesses, run by different companies, in different countries, "
    "with different problems.",
    "<strong>The architecture</strong> is the instruction set. The basic grammar "
    "the chip understands: add this, fetch that, compare these two. ARM sells "
    "this grammar and does not make anything at all. It licenses the design and "
    "takes a royalty on every chip anybody stamps it into, which is roughly "
    "thirty billion chips a year.",
    "<strong>The design</strong> is the actual layout. NVIDIA, Apple and "
    "Qualcomm do this. They draw an extraordinarily complicated picture and own "
    "no factory whatsoever. The industry calls them fabless, which sounds like "
    "an insult and is a business model.",
    "<strong>The manufacture</strong> is the factory, called a fab, and this is "
    "where it gets strange. A leading-edge fab costs upward of twenty billion "
    "dollars, takes years to build, and there are effectively three companies on "
    "earth that can run one at the smallest sizes. The most advanced of them, "
    "TSMC, is in Taiwan.",
   ]),
   ("Why that last sentence keeps governments awake", [
    "Read it again. Nearly every advanced chip in the world is made in one place, "
    "and that place is the subject of an unresolved territorial dispute.",
    "This is why a committee you have never heard of blocked the largest "
    "technology takeover ever attempted, why there are export controls on "
    "machines most people could not identify, and why several governments have "
    "spent enormous sums trying to build fabs at home. Chips stopped being a "
    "component somewhere around 2018 and became a strategic reserve, like oil, "
    "except harder to find and considerably harder to make.",
   ]),
   ("The one machine", [
    "If you want a single fact that makes the whole field feel absurd, it is "
    "this. The machines that print the smallest circuits use extreme "
    "ultraviolet light, and exactly one company in the world makes them. ASML, "
    "in the Netherlands. Each machine costs a few hundred million dollars and "
    "ships in several aeroplanes.",
    "So the supply chain for the most important product of the century runs "
    "through one Dutch machine, one Taiwanese factory, and one British "
    "instruction set owned by a Japanese holding company. Nobody designed it this "
    "way. It simply happened, the way cities happen.",
   ]),
  ],
  takeaway=("Nobody makes a chip. Three different companies in three different "
            "countries each make part of one, and every argument in this section "
            "is about which part was worth owning."),
  words=[
   ("Semiconductor", "A chip. Silicon with switches printed on it."),
   ("Architecture", "The grammar a chip understands. ARM sells this."),
   ("Fabless", "A company that designs chips and owns no factory. NVIDIA, Apple, Qualcomm."),
   ("Foundry", "A company that makes chips it did not design. TSMC."),
   ("Fab", "The factory. Costs tens of billions. Very few exist."),
   ("Node", "How small the features are. Smaller is faster and far harder."),
  ]),

 dict(
  slug="what-the-cloud-is", roman="II",
  lead="What", line1="The Cloud", conn="", line2="Is",
  sub=("IT IS A BUILDING, IT HAS AN ADDRESS<br>AND SOMEBODY PAYS ITS POWER BILL"),
  lede=("The cloud is somebody else&rsquo;s computer in a building you will never "
        "visit. That is not a simplification to be nice to you. That is "
        "literally what it is, and holding onto that one fact will carry you "
        "through most of the last fifteen years."),
  sections=[
   ("The thing that actually changed", [
    "Before roughly 2010, if you ran a company and needed computing, you bought "
    "computers. You put them in a room, hired people to look after them, and "
    "wrote a very large cheque up front for capacity you would mostly not use.",
    "Then Amazon, which had built a lot of computers for its shop, noticed it "
    "could rent out the spare ones. You stopped buying the computers and started "
    "renting them by the hour.",
    "In accounting terms, a large one-off purchase became a monthly bill. That "
    "sounds like a technicality and it rearranged the entire industry, because a "
    "monthly bill is something a company with no money can afford. Two people in "
    "a flat could suddenly have the same computing power as a bank. Almost every "
    "software company you can name exists because of this one change.",
   ]),
   ("There are three of them, and that is the problem", [
    "Amazon got there first and is still the largest. Microsoft came second and "
    "had an unfair advantage, which is that it was already inside every "
    "corporate building on earth selling them Office. Google came third and has "
    "stayed third.",
    "Once your company&rsquo;s data lives in one of them, moving it is not a "
    "decision, it is a project. It takes years, it costs a fortune, and nothing "
    "visibly improves when you are done. So people do not move. The industry word "
    "for this is lock-in, and it is the most valuable thing any of these "
    "companies owns.",
   ]),
   ("Which is why multicloud is a fighting word", [
    "Large companies worked out the lock-in problem and started deliberately "
    "keeping things in more than one cloud, so no single provider could put the "
    "price up and be obeyed. That is multicloud.",
    "It also creates a genuinely valuable position: the company whose software "
    "works across all three. If you sell something that runs everywhere, you get "
    "paid regardless of who wins, and you are the only one in the room who does "
    "not care.",
    "Hold that thought. IBM paid $34bn for it in 2018 and Google paid $32bn for "
    "it in 2025, and the two deals are the same move wearing different clothes.",
   ]),
  ],
  takeaway=("The cloud is a rental business, and the most valuable seat in a "
            "rental business is not owning the building. It is being the thing "
            "every tenant needs regardless of which building they are in."),
  words=[
   ("Hyperscaler", "One of the three enormous cloud providers. Amazon, Microsoft, Google."),
   ("Capex", "Money spent buying a thing you keep. The old way."),
   ("Opex", "Money spent running the business month to month. The rental way."),
   ("Lock-in", "How expensive it would be to leave. Usually the real asset."),
   ("Multicloud", "Deliberately using more than one, so none of them owns you."),
  ]),

 dict(
  slug="what-ai-needs", roman="III",
  lead="What", line1="AI", conn="Actually", line2="Needs",
  sub=("WHY A SOFTWARE BREAKTHROUGH TURNED INTO<br>AN ARGUMENT ABOUT ELECTRICITY"),
  lede=("Everybody understood that something happened in late 2022. Almost "
        "nobody was told the part that mattered commercially, which is that the "
        "breakthrough did not create demand for programmers. It created demand "
        "for power stations."),
  sections=[
   ("Training and inference, which are not the same job", [
    "<strong>Training</strong> is building the model. You show a system an "
    "enormous amount of text or images and it adjusts billions of internal "
    "numbers until it gets good at predicting what comes next. This takes weeks "
    "or months, runs on thousands of chips at once, and costs somewhere between a "
    "lot and an astonishing amount.",
    "<strong>Inference</strong> is using it. You ask a question, the model "
    "answers. That is cheap per question and ruinous at scale, because there are "
    "a great many questions.",
    "Training is a construction project. Inference is a utility bill. The "
    "industry spent 2023 and 2024 on the first and is now discovering the second.",
   ]),
   ("Why thousands of chips, and not one fast one", [
    "A normal processor, the kind in your laptop, is built to do one thing after "
    "another very quickly. A GPU is built to do thousands of simple things at "
    "the same time. It was invented for video games, where you need to work out "
    "the colour of two million pixels simultaneously and nobody cares what order "
    "you do it in.",
    "Training a model turns out to be the same shape of problem. Which is how a "
    "company that made graphics cards for teenagers became the most valuable "
    "company in the world, and it is not a joke, it is just what happened.",
    "But one GPU is not enough. You need ten thousand of them behaving like a "
    "single machine, which means the wiring between them matters as much as the "
    "chips. This is the entire reason the Mellanox deal is on the timeline.",
   ]),
   ("And then it stops being a technology problem", [
    "Ten thousand chips in a room draw an extraordinary amount of electricity and "
    "convert nearly all of it into heat. So you need power, and you need to "
    "remove the heat, and both of those are civil engineering rather than "
    "software.",
    "The constraint on artificial intelligence in 2026 is not ideas and it is not "
    "chips. It is grid connections. There are places where you can buy the "
    "hardware tomorrow and wait four years for the power.",
   ]),
  ],
  takeaway=("The most advanced industry on earth spent three years discovering "
            "that its hard limit is the same one that constrained a nineteenth "
            "century steel mill. Somewhere to put it, and enough power to run it."),
  words=[
   ("Model", "The thing that was trained. Billions of numbers that encode patterns."),
   ("Training", "Building it. Thousands of chips, weeks on end, enormous cost."),
   ("Inference", "Using it. Cheap each time, expensive by the billion."),
   ("GPU", "A chip that does thousands of simple things at once. Invented for games."),
   ("Parameters", "The internal numbers a model adjusts. More is usually better and always costlier."),
  ]),

 dict(
  slug="the-building", roman="IV",
  lead="The", line1="Building", conn="", line2="Itself",
  sub=("THE HOTTEST ASSET IN TECHNOLOGY IS A SHED<br>WITH GOOD ACCESS TO A POWER LINE"),
  lede=("A data centre is a warehouse full of computers, and describing it that "
        "way undersells how strange a business it has become. It is not really a "
        "technology asset. It is a property with an electricity contract, and in "
        "2026 that is the scarcest thing in the industry."),
  sections=[
   ("What is actually in there", [
    "Rows of metal racks. Each rack holds servers, each server holds chips. "
    "Overhead, power. Underneath or alongside, cooling, because every watt that "
    "goes in comes out as heat and silicon stops working when it gets hot.",
    "That is it. There is no magic floor. The interesting engineering is almost "
    "entirely about moving electricity in and moving heat out, which is why the "
    "people who build these increasingly come from industrial construction rather "
    "than from software.",
   ]),
   ("The unit of account is the megawatt", [
    "Here is the tell that this is not a technology business any more. Data "
    "centres are not measured in square feet or in servers. They are measured in "
    "megawatts, which is a measure of electricity.",
    "A megawatt is roughly what eight hundred homes draw. A large AI facility "
    "wants hundreds of them. You are not building a building. You are building "
    "something closer to a small town&rsquo;s worth of demand, in one place, "
    "that runs flat out at three in the morning.",
    "Water matters too, because a lot of cooling is evaporative, which has made "
    "data centres a local political issue in places that do not have much.",
   ]),
   ("Why the money started going here", [
    "Follow the chain. A model needs thousands of chips. Thousands of chips need "
    "a building. The building needs power. Power needs a grid connection, and "
    "grid connections are issued by utilities on timescales measured in years.",
    "So the bottleneck moved, step by step, from the clever part to the dull "
    "part, and the capital followed it. Spending that used to go to engineers now "
    "goes to concrete, transformers and industrial air conditioning. This is the "
    "single most important thing that happened to technology between 2023 and "
    "2026, and it is almost never the headline.",
   ]),
  ],
  takeaway=("Every AI company is now partly an energy company, whether it says "
            "so or not. The ones that admitted it early bought land near power."),
  words=[
   ("Data centre", "A warehouse of computers. Measured in megawatts, not square feet."),
   ("Rack", "The metal frame the servers sit in. The basic unit inside."),
   ("Megawatt", "A million watts. Roughly eight hundred homes. The real currency here."),
   ("Capex cycle", "A stretch of years where an industry spends heavily on physical things."),
  ]),

 dict(
  slug="what-a-bank-does", roman="V",
  lead="What", line1="A Bank", conn="Actually", line2="Does",
  sub=("ON ADVICE, MONEY, AND THE DIFFERENCE<br>BETWEEN THE TWO CHAIRS AT THE TABLE"),
  lede=("An investment bank does two things that look like one thing. It gives "
        "advice, and it arranges money. Almost everything written about the "
        "industry, including the funny parts, is about the hours rather than the "
        "work, so here is the work."),
  sections=[
   ("Advice, which means running the process", [
    "When a company is sold, somebody has to run the sale. Decide who to "
    "approach, in what order, with what information, on what timetable. Build the "
    "model that says what the thing is worth. Manage a room of people who each "
    "want a different outcome, including the founder, who is about to make a "
    "decision they will think about for the rest of their life.",
    "That is sell-side. The bank is paid a percentage when it closes, and close "
    "to nothing if it does not, which tells you most of what you need to know "
    "about the incentives in the room.",
    "Buy-side is the other chair. You represent the acquirer: what to pay, how to "
    "structure it, how to not overpay in an auction designed to make you overpay.",
   ]),
   ("Money, which is the half nobody writes about", [
    "The other business is arranging the money, and in a decade like this one it "
    "is arguably the more interesting half.",
    "A company that wants to grow can sell shares, which means giving away a "
    "slice of itself forever, or borrow, which means promising to pay it back. "
    "Banks arrange both, and the choice between them is one of the most revealing "
    "things a company ever does.",
    "<strong>Equity</strong> is ownership. An IPO is the first public sale of it. "
    "<strong>Debt</strong> is a loan. A <strong>convertible note</strong> is a "
    "loan allowed to change its mind and become shares, which is why companies "
    "like it, the interest is cheap, and why lenders like it, because if the "
    "stock runs they stop being a lender and start being an owner. A "
    "<strong>term loan B</strong> is a large floating-rate loan chopped up and "
    "sold to funds rather than held by one bank. The B is where it sits in the "
    "queue if things go wrong. There is an A. Nobody talks about the A.",
   ]),
   ("Coverage, and why the word exists", [
    "Banks organise themselves by industry, and a coverage group is the team that "
    "owns the relationship with companies in one of them. Technology coverage "
    "knows the semiconductor chief executives, has read every filing, and is in "
    "the room before there is a transaction to be in the room for.",
    "The job is substantially about being known. You cannot pitch your way into a "
    "founder&rsquo;s decision in the week they make it. You are either already "
    "the person they call or you are not, and that relationship took eleven years "
    "to build.",
    "Which is why banks hire bankers rather than train them, and why a senior "
    "move between firms is reported like a transfer window. They are not buying "
    "the person&rsquo;s process. They are buying the phone.",
   ]),
   ("What the money is for", [
    "The fee is a percentage and the percentage falls as the deal gets larger. On "
    "something enormous it can be a fraction of a percent, which still runs to "
    "tens of millions, which is the part everyone finds outrageous and is also "
    "the part that is genuinely contested on every deal.",
    "Whether it is worth it is a real question and I am not going to pretend it "
    "is settled. What I will say is that the mistakes are expensive in a way that "
    "is hard to see from outside. A company sold at the wrong moment, or to the "
    "wrong buyer, or on terms that unravel in the regulatory review, costs its "
    "owners vastly more than the fee. Several of the toppled columns on the "
    "timeline are that mistake, in public, at scale.",
   ]),
  ],
  takeaway=("Strip the hours and the shirts away and the job is this: somebody "
            "has to decide what a thing is worth, and somebody has to find the "
            "money. Everything else is the apparatus around those two sentences."),
  words=[
   ("Sell-side", "Representing the company being sold. Paid on closing."),
   ("Buy-side", "Representing the acquirer."),
   ("Coverage", "The team that owns the relationship with one industry."),
   ("Equity", "Ownership. Shares."),
   ("Debt", "A loan. Must be repaid, ranks ahead of equity."),
   ("Convertible note", "A loan that can turn into shares."),
   ("Term loan B", "A big floating-rate loan sold to funds. There is an A."),
   ("EBITDA", "Profit before interest, tax and the cost of things wearing out. A rough proxy for cash, and a choice."),
  ]),
]
