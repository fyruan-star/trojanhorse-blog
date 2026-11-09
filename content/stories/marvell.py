"""Trojan Horse of the Week, week of 9 November 2026: Marvell and Lumentum.

By Ryan Chian, who asked for his name under the title (AUTHOR). Posted from
his own text, which is kept as written.

Its place on the homepage is set by STORIES in content/home.py.

Sources checked on 9 November 2026: the joint press release (Exhibit 99.1 to
Lumentum's 8-K of 2 November 2026), the merger agreement (Exhibit 2.1, fixed
4.50 exchange ratio, adjusted only for splits and stock dividends, no collar),
Lumentum's FY2026 10-K (Customer A 26.6% and 15.4%, Customer B 15.0%), Reuters
via Investing.com, The Star on Microsoft's adoption report, and Gotrade on the
29 October fall. Gotrade's piece on Marvell's custom chip customers now returns
410 Gone, so the link is the Wayback Machine copy of 12 May 2026.

No em dashes, no semicolons.
"""

WEEK = "Week of 9 November 2026"
SLUG = "marvell-lumentum"
KICKER = "Trojan Horse of the Week"
TITLE = "Trading Copper for Light"
AUTHOR = "Ryan Chian"
HOOK = ("Marvell agreed to pay about $115 billion in stock for Lumentum, whose "
        "two biggest customers make up 41.6% of its sales and can already buy "
        "their optics elsewhere.")
MARVELL = {"file": "marvell.svg", "w": 1003.6, "h": 288, "name": "Marvell", "height": 29}
LUMENTUM = {"file": "lumentum.svg", "w": 243, "h": 47, "name": "Lumentum", "height": 16}
LOGO = [MARVELL, LUMENTUM]
GO = ("the-hourglass.html", "The previous Trojan horse: The Hourglass &rarr;")

RELEASE = ("https://www.sec.gov/Archives/edgar/data/0001633978/000119312526442758/"
           "d163169dex991.htm")
TENK = ("https://www.sec.gov/Archives/edgar/data/0001633978/000162828026057358/"
        "lite-20260627.htm")
REUTERS = ("https://www.investing.com/news/stock-market-news/marvell-to-buy-"
           "lumentum-in-115-billion-deal-in-ai-datacenter-bet-4991167")
STAR = ("https://www.thestar.com.my/tech/tech-news/2026/05/08/ai-use-surges-"
        "globally-but-rich-poor-divide-widens-microsoft-says")
CHIPS = ("https://web.archive.org/web/20260512061428/https://www.heygotrade.com/"
         "en/blog/marvell-mrvl-custom-ai-silicon-beyond-nvidia-broadcom/")
DROP = ("https://www.heygotrade.com/en/news/marvell-mrvl-stock-news-october-30-"
        "2026/")

SECTIONS = [

 ("", [
  "Picture a life without ChatGPT: you comb through dozens of research papers "
  "to find one good source for an essay, you write thousands of lines of code "
  "to build a barely functional website, and you rely on imperfect Google "
  "searches for your every answer.",

  "Now, step back into today. AI is shaping our everyday life &ndash; how we "
  "work, shop, learn, and so much more. In the first quarter of 2026, 17.8% of "
  "the world&rsquo;s working-age population used generative AI, including "
  f"31.3% of Americans (<a href=\"{STAR}\">The Star</a>). As the world becomes "
  "more reliant on AI, the physical components behind how AI works are no "
  "longer as sustainable. Thousands of chips talk to each other at once, and "
  "the copper wires connecting them are reaching their physical limits.",

  "On 2 November 2026, Marvell Technology agreed to acquire Lumentum in an "
  "all-stock transaction to become a leader in AI connectivity, a market the "
  f"companies size at $550 billion (<a href=\"{RELEASE}\">Marvell and "
  "Lumentum</a>). Lumentum builds optical circuit switches, lasers and "
  "transceivers that are meant to replace the traditional copper cables inside "
  "these massive data centers. The deal was welcomed because it pairs "
  "Marvell&rsquo;s electrical chips with Lumentum&rsquo;s optics, as copper is "
  "hitting its limits.",
 ]),

 ("End of a Neutral Party", [
  "What came along with the deal was a loss of Lumentum&rsquo;s neutrality. "
  "Before the deal, Lumentum sold optics to everyone: Nvidia, Google, "
  "Microsoft, and more. It made no chips of its own and wasn&rsquo;t competing "
  "with any of them. However, Lumentum&rsquo;s biggest customers are now buying "
  "optics from Marvell, a company that competes indirectly in the chip business "
  f"with some of its customers (<a href=\"{CHIPS}\">Gotrade</a>). Because these "
  "customers were already buying from rivals like Broadcom and Coherent, they "
  "can now move their orders elsewhere and Marvell loses a part of what it paid "
  f"for (<a href=\"{REUTERS}\">Reuters</a>).",

  "It&rsquo;s similar to how Apple originally bought its iPhone screens from "
  "Samsung. However, Apple has spent years adding other screen suppliers so "
  "that it doesn&rsquo;t depend on a competitor. This is exactly what I believe "
  "Lumentum&rsquo;s customers will do.",
 ]),

 ("What Comes With the Deal", [
  "Lumentum&rsquo;s top two customers made up 41.6% of its FY2026 revenue, and "
  "because Lumentum&rsquo;s customers also buy from rival optics suppliers, "
  "it&rsquo;s possible that they shift orders away and Marvell loses some of "
  "the revenue that it paid for. The structure of the deal also adds a second "
  "risk. Marvell agreed to pay a 23.9% premium in an all-stock purchase of "
  "Lumentum. Marvell&rsquo;s shareholders will be diluted from owning 100% of "
  "the company to about 67%, while Lumentum&rsquo;s shareholders are tied to "
  "Marvell&rsquo;s stock through the 4.5 exchange ratio "
  f"(<a href=\"{RELEASE}\">Marvell and Lumentum</a>). Marvell&rsquo;s stock "
  "fell about 13% on 29 October, the day talks were first reported "
  f"(<a href=\"{DROP}\">Gotrade</a>).",

  "Furthermore, because the exchange ratio is fixed, Lumentum&rsquo;s "
  "shareholders are exposed to Marvell&rsquo;s stock. If customers start "
  "looking elsewhere for optics and Marvell&rsquo;s stock continues to go down, "
  "Lumentum&rsquo;s shareholders feel these effects before the deal even "
  "closes.",
 ]),

 ("What Makes It Worth It?", [
  "Even though the deal was a strategic fit for Marvell, it&rsquo;s dilutive "
  "to Marvell&rsquo;s shareholders. An important factor to consider is how the "
  "deal could play out in the long term.",

  "The questions that need to be answered are 1) does Marvell deliver the $1B+ "
  f"a year in cost synergies (<a href=\"{RELEASE}\">Marvell and Lumentum</a>)? "
  "2) does the optics market continue to grow? 3) do Lumentum&rsquo;s "
  "customers stay? For example, if Lumentum&rsquo;s products are hard to "
  "replace, or demand greatly exceeds supply, customers can&rsquo;t afford to "
  "switch suppliers.",

  "Furthermore, Lumentum&rsquo;s largest customer went from 15.4% to 26.6% of "
  f"revenue in one year (<a href=\"{TENK}\">Lumentum 10-K</a>), as the AI "
  "optics market was booming. Purchasing Lumentum in a bull market could mean "
  "that Marvell paid too much of a premium (~$20B). In addition, in all-stock "
  "deals, relative prices matter more than absolute ones.",

  "It&rsquo;s important to consider what Marvell&rsquo;s stock is worth "
  "compared with Lumentum&rsquo;s as of the signing. If Marvell&rsquo;s stock "
  "was high, then it means that they gave up less in the acquisition.",

  "My bet is that as the demand for AI infrastructure grows, this deal could "
  "justify its roughly $20 billion premium in the long run, but only if "
  "Lumentum&rsquo;s customers keep buying from a supplier now owned by a "
  "company tied to their competitors.",
 ]),
]

NOTE = ("The deal terms, the premium, the exchange ratio, the ownership split, "
        "the synergy target and the $550 billion market come from the "
        "companies&rsquo; joint announcement. The customer figures come from "
        "Lumentum&rsquo;s annual report for fiscal 2026, which does not name "
        "the customers. Marvell&rsquo;s fall on 29 October comes from "
        "Gotrade&rsquo;s market report. The argument about Lumentum&rsquo;s "
        "neutrality is mine.")
