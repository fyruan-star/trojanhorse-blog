"""Trojan Horse of the Week: health becomes an aesthetic.

Rewritten 3 November 2026 to the owner's brief: one point, argued with
conviction. Health tech is a small slice of startups but the fastest-growing
one, and it will keep exploding because people now buy health the way they buy
fashion, by how it looks and feels. That is how it reaches Amazon, clothing
resale, Uber Eats and the look of tech itself. Predictions are labelled as
predictions. No figure is invented.

Sources read: YC directory industry pages, downloaded 3 November 2026 (counts
are the author's arithmetic, grouped by batch year). KFF poll, Oct to Nov 2025.
Rock Health Q3 2026 via HIT Consultant. Function Health's Series B via Athletech
News. Amazon's own Medicare GLP-1 announcement. Scripps on high-protein menus.
RonanRx figures are self-reported on its YC profile.

No em dashes, no semicolons, no rhetorical questions, no sub-description.
"""

WEEK = "3 November 2026"
SLUG = "personalized-health"
KICKER = "Trojan Horse of the Week"
TITLE = "Peptides Inject Their Way Into Tech"
HOOK = ("Y Combinator funded 56% more healthcare startups in 2026 than in 2025, "
        "and the demand behind them looks more like fashion than medicine.")
LOGO = {"file": "ycombinator.svg", "w": 256, "h": 256, "name": "Y Combinator",
        "height": 36}
GO = ("uber-rival-dinner.html",
      "The previous Trojan horse: Uber Eats, Uber Hotels, Uber Catering, Uber Everything? &rarr;")

YC = "https://www.ycombinator.com/companies/"
YC_HEALTH = "https://www.ycombinator.com/companies/industry/healthcare"
RONAN = YC + "ronanrx-inc"
LUMERIA = YC + "lumeria"
LAYERS = YC + "layers"
HELIOS = YC + "helios-intelligence"
KFF = ("https://www.kff.org/health-costs/poll-1-in-8-adults-say-they-are-currently-"
       "taking-a-glp-1-drug-for-weight-loss-diabetes-or-another-condition-even-as-"
       "half-say-the-drugs-are-difficult-to-afford/")
ROCK = "https://hitconsultant.net/?p=98197"
FUNCTION = "https://athletechnews.com/function-health-raises-298-million-at-2-5-billion-valuation/"
AMAZON = "https://www.aboutamazon.com/news/retail/amazon-pharmacy-glp-1-medicare"
MENUS = ("https://www.scrippsnews.com/life/money/heres-how-the-glp-1-boom-is-"
         "changing-fast-food-menus-and-prices")

SECTIONS = [

 ("", [
  "Walk into a grocery store and count the things promising protein. Cereal. "
  "Pancakes. Chips. Ice cream. The interesting question is what the customer "
  "buys next.",

  "My answer: more health, every year, from more of the companies they already "
  "use. The health boom is nowhere near its peak, and the reason is simple. "
  "People now buy health to look well, and looking well is a purchase that "
  "never finishes. That is this week&rsquo;s "
  "Trojan horse. A protein shake looks like a snack. Inside it rides a customer "
  "who will pay for the rest of their life to see their body change. There is "
  "no acquisition in this story. It is a prediction about where that customer "
  "takes the rest of tech.",
 ]),

 ("The numbers already point one way", [
  "Healthcare is a small slice of Y Combinator, 67 of the 813 companies it "
  f"funded in 2026 by my count of its <a href=\"{YC_HEALTH}\">directory</a>. "
  "It is also the slice that is growing fastest. In 2025 YC funded 43 "
  "healthcare companies. This year it funded 67, a rise of 56%, while the "
  "whole program grew 34%. The consumer companies in that group cover the "
  f"entire body: a <a href=\"{HELIOS}\">1,000-biomarker blood test</a>, a "
  f"<a href=\"{LUMERIA}\">skin scanner</a> that calls itself the Oura Ring for "
  f"skin, and <a href=\"{RONAN}\">RonanRx</a>, which sells personalized "
  "peptides and GLP-1s and says it has grown 50% a week since launch.",

  "The money is following. Digital health startups raised "
  f"<a href=\"{ROCK}\">$11.1 billion</a> through the third quarter, according "
  "to Rock Health, which expects more than $14.8 billion for the year, and the "
  "average round has grown from $20.6 million in 2024 to $31.0 million. "
  f"Function Health, which sells a yearly blood-testing membership, raised "
  f"<a href=\"{FUNCTION}\">$298 million at a $2.5 billion valuation</a>.",

  "And the customers are already here. One in eight American adults says they "
  f"are <a href=\"{KFF}\">currently taking a GLP-1 drug</a>, up from 18 months "
  "earlier. Rock Health finds 46% own a wearable and 57% track their health "
  "digitally.",
 ]),

 ("Why it keeps exploding", [
  "Health is an aesthetic purchase now. People care far more about how they look "
  "and feel than they did a decade ago, and a product that works but does not "
  "look the part loses to one that does.",

  "That changes the economics. Feeling better is invisible, so people stop "
  "paying once they feel fine. Looking better is visible, measurable and "
  "public, so people keep paying to keep it. Peptides and GLP-1s are the "
  "clearest case: the result shows in the mirror and in every photo, and that "
  f"makes the next refill an easy sale. <a href=\"{LAYERS}\">Layers</a>, a YC "
  "company, says it outright on its profile, that improving how you look and "
  "feel leads to better outcomes in career and relationships, and that belief "
  "is the demand I expect to drive the next decade of health spending.",
 ]),

 ("How it trickles into the platforms", [
  "The boom will not stay inside health companies. It will leak into every "
  "app that already has the customer, and the first leaks are visible.",

  f"Amazon is already a weight-loss pharmacy. It now <a href=\"{AMAZON}\">"
  "delivers GLP-1 drugs</a> to eligible Medicare patients for $50 a month, runs "
  "a One Medical weight-management program in 48 states, and offers same-day "
  "pharmacy delivery in more than 3,100 American cities and towns. My "
  "prediction: the next step is the cart around the prescription, with protein, "
  "scales and supplements recommended beside the refill.",

  "Clothing is next. My prediction is that eBay and Etsy become quiet winners "
  "of the GLP-1 era. A body that changes size needs a new wardrobe, and the old "
  "one has to go somewhere. Resale gets both sides of that trade, the closet "
  "people sell and the smaller sizes they buy, and sellers who list by fit and "
  "body change will get found first.",

  "Food delivery follows. Chains are already adding "
  f"<a href=\"{MENUS}\">high-protein menus</a> for GLP-1 customers. My "
  "prediction is a Healthy section on Uber Eats, with protein filters, smaller "
  "portions and sponsored placement for the restaurants that cook for it. The "
  "spending already exists. The app that organizes it collects the fee and the "
  "advertising.",
 ]),

 ("Tech has to look like health", [
  "If health is an aesthetic, then technology has to look healthy. Look at the brands winning "
  "this market: clean futuristic marks, thin precise type, matte surfaces, "
  "dashboards that read like a lab report. Oura, Function and the new YC "
  "companies all look like they came out of the same clinic of the future.",

  "My prediction is that this look spreads to companies that have nothing to "
  "do with health. Logos, fonts and app screens will keep moving toward that "
  "calm, clinical style, because customers now read it as trust. The companies "
  "that win the next decade of consumer tech will be the ones that hold a daily "
  "measurement of the body and look good enough to be opened every morning.",
 ]),

 ("What would prove me wrong", [
  "Two things. If GLP-1 prices or rules cut access sharply, the most visible "
  "results disappear and the spending slows. And if results stop showing, the "
  "aesthetic case loses its proof.",
 ]),
]

NOTE = ("YC counts are my arithmetic from the directory&rsquo;s industry pages "
        "on 3 November 2026, grouped by batch year. RonanRx&rsquo;s growth is "
        "company-reported. Rock Health figures are as reported by HIT Consultant. "
        "Statements marked as predictions are mine. Nothing here is medical "
        "advice.")
