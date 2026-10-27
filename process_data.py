"""The whole sell-side business on one page.

Part One is how the bank gets chosen, carried over from The Mandate, which was
this same subject arriving a page early. Winning the assignment is stage one of
selling a company, so the two were always one piece.

Part Two is the standard sequence, stage by stage, with the problem each stage
solves for the seller. Its real-world evidence is the Background of the Merger
section of Splunk's 2023 proxy, which records a sale with one bidder and no
market check.

Part Three is my own argument, about the unit this industry is measured in and
the unit a nineteen year old is actually choosing between.

No em dashes, no semicolons.
"""

KICKER = "Sell-side M&amp;A"
PART1_H = "Part One. How the bank gets chosen"
PART2_H = "Part Two. The eight stages"
PART3_H = "Part Three. What this means if you are nineteen"
TITLE = "How a Company Gets Sold"
LEDE = ("A sale process is a sequence built to control what each buyer knows "
        "and when, and to make buyers compete. Before any of it starts, "
        "somebody has to be chosen to run it, and that choice is made long "
        "before anything is for sale.")

INTRO = [
 "A software company agrees to buy a competitor for $5 billion. The "
 "announcement explains the price and the strategic rationale and, near the "
 "bottom, names the investment banks that advised each side. Each of those "
 "banks had to win the assignment, which is called the mandate, by persuading "
 "a company to trust it with a decision that could change its future.",
 "An owner could sell a business without help, and very few do. Selling "
 "requires knowing what the business is worth, who would want it and what "
 "separates it from the other companies a buyer is looking at that quarter. "
 "Each of those is a full-time question and the owner is already occupied. "
 "So a bank is hired to run the process.",
 "My argument is that the standard sequence below is best understood as a "
 "set of solutions. The bake-off solves the problem of choosing an adviser "
 "whose quality cannot be tested. Preparation and the documents solve the "
 "problem of making the company legible to strangers. Marketing, meetings "
 "and bids solve the problem of finding the highest price without losing "
 "control of the information. Diligence and completion solve the problem of "
 "keeping a price once it has been agreed. The sequence is the standard "
 "version, and it usually runs from three months to several years. Not every "
 "sale follows it, and the last section uses a sale that did not.",
 "This page runs in three parts. How the bank is chosen, which is settled "
 "before anything is for sale. What the bank then does, in order, with "
 "roughly how long each stage takes. And what both of those mean if you are "
 "nineteen and trying to decide which of these firms to join.",
]

# ======================================= PART ONE: GETTING HIRED ===
# Carried over from The Mandate, which was this same subject arriving a
# page early. Winning the assignment is stage one of selling a company.
PART1 = [
 ('Two views of what an adviser is for', [
  'Independent advisory firms present objectivity as their main reason to be chosen. Evercore says in its annual report that it “was founded on the belief that there is an opportunity within the investment banking industry for a firm free of the potential conflicts of interest created within large, multi-product, capital intensive financial institutions” (<a href="https://www.sec.gov/Archives/edgar/data/1360901/000162828026010273/evr-20251231.htm">Evercore 10-K</a>). Centerview describes its advice as independent and “unencumbered by institutional constraints or conflicts of interest” (<a href="https://centerviewpartners.com/corporateadvisory.aspx">Centerview</a>).',
  'A study by four economists at the Federal Reserve Bank of New York points the other way. Linda Allen, Julapa Jagtiani, Stavros Peristiani and Anthony Saunders found in 2002 that “acquirers tend to choose their own banks” as merger advisers, meaning banks that already lent to them (<a href="https://www.newyorkfed.org/research/staff_reports/sr143.html">New York Fed, Staff Report 143</a>). The sample is historical, but it shows that a bank\'s lending relationship was commercially valuable to the client when it chose an adviser.',
  'Both observations are accurate, and they describe different clients with different problems.',
 ]),
 ('Why relationships decide', [
  'On a $5 billion purchase, a one percent difference in price is $50 million. A useful adviser might help the buyer avoid paying that extra amount, might recognize that the business deserves a higher price, or might tell the buyer to stop negotiating altogether. The client is paying for judgment whose quality becomes clear only after the decisions have been made. A polished presentation demonstrates preparation and shows little about how someone will behave when a negotiation turns difficult.',
  'Relationships address that problem by giving the client evidence before the transaction. Banks organize teams around industries so their people stay close to potential clients. A banker covering software can study competitors, follow management changes and bring executives ideas long before there is a deal to discuss.',
  'Consider two hypothetical bankers approaching the same chief executive. One arrives when a sale becomes likely. The other has spent years offering useful observations about the business, including reasons to reject earlier acquisition ideas. The second has given the executive more evidence on which to judge the advice. A formal pitch can still matter, but the relationship shapes how the client weighs what it hears.',
 ]),
 ('Why financing changes the choice', [
  'Now suppose the buyer needs to borrow $2 billion to complete the acquisition. The company needs advice about the purchase and confidence that it can fund it. A large bank can offer both through different teams. Bank of America describes this structure on its own site: its Global Banking and Global Markets divisions operate under the Bank of America and BofA Securities names, with advisory work done by BofA Securities and lending by banking affiliates (<a href="https://business.bofa.com/content/boaml.html">business.bofa.com</a>).',
  "For the buyer, that combination reduces coordination problems, because a recommendation is more useful when the company already understands how it could pay for it. The New York Fed authors linked the choice of a lending bank to access to acquisition financing, which is the same advantage described from the client's side. My interpretation is that financing capability gives a bank another reason to be chosen, and that the size of the advantage depends on what the transaction requires.",
  'A company\'s own board can state this logic in a filing. When Splunk chose advisers for its 2023 sale to Cisco, its proxy statement said it retained Morgan Stanley partly because the bank had “served as a lead underwriter on various Splunk capital markets transactions, including its initial public offering” (<a href="https://www.sec.gov/Archives/edgar/data/1353283/000114036123050211/ny20011269x2_defm14a.htm">Splunk proxy statement</a>). The board treated the bank\'s earlier work arranging money as a reason to trust its advice.',
 ]),
 ("The conflict and the client's response", [
  "The same advantage creates a tension. If the bank earns fees from advising the software buyer and from arranging its debt, completing the acquisition produces revenue from both. The client wants the adviser to recommend whatever creates the most value, including walking away. The New York Fed authors identified conflicts associated with advising and lending to the same acquirer, including the bank's existing and prospective credit exposure.",
  'Independence does not remove every incentive. Evercore states that it is “not paid until the successful consummation of the transactions,” and advisory fees that depend on completion give any adviser a reason to favor a deal that closes. The question a client can ask of every adviser is how it gets paid and how that could influence its recommendation.',
  "A client can combine advantages. Our software buyer could hire an independent firm for acquisition advice and use a large bank for financing, or appoint several advisers with different strengths. A lender has the advantage when financing is difficult. An industry specialist has it when understanding the asset requires unusual expertise. A trusted adviser has it when a board faces a decision it has never encountered. A division of the market into large banks that advise buyers and independent firms that advise sellers misses this, because buyers need independent judgment, sellers may value a large bank's industry knowledge and relationships, and a particular banker's experience can outweigh the institution's model.",
 ]),
 ('Why a firm might advise only sellers', [
  "Part of the conflict just described has nothing to do with lending. It "
  "follows from advising both sides of the same market in different "
  "transactions.",
  "A bank that advises acquirers holds relationships with acquirers. On a "
  "sell-side mandate its duty runs the other way, because the seller is "
  "paying it to take as much money out of the buyer as the buyer will part "
  "with. Performing that duty to the limit is unwelcome to the party across "
  "the table, and that party is a firm the same bank would like to be hired "
  "by next year. So the incentive to press for the last increment of price "
  "is weaker at a bank that wants the buyer as a future client than at one "
  "that does not.",
  "I cannot measure the size of that effect and I would not claim it decides "
  "many outcomes. The claim is narrower. It is a reason a seller might "
  "prefer an adviser with no buy-side business to protect, and unlike the "
  "conflict in the previous section it has nothing to do with a balance "
  "sheet. It would apply to an independent firm that advised both sides just "
  "as it applies to a bank.",
  "Some firms are built so that the question does not arise. Qatalyst "
  "Partners, founded in 2008 by Frank Quattrone, publishes a "
  "<a href=\"https://qatalyst.com/deals/\">deal list</a> of 278 "
  "transactions, and roughly three quarters of them carry a label written "
  "from the target&rsquo;s side, either acquired by or agreement to be "
  "acquired by. Labels written from a buyer&rsquo;s side number in the low "
  "single digits.",
  "That firm does not make the argument I have just made. By "
  "<a href=\"https://www.qatalyst.com/\">its own description</a> it is a "
  "global, independent investment bank providing strategic and "
  "financial advice to senior management and boards, and it says nothing "
  "about conflicts of interest, which is a difference worth noting from "
  "Evercore, quoted earlier, which does make the claim in a filing. The "
  "inference from the composition of a deal list is mine, and a reader "
  "should weigh it as an inference rather than as a position the firm has "
  "taken.",
 ]),

 ('Reputation as a constraint', [
  "An adviser may gain from completing a transaction today. It also wants the client's next assignment and recommendations to other executives, and those future opportunities give it a reason to protect the quality of its advice. A recommendation to abandon a deal can therefore have commercial value, because the adviser gives up a fee and gives the client evidence that its judgment can be trusted.",
  'That outcome depends on how much the adviser values future business, so reputation encourages good advice without guaranteeing it, and clients still need to evaluate each recommendation. It also helps explain why senior bankers matter so much to their firms. Evercore lists the departure of senior professionals as a risk that “could jeopardize our relationships with clients and result in the loss of client engagements and revenues.”',
 ]),
 ('The strongest objection', [
  'The New York Fed study covers a historical sample, and the market has changed since. Boards now run formal competitions among advisers more often and hire several at once, which would reduce the weight of any one relationship. If that is right, lending relationships and coverage should predict mandates less than they once did.',
  'That is testable. The adviser lists in merger filings show whether the bank that lent to an acquirer in the preceding years is still the one named on its acquisitions, and whether independent firms appear more often alongside the lenders than they did. A pattern of acquirers hiring their own lenders would support the argument here, and a pattern of unconnected advisers would weaken it.',
 ]),
]

# =============================== PART THREE: THE UNIT BEING MEASURED ===
# My own argument. Hard to see from outside, because every source a student
# can reach is organised by institution.
PART3 = [

 ("The unit everyone measures is the wrong one", [
  "Everything above is about an institution. The people recruiting into this "
  "industry almost never are.",
  "A student choosing between banks reads league tables, which rank firms by "
  "the value of the deals they advised on. The tables are real and they "
  "measure something. They also measure the wrong unit. A bank does not have "
  "relationships. The people inside it do, and Evercore says so to the SEC, "
  "listing the departure of senior professionals as a risk that could "
  "jeopardise its relationships with clients and result in the loss of client "
  "engagements and revenues. A firm that discloses its dependence on "
  "individuals in its own annual report is telling you where the asset sits.",
  "Follow that through the stages above. The mandate in stage one comes from "
  "a managing director who has spent years in front of an owner with nothing "
  "to sell. The pitch is built by the team. The reason the pitch is being "
  "heard at all usually belongs to one person. If that person leaves, the "
  "pitches keep getting built and fewer of them get heard.",
  "So the question a student is really asking, without knowing it, is not "
  "which bank. It is which five or six people.",
 ]),

 ("Two analysts, same firm, different jobs", [
  "Two people can join the same firm in the same city in the same month and "
  "have unrecognisably different two years.",
  "One lands in a group whose managing director is winning live sell-side "
  "mandates. That analyst spends the year inside the sequence above, turning "
  "a company&rsquo;s records into something a stranger can read, sitting on "
  "the calls where bids come back, watching a board decide whether to run a "
  "market check. The other lands in a group whose coverage list is quiet and "
  "builds pitch books for meetings that do not convert. Same logo on the "
  "building, same training, same pay. Different job, and after two years a "
  "different set of things that person can credibly say they have done.",
  "The industry does not hide this. It is invisible from outside because "
  "every source a student can reach is organised by institution. League "
  "tables are by institution. Rankings are by institution. Recruiting is by "
  "institution, and it has to be, since a firm hires for the whole firm and "
  "does not yet know which group will have the opening.",
 ]),

 ("The work is set by the client, not by the title", [
  "The same argument explains something about the job that recruiting "
  "materials describe poorly. An analyst&rsquo;s week is determined by what "
  "a particular client is asking for at that moment, which is why the work "
  "varies so much between people with identical titles.",
  "Two examples make the range clear. A buyer considering a target wants to "
  "know what it has historically cost to acquire companies of that kind, so "
  "the work is valuation: trading comparables, precedent transactions, how "
  "the multiple paid for similar businesses has moved over recent years, and "
  "what that implies about whether the current price is high or low. Another "
  "client is not asking about price at all. It has a specific counterparty "
  "in mind and wants the case for why the two businesses belong together, so "
  "the work is research and argument, and weeks can pass without a valuation "
  "being built.",
  "Both are the job. Neither is more senior than the other. Which one a "
  "person spends a year doing is a function of the clients their group "
  "happens to be serving, which is settled by the relationships described in "
  "Part One and not by anything the person controls.",
 ]),

 ("What to ask instead", [
  "Ask who the senior people in the group are and what they have closed in "
  "the past two years, by name. Ask how long they have been there. Ask who "
  "left recently and where they went.",
  "These are polite questions and bankers usually answer them, because a good "
  "answer is a source of pride. A group that deflects has also answered.",
  "The last thing worth knowing is that a league table is a lagging indicator "
  "of where people were. Bankers move, and their mandates follow on a delay "
  "of a year or two, which is roughly the length of an analyst programme.",
 ]),
]

# (roman, name, duration, [paragraphs])
STAGES = [

 ("I", "Choosing the bank", "One to two weeks", [
  "Several banks are invited to present on why they should sell the "
  "company, an exercise the industry calls a bake-off. The problem it "
  "addresses is that the owner is paying for judgment whose quality cannot be "
  "checked in advance, so the pitch is a way to look for evidence of care and "
  "of understanding the business.",
  "The outcome is often decided before the meeting. Senior bankers spend "
  "years in contact with owners who have nothing to sell, bringing them "
  "observations about competitors and about what similar businesses have "
  "fetched, so by the time a sale is real the owner often has a view "
  "already, for the reasons set out in Part One.",
  "That does not make the meeting ceremonial. A managing director is paid on "
  "the mandates brought in, so the pitch decides a large share of several "
  "people's income for the year, and the presentation is built by analysts "
  "and associates in a week or two. It can be built that quickly because "
  "much of it already exists. A firm that covers a sector holds its previous "
  "market analyses and precedent transaction work, and a new pitch is "
  "assembled from that stock as much as it is written.",
  "The years of contact that settle the outcome are unpaid. A bank bills for "
  "transactions and not for meetings, so the coverage work that produces a "
  "mandate is carried as a cost against a fee that may never arrive. That is "
  "the commercial reason banks organise by sector rather than by deal. A "
  "team that appears only once a sale is live has no way to accumulate the "
  "evidence the owner is looking for, and it is bidding against people who "
  "have been accumulating it for years. Banks lose these competitions, and "
  "two weeks of work ends with no fee at all.",
 ]),

 ("II", "Preparation", "Two to four months", [
  "Once the bank has won, nothing is for sale yet. The problem now is that a "
  "buyer will not trust a profit figure the seller prepared itself. An "
  "independent accounting firm is therefore brought in to examine the "
  "company's earnings, in what is called a quality of earnings review, which "
  "checks that the profit is real, repeatable and not the result of one "
  "unusual year. The seller commissions it so that the buyer's own "
  "examination finds nothing the seller has not already found.",
  "While that runs, the bank assembles answers to the questions every buyer "
  "asks, which run to several hundred. They cover financial statements and "
  "projections, customer contracts, legal standing, litigation and how "
  "concentrated the customer base is. Some answers are so routine that "
  "their absence becomes the finding, because a buyer who asks for revenue by "
  "customer and does not receive it concludes either that the company does "
  "not know or that it would prefer not to say.",
  "The financial model is the visible deliverable and not the largest part "
  "of the work. A company records what it needs in order to run itself, "
  "which is not what a stranger needs in order to value it, and the gap "
  "between those two things is what this stage closes. Most of the hours go "
  "into converting records that were never kept for this purpose into "
  "analysis a buyer can read without having to trust the seller.",
 ]),

 ("III", "The documents", "Runs alongside preparation", [
  "Three documents carry the sale, and they are written in a deliberate "
  "order of disclosure so that the seller reveals more only as a buyer shows "
  "more interest. The teaser is one or two pages and usually does not name "
  "the company. It describes the business well enough for a buyer to know "
  "whether it is interested, and not well enough to identify it. The "
  "confidential information memorandum, called the CIM, runs fifty pages or "
  "more and is the full argument: what the company does, why it wins, what "
  "the numbers have been doing and where growth is supposed to come from. "
  "The management presentation is the deck the chief executive uses to talk "
  "through the business in a meeting.",
  "All three are marketing documents and also the company's formal argument "
  "about itself. Writing them well requires understanding both what the "
  "business does and what a particular kind of buyer is listening for.",
 ]),

 ("IV", "Marketing", "Four to eight weeks", [
  "The teaser goes out, usually by email from a senior banker to people he "
  "knows. The seller's problem here is a trade-off between price and secrecy. "
  "Breadth finds the highest price, and narrowness keeps the sale quiet, which "
  "matters when employees, customers and competitors would all behave "
  "differently if they knew. A middle-market business affordable to many "
  "buyers might be shown to two hundred parties, and a large or sensitive "
  "asset might be shown to eight.",
  "A buyer who wants more signs a non-disclosure agreement, then receives the "
  "CIM. Meanwhile the bank builds a data room, a secure file system holding "
  "the prepared answers, with access staged. Early buyers see one layer and "
  "serious buyers see more. The sequencing is part of the design, and a "
  "buyer who has been through several of these reads the pacing as well as "
  "the files.",
 ]),

 ("V", "Management meetings", "Two to four weeks", [
  "Buyers who are still interested meet the management team, and the bank "
  "rehearses the team first. Running a company and explaining it to a "
  "skeptical buyer are different skills, and the second is rarely practised "
  "because the occasion to use it is rare. The questions that land badly are "
  "predictable, so they are rehearsed. Management's credibility is part of "
  "what a buyer is pricing, which is why the meeting receives that "
  "preparation.",
 ]),

 ("VI", "First bids", "One week, then a decision", [
  "Buyers submit an indication of interest, a number with almost no "
  "commitment that is not binding and will move. Its purpose is sorting. The "
  "number separates the buyers who want the business from those who were "
  "curious, and it gives the first reading of where the market is and not "
  "where the seller hoped it would be.",
  "The bank then presents every bid to the owner with its own view of what "
  "the company is worth and which buyer it would prefer to deal with in two "
  "months. In Splunk's 2023 sale, Cisco's first indication was $130 a "
  "share in cash. The board's transaction committee judged it “not "
  "compelling” and told Cisco it did not reflect Splunk's standalone value "
  "(<a href=\"https://www.sec.gov/Archives/edgar/data/1353283/000114036123050211/ny20011269x2_defm14a.htm\">Splunk proxy statement</a>).",
 ]),

 ("VII", "Final bids and negotiation", "Four to six weeks", [
  "The field narrows, and the remaining buyers get deeper access and "
  "answers to specific questions. The senior banker's work here is hard "
  "to teach. He is on calls the seller is not on, telling "
  "a buyer what it would take to end the competition. A price above a "
  "certain figure might win exclusivity, meaning everyone else is sent "
  "home. He has to make each buyer believe it can win at a price good for the "
  "seller without pushing so hard that a buyer leaves and the process has one "
  "fewer bidder.",
  "With one bidder the same work becomes a negotiation, and the Splunk record "
  "shows it in detail. Cisco offered $142 on 25 August 2023. Splunk countered "
  "at $168. Cisco moved to $146, Splunk to $160, and Cisco to $152 and then "
  "$156 on 30 August, when Splunk indicated it would accept $158. Cisco made a "
  "verbal offer of $157 on 31 August and proposed exclusivity. In six days "
  "the gap between the sides closed from $26 to $1.",
  "Binding offers then arrive, in a letter of intent, and one is accepted.",
 ]),

 ("VIII", "Diligence and completion", "Two to four months", [
  "Having agreed a price, the winning buyer now looks for reasons the price "
  "should be lower. That is the function of confirmatory diligence rather "
  "than a breach of the bargain, and if the "
  "preparation in the second stage was done properly there is little left to "
  "find. Where something is found, it is negotiated into the purchase "
  "agreement, a long document that specifies what adjusts the price, how much "
  "cash stays in the business and what happens to the management team.",
  "The agreement also allocates the risk that the deal will not close. "
  "Splunk's agreement provided for a $1 billion fee payable by Splunk to "
  "Cisco in specified circumstances and $1.478 billion payable by Cisco to "
  "Splunk in others. Signing came on 20 September 2023, followed by "
  "regulatory filings and, in Cisco's case, completion on 18 March 2024. "
  "Afterward the junior team documents the transaction, which takes longer "
  "than anyone expects, because the record becomes the credential the bank "
  "shows the next client.",
 ]),
]

CLOSE_HEAD = "When the sale is not an auction"
CLOSE = [
 "The sequence above describes a competitive sale, and Splunk's was not one. "
 "Cisco first approached Splunk's chair in November and December 2021 and "
 "made an unsolicited indication of $165 to $175 a share on 17 December. "
 "Its indication rose to $193 in February 2022, Splunk's chair countered at "
 "$212, and Cisco withdrew the same day, citing concerns about Splunk's "
 "search for a chief executive. Cisco returned in April 2023, and after "
 "its $130 indication the board decided against running a market check "
 "because it judged that no other party was likely to be interested. On 1 "
 "September 2023 it decided again not to run one, so the proxy records no "
 "other buyer being contacted in 2023. The final price of $157 was below "
 "Cisco's own indication of $193 in February 2022.",
 "The strongest objection to the argument of this page is that the "
 "standard sequence is a textbook and that real sales rarely follow it. I "
 "agree that this one did not, and I read the example as supporting the "
 "argument. The stages still describe the problems a seller has, and the "
 "board's decision to skip the competition was a judgment about one of "
 "them. A seller that skips the market check is accepting the risk that "
 "another buyer would have paid more, in exchange for secrecy and speed, "
 "and the shareholders who approved the deal were told so in the proxy.",
 "A reader should therefore look for two things in any sale. One is the "
 "description of the process in the merger filing, called the Background of "
 "the Merger, which records who approached whom, how many buyers were "
 "contacted and whether a market check was run. The other is the price "
 "history in that section, because a final price that is lower than an "
 "earlier offer, as here, shows how much the conditions around the sale "
 "mattered. Failed or paused processes are common as well, and they appear "
 "in the record only when the company chooses or is required to disclose "
 "them.",
]

NOTE = ("The argument about advising only sellers is mine. Its factual basis is Qatalyst&rsquo;s published deal list and its own description of itself, both read in October 2026, and the firm makes no claim about conflicts. The account of what analyst work consists of comes from practitioner accounts rather than from filings. Part One otherwise cites Evercore&rsquo;s annual report, the New York Fed staff "
        "report by Allen, Jagtiani, Peristiani and Saunders, whose findings "
        "describe a historical sample, Bank of America&rsquo;s description of "
        "its own structure, and Splunk&rsquo;s merger proxy. Part Three is my "
        "own argument, built on the Evercore disclosure and on how the stages "
        "above work. Part Two sources: the Background of the Merger section and the termination fee "
        "terms of Splunk's definitive proxy statement of October 2023, "
        "<a href=\"https://www.sec.gov/Archives/edgar/data/1353283/000114036123050211/ny20011269x2_defm14a.htm\">sec.gov</a>. "
        "Stage durations are typical ranges and vary by transaction.")
