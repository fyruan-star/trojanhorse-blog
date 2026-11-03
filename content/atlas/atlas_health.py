"""Tech Atlas, Phase 2, sector 14: Health technology."""

ENT = {
 "abridge": ("Abridge", "AI note-taking for doctors, used by large health systems."),
 "openevidence": ("OpenEvidence", "AI reference tool for clinicians, valued at $15bn."),
 "hippocratic": ("Hippocratic AI", "Healthcare staffing agents."),
 "ambience": ("Ambience Healthcare", "AI scribe and coding for health systems."),
 "isomorphic": ("Isomorphic Labs", "Alphabet's AI drug discovery company."),
 "insilico": ("Insilico Medicine", "AI drug discovery company with a Phase 3 trial."),
 "recursion": ("Recursion", "Biotech using automated labs and AI."),
 "xaira": ("Xaira Therapeutics", "AI drug discovery startup."),
 "intuitive": ("Intuitive Surgical", "da Vinci surgical robots and the Ion lung system."),
}

SECTOR = dict(
 id="health", name="Health technology", band="industries",
 blurb="The AI tools doctors use, the drugs AI claims to have found, and the robots in the operating room.",
 positions=[

  dict(id="clinical", name="Clinical AI",
   metric=("No usage share exists for AI scribes. Abridge reports over $100m of ARR and more than 300 health systems, including all 40 Kaiser Permanente hospitals. OpenEvidence is reported at $15bn after a $250m round in September 2026 with about $300m of annualized revenue. Valuations come from aggregators."),
   metric_src="https://valueaddvc.com/blog/abridge-valuation-2026-5-3b-100m-arr-and-how-the-ai-scribe-beat-nuance-and-ambience",
   players=[
    dict(e="abridge", t="starter", conf="reported",
     stat="$5.3bn valuation, over $100m of ARR, more than 300 health systems. Integrated with Epic.",
     why="Won the largest health systems early and plugs into the main medical record.", cond="Epic and Microsoft's Dragon Copilot were not researched here, and both sell similar tools.",
     src="https://valueaddvc.com/blog/abridge-valuation-2026-5-3b-100m-arr-and-how-the-ai-scribe-beat-nuance-and-ambience"),
    dict(e="ambience", t="second", conf="reported",
     stat="Reported $243m Series C and a valuation above $1bn.", why="Sells scribe and coding together.", cond="Smaller than Abridge.",
     src="https://newmarketpitch.com/blogs/news/healthcare-ai-top-startups-valuation"),
    dict(e="hippocratic", t="second", conf="reported",
     stat="$126m raised in November 2025 at a $3.5bn valuation, about $404m in total.", why="Sells agents that call patients and handle routine staff tasks.", cond="No 2026 round was found.",
     src="https://aifundingtracker.com/top-ai-healthcare-startups/"),
    dict(e="openevidence", t="rookie", conf="reported",
     stat="$250m at $15bn in September 2026, after $250m at $12bn in January 2026. About $300m of annualized revenue and about $700m raised.",
     why="Clinicians use it to look things up, and advertising can pay for it.", cond="Earlier valuations come from sources that do not fully agree.",
     src="https://sacra.com/c/openevidence/"),
   ]),

  dict(id="drugs", name="AI drug discovery",
   metric=("No drug discovered mainly by AI has been approved yet, and AI-designed drugs fail in Phase 2 about as often as other drugs (one source). Insilico's rentosertib is the most advanced AI-linked candidate, in a 320-patient Phase 3 trial whose start date is reported as July or September 2026."),
   metric_src="https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026",
   players=[
    dict(e="insilico", t="starter", conf="reported",
     stat="Rentosertib for idiopathic pulmonary fibrosis in a registered 320-patient Phase 3, with sources conflicting on timing.",
     why="First with both an AI-found target and an AI-designed molecule at this stage.", cond="Trial results, which are years away.",
     src="https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026"),
    dict(e="recursion", t="second", conf="reported",
     stat="Lead program REC-4881 is listed as Phase 2 in one source and Phase 1b/2 in another.", why="Runs its own automated labs to feed models.", cond="Stage is unclear across sources.",
     src="https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026"),
    dict(e="isomorphic", t="rookie", conf="reported",
     stat="$2.1bn Series B announced 12 May 2026. First clinical trials expected by the end of 2026. No molecule disclosed as of May.",
     why="Built on the protein-structure research that won a Nobel Prize.", cond="One source's claim of $3bn in pharma partnerships is uncorroborated.",
     src="https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026"),
    dict(e="xaira", t="rookie", conf="reported",
     stat="First drug programs reportedly revealed in October 2026, preclinical.", why="Large funding to build models and a lab at once.", cond="Single source.",
     src="https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026"),
   ]),

  dict(id="devices", name="Surgical robots",
   metric=("Intuitive's da Vinci installed base was about 11,710 systems at 30 June 2026, up 12%. Da Vinci procedures grew about 15% and Ion procedures about 36% in Q2. US da Vinci growth slowed to 12%, which management tied to the expiry of enhanced ACA subsidies."),
   metric_src="https://www.sec.gov/Archives/edgar/data/0001035267/000103526726000058/isrg-20260630.htm",
   players=[
    dict(e="intuitive", t="starter",
     stat="468 da Vinci systems placed in Q2 2026, 246 of them da Vinci 5. 2026 da Vinci procedure growth guided to 13.5% to 15.5%. Shares fell about 12% on the guidance.",
     why="An installed base of nearly 12,000 robots that surgeons are trained on.", cond="US procedure growth slowing from 14% to 12%.",
     src="https://www.sec.gov/Archives/edgar/data/0001035267/000103526726000047/q226ex-991earningsrelease.htm"),
   ]),
 ])

EDGES = [
 dict(a="google", b="isomorphic", type="ownership", text="Isomorphic Labs is an Alphabet company. It raised a $2.1bn Series B in May 2026.", src="https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026", date="2026-05", conf="inferred"),
 dict(a="abridge", b="openevidence", type="rivalry", text="Both sell AI to clinicians, one for documentation and one for reference.", src="https://newmarketpitch.com/blogs/news/healthcare-ai-top-startups-valuation", date="2026", conf="inferred"),
 dict(a="abridge", b="ambience", type="rivalry", text="AI scribe competitors.", src="https://newmarketpitch.com/blogs/news/ai-medical-scribe-top-startups-valuation", date="2026", conf="reported"),
 dict(a="isomorphic", b="insilico", type="rivalry", text="AI drug discovery, with Insilico furthest along in the clinic.", src="https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026", date="2026", conf="reported"),
 dict(a="isomorphic", b="xaira", type="rivalry", text="Well-funded AI discovery startups at the preclinical stage.", src="https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026", date="2026", conf="inferred"),
 dict(a="nvidia", b="recursion", type="dependency", text="AI drug discovery depends on large GPU capacity.", src="https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026", date="2026", conf="inferred"),
]
