"""Trojan Horse of the Week: Uber buys ezCater.

Tightened 3 November 2026 to one point argued with conviction: ezCater makes
Uber the default vendor inside corporate accounts, and that relationship is
the asset a robotaxi cannot take. Under 1,200 words with the note.

Rewritten 3 November 2026 around the owner's brief: ezCater first and the B2B
synergy with Uber's network, with Delivery Hero and hotel booking as the other
rooms of the same house, and the robotaxi threat as the reason for building it.

Every company figure is from a source that was read: Uber's own business page
(300,000 businesses), the ezCater announcement as reported by PYMNTS, QSR Web
and AWP, the hotel launch as reported from Uber's Go-Get event and by The
Points Guy, Uber's Delivery Hero announcement, Q2 release, 10-Q and 10-K. The
synergy argument is the author's, because Uber gave no synergy figure. The
office manager in Boston is invented and labelled. One direct quote, the CEO's.

No em dashes, no semicolons, no rhetorical questions, no sub-description under
the title.
"""

WEEK = "3 November 2026"
SLUG = "uber-rival-dinner"
KICKER = "Trojan Horse of the Week"
TITLE = "Uber Gets Into the Expense Report"
HOOK = ("Uber is paying $2.3 billion for ezCater, whose orders average more than "
        "$400, to put the office lunch on the account that already pays for the ride.")
LOGO = {"file": "uber.svg", "w": 926.906, "h": 321.777, "name": "Uber", "height": 34}
GO = ("oura-ipo.html",
      "The previous Trojan horse: Oura sleeps on its IPO &rarr;")

EZ = ("https://www.pymnts.com/news/acquiring/2026/uber-eats-enters-catering-space-"
      "with-2-billion-dollar-ezcater-deal/")
EZ_QSR = "https://www.qsrweb.com/news/uber-to-purchase-ezcater-in-23b-deal/"
EZ_AWP = ("https://www.vermoegenszentrum.ch/en/stock-exchange-and-markets/news/"
          "uber-acquires-us-corporate-catering-firm-ezcater-usd23-billion")
EZ_BNN = ("https://www.bnnbloomberg.ca/business/company-news/2026/10/06/uber-to-buy-"
          "us-catering-platform-ezcater-for-us23b/")
EZ_GLOBE = "https://www.bostonglobe.com/2026/10/06/business/ezcater-acquired-uber-eats/"
UFB = "https://www.uber.com/us/en/business/"
HOTEL = ("https://www.hotel-online.com/index.php/news/uber-makes-massive-move-into-"
         "travel-with-hotels-vacation-rentals-and-new-app-features")
TPG = "https://thepointsguy.com/travel/uber-expedia/"
DH = ("https://www.sec.gov/Archives/edgar/data/0001543151/000155278126000382/"
      "e26302_ex99-1.htm")
Q2 = ("https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/"
      "uberq226earningspressrelea.htm")
CNBC = "https://www.cnbc.com/2026/08/05/uber-stock-q2-2026-earnings.html"
K10 = "https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm"
WAYMO_UBER = "https://waymo.com/waymo-on-uber"

SECTIONS = [

 ("", [
  "Almost everyone who travels for work has expensed an Uber. Fewer have "
  "thought to order a $400 tray of sandwiches through it. On 6 October 2026 "
  f"Uber agreed to pay <a href=\"{EZ}\">$2.3 billion in cash</a> for ezCater, "
  "the American workplace-catering platform, to close that gap. Its chief "
  "executive, Dara Khosrowshahi, put the logic plainly: &ldquo;Catering "
  "is a big business.&rdquo;",

  "My argument is that this is the most important deal Uber has made this "
  "year, bigger in meaning than its far larger offer for Delivery Hero. ezCater "
  "turns Uber into the default vendor inside the corporate expense account, and "
  "a relationship with a finance department is the one asset a robotaxi can "
  "never take away from it.",
 ]),

 ("The horse is the expense account", [
  f"<a href=\"{UFB}\">Uber says</a> more than 300,000 businesses use Uber for "
  "Business, including more than half of the Fortune 500. It sells them one "
  "dashboard to manage employee rides and meals, set policy and track spend, "
  "with expenses reconciled automatically. A finance team welcomes that for "
  "ordinary reasons: fewer receipts, fewer arguments, one bill.",

  "That is the Trojan horse. What rides inside is a marketplace that becomes "
  "the company&rsquo;s default for every errand involving a car, a meal or a "
  "room. Every new service arrives with the account approved, the card on file "
  "and the policy written. A catering company selling on its own has to win "
  "each customer. Inside Uber, catering only has to appear in an app the "
  "company already pays.",
 ]),

 ("What $2.3 billion buys", [
  "ezCater handles the meetings, training days and recurring office lunches "
  "companies order in advance. It booked more than $2.5 billion of gross "
  "bookings over the trailing twelve months, growing in the high teens, through "
  f"more than 140,000 restaurants, with an average order above $400 (<a "
  f"href=\"{EZ_QSR}\">QSR Web</a>). Uber says it is profitable on a non-GAAP "
  f"operating basis and will lift Uber&rsquo;s margins (<a href=\"{EZ_AWP}\">"
  "AWP</a>).",

  "By my arithmetic Uber is paying a little under one year of ezCater&rsquo;s "
  "gross bookings. For a food-delivery business that would be rich. For a "
  "business whose customers are companies with budgets, it is a bargain.",
 ]),

 ("Why the business lunch is worth more than dinner", [
  "Nobody has published a synergy figure, so this is my case, and it rests "
  "on four things Uber already owns.",

  "The buyer. The person who sets the meal policy is already logged in to Uber "
  "for Business. ezCater adds the order too big for a meal voucher, and gains a "
  "sales force of 300,000 existing accounts that never has to make a cold call.",

  "The ticket. A $400 order placed days ahead is worth many takeout orders to a "
  "restaurant, and it arrives with notice. The announcement promised couriers "
  f"new earning opportunities (<a href=\"{EZ}\">PYMNTS</a>). Scheduled demand "
  "is the cheapest kind for a delivery network to serve.",

  "The bill. ezCater already invoices companies and Uber already reconciles "
  "their expenses. Together they put the ride to the client, the lunch for the "
  "meeting and the dinner afterward on one statement, and one statement is very "
  "hard to replace.",

  f"The rival. <a href=\"{EZ_BNN}\">BNN Bloomberg</a> framed the deal as Uber "
  "narrowing its gap with DoorDash in American delivery. Corporate catering is "
  "the corner of that market where the customer is a company, and companies "
  "change vendors far less often than people change apps.",
 ]),

 ("Every move this year points the same way", [
  f"In July Uber offered <a href=\"{DH}\">&euro;41.50 a share for Delivery "
  "Hero</a>, valuing it at $14.8 billion, and says customers who use both rides "
  "and delivery generate about three times the gross bookings of those who use "
  "one. In April it began selling hotel rooms through a partnership with "
  f"Expedia, more than 700,000 properties inside the app (<a href=\"{HOTEL}\">"
  "Hotel Online</a>). Hotels are a consumer feature today. My prediction is that "
  "they reach business accounts next, and then a whole business trip lives in "
  "one app: the airport ride, the room, the client lunch and the dinner.",
 ]),

 ("Why a robotaxi cannot touch this", [
  "Delivery is already nearly as big as rides. In the second quarter Uber "
  "booked $27.5 billion in delivery against $29.0 billion in mobility, and "
  f"delivery grew faster, 26% to 22% (<a href=\"{Q2}\">the earnings "
  f"release</a>). Rides carry the long-term risk. Uber&rsquo;s <a "
  f"href=\"{K10}\">annual report</a> names Waymo, Zoox and Tesla among "
  "companies that compete with it or may in future, even as autonomous trips "
  f"remain under 0.5% of its weekly volume (<a href=\"{CNBC}\">CNBC</a>).",

  "A robotaxi can carry a tray of sandwiches. It cannot sign a vendor agreement "
  "with a finance department, and a vendor agreement is most of what ezCater "
  "is. Uber is moving its weight onto contracts and accounts, the part of the "
  "business that does not depend on who is driving.",
 ]),

 ("What would slow it", [
  "Three integrations at once is a heavy load, office catering depends on "
  "people coming in to the office, and DoorDash wants the same lunch. The bundle "
  "also has to win line by line before it wins as a bundle. The first test is "
  "simple: whether ezCater closes on schedule and appears inside Uber for "
  "Business accounts, which is where this case either shows up or does not.",
 ]),
]

NOTE = ("ezCater&rsquo;s figures are from the 6 October 2026 announcement as "
        "reported by PYMNTS, QSR Web and AWP, because I could not read "
        "Uber&rsquo;s release directly. No outlet gave a synergy figure, so the "
        "synergy case is mine. Delivery Hero terms, second-quarter figures and "
        "the competitor list are from Uber&rsquo;s filings. The price compared "
        "with gross bookings is my arithmetic.")
