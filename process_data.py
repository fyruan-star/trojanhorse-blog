"""How a company actually gets sold, stage by stage.

The standard sequence is described stage by stage, with the problem each stage
solves for the seller. The real-world evidence is the Background of the Merger
section of Splunk's 2023 proxy statement, which records a sale with one bidder
and no market check. Durations are typical ranges and vary by deal.

No em dashes, no semicolons.
"""

KICKER = "Sell-side M&amp;A"
TITLE = "How a Company Gets Sold"
LEDE = ("A sale process is a sequence built to control what each buyer knows "
        "and when, and to make buyers compete. Each stage solves a specific "
        "problem for the seller, and a real sale shows which of those "
        "problems were present.")

INTRO = [
 "An owner could sell a business without help, and very few do. Selling "
 "requires knowing what the business is worth, who would want it and what "
 "separates it from the other companies a buyer is looking at that quarter. "
 "Those are full-time questions, and the owner already has a full-time job. "
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
  "already. The piece on <a href=\"strategemata.html\">how banks win the "
  "mandate</a> gives the evidence for that.",
  "That does not make the meeting ceremonial. A managing director is paid on "
  "the mandates brought in, so the pitch decides a large share of several "
  "people's income for the year, and the presentation is built by analysts "
  "and associates in a week or two. Small errors matter for a reason "
  "of inference and not of vanity. An owner reading a hypothetical deck with "
  "misaligned logos may conclude the firm would be equally careless with the "
  "sale. Banks lose these competitions, and two weeks of work ends with no "
  "fee at all.",
 ]),

 ("II", "Preparation", "Two to four months", [
  "Once the bank has won, nothing is for sale yet. The problem now is that a "
  "buyer will not trust a profit figure the seller prepared itself. An "
  "independent accounting firm is therefore brought in to examine the "
  "company's earnings, in what is called a quality of earnings review, which "
  "checks that the profit is real, repeatable and not the result of one "
  "unusual year. It plays the role of a structural survey commissioned "
  "before listing a house, so that the buyer's own surveyor finds nothing "
  "the seller has not already seen.",
  "While that runs, the bank assembles answers to the questions every buyer "
  "asks, which run to several hundred. They cover financial statements and "
  "projections, customer contracts, legal standing, litigation and how "
  "concentrated the customer base is. Some answers are so routine that "
  "their absence becomes the finding, because a buyer who asks for revenue by "
  "customer and does not receive it concludes either that the company does "
  "not know or that it would prefer not to say.",
  "A hypothetical example shows the kind of work involved. A buyer wants to "
  "know customer concentration, repeat purchase rates and geographic spread. "
  "The company has never produced that analysis. What it can produce is a "
  "file of every transaction it has recorded, and someone spends two days "
  "turning it into three charts. The financial model is the visible "
  "deliverable, and much of the effort goes into converting the company's "
  "records into something a stranger can read.",
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
  "rehearses the team first. A chief executive is usually excellent at "
  "running the company and has never had to describe it to a skeptical "
  "stranger holding a checkbook. The questions that land badly are "
  "predictable, so they are practiced. Management's credibility is part of "
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
  "The winning buyer now does something the seller rarely enjoys. Having "
  "agreed a price, it looks for reasons the price should be lower. That is "
  "not bad faith. It is what confirmatory diligence is for, and if the "
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

NOTE = ("Sources: the Background of the Merger section and the termination fee "
        "terms of Splunk's definitive proxy statement of October 2023, "
        "<a href=\"https://www.sec.gov/Archives/edgar/data/1353283/000114036123050211/ny20011269x2_defm14a.htm\">sec.gov</a>. "
        "Stage durations are typical ranges and vary by transaction.")
