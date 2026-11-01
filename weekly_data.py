"""Trojan Horse of the Week: the current feature, linked from the top of the
homepage. To change the feature, replace this module's values (or point
build-site.py at a different module) and rebuild. Earlier weeks live in
weekly_*.py and keep their pages.

This week: Oura postpones its IPO. Written in the register of the homepage Troy
anecdote: a scene first, warm and a little funny, the analogy doing the
explaining, the hard facts underneath it. There is no standfirst under the
title. The single direct quote is the CEO's.

Every figure comes from the company's Form S-1 or from reporting of the
29 September 2026 postponement that could be read: CNBC, Renaissance Capital and
IPOScoop. The woman in Austin is labelled as invented. Outlets disagree about
the valuation the offering implied and about the loss figure, so the story uses
neither.

No em dashes, no semicolons.
"""

WEEK = "31 October 2026"
SLUG = "oura-ipo"
KICKER = "Trojan Horse of the Week"
TITLE = "Oura Sleeps On Its IPO"
GO = ("thorne-loyalty.html",
      "The previous Trojan horse: can P&amp;G keep Thorne&rsquo;s customers loyal? &rarr;")

# a story, so the one section has no heading
SECTIONS = [
 ("", [
  "Picture the morning of Tuesday 29 September 2026. For eight days a ring "
  "company that began in Finland and now lives in San Francisco had been "
  "walking investors through <a href=\"https://www.cnbc.com/2026/09/29/smart-"
  "ring-maker-oura-postpones-ipo-due-to-market-uncertainty.html\">its Nasdaq "
  "debut</a>. Fifty million shares at $40 to $44 each. <a href=\"https://www."
  "renaissancecapital.com/IPO-Center/News/121945/smart-ring-maker-oura-"
  "postpones-2.1-billion-ipo\">Seventeen banks</a> standing behind them. A "
  "ticker symbol, OURA, waiting at the exchange, and a pricing due within the "
  "week. Then, in place of a price, came a press release. The company would "
  "wait. Demand was strong, it said, and the business had grown stronger since "
  "the process began, and the market was uncertain, and its chief executive, "
  "Tom Hale, observed that the company had &ldquo;the luxury of choosing our "
  "moment.&rdquo; I love this part of the story. Oura makes a ring whose whole "
  "job is to tell five million paying members how well they slept, and on the "
  "morning it counted, the company decided to sleep on it.",

  "Nobody had to be talked into liking the ring. Suppose a woman in Austin, who "
  "exists only in this story, has worn one for two years. She takes it off to "
  "wash the dishes and puts it back on before she forgets. Every morning it "
  "grades her on an exam she does not remember sitting, and she has come to "
  "trust it the way people trust a friend who has seen them at their worst. "
  "Multiply her by five million. The filing says Oura served 5.0 million paid "
  "members on 30 June 2026, up from 2.9 million at the end of fiscal 2025. "
  "Revenue for the nine months to June was $1.21 billion against $698 million "
  "a year earlier, and net income was $60.8 million against $1.6 million. The "
  "company told the market it expects revenue to grow 90 percent this fiscal "
  "year. A company people love, growing fast and making money, walks up to the "
  "gate of the public market and knocks, and of course the city comes out to "
  "look.",

  "Every city has a priest who has read the fine print, and here the fine print "
  "is <a href=\"https://www.sec.gov/Archives/edgar/data/0002133022/"
  "000119312526381855/d119865ds1.htm\">the S-1</a>, the registration statement "
  "the company filed publicly in early September. It spends page after page "
  "telling the reader where the wood is soft. A class action was filed against "
  "the company in August 2026 alleging that it falsely advertises the accuracy "
  "of its sleep tracking. The company has no manufacturing of its own and relies "
  "on a limited number of contract manufacturers, some of them sole suppliers "
  "of certain parts. Hardware made about 83 percent of revenue in fiscal 2025 "
  "and about 80 percent in the nine months to June, which sits beside the "
  "company&rsquo;s description of itself as a health intelligence platform. "
  "Members may cancel at any time without penalty. Its AI uses select models "
  "from OpenAI, Anthropic and Google, under non-exclusive agreements. The law "
  "requires a company to disclose all of this before it asks for money, and it "
  "is to Oura&rsquo;s credit that every item can be found by anyone who looks.",

  "What delights me about an IPO is how much of it is a story told well. The "
  "Greeks built Troy a gift in the shape of what Troy wanted most. A listing "
  "offers the public the shape of what the public wants most as well, which is "
  "a share of a company it already loves, and this one has an unusual "
  "advantage, because the product is on your finger and you can feel it "
  "working. A person who loves a ring and a person who values a company are "
  "doing two different jobs, and the S-1 is the document for the second one.",

  "Then there is the question of who was selling. Of the 50 million shares on "
  "offer, Oura was selling 13.5 million and its existing stockholders were "
  "selling the other 36.5 million, which is 73 percent of the offering (<a "
  "href=\"https://www.iposcoop.com/?p=39366\">IPOScoop</a> has the split, and "
  "Renaissance Capital gives the same share). At the $42 midpoint that comes to "
  "roughly $567 million for the company and $1.5 billion for the holders, "
  "before fees, and the filing states that the company receives no proceeds "
  "from the selling stockholders&rsquo; shares. Existing holders selling into "
  "an IPO is ordinary, and it changes one thing, which is whose pocket the "
  "money lands in. Oura said it would use its own proceeds for general "
  "corporate purposes. None of this implies that the price was wrong, and all "
  "of it is a reason for a buyer to read before buying.",

  "An IPO is a sale, which is why it belongs in a journal about deals. A "
  "company decides the moment is right to hand pieces of itself to strangers, "
  "and the strangers decide how much of the story to believe, and each side "
  "studies the other as closely as the Greeks and the Trojans did. The reason "
  "Oura gave for stopping concerns the market and says nothing against the "
  "business, which it described as stronger than when the process began. The "
  "lawsuit, the contract manufacturers, the revenue mix and the members who "
  "can leave on any day were in the filing before the market turned, and they "
  "are all still in it.",

  "Some outlets have called the move a withdrawal, and the company and most of "
  "the financial press that covered it call it a postponement. It has given no "
  "new date, and the filing remains on the SEC&rsquo;s site for anyone to "
  "read. A reader who loves the ring has been handed some time, and the useful "
  "way to spend it is to read the lawsuit, the revenue mix and the selling "
  "stockholders&rsquo; share now, and to see whether the account of those "
  "three things changes when the company next opens its gate.",
 ]),
]

NOTE = ("Figures come from Oura&rsquo;s Form S-1 (fiscal 2025 and the nine months "
        "to 30 June 2026), from CNBC and Renaissance Capital on the 29 September "
        "2026 postponement, and from IPOScoop on the offering terms. Outlets "
        "differ on the valuation the offering implied and on the size of the "
        "loss attributable to common stockholders, which the filing attributes "
        "to a deemed dividend to preferred holders, so the story uses neither. "
        "The company&rsquo;s forecast of 90 percent revenue growth is its own. "
        "The woman in Austin is invented, and the split between company and "
        "selling shares is described as a fact about the offering and not as a "
        "judgment on the price.")
