"""Trojan Horse of the Week: Uber buys ezCater.

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

 ("A lunch for twenty", [
  "Picture the morning of Tuesday 6 October 2026, a little before eleven. An "
  "office manager in Boston, who exists only in this story, is feeding a "
  "twenty-person meeting. She opens ezCater, finds a restaurant that can manage "
  "a tray of sandwiches and the vegetarian option nobody touches, and the order "
  "lands a little above four hundred dollars, which is about where ezCater says "
  f"its average order sits (<a href=\"{EZ_QSR}\">QSR Web</a>). That same morning "
  f"Uber said it would buy ezCater, a Boston company, for <a href=\"{EZ}\">$2.3 "
  "billion in cash</a>. Its chief executive, Dara Khosrowshahi, put it "
  "plainly: &ldquo;Catering is a big business.&rdquo; I love the "
  "timing. The company that taught a generation to expense a ride had decided "
  "the sandwiches belong on the same receipt.",
 ]),

 ("The horse is the expense account", [
  "Every Trojan horse has the same parts. Something is welcomed by people with "
  "good reason to like it, it looks like a gift, and something else rides "
  f"inside. Here the horse is the corporate account. <a href=\"{UFB}\">Uber says</a> "
  "more than 300,000 businesses use Uber for Business, including more than half "
  "of the Fortune 500, and it sells them a tidy idea: manage employee rides and "
  "meals, set policy controls and track spend from one dashboard, with expenses "
  "reconciled automatically.",

  "A finance team welcomes that for ordinary reasons. It means fewer receipts, "
  "fewer arguments and one bill. What rides inside is a marketplace that would "
  "like to become the company&rsquo;s default for every errand involving a car, "
  "a meal or a room. Each new service arrives with the account already "
  "approved, the card already on file and the policy already written. That is "
  "the part rivals should lose sleep over. A catering platform selling on its "
  "own has to win each company. Inside Uber, catering only has to appear in an "
  "app the company already pays.",
 ]),

 ("What $2.3 billion buys", [
  "ezCater sells workplace catering, the meetings, training days and "
  "recurring office lunches that companies order in advance. It booked more than $2.5 billion of gross bookings over the trailing twelve "
  "months, growing in the high teens, through more than 140,000 restaurants "
  f"(<a href=\"{EZ_QSR}\">QSR Web</a>). Uber said the business is profitable on a "
  "non-GAAP operating income basis and expects it to lift its margins "
  f"(<a href=\"{EZ_AWP}\">AWP</a>). The deal needs regulatory approval and is "
  "expected to close in the coming months. The announcement framed it as "
  "ezCater&rsquo;s catering and B2B expertise joined to Uber "
  "Eats&rsquo; customers and restaurants and to Uber for Business.",

  "Put the two headline numbers side by side and Uber is paying a little under "
  "one year of ezCater&rsquo;s gross bookings, by my arithmetic. That is a "
  "generous price for food delivery and an ordinary one for a business whose "
  "customers are companies with budgets. The difference between those two "
  "readings is the whole bet.",
 ]),

 ("Why business lunch is the prize", [
  "None of the coverage I read gives a synergy figure, so what follows is my "
  "reading of where the value sits. It sits in four places, and each one starts "
  "with something Uber already owns.",

  "The first is the buyer. Uber for Business already handles employee meals, "
  "which means the person who sets the meal policy is already logged in. "
  "ezCater adds the order that is too big for a meal voucher, the lunch for "
  "twenty. Uber gets a new product to sell into 300,000 accounts, and ezCater "
  "gets a sales force that never has to make a cold call.",

  "The second is the size of the ticket. An order above $400, placed ahead of "
  "time, is worth many ordinary takeout orders to a restaurant and arrives "
  "with notice. Khosrowshahi described catering as a potential major revenue "
  "stream for restaurants, and the announcement promised couriers new earning "
  f"opportunities (<a href=\"{EZ}\">PYMNTS</a>). Scheduled demand is the "
  "easiest kind for a delivery network to plan around.",

  "The third is the bill. ezCater already invoices companies, and Uber for "
  "Business already reconciles expenses. Together they can put a ride to the "
  "client, the lunch for the meeting and the dinner afterward onto one "
  "statement, and a single statement is very hard to replace.",

  "The fourth is the competitor. <a href=\"" + EZ_BNN + "\">BNN Bloomberg</a> "
  "framed the deal as Uber&rsquo;s bet to narrow its gap with DoorDash in "
  "American food delivery. Corporate catering is a corner of that market where "
  "the customer is a company, and a company changes vendors far less often than "
  "a person changes apps.",
 ]),

 ("Two more rooms in the house", [
  "ezCater is the third move of the year, and the other two explain it. In July "
  f"Uber offered <a href=\"{DH}\">€41.50 a share in cash for Delivery Hero</a>, "
  "valuing the Berlin food delivery group at $14.8 billion. The combined company "
  "would operate in 99 markets, the number of markets where Uber offers both "
  "rides and delivery would rise from 34 to 58, and Uber says customers who use "
  "both services generate about three times the gross bookings and profit of "
  "customers who use one. It is paying from cash and new debt, with a committed "
  "bridge of about €14 billion, and expects to close in the second half of 2027.",

  "In April, at its Go-Get event, Uber began selling hotel rooms. It partnered "
  "with Expedia to give American customers more than 700,000 properties inside "
  "the Uber app, with 10% back in Uber One credits on every booking and Vrbo "
  f"rentals to follow (<a href=\"{HOTEL}\">Hotel Online</a>). Expedia processes "
  f"the bookings and handles the customer service (<a href=\"{TPG}\">The Points "
  "Guy</a>), so Uber is the storefront and Expedia owns the shelves. "
  "Khosrowshahi described Uber at the event as an app for everything.",

  "Put the three together and you can see a business trip that never leaves "
  "the app: the ride from the airport, the room, the dinner and the lunch for "
  "the client. Hotel booking is a consumer feature for American customers today, "
  "and Uber has not said it is coming to business accounts. It is the obvious "
  "next room, and the expense account is the hallway that connects them.",
 ]),

 ("Why a ride company wants your lunch", [
  "Delivery is already nearly as large as rides. In the second quarter Uber "
  "booked $27.5 billion in delivery against $29.0 billion in mobility, and "
  f"delivery grew faster, 26% to 22% (<a href=\"{Q2}\">the earnings release</a>). "
  "Rides are also the business with a cloud over it. Uber&rsquo;s "
  f"<a href=\"{K10}\">annual report</a> names Alphabet&rsquo;s Waymo, "
  "Amazon&rsquo;s Zoox and Tesla among companies that compete with it or may in "
  "future, while Waymo is also a partner whose cars can be hailed only through "
  f"Uber in <a href=\"{WAYMO_UBER}\">Austin and Atlanta</a>. Autonomous trips are "
  f"still under 0.5% of Uber&rsquo;s weekly volume (<a href=\"{CNBC}\">CNBC</a>).",

  "A robotaxi can carry a tray of sandwiches. It cannot sign a vendor agreement "
  "with a finance department, and a vendor agreement is most of what ezCater "
  "is. Every move this year points the same way, toward the parts of the "
  "business that depend on relationships, contracts and accounts, and away from "
  "the part that depends on who is driving.",
 ]),

 ("The case against", [
  "Three deals at once is a great deal of integration. Delivery Hero needs "
  "acceptances and clearances across many countries and will not close until "
  "the second half of 2027. ezCater still needs regulatory approval. The hotel "
  "business belongs, in the ways that matter most, to Expedia, which holds the "
  "inventory and the customer service.",

  "Office catering also depends on offices. Its growth rests on people being "
  "in the room for the meeting, and that is a habit no acquisition controls. "
  "DoorDash wants the same corporate lunch. And a single statement is only "
  "sticky if the services on it are each good enough to keep, so the bundle "
  "has to win line by line before it can win as a bundle.",
 ]),

 ("What to watch", [
  "First, whether ezCater closes on schedule and shows up inside Uber for "
  "Business accounts, which is where the synergy either appears or does not. "
  "Second, whether hotel booking reaches business accounts or travels beyond "
  "the United States. Third, the Delivery Hero acceptances during 2027. Fourth, "
  "Uber&rsquo;s third-quarter results, not yet reported as of 3 November, for "
  "whether delivery keeps outgrowing rides. A company that owns the expense "
  "account owns the habit, and these four numbers show how much of the habit "
  "Uber has bought.",
 ]),
]

NOTE = ("ezCater&rsquo;s figures are from the 6 October 2026 announcement as "
        "reported by PYMNTS, QSR Web and AWP. I could not read Uber&rsquo;s own "
        "release page, and none of the coverage I read gave a synergy figure, so "
        "the synergy argument is mine. The 300,000 businesses and the description "
        "of the account are from Uber&rsquo;s business page. Hotel details are "
        "from coverage of the 29 April Go-Get event and from The Points Guy. "
        "Delivery Hero terms, second-quarter figures and the competitor list "
        "come from Uber&rsquo;s own filings. The price compared with gross "
        "bookings is my arithmetic. The office manager is invented.")
