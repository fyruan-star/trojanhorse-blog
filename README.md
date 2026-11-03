# The Trojan Horse

The website at **https://trojanhorse.blog**. Every change committed here goes live by itself in about two minutes.

## Change something

1. Open the file from the table below, here on GitHub.
2. Click the **pencil icon**, change the words, then click **Commit changes**.
3. Wait two minutes and refresh the site.

| To change | Open |
| --- | --- |
| Homepage tagline, essay, story order, podcast list | `content/home.py` |
| A Trojan Horse story | `content/stories/` |
| The Prologue timeline | `content/prologue.py` |
| The Tech Atlas: companies, relationships, ratings | `content/atlas/atlas.json` (see below) |
| A company stats page (NBA-style) | words in `content/companies/<name>.py`, numbers in `<name>.json` (run `python3 scripts/fetch_company.py <name> <SEC CIK>` to refresh them) |
| Any other page | `content/` (file names match the pages) |
| Colours, fonts, layout | `assets/site.css` |
| Images and logos | `assets/images/` |

Change only the words inside the quotation marks. Keep tags such as `<p>` and `<a href="...">`. Write `&rsquo;` for an apostrophe, `&amp;` for &, and `&ldquo;` `&rdquo;` for quotation marks.

## Add a story

1. Copy `content/stories/uber.py` to `content/stories/yourname.py` and replace its words.
2. Put the company logo in `assets/images/logos/` and update `LOGO` in your file.
3. Add `"yourname"` to `STORIES` in `content/home.py`.

## Edit the Tech Atlas

Every company, card, relationship and rating lives in `content/atlas/atlas.json`. The List and the Map are both built from it.

- **A company** is an entry under `companies`: `name`, `description`, `sector` (its home on the map; `backers` for an owner or investor with no card) and its rating fields.
- **A card** (a company's place in a sector) is an entry in `placements`: `company`, `sector`, `row`, `rank` (`starter`, `second_string` or `practice_squad`), an optional `label` such as `newly public`, then `key_figure`, `why`, `could_change`, `source` and `trust` (`sourced` or `reported`).
- **A relationship** is an entry in `relationships`: `from`, `to`, `type` (`alliance`, `supply`, `license`, `dependency`, `rivalry`, `ownership` or `investment`), `text`, `source`, `trust`, `date` and `added`. For ownership and investment, `from` is the owner or backer.
- **Ratings** are six attributes under `attributes`: `dominance`, `momentum`, `leverage`, `durability`, `firepower` and `deal_heat`. Each has `value` (40 to 99, or `null` for unrated), a one-sentence `reason`, `evidence` (links with their trust tag) and `status` (`draft` or `reviewed`). Leverage stores `adjust` instead of `value`, because the build adds it to a base worked out from the relationships. OVR is calculated from the six, never typed in. `ovr_reason` is the headline sentence on the card.
- **Badges.** Chokepoint and Kingmaker are calculated. Single-Customer Risk and In Play are listed under `badges` as `{"id": "in_play", "reason": ..., "evidence": [...], "status": "draft"}`.
- **Profile extras**, all optional. `bio` on a company holds `ticker`, `listed` (`Public` or `Private`), `hq`, `founded` and `ceo`, each with its link in `bio.sources`. Fill a field only from a page you read, and the profile shows only the filled ones. `stats` on a card holds three or four `{"label", "value"}` headline numbers for the profile, and each value must already be in that card's `key_figure`.
- **Logos.** `logo` on a company is `{"file", "kind", "source", "license"}` for an official file in `assets/logos/` (`kind` is `simple-icons`, `commons` or `press-kit`), with `"ground": "dark"` for a white mark. A company without one gets an initials monogram in its sector colour. Never draw or alter a logo.
- **Teams** are listed under `teams` (`id`, `name`, `captains`). The build places every company by the rules in `docs/ratings-rubric.md`. To move a company, give it `team` (a team id, or `independent`) and a one-sentence `team_reason`. The build fails on an even tie until one is set.
- The weights, what each level means, the team rules and how to review a draft are in `docs/ratings-rubric.md`.

Run `python3 scripts/validate_atlas.py` after an edit. GitHub runs the same checks, so a mistake shows a red X instead of reaching the site.

**Draft ratings.** Attributes and badges marked `"status": "draft"` are labelled DRAFT on the site. To hide every draft attribute, badge and the OVRs built from them, set `SHOW_DRAFT_RATINGS = False` near the top of `content/atlas/atlas_data.py`.

**Linking into the Atlas.** Every company has a profile page, such as `atlas/oracle.html`, which is the link to use from a story. `tech-atlas.html#c-oracle` opens the map with Oracle in the spotlight, `#s-silicon` opens a sector and `#t-nvidia` lights up a team. Sector standings are at `atlas/sector-<id>.html` and teams at `atlas/teams.html`. Company ids are the keys under `companies`.

**Browser checks.** `node scripts/check_atlas_map.mjs` drives the map and the new pages in Chromium and WebKit against a local preview (it needs the `playwright` package, which the build does not).

## If the site did not update

Open the **Actions** tab. A red ✗ means the edit broke the build. Click it to read the error, fix the file, and commit again. The site keeps showing the last good version until then.

## No edit access?

Click the pencil anyway. GitHub turns your edit into a pull request, and the owner publishes it.

---

House style and sourcing rules: `CLAUDE.md`. Full guide: `docs/HANDOFF.md`. Preview on your own computer (optional): `python3 build.py && python3 -m http.server -d _site 8731`. Tests: `python3 -m unittest discover tests` and `node --test`.
