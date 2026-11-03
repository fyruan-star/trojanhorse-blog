"""Trojan Horse of the Week: ultra-personalized health.

Rewritten 3 November 2026 to the owner's brief: what these businesses reveal
about consumers, how that behavior becomes recurring revenue, and how the
spending reaches mainstream tech platforms. Under 1,200 words with the note.

Y Combinator counts are the author's arithmetic from the directory's industry
pages, downloaded 3 November 2026 (5,243 companies across the eight top-level
industries, each company listed once). "Consumer health" means YC's own
Consumer Health and Wellness label, so the same definition covers every year.
Company descriptions and headquarters are self-reported on YC profiles. Hims &
Hers figures are from its second-quarter 2026 release and its 2025 10-K. Oura's
panels are from Oura's own page. SURMOUNT-4 is from the ACC summary of the JAMA
Internal Medicine analysis. Platform features marked as proposals are the
author's.

No em dashes, no semicolons, no rhetorical questions, no sub-description.
"""

WEEK = "3 November 2026"
SLUG = "personalized-health"
KICKER = "Trojan Horse of the Week"
TITLE = "The Protein Shake Is the Front Door"
HOOK = ("A tub of protein is bought once, and a whole set of companies is "
        "betting its buyer will pay every month to be measured, interpreted "
        "and treated.")
LOGO = {"file": "ycombinator.svg", "w": 256, "h": 256, "name": "Y Combinator",
        "height": 36}
GO = ("uber-rival-dinner.html",
      "The previous Trojan horse: Uber gets into the expense report &rarr;")

YC = "https://www.ycombinator.com/companies/"
YC_HEALTH = "https://www.ycombinator.com/companies/industry/healthcare"
YC_CHW = "https://www.ycombinator.com/companies/industry/consumer-health-and-wellness"
HELIOS = YC + "helios-intelligence"
GUT = YC + "gutgutgoose"
RONAN = YC + "ronanrx-inc"
ILLUME = YC + "illume-labs"
HIMS = ("https://www.sec.gov/Archives/edgar/data/0001773751/000177375126000161/"
        "hims-20260630x8xkearningsr.htm")
HIMS_10K = "https://www.sec.gov/Archives/edgar/data/1773751/000177375126000022/hims-20251231.htm"
SURMOUNT = ("https://www.acc.org/latest-in-cardiology/journal-scans/2025/12/09/"
            "16/51/surmount-4")
OURA_LABS = "https://ouraring.com/blog/health-panels/"
INSTACART = "https://company.instacart.com/health"
MENUS = ("https://www.scrippsnews.com/life/money/heres-how-the-glp-1-boom-is-"
         "changing-fast-food-menus-and-prices")

SECTIONS = [

 ("", [
  "Walk into a grocery store and count the things promising protein. Cereal. "
  "Pancakes. Chips. Ice cream. The interesting question is what the customer "
  "buys next.",

  "A tub of whey is a one-time sale. The person who bought it has told the "
  "market something worth far more: they want their body to change, and they "
  "will pay to watch it happen. That is this week&rsquo;s Trojan horse. The "
  "first purchase is cheap and sensible, and inside it rides a willingness to "
  "pay again, every month, for measurement, interpretation and treatment. "
  "There is no acquisition in this story.",
 ]),

 ("What the startups reveal", [
  "Recent Y Combinator profiles point to four things customers want.",

  f"They want specific answers. <a href=\"{HELIOS}\">Helios Intelligence</a>, "
  "a Boston company from the fall 2026 batch, says its home kit reads more "
  "than 1,000 biomarkers from a drop of blood.",

  f"They want visible progress. <a href=\"{GUT}\">Gutgutgoose</a>, in San "
  "Francisco, sequences a customer&rsquo;s stool, formulates probiotics, then "
  "sequences again 90 days later to see what took hold. The retest is part of "
  "the product.",

  f"They want easy access. <a href=\"{RONAN}\">RonanRx</a>, also based in San "
  "Francisco, makes personalized peptides and GLP-1 drugs and sells them after "
  "a telehealth visit. Its base is one city, but where it can treat patients "
  "depends on state licenses, which it says it won in 33 states in ten weeks.",

  f"They want to be told what to do next. <a href=\"{ILLUME}\">Illume Labs</a> "
  "joins wearable, blood and genetic data and texts users their next step.",

  "None of these profiles proves that customers stay. They show where founders "
  "are placing bets.",
 ]),

 ("How big the bet is", [
  "Healthcare is a small part of Y Combinator. By my count of its "
  f"<a href=\"{YC_HEALTH}\">directory</a>, 67 of the 813 companies YC funded "
  "in 2026 are healthcare companies, about 8%. YC labels 8 of those 67 as "
  f"<a href=\"{YC_CHW}\">consumer health and wellness</a>, about 12%. That is "
  "no surge. By the same label the share was 21 of 92 in 2021.",

  "RonanRx and Gutgutgoose carry other tags, so the label undercounts the "
  "theme. What stands out this year is breadth: blood testing, gut "
  "sequencing, prescription drugs and the software that reads "
  "them all. Most are in San Francisco, like 46 of this year&rsquo;s 67 YC "
  "healthcare companies, so headquarters says more about YC than about the "
  "market. Licenses and lab networks decide where each one can sell.",
 ]),

 ("Recurring revenue is not cash", [
  "Each step invites a repeat. A blood panel invites a retest. A wearable "
  "carries a membership. A prescription refills. Treatment can also run long. "
  f"In Lilly&rsquo;s SURMOUNT-4 trial, <a href=\"{SURMOUNT}\">82% of the "
  "participants</a> switched from tirzepatide to placebo regained more than a "
  "quarter of their lost weight within a year, and the rest did not. Peptides "
  "are a looser group, with far less evidence behind most of them.",

  "Hims &amp; Hers shows the economics in public. In the second quarter it "
  f"reported <a href=\"{HIMS}\">nearly 2.9 million subscribers</a> paying an "
  "average of $92 a month, and revenue of $753.2 million. It also spent $262.2 "
  "million on marketing, about 35% of revenue by my arithmetic, saw gross "
  "margin fall to 64% from 76%, and reported free cash flow of negative $68.2 "
  "million.",

  "Recurring revenue is a promise of future payments. Cash flow is what "
  "remains after the drug, the pharmacy, the clinician, the lab, shipping, "
  "advertising and every customer who cancels. The customer comes back because the next measurement says whether the last "
  "purchase worked.",
 ]),

 ("Where the spending reaches tech", [
  "Every new health habit is a product change waiting for a platform that "
  "already has the customer.",

  "Wearables are becoming lab storefronts. Oura now sells "
  f"<a href=\"{OURA_LABS}\">$99 blood panels</a> to members in most American "
  "states, drawn at Quest and reported inside the app. A ring that measured "
  "sleep now sells the next measurement. That is new spending on top of the "
  "membership, and one more reason not to cancel it.",

  "Grocery apps can turn plans into baskets. Instacart already runs "
  f"<a href=\"{INSTACART}\">AI-powered health tags</a> across its catalog and "
  "Care Carts that let providers send groceries to patients. My proposal: a "
  "nutrition plan from a blood test becomes a weekly basket that reorders "
  "itself. That captures grocery spending from rival stores and makes orders "
  "more frequent.",

  "Delivery apps can sell the high-protein lunch. Chains are already adding "
  f"<a href=\"{MENUS}\">high-protein menus</a> for the GLP-1 era. I found no "
  "protein filter on Uber Eats, so these are proposals: filters by protein, "
  "discovery by nutrition goal, a standing weekly order and sponsored placement "
  "for high-protein dishes. Most of that captures spending from home cooking "
  "and rivals. Sponsored placement adds advertising revenue on top, sold to "
  "restaurants the app already serves.",

  f"Ad platforms collect from all of it. Hims <a href=\"{HIMS_10K}\">says</a> it "
  "buys space on digital, social, television, radio and outdoor media, and its "
  "marketing bill was a third of revenue. For whoever sells that space, it is "
  "additional spending, paid by the whole category.",
 ]),

 ("Who keeps the customer", [
  "Whoever holds the latest measurement holds the relationship, because the "
  "latest number decides what gets recommended next and where it is bought. A "
  "ring that sells blood tests, or a grocery app that receives the plan, sits "
  "closer to that decision than a supplement on a shelf. Even "
  f"<a href=\"thorne-loyalty.html\">Thorne</a>, which P&amp;G agreed to buy for "
  "$3.8 billion, could become the product someone else&rsquo;s app recommends.",
 ]),

 ("What could break it", [
  "Customers quit when the numbers stop moving, and Hims&rsquo; marketing bill "
  "shows what replacing them costs. A thousand biomarkers will flag some that "
  "mean nothing, and each false alarm costs a follow-up. Hims reshaped its weight-loss offer this year "
  "and now offers compounded GLP-1 drugs only on a limited scale. And if "
  "testing does not lead to results people can see, the retest is the first "
  "purchase they cancel.",
 ]),
]

NOTE = ("YC counts are my arithmetic from the directory&rsquo;s industry pages "
        "on 3 November 2026, and consumer health means YC&rsquo;s own label. "
        "Startup descriptions and RonanRx&rsquo;s license count are "
        "company-reported. Features marked as proposals are mine. Nothing here is medical advice.")
