# The Trojan Horse (trojanhorse.blog)

**Before you change anything, read `HANDOFF.md` in full.** It has the current state of the site, which source file feeds which page, and step-by-step procedures. This file holds only the rules that always apply.

An M&A journal by Francis Ruan. Static site on GitHub Pages (branch `main`, folder `/`), repo `fyruan-star/trojanhorse-blog`, domain trojanhorse.blog. Python 3, standard library only.

Start Claude Code **inside this folder**. A `CLAUDE.md` in a subfolder loads only after Claude reads a file there, and project memory is keyed to the git repo, so a session started in a parent folder will not see this guidance up front.

## The rule that matters most: the HTML is generated

Every page in the repo root except `404.html` is written by `python3 build-site.py` from data modules (`*_data.py`, `weekly_*.py`) and from templates inside `build-site.py`. A hand edit to generated HTML is overwritten by the next build.

Hand-editable files: `site.css`, `story.css`, `atlas.css`, `atlas.js`, `404.html`, `images/`, `CNAME`.

To change the live site:

1. Edit the source. `HANDOFF.md` section 6 maps each page to its source.
2. Run `python3 build-site.py`.
3. Preview with `python3 -m http.server 8731` and open http://localhost:8731/ (add `?v=2` to bypass cached CSS). Check about 1280px, 900px and 375px wide.
4. Audit the changed pages (snippet in `HANDOFF.md` section 11).
5. Run `git status`. Stage the source files and the regenerated HTML **by name**, never `git add -A`, because another person or session may have uncommitted work in the same folder. Commit.
6. `git push origin main`.
7. Confirm it is live: curl the page for a string from your change. Pages normally publishes in 20 to 90 seconds. If it is not live after 3 minutes the build has hung, and `gh api -X POST repos/fyruan-star/trojanhorse-blog/pages/builds` requests a fresh one.

The owner wants every change pushed and confirmed live without waiting for approval. Ask first only before anything destructive: deleting pages or history, force-pushing, or changing DNS or Pages settings.

## Editorial rules for all prose on the site

- Thesis early and stated plainly. State the prevailing view fairly and attribute it, and never invent a consensus. Build step by step, make assumptions explicit, give a concrete example for each abstract claim, label hypotheticals and invented people, answer the strongest counterargument, end on a practical implication, and put source links beside the claims they support.
- Banned: em dashes (U+2014), semicolons in prose, rhetorical questions, contrast constructions ("It wasn't X. It was Y", "not X but Y"), theatrical fragments, slogans and one-line dramatic closers, sentences that announce the writing or perform humility, "here is the part that..." phrasing, and decorative language. A question mark is fine in a story title.
- Quotes: few, short, verified, attributed and linked, primary sources first. Never invent a quote or present a paraphrase as one. Trojan Horse stories use at most one direct quote, so paraphrase and link everyone else.
- Never state a figure that is not in a source you actually read. Prefer filings and company releases over summaries, which have been wrong here more than once. Label your own arithmetic ("by my arithmetic"). Say when outlets disagree. If a source cannot be read (paywall, bot block), do not cite it for claims, and say so.
- When the owner's notes contradict the sources, write what the sources show and tell him in your reply.
- Do not name private individuals who supplied information.

## Trojan Horse of the Week stories (`weekly_*.py`)

- Name the horse early, in the story's own words: what is welcomed, who welcomes it, why it looks like a gift, what rides inside, how it harms. Then tell it as a story whose chapters open on an image, not as a list of findings.
- Register: a dated scene opening ("Picture the morning of..."), first person, warm, dry humor carried by a concrete image, and a labelled analogy where an abstraction would sit. Never disparage the company the story is about.
- No standfirst or sub-description under any title.
- `HOOK` is exactly one sentence with a concrete number or a tension and no cliche. It is the only text on the homepage card besides the headline.
- Every story carries the subject company's logo (`LOGO`, file in `images/logos/`).
- Homepage card order is the order of `WEEKLIES` in `build-site.py`, not date order.
- Full procedure: `HANDOFF.md` section 7B.

## Gotchas that have already cost time

- `HEAD.format(...)` builds every page title and description, so never put `{` or `}` in them.
- In data modules use an f-string only on lines that contain a placeholder. A plain string holding `{NAME}` leaks the braces into the page.
- Prose strings are inserted as raw HTML. Write `&rsquo;`, `&amp;`, `&ldquo;`, `&rarr;`.
- The repo is public and `.nojekyll` is set, so every committed file is served. Never commit secrets, private notes or personal data. `archive/` is git-ignored and local only.
- Run scripts with plain `python3`. The `-I` flag removes the script folder from the import path and breaks the local modules.
- Browsers cache `site.css`, so add `?v=N` to the preview URL. Screenshots can lag behind scrolling, so measure with DOM queries (widths, positions) before trusting a picture.

## Working with the owner

- No em dashes in replies either.
- Lead with what changed and what you verified. State plainly what you could not verify and what you left out.
- If a request rests on a premise the sources do not support, say so and show the source.
