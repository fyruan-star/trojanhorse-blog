#!/usr/bin/env python3
"""Emit the index, the stories page and the podcast page.

The site shows one story. Everything previously published lives in archive/,
which is git-ignored, so it stays on disk and never reaches the web. To bring
a piece back: move its html out of archive/, add it to STORY below, rebuild.
"""
import pathlib, sys
import sketch
from weekly_data import (WEEK as W_WEEK, SLUG as W_SLUG, KICKER as W_KICKER,
                         TITLE as W_TITLE, DEK as W_DEK, LEDE as W_LEDE,
                         SECTIONS as W_SECTIONS, NOTE as W_NOTE)

ROOT = pathlib.Path(__file__).parent

# The one story the site shows. Everything else lives in archive/, which is
# git-ignored and never deployed.
STORY = {
 "the-buyers-bank": ("The Buyer&rsquo;s Bank", "BofA Securities", "Technology Coverage M&amp;A"),
}

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&display=swap" rel="stylesheet">
<link rel="icon" href="/favicon.ico?v=2" sizes="any">
<link rel="icon" type="image/png" href="/favicon.png?v=2">
<link rel="apple-touch-icon" href="/apple-touch-icon.png?v=2">
<link rel="stylesheet" href="site.css">
</head>
<body>
"""

# the column capital, drawn once and referenced by every silo card
CAPITAL_DEF = """
<svg width="0" height="0" aria-hidden="true" focusable="false" style="position:absolute">
  <defs>
    <symbol id="capital" viewBox="0 0 100 124">
      <g fill="currentColor">
        <path d="M13 5h74v4.6H13z"/><path d="M16.5 9.6h67v5.2h-67z" opacity=".92"/>
        <path d="M50 17c-6 5-8.4 13-6.2 21.4 3-3.6 4.2-7.6 6.2-10.8 2 3.2 3.2 7.2 6.2 10.8C58.4 30 56 22 50 17Z"/>
        <path d="M34.5 20.5c-4.2 5.8-4.4 13.6-1.4 19.6 3-4.8 3.2-11.4 5-15.4Z" opacity=".88"/>
        <path d="M65.5 20.5c4.2 5.8 4.4 13.6 1.4 19.6-3-4.8-3.2-11.4-5-15.4Z" opacity=".88"/>
        <path d="M25 41.5h50v4.4H25z"/><path d="M28.5 45.9h43v3.2h-43z" opacity=".92"/>
      </g>
      <g fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round">
        <path d="M21 16.5c-8 4-8 14 0 17 6 2.2 10-2 8-6.2-1.8-3.2-6-2.2-6 .8"/>
        <path d="M79 16.5c8 4 8 14 0 17-6 2.2-10-2-8-6.2 1.8-3.2 6-2.2 6 .8"/>
      </g>
      <!-- flutes: bars with the card showing through as the grooves -->
      <g fill="currentColor" opacity=".96">
        <rect x="31.5" y="50" width="4.4" height="68" rx="1"/>
        <rect x="38.2" y="50" width="4.4" height="68" rx="1"/>
        <rect x="44.9" y="50" width="4.4" height="68" rx="1"/>
        <rect x="51.6" y="50" width="4.4" height="68" rx="1"/>
        <rect x="58.3" y="50" width="4.4" height="68" rx="1"/>
        <rect x="65" y="50" width="4.4" height="68" rx="1"/>
      </g>
    </symbol>
  </defs>
</svg>
"""

VINE_DEF = """
<!-- vine artwork, defined once and referenced in every gap -->
<svg width="0" height="0" aria-hidden="true" focusable="false" style="position:absolute">
  <defs>
    <linearGradient id="vstem" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3E7A63"/><stop offset=".55" stop-color="#2A5644"/><stop offset="1" stop-color="#1D3E33"/>
    </linearGradient>
    <linearGradient id="vleaf" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#3B7460"/><stop offset=".6" stop-color="#27513F"/><stop offset="1" stop-color="#1A3A30"/>
    </linearGradient>
    <symbol id="vine-seg" viewBox="0 0 240 220">
      <g stroke="url(#vstem)" fill="none" stroke-linecap="round">
        <path d="M120 0 C120 44 64 56 58 98 C52 140 114 152 120 220" stroke-width="4.4"/>
        <path d="M58 98 C38 90 27 105 38 116 C47 125 61 116 54 107" stroke-width="2.6" opacity=".9"/>
        <path d="M86 62 C74 52 62 54 56 44" stroke-width="2" opacity=".75"/>
        <path d="M92 168 C104 162 114 166 122 158" stroke-width="2" opacity=".75"/>
      </g>
      <g fill="url(#vleaf)">
        <path d="M0 0 C11 -15 33 -19 46 -7 C34 9 11 13 0 0 Z" transform="translate(98 44) rotate(-38) scale(.88)"/>
        <path d="M0 0 C11 -15 33 -19 46 -7 C34 9 11 13 0 0 Z" transform="translate(70 78) rotate(148) scale(.96)"/>
        <path d="M0 0 C11 -15 33 -19 46 -7 C34 9 11 13 0 0 Z" transform="translate(56 116) rotate(-162) scale(.8)"/>
        <path d="M0 0 C11 -15 33 -19 46 -7 C34 9 11 13 0 0 Z" transform="translate(80 152) rotate(26) scale(.92)"/>
        <path d="M0 0 C11 -15 33 -19 46 -7 C34 9 11 13 0 0 Z" transform="translate(114 192) rotate(163) scale(.68)"/>
        <path d="M0 0 C11 -15 33 -19 46 -7 C34 9 11 13 0 0 Z" transform="translate(56 44) rotate(-108) scale(.6)"/>
      </g>
      <g stroke="#4E8E76" stroke-width="1.1" fill="none" opacity=".5">
        <path d="M98 44 L124 22"/><path d="M70 78 L44 96"/><path d="M80 152 L106 140"/>
      </g>
    </symbol>
  </defs>
</svg>
"""

COVER = """
<!-- ============================================================= COVER === -->
<header class="cover">
  <div class="shell"><div class="cover__rule"></div></div>

  <div class="shell cover__top">
    <p class="cover__wordmark">The Trojan Horse</p>
  </div>

  <div class="shell cover__stage">
    <img class="cover__horse" src="images/horse-light.png"
         alt="A rearing horse drawn in silver line work, its hindquarters breaking apart into fragments">
    <p class="cover__tag">Mergers &amp; Acquisitions<span class="cover__tag__sub">Technology Deals and the Incentives Behind Them</span></p>
  </div>

  <div class="cover__mist" aria-hidden="true"></div>

  <div class="shell cover__foot">
    <div class="cover__rule"></div>
    <a class="cover__scroll" href="#opening">Scroll</a>
  </div>
</header>

"""

ESSAY = """
<!-- ============================================================== TALE === -->
<section class="essay" id="opening">
  <div class="shell">

    <div class="tale">
      <p class="tale__open"><span class="tale__cap">P</span>icture the morning the Trojans woke up to an empty beach. Ten years of tents and smoke and shouting had vanished overnight. The black ships were gone, and where the Greek camp had stood there was trampled sand and one enormous horse of fresh-cut pine. I love this part of the story. The whole city poured out through the gates to look at it.</p>
    </div>

    <figure class="sk sk--dark">{COAST}</figure>

    <div class="tale">
      <p>Children ran up and slapped the wood. Somebody&rsquo;s grandmother, who had spent a decade sleeping in her clothes, stood in the sun and cried because the war looked finished. A priest named Laocoön had his doubts. He said he feared the Greeks even when they came bearing gifts, and he hurled a spear into the horse&rsquo;s side. It stuck there, quivering, and from deep inside the wood came a low hollow groan. Then a Greek named Sinon, who had let himself be captured on purpose, wept and swore the horse was an offering to Athena that would protect the city if it stood inside. The Trojans believed him. The horse was too big for the gate, so they tore down a stretch of their own wall to bring it in, and that night the soldiers climbed out of its belly and opened the city from within.</p>

      <p>What delights me is how well that plan understood its audience. The Greeks had given up on the walls and started studying the people behind them. Ten years of siege taught them what Troy wanted most, which was for the war to be over, and they built that wish out of timber and left it where it would be found. The Trojans felt rewarded, and a person who feels rewarded stops inspecting the gift.</p>

      <p>Mergers and acquisitions run on the same instincts. At the end of the day a company acquires something in order to win, whether that is a customer base, a technology or a position its rival cannot reach, and the people across the table are studying what you want just as closely. So every deal is a horse standing at somebody&rsquo;s gate, and the useful thing to do is walk up to it and ask what it is carrying. A bank welcomes a private credit partner because the partner brings capital to its clients, and the partner gets to know those clients. A bank hands its junior analysts an AI assistant that finishes in minutes the hands-on work they used to do late at night, and that work is where they learned to judge a business. A chipmaker prepays a supplier two billion dollars to guarantee its wafers, the supplier runs into trouble, and the chipmaker ends up holding a large share of the supplier&rsquo;s stock. Each of those was welcomed for a good reason by sensible people.</p>

      <p>The thinking behind those moves is what I want to write about. I want to know why a seller turns down $23 billion and accepts $32 billion eight months later, and why a buyer pays cash when cash is expensive. I want to know what each side believes about the other, what it is afraid of, and who holds the leverage at the moment an offer crosses the table. An announcement is the last line of a long conversation, and I like to go back and hear the whole thing.</p>

      <p>Any curious person can follow these stories. All it takes is the willingness to walk up to a very large gift and find out who built it. I will tell the deals one at a time, with the strategy as it unfolded and the sources beside every claim. Welcome to The Trojan Horse.</p>
      <p class="tale__sign">Francis Ruan</p>
    </div>

  </div>
</section>
"""

# Episodes are questions, not deal recaps: the thing worth an hour is the
# mechanism underneath, not the transaction on top.
EPISODES = [
 ("Why Models Fail",
  "A discounted cash flow depends on forecast growth and a discount rate, and both are assumptions. This episode examines where valuation models break when applied to a real business, and what a forecast claims when it assumes that growth costs nothing.",
  "Recording October"),
 ("Sleep As Capital",
  "Junior bankers regularly work through the night. This episode examines what research on sleep deprivation shows about judgment, and whether a team that relies on long hours is gaining output or borrowing against later performance.",
  "In production"),
 ("The Adjusted Truth",
  "Adjusted EBITDA excludes items that management classifies as unusual. This episode examines who sets that definition, how it varies between companies and how it changes the multiple a buyer pays.",
  "In production"),
 ("Managing The Number",
  "Companies shape reported earnings through legal choices about timing and classification. This episode examines how those choices are used to meet consensus estimates and what they imply about the quarters that are not reported.",
  "In production"),
 ("Who Picks Comparables",
  "A valuation based on comparable companies depends on which companies are chosen. This episode examines how different peer sets change the answer, and why the selection is rarely shown.",
  "In production"),
 ("Writers Make Bankers",
  "Much of an analyst's work is persuasive writing about a business. This episode examines what separates strong writing from weak writing in banking and how analysts learn it.",
  "Recording October"),
 ("The Confidence Trap",
  "Two valuation methods that agree can seem to confirm each other. This episode examines how one assumption can enter both, which makes the agreement weaker evidence than it appears.",
  "In production"),
 ("Disconnected",
  "An experiment in building a complex model with the internet switched off, to test how much a person can recall without searching.",
  "In production"),
]
ROMAN_EP = ["I","II","III","IV","V","VI","VII","VIII"]

def episode_rows():
    rows = []
    for i,(title, q, status) in enumerate(EPISODES):
        slug = title.lower().replace(" ","-")
        rows.append(f'''      <li class="ep">
        <span class="ep__no">No. {ROMAN_EP[i]}</span>
        <div class="ep__body">
          <h3 class="ep__title">{title}</h3>
          <p class="ep__q">{q}</p>
          <!-- DROP MP3 HERE: replace this comment with
               <audio class="ep__audio" controls preload="none" src="audio/{i+1:02d}-{slug}.mp3"></audio> -->
        </div>
        <span class="ep__status">{status}</span>
      </li>''')
    return "\n".join(rows)


def build_podcast():
    html = (HEAD.format(title="In The Belly | The Trojan Horse",
                        desc="The Trojan Horse podcast. Conversations on the mechanisms underneath M&amp;A.")
            + '''
<a class="back" href="index.html">&larr; The Trojan Horse</a>

<header class="silohead">
  <div class="shell">
    <p class="silohead__kicker">The Podcast</p>
    <h1 class="silohead__name">In The Belly</h1>
    <p class="silohead__blurb">Conversations on the mechanisms underneath M&amp;A. Guests are being booked now, and episodes appear here as they are cut.</p>
    <div class="silohead__line" aria-hidden="true"></div>
  </div>
</header>

<main class="pod pod--page">
  <div class="shell">
    <ol class="pod__list">
''' + episode_rows() + '''
    </ol>
  </div>
</main>
''' + FOOT)
    (ROOT / "podcast.html").write_text(html, encoding="utf-8")
    print("podcast.html")


# The podcast is the last thing on the page and says nothing. The mark is the
# whole invitation; it opens the page of episodes that are still being cut.
ROOMS = """
<!-- =========================================================== PODCAST === -->
<section class="spot">
  <a class="spot__link" href="podcast.html" aria-label="In The Belly, the Trojan Horse podcast">
    <svg class="spot__mark" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      <path fill="currentColor" d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/>
    </svg>
  </a>
</section>
"""

FOOT = """
<footer class="foot">
  <div class="shell foot__in">
    <span>&copy; 2026 The Trojan Horse</span>
    <span>Francis Ruan &middot; Los Angeles</span>
  </div>
</footer>

</body>
</html>
"""

def belt(slugs):
    """The vine-threaded column of books for one silo."""
    out = ['    <div class="belt__track">\n']
    for i, slug in enumerate(slugs):
        title, party, sector = STORY[slug]
        out.append(f'''      <a class="story" href="{slug}.html">
        <article class="book">
          <div class="book__pages" aria-hidden="true"></div>
          <div class="book__face">
            <h2 class="book__title">{title}</h2>
            <p class="book__author">{party}</p>
            <div class="book__helmet"><img src="images/helmet.png" alt=""></div>
            <p class="book__sector">{sector}</p>
            <p class="book__press">The Trojan Horse</p>
          </div>
        </article>
      </a>
''')
        if i < len(slugs) - 1:
            flip = "" if i % 2 == 0 else " vine--flip"
            out.append(f'''      <div class="vine{flip}" aria-hidden="true">
        <svg viewBox="0 0 240 220"><use href="#vine-seg"/></svg>
      </div>
''')
    out.append('''      <div class="vine vine--tail" aria-hidden="true">
        <svg viewBox="0 0 240 220"><use href="#vine-seg"/></svg>
      </div>
''')
    out.append('    </div>')
    return "".join(out)


def build_index():
    # The doors come after the writing now. A reader who has finished the Troy
    # passage is in a position to choose; a reader who has just arrived is not.
    doors = [
        ("Ten Years",     "2016 to 2026",              "ten-years.html"),
        ("Atlas",         "A depth chart of technology", "tech-atlas.html"),
        ("Trojan Horses", "P&amp;G and Thorne",          "trojan-horses.html"),
    ]
    cards = "".join(
        f'''<a class="idx__c" href="{href}">
        <span class="idx__n">{i:02d}</span>
        <span class="idx__t">{name}</span>
        <span class="idx__d">{desc}</span>
      </a>'''
        for i, (name, desc, href) in enumerate(doors, 1))

    weekly = f'''
<!-- ============================================================ HORSE OF THE WEEK === -->
<section class="wk">
  <a class="wk__in" href="{W_SLUG}.html">
    <p class="wk__k">{W_KICKER}<span>{W_WEEK}</span></p>
    <span class="wk__t">{W_TITLE}</span>
    <span class="wk__s">{W_DEK}</span>
    <span class="wk__go">Read it &rarr;</span>
  </a>
</section>
'''

    index = weekly + f'''
<!-- ============================================================= INDEX === -->
<nav class="idx" aria-label="The journal">
  <div class="shell">
    <p class="idx__k">The Journal</p>
    <div class="idx__row">{cards}</div>
  </div>
</nav>
'''

    html = (HEAD.format(title="The Trojan Horse",
                        desc="A mergers and acquisitions journal and podcast by Francis Ruan.")
            + CAPITAL_DEF + COVER + ESSAY.replace("{COAST}", sketch.coast())
            + index + ROOMS + FOOT)
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print("index.html")


def build_weekly():
    body = []
    for head, paras in W_SECTIONS:
        inner = "\n".join(f'        <p class="wp__p">{x}</p>' for x in paras)
        body.append(f'''      <section class="ch">
        <h2 class="ch__h">{head}</h2>
{inner}
      </section>''')
    html = (HEAD.format(title=f"{W_TITLE} | The Trojan Horse",
                        desc="P&G is paying $3.8 billion for Thorne, a brand "
                             "whose value is customer trust, and the customers "
                             "were not part of the deal.")
            + f'''
<a class="back back--dark" href="index.html">&larr; The Trojan Horse</a>

<header class="plate">
  <div class="shell plate__in">
    <p class="plate__k">{W_KICKER}<span class="plate__wk">{W_WEEK}</span></p>
    <h1 class="plate__t">{W_TITLE}</h1>
    <p class="plate__l">{W_LEDE}</p>
  </div>
</header>

<main class="white">
  <div class="shell">
    <article class="wp">
{chr(10).join(body)}

      <p class="wp__note">{W_NOTE}</p>

      <a class="wp__go" href="trojan-horses.html">The prices and dates behind this deal &rarr;</a>
    </article>
  </div>
</main>
''' + FOOT)
    (ROOT / f"{W_SLUG}.html").write_text(html, encoding="utf-8")
    print(f"{W_SLUG}.html  ({len(W_SECTIONS)} sections)")


from mandate_data import (KICKER as M_KICKER, TITLE as M_TITLE, LEDE as M_LEDE,
                          SECTIONS as M_SECTIONS, SOURCES as M_SOURCES,
                          TAKEAWAY as M_TAKEAWAY)

def build_stories_page():
    """The Mandate was merged into the sale page, where it is Part One. The old
    URL still exists so links to it keep working."""
    (ROOT / "strategemata.html").write_text(
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<title>How a Company Gets Sold | The Trojan Horse</title>'
        '<link rel="canonical" href="https://trojanhorse.blog/how-a-company-gets-sold.html">'
        '<meta http-equiv="refresh" content="0; url=how-a-company-gets-sold.html">'
        '</head><body><p><a href="how-a-company-gets-sold.html">How a Company Gets Sold</a></p>'
        '</body></html>\n', encoding="utf-8")
    print("strategemata.html  (redirect into the merged page)")


# ====================================================== THE GROUND FLOOR ===
from primers_data import PRIMERS
from deals_data import DEALS
from kata_data import YEARS, INTRO, INTRO_2, CLOSE_HEAD, CLOSE

DEAL_LINKS = {
 "SoftBank / Arm":      "the-blueprint",
 "Broadcom / Qualcomm": "the-blocked-bid",
 "IBM / Red Hat":       "the-layer-above",
 "Nvidia / Mellanox":   "the-wiring",
 "AMD / Xilinx":        "paid-in-paper",
 "Nvidia / Arm":        "too-central",
 "Broadcom / VMware":   "the-price-machine",
 "Cisco / Splunk":      "reading-the-record",
 "Google / Wiz":        "third-in-line",
 "DDN / Blackstone":    "fetching",
}

# background reading, offered where the subject first comes up
PRIMER_AT = {
 "SoftBank / Arm":                          ("what-a-chip-is",    "what a chip is"),
 "IBM / Red Hat":                           ("what-the-cloud-is", "what the cloud is"),
 "A change in what customers were asking for": ("what-ai-needs",  "what training a model requires"),
 "Spending moves toward buildings and power":  ("the-building",   "what is inside a data centre"),
 "How the construction was financed":          ("what-a-bank-does","what an investment bank does"),
}

SHEET = """<a class="back" href="{back}">&larr; {backlabel}</a>

<article class="sheet sheet--long">

  <h1 class="tt">
    {lead}<span class="tt__big">{line1}</span>
    {row2}
  </h1>

  <p class="sub">{sub}</p>

  <p class="byline">Francis Ruan</p>

  <div class="opening"><p class="lede">{lede}</p></div>

  <div class="body">
{sections}
  </div>

  {takeaway_html}<figure class="mark"><img src="images/horse.png" alt="The Trojan Horse engraving"></figure>

{tail}

  <footer class="colophon">
    <p class="colophon__loc">At Los Angeles</p>
    <p>Published by <em>The Trojan Horse</em></p>
    <p>{series} &middot; {roman}</p>
    <p class="colophon__last">{last}</p>
  </footer>

</article>
"""

def _title(lead, line1, line2):
    ld = f'<span class="tt__lead">{lead}</span>' if lead else ""
    row = (f'<span class="tt__row"><span class="tt__big">{line2}</span></span>'
           if line2 else "")
    return ld, row

def _sections(sections):
    out = []
    for head, paras in sections:
        out.append(f'    <h2 class="h2">{head}</h2>')
        out.extend(f"    <p>{x}</p>" for x in paras)
    return "\n".join(out)


def build_primers():
    for pr in PRIMERS:
        ld, row = _title(pr["lead"], pr["line1"], pr["line2"])
        words = "".join(
          f'<li><span class="w__t">{t}</span><span class="w__d">{d}</span></li>'
          for t, d in pr["words"])
        tail = ('  <div class="words">\n    <h3>Words you now own</h3>\n'
                f'    <ul>{words}</ul>\n  </div>')
        html = (HEAD.format(title=f'{pr["lead"]} {pr["line1"]} {pr["line2"]} | The Trojan Horse'.replace("  "," ").strip(),
                            desc=pr["lede"][:180])
                + '\n<link rel="stylesheet" href="story.css">\n'
                + SHEET.format(back="ten-years.html", backlabel="Ten Years",
                               lead=ld, line1=pr["line1"], row2=row, sub=pr["sub"],
                               lede=pr["lede"], sections=_sections(pr["sections"]),
                               takeaway_html=(f'<p class="takeaway">{pr["takeaway"]}</p>\n\n  ' if pr.get("takeaway") else ''), tail=tail,
                               series="Background", roman=f'No. {pr["roman"]}',
                               last="Ten Years in Technology")
                + "\n</body>\n</html>\n")
        (ROOT / f'{pr["slug"]}.html').write_text(html, encoding="utf-8")
    print(f"{len(PRIMERS)} background pages")


def build_deals():
    for d in DEALS:
        ld, row = _title(d["lead"], d["line1"], d["line2"])
        srcs = "\n".join(f"      <li>{x}</li>" for x in d["srcs"])
        tail = ('  <div class="srcs">\n    <h3>Sources</h3>\n    <ol>\n'
                + srcs + '\n    </ol>\n  </div>')
        html = (HEAD.format(title=f'{d["lead"]} {d["line1"]} {d["line2"]} | The Trojan Horse'.replace("  "," ").strip(),
                            desc=f'{d["party"]} &middot; {d["value"]} &middot; {d["dated"]}.')
                + '\n<link rel="stylesheet" href="story.css">\n'
                + SHEET.format(back="ten-years.html", backlabel="Ten Years",
                               lead=ld, line1=d["line1"], row2=row, sub=d["sub"],
                               lede=d["lede"], sections=_sections(d["sections"]),
                               takeaway_html=(f'<p class="takeaway">{d["takeaway"]}</p>\n\n  ' if d.get("takeaway") else ''), tail=tail,
                               series="Ten Years", roman=f'No. {d["roman"]}',
                               last=f'{d["party"]} &middot; {d["value"]}')
                + "\n</body>\n</html>\n")
        (ROOT / f'{d["slug"]}.html').write_text(html, encoding="utf-8")
    print(f"{len(DEALS)} deal notes")


from desk_data import DESK, DESK_INTRO

def build_desk():
    """Three stories from the Palo Alto software team's list, one page each."""
    for d in DESK:
        ld, row = _title(d["lead"], d["line1"], d["line2"])
        srcs = "\n".join(f"      <li>{x}</li>" for x in d["srcs"])
        tail = ('  <div class="srcs">\n    <h3>Sources</h3>\n    <ol>\n'
                + srcs + '\n    </ol>\n  </div>')
        html = (HEAD.format(title=f'{d["lead"]} {d["line1"]} {d["line2"]} | The Trojan Horse'.replace("  "," ").strip(),
                            desc=f'{d["party"]} &middot; {d["value"]} &middot; {d["dated"]}.')
                + '\n<link rel="stylesheet" href="story.css">\n'
                + SHEET.format(back="palo-alto.html", backlabel="Deals From Palo Alto",
                               lead=ld, line1=d["line1"], row2=row, sub=d["sub"],
                               lede=d["lede"], sections=_sections(d["sections"]),
                               takeaway_html=(f'<p class="takeaway">{d["takeaway"]}</p>\n\n  ' if d.get("takeaway") else ''), tail=tail,
                               series="Deals From Palo Alto", roman=f'No. {d["roman"]}',
                               last=f'{d["party"]} &middot; {d["value"]}')
                + "\n</body>\n</html>\n")
        (ROOT / f'{d["slug"]}.html').write_text(html, encoding="utf-8")
    print(f"{len(DESK)} Palo Alto stories")


def build_desk_index():
    rows = []
    for d in DESK:
        name = f'{d["lead"]} {d["line1"]} {d["line2"]}'.replace("  ", " ").strip()
        rows.append(f'      <li><a href="{d["slug"]}.html">'
                    f'<span class="g__n">No. {d["roman"]}</span>'
                    f'<span class="g__t">{name}</span></a></li>')
    html = (HEAD.format(title="Deals From Palo Alto | The Trojan Horse",
                        desc="Technology transactions from the BofA Securities Palo Alto software team, told as stories.")
            + '''
<a class="back" href="ten-years.html">&larr; Ten Years</a>

<header class="silohead">
  <div class="shell">
    <p class="silohead__kicker">A sub journal to Ten Years</p>
    <h1 class="silohead__name">Deals From Palo Alto</h1>
    <p class="silohead__blurb">''' + DESK_INTRO + '''</p>
    <div class="silohead__line" aria-hidden="true"></div>
  </div>
</header>

<section class="ground">
  <div class="shell">
    <ol class="ground__l">
''' + "\n".join(rows) + '''
    </ol>
  </div>
</section>
''' + FOOT)
    (ROOT / "palo-alto.html").write_text(html, encoding="utf-8")
    print("palo-alto.html")


DESK_DOOR = """
<section class="ground">
  <div class="shell">
    <p class="ground__k">Sub journal</p>
    <p class="ground__n">Three transactions from the BofA Securities Palo Alto
    software team's list, each examined as a case. <a href="palo-alto.html">Deals
    From Palo Alto &rarr;</a></p>
    <p class="ground__n">A depth chart of nine technology sectors, with who is allied,
    competing and backed by whom. <a href="tech-atlas.html">The Tech Atlas &rarr;</a></p>
  </div>
</section>
"""


from buyers_data import SUB as B_SUB, LEDE as B_LEDE, SECTIONS as B_SECTIONS, SRCS as B_SRCS

def build_buyers():
    """The Buyer's Bank, generated from buyers_data like every other piece."""
    ld, row = _title("The", "Buyer&rsquo;s", "Bank")
    srcs = "\n".join(f"      <li>{x}</li>" for x in B_SRCS)
    tail = ('  <div class="srcs">\n    <h3>Sources and method</h3>\n    <ol>\n'
            + srcs + '\n    </ol>\n  </div>')
    html = (HEAD.format(title="The Buyer&rsquo;s Bank | The Trojan Horse",
                        desc="BofA Securities' technology record across 2025 and 2026 is built on acquirers and not on founders, and why that matters.")
            + '\n<link rel="stylesheet" href="story.css">\n'
            + SHEET.format(back="how-a-company-gets-sold.html", backlabel="How a Company Gets Sold",
                           lead=ld, line1="Buyer&rsquo;s", row2=row, sub=B_SUB,
                           lede=B_LEDE, sections=_sections(B_SECTIONS),
                           takeaway_html="", tail=tail,
                           series="The Mandate", roman="September 2026",
                           last="On coverage &middot; BofA Securities, 2025 to 2026")
            + "\n</body>\n</html>\n")
    (ROOT / "the-buyers-bank.html").write_text(html, encoding="utf-8")
    print("the-buyers-bank.html")


# ================================================================ TECH ATLAS ===
import json as _json
from urllib.parse import urlparse as _urlparse
import atlas_data as AD
from atlas_essays import INTRO as AT_INTRO, SECTOR_PIECES as AT_PIECES
from atlas_log import METHOD as AT_METHOD, GAPS as AT_GAPS, NOT_YET as AT_NOT_YET

def _host(u):
    h = _urlparse(u).netloc.replace("www.", "")
    return h or "source"

def _esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

def build_atlas():
    names = {k: v[0] for k, v in AD.ENT.items()}
    sec_name = {s["id"]: s["name"] for s in AD.SECTORS}
    # first card id for each company, so connections can link to it
    card_id = {}
    for s in AD.SECTORS:
        for p in s["positions"]:
            for pl in p["players"]:
                card_id.setdefault(pl["e"], f'c-{s["id"]}-{p["id"]}-{pl["e"]}')

    by_ent = {}
    for ed in AD.EDGES:
        by_ent.setdefault(ed["a"], []).append(ed)
        by_ent.setdefault(ed["b"], []).append(ed)

    VERB = {"ownership": ("owns", "owned by"), "investment": ("funds", "funded by")}

    def conn_html(ent):
        """Relationships in three groups: allies, rivals, owners and backers."""
        groups = {"allies": [], "rivals": [], "backers": []}
        for ed in by_ent.get(ent, []):
            other = ed["b"] if ed["a"] == ent else ed["a"]
            g = AD.GROUP[ed["type"]]
            if other in card_id:
                who = f'<a href="#{card_id[other]}" data-go="{other}">{_esc(names[other])}</a>'
            else:
                who = _esc(names.get(other, other))
            verb = ""
            if g == "backers":
                v = VERB[ed["type"]]
                verb = f'<span class="conn__v">{v[0] if ed["a"] == ent else v[1]}</span> '
            where = ""
            oh = AD.HOME.get(other)
            if oh and oh not in {x[0] for x in AD.APPEARS.get(ent, [])}:
                where = f' <span class="conn__s">in {_esc(sec_name[oh])}</span>'
            groups[g].append(
                f'<li data-g="{g}">{verb}{who}{where}<br><span class="conn__x">{_esc(ed["text"])} '
                f'<a href="{ed["src"]}">{_host(ed["src"])}</a></span></li>')
        out = []
        for g in ("allies", "rivals", "backers"):
            if groups[g]:
                out.append(f'<div class="rel rel--{g}" data-g="{g}"><p class="rel__h">{AD.GROUP_LABEL[g]}</p><ul>{"".join(groups[g])}</ul></div>')
        return "".join(out)

    def card_html(s, p, pl):
        e = pl["e"]
        cid = f'c-{s["id"]}-{p["id"]}-{e}'
        t = pl["t"]
        conf = pl.get("conf", "sourced")
        badge = pl.get("badge") or {"starter": "leading", "second": "rising", "rookie": "rookie"}[t]
        bcls = {"leading": "badge--leading", "rising": "badge--rising", "changes the premise": "badge--premise"}.get(badge, "")
        also = sorted({sec_name[x[0]] for x in AD.APPEARS.get(e, []) if x[0] != s["id"]})
        also_html = f'<p class="also">Also in {_esc(", ".join(also))}</p>' if also else ""
        label = {"starter": "Why it leads", "second": "Why it may rise", "rookie": "Why it matters"}[t]
        conns = conn_html(e)
        return f"""<details class="card card--{t}" id="{cid}" data-e="{e}" data-conf="{conf}">
  <summary>
    <div class="card__top"><span class="card__name">{_esc(names[e])}</span><span class="badge {bcls}">{_esc(badge)}</span></div>
    <div class="card__stat">{_esc(pl["stat"])}</div>
  </summary>
  <div class="card__more">
    <p>{_esc(AD.ENT[e][1])}</p>
    <p><b>{label}</b>{_esc(pl["why"])}</p>
    <p><b>What could change it</b>{_esc(pl["cond"])}</p>
    <p class="card__src"><span class="conf conf--{conf}">{conf}</span> <a href="{pl["src"]}">{_host(pl["src"])}</a></p>
    {also_html}
    {conns}
  </div>
</details>"""

    def position_html(s, p):
        cols = {"starter": [], "second": [], "rookie": []}
        for pl in p["players"]:
            cols[pl["t"]].append(card_html(s, p, pl))
        tiers = []
        for t in ("starter", "second", "rookie"):
            inner = "\n".join(cols[t]) if cols[t] else ""
            tiers.append(f'<div class="tier{"" if cols[t] else " tier--empty"}" data-tier="{AD.TIER_LABEL[t]}">{inner}</div>')
        return f"""<div class="pos">
  <div class="pos__h"><h3 class="pos__n">{_esc(p["name"])}</h3></div>
  {"".join(tiers)}
</div>"""

    sectors_html = []
    for s in AD.SECTORS:
        pos = "\n".join(position_html(s, p) for p in s["positions"])
        note = "\n".join(f"<p>{x}</p>" for x in AT_PIECES[s["id"]])
        sectors_html.append(f"""<section class="sector" id="sector-{s["id"]}" data-sector="{s["id"]}">
  <h2 class="sector__h">{_esc(s["name"])}</h2>
  <p class="sector__b">{_esc(s["blurb"])}</p>
  <div class="board">
    <svg class="lines" aria-hidden="true"></svg>
    <div class="cols"><span></span><span>Starters</span><span>Second string</span><span>Practice squad</span></div>
    {pos}
  </div>
  <details class="note"><summary>The story of this sector</summary>{note}</details>
</section>""")

    # overview tiles, grouped by band
    order = {"end": ["internet", "devices", "fintech"],
             "platform": ["models", "software", "security"],
             "stack": ["silicon", "infra", "cloud"]}
    sec = {s["id"]: s for s in AD.SECTORS}
    def tile(sid):
        s = sec[sid]
        return f"""<a class="tile" id="t-{sid}" href="#sector-{sid}" data-sector="{sid}">
  <span class="tile__n">{_esc(s["name"])}</span><span class="tile__b">{_esc(s["blurb"])}</span>
</a>"""
    bands = []
    for band in ("end", "platform", "stack"):
        bands.append(f'<div class="band"><p class="band__label">{AD.BAND_LABEL[band]}</p><div class="band__row">' +
                     "".join(tile(x) for x in order[band]) + "</div></div>")

    chips = "".join(f'<button class="chip" type="button" data-sector="{s["id"]}" aria-pressed="false">{_esc(s["name"])}</button>' for s in AD.SECTORS)
    toggles = "".join(
        f'<label><input type="checkbox" data-group="{k}" checked><span class="key key--{k}"></span>{v}</label>'
        for k, v in AD.GROUP_LABEL.items())
    datalist = "".join(f'<option value="{_esc(names[e])}">' for e in sorted(card_id, key=lambda k: names[k]))

    js_data = {
        "asof": AD.ASOF,
        "names": {e: names[e] for e in card_id},
        "home": AD.HOME,
        "edges": [{"a": e["a"], "b": e["b"], "g": AD.GROUP[e["type"]]} for e in AD.EDGES],
    }
    full = {
        "asof": AD.ASOF,
        "sectors": AD.SECTORS,
        "entities": {k: {"name": v[0], "description": v[1], "home": AD.HOME.get(k)} for k, v in AD.ENT.items()},
        "edges": AD.EDGES,
    }
    (ROOT / "tech-atlas.json").write_text(_json.dumps(full, ensure_ascii=False, indent=1), encoding="utf-8")

    gaps_html = "".join(
        f'<details><summary>{_esc(sec[sid]["name"])}</summary><ul>' + "".join(f"<li>{_esc(x)}</li>" for x in AT_GAPS[sid]) + "</ul></details>"
        for sid in [s["id"] for s in AD.SECTORS])
    method = "".join(f"<p>{_esc(x)}</p>" for x in AT_METHOD)
    intro = "".join(f"<p>{x}</p>" for x in AT_INTRO)
    n_cards = sum(len(p["players"]) for s in AD.SECTORS for p in s["positions"])

    html = (HEAD.format(title="The Tech Atlas | The Trojan Horse",
                        desc="A depth chart of the technology industry: who leads, who is catching up, and who is allied with, competing with or backed by whom.")
            + '<link rel="stylesheet" href="atlas.css">\n'
            + f"""
<a class="back" href="index.html">&larr; The Trojan Horse</a>

<div class="atlas-wide">
  <header class="atlas-head">
    <p class="atlas-head__k">As of {AD.ASOF}</p>
    <h1 class="atlas-head__t">The Tech Atlas</h1>
    <p class="atlas-head__l">{len(AD.SECTORS)} sectors, {n_cards} companies, ranked like a depth chart.</p>
  </header>
  <div class="atlas-intro">{intro}</div>
</div>

<nav class="atlas-bar" aria-label="Atlas controls">
  <div class="atlas-wide"><div class="atlas-bar__in">
    <input id="atlas-search" class="atlas-search" list="atlas-names" placeholder="Find a company" aria-label="Find a company">
    <datalist id="atlas-names">{datalist}</datalist>
    <div class="toggles" aria-label="Relationships to show">{toggles}</div>
    <div class="chips">{chips}</div>
  </div></div>
</nav>

<div class="atlas-wide">
  <section class="overview" id="overview">
    {"".join(bands)}
  </section>

  {"".join(sectors_html)}

  <section class="atlas-foot">
    <details>
      <summary>Method, and what this does not cover</summary>
      {method}
      <p>{_esc(AT_NOT_YET)}</p>
      <p>The full data is in <a href="tech-atlas.json">tech-atlas.json</a>, with every card and relationship and its source.</p>
      <p><b>Research log.</b> What each sector's evidence leaves open.</p>
      {gaps_html}
    </details>
  </section>
</div>
<script type="application/json" id="atlas-data">{_json.dumps(js_data, ensure_ascii=False)}</script>
<script src="atlas.js" defer></script>
""" + FOOT)
    (ROOT / "tech-atlas.html").write_text(html, encoding="utf-8")
    print(f"tech-atlas.html  ({len(AD.SECTORS)} sectors, {n_cards} cards, {len(AD.EDGES)} edges)")


GROUND = """
<section class="ground">
  <div class="shell">
    <p class="ground__k">Background</p>
    <p class="ground__n">Five explanations of the technology and banking
    concepts the entries rely on.</p>
    <ol class="ground__l">
{ITEMS}
    </ol>
  </div>
</section>
"""

def ground():
    rows = []
    for pr in PRIMERS:
        name = f'{pr["lead"]} {pr["line1"]} {pr["line2"]}'.replace("  ", " ").strip()
        rows.append(f'      <li><a href="{pr["slug"]}.html">'
                    f'<span class="g__n">No. {pr["roman"]}</span>'
                    f'<span class="g__t">{name}</span></a></li>')
    return GROUND.replace("{ITEMS}", "\n".join(rows))


# ==================================================== TEN YEARS, THE PAGE ===

MAXW = 48          # px, the widest the spine ever gets
def _clip(a, b):
    """A trapezoid from width a at the top to width b at the bottom."""
    ha, hb = a / MAXW * 50, b / MAXW * 50
    return (f"polygon({50-ha:.2f}% 0%, {50+ha:.2f}% 0%, "
            f"{50+hb:.2f}% 100%, {50-hb:.2f}% 100%)")

def _reading(title):
    """The entries used to carry a link out to a primer explaining what a chip
    or a data centre is. The map is the page now, so an entry no longer sends
    the reader away from it."""
    return ""

def kata_nodes():
    out, side = [], 0
    for i, (year, width, nodes) in enumerate(YEARS):
        nxt = YEARS[i+1][1] if i + 1 < len(YEARS) else width * .5
        out.append(f'''    <section class="yr" id="y{year}">
      <div class="yr__spine" aria-hidden="true" style="clip-path:{_clip(width, nxt)}"></div>
      <p class="yr__num">{year}</p>
''')
        for kind, tag, title, paras, note in nodes:
            s_ = " node--l" if side % 2 == 0 else " node--r"
            side += 1
            mk = {"seal": '<span class="node__mk node__mk--seal" aria-hidden="true">'
                          '<img src="images/helmet.png" alt=""></span>',
                  "column": '<span class="node__mk node__mk--col" aria-hidden="true">'
                            '<svg viewBox="0 0 100 124"><use href="#capital"/></svg></span>',
                  "stone": '<span class="node__mk" aria-hidden="true"></span>'}[kind]
            slug = DEAL_LINKS.get(title)
            t_ = (f'<a class="node__t node__t--go" href="{slug}.html">{title}'
                  f'<span class="node__go">Read the full note &rarr;</span></a>'
                  if slug else f'<h3 class="node__t">{title}</h3>')
            k_ = f'<p class="node__k">{tag}</p>\n          ' if tag else ""
            body = "\n          ".join(f'<p class="node__p">{x}</p>' for x in paras)
            n_ = (f'\n          <div class="node__why">'
                  f'<span class="node__hl">What it shows</span>'
                  f'<p class="node__p">{note}</p></div>') if note else ""
            out.append(f'''      <article class="node node--{kind}{s_}">
        {mk}
        <div class="node__b">
          {k_}{t_}
          {body}{n_}{_reading(title)}
        </div>
      </article>
''')
        out.append("    </section>\n")
    return "".join(out)


def build_katabasis():
    """Just the map. The page used to open with two paragraphs of argument,
    carry a Ground Floor of primers explaining what a chip and a data centre
    are, and close with an essay on what the entries support. All of it was
    standing between the reader and the ten years."""
    html = (HEAD.format(title="Ten Years in Technology | The Trojan Horse",
                        desc="A map of technology transactions from 2016 to 2026.")
            + CAPITAL_DEF + f'''
<a class="back" href="index.html">&larr; The Trojan Horse</a>

<header class="silohead silohead--bare">
  <div class="shell">
    <p class="silohead__kicker">2016 to 2026</p>
    <h1 class="silohead__name">Ten Years</h1>
    <div class="silohead__line" aria-hidden="true"></div>
  </div>
</header>

<main class="kata">
  <div class="shell">
{kata_nodes()}
  </div>

  <p class="kata__note">The band down the page is a hand-drawn outline of deal
  activity and not a data series. Values are announced values unless an entry
  says final.</p>
</main>
''' + FOOT)
    (ROOT / "ten-years.html").write_text(html, encoding="utf-8")
    # the page was published once under its old name
    (ROOT / "katabasis.html").write_text(
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<title>Ten Years | The Trojan Horse</title>'
        '<link rel="canonical" href="https://trojanhorse.blog/ten-years.html">'
        '<meta http-equiv="refresh" content="0; url=ten-years.html">'
        '</head><body><p><a href="ten-years.html">Ten Years in Technology</a></p>'
        '</body></html>\n', encoding="utf-8")
    n = sum(len(y[2]) for y in YEARS)
    print(f"ten-years.html  ({len(YEARS)} years, {n} entries)")



# ================================================== THE PROCESS, A CHAPTER ===
from process_data import (KICKER as P_KICKER, TITLE as P_TITLE, LEDE as P_LEDE,
                          INTRO as P_INTRO, STAGES as P_STAGES,
                          CLOSE_HEAD as P_CLOSE_HEAD, CLOSE as P_CLOSE,
                          PART1 as P_PART1, PART3 as P_PART3,
                          PART1_H as P_P1H, PART2_H as P_P2H, PART3_H as P_P3H,
                          NOTE as P_NOTE)

def rail():
    """The horizontal route map. One stop per stage, a line running through
    the markers, each stop jumping to its chapter."""
    out = ['<div class="rail"><div class="rail__track">']
    for roman, name, dur, _ in P_STAGES:
        out.append(f'''<a class="stop" href="#s{roman}">
          <span class="stop__n">{roman}</span>
          <span class="stop__dot" aria-hidden="true"></span>
          <span class="stop__t">{name}</span>
          <span class="stop__d">{dur}</span>
        </a>''')
    out.append("</div></div>")
    return "".join(out)


def _parts(sections):
    """Headed prose sections, same furniture as the numbered stages minus the
    numeral and the duration."""
    out = []
    for head, paras in sections:
        body = "\n".join(f'        <p class="wp__p">{x}</p>' for x in paras)
        out.append(f'''      <section class="ch">
        <h2 class="ch__h">{head}</h2>
{body}
      </section>''')
    return chr(10).join(out)


def build_process():
    chapters = []
    for roman, name, dur, paras in P_STAGES:
        body = "\n".join(f'        <p class="wp__p">{x}</p>' for x in paras)
        chapters.append(f'''      <section class="ch" id="s{roman}">
        <p class="ch__k"><span class="ch__n">{roman}</span>{dur}</p>
        <h2 class="ch__h">{name}</h2>
{body}
      </section>''')

    intro = "\n".join(f'      <p class="wp__p wp__p--lead">{x}</p>' for x in P_INTRO)
    close = "\n".join(f'        <p class="wp__p">{x}</p>' for x in P_CLOSE)

    html = (HEAD.format(title=f"{P_TITLE} | The Trojan Horse",
                        desc="How an investment bank gets hired, how a sale "
                             "then runs stage by stage, and why the managing "
                             "director matters more than the logo.")
            + f'''
<a class="back back--dark" href="index.html">&larr; The Trojan Horse</a>

<header class="plate">
  <div class="shell plate__in">
    <p class="plate__k">{P_KICKER}</p>
    <h1 class="plate__t">{P_TITLE}</h1>
    <p class="plate__l">{P_LEDE}</p>
  </div>
</header>

<main class="white">
  <div class="shell">
    <article class="wp wp--wide">
{intro}
    </article>

    <figure class="sk">{sketch.coast()}</figure>

    <article class="wp">
      <p class="part">{P_P1H}</p>
{_parts(P_PART1)}
    </article>

    <div class="wv">{sketch.wave()}</div>
    <p class="part part--rail">{P_P2H}</p>
    {rail()}

    <article class="wp">
{chr(10).join(chapters)}

      <section class="ch ch--close">
        <h2 class="ch__h">{P_CLOSE_HEAD}</h2>
{close}
      </section>
    </article>

    <article class="wp">
      <div class="wv">{sketch.wave()}</div>
      <p class="part">{P_P3H}</p>
{_parts(P_PART3)}

      <p class="wp__note">{P_NOTE}</p>

      <a class="wp__go" href="trojan-horses.html">Next: two things in this business that I think are mislabelled &rarr;</a>
    </article>
  </div>
</main>
''' + FOOT)
    (ROOT / "how-a-company-gets-sold.html").write_text(html, encoding="utf-8")
    print(f"how-a-company-gets-sold.html  ({len(P_STAGES)} stages)")


# =================================================== TROJAN HORSES ===
# Argument rather than reporting, and the page says so. A landing page with two
# circular horses, each opening its own reading.
from horses_data import (KICKER as H_KICKER, TITLE as H_TITLE, LEDE as H_LEDE,
                         SECTIONS as H_SECTIONS, NOTE as H_NOTE)

def build_horses():
    """One transaction, on the white plate. The section used to be a landing
    with two circular horses opening two speculative readings. It carries a
    single piece now, so the landing and the sub-pages are gone."""
    body = []
    for head, paras in H_SECTIONS:
        inner = "\n".join(f'        <p class="wp__p">{x}</p>' for x in paras)
        body.append(f'''      <section class="ch">
        <h2 class="ch__h">{head}</h2>
{inner}
      </section>''')

    html = (HEAD.format(title=f"{H_TITLE} | The Trojan Horse",
                        desc="P&G agreed to buy Thorne for $3.8 billion, three "
                             "years after L Catterton took it private for about "
                             "$680 million. The record shows both prices and not "
                             "the reason.")
            + f'''
<a class="back back--dark" href="index.html">&larr; The Trojan Horse</a>

<header class="plate">
  <div class="shell plate__in">
    <p class="plate__k">{H_KICKER}</p>
    <h1 class="plate__t">{H_TITLE}</h1>
    <p class="plate__l">{H_LEDE}</p>
  </div>
</header>

<main class="white">
  <div class="shell">
    <article class="wp">
{chr(10).join(body)}

      <p class="wp__note">{H_NOTE}</p>

      <a class="wp__go" href="how-a-company-gets-sold.html">How a bank gets hired, and how a sale runs &rarr;</a>
    </article>
  </div>
</main>
''' + FOOT)
    (ROOT / "trojan-horses.html").write_text(html, encoding="utf-8")
    # the two readings were published under their own names
    for slug, label in (("horse-credit", "Trojan Horses"),
                        ("horse-apprenticeship", "Trojan Horses")):
        (ROOT / f"{slug}.html").write_text(
            '<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<title>{label} | The Trojan Horse</title>'
            '<link rel="canonical" href="https://trojanhorse.blog/trojan-horses.html">'
            '<meta http-equiv="refresh" content="0; url=trojan-horses.html">'
            '</head><body><p><a href="trojan-horses.html">Trojan Horses</a></p>'
            '</body></html>\n', encoding="utf-8")
    print(f"trojan-horses.html  ({len(H_SECTIONS)} sections, 2 redirects)")


if __name__ == "__main__":
    build_index()
    build_stories_page()
    build_process()
    build_horses()
    build_weekly()
    build_primers()
    build_deals()
    build_desk()
    build_desk_index()
    build_buyers()
    build_atlas()
    build_katabasis()
    build_podcast()
