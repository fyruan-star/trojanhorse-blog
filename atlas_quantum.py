"""Tech Atlas, Phase 2, sector 16: Quantum computing."""

ENT = {
 "ibm": ("IBM", "Quantum hardware roadmap alongside its enterprise business."),
 "quantinuum": ("Quantinuum", "Trapped-ion quantum computers, listed on Nasdaq in June 2026."),
 "ionq": ("IonQ", "Trapped-ion quantum company that has grown by acquisition."),
 "rigetti": ("Rigetti", "Superconducting quantum chips."),
 "dwave": ("D-Wave", "Quantum annealing systems."),
 "iqm": ("IQM", "Finnish quantum hardware company, listed in July 2026."),
 "infleqtion": ("Infleqtion", "Neutral-atom quantum company, listed in February 2026."),
 "psiquantum": ("PsiQuantum", "Photonic quantum startup building large facilities."),
 "honeywell": ("Honeywell", "Industrial company that backs Quantinuum."),
 "skywater": ("SkyWater", "US chip foundry acquired by IonQ."),
}

SECTOR = dict(
 id="quantum", name="Quantum computing", band="foundation",
 blurb="Who is racing to build a fault-tolerant machine, and which listed companies are living on revenue meanwhile.",
 positions=[

  dict(id="hardware", name="The fault-tolerance race",
   metric=("IBM's roadmap lists a 2026 target of circuits of 7,500 gates across up to three 120-qubit Nighthawk modules, and a fault-tolerant machine, Starling, with 200 logical qubits running 100 million gates in 2029. Quantinuum's Helios is a 98-qubit trapped-ion system launched in November 2025. No independent benchmark ranks the leaders."),
   metric_src="https://www.ibm.com/roadmaps/quantum/2026/",
   players=[
    dict(e="ibm", t="starter",
     stat="Roadmap: Nighthawk in 2026 and Starling, 200 logical qubits and 100 million gates, in 2029 (IBM roadmap).",
     why="Publishes dates for each step and the engineering to meet them.", cond="A reported 2026 advantage claim was later reproduced classically in at least one case (third-party tracker).",
     src="https://www.ibm.com/roadmaps/quantum/2026/"),
    dict(e="google", t="starter", conf="reported",
     stat="Willow was the first processor to operate below the error-correction threshold. No 2026 roadmap update was found.",
     why="Showed errors falling as the machine grew.", cond="That result does not yet show fault tolerance at a useful scale.",
     src="https://quantumsecuritydefence.com/quantum-news/quantum-computing-progress-2026-ibm-google/"),
    dict(e="quantinuum", t="second", conf="reported",
     stat="Nasdaq IPO on 4 June 2026 at $60 a share raising about $1.68bn. Valuation reports range from about $13bn to $15bn, with higher figures before pricing. Honeywell is its backer.",
     why="Trapped-ion machines with high accuracy, and the cash to scale.", cond="Valuation sources conflict.",
     src="https://www.cnbc.com/2026/06/04/honeywells-quantinuum-raises-1point68-billion-in-us-ipo-as-quantum-computing-heats-up-reuters-reports.html"),
    dict(e="psiquantum", t="rookie", conf="reported",
     stat="No 2026 valuation or funding was found. Reported to be breaking ground on large compute centers in Chicago and Brisbane in 2026.",
     why="Bets on photonics and building big facilities first.", cond="Funding and status unverified.",
     src="https://thequantuminsider.com/2026/06/04/quantinuum-to-debut-on-nasdaq-after-raising-1-68-billion-in-ipo/"),
   ]),

  dict(id="public", name="Listed quantum companies",
   metric=("Q2 2026 revenue: IonQ $80.05m (up 286.8%, helped by the SkyWater acquisition), Rigetti $5.1m, D-Wave $3.1m. IonQ guides 2026 revenue to $280m to $290m."),
   metric_src="https://www.datacenterdynamics.com/en/news/quantum-earnings-q2-2026-d-wave-ionq-and-rigetti-publish-financial-results-alongside-newly-ipo-ed-iqm-quantum-computers/",
   players=[
    dict(e="ionq", t="starter",
     stat="Q2 2026 revenue $80.05m, up 286.8%. 2026 guide raised to $280m to $290m. A $2bn equity offering followed a $1.3bn Elisity stock deal.",
     why="Grew revenue fast by buying other companies.", cond="Dilution from the equity offering and acquisitions.",
     src="https://finance.yahoo.com/markets/stocks/articles/ionq-falls-6-2b-equity-134408968.html"),
    dict(e="rigetti", t="second",
     stat="Q2 revenue $5.1m against $1.8m a year earlier. About $541m of cash and no debt.", why="Large cash cushion.", cond="Revenue is small.",
     src="https://finance.yahoo.com/markets/stocks/articles/rigetti-d-wave-ionq-quantum-192000732.html"),
    dict(e="dwave", t="second",
     stat="Q2 revenue $3.1m, flat. Bookings $2.1m, up 59%. First-half bookings $35.5m include a $20m system sale.",
     why="Sells annealing systems to customers now.", cond="Revenue depends on a few large sales.",
     src="https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-second-quarter-2026-results/"),
    dict(e="iqm", t="rookie", badge="newly public", conf="reported",
     stat="Reported SPAC merger of about $1.8bn closed on 2 July 2026, trading as IQMX (aggregator sources).",
     why="The first European quantum hardware company on a major US exchange.", cond="Listing details need a filing to confirm.",
     src="https://en.wikipedia.org/wiki/IQM_Quantum_Computers"),
    dict(e="infleqtion", t="rookie", badge="newly public", conf="reported",
     stat="Listed on the NYSE on 17 February 2026 through a SPAC, raising over $550m gross.",
     why="Neutral-atom approach, an alternative to ions and superconducting circuits.", cond="Single source.",
     src="https://thequantuminsider.com/2026/06/04/quantinuum-to-debut-on-nasdaq-after-raising-1-68-billion-in-ipo/"),
   ]),
 ])

EDGES = [
 dict(a="honeywell", b="quantinuum", type="ownership", text="Honeywell is the backer of Quantinuum, which raised $1.68bn in its June 2026 IPO.", src="https://www.cnbc.com/2026/06/04/honeywells-quantinuum-raises-1point68-billion-in-us-ipo-as-quantum-computing-heats-up-reuters-reports.html", date="2026-06", conf="reported"),
 dict(a="ionq", b="skywater", type="ownership", text="IonQ's SkyWater acquisition contributed to its Q2 2026 revenue growth.", src="https://www.datacenterdynamics.com/en/news/quantum-earnings-q2-2026-d-wave-ionq-and-rigetti-publish-financial-results-alongside-newly-ipo-ed-iqm-quantum-computers/", date="2026", conf="reported"),
 dict(a="ibm", b="google", type="rivalry", text="Both are racing to a fault-tolerant machine, IBM with a dated roadmap and Google with the below-threshold result.", src="https://quantumsecuritydefence.com/quantum-news/quantum-computing-progress-2026-ibm-google/", date="2026", conf="reported"),
 dict(a="quantinuum", b="ionq", type="rivalry", text="Both build trapped-ion machines, Quantinuum in the fault-tolerance race and IonQ on revenue.", src="https://www.datacenterdynamics.com/en/news/quantum-earnings-q2-2026-d-wave-ionq-and-rigetti-publish-financial-results-alongside-newly-ipo-ed-iqm-quantum-computers/", date="2026", conf="reported"),
 dict(a="rigetti", b="dwave", type="rivalry", text="Small listed quantum companies at $5.1m and $3.1m of Q2 revenue.", src="https://www.fool.com/investing/2026/09/25/rigetti-d-wave-or-ionq-which-quantum-stock-has-the/", date="2026-Q2", conf="reported"),
 dict(a="psiquantum", b="ibm", type="rivalry", text="Photonic approach against IBM's superconducting one.", src="https://thequantuminsider.com/2026/06/04/quantinuum-to-debut-on-nasdaq-after-raising-1-68-billion-in-ipo/", date="2026", conf="inferred"),
]
