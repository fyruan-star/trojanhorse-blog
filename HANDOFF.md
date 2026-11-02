# Handoff: The Trojan Horse (trojanhorse.blog)

Written 2 November 2026, after commit `b6678dd`. This is the working guide for anyone, human or AI, picking the project up from where it stands now. `CLAUDE.md` carries the short list of rules that always apply. This file carries everything else.

**To start a new Claude Code session**, open Claude Code in this folder and say:

> Work on the Trojan Horse blog in this folder. Read CLAUDE.md and HANDOFF.md first, tell me the current state in five lines, then ask what I want to change.

## 1. Snapshot

- Live at https://trojanhorse.blog. HTTPS is enforced and `www` redirects to the apex domain.
- An M&A journal by Francis Ruan. Tagline on the cover: "Hidden Risks Behind Promising Deals".
- 34 HTML pages, four of them redirects. Three Trojan Horse stories (Oura, Thorne, Uber), a "Prologue" timeline of ten years of tech deals with ten deal notes and five background pages, a three-story Palo Alto sub-journal, a Tech Atlas (9 sectors, 159 cards, 89 relationships), an essay-style process page, and a podcast page with no audio yet.
- The site is fully generated. A clean clone rebuilt from scratch on 2 November 2026 produced output identical to what is live.

## 2. Where everything lives, and who has access

| Thing | Where |
| --- | --- |
| Live site | https://trojanhorse.blog |
| Repository | https://github.com/fyruan-star/trojanhorse-blog (public) |
| Hosting | GitHub Pages, legacy build, branch `main`, folder `/`. `CNAME` sets the domain. `.nojekyll` is set, so every file in the repo is served exactly as committed. |
| Domain | Porkbun is both registrar and DNS. The apex has A records for GitHub Pages (185.199.108.153 through .111.153) and `www` is a CNAME to `fyruan-star.github.io`. Registered 2026-09-27, expires 2027-09-27. |
| Francis's local copy | `~/Desktop/3 Projects & Code/trojan-horse` |
| Local only, not in git | `archive/` (14 retired pieces from September 2026) and `images/horse.webp`. Both are git-ignored. A fresh clone does not have them, and the site does not need them. Back up `archive/` if it matters. |

**Access.** Only the owner (`fyruan-star`) can push. To let someone else publish, go to the repo's Settings, then Collaborators, then Add people, or run `gh api -X PUT repos/fyruan-star/trojanhorse-blog/collaborators/<username> -f permission=push`. Anyone with push access publishes straight to the live site with no review. If several people will edit, protect `main` and work by pull request. Without push access, fork the repo, build, and open a pull request.

**Nothing else needs configuring.** There are no secrets, API keys, environment variables or build services anywhere in the project.

**Owner-only tasks** are at Porkbun: the domain lock (see section 12), renewal and DNS.

## 3. Set up and daily commands

You need Python 3 (built and tested on 3.13, standard library only) and git. The `gh` CLI is optional and useful for checking Pages.

```bash
git clone https://github.com/fyruan-star/trojanhorse-blog.git && cd trojanhorse-blog
python3 build-site.py            # rebuilds every page
python3 -m http.server 8731      # preview at http://localhost:8731/
pkill -f "http.server 8731"      # stop the preview
```

Reproducibility check: in a fresh clone, run `python3 build-site.py` and then `git status`. It should list nothing. If a build changes files you did not intend to change, the sources and the committed HTML have drifted apart.

## 4. How the build works

`build-site.py` imports the data modules, and its `build_*` functions write the pages using templates held in the same file (`HEAD`, `FOOT`, `SHEET`, `COVER`, `ESSAY`, `ROOMS`, `CAPITAL_DEF`, `GROUND`, `DESK_DOOR`). The entry point runs, in order: `build_index`, `build_stories_page`, `build_process`, `build_horses`, `build_weekly` for each module in `WEEKLIES`, `build_primers`, `build_deals`, `build_desk`, `build_desk_index`, `build_buyers`, `build_atlas`, `build_katabasis`, `build_podcast`.

It is deterministic. The line art in `sketch.py` draws from a fixed random seed, so repeated builds are byte identical.

Stylesheets: `site.css` is used by every page (its section headers are listed in section 7E), `story.css` by deal notes, background pages and the Palo Alto stories, and `atlas.css` plus `atlas.js` by the Atlas. Fonts come from Google Fonts (Cormorant Garamond). Colours are tokens at the top of `site.css`: navy `#303D52`, cream `#F7F4EE`, and a deeper blue `#1C2675` used for type on the white plates.

**Hand-editable files:** `site.css`, `story.css`, `atlas.css`, `atlas.js`, `404.html`, `images/`, `CNAME`. Everything else in the root is generated or is source.

## 5. The homepage, top to bottom

1. **Cover**: the horse artwork, the wordmark and the tagline. Template `COVER` in `build-site.py`.
2. **The Troy essay**: five paragraphs and a sign-off, opening at the gates of Troy and turning to M&A. Template `ESSAY`.
3. **Prologue row**: one row linking to `ten-years.html`, labelled "2016 to 2026". Built inside `build_index`.
4. **Trojan Horses**: three equal columns, one per story in `WEEKLIES` order (Oura, Thorne, Uber). Each card has the company logo, a date, the headline, a one-sentence `HOOK` and a "Continue reading" link. Built inside `build_index` from the `weekly_*.py` modules.
5. **Spotify mark** linking to `podcast.html`, with a small "Atlas" link under it to `tech-atlas.html`. Template `ROOMS`.
6. **Footer**. Template `FOOT`.

## 6. Which source feeds which page

| Page(s) | Edit this | Built by |
| --- | --- | --- |
| `index.html` | `COVER`, `ESSAY`, `ROOMS`, `FOOT` in `build-site.py`, and the card text comes from the weekly modules | `build_index` |
| `ten-years.html` (the Prologue) | `kata_data.py` (`YEARS`: eleven years, 28 entries). Its `INTRO`, `INTRO_2` and `CLOSE` are imported but no longer rendered | `build_katabasis` |
| `katabasis.html` | redirect to `ten-years.html` (old name) | `build_katabasis` |
| 10 deal notes | `deals_data.py` (`DEALS`). Prologue entries link to them through `DEAL_LINKS` in `build-site.py` | `build_deals` |
| 5 background pages | `primers_data.py` (`PRIMERS`). The links to them from the Prologue were removed, so they are currently unlinked | `build_primers` |
| `palo-alto.html`, `desk-ddn.html`, `desk-wolfspeed.html`, `desk-wasabi.html` | `desk_data.py` | `build_desk`, `build_desk_index` |
| `the-buyers-bank.html` | `buyers_data.py` | `build_buyers` |
| `how-a-company-gets-sold.html` | `process_data.py` (Part One carried over from the old Mandate page, the eight stages, Part Three on managing directors), plus `sketch.py` for the line art | `build_process` |
| `strategemata.html` | redirect to the page above (the old "Mandate" page). `mandate_data.py` still holds its original text but is not rendered | `build_stories_page` |
| `trojan-horses.html` | `horses_data.py`: the "P&G and Thorne" prices piece | `build_horses` |
| `horse-credit.html`, `horse-apprenticeship.html` | redirects to `trojan-horses.html` | `build_horses` |
| `oura-ipo.html` | `weekly_data.py` (the module name is a leftover and it holds the Oura story) | `build_weekly` |
| `thorne-loyalty.html` | `weekly_thorne.py` | `build_weekly` |
| `uber-rival-dinner.html` | `weekly_uber.py` | `build_weekly` |
| `tech-atlas.html`, `tech-atlas.json` | `atlas_data.py` and the `atlas_*.py` sector modules. `_MODULES` in `atlas_data.py` lists the nine active sectors | `build_atlas` |
| `podcast.html` | `EPISODES` in `build-site.py` | `build_podcast` |
| `404.html` | hand-written, not generated | none |

## 7. Procedures

### 7A. Change text on an existing page

Find the page in section 6, edit the source, then follow the seven steps in `CLAUDE.md`. Examples: the cover tagline is in `COVER`, the Troy essay is `ESSAY`, a story's wording is in its `weekly_*.py` `SECTIONS`, a homepage hook is that module's `HOOK`.

### 7B. Add a new Trojan Horse story

1. **Research first.** Read the primary documents (filings, releases) and note every figure with its source. Note what you could not read. Section 9 has the evidence rules.
2. **Create `weekly_<company>.py`** by copying `weekly_uber.py`. Required names:
   - `WEEK`: the display date, for example `"1 November 2026"`.
   - `SLUG`: the page name without `.html`. It must be unique.
   - `KICKER`: `"Trojan Horse of the Week"`.
   - `TITLE`, written with HTML entities (`&amp;`, `&rsquo;`).
   - `HOOK`: one sentence with a concrete number or tension.
   - `LOGO`: see step 3.
   - `GO`: `(href, label)`, the closing link on the story page. Each story currently links to the previous one.
   - `SECTIONS`: a list of `(heading, [paragraph, ...])`. Paragraphs are raw HTML. An empty heading renders running prose with a larger first paragraph.
   - `NOTE`: the sourcing note under the story. Say where figures come from, what could not be verified, which numbers are your arithmetic, and which people are invented.
3. **Get the logo.** Take it from the company's own site (view source for the header `<svg>` or an `<img src="...svg">`) or from Wikimedia Commons when the site hides it (Uber's header draws its mark in CSS, so its file came from Commons, where it is tagged public domain and flagged as a trademark). Before use, open the file and confirm it contains no `<script>`, no `on...=` handlers, no `<foreignObject>`, no `<image>`, and no external `href` or `url(http`. Save it as `images/logos/<name>.svg` and set `LOGO = {"file": "<name>.svg", "w": <viewBox width>, "h": <viewBox height>, "name": "<Company>", "height": <px>}`. Choose `height` so the rendered width lands near 100 to 135 px (Oura 34, Thorne 20, Uber 34). The mark renders as a single-colour mask, silver on the homepage and navy on the story header, so it never needs recolouring. These are the companies' trademarks, used only to identify the subject.
4. **Register it** in `build-site.py`: add the module to the `import weekly_data, weekly_thorne, weekly_uber` line, and add it to `WEEKLIES` in the position you want on the homepage. Position is the order of the list, not the date.
5. **Build and preview.** Check the homepage card and the story page at about 1280px, 900px and 375px. Below 900px the cards stack.
6. **Audit** with the snippet in section 11.
7. **Commit and push**: the new module, `images/logos/<name>.svg`, `<slug>.html`, `index.html` and `build-site.py`. Then confirm it is live.
8. Optionally point the neighbouring story's `GO` at the new one.

### 7C. Reorder, hide or retire a story

`WEEKLIES` controls both the homepage order and which story pages get rebuilt. Reorder the list to reorder the cards. Removing a story from the list takes it off the homepage and stops rebuilding its page, but the existing HTML stays live, frozen. There is no way yet to rebuild a page without showing it on the homepage. To retire a page fully, `git rm` its HTML, remove it from `WEEKLIES`, and if the URL was ever shared add a redirect (see `build_stories_page` for the pattern).

### 7D. Podcast page

`EPISODES` in `build-site.py` is a list of `(title, blurb, status)`. There is no audio yet and `audio/` is empty. The Spotify mark on the homepage links to `podcast.html`.

### 7E. CSS changes

`site.css` section headers, in file order: TOKENS, COVER, TALE, SPOTIFY, THE BELT, FOOTER, RESPONSIVE, THE PICKER ON THE COVER, SILO HEADER, DEFINITION, PODCAST, FIRST PRINCIPLES, KATABASIS, GROUND FLOOR, THE WHITE PLATE, THE PROCESS RAIL, TROJAN HORSES (older, now unused), THE JOURNAL INDEX, LINE ART, TROJAN HORSES (current). The current homepage stories section is the `.th*` rules, the logo masks are `.th__logo` and `.plate__logo`, and the white story pages use `.plate`, `.white`, `.wp` and `.ch`. The stories stack at a 900px breakpoint. About 76 of 189 class names in `site.css` are used by no built page (see section 12). Check built HTML before deleting any rule.

### 7F. Deal notes, background pages, Palo Alto stories

Each is a dictionary in its data module (`deals_data.py`, `primers_data.py`, `desk_data.py`) with a `slug`, title lines, sections and sources. Prologue entries find their deal note by title through `DEAL_LINKS`. Follow the existing entries for shape, and rebuild.

## 8. Page inventory and how each page is reached

- **Linked from the homepage:** `ten-years.html` (Prologue), `oura-ipo.html`, `thorne-loyalty.html`, `uber-rival-dinner.html`, `tech-atlas.html`, `podcast.html`.
- **Reached from other pages:** `trojan-horses.html` (from the Thorne story), `how-a-company-gets-sold.html` (only from `trojan-horses.html`), the ten deal notes (from Prologue entries), and the Palo Alto pages (reached through the `fetching.html` deal note, then `desk-ddn.html`, then `palo-alto.html`).
- **Live but linked from nowhere:** `the-buyers-bank.html` and the five background pages (`what-a-chip-is.html`, `what-the-cloud-is.html`, `what-ai-needs.html`, `the-building.html`, `what-a-bank-does.html`), plus `404.html`.
- **Redirects:** `strategemata.html`, `horse-credit.html`, `horse-apprenticeship.html`, `katabasis.html`.

## 9. Editorial standards in full

The rules in `CLAUDE.md` are the short version. The detail behind them:

**Structure.** State the thesis early and plainly. Present the prevailing view fairly and name whose view it is. Then give the alternative reading in concrete terms. Each paragraph sets up the next. Make load-bearing assumptions explicit. Use a concrete example for each abstract claim, and label hypotheticals. Address the strongest counterargument and say what evidence would decide it. End with the practical implication.

**Evidence hierarchy.** Use the company's own filings first (S-1, 10-K, 10-Q, 8-K), then releases from the company or its counsel, then established financial press, then trade press. Commentary and aggregators may be cited only with attribution to what they report. Read the document yourself. Summaries have been wrong here: one gave a different use-of-proceeds figure from the filing, one claimed a Customs ruling that could not be confirmed, and the owner's own notes had a claim about Waymo that the record narrows. The SEC pages are huge and the fetch tool truncates near 450,000 characters, so late sections such as the principal and selling stockholders table may be unreachable. Say so when that happens.

**Numbers.** Label your own arithmetic. Give a range when outlets disagree. Never present a figure you did not see in a source.

**Quotes.** At most one direct quote per Trojan Horse story, under about 15 words, attributed and linked. Paraphrase everyone else and link them.

**Privacy.** Do not name private individuals who supplied information for a piece.

**Story register.** See `CLAUDE.md`. The owner rejected two earlier Oura drafts: the first never named the horse, and the second was eleven separate findings that read like a walkthrough of the filing. The accepted version has eight chapters, names the horse early, and follows one idea through the numbers (every dollar in an IPO has a return address).

**Older pages.** The process page, the Prologue, the Palo Alto stories and the Atlas were rewritten in a plainer, argument-first register. The weekly stories are the one place where humor and analogy are wanted.

## 10. Decision log

- **2026-09-28:** the homepage became the Troy myth alone and one story stayed live. Everything else went to the local `archive/`.
- **2026-10-19:** the "Katabasis" ten-year timeline was built with five background pages and ten deal notes, then rewritten in plain prose.
- **2026-10-22:** the Mandate page, the eight-stage process page, the Palo Alto sub-journal and a first Trojan Horses landing were added. All writing was restructured under the owner's rewrite brief (thesis first, source-linked).
- **2026-10-23:** the home essay was reopened at the gates of Troy. The Mandate was merged into the process page as Part One, with a new Part Three on managing directors. The Tech Atlas was cut to nine sectors and every relationship was checked against its source.
- **2026-10-27:** the timeline was stripped to the map alone. The process page was cut back to argument only.
- **2026-10-30:** Trojan Horses was reduced to a single P&G and Thorne piece, then the weekly-story format began with the Thorne loyalty story. The tagline became "Hidden Risks Behind Promising Deals", the homepage drawing was removed, the Troy essay lost one paragraph, and the owner set the standing rule of no sub-descriptions under story titles.
- **2026-10-31:** the Oura story was written and rewritten twice. The Uber story was added. The homepage was rebuilt: the ten-year page was renamed Prologue, the stories moved into a three-column section with one-sentence hooks, Atlas moved under the Spotify mark, and company logos were added to every story.

## 11. Verification and deploy

**Audit the pages you changed** for banned punctuation and quote count:

```bash
python3 - <<'PY'
import re, html, pathlib
PAGES = ["index.html", "oura-ipo.html"]          # list the pages you changed
for f in PAGES:
    t = pathlib.Path(f).read_text(encoding="utf-8")
    m = t[t.index("<main"):t.index("</main>")] if "<main" in t else t
    b = html.unescape(re.sub(r"<[^>]+>", " ", m))
    quotes = len(re.findall("“[^”]+”", b))
    print(f"{f:26} em dashes {b.count(chr(0x2014))} | semicolons {b.count(';')} | question marks {b.count('?')} | direct quotes {quotes}")
PY
```

Em dashes and semicolons should be 0. A story's closing link can contribute a question mark when it points to the Thorne story, whose title ends in one. A story should have 1 direct quote.

**Check internal links:**

```bash
python3 - <<'PY'
import re, pathlib
have = {p.name for p in pathlib.Path(".").glob("*.html")}
bad = [(p.name, h) for p in sorted(pathlib.Path(".").glob("*.html"))
       for h in re.findall(r'href="([^"#?:]+\.html)"', p.read_text(errors="ignore")) if h not in have]
print("broken internal links:", bad or "none")
PY
```

**Confirm a push is live:**

```bash
for i in $(seq 1 30); do
  curl -s https://trojanhorse.blog/<page>.html | grep -q "<a string from your change>" && echo LIVE && break
  sleep 10
done
```

**If it is not live after about 3 minutes**, the Pages build has hung. This has happened, including once for four hours after a machine slept. Check `gh api repos/fyruan-star/trojanhorse-blog/pages/builds/latest --jq .status`, and if it still says `building`, run `gh api -X POST repos/fyruan-star/trojanhorse-blog/pages/builds`. A fresh build normally finishes in about 20 seconds.

## 12. Open items

1. **Domain lock is off.** On 2026-11-02 `whois` showed only `serverTransferProhibited`, and the owner-controlled `clientTransferProhibited` was absent. Turning it on is an owner task at Porkbun. The domain expires 2027-09-27, so confirm auto-renew.
2. **Only one GitHub collaborator.** Add anyone who will publish (section 2).
3. **`archive/` exists only on Francis's Mac.** Back it up if the old pieces matter.
4. **Podcast statuses are stale.** `EPISODES` still says "Recording October" on two entries and "In production" on six. It is now November, and there is no audio.
5. **Standfirsts remain on two pages**, `how-a-company-gets-sold.html` and `trojan-horses.html` (class `plate__l`). The owner's rule is no sub-descriptions, but he only pointed at the weekly stories, so ask before stripping them. The homepage Prologue row also carries the label "2016 to 2026".
6. **Orphaned pages.** The Buyer's Bank and the five background pages have no inbound links. The process page is reachable only through `trojan-horses.html`. The Palo Alto stories are reachable only through the Fetching deal note. Decide whether to relink, redirect or delete.
7. **Stories go stale as events land.** P&G said the Thorne purchase should close in the fourth quarter of 2026. Uber's Delivery Hero offer is expected to close in the second half of 2027 and needs acceptances and clearances. Oura gave no new IPO date and may relaunch. Check each story's facts before promoting it again.
8. **Verification gaps in the current stories.**
   - Oura: the filing's note tying the $985.0 million deemed dividend to a specific repurchase, and its principal and selling stockholders table, were outside the readable part. The WSJ article the owner pointed to could not be found or read, so it is not cited.
   - Thorne: the Flow Space roundup of reactions was seen only through search summaries (it is pay-per-crawl). Reddit blocks automated reading, so there is no post-level evidence and the page says so. A reported "no plans to change formulation" statement could not be confirmed from a readable source and is not used.
   - Uber: the Citizens analyst view is as reported by Parameter, not from the Citizens note. Waymo's goal of one million weekly rides rests on a Bloomberg headline. Only part of the 10-K risk-factor text was read.
9. **Dead CSS.** About 76 of 189 class names in `site.css` are used by no built page: the circular-horse landing (`.horse`, `.pair`), the cover picker (`.silo*`), First Principles (`.fp*`) and `.belt*`. The file has two sections titled TROJAN HORSES, and the older one is dead.
10. **Dead data.** `mandate_data.py`, and `INTRO`, `INTRO_2` and `CLOSE` in `kata_data.py`, are imported but not rendered. The Atlas modules for telecom, foundation, mobility, robotics, health, defense, quantum and energy exist but are not in `_MODULES`. `weekly_data.py` is the Oura story, and renaming it `weekly_oura.py` would match the naming of the others.
11. **Palo Alto sub-journal is unfinished.** Three of the thirteen deals on the BofA Securities Palo Alto software team's list are written. The other ten are not, and the source list is not in the repo.

## 13. Lessons from the build

- Hand-edited HTML is lost on the next build. Always change the source.
- `git add -A` has swept in another session's work. Stage by name.
- A plain string containing `{NAME}` leaked the braces into a page once. Use f-strings only where a line has a placeholder. A bad f-string in a data file also broke a build with a syntax error.
- Shell and Python heredoc checks can report false negatives when the string you test for is not literally in the file. Test the thing itself.
- A long document truncated by a fetch tool looks complete. Check what range you actually read.
- Screenshots lag. Measure.
- The owner reads the live site, so an unpushed change is an invisible one.
