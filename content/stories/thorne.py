"""Trojan Horse of the Week, 26 October 2026: Thorne.

Its place on the homepage is set by STORIES in content/home.py.

Register for this slot, set by Francis on 2026-10-30: philosophical and dry,
professional, with a labelled analogy doing the work an abstraction would
otherwise do. It never disparages the acquirer. There is no standfirst or
sub-description under the title, on the homepage or on the page itself.

This week's piece rests on sources that could be read: Thorne's announcement,
Jones Day's deal record, trade reporting on P&G's earlier supplement purchase
and the FDA's recall notice. Forum posts could not be read directly, so the page
says what the discussion is on the strength of published reporting of it and
does not claim a count.

Tightened 3 November 2026 to one point argued with conviction: the price
rides on the small group of practitioners and serious users who can verify the
product, and P&G keeps every customer if it keeps them. Under 1,200 words with
the note.

No em dashes, no semicolons.
"""

WEEK = "Week of 26 October 2026"
SLUG = "thorne-loyalty"
KICKER = "Trojan Horse of the Week"
TITLE = "Thorne&rsquo;s Practitioners Hold P&amp;G&rsquo;s $3.8 Billion"
HOOK = ("P&amp;G agreed to pay $3.8 billion for a supplement brand, and the "
        "customers who justify that price never signed anything.")
LOGO = {"file": "thorne.svg", "w": 146, "h": 22, "name": "Thorne", "height": 20}
GO = ("trojan-horses.html", "The prices and dates behind this deal &rarr;")

MD = ("https://www.marketingdive.com/news/how-thornes-brand-platform-led-to-a-38b-"
      "pg-deal-and-whats-next/831494/")
FLOW = ("https://www.theflowspace.com/physical-health/prevention-longevity/"
        "procter-gamble-buys-thorne-supplements-3039451/")
NO = ("https://nutritionaloutlook.com/view/pgs-new-chapter-acquisition-year-later-"
      "what-difference-can-year-make")
NUTRA26 = ("https://www.nutraingredients.com/Article/2026/08/04/pg-to-acquire-thorne-"
           "in-premium-wellness-play/")
NUTRA18 = ("https://www.nutraingredients.com/Article/2018/07/12/New-Chapter-founders-"
           "leave-brand-saying-Procter-Gamble-s-profit-pressure-threatens-to-"
           "undermine-mission")
BRUSH = ("https://www.newhope.com/industry-news/industry-experts-analyze-proctor-"
         "gamble-acquisition-thorne")
NSF = "https://www.thorne.com/nsf-certified-for-sport"
JONES = ("https://www.jonesday.com/en/practices/experience/2026/08/the-procter-amp-"
         "gamble-company-acquires-thorne-from-l-catterton-for-38-billion")
FDA = ("https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts/pg-issues-"
       "voluntary-recall-aerosol-dry-conditioner-spray-products-and-aerosol-dry-"
       "shampoo-spray")

SECTIONS = [

 ("", [
  "Stand in a supplement aisle and every bottle makes the same promise. Most "
  "shoppers pick the one someone they trust told them to buy. For Thorne, that "
  "someone is usually a doctor, a dietitian, a coach or an athlete.",

  "P&amp;G agreed on 4 August 2026 to pay $3.8 billion for Thorne, about five "
  "and a half times the roughly $680 million L Catterton paid in 2023, for a "
  f"company that <a href=\"{MD}\">Marketing Dive</a> reports passed $500 "
  "million in annual revenue (the prices and dates are in <a "
  "href=\"trojan-horses.html\">the earlier piece on this deal</a>). My "
  "argument is that the whole price rides on a small group of people who can "
  "tell whether the product has changed, and that P&amp;G keeps every Thorne "
  "customer if it keeps them.",
 ]),

 ("The loyalty nobody signed", [
  "Buying a restaurant buys the lease, the ovens and the chairs. It does not "
  "buy the regulars, who stay free to walk out. Loyalty is the Trojan horse in "
  "this deal. It is the reason the price is what it is, so it is the most "
  "welcome part of the purchase, and it is the one part the buyer cannot take "
  "delivery of.",

  "Picture a friend famous for his boxed macaroni and cheese who buys a "
  "Michelin-starred restaurant. You will go, and before you sit down you will "
  "check the menu for the blue box. That is no insult to him. It is what "
  "people do when a place they love changes hands. P&amp;G is the friend, and "
  "Thorne&rsquo;s customers are already reading the menu.",
 ]),

 ("A few people decide for everyone", [
  "Thorne&rsquo;s own research, as Marketing Dive reports it, found consumers "
  "overwhelmed and confused by the supplement market, and found that its "
  "messages about scientific rigor mattered less to them than the company had "
  "assumed. Most buyers steer by a few visible cues: the price, the label, how "
  "the capsule agrees with them. A change nobody can see would pass them by.",

  "The people who would notice are the minority who can verify: "
  "practitioners, athletes and heavy users. Everyone else borrows their "
  "judgment, the way a table borrows the one friend who can read the wine list. "
  "That makes them the real asset. If they keep recommending Thorne, the mass "
  "of customers never questions the bottle. If they stop, the doubt spreads "
  "through everyone who trusted them. The sources do not split revenue between "
  "the two groups, so this is my reading of how the brand works.",
 ]),

 ("The fear, and the record", [
  f"A <a href=\"{FLOW}\">Flow Space roundup</a> of online reaction found "
  "customers split, some hoping for lower prices and wider availability, "
  "others fearing reformulation. It is the same worry recorded when P&amp;G "
  f"bought New Chapter in 2012 (<a href=\"{NO}\">Nutritional Outlook</a>). "
  "Thorne&rsquo;s chief executive, Colin Watts, has said the company will "
  "expand with P&amp;G while keeping to its values and standards "
  f"(<a href=\"{NUTRA26}\">NutraIngredients</a>).",

  "P&amp;G&rsquo;s record is better than the fear. After a year with New "
  "Chapter it had added staff for quality control and innovation, left the "
  "price alone and kept the brand out of mass retail despite requests, and the "
  f"founder said it was keeping its promise. <a href=\"{BRUSH}\">Marc "
  "Brush</a>, a former editor of Nutrition Business Journal, says P&amp;G has "
  "done a better job than most buyers of protecting brand equity in "
  "supplements. The warning comes from the same history. New Chapter&rsquo;s "
  "founders left in 2018 citing &ldquo;financial pressures to accelerate "
  f"profits&rdquo; (<a href=\"{NUTRA18}\">NutraIngredients</a>), and Brush "
  "says a price this high requires fast growth. Pressure to grow is exactly "
  "what tempts a quiet cost cut.",
 ]),

 ("How P&amp;G wins this", [
  "P&amp;G wins by treating the practitioners as the customer. Keep the "
  "formulas, keep the testing visible, and give the professionals who "
  "recommend Thorne a reason to keep doing it. The one recent stumble critics "
  f"cite, the 2021 <a href=\"{FDA}\">benzene recall</a> of aerosol dry "
  "shampoos traced to a propellant, is a reminder that a testing brand lives or "
  "dies on its inputs.",

  "Three things will show whether it is working once the deal closes, which "
  f"<a href=\"{JONES}\">Jones Day</a> expects in the fourth quarter of 2026. "
  "The first is whether Thorne keeps its NSF Certified for Sport mark, which "
  f"<a href=\"{NSF}\">Thorne says</a> covers more than 20 of its products. "
  "The second is whether prices or pack sizes change on its best sellers. The "
  "third is whether practitioners keep recommending it. My bet is that "
  "P&amp;G, having paid this much for trust, guards it.",
 ]),
]

NOTE = ("Prices and dates come from Thorne&rsquo;s announcement and the deal "
        "record published by P&amp;G&rsquo;s counsel. The consumer reaction "
        "rests on a published roundup I could read only as a search summary, "
        "and I could not read Reddit or other forums directly, so this is not a "
        "count of posts. The argument about who decides the outcome is mine.")
