"""Trojan Horses in Tech Banking.

An argument, and the page says so. A landing page carries the framing and two
circular horses. Each horse opens its own reading. Francis's text, set as
written, with the source links gathered into a list at the foot of each reading.

Register: first person, plain, uncertainty stated flatly. No em dashes, no
semicolons.
"""

KICKER = "What might change"
TITLE = "Trojan Horses in Tech Banking"
LEDE = ("Banks are welcoming private credit partnerships because they expand "
        "financing options for clients. They are adopting AI because it helps "
        "employees complete work faster. Both decisions offer immediate "
        "benefits. I think they also carry risks to two things an investment "
        "bank needs to survive: access to clients and the ability to develop "
        "experienced advisers.")

INTRO = [
 "In the Greek story, the Trojans brought a wooden horse inside their walls "
 "because they believed it was an offering left by the departing Greeks. The "
 "soldiers concealed inside emerged at night and opened the gates. Troy’s "
 "defenses failed because the Trojans admitted something they believed was "
 "safe.",
 "The banking comparison begins with the reasons these developments are being "
 "welcomed. Private credit brings capital. AI brings efficiency. The question "
 "is whether accepting those benefits also creates a way to weaken the "
 "business from within.",
]

# slug, ordinal, kicker, title, the sentence that opens the horse, paragraphs,
# sources, flip (the second horse faces the other way)
HORSES = [

 dict(slug="horse-credit", n="The first horse", sub="Private credit partnerships",
  title="Cuckoos Grow Up In Nests They Did Not Build",
  line=("Private credit could help competing institutions build the "
        "relationships that lead to advisory mandates."),
  flip=False,
  paras=[
   "In September 2024, Citi and Apollo announced a direct lending program "
   "expected to finance approximately $25 billion of debt opportunities. "
   "Citi’s banking head, Viswas Raghavan, said the partnership would give "
   "clients “a range of options to meet their evolving financing needs.” "
   "Apollo’s co-president, Jim Zelter, described the opportunity to “tap into "
   "Citi’s extensive client relationships.” The announcement called it a "
   "“win-win arrangement.”",

   "Those statements explain the immediate commercial logic. Citi contributes "
   "client access and banking expertise. Apollo contributes capital. Together, "
   "they can offer financing that either might find harder to provide alone.",

   "They also identify what could make the arrangement consequential for "
   "advisory work. Apollo gains access to relationships that Citi has spent "
   "years developing.",

   "That matters because financing can influence the choice of an adviser. A "
   "2002 Federal Reserve Bank of New York paper found that “acquirers tend to "
   "choose their own banks” as merger advisers. The researchers connected that "
   "choice to access to loans that could finance the acquisition. The study "
   "concerns a historical sample, but it provides evidence that lending and "
   "advisory relationships can reinforce one another.",

   "Consider a software company borrowing to fund acquisitions. Its lender "
   "reviews financial performance, discusses borrowing capacity, and "
   "evaluates proposed purchases. Over time, those interactions can give the "
   "lender knowledge of the business and access to its decision-makers.",

   "If that institution develops additional capabilities, it can compete for "
   "more assignments. KKR’s capital markets business already provides "
   "financing services to “both our portfolio companies and independent "
   "clients.” Capital markets execution differs from M&amp;A advisory, but it "
   "demonstrates that an alternative asset manager can build a financial "
   "services business extending beyond its own investments.",

   "My argument is that banks should treat these partnerships as decisions "
   "about future competition as well as current financing capacity. A partner "
   "supplying capital today may become qualified to win more of the client’s "
   "business tomorrow.",

   "This challenges the assumption that the bank can contribute its "
   "relationships while keeping its position as the client’s principal "
   "financial adviser. Relationships are strengthened through repeated useful "
   "interactions. A financing partner participating in those interactions has "
   "an opportunity to establish its own standing with management.",

   "That is how private credit could function as a Trojan Horse. The bank "
   "welcomes an outside institution because its capital improves the bank’s "
   "offering. The same arrangement gives that institution access to clients it "
   "might otherwise struggle to reach. The potential threat enters through a "
   "service the bank has chosen to provide.",

   "There is a strong counterargument. Partnerships can help banks retain "
   "clients they might otherwise lose, and the bank may remain responsible "
   "for the relationship. A borrower can also choose separate lenders and "
   "advisers, particularly when it wants independent advice. Access alone does "
   "not guarantee that a private credit manager will win an advisory mandate.",

   "The outcome depends on who becomes more valuable to the client over time. "
   "I would therefore watch whether these partnerships produce repeat business "
   "for the bank, the capital provider, or both, and whether the capital "
   "provider begins winning assignments independently.",
  ],
  srcs=[
   "Citi and Apollo, press release, September 2024. Announcement of a $25 billion private credit direct lending program, with the statements from Viswas Raghavan and Jim Zelter. "
   "<a href=\"https://www.citigroup.com/global/news/press-release/2024/citi-and-apollo-announce-25-billion-private-credit-direct-lending-program\">citigroup.com</a>",
   "Federal Reserve Bank of New York, Staff Report no. 143, 2002, on acquirers and their choice of merger advisers. "
   "<a href=\"https://www.newyorkfed.org/research/staff_reports/sr143.html\">newyorkfed.org</a>",
   "KKR, Capital Markets, description of financing services for portfolio companies and independent clients. "
   "<a href=\"https://www.kkr.com/invest/capital-markets\">kkr.com</a>",
  ]),

 dict(slug="horse-apprenticeship", n="The second horse", sub="Automating the apprenticeship",
  title="Caterpillars Must Cocoon Before Becoming A Butterfly",
  line=("AI could remove some of the work through which junior bankers "
        "develop the judgment those mandates require."),
  flip=True,
  paras=[
   "AI offers banks a different benefit. It can reduce the time required to "
   "retrieve information, summarize documents, and prepare initial analysis. "
   "Morgan Stanley introduced AskResearchGPT to help investment banking and "
   "other employees draw information from its research.",

   "The optimistic argument is straightforward. Automate routine preparation, "
   "then give bankers more time for analysis, clients, and decisions.",

   "Goldman Sachs’s George Lee described this possibility in a 2025 "
   "discussion about AI and employment. He suggested that “the quality of the "
   "apprenticeship rather than the quantity” could help firms “breed even "
   "better senior leaders.” In the same discussion, he acknowledged the "
   "challenge of developing future leaders if firms employ fewer juniors.",

   "I think the optimistic outcome requires more organizational change than "
   "the productivity argument usually establishes. Completing a task faster "
   "creates available time. It does not determine how that time will be used "
   "or what an analyst will learn.",

   "Banks themselves describe practical work as central to development. "
   "Goldman tells prospective interns: “Our interns don’t learn by watching, "
   "they learn by getting involved in real projects.”",

   "Some of those projects contain tasks that AI can help perform. The "
   "difficulty is separating repetitive effort from useful practice.",

   "An analyst preparing comparable company analysis for a software business "
   "must decide which companies belong in the group. Similar revenue growth "
   "can conceal differences in customer retention, profitability, or "
   "dependence on a few large contracts. An experienced banker’s corrections "
   "help the analyst understand which differences matter.",

   "If AI prepares the analysis, the analyst may gain time to investigate "
   "those issues more deeply. But if the bank uses the savings to assign more "
   "projects to fewer people, the analyst may spend that time checking and "
   "forwarding outputs. The work gets completed while the opportunity to "
   "explain and defend the underlying decisions becomes smaller.",

   "That creates a potential Trojan Horse inside the bank’s operating model. "
   "AI enters as a tool for improving productivity. If the bank responds by "
   "removing junior responsibilities without replacing their educational "
   "value, its adoption can weaken the process that produces experienced "
   "bankers.",

   "The effect would take time to appear. Today’s senior bankers would "
   "continue advising clients. Current projects might finish faster. The "
   "consequences would become clearer as later cohorts reached positions "
   "requiring independent judgment.",

   "The strongest objection is that AI could make learning substantially "
   "better. Juniors could test more assumptions, compare alternative "
   "approaches, and receive faster feedback. I think that is plausible. It "
   "supports a deliberate redesign of the apprenticeship.",

   "A bank pursuing that outcome would require analysts to defend "
   "recommendations, explain changes to generated work, participate in client "
   "discussions, and review decisions with senior colleagues. Those "
   "activities need protected time and management attention. They cannot "
   "depend entirely on whatever time remains after the next assignment "
   "arrives.",
  ],
  srcs=[
   "Morgan Stanley, press release announcing AskResearchGPT. "
   "<a href=\"https://www.morganstanley.com/press-releases/morgan-stanley-research-announces-askresearchgpt\">morganstanley.com</a>",
   "Goldman Sachs Exchanges, “AI’s impact on employment,” transcript, 2025, with George Lee. "
   "<a href=\"https://d3cobg6h0snvt3.cloudfront.net/pdfs/insights/goldman-sachs-exchanges/ai-exchanges-ais-impact-on-employment/transcript.pdf\">goldmansachs.com</a>",
   "Goldman Sachs, careers for students, on how interns learn. "
   "<a href=\"https://www.goldmansachs.com/careers/students\">goldmansachs.com</a>",
  ]),
]

CLOSE_HEAD = "What the two horses could change"
CLOSE = [
 "Private credit partnerships and AI adoption can improve a bank’s results "
 "while changing how it competes in the future. One can give another "
 "institution a stronger relationship with its clients. The other can reduce "
 "the experience available to its future advisers.",
 "That is my thesis: banks risk weakening their advisory businesses if they "
 "judge these developments mainly by the capital they provide and the costs "
 "they remove.",
 "In the Greek story, the horse crossed the walls because the Trojans "
 "accepted the explanation for bringing it inside. Banks have substantial "
 "reasons to welcome both private credit and AI. They also need to examine "
 "what those decisions allow to happen afterward.",
]

NOTE = ("This page is argument and not reporting. The quotations and facts are "
        "sourced at the foot of each reading. The reasoning built on them is "
        "mine, and each reading names the objection I think is strongest.")
