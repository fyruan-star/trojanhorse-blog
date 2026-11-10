"""The homepage: its tagline, the Troy essay, the order of the stories, and the
podcast list. Edit the words here, keep the HTML tags as they are, and the site
rebuilds itself after you commit.
"""

# The line under "Mergers & Acquisitions" on the cover.
TAGLINE = "Hidden Risks Behind Promising Deals"

# Every Trojan Horse story. Each name is a file in content/stories/ (without
# .py). To add a story, add its file there and its name here. The homepage
# features the newest by date and the Articles page lists them all by date.
STORIES = ["oura", "thorne", "uber", "health", "attention", "hourglass", "marvell"]

# The smaller list under the stories on the Articles page: (link, title, one line).
MORE_FROM_JOURNAL = [
    ("palo-alto.html", "Deals From Palo Alto",
     "Technology transactions from the BofA Securities Palo Alto software team, told as stories."),
    ("the-buyers-bank.html", "The Buyer&rsquo;s Bank",
     "BofA Securities&rsquo; technology record across 2025 and 2026, built on acquirers."),
    ("how-a-company-gets-sold.html", "How a Company Gets Sold",
     "How an investment bank gets hired, how a sale then runs stage by stage, and why the managing director matters more than the logo."),
]

# The essay under the cover. It is HTML, so keep the <p> tags and write
# &rsquo; for an apostrophe and &amp; for an ampersand.
ESSAY = """
<!-- ============================================================== TALE === -->
<section class="essay" id="opening">
  <div class="shell">

    <div class="tale">
      <p class="tale__open"><span class="tale__cap">P</span>icture the morning the Trojans woke up to an empty beach. Ten years of tents and smoke and shouting had vanished overnight. The black ships were gone, and where the Greek camp had stood there was trampled sand and one enormous horse of fresh-cut pine. I love this part of the story. The whole city poured out through the gates to look at it.</p>
    </div>

    <div class="tale">
      <p>Children ran up and slapped the wood. Somebody&rsquo;s grandmother, who had spent a decade sleeping in her clothes, stood in the sun and cried because the war looked finished. A priest named Laocoön had his doubts. He said he feared the Greeks even when they came bearing gifts, and he hurled a spear into the horse&rsquo;s side. It stuck there, quivering, and from deep inside the wood came a low hollow groan. Then a Greek named Sinon, who had let himself be captured on purpose, wept and swore the horse was an offering to Athena that would protect the city if it stood inside. The Trojans believed him. The horse was too big for the gate, so they tore down a stretch of their own wall to bring it in, and that night the soldiers climbed out of its belly and opened the city from within.</p>

      <p>What delights me is how well that plan understood its audience. The Greeks had given up on the walls and started studying the people behind them. Ten years of siege taught them what Troy wanted most, which was for the war to be over, and they built that wish out of timber and left it where it would be found. The Trojans felt rewarded, and a person who feels rewarded stops inspecting the gift.</p>

      <p>Mergers and acquisitions run on the same instincts. At the end of the day a company acquires something in order to win, whether that is a customer base, a technology or a position its rival cannot reach, and the people across the table are studying what you want just as closely. So every deal is a horse standing at somebody&rsquo;s gate, and the useful thing to do is walk up to it and ask what it is carrying. A bank welcomes a private credit partner because the partner brings capital to its clients, and the partner gets to know those clients. A bank hands its junior analysts an AI assistant that finishes in minutes the hands-on work they used to do late at night, and that work is where they learned to judge a business. A chipmaker prepays a supplier two billion dollars to guarantee its wafers, the supplier runs into trouble, and the chipmaker ends up holding a large share of the supplier&rsquo;s stock. Each of those was welcomed for a good reason by sensible people.</p>

      <p>Any curious person can follow these stories. All it takes is the willingness to walk up to a very large gift and find out who built it. I will tell the deals one at a time, with the strategy as it unfolded and the sources beside every claim. Welcome to The Trojan Horse.</p>
      <p class="tale__sign">Francis Ruan</p>
    </div>

  </div>
</section>
"""

# The podcast page. Each entry is (title, description, status).
EPISODES = [
 ("Why Models Fail",
  "A discounted cash flow depends on forecast growth and a discount rate, and both are assumptions. This episode examines where valuation models break when applied to a real business, and what a forecast claims when it assumes that growth costs nothing.",
  "Recording October"),
 ("Sleep As Capital",
  "Junior bankers regularly work through the night. This episode examines what research on sleep deprivation shows about judgment, and whether a team that relies on long hours is gaining output or borrowing against later performance.",
  "In production"),
 ("The Adjusted Truth",
  "Adjusted EBITDA excludes items that management classifies as unusual. This episode examines who sets that definition, how it varies between companies and how it changes the multiple a buyer pays.",
  "In production"),
 ("Managing The Number",
  "Companies shape reported earnings through legal choices about timing and classification. This episode examines how those choices are used to meet consensus estimates and what they imply about the quarters that are not reported.",
  "In production"),
 ("Who Picks Comparables",
  "A valuation based on comparable companies depends on which companies are chosen. This episode examines how different peer sets change the answer, and why the selection is rarely shown.",
  "In production"),
 ("Writers Make Bankers",
  "Much of an analyst's work is persuasive writing about a business. This episode examines what separates strong writing from weak writing in banking and how analysts learn it.",
  "Recording October"),
 ("The Confidence Trap",
  "Two valuation methods that agree can seem to confirm each other. This episode examines how one assumption can enter both, which makes the agreement weaker evidence than it appears.",
  "In production"),
 ("Disconnected",
  "An experiment in building a complex model with the internet switched off, to test how much a person can recall without searching.",
  "In production"),
]
