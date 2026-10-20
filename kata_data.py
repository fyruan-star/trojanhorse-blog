"""Ten years of technology coverage, 2016 to 2026.

Every entry carries the same move: the received reading, then the thing in the
belly nobody priced. That device is the point of the section and nothing goes
on the spine without one.

`width` is the spine's thickness for that year. It draws the shape of the
cycle, not a dataset, and the page says so rather than implying a precision it
does not have.

Voice: explain first, be clever second. Deflate the jargon, never the reader.
No em dashes anywhere.
"""

# kind: seal (a deal that closed), column (a deal that died), stone (not a deal)
YEARS = [

 ("2016", 20, [
  ("stone", "", "The finish line",
   "Smartphone shipments stop growing. Every human who was going to buy one "
   "had bought one. You sprint at a finish line for a decade, cross it, and "
   "find there is just more field."),

  ("seal", "Acquisition &middot; $32bn &middot; July", "SoftBank / ARM",
   "Read everywhere as a very expensive bet on phones, by a man famous for very "
   "expensive bets.",
   "ARM does not make chips. It licenses the blueprint and collects a royalty "
   "every time somebody stamps it into silicon. That blueprint was about to "
   "walk into the data centre, which was Intel&rsquo;s house, and into nearly "
   "every AI accelerator built since."),
 ]),

 ("2017", 17, [
  ("seal", "Acquisition &middot; $15.3bn &middot; March", "Intel / Mobileye",
   "Intel paying roughly forty times revenue for a company that makes cameras "
   "for cars, which made a lot of people cough.",
   "Intel had missed the phone completely and knew it. This was never really "
   "about cars. It was a very large cheque written in order to not miss the "
   "next one, and the next one turned out to be anything that computes while "
   "moving."),

  ("seal", "Carve-out &middot; ~$18bn &middot; September", "Toshiba Memory",
   "A struggling Japanese conglomerate selling a division to cover losses "
   "somewhere else.",
   "The division made the memory chips that store everything. Who owns memory "
   "turns out to be a national question rather than a commercial one, which is "
   "why a straightforward sale took a year and involved three governments."),
 ]),

 ("2018", 26, [
  ("column", "Blocked &middot; $117bn &middot; March", "Broadcom / Qualcomm",
   "The largest technology takeover ever attempted. Hostile, fully financed, "
   "and on its way.",
   "It was stopped by a presidential order, on the advice of a committee most "
   "people in technology could not have named. Not by a board. Not by a price. "
   "Chips stopped being a product that day and became territory, and the export "
   "controls, the subsidies and the fabs in Arizona were all already in that "
   "belly."),

  ("column", "Abandoned &middot; $44bn &middot; July", "Qualcomm / NXP",
   "A finished deal waiting on one last signature.",
   "The signature was Chinese and it never came. Qualcomm paid NXP $2bn to walk "
   "away from its own deal. The lesson a whole generation of dealmakers took "
   "from it: in semiconductors, the final approval is a foreign policy "
   "decision."),

  ("seal", "Acquisition &middot; $34bn &middot; October", "IBM / Red Hat",
   "An old company paying an enormous premium for a company that gives its "
   "software away free.",
   "Red Hat&rsquo;s bet was that no serious business would put everything in "
   "one cloud. IBM was buying the layer that sits across all of them. It is the "
   "same move Google makes seven years later with Wiz, for almost exactly the "
   "same money."),
 ]),

 ("2019", 19, [
  ("seal", "Acquisition &middot; $6.9bn &middot; March", "NVIDIA / Mellanox",
   "A networking bolt-on. Cables and switches, the equipment that lets one "
   "computer talk to another computer, which sits somewhere below the paper "
   "clip on any list of thrilling technologies.",
   "When you train an AI model you do not use one chip. You use ten thousand, "
   "and you need all ten thousand to behave like a single enormous brain. The "
   "thing that makes them behave like one is not the chips. It is the wiring "
   "between them. NVIDIA bought the wiring three years before anybody needed "
   "it, for less than it would later clear in a single quarter."),

  ("seal", "Acquisition &middot; $15.7bn &middot; June", "Salesforce / Tableau",
   "A software company buying a charts company.",
   "Nobody switches software because of the software. They switch because of "
   "where their data already sits, and moving it is a year of somebody&rsquo;s "
   "life. Salesforce was not buying charts. It was buying gravity."),
 ]),

 ("2020", 24, [
  ("stone", "", "Free money",
   "Central banks take rates to roughly zero and leave them there. When money "
   "costs nothing, anything with growth in it gets more expensive and patience "
   "gets cheaper. Every deal for the next two years has this one fact sitting "
   "underneath it."),

  ("seal", "Acquisition &middot; $35bn &middot; October", "AMD / Xilinx",
   "AMD, which had been close to bankrupt a few years earlier, buying a "
   "thirty-five billion dollar company.",
   "It paid entirely in its own shares, which had risen roughly tenfold. This "
   "is the most useful thing to understand about stock-funded deals: the number "
   "on the press release is a photograph of one day&rsquo;s share price, not a "
   "cheque anybody wrote."),
 ]),

 ("2021", 40, [
  ("stone", "", "Peak",
   "The busiest year in the history of dealmaking. Record volumes, a "
   "blank-cheque company for every idea somebody had in a bar, and an "
   "unshakeable sense that this was simply how things were now. It was the top. "
   "Nobody rings a bell at the top."),

  ("seal", "Acquisition &middot; $19.7bn &middot; April", "Microsoft / Nuance",
   "Microsoft buying the company behind the speech recognition your doctor "
   "mutters into.",
   "Hospital data is the hardest data in the world to get anywhere near, for "
   "extremely good reasons. Microsoft bought a company that was already inside "
   "the room, about eighteen months before anybody worked out what a language "
   "model would be worth with access to that room."),
 ]),

 ("2022", 20, [
  ("stone", "", "The window shuts",
   "Rates rise faster than at any point in forty years. The Nasdaq falls about "
   "a third. Companies that were going to go public stop going public and stay "
   "private, which is where a great deal of this story now lives and where very "
   "little of it is visible."),

  ("column", "Abandoned &middot; $40bn &middot; February", "NVIDIA / ARM",
   "The deal that would have handed one company the design nearly every other "
   "chip is built from.",
   "Regulators on three continents said no, and what actually killed it was "
   "that ARM&rsquo;s customers were NVIDIA&rsquo;s competitors. ARM listed "
   "separately instead and is now worth a great deal more than $40bn, which is "
   "the most expensive compliment ever paid to an antitrust lawyer."),

  ("seal", "Announced &middot; $61bn &middot; May", "Broadcom / VMware",
   "An enormous cheque written straight into a closing door. Completed in "
   "November 2023, after eighteen months of regulators.",
   "Broadcom&rsquo;s model is not growth. It buys infrastructure software that "
   "large companies cannot realistically switch away from, raises the price, "
   "and removes everything that is not the price. It is one of the most "
   "reliable money machines in technology and almost nobody describes it out "
   "loud."),
 ]),

 ("2023", 8, [
  ("stone", "", "A chatbot appears",
   "ChatGPT crosses from a demo into every boardroom on earth. It looked like a "
   "toy you could ask to write a poem. What was actually in it was a capital "
   "expenditure supercycle, and within two years the most contested resource in "
   "technology would be electricity."),

  ("stone", "", "The trough",
   "And yet the quietest year for technology dealmaking since the financial "
   "crisis. Bankers call this a dislocation. Everybody else calls it nothing "
   "happening."),

  ("seal", "Acquisition &middot; $28bn &middot; September", "Cisco / Splunk",
   "Cisco paying up for a company that reads log files, which is as "
   "unglamorous as it sounds.",
   "Every machine writes down what it just did. Splunk reads all of it. In a "
   "year when almost nobody could tell you what their own systems were actually "
   "doing, the company that reads the record quietly became strategic."),
 ]),

 ("2024", 14, [
  ("stone", "", "The money changes shape",
   "Spending stops going to engineers and starts going to concrete, "
   "transformers and industrial air conditioning. The hottest asset in "
   "technology becomes a shed with good access to a power line."),

  ("seal", "Announced &middot; ~$1.46bn &middot; March", "Keysight / Spirent",
   "Test equipment. Genuinely, the machines that check whether other machines "
   "work. Completed October 2025.",
   "You cannot build a network moving this much data without being able to "
   "prove that it moves. Picks and shovels, except this is the company that "
   "inspects the shovels, and in a buildout this large somebody has to."),
 ]),

 ("2025", 26, [
  ("seal", "Acquisition &middot; $32bn &middot; March", "Google / Wiz",
   "The largest purchase of a private technology company ever made.",
   "Wiz runs on Amazon&rsquo;s cloud and Microsoft&rsquo;s as well as "
   "Google&rsquo;s, and Google committed publicly to keeping it that way. "
   "Google is a durable third in cloud. It did not buy a feature for its own "
   "estate. It bought the security layer sitting above everybody&rsquo;s, "
   "including the two it keeps losing to."),

  ("seal", "Investment &middot; $300m at $5bn &middot; January", "DDN / Blackstone",
   "A private equity cheque into a storage company founded in 1998. Storage. "
   "The dullest available word in this entire industry.",
   "A GPU does not think slowly. It waits. The most expensive processor ever "
   "mass produced sits idle in the dark because the thing it needs to look at "
   "next has not arrived from storage yet. The bottleneck in artificial "
   "intelligence was never intelligence. It was fetching."),

  ("stone", "", "Where the money actually comes from",
   "Convertible notes at Datadog. Exchangeable notes at Seagate. A term loan at "
   "LendingTree. None of this makes a headline and all of it is how the "
   "buildout gets paid for. A convertible note is a loan that is allowed to "
   "change its mind and become shares instead. Companies like them because the "
   "interest is cheap. Lenders like them because if the stock runs they stop "
   "being a lender and start being an owner."),
 ]),

 ("2026", 36, [
  ("seal", "Acquisition &middot; $11.9bn", "IBM / Confluent",
   "A data plumbing company, bought by IBM, for nearly twelve billion dollars.",
   "An AI agent acting on your behalf cannot work from last night&rsquo;s data. "
   "It needs what is true right now. Confluent moves data while it is still "
   "happening, and that turns out to be the whole difference between a model "
   "that answers you and a model that does something."),

  ("stone", "", "Rust is back",
   "Hard drives were declared dead a decade ago. Flash was faster and had no "
   "moving parts and that was supposed to be the end of it. Then machines that "
   "read everything needed somewhere enormous and cheap to keep the things they "
   "might want later, and the spinning platter became strategic again. Seagate, "
   "left for dead, spent the year raising money on terms usually reserved for "
   "growth companies."),

  ("stone", "", "Here",
   "Which is roughly where you are standing. Over ten years the industry "
   "stopped buying software and started buying physics, and the question "
   "underneath every single thing on this spine has been the same one. What is "
   "in the horse."),
 ]),
]
