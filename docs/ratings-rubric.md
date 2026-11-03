# Tech Atlas ratings rubric

Every company in the Atlas can carry an overall rating, OVR, from 40 to 99, in the style of an NBA 2K player rating. OVR is a reading of the evidence already in the Atlas, never new research. It answers one question: how much does this company matter in the row where it plays, today?

The ratings live in `content/atlas/atlas.json` on each company. The validator (`python3 scripts/validate_atlas.py`) checks every rule below that a machine can check.

## The tiers

| OVR | Tier | What it means |
| --- | --- | --- |
| 95 to 99 | Generational | A chokepoint the whole industry depends on. Removing it would stall its row and the rows that buy from it. |
| 90 to 94 | Superstar | Leads its row by a wide margin and sets the terms others follow. |
| 85 to 89 | All-Star | A clear leader or co-leader, with scale that rivals cannot match quickly. |
| 80 to 84 | Starter | A leader in its row, with credible rivals close behind. |
| 75 to 79 | Rotation | A strong number two or a leader of a smaller niche. |
| 70 to 74 | Role player | Scaled and relevant, without pricing power over its row. |
| 60 to 69 | Bench | A real business whose position depends on events it does not control. |
| 40 to 59 | Prospect | Early, small or unproven. The rating is mostly about what has to happen next. |

## How a score is built

Start from the company's place on the depth chart, then adjust.

1. **Position and scale in its row.** The rank sets the starting band. A starter usually sits from 80 to 99, a second-string player from 68 to 86, and a practice-squad player from 45 to 75. Within the band, the key figure decides: share of the row, revenue against the row's headline metric, or the size of the commitment behind it.
2. **Momentum, up to 4 points either way.** Growth against peers in the same row. A segment growing 117% year on year beside peers growing 25% earns the points. A company losing share loses them.
3. **Leverage, up to 5 points up.** How much others depend on it. A sole supplier, a licence most of the row needs, or a platform its rivals buy from earns the most.
4. **Exposure, up to 6 points down.** Customer concentration, debt, regulatory or legal risk named in the card's "what could change it" line, and dependence on a single deal that has not closed.

A company with cards in more than one row is rated on its strongest card, and the reason names that row.

Companies that appear only as owners or backers have no card, so they stay unrated (`"ovr": null`).

## The fields

| Field | Rule |
| --- | --- |
| `ovr` | A whole number from 40 to 99, or `null` for unrated. |
| `ovr_status` | `"draft"` until a person has checked it, then `"reviewed"`. |
| `ovr_reason` | One sentence that names the figure or fact the score rests on. House style applies: no em dashes, semicolons or question marks. |
| `ovr_evidence` | A list of `{"url": ..., "trust": ...}`. Use the source of the card or relationship the reason cites, with its trust tag (`sourced`, `reported` or `inferred`). |
| `ovr_updated` | The date the rating last changed, as `2026-11-02`. |
| `ovr_by` | Who set it. Drafts written by Claude say `"Claude (draft)"`. A reviewer replaces this with their own name. |

Reserved for later, and already allowed by the validator: `attributes` (sub-ratings such as scale or momentum), `badges` (a list of short labels) and `ovr_history` (earlier ratings, each `{"ovr": ..., "date": ..., "by": ..., "note": ...}`).

## Evidence rules

- Use only facts already in the Atlas: the card's key figure, why it leads, what could change it, the row's headline metric, and the company's relationships.
- Quote figures exactly as the Atlas states them, with the period they cover.
- Never introduce a number that is not in the Atlas. To use a new fact, add it to the card first, with its source.

## Reviewing a draft

1. Read the reason and open the evidence link.
2. Change `ovr` if you disagree, and rewrite the reason so it still names the figure.
3. Set `ovr_status` to `"reviewed"`, `ovr_by` to your name and `ovr_updated` to today.
4. If a reviewed rating changes later, add the old one to `ovr_history` first.

## Showing or hiding drafts

`SHOW_DRAFT_RATINGS` at the top of `content/atlas/atlas_data.py` controls the public site. When it is `False`, the build removes every draft rating from `tech-atlas.html` and `tech-atlas.json`, and only reviewed ratings are published. When it is `True`, drafts are published and labelled DRAFT on every card.
