"""Trojan Horse of the Week: the current feature, linked from the top of the
homepage. To change the feature, replace this module's values (or point
build-site.py at a different module) and rebuild. Earlier weeks live in
weekly_*.py and keep their pages.

This week: Oura postpones its IPO. Structured in headed sections, each doing one
job, in the manner of a venture investor reading a filing line by line, and
kept in the homepage Troy anecdote's voice: a dated scene first, warm, a little
funny, an analogy where an abstraction would otherwise sit.

Sources, in order of weight: Oura's Form S-1 and S-1/A on EDGAR for every
company figure, Fortune (6 October 2026) for the experts and the seller split,
IFR for the lock-up, the valuation framing and the selling holders, CNBC and
Renaissance Capital for the postponement itself, and trade reporting for the
patent outcome. Experts are paraphrased and linked. The single direct quote is
the CEO's. The woman in Austin is labelled as invented.

No em dashes, no semicolons, no rhetorical questions, no sub-description under
the title.
"""

WEEK = "31 October 2026"
SLUG = "oura-ipo"
KICKER = "Trojan Horse of the Week"
TITLE = "Oura Sleeps On Its IPO"
HOOK = ("Orders reached four to five times the shares on offer, and 73% of those "
        "shares belonged to the people selling them.")
LOGO = {"file": "oura.svg", "w": 993, "h": 311, "name": "Oura", "height": 34}
GO = ("thorne-loyalty.html",
      "The previous Trojan horse: can P&amp;G keep Thorne&rsquo;s customers loyal? &rarr;")

S1 = "https://www.sec.gov/Archives/edgar/data/0002133022/000119312526381855/d119865ds1.htm"
S1A = "https://www.sec.gov/Archives/edgar/data/0002133022/000119312526396051/d119865ds1a.htm"
FORTUNE = "https://fortune.com/2026/10/06/why-did-oura-pull-its-ipo/"
IFR = ("https://www.ifre.com/equities/2493350/smart-ring-maker-oura-pulls-us2.2bn-"
       "ipo-over-valuation-and-lockup")
CNBC = ("https://www.cnbc.com/2026/09/29/smart-ring-maker-oura-postpones-ipo-due-to-"
        "market-uncertainty.html")
RENCAP = ("https://www.renaissancecapital.com/IPO-Center/News/121945/smart-ring-maker-"
          "oura-postpones-2.1-billion-ipo")
IPOSCOOP = "https://www.iposcoop.com/?p=39366"
LICENSE = "https://athletechnews.com/?p=140346"

SECTIONS = [

 ("Eight days on the road", [
  "Picture the morning of Tuesday 29 September 2026. For eight days a ring "
  f"company that began in Finland and now lives in San Francisco had been "
  f"walking investors through <a href=\"{CNBC}\">its Nasdaq debut</a>. Fifty "
  f"million shares at $40 to $44 each. <a href=\"{RENCAP}\">Seventeen "
  "banks</a> standing behind them. A ticker symbol, OURA, waiting at the "
  "exchange, and a pricing due within the week. Then, in place of a price, came "
  "a press release. The company would wait. I love this part of the story. Oura "
  "makes a ring whose whole job is to tell five million paying members how well "
  "they slept, and on the morning it counted, the company decided to sleep on "
  "it.",

  "The demand had looked excellent. Two investors had already said what they "
  f"intended to do, and <a href=\"{S1A}\">the amended filing</a> names them: "
  "Eli Lilly indicated an interest in up to $100 million of shares and funds "
  "affiliated with Dragoneer up to $300 million. Those are non-binding, and "
  "together they came to about a fifth of the $2.1 billion on offer at the "
  "midpoint. Reports put the whole book at four to five times the shares "
  f"available, with <a href=\"{FORTUNE}\">Fortune</a> hearing five from a "
  "source. On paper it was one of the hotter listings of the autumn.",
 ]),

 ("The reason on the press release", [
  "Oura said it was postponing despite strong demand because of uncertainty in "
  "the IPO market. Its chief executive, Tom Hale, said the company had &ldquo;the "
  "luxury of choosing our moment,&rdquo; and the company added that it is "
  "profitable and that its business had strengthened since the process began. "
  "The people who study IPOs were not persuaded.",

  f"<a href=\"{FORTUNE}\">Fortune</a> asked several of them. Jay Ritter, who "
  "runs the IPO initiative at the University of Florida, said issuers habitually "
  "blame market conditions and seldom admit they overestimated what they were "
  "worth. Kat Liu of IPOX, a firm that builds IPO indexes, said companies rarely "
  "volunteer weakness. Gil Luria of D.A. Davidson called the market explanation "
  "a stretch, and the article noted that the S&amp;P 500 was up more than 13% for "
  "the year and less than 1% below its record in early October. Other listings "
  "did slip in the same weeks. Holtec Nuclear postponed in early September, and "
  "Bamboo Insurance and Amaero shelved theirs at about the same time.",
 ]),

 ("A ring, a membership and a valuation", [
  "Oura began in Finland in 2013, and for years it made a ring for people who "
  "liked to measure their own sleep. Tom Hale has run it since 2022. The "
  "decision that changed its economics was to sell the ring once and charge a "
  f"monthly membership for the insights. <a href=\"{S1}\">The S-1</a> shows how "
  "well that has sold. Oura sold 3.1 million rings in the nine months to June "
  "2026, up from 1.8 million a year earlier, and paid members rose from 2.9 "
  "million at the end of fiscal 2025 to 5.0 million on 30 June.",

  "Suppose a woman in Austin, who exists only in this story, has worn one for "
  "two years. She takes it off to wash the dishes and puts it back on before she "
  "forgets. Every morning it grades her on an exam she does not remember "
  "sitting, and she has come to trust it the way people trust a friend who has "
  "seen them at their worst. Multiply her by five million and the bankers&rsquo; "
  "enthusiasm becomes easy to understand.",

  "The company also defended its position in court. The U.S. International "
  "Trade Commission found that Ultrahuman and RingConn infringed Oura&rsquo;s "
  "patents and barred Ultrahuman&rsquo;s rings from import and sale in the "
  f"United States. RingConn settled and <a href=\"{LICENSE}\">took a "
  "multi-year license that includes royalties to Oura</a>. Investors followed "
  "the progress. The last private round, the Series E, "
  f"valued Oura at $11 billion, and <a href=\"{IFR}\">IFR reported</a> that the "
  "top of the IPO range implied a fully diluted valuation of $15.6 billion.",
 ]),

 ("The case for a software multiple", [
  "The strongest part of the filing is the membership. Membership revenue was "
  "$240.5 million in the nine months to June, up 121% from $108.8 million, at "
  "an 89% gross margin. Historically more than 94% of ring activations convert "
  "into paid members, and weighted-average twelve-month retention was about 85% "
  "as of 30 June. Total revenue was $1.21 billion, up 74%. Net income was $60.8 "
  "million against $1.6 million a year earlier, and adjusted EBITDA was $106.7 "
  "million.",

  "Those numbers support the argument for valuing Oura like software. The "
  "customer arrives through a one-time hardware sale and then stays in a "
  "high-margin subscription, and software companies earn high multiples "
  "because each additional customer costs little to serve.",
 ]),

 ("Who was selling", [
  "An IPO can sell two kinds of shares. Primary shares are new, the company "
  "issues them, and the money goes to the company, which makes the offering a "
  "fundraise. Secondary shares already exist and belong to founders, employees "
  "and early investors, and the money goes to them, which makes it a cash-out. "
  "The restaurant version is the difference between printing new seats to fund "
  "a second location and the original investors selling the seats they already "
  "hold.",

  f"Oura&rsquo;s offering was 13.5 million primary shares and 36.5 million "
  f"secondary shares (<a href=\"{S1A}\">the amended filing</a>), so 73% of it "
  "was existing holders selling. At the $42 midpoint that is roughly $567 "
  "million of gross proceeds for the company and $1.53 billion for the sellers, "
  f"per <a href=\"{FORTUNE}\">Fortune</a>. <a href=\"{IFR}\">IFR reported</a> "
  "that three venture firms were behind the 36.5 million, that Forerunner "
  "Ventures planned to sell all 28.7 million of its shares, which comes to "
  "about $1.2 billion at the midpoint, and that Lifeline Ventures planned to "
  "sell the 7 million it had left.",

  "Selling in an IPO is ordinary. Venture funds have fixed lives and must "
  "return money to their own investors, and employees paid in stock for years "
  "want to turn it into something. The listing is where that happens. The "
  "ratio is what an outside buyer reads. Liu called the share of insider "
  "selling a flag for the market, a sign the offering was not meant to fund "
  "growth.",
 ]),

 ("Where the company&rsquo;s share was going", [
  "The company&rsquo;s own slice was smaller than it looked. Oura planned to "
  "use about $526.4 million of its estimated $532.6 million in net proceeds to "
  f"pay tax withholding on employee stock (<a href=\"{S1A}\">the amended "
  "filing</a>), which leaves about $6 million for everything else. Many "
  "employees are paid in restricted stock units, a large batch vests when a "
  "company lists, and the employees owe tax on it. Companies often hold back "
  "some of the shares and pay that tax in cash on the employees&rsquo; behalf, "
  "which the filing calls the RSU net settlement. About 99% of what the company "
  "would net was therefore headed to the tax authorities for its staff, so the "
  "offering raised almost no money to grow the business.",

  "The filing carries one more figure that needs reading. It shows net income "
  "of $60.8 million for the nine months and, in the same period, a net loss "
  "attributable to common stockholders of $924.3 million. The difference is a "
  "$985.0 million deemed dividend to preferred holders. The S-1 explains the "
  "treatment: when the company repurchases preferred shares for more than "
  "their carrying value, the excess is recorded as a deemed dividend. The loss "
  "is bookkeeping for payments to early holders, net income stays at $60.8 "
  "million, and the entry shows early holders being paid before the listing.",
 ]),

 ("The case against", [
  "About 80% of revenue still comes from selling rings. Hardware was 84% of "
  "revenue in the nine months to June 2025 and 80% a year later, so the mix is "
  "moving and has not arrived. Gross margin was 65% in fiscal 2024, 52% in "
  "fiscal 2025 and 55% in the nine months to June 2026, and net income was "
  "about 5% of revenue by my arithmetic.",

  f"At the top of the range the fully diluted valuation of $15.6 billion was "
  f"about eleven times the $1.43 billion of revenue for the twelve months to "
  f"June (<a href=\"{IPOSCOOP}\">IPOScoop</a> for the revenue), again by my "
  "arithmetic. IFR reported that the banks supported the price with 2028 "
  "projections, a mid-4x multiple of revenue against about 5x for a comparison "
  "group that included Apple, Garmin, Netflix and Spotify, assuming 45% annual "
  "revenue growth through 2028 against 15% for the group. The price rested on "
  "the next two years. A ring comes with a physical product behind every sale, "
  "and Oura was asking a public buyer for a software price while four fifths of "
  "its revenue still shipped in a box.",
 ]),

 ("Precedents and neighbors", [
  "Public investors have heard this pitch before, from a hardware company with "
  "a subscription story and a lifestyle brand. GoPro priced at $24 in 2014 and "
  "Peloton at $29 in 2019, and Fortune reported them down more than 94% and 82% "
  "from those prices. Luria said investors have long memories, and Ritter "
  "pointed to single-product companies whose growth stalled after listing. "
  "People loved both products. The hardware economics showed once growth "
  "slowed.",

  "The size of the market is the other question. The amended filing says Oura "
  "represented about 2% of annual global wearable shipments in the twelve "
  "months to June, citing IDC&rsquo;s estimate of 212 million wearables. Luria "
  "noted that Apple would only have to decide to make a ring, and Apple sells "
  "none today. Samsung&rsquo;s Galaxy Ring carries no required subscription. "
  "Oura&rsquo;s answers are the 85% retention, the patent record and its lead "
  "in rings, and a buyer weighing those against a hardware history can "
  "reasonably ask for a discount until the retention has been tested by time.",
 ]),

 ("What oversubscribed means", [
  "Four to five times covered sounds like proof of demand, and it proves less "
  "than it seems. An order book is a list of prices as much as a list of "
  "shares. Institutions often submit orders with limits, so a buyer can be "
  "large at $38, smaller at $42 and absent at $44. A restaurant can have a "
  "waiting list four times its seating and still seat nobody at $44 a plate.",

  f"Fortune relayed Bloomberg&rsquo;s report that some prospective buyers "
  f"stayed out over concern about the valuation. <a href=\"{IFR}\">IFR</a> added "
  "that investors objected to a loose lock-up, which would have let early "
  "backers sell in waves soon after listing, with ten rolling releases from 35 "
  "days and a full release after 180 days.",
 ]),

 ("Why neither side moved", [
  "The structure explains the standoff. In an ordinary offering a lower price "
  "means the company raises less, which hurts and still funds the company. In "
  "this one most of the shares belonged to the sellers, so a lower price mostly "
  "meant early holders receiving less for the same stock, and the company&rsquo;s "
  "own slice was largely going to employee taxes. Oura is profitable and did "
  "not need the money to operate. The buyers wanted a discount, the sellers "
  "were unwilling to give one, and the company could afford to wait, which "
  "gives the luxury of choosing the moment a precise meaning. This is an "
  "inference from the structure, since the company has stated one reason, which "
  "is the market.",
 ]),

 ("What to read first", [
  "Some outlets have called the move a withdrawal, and the company and most of "
  "the financial press that covered it call it a postponement. It has given no "
  "new date, and the filing remains on the SEC&rsquo;s site.",

  "For a founder, an IPO is a fundraise and a payday for early backers at the "
  "same moment, and how the two are split tells every buyer what to think. For "
  "an investor, three lines come before the pitch: how many shares are new, how "
  "many belong to insiders, and where the company&rsquo;s own money goes. The "
  "next time Oura opens its gate, those three numbers are where to look first.",
 ]),
]

NOTE = ("Company figures come from Oura&rsquo;s Form S-1 and the amended S-1/A. "
        "The experts&rsquo; views are from Fortune&rsquo;s 6 October 2026 report "
        "and are paraphrased, and the lock-up, the banks&rsquo; valuation framing "
        "and the selling holders are from IFR. Outlets differ on the book&rsquo;s "
        "size, four to five times, and the figure is given as a range. The "
        "filing&rsquo;s note tying the $985.0 million deemed dividend to a "
        "specific repurchase was outside the part I could read, so the story "
        "describes the accounting treatment and not the transaction. "
        "Forerunner&rsquo;s $1.2 billion is IFR&rsquo;s 28.7 million shares at "
        "the $42 midpoint, and the 5% net margin and eleven times revenue are my "
        "arithmetic from the filing and the reported valuation. The woman in "
        "Austin is invented.")
