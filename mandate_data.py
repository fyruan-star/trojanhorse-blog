"""How a bank wins the assignment.

Every company claim is checked against a primary source. The Evercore language
is quoted from its annual report and the New York Fed finding from the staff
report. Sources are linked beside the claims they support and listed at the
foot.

No em dashes, no semicolons.
"""

KICKER = "The strategy and incentives behind investment banking"
TITLE = "How Banks Win the Mandate"
LEDE = ("A company chooses its adviser on judgment it cannot test in advance, "
        "so it relies on relationships and on a bank's ability to finance the "
        "deal. Those same advantages create conflicts, and the best response "
        "is often to use more than one adviser.")

# a section with an empty heading prints as plain paragraphs
SECTIONS = [

 ("", [
  "Imagine a software company agrees to buy a competitor for $5 billion. The "
  "announcement explains the price and the strategic rationale and, near the "
  "bottom, names the investment banks that advised each side. Each of those "
  "banks had to win the assignment, which is called the mandate, by "
  "persuading a company to trust it with a decision that could change the "
  "company's future.",
  "My thesis is that the choice of adviser is a decision about what problem "
  "the client needs solved, and that the advisers named in an announcement "
  "are evidence of how the client saw its problem. The choice is not a "
  "simple one between an independent firm and a large bank. The evidence "
  "shows that clients are pulled both ways, and that the same features that "
  "attract them to a bank also create the conflicts that attract them to an "
  "alternative.",
 ]),

 ("Two views of what an adviser is for", [
  "Independent advisory firms present objectivity as their main reason to be "
  "chosen. Evercore says in its annual report that it “was founded on the "
  "belief that there is an opportunity within the investment banking "
  "industry for a firm free of the potential conflicts of interest created "
  "within large, multi-product, capital intensive financial institutions” "
  "(<a href=\"https://www.sec.gov/Archives/edgar/data/1360901/000162828026010273/evr-20251231.htm\">Evercore 10-K</a>). "
  "Centerview describes its advice as independent and “unencumbered by "
  "institutional constraints or conflicts of interest” "
  "(<a href=\"https://centerviewpartners.com/corporateadvisory.aspx\">Centerview</a>).",
  "A study by four economists at the Federal Reserve Bank of New York points "
  "the other way. Linda Allen, Julapa Jagtiani, Stavros Peristiani and "
  "Anthony Saunders found in 2002 that “acquirers tend to choose their own "
  "banks” as merger advisers, meaning banks that already lent to them "
  "(<a href=\"https://www.newyorkfed.org/research/staff_reports/sr143.html\">New York Fed, Staff Report 143</a>). "
  "The sample is historical, but it shows that a bank's lending relationship "
  "was commercially valuable to the client when it chose an adviser.",
  "Both observations are accurate, and they describe different clients with "
  "different problems.",
 ]),

 ("Why relationships decide", [
  "On a $5 billion purchase, a one percent difference in price is $50 "
  "million. A useful adviser might help the buyer avoid paying that extra "
  "amount, might recognize that the business deserves a higher price, or "
  "might tell the buyer to stop negotiating altogether. The client is paying "
  "for judgment whose quality becomes clear only after the decisions have "
  "been made. A polished presentation demonstrates preparation and shows "
  "little about how someone will behave when a negotiation turns difficult.",
  "Relationships address that problem by giving the client evidence before "
  "the transaction. Banks organize teams around industries so their people "
  "stay close to potential clients. A banker covering software can study "
  "competitors, follow management changes and bring executives ideas long "
  "before there is a deal to discuss.",
  "Consider two hypothetical bankers approaching the same chief executive. "
  "One arrives when a sale becomes likely. The other has spent years "
  "offering useful observations about the business, including reasons to "
  "reject earlier acquisition ideas. The second has given the executive more "
  "evidence on which to judge the advice. A formal pitch can still matter, "
  "but the relationship shapes how the client weighs what it hears.",
 ]),

 ("Why financing changes the choice", [
  "Now suppose the buyer needs to borrow $2 billion to complete the "
  "acquisition. The company needs advice about the purchase and confidence "
  "that it can fund it. A large bank can offer both through different "
  "teams. Bank of America describes this structure on its own site: its "
  "Global Banking and Global Markets divisions operate under the Bank of "
  "America and BofA Securities names, with advisory work done by BofA "
  "Securities and lending by banking affiliates "
  "(<a href=\"https://business.bofa.com/content/boaml.html\">business.bofa.com</a>).",
  "For the buyer, that combination reduces coordination problems, because a "
  "recommendation is more useful when the company already understands how "
  "it could pay for it. The New York Fed authors linked the choice of a "
  "lending bank to access to acquisition financing, which is the same "
  "advantage described from the client's side. My interpretation is that "
  "financing capability gives a bank another reason to be chosen, and that "
  "the size of the advantage depends on what the transaction requires.",
  "A company's own board can state this logic in a filing. When Splunk "
  "chose advisers for its 2023 sale to Cisco, its proxy statement said it "
  "retained Morgan Stanley partly because the bank had “served as a lead "
  "underwriter on various Splunk capital markets transactions, including its "
  "initial public offering” "
  "(<a href=\"https://www.sec.gov/Archives/edgar/data/1353283/000114036123050211/ny20011269x2_defm14a.htm\">Splunk proxy statement</a>). "
  "The board treated the bank's earlier work arranging money as a reason to "
  "trust its advice.",
 ]),

 ("The conflict and the client's response", [
  "The same advantage creates a tension. If the bank earns fees from "
  "advising the software buyer and from arranging its debt, completing the "
  "acquisition produces revenue from both. The client wants the adviser to "
  "recommend whatever creates the most value, including walking away. The "
  "New York Fed authors identified conflicts associated with advising and "
  "lending to the same acquirer, including the bank's existing and "
  "prospective credit exposure.",
  "Independence does not remove every incentive. Evercore states that it is "
  "“not paid until the successful consummation of the transactions,” and "
  "advisory fees that depend on completion give any adviser a reason to "
  "favor a deal that closes. The question a client can ask of every adviser "
  "is how it gets paid and how that could influence its recommendation.",
  "A client can combine advantages. Our software buyer could hire an "
  "independent firm for acquisition advice and use a large bank for "
  "financing, or appoint several advisers with different strengths. A "
  "lender has the advantage when financing is difficult. An industry "
  "specialist has it when understanding the asset requires unusual "
  "expertise. A trusted adviser has it when a board faces a decision it has "
  "never encountered. A division of the market into large banks that advise "
  "buyers and independent firms that advise sellers misses this, because "
  "buyers need independent judgment, sellers may value a large bank's "
  "industry knowledge and relationships, and a particular banker's "
  "experience can outweigh the institution's model.",
 ]),

 ("Reputation as a constraint", [
  "An adviser may gain from completing a transaction today. It also wants "
  "the client's next assignment and recommendations to other executives, and "
  "those future opportunities give it a reason to protect the quality of its "
  "advice. A recommendation to abandon a deal can therefore have commercial "
  "value, because the adviser gives up a fee and gives the client evidence "
  "that its judgment can be trusted.",
  "That outcome depends on how much the adviser values future business, so "
  "reputation encourages good advice without guaranteeing it, and clients "
  "still need to evaluate each recommendation. It also helps explain why "
  "senior bankers matter so much to their firms. Evercore lists the "
  "departure of senior professionals as a risk that “could jeopardize our "
  "relationships with clients and result in the loss of client engagements "
  "and revenues.”",
 ]),

 ("The strongest objection", [
  "The New York Fed study covers a historical sample, and the market "
  "has changed since. Boards now run formal competitions among advisers more "
  "often and hire several at once, which would reduce the weight of any one "
  "relationship. If that is right, lending relationships and coverage "
  "should predict mandates less than they once did.",
  "That is testable. The adviser lists in merger filings show whether the "
  "bank that lent to an acquirer in the preceding years is still the one "
  "named on its acquisitions, and whether independent firms appear more "
  "often alongside the lenders than they did. A pattern of acquirers hiring "
  "their own lenders would support the argument here, and a pattern of "
  "unconnected advisers would weaken it.",
 ]),

 ("What a reader should take from it", [
  "The next time you read an acquisition announcement, look at the advisers "
  "alongside the purchase price. Consider what the buyer needed to "
  "finance, what expertise the transaction required and which relationships "
  "may have influenced the choice, using merger filings and financing "
  "announcements to investigate each. Each bank can then be read as a "
  "business that was chosen to solve a particular problem, and the pattern of "
  "who advises and who lends in a deal shows how its principals judged "
  "their own risks.",
 ]),
]

TAKEAWAY = ""

SOURCES = [
 "Evercore Inc., Form 10-K for fiscal year 2025, on the founding belief, fee timing and the risk from senior departures. "
 "<a href=\"https://www.sec.gov/Archives/edgar/data/1360901/000162828026010273/evr-20251231.htm\">sec.gov</a>",
 "Linda Allen, Julapa Jagtiani, Stavros Peristiani and Anthony Saunders, “The Role of Bank Advisors in Mergers and Acquisitions,” Federal Reserve Bank of New York Staff Report 143, February 2002. "
 "<a href=\"https://www.newyorkfed.org/research/staff_reports/sr143.html\">newyorkfed.org</a>",
 "Centerview Partners, strategic advisory page. "
 "<a href=\"https://centerviewpartners.com/corporateadvisory.aspx\">centerviewpartners.com</a>",
 "Bank of America, business site, on the Global Banking and Global Markets divisions and the BofA Securities name. "
 "<a href=\"https://business.bofa.com/content/boaml.html\">business.bofa.com</a>",
 "The $5 billion acquisition and $2 billion borrowing are hypothetical.",
]
