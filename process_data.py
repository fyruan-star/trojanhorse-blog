"""How a company actually gets sold, stage by stage.

The mechanics here are standard and widely documented. The texture, meaning
what the work feels like and where the hours actually go, comes from
practitioner accounts rather than filings, and the page says so.

Running analogy is a house sale, used where it illuminates and dropped where
the differences matter more than the resemblance.

Plain register. No em dashes, no semicolons, no punchline endings.
"""

KICKER = "Sell-side M&amp;A"
TITLE = "How a Company Gets Sold"
LEDE = ("A company is sold the way a house is sold, in that somebody is hired "
        "to run the sale. After that the resemblance stops being useful, and "
        "the places where it stops are the interesting part.")

INTRO = [
 "An owner could sell the business without help. In practice very few do. "
 "Owners are in the business of running a business, and selling one requires "
 "knowing what it is worth, who would want it, and what makes it different "
 "from the four other companies a buyer is looking at that quarter. Those are "
 "full-time questions and the owner already has a full-time job.",
 "So a bank is hired to run the process. What follows is that process, in "
 "order, with roughly how long each part takes. The whole thing runs anywhere "
 "from three months to several years.",
]

# (roman, name, duration, [paragraphs])
STAGES = [

 ("I", "The Bake-Off", "One to two weeks", [
  "Several banks are invited to present on why they should be the one to sell "
  "the company. The industry calls it a bake-off. It is the same exercise as "
  "interviewing three estate agents, except the agents arrive with a hundred "
  "pages each.",
  "Here is the part that surprises people. The outcome is often decided before "
  "the meeting. Senior bankers spend years in contact with owners who have "
  "nothing to sell, bringing them observations about competitors, about what "
  "similar businesses have fetched, sometimes about why an approach they have "
  "received is worth ignoring. By the time a sale is real, the owner usually "
  "has a view already.",
  "That does not make the pitch ceremonial. A managing director is paid on the "
  "mandates brought in, so the meeting decides a large share of several "
  "people&rsquo;s income for the year. The presentation itself is built by "
  "analysts and associates in a week or two.",
  "This explains behaviour that looks irrational from outside. A managing "
  "director will send a deck back at one in the morning because two logos are "
  "misaligned. The reasoning is that an owner looking at a careless document "
  "will wonder how carefully the same firm would handle the sale. The logo is "
  "a proxy and everyone in the room knows it is a proxy.",
  "Banks lose these. Two weeks of work ends with somebody else getting the "
  "assignment and no fee at all.",
 ]),

 ("II", "Preparation", "Two to four months", [
  "The bank has won. Nothing is for sale yet.",
  "First an independent accounting firm is brought in to examine the "
  "company&rsquo;s earnings. This is a quality of earnings review, usually "
  "shortened to QoE, and it checks that the profit figure is real, repeatable "
  "and not the product of one unusual year. It is the equivalent of the seller "
  "commissioning a structural survey before listing, so that the buyer&rsquo;s "
  "own surveyor finds nothing the seller has not already seen.",
  "While that runs, the bank assembles answers. There is a standard set of "
  "questions every buyer asks, and it runs to several hundred. Financial "
  "statements and projections. Customer contracts. Evidence the company is "
  "legally what it says it is. Any litigation. Who the customers are and how "
  "concentrated they are.",
  "Some of those answers are so routine that their absence becomes the "
  "finding. A buyer who asks for revenue by customer and does not receive it "
  "concludes either that the company does not know, or that it would rather "
  "not say. Both are answers.",
  "The work is mostly not what undergraduates expect. Building the financial "
  "model is a visible deliverable and a small share of the hours. Practitioners "
  "put it at around a sixth of the time on a sell-side process. The rest is "
  "turning a company&rsquo;s actual records into something a stranger can read.",
  "A concrete version. A buyer wants to know customer concentration, repeat "
  "purchase rates and geographic spread. The company has never produced that "
  "analysis, or produced it once, a year ago. What it can produce is a file of "
  "every transaction it has ever recorded. Somebody then spends two days in a "
  "spreadsheet turning that into three charts.",
 ]),

 ("III", "The Documents", "Runs alongside preparation", [
  "Three documents carry the sale, and they are written in a deliberate order "
  "of disclosure.",
  "<strong>The teaser</strong> is one or two pages and usually does not name "
  "the company. It describes the business well enough for a buyer to know "
  "whether it is interested and not well enough to identify it. A listing with "
  "the address withheld.",
  "<strong>The confidential information memorandum</strong>, the CIM, runs "
  "fifty pages or more. It is the full argument: what the company does, why it "
  "wins, what the numbers have been doing, where the growth is supposed to "
  "come from.",
  "<strong>The management presentation</strong> is the deck the chief "
  "executive uses to talk through the business in a meeting. It exists to "
  "structure a conversation rather than to be read alone.",
  "All three are marketing documents and all three are also the "
  "company&rsquo;s formal argument about itself. Getting them right requires "
  "understanding both what the business does and what a particular kind of "
  "buyer is listening for, which is why this part takes strategy and not only "
  "hours.",
 ]),

 ("IV", "Marketing", "Four to eight weeks", [
  "The teaser goes out, usually by email from a senior banker to people he "
  "knows.",
  "How many people depends entirely on the deal. A middle market business "
  "affordable to many buyers might be shown to two hundred parties. A large or "
  "sensitive asset might be shown to eight. Breadth finds the highest price. "
  "Narrowness keeps the sale quiet, which matters when employees, customers and "
  "competitors would all behave differently if they knew.",
  "A buyer who wants more signs a non-disclosure agreement first, negotiated "
  "between the two sets of lawyers with junior bankers in the middle. Then the "
  "CIM goes over.",
  "Meanwhile the data room is built. This is a secure file system holding the "
  "several hundred prepared answers, and access to it is staged rather than "
  "granted all at once. Early buyers see one layer. Serious buyers see more. "
  "The sequencing is part of the process design, and a buyer who has been "
  "through a few of these reads the pacing as well as the files.",
 ]),

 ("V", "Management Meetings", "Two to four weeks", [
  "Buyers who are still interested meet the management team.",
  "The bank rehearses them first. A chief executive is usually excellent at "
  "running the company and has never had to describe it to a sceptical "
  "stranger holding a cheque. The questions that land badly are predictable, so "
  "they get practised.",
  "A large and genuinely underreported share of the junior work here is "
  "scheduling. Getting four busy buyers into rooms with one busy management "
  "team, repeatedly, across time zones, is most of several people&rsquo;s week. "
  "Nobody puts that on a recruiting slide and it is a real part of the job.",
 ]),

 ("VI", "First Bids", "One week, then a decision", [
  "Buyers submit an indication of interest, which is a number and almost no "
  "commitment. It is not binding and it will move.",
  "Its purpose is sorting. The number separates the buyers who want the "
  "business from those who were curious, and it gives the first read on where "
  "the market actually is rather than where the seller hoped it would be.",
  "The bank then presents every bid back to the owner alongside its own view of "
  "what the company is worth and who it would rather be dealing with in two "
  "months. This is one of the few moments in the process where the advice is "
  "unambiguously advice.",
 ]),

 ("VII", "Final Bids", "Four to six weeks", [
  "The field narrows. The remaining buyers get deeper access, more meetings and "
  "answers to questions that are now specific rather than standard. A buyer at "
  "this stage is no longer asking what the company does.",
  "Volume becomes the problem. Requests arrive continuously and all of them "
  "need routing, answering and tracking, which is why this stage is staffed the "
  "way it is.",
  "The senior banker&rsquo;s work here is the part that is difficult to teach. "
  "He is on calls the seller is not on, telling a buyer what it would take to "
  "end the competition. A price above a certain figure might win exclusivity, "
  "meaning everyone else is sent home. He has to make each buyer believe it can "
  "win, at a price good for the seller, without pushing so hard that the buyer "
  "leaves and the process has one fewer bidder. Doing that to four parties at "
  "once is most of what the fee is for.",
  "Then binding offers arrive, in a letter of intent, and one of them is "
  "accepted.",
 ]),

 ("VIII", "Diligence and Completion", "Two to four months", [
  "The winning buyer now does something the seller rarely enjoys. Having agreed "
  "a price, it goes looking for reasons the price should be lower.",
  "That is not bad faith. It is what confirmatory diligence is for, and if the "
  "preparation in stage two was done properly there is little left to find. "
  "Where something is found, it gets negotiated into the purchase agreement, "
  "which is a long document specifying what adjusts the price, how much cash "
  "stays in the business, and what happens to the management team.",
  "Then signing, which is when everyone treats it as done, followed by "
  "regulatory filings including antitrust where the size requires it, and "
  "finally closing, when the money actually moves.",
  "Afterwards the junior team documents what happened, which takes longer than "
  "anyone expects, because the record becomes the credential the bank shows the "
  "next client. There is usually a dinner. There is almost always a small "
  "engraved object commemorating the transaction, which bankers accumulate and "
  "display.",
 ]),
]

CLOSE_HEAD = "What this does not tell you"
CLOSE = [
 "The sequence above is the version that works. A great many processes do not "
 "reach the end of it.",
 "Some reach marketing and find that nobody is interested, which is a brutal "
 "and reasonably common outcome. Some find buyers whose numbers never approach "
 "what the owner will accept, and the sale is paused and restarted a year or "
 "two later when the market or the company has changed. Some are agreed and "
 "then die in a regulator&rsquo;s office.",
 "The price itself depends on things largely outside anyone&rsquo;s control. "
 "What else is on the market that quarter. Whether buyers already understand "
 "the category. How many of them there are. The process is run to influence "
 "those conditions at the margin, and the margin is where the fee lives.",
]

NOTE = ("The stages, documents and terminology here are standard and widely "
        "documented. The texture, meaning where the hours actually go and what "
        "the work feels like at each stage, is drawn from practitioner "
        "accounts rather than from filings. Durations are typical rather than "
        "fixed, and a real process can compress or stall at any point.")
