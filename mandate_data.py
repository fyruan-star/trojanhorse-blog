"""How a bank wins the assignment, which is the part nobody writes about.

Every company claim here is checked against a primary source. The Evercore
language is quoted from its own 10-K. The New York Fed finding is from the
staff report itself. Where a source is dated, the text says so.

Plain register. No em dashes, no semicolons, no punchline endings.
"""

KICKER = "The strategy and incentives behind investment banking"
TITLE = "How Banks Win the Mandate"
LEDE = "Why a company chooses one adviser over another."

# a section with an empty heading prints as plain paragraphs
SECTIONS = [

 ("", [
  "Imagine a software company agrees to buy a competitor for $5 billion. The "
  "announcement explains the price, the strategic rationale, and the expected "
  "benefits. Near the bottom, it names the investment banks that advised each "
  "side.",
  "Those names deserve some attention. Each bank had to persuade a company to "
  "trust it with a decision that could change the company&rsquo;s future. "
  "Understanding how it won that trust tells you something about the "
  "transaction itself.",
  "That is the idea behind The Trojan Horse. I want to make the strategy "
  "inside investment banking understandable to people outside the industry. "
  "There are interesting problems here: how companies negotiate, how advisers "
  "build an advantage, and how incentives influence decisions involving "
  "billions of dollars. You should be able to understand those problems "
  "without having worked at a bank.",
  "A useful place to begin is the mandate, which is simply the assignment to "
  "advise a client.",
  "Before a bank can help a company buy or sell a business, it has to win that "
  "assignment. That competition explains a surprising amount about how "
  "investment banking works.",
 ]),

 ("The company is buying judgment", [
  "Return to the software acquisition. The buyer needs to decide what the "
  "competitor is worth, how much it can afford to pay, and whether owning the "
  "business would improve its position. It also needs to consider the "
  "seller&rsquo;s alternatives. A rival bidder could change the negotiation. "
  "So could the seller&rsquo;s willingness to remain independent.",
  "Financial analysis helps answer these questions. The difficult part is "
  "deciding which assumptions deserve confidence and how to act while "
  "important facts remain uncertain.",
  "On a $5 billion purchase, a 1 percent difference in price is $50 million. A "
  "useful adviser might help the buyer avoid paying that extra amount. It "
  "might also recognize that the business deserves a higher price, or that the "
  "buyer should stop negotiating altogether.",
  "This makes choosing an adviser difficult. The client is paying for judgment "
  "whose quality will become clearer only after decisions have been made. A "
  "polished presentation can demonstrate preparation. It offers less certainty "
  "about how someone will behave when a negotiation becomes difficult.",
  "Relationships help address that problem.",
  "Banks organize teams around industries so their people can develop "
  "expertise and stay close to potential clients. A banker covering software "
  "can study competitors, follow management changes, and bring executives "
  "ideas before there is a transaction to discuss.",
  "Consider two bankers approaching the same chief executive. One arrives when "
  "a sale becomes likely. The other has spent years offering useful "
  "observations about the business, including reasons to reject previous "
  "acquisition ideas. The second banker has given the executive more evidence "
  "on which to judge the advice.",
  "A formal pitch can still matter. The relationship influences how the client "
  "evaluates what it hears.",
 ]),

 ("Financing changes the choice", [
  "Now suppose our buyer needs to borrow $2 billion to complete the "
  "acquisition.",
  "The adviser selection becomes more complicated. The company needs advice "
  "about the purchase and confidence that it can fund it.",
  "A large bank can offer several services through different teams, including "
  "acquisition advice, lending, and help raising money from investors. Bank of "
  "America describes this combination explicitly in its corporate and "
  "investment banking business.",
  "For the buyer, that combination can reduce coordination problems. A "
  "recommendation becomes more useful when the company understands how it "
  "could pay for it.",
  "There is historical evidence that lending relationships influence adviser "
  "selection. A 2002 New York Fed study by Linda Allen, Julapa Jagtiani, "
  "Stavros Peristiani, and Anthony Saunders found that acquirers tended to "
  "hire banks that already lent to them. The authors linked that choice to "
  "access to acquisition financing. Their findings describe a historical "
  "sample, but they help explain the commercial logic of combining lending and "
  "advice.",
  "My interpretation is straightforward: financing capability gives a bank "
  "another reason for the client to choose it. The size of that advantage "
  "depends on what the transaction requires.",
 ]),

 ("The same advantage creates a tension", [
  "Suppose a bank could earn money from advising our software buyer and "
  "arranging its debt. Completing the acquisition could produce revenue from "
  "both activities.",
  "The client wants the adviser to recommend whatever creates the most value, "
  "including walking away. The bank&rsquo;s potential revenues introduce "
  "another consideration. The New York Fed researchers identified conflicts "
  "associated with advising and lending to an acquirer, including the "
  "bank&rsquo;s existing and prospective credit exposure.",
  "This helps explain the appeal of independent advisory firms.",
  "Evercore makes the point in its own annual report, which says the firm was "
  "founded on the belief that there was an opportunity free of the potential "
  "conflicts of interest created within large, multi-product capital intensive "
  "financial institutions. Centerview describes itself more simply as an "
  "independent investment bank providing objective advice. Neither firm lends, "
  "so neither has a loan to protect.",
  "Independence still leaves other incentives to consider. Advisory fees can "
  "depend heavily on completing a transaction. The same Evercore filing states "
  "that the firm earns a majority of its revenue from advisory engagements and "
  "is not paid until the successful consummation of the transactions.",
  "The useful question for a client is how an adviser gets paid and how that "
  "could influence its recommendations.",
 ]),

 ("The client can combine advantages", [
  "Our software buyer could hire an independent firm for acquisition advice "
  "and use a large bank for financing. It could also appoint multiple advisers "
  "with different strengths.",
  "This is why a simple division between large banks advising buyers and "
  "independent firms advising sellers misses too much. Buyers need independent "
  "judgment. Sellers may value a large bank&rsquo;s industry knowledge and "
  "relationships. A particular banker&rsquo;s experience can matter more than "
  "the institution&rsquo;s general business model.",
  "The strategic problem for each bank is to identify where its strengths "
  "matter enough to win the assignment.",
  "A lender may have an advantage when financing is difficult. An industry "
  "specialist may have an advantage when understanding the asset requires "
  "unusual expertise. A trusted adviser may have an advantage when a board "
  "faces a decision it has never encountered before.",
  "The strongest proposition depends on the client&rsquo;s problem.",
 ]),

 ("Reputation changes the incentives", [
  "There is a game theory problem here that I find especially interesting.",
  "An adviser may benefit financially from getting a transaction completed "
  "today. It also wants the client&rsquo;s next assignment and recommendations "
  "to other executives. Those future opportunities give it a reason to protect "
  "the quality of its advice.",
  "A recommendation to abandon a deal can therefore have commercial value. The "
  "adviser gives up a potential fee while giving the client evidence that its "
  "judgment can be trusted.",
  "That outcome depends on the value placed on future business. Reputation "
  "creates an incentive for good advice, but clients still need to evaluate "
  "each recommendation.",
  "It also helps explain why senior bankers matter so much to their firms. "
  "Their expertise and client relationships influence future revenue. Evercore "
  "lists the departure of senior professionals as a risk, warning that it "
  "could jeopardize relationships with clients and result in the loss of "
  "client engagements and revenues.",
 ]),

 ("Read the adviser list differently", [
  "The next time you read an acquisition announcement, look at the advisers "
  "alongside the purchase price. Consider what the buyer needed to finance, "
  "what expertise the transaction required, and which relationships might have "
  "influenced the choice. Merger filings and financing announcements can help "
  "you investigate those possibilities.",
  "You will begin to see each bank as a business competing to solve a "
  "particular problem.",
  "That is what I want The Trojan Horse to help you understand: how the people "
  "involved assess their options, respond to incentives, and earn the right to "
  "influence a consequential decision.",
 ]),
]

TAKEAWAY = ""
SOURCES = []
