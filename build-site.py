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
      stories=["buying-the-standard", "bought-then-freed"]),
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
    <p class="cover__tag">A Mergers and Acquisitions<br>Journal &amp; Podcast</p>
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
<!-- ============================================================= ESSAY === -->
<section class="essay" id="opening">
  <div class="shell">

    <div class="essay__inner">
      <p>Ever since I was a kid, I&rsquo;ve found my peace through writing, in stories, letters, -isms, and planning. Being able to jot down and wrestle with complex ideas or experiences has always brought along great joy in my life.</p>
      <p>Yet today&rsquo;s status quo demands the exact opposite. I see a heavy reliance on consensus narratives, a collective cognitive offloading that is increasingly eroding our fundamental instinct to question the norm.</p>
      <p>The idea for this site actually started because I just wanted to find my own thoughts among the clutter of financial news and show it to the world through my art and personality.</p>
      <p>With the rise of over summarization and a splurge of low friction short form content, it is often easy to allow for neuroplastic degradation, or in normal english: a loss of curiosity.</p>
    </div>

    <figure class="defn">
      <p class="defn__w">curiosity</p>
      <div class="defn__b">
        <p class="defn__d">not the wish to know a thing, which is appetite and passes, but the refusal to accept the headline as the answer. the suspicion that every explanation you were handed is the shortened version, and the willingness to be the only person in the room still asking after everybody else has moved on.</p>
        <p class="defn__p">[ kyoor-ee-<em>os</em>-i-tee ]</p>
      </div>
    </figure>

    <div class="essay__inner">
      <p>The Trojan Horse was built to challenge complacency. Why M&amp;A? Because corporate acquisitions are the invisible architecture of our daily lives. M&amp;A is the ultimate collision of game theory, psychology, and global power. It is a hyper-complex puzzle that forces us to look past the spreadsheets and ask why the pieces are actually moving. It&rsquo;s a vehicle meant to bypass the noise and wake up our inherent desire to decode the world.</p>
      <p>I built this to refine my voice and present analysis as art.</p>
      <p class="essay__sign">My name is Francis Ruan, and I welcome you to the Trojan Horse.</p>
    </div>

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
    cards = []
    for s in SILOS:
        cards.append(f'''      <a class="silo" href="{s["slug"]}.html">
        <span class="silo__name">{s["name"]}</span>
        <svg class="silo__cap" viewBox="0 0 100 124" aria-hidden="true"><use href="#capital"/></svg>
        <span class="silo__word">{s["word"]}</span>
      </a>''')

    picker = ('  <div class="shell cover__picker">\n'
              '    <div class="silos__grid">\n'
              + "\n".join(cards) + "\n"
              '    </div>\n'
              '  </div>\n')

    html = (HEAD.format(title="The Trojan Horse",
                        desc="A mergers and acquisitions journal and podcast by Francis Ruan.")
            + CAPITAL_DEF + COVER.replace("{PICKER}", picker) + ESSAY + FOOT)
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print("index.html")


def build_silo(s):
    desc = s["word"]
    html = (HEAD.format(title=f'{s["name"]} | The Trojan Horse',
                        desc=f'{desc}. {s["blurb"]}')
            + VINE_DEF + f'''
<a class="back" href="index.html">&larr; All verticals</a>

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
    for s in SILOS:
        build_silo(s)
