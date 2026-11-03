"""Trojan Horse of the Week: ultra-personalized health.

Written 3 November 2026 from the owner's brief: no single deal this week, a
waterfall of consumer health that starts with protein and ends back at the
recommendation, and how many Y Combinator startups now sit on it.

Every company description is the company's own, from its Y Combinator profile,
read on 3 November 2026 from the directory's healthcare and consumer health
pages. The count of eight is the author's reading of the 49 newest healthcare
listings (all 2026 batches) and says so. Oura and Thorne figures are from the
earlier stories, which cite the S-1 and P&G. The student buying protein is
invented and labelled. One direct quote, RonanRx's own last line.

No em dashes, no semicolons, no rhetorical questions, no sub-description under
the title.
"""

WEEK = "3 November 2026"
SLUG = "personalized-health"
KICKER = "Trojan Horse of the Week"
TITLE = "The Protein Shake Is the Front Door"
HOOK = ("By my count, eight of Y Combinator&rsquo;s 49 newest healthcare startups "
        "sell personalized health straight to consumers, and together they cover "
        "nearly every step from a tub of protein to a prescription.")
LOGO = {"file": "ycombinator.svg", "w": 256, "h": 256, "name": "Y Combinator",
        "height": 36}
GO = ("uber-rival-dinner.html",
      "The previous Trojan horse: Uber gets into the expense report &rarr;")

YC = "https://www.ycombinator.com/companies/"
YC_HEALTH = "https://www.ycombinator.com/companies/industry/healthcare"
YC_CHW = "https://www.ycombinator.com/companies/industry/consumer-health-and-wellness"
LAYERS = YC + "layers"
MITO = YC + "mito-health"
GUT = YC + "gutgutgoose"
LUMERIA = YC + "lumeria"
RONAN = YC + "ronanrx-inc"
PHOENIX = YC + "phoenix"
HELIOS = YC + "helios-intelligence"
INSTALAB = YC + "instalab"
LUCIS = YC + "lucis"
ILLUME = YC + "illume-labs"
NORI = YC + "nori"
PRANA = YC + "prana-health"
CLARA = YC + "clara-2"

SECTIONS = [

 ("A tub of protein", [
  "Picture the evening of Monday 3 November 2026. A sophomore, who exists only "
  "in this story, has decided he would like to look better by spring. He does "
  "what everyone does first. He buys a tub of whey, stocks the fridge with eggs "
  "and chicken thighs, and downloads an app to count grams of protein. It is the "
  "cheapest, safest and most sensible step in all of health, and it is also the "
  "front door to an industry that would like him to keep walking.",

  "There is no acquisition in this week&rsquo;s story. This one is about a "
  "market that is assembling itself, step by step, and about how many young "
  "companies are building the steps.",
 ]),

 ("The horse is the word personal", [
  "Every Trojan horse has the same parts. Here the horse is personalization. "
  "The customer welcomes it because generic advice has failed him before, and a "
  "plan built from his own body looks like the opposite of a sales pitch. It "
  "looks like a gift, an expert who has read his file. What rides inside is a "
  "measurement, and every measurement is built to find the next thing worth "
  "measuring. The harm, when there is any, is gradual. A goal that began in the "
  "gym can travel, one reasonable step at a time, to a prescription and a "
  "monthly lab draw, and each step is sold by the data from the step before.",

  "A labelled analogy helps. Think of a waterfall with pools. Water lands in "
  "the first pool, fills it, and spills into the next one down. Each pool is a "
  "business, and the water is the customer&rsquo;s attention, money and data. "
  "The pools sit lower and lower, closer to medicine, and the spill from one is "
  "the inflow of the next.",
 ]),

 ("The first three pools", [
  "The first pool is food. Protein and whole foods ask for no data at all, "
  "which is exactly why everyone starts there. Then the goal sharpens. "
  f"<a href=\"{LAYERS}\">Layers</a>, a 2025 Y Combinator company, says on its "
  "profile that improving how you look and feel leads to better outcomes in "
  "career and relationships, and that the body can be optimized like any other "
  "system. That sentence is the whole first pool, written as a mission "
  "statement.",

  "The second pool is supplements. This is where the money first became large "
  "enough for a consumer giant to notice. P&amp;G "
  "agreed in August to pay <a href=\"thorne-loyalty.html\">$3.8 billion for "
  "Thorne</a>. Below that sit the startups that personalize the pill bottle. "
  f"<a href=\"{GUT}\">Gutgutgoose</a> sequences a customer&rsquo;s stool, "
  "formulates the probiotics it says the gut is missing, and sequences again 90 "
  f"days later to see what took hold. <a href=\"{MITO}\">Mito Health</a> sells "
  "a $9 a month membership that includes more than 11,000 practitioner-grade "
  "supplements at cost, Thorne among them.",

  "The third pool is the wearable and the gym. A ring or a watch turns the "
  "workout into a score, and a score asks to be improved. Oura reported "
  f"<a href=\"oura-ipo.html\">5.0 million paid members</a> by June, and about "
  "85% of members still paying after a year. The idea has become a unit of "
  f"description. <a href=\"{LUMERIA}\">Lumeria</a>, from the summer 2026 batch, "
  "calls itself the Oura Ring for skin. It clips a multispectral camera onto a "
  "phone, tracks breakouts and wrinkles over time, and matches products to what "
  "the customer&rsquo;s own data says works.",
 ]),

 ("Two pools closer to the doctor", [
  "The fourth pool is where the water turns medical: peptides, testosterone "
  "and hormone therapy. <a href=\"" + RONAN + "\">RonanRx</a>, also from the "
  "summer 2026 batch, describes itself as a full-stack pharmaceutical company "
  "starting with personalized peptides and GLP-1s. Its profile says it went "
  "from no pharmacy to licenses in 33 states in its first ten weeks, has grown "
  "50% week over week since launch, manufactures the drugs itself and sells "
  "directly to patients after a telehealth visit with a licensed doctor. Its "
  "last line names the next pool: &ldquo;Next comes hormone therapy and the "
  "rest of personalized medicine.&rdquo; An older Y Combinator company, "
  f"<a href=\"{PHOENIX}\">Phoenix</a>, already runs a digital clinic for men in "
  "Canada.",

  "The fifth pool is the blood test, and it is the busiest. "
  f"<a href=\"{HELIOS}\">Helios Intelligence</a>, from the fall 2026 batch, "
  "sells an at-home test that it says measures more than 1,000 biomarkers from "
  "a drop of blood, and describes its goal as a world model of human biology. "
  f"<a href=\"{INSTALAB}\">Instalab</a> sells proactive testing to what it calls "
  f"tens of thousands of founders, executives and athletes. <a href=\"{LUCIS}\">"
  "Lucis</a> describes itself as Function Health for Europe, which tells you "
  "that a blood-testing brand has also become a unit of description. Mito "
  "Health lists more than 12,000 lab tests.",
 ]),

 ("The pool that feeds the first one", [
  "A waterfall ends in a river. This one ends in a recommendation, and the "
  "recommendation sends the customer back to the top. "
  f"<a href=\"{ILLUME}\">Illume Labs</a> connects wearables, blood panels and "
  "genetic data and texts its users what changed and what to do next. "
  f"<a href=\"{NORI}\">Nori</a> turns Apple Health, records and wearables into "
  f"a daily plan. <a href=\"{PRANA}\">Prana</a> watches records and wearables "
  f"for what it calls clinical drift. <a href=\"{CLARA}\">Clara</a> calls itself "
  "an AI primary care and longevity practice. RonanRx says labs, wearables and "
  "treatment response feed back into its platform so doctors can refine the "
  "dose.",

  "Follow the sophomore through it. His blood test says his vitamin D is low, "
  "so the plan recommends a supplement. His ring says his sleep is poor, so the "
  "plan recommends magnesium and an earlier dinner. A later panel suggests a "
  "conversation about hormones. Each recommendation is reasonable on its own, "
  "and each one buys a product from an earlier pool and books a measurement "
  "from a later one. The water goes round. Gutgutgoose puts the economics "
  "plainly on its profile: most data companies pay for their data and its "
  "own data pays for itself.",
 ]),

 ("How many, really", [
  f"Y Combinator&rsquo;s <a href=\"{YC_HEALTH}\">healthcare directory</a> runs "
  "to thirteen pages of fifty, more than 600 companies by my arithmetic, and "
  f"its <a href=\"{YC_CHW}\">consumer health and wellness</a> list holds about "
  "90. On 3 November the 49 newest healthcare listings were all from 2026 "
  "batches. By my count eight of them sell personalized health directly to "
  "people: Helios Intelligence, Lumeria, RonanRx, Gutgutgoose, Illume Labs, "
  "Omanta, Clara and Juno. Most of the other 41 sell artificial intelligence "
  "to hospitals, clinics and insurers, for billing, radiology and the front "
  "desk.",

  "So the honest answer is that consumer health is a minority of what Y "
  "Combinator is funding in healthcare, about one in six of the newest "
  "companies. The striking thing is the coverage. Within a single year of "
  "batches there is a company for nearly every pool: skin scanning, gut "
  "sequencing, peptides, a thousand-biomarker blood test, and a texting "
  "companion that ties them together. Y Combinator does not plan the "
  "waterfall, and its founders build it anyway, each one assuming the pool "
  "above will keep filling.",
 ]),

 ("Where it could break", [
  "Three things could slow the water. The first is the false alarm. A test "
  "that measures a thousand markers will flag some of them, and a flag that "
  "means nothing still costs a follow-up, a supplement or an anxious week. The "
  "second is the stakes. The first three pools sell food, pills and devices, "
  "while the fourth sells prescription drugs, which is why RonanRx puts a "
  "licensed doctor between the intake and the medicine. Mistakes cost more at "
  "the bottom of the falls. The third is the bill. A membership, a ring, a "
  "panel, a prescription and a protein subscription each look modest, and "
  "together they become a second rent.",

  "The case for the waterfall is also strong. People stay. Oura&rsquo;s "
  "retention shows that customers who are measured every morning keep paying, "
  "and Mito Health&rsquo;s pitch, prices at cost with itemized receipts, shows "
  "that some founders are competing on the cost problem directly.",
 ]),

 ("What to watch", [
  "First, whether RonanRx reaches hormone therapy, the step it has already "
  "named. Second, whether a large consumer company that bought into an upper "
  "pool, as P&amp;G did with Thorne, reaches down into testing or "
  "prescriptions. Third, how many of the Winter 2027 companies, whose "
  "applications were due by 2 November, land in consumer health. Fourth, whether "
  "the companies that recommend begin to own the products they recommend, "
  "because that is the moment a waterfall becomes a single business. The "
  "sophomore only wanted to look better by spring, and every pool below him is "
  "betting that he will want to know why.",
 ]),
]

NOTE = ("Company descriptions and figures are the companies&rsquo; own, from "
        "their Y Combinator profiles read on 3 November 2026, and were not "
        "independently checked. The count of eight, the share of the newest "
        "listings and the size of the directory are my arithmetic from the "
        "directory&rsquo;s pages. Oura and Thorne figures come from the earlier "
        "stories and their sources. Y Combinator has not acquired anything here, "
        "and its mark identifies the batch and implies no endorsement. The "
        "sophomore is invented. Nothing here is medical advice.")
