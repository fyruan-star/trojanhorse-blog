"""Trojan Horse of the Week, 1 November 2026: Uber.

Written in the register of the Oura story: a dated scene, warm and a little
funny, an analogy doing the explaining, the figures underneath. Every company
figure is from Uber's own filings (Q2 2026 earnings release, the FY2025 10-K,
the Q2 10-Q, the Delivery Hero announcement and the Autonomous Solutions
release). Waymo's scale is from TechCrunch and its Uber arrangement from
Waymo's own page. The analyst view is attributed to the report it came from.
One direct quote, the CEO's.

The notes this was written from described Uber as distressed. The filings do
not support that word, so the story treats the worry as strategic, from a
position of record cash flow, which is the midlife-crisis shape of the thing.
It also says Waymo's only active delivery operation, as of its October 2025
announcement, is a pilot with DoorDash, which is narrower than "cannot deliver."

No em dashes, no semicolons, no rhetorical questions, no sub-description under
the title.
"""

WEEK = "1 November 2026"
SLUG = "uber-rival-dinner"
KICKER = "Trojan Horse of the Week"
TITLE = "Uber Invites Its Rival to Dinner"
HOOK = ("Uber offered $14.8 billion for Delivery Hero while its own annual "
        "report names Waymo, its robotaxi partner, as a potential competitor.")
LOGO = {"file": "uber.svg", "w": 926.906, "h": 321.777, "name": "Uber", "height": 34}
GO = ("oura-ipo.html",
      "The previous Trojan horse: Oura sleeps on its IPO &rarr;")

Q2 = ("https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/"
      "uberq226earningspressrelea.htm")
CNBC = "https://www.cnbc.com/2026/08/05/uber-stock-q2-2026-earnings.html"
K10 = "https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm"
Q10 = "https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000032/uber-20260630.htm"
DH = ("https://www.sec.gov/Archives/edgar/data/0001543151/000155278126000382/"
      "e26302_ex99-1.htm")
AVS = ("https://investor.uber.com/news-events/news/press-release-details/2026/"
       "Uber-Unveils-Uber-Autonomous-Solutions-to-Accelerate-Autonomous-Mobility--"
       "Delivery-Worldwide/default.aspx")
WAYMO_UBER = "https://waymo.com/waymo-on-uber"
WAYMO_RIDES = "https://techcrunch.com/2026/03/27/waymo-skyrocketing-ridership-in-one-chart"
WAYMO_GOAL = ("https://www.bloomberg.com/news/articles/2026-02-11/waymo-co-ceo-"
              "outlines-path-to-1-million-weekly-trips-in-2026")
DOORDASH = ("https://techcrunch.com/2025/10/16/waymo-dips-its-wheels-back-into-"
            "delivery-this-time-with-doordash/")
CITIZENS = ("https://parameter.io/uber-uber-stock-analysts-maintain-bullish-outlook-"
            "following-13-7b-delivery-hero-acquisition/")
TASKS = ("https://www.inquirer.com/business/uber-data-tasks-ai-labeling-datasets-"
         "drivers-20251018.html")

SECTIONS = [

 ("A good quarter and a worse mood", [
  "Picture the morning of Wednesday 5 August 2026. Uber had just reported a "
  f"quarter most companies would frame and hang in the lobby (<a href=\"{Q2}\">"
  "the earnings release</a>). Gross bookings were $58.0 billion, up 24%. Net "
  "income was $2.4 billion, including a $1.6 billion pre-tax gain from revaluing "
  "its investments. Free cash flow over the trailing twelve months passed $10 "
  "billion for the first time in the company&rsquo;s history. By the close the "
  f"shares were down 5.3%, and <a href=\"{CNBC}\">CNBC reported</a> they had "
  "been down 12% for the year while the Nasdaq was up 14%. I love a company "
  "that does its worrying from a position of strength. It resembles a person "
  "with a corner office, a good salary and a sudden interest in sailing, and the "
  "use of a midlife crisis is that it reveals what the person is afraid of.",
 ]),

 ("What the annual report admits", [
  "Uber is afraid of cars that drive themselves, and it says so in writing. In "
  f"<a href=\"{K10}\">its annual report</a> it names Alphabet&rsquo;s Waymo, "
  "Amazon&rsquo;s Zoox and Tesla among the companies that either compete with "
  "it or may compete with it in the future. The risk factors add that Waymo has "
  "already put a commercial fleet on its own platform, that rivals could "
  "deploy autonomous vehicles on platforms other than Uber&rsquo;s, and that "
  "Uber&rsquo;s own partners could remove their vehicles from its network.",

  "Waymo is also one of those partners. In Austin and Atlanta its cars can be "
  f"hailed only through Uber&rsquo;s app, <a href=\"{WAYMO_UBER}\">according to "
  "Waymo&rsquo;s own page</a>, and in most of its other cities Waymo runs its "
  "own app. Imagine a restaurant that rents its dining room to a chef who is "
  "opening a place across the street, and then add that the chef is very good.",

  "The threat is real and small at once. Waymo reported <a "
  f"href=\"{WAYMO_RIDES}\">500,000 paid rides a week across ten U.S. "
  f"cities</a> in March and has talked about reaching a million by the end of "
  f"the year (<a href=\"{WAYMO_GOAL}\">Bloomberg</a>). Uber does roughly 300 "
  "million trips a week, which puts Waymo&rsquo;s rides at about one in 600 of "
  "Uber&rsquo;s volume by my arithmetic, and Uber says autonomous trips of every "
  "kind are under 0.5% of its total. Its chief executive says trips grew faster "
  "in markets where robotaxis are widely available through Uber (CNBC). That "
  "is Uber&rsquo;s argument, that the cars are supply and supply fills "
  "demand. The annual report worries about the reverse, a supply that learns "
  "to find the demand without Uber.",
 ]),

 ("Move one: open every door", [
  "On 23 February 2026 Uber launched <a href=\"" + AVS + "\">Uber Autonomous "
  "Solutions</a>, a menu of services for anyone building a robotaxi. It covers "
  "data and mapping, the software a rider sees inside the car, and what Uber "
  "calls fleet operations: a mission-control system that shows operators every "
  "vehicle, remote assistance, field teams that handle lost items, towing and "
  "cleaning, and insurance. The partners include Nuro and Lucid, Volkswagen, "
  "Avride, Wayve, WeRide and NVIDIA. Its chief executive has said Uber "
  "expects to commit more than $10 billion over the coming years, and in the "
  "second-quarter release its chief "
  "executive, Dara Khosrowshahi, said Uber is building &ldquo;the world&rsquo;s "
  "largest platform for autonomous vehicles.&rdquo;",

  "There is a logic to it. A company that builds a self-driving car is good at "
  "software and short of exactly what Uber already has, which is riders, field "
  "crews who will clean a car at midnight, and an insurer. Uber is offering a "
  "new robotaxi maker customers and the unglamorous work in one contract. That "
  "is the horse. The partners arrive as gifts, new supply with no driver "
  "attached, and the exposure comes through the same gate, since the 10-K says "
  "those vehicles can leave. Uber and Waymo have said they will end their "
  "exclusive arrangement in Atlanta and Austin by early 2028, which CNBC "
  "described as Waymo pulling away.",
 ]),

 ("Move two: buy dinner", [
  f"On 16 July 2026 Uber offered <a href=\"{DH}\">€41.50 a share in cash for "
  "Delivery Hero</a>, the Berlin-based food delivery group. That values the "
  "whole company at $14.8 billion, or $13.7 billion once the stake Uber had "
  "already bought is netted out. It was no stranger&rsquo;s bid. Uber already "
  "held about 25% of the voting shares and about 12% more through derivatives, "
  f"and <a href=\"{Q10}\">its 10-Q</a> shows $1.6 billion of total return swaps "
  "on Delivery Hero stock in the second quarter. Prosus has agreed to tender its "
  "remaining stake of about 17%, which would bring Uber&rsquo;s economic "
  "interest to about 53%.",

  "The offer needs 50% plus one share and merger-control and financial "
  "regulatory clearances, and Uber expects to close in the second half of 2027. "
  "It will pay from cash and new debt, with a committed bridge facility of about "
  "€14 billion, and it says it expects to keep an investment grade rating and "
  "gross leverage below 2x. Uber&rsquo;s pitch is breadth. The combined "
  "company would operate in 99 markets with pro forma 2025 gross bookings of "
  "$236 billion, and the number of markets where it offers both rides and "
  "delivery would rise from 34 to 58. Uber says customers who use both "
  "services generate about three times the gross bookings and profit of "
  "customers who use one.",

  "Dinner is already close to the size of the ride. In the second quarter "
  "delivery gross bookings were $27.5 billion against $29.0 billion for "
  "mobility, and delivery grew faster, 26% to 22%. A robotaxi&rsquo;s job "
  "description is moving a person. Waymo&rsquo;s one active delivery operation, "
  f"as of <a href=\"{DOORDASH}\">its October 2025 announcement</a>, was a "
  "Phoenix pilot with DoorDash, Uber Eats&rsquo; rival, carrying orders from "
  "DoorDash&rsquo;s own stores. Citizens&rsquo; Andrew Boone, as <a "
  f"href=\"{CITIZENS}\">Parameter reports</a> it, holds that delivery has a "
  "stronger competitive position than mobility.",
 ]),

 ("What Uber has to trade with", [
  "Uber has three things a robotaxi company lacks, and each shows in the "
  "filings. The first is the name. In the second quarter 208 million people "
  "used the platform in a month, up 16%, and they took 3.9 billion trips. The "
  "second is cash. Free cash flow was $2.8 billion in the quarter, the company "
  "spent $3.5 billion on buybacks in the first six months, and it has lined up "
  "a bridge for the Delivery Hero offer without changing its buyback "
  "framework.",

  f"The third is people. Uber has drivers and couriers, and a business built "
  f"around the unglamorous work of cars in the physical world. Its data-services "
  f"unit, Uber AI Solutions, offers drivers small digital tasks when they are "
  f"offline, such as recording audio samples or uploading menus, and Uber&rsquo;s "
  f"product chief said it was a way to keep drivers earning and not a response "
  f"to being displaced by autonomous vehicles (<a href=\"{TASKS}\">Bloomberg, via "
  f"the Inquirer</a>). The field teams that clean and tow robotaxis apply the "
  f"same idea to a different customer.",
 ]),

 ("The case against", [
  "The honest worry comes in two parts. The first is the borrowing. A $14.8 "
  "billion offer funded partly by new debt, with a closing a year away, is a "
  "commitment made while the stock is down. Uber is also promising no workforce "
  "changes at the Berlin headquarters until at least 2029 and a €2 billion "
  "investment in Germany over five years, which narrows where it can find "
  "savings.",

  "The second is that dinner does not hedge the ride. Rides remain the larger "
  "business, the 10-K says its autonomous partners could leave or compete, and "
  "delivery has its own robotaxi pilot under way, run by a competitor. A "
  "commitment of more than $10 billion to partners that may not "
  "stay is a bet on many horses, and the document that describes the bet also "
  "describes the exit.",
 ]),

 ("What to watch", [
  "Four things can be checked in public. The first is what happens to Waymo on "
  "Uber&rsquo;s app once the exclusive arrangement in Austin and Atlanta ends "
  "by early 2028. The second is how the Delivery Hero offer moves through "
  "acceptance and clearances during the second half of 2027. The third is "
  "whether autonomous trips climb past the 0.5% of Uber&rsquo;s volume that "
  "Uber reports today. The fourth is whether delivery keeps growing faster than "
  "rides, 26% against 22% in the latest quarter. A company can be "
  "worried and well run at the same moment, and these four numbers show which "
  "of the two is gaining.",
 ]),
]

NOTE = ("Company figures come from Uber&rsquo;s second-quarter 2026 earnings "
        "release, its 2025 annual report, its second-quarter 10-Q and its "
        "Delivery Hero announcement and Autonomous Solutions release. Waymo&rsquo;s "
        "ride count is from TechCrunch, its year-end goal is from Bloomberg&rsquo;s "
        "headline, and its Uber arrangement is from Waymo&rsquo;s own page. The "
        "analyst view is as reported by Parameter and was not checked against "
        "Citizens&rsquo; own note. The share of Uber&rsquo;s volume that Waymo "
        "represents is my arithmetic from a March figure and an August one, so it "
        "is a scale and not a measurement. The notes this story grew from called "
        "Uber distressed. Its filings show record cash flow, so the story treats "
        "the worry as strategic.")
