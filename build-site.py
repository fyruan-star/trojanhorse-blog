#!/usr/bin/env python3
"""Emit the index and the three silo pages from one source of truth.

The reader picks a vertical before any story is shown. Each story belongs to
exactly one silo; SILOS below is the only place that mapping lives, and
check_disjoint() refuses to build if a slug ever appears twice.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).parent

# slug, three-word title, the party, the M&A line printed under it
STORY = {
 "buying-the-standard":    ("Buying The Standard",    "Databricks / Tabular",                "Enterprise Data M&amp;A"),
 "the-boring-layer":       ("The Boring Layer",       "DDN / Blackstone",                    "AI Infrastructure M&amp;A"),
 "bought-then-freed":      ("Bought Then Freed",      "NVIDIA / Run:ai",                     "AI Infrastructure M&amp;A"),
 "the-missing-fifth":      ("The Missing Fifth",      "Unilever / Gr&uuml;ns",               "Consumer Health M&amp;A"),
 "premium-without-profit": ("Premium Without Profit", "Mars / Hotel Chocolat",               "Premium Consumer M&amp;A"),
 "the-margin-gap":         ("The Margin Gap",         "Danone / Huel",                       "Functional Nutrition M&amp;A"),
 "two-versus-six":         ("Two Versus Six",         "L Catterton / Good Culture",          "Sponsor Strategy M&amp;A"),
 "owning-the-clock":       ("Owning The Clock",       "Infinite Epigenetics / Tally Health", "Longevity Tech M&amp;A"),
}

SILOS = [
 dict(slug="agorastes", name="Agorastes", word="Consumer", desc=("On The Consumer",),
      blurb="Brands bought for shelf, story and the household that already trusts them.",
      stories=["premium-without-profit", "two-versus-six"]),
 dict(slug="hygeia", name="Hygeia", word="Health", desc=("On Wellness", "and Health"),
      blurb="Supplements, nutrition and the long argument about living longer.",
      stories=["the-missing-fifth", "the-margin-gap", "owning-the-clock"]),
 dict(slug="techne", name="Techne", word="Tech", desc=("On Technology", "and Innovation"),
      blurb="Infrastructure, standards and the software underneath the software.",
      stories=["buying-the-standard", "bought-then-freed", "the-boring-layer"]),
]

def check_disjoint():
    seen, dupes = {}, []
    for s in SILOS:
        for slug in s["stories"]:
            if slug not in STORY:
                sys.exit(f"unknown story: {slug}")
            if slug in seen:
                dupes.append(f'{slug} in both {seen[slug]} and {s["slug"]}')
            seen[slug] = s["slug"]
    missing = set(STORY) - set(seen)
    if dupes: sys.exit("stories duplicated across silos:\n  " + "\n  ".join(dupes))
    if missing: sys.exit(f"stories in no silo: {sorted(missing)}")
    return seen

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

FIRST = """
<!-- ==================================================== FIRST PRINCIPLES === -->
<section class="fp" id="first-principles">
  <div class="shell">
    <div class="fp__head">
      <p class="fp__label">First Principles</p>
      <h2 class="fp__title">Underneath It</h2>
      <p class="fp__note">Pieces that go at the assumption rather than the deal. Slower, and the ones I care most about.</p>
    </div>
    <ol class="fp__list">
      <li>
        <a class="fp__item" href="the-wrong-question.html">
          <span class="fp__no">No. I</span>
          <span class="fp__body">
            <span class="fp__h">The Wrong Question</span>
            <span class="fp__q">A spreadsheet can be perfectly calculated and still answer the wrong question. What a record of 13,019 valuation multiples says about the habits underneath the methods.</span>
          </span>
          <span class="fp__go">Read &rarr;</span>
        </a>
      </li>
    </ol>
  </div>
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
    <div class="silos__grid silos__grid--one">
      <a class="silo silo--solo" href="strategemata.html">
        <span class="silo__name">Strategemata</span>
        <svg class="silo__cap" viewBox="0 0 100 124" aria-hidden="true"><use href="#capital"/></svg>
        <span class="silo__word">Read Stories</span>
      </a>
    </div>
  </div>
''')

    html = (HEAD.format(title="The Trojan Horse",
                        desc="A mergers and acquisitions journal and podcast by Francis Ruan.")
            + CAPITAL_DEF + COVER.replace("{PICKER}", picker) + ESSAY + FIRST + ROOMS + FOOT)
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print("index.html")


STRAT_BLURB = ("Frontinus wrote down the stratagems of Roman commanders so the "
               "next one would recognise the move on sight. Mine are here for "
               "the same reason.")

def build_stories_page():
    """Every deal note on one vine, in silo order so neighbours rhyme."""
    order = [slug for s in SILOS for slug in s["stories"]]
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


def build_silo(s):
    desc = s["word"]
    html = (HEAD.format(title=f'{s["name"]} | The Trojan Horse',
                        desc=f'{desc}. {s["blurb"]}')
            + VINE_DEF + f'''
<a class="back" href="strategemata.html">&larr; All stories</a>

<header class="silohead">
  <div class="shell">
    <p class="silohead__kicker">{desc}</p>
    <h1 class="silohead__name">{s["name"]}</h1>
    <p class="silohead__blurb">{s["blurb"]}</p>
    <div class="silohead__line" aria-hidden="true"></div>
  </div>
</header>

<main class="belt" id="stories">
  <div class="shell">
{belt(s["stories"])}
  </div>
</main>
''' + FOOT)
    (ROOT / f'{s["slug"]}.html').write_text(html, encoding="utf-8")
    print(f'{s["slug"]}.html  ({len(s["stories"])} stories)')


if __name__ == "__main__":
    mapping = check_disjoint()
    print(f"{len(mapping)} stories, each in exactly one silo\n")
    build_index()
    build_stories_page()
    for s in SILOS:
        build_silo(s)
    build_podcast()
