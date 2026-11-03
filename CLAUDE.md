# The Trojan Horse (trojanhorse.blog)

**Before you change anything, read `docs/HANDOFF.md` in full.** It has the current state of the site, which file feeds which page, and step-by-step procedures. This file holds only the rules that always apply.

An M&A journal by Francis Ruan, Ryan Chian and Timothy Zhang. Repo `fyruan-star/trojanhorse-blog` (public), domain trojanhorse.blog. Python 3, standard library only. Start Claude Code **inside this folder** so this file loads.

## How the site gets built

- `content/` holds every word. `assets/` holds CSS, JavaScript, images, logos, `404.html` and `CNAME`. `build.py` reads both and writes the whole site into `_site/`.
- `_site/` is git-ignored. Never commit built HTML, and never edit it, because the next build replaces it.
- `.github/workflows/publish.yml` runs `python3 build.py` on GitHub for every commit to `main` and publishes `_site/` to Pages. Pull requests are built but not published.

To change the live site:

1. Edit a file in `content/` or `assets/` (`docs/HANDOFF.md` section 6 maps pages to files).
2. Preview: `python3 build.py && python3 -m http.server -d _site 8731`, then open http://localhost:8731/ (add `?v=2` to bypass cached CSS). Check about 1280px, 900px and 375px wide.
3. Audit the changed pages (snippet in `docs/HANDOFF.md` section 11).
4. Run `git status`. Stage files **by name**, never `git add -A`, because another person or session may have work in the same folder. Commit and `git push origin main`.
5. Watch the build with `gh run watch` (or the Actions tab), then curl the live page for a string from your change. A red build leaves the previous site live. Fix and push again. To republish without a change, run `gh workflow run publish.yml`.

The owner wants every change pushed and confirmed live without waiting for approval. Ask first only before anything destructive: deleting content or history, force-pushing, or changing DNS, Pages or repository settings.

## Editorial rules for all prose on the site

- Thesis early and stated plainly. State the prevailing view fairly and attribute it, and never invent a consensus. Build step by step, make assumptions explicit, give a concrete example for each abstract claim, label hypotheticals and invented people, answer the strongest counterargument, end on a practical implication, and put source links beside the claims they support.
- Banned: em dashes (U+2014), semicolons in prose, rhetorical questions, contrast constructions ("It wasn't X. It was Y", "not X but Y"), theatrical fragments, slogans and one-line dramatic closers, sentences that announce the writing or perform humility, "here is the part that..." phrasing, and decorative language. A question mark is fine in a story title.
- Quotes: few, short, verified, attributed and linked, primary sources first. Never invent a quote or present a paraphrase as one. Trojan Horse stories use at most one direct quote, so paraphrase and link everyone else.
- Never state a figure that is not in a source you actually read. Prefer filings and company releases over summaries, which have been wrong here more than once. Label your own arithmetic ("by my arithmetic"). Say when outlets disagree. If a source cannot be read (paywall, bot block), do not cite it for claims, and say so.
- When the owner's notes contradict the sources, write what the sources show and tell him in your reply.
- Do not name private individuals who supplied information.

## Trojan Horse stories (`content/stories/`)

- **Length: under 1,200 words including the `NOTE`, aiming for 800 to 1,000.** Every paragraph must advance the argument. Cut company descriptions that do not support the thesis, repeated caveats and unsupported numbers. Count with the snippet in `docs/HANDOFF.md` section 11.
- **Opening:** start with a familiar, concrete observation that raises the business question at once. Never open with "Picture the morning", an invented character, or a date and time. Example: "Walk into a grocery store and count the things promising protein... The interesting question is what the customer buys next."
- Name the horse early and briefly (what is welcomed, what rides inside), then spend the words on the argument. Do not build or explain an extended metaphor.
- Register: direct, vivid and conversational, first person, short paragraphs, a few useful subheadings. Explain sequences through customer decisions and business incentives. Keep what the evidence shows separate from what founders or companies are betting on, and label proposed features as proposals. Never disparage the company the story is about.
- No standfirst or sub-description under any title.
- `HOOK` is exactly one sentence with a concrete number or a tension and no cliche. It is the only text on the homepage card besides the headline.
- Every story carries the subject company's logo (`LOGO`, file in `assets/images/logos/`).
- Homepage order is `STORIES` in `content/home.py`, not date order.
- Full procedure: `docs/HANDOFF.md` section 7B.

## Gotchas that have already cost time

- `HEAD.format(...)` builds every page title and description, so never put `{` or `}` in them.
- In content files use an f-string only on lines that contain a placeholder. A plain string holding `{NAME}` leaks the braces into the page.
- Content strings are inserted as raw HTML. Write `&rsquo;`, `&amp;`, `&ldquo;`, `&rarr;`. A straight double quote inside a double-quoted string breaks the build.
- The repo is public, so never commit secrets, private notes or personal data. `archive/` is git-ignored and exists only on the owner's Mac.
- Run scripts with plain `python3`. The `-I` flag removes the script folder from the import path.
- Browsers cache `site.css`, so add `?v=N` to the preview URL. Screenshots can lag behind scrolling, so measure with DOM queries before trusting a picture.

## Working with the owner

- No em dashes in replies either.
- Lead with what changed and what you verified. State plainly what you could not verify and what you left out.
- If a request rests on a premise the sources do not support, say so and show the source.
