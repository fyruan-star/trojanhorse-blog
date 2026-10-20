#!/usr/bin/env python3
"""Emit the index, the stories page and the podcast page.

The site shows one story. Everything previously published lives in archive/,
which is git-ignored, so it stays on disk and never reaches the web. To bring
a piece back: move its html out of archive/, add it to STORY below, rebuild.
"""
import pathlib, sys

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
    <p class="cover__tag">Mergers &amp; Acquisitions<span class="cover__tag__sub">A Journal of Strategy &amp; Conquest</span></p>
  </div>

  <div class="cover__mist" aria-hidden="true"></div>

{PICKER}
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
      <p class="tale__open"><span class="tale__cap">F</span>or ten years the Greeks hurled themselves against the walls of Troy and never breached them. Then they built a wooden horse, left it on the shore as a gift, and sailed away as though the war were over. The Trojans wheeled it through their own gates. That night, soldiers slipped from its belly and opened the city from within.</p>
    </div>

    <figure class="creed">
      <p class="creed__l">The strongest walls are rarely broken.</p>
      <p class="creed__l creed__l--turn">They are opened by the people they were built to protect.</p>
    </figure>

    <div class="tale">
      <p>Mergers and acquisitions are wars fought in boardrooms rather than on battlefields. Companies lay siege to one another, build defenses, forge alliances, and, when force fails, reach for the oldest weapon of all: an offer too attractive to refuse. Every deal is a horse left at the gates, and the question is always what it holds.</p>
      <p>Here, I tell those deals as stories. I trace the strategy behind every move, the deception, real and imagined, that shapes what each side believes, and the leverage that passes from hand to hand. No finance degree required. Only the curiosity to stand before the horse and wonder what&rsquo;s inside.</p>
      <p class="tale__sign">My name is Francis Ruan.<br>Welcome to The Trojan Horse.</p>
    </div>

  </div>
</section>
"""

# Episodes are questions, not deal recaps: the thing worth an hour is the
# mechanism underneath, not the transaction on top.
EPISODES = [
 ("Why Models Fail",
  "A discounted cash flow is right up until it meets a business. Where it breaks first, why the failure is almost never arithmetic, and what a forecast is actually claiming when it says growth costs nothing.",
  "Recording October"),
 ("Sleep As Capital",
  "The analyst at three in the morning is a depreciating asset nobody books. What the sleep research says about judgement under deprivation, and whether a desk that runs on it is buying output or borrowing against it.",
  "In production"),
 ("The Adjusted Truth",
  "Adjusted EBITDA excludes whatever management has decided is unusual. Who audits the definition of unusual, and what happens to a multiple when the denominator is a choice.",
  "In production"),
 ("Managing The Number",
  "Companies rarely fake earnings. They shape them. The entirely legal machinery for landing on consensus, and why the quarter you cannot see is the interesting one.",
  "In production"),
 ("Who Picks Comparables",
  "Every comp set is an argument about what a company is. Change the peers and you change the answer, and almost nobody shows their working.",
  "In production"),
 ("Writers Make Bankers",
  "Underneath the models the job is persuasive narrative. What separates good writing from great, and why nobody tells you that on the way in.",
  "Recording October"),
 ("The Confidence Trap",
  "Two methods agreeing feels like proof. Often it is one assumption counted twice, wearing a second coat.",
  "In production"),
 ("Disconnected",
  "Build something genuinely complicated with the internet switched off. A running experiment in what recall costs when retrieval is free.",
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
    <p class="silohead__blurb">Conversations on the mechanisms underneath M&amp;A. Guests are being booked now; episodes appear here as they are cut.</p>
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
    # One door, not three. The verticals still organise the writing; they are
    # no longer the first decision a reader is asked to make.
    picker = ('''  <div class="shell cover__picker">
    <div class="silos__grid silos__grid--two">
      <a class="silo silo--solo" href="strategemata.html">
        <span class="silo__name">Strategemata</span>
        <svg class="silo__cap" viewBox="0 0 100 124" aria-hidden="true"><use href="#capital"/></svg>
        <span class="silo__word">Read Stories</span>
      </a>
      <a class="silo silo--solo" href="katabasis.html">
        <span class="silo__name">Katabasis</span>
        <svg class="silo__cap" viewBox="0 0 100 124" aria-hidden="true"><use href="#capital"/></svg>
        <span class="silo__word">Ten Years</span>
      </a>
    </div>
  </div>
''')

    html = (HEAD.format(title="The Trojan Horse",
                        desc="A mergers and acquisitions journal and podcast by Francis Ruan.")
            + CAPITAL_DEF + COVER.replace("{PICKER}", picker) + ESSAY + ROOMS + FOOT)
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print("index.html")


STRAT_BLURB = ("Frontinus wrote down the stratagems of Roman commanders so the "
               "next one would recognise the move on sight. Mine are here for "
               "the same reason.")

def build_stories_page():
    """Every deal note on one vine, in silo order so neighbours rhyme."""
    order = list(STORY)
    html = (HEAD.format(title="Strategemata | The Trojan Horse",
                        desc="Every deal note in The Trojan Horse. " + STRAT_BLURB)
            + VINE_DEF + f'''
<a class="back" href="index.html">&larr; The Trojan Horse</a>

<header class="silohead">
  <div class="shell">
    <p class="silohead__kicker">The Stories</p>
    <h1 class="silohead__name">Strategemata</h1>
    <p class="silohead__blurb">{STRAT_BLURB}</p>
    <div class="silohead__line" aria-hidden="true"></div>
  </div>
</header>

<main class="belt" id="stories">
  <div class="shell">
{belt(order)}
  </div>
</main>
''' + FOOT)
    (ROOT / "strategemata.html").write_text(html, encoding="utf-8")
    print(f"strategemata.html  ({len(order)} stories)")





# ====================================================== THE GROUND FLOOR ===
from primers_data import PRIMERS
from deals_data import DEALS

# a timeline node's title to the page it opens
DEAL_LINKS = {
 "SoftBank / ARM":      "the-blueprint",
 "Broadcom / Qualcomm": "the-blocked-bid",
 "IBM / Red Hat":       "the-layer-above",
 "NVIDIA / Mellanox":   "the-wiring",
 "AMD / Xilinx":        "paid-in-paper",
 "NVIDIA / ARM":        "too-central",
 "Broadcom / VMware":   "the-price-machine",
 "Cisco / Splunk":      "reading-the-record",
 "Google / Wiz":        "third-in-line",
 "DDN / Blackstone":    "fetching",
}

# a primer is offered at the point on the spine where it first matters
PRIMER_AT = {
 "SoftBank / ARM":                    ("what-a-chip-is",   "what a chip actually is"),
 "IBM / Red Hat":                     ("what-the-cloud-is", "what the cloud actually is"),
 "A chatbot appears":                 ("what-ai-needs",     "what AI actually needs"),
 "The money changes shape":           ("the-building",      "what is inside the building"),
 "Where the money actually comes from": ("what-a-bank-does", "what a bank actually does"),
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

  <p class="takeaway">{takeaway}</p>

  <figure class="mark"><img src="images/horse.png" alt="The Trojan Horse engraving"></figure>

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
                + SHEET.format(back="katabasis.html", backlabel="Katabasis",
                               lead=ld, line1=pr["line1"], row2=row, sub=pr["sub"],
                               lede=pr["lede"], sections=_sections(pr["sections"]),
                               takeaway=pr["takeaway"], tail=tail,
                               series="The Ground Floor", roman=f'No. {pr["roman"]}',
                               last="Katabasis")
                + "\n</body>\n</html>\n")
        (ROOT / f'{pr["slug"]}.html').write_text(html, encoding="utf-8")
    print(f"{len(PRIMERS)} primers")


def build_deals():
    for d in DEALS:
        ld, row = _title(d["lead"], d["line1"], d["line2"])
        srcs = "\n".join(f"      <li>{x}</li>" for x in d["srcs"])
        tail = ('  <div class="srcs">\n    <h3>Sources</h3>\n    <ol>\n'
                + srcs + '\n    </ol>\n  </div>')
        html = (HEAD.format(title=f'{d["lead"]} {d["line1"]} {d["line2"]} | The Trojan Horse'.replace("  "," ").strip(),
                            desc=f'{d["party"]} &middot; {d["value"]} &middot; {d["dated"]}.')
                + '\n<link rel="stylesheet" href="story.css">\n'
                + SHEET.format(back="katabasis.html", backlabel="Katabasis",
                               lead=ld, line1=d["line1"], row2=row, sub=d["sub"],
                               lede=d["lede"], sections=_sections(d["sections"]),
                               takeaway=d["takeaway"], tail=tail,
                               series="Katabasis", roman=f'No. {d["roman"]}',
                               last=f'{d["party"]} &middot; {d["value"]}')
                + "\n</body>\n</html>\n")
        (ROOT / f'{d["slug"]}.html').write_text(html, encoding="utf-8")
    print(f"{len(DEALS)} deal notes")


GROUND = """
<section class="ground">
  <div class="shell">
    <p class="ground__k">The Ground Floor</p>
    <p class="ground__n">Five things that make the rest of this readable. Take
    them first if you want, or pick them up off the spine where they start to
    matter. No prior knowledge is assumed anywhere in them.</p>
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


# ========================================================== KATABASIS =====
from kata_data import YEARS

KATA_BLURB = ("Greek, the going down. Ten years of technology coverage read "
              "from the surface to wherever we are now, on the understanding "
              "that every one of these deals was a horse somebody wheeled "
              "through their own gates.")

MAXW = 48          # px, the widest the spine ever gets
def _clip(a, b):
    """A trapezoid from width a at the top to width b at the bottom."""
    ha, hb = a / MAXW * 50, b / MAXW * 50
    return (f"polygon({50-ha:.2f}% 0%, {50+ha:.2f}% 0%, "
            f"{50+hb:.2f}% 100%, {50-hb:.2f}% 100%)")

def _stone(title):
    """The lift-the-stone offer, placed where a term first needs explaining."""
    pr = PRIMER_AT.get(title)
    if not pr: return ""
    slug, label = pr
    return (f'\n          <a class="node__stone" href="{slug}.html">'
            f'Lift the stone: {label}</a>')

def kata_nodes():
    out, side = [], 0
    for i, (year, width, nodes) in enumerate(YEARS):
        nxt = YEARS[i+1][1] if i + 1 < len(YEARS) else width * .5
        out.append(f'''    <section class="yr" id="y{year}">
      <div class="yr__spine" aria-hidden="true" style="clip-path:{_clip(width, nxt)}"></div>
      <p class="yr__num">{year}</p>
''')
        for n in nodes:
            kind = n[0]
            s_ = " node--l" if side % 2 == 0 else " node--r"
            side += 1
            if kind == "stone":
                _, _, title, body = n
                out.append(f'''      <article class="node node--stone{s_}">
        <span class="node__mk" aria-hidden="true"></span>
        <div class="node__b">
          <h3 class="node__t">{title}</h3>
          <p class="node__p">{body}</p>{_stone(title)}
        </div>
      </article>
''')
            else:
                _, tag, title, look, horse = n
                mk = ('<span class="node__mk node__mk--seal" aria-hidden="true">'
                      '<img src="images/helmet.png" alt=""></span>') if kind == "seal" else (
                     '<span class="node__mk node__mk--col" aria-hidden="true">'
                     '<svg viewBox="0 0 100 124"><use href="#capital"/></svg></span>')
                slug = DEAL_LINKS.get(title)
                t_ = (f'<a class="node__t node__t--go" href="{slug}.html">{title}'
                      f'<span class="node__go">Read the note &rarr;</span></a>'
                      if slug else f'<h3 class="node__t">{title}</h3>')
                out.append(f'''      <article class="node node--{kind}{s_}">
        {mk}
        <div class="node__b">
          <p class="node__k">{tag}</p>
          {t_}
          <p class="node__look">{look}</p>
          <p class="node__horse"><span class="node__hl">In the belly</span>{horse}</p>{_stone(title)}
        </div>
      </article>
''')
        out.append("    </section>\n")
    return "".join(out)


def build_katabasis():
    html = (HEAD.format(title="Katabasis | The Trojan Horse",
                        desc="Ten years of technology dealmaking, 2016 to 2026, "
                             "explained from the ground up.")
            + CAPITAL_DEF + f'''
<a class="back" href="index.html">&larr; The Trojan Horse</a>

<header class="silohead">
  <div class="shell">
    <p class="silohead__kicker">Ten Years</p>
    <h1 class="silohead__name">Katabasis</h1>
    <p class="silohead__blurb">{KATA_BLURB}</p>
    <div class="silohead__line" aria-hidden="true"></div>
  </div>
</header>

{ground()}
<main class="kata">
  <div class="shell">
{kata_nodes()}
  </div>
  <p class="kata__note">The spine is the money. It thickens as capital floods
  in and thins when the window shuts, drawn to the shape of the cycle rather
  than to a dataset, because an exact one would imply a precision this does not
  have. Deal values are as announced. Where a deal closed at a different time or
  a different number, the entry says so.</p>
</main>
''' + FOOT)
    (ROOT / "katabasis.html").write_text(html, encoding="utf-8")
    n = sum(len(y[2]) for y in YEARS)
    print(f"katabasis.html  ({len(YEARS)} years, {n} nodes)")


if __name__ == "__main__":
    build_index()
    build_stories_page()
    build_primers()
    build_deals()
    build_katabasis()
    build_podcast()
