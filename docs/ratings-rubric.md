# Tech Atlas ratings rubric

Every company with a card in the Atlas is rated like an NBA 2K player: six attributes from 40 to 99, an overall rating (OVR) calculated from them, and badges. Ratings are a reading of the evidence already in the Atlas, never new research.

Everything lives on the company in `content/atlas/atlas.json`. The build calculates OVR, Leverage and the rule-based badges, and `python3 scripts/validate_atlas.py` checks every rule below that a machine can check.

## The six attributes

Each attribute is a whole number from 40 to 99, or `null` when the Atlas does not hold the facts to rate it. An unrated attribute shows as "unrated" on the card. It is never guessed.

### Dominance: share and scale in its row

| Value | Meaning |
| --- | --- |
| 95 to 99 | Sole supplier, or a majority share of its row (above about 60%). |
| 85 to 94 | The clear leader of its row by share or revenue. |
| 75 to 84 | A co-leader, or a strong number two with a stated share. |
| 65 to 74 | A scaled participant without a leading share. |
| 55 to 64 | A small stated share, or a niche position. |
| 40 to 54 | Early: no share, or pre-revenue. |

Without a share or scale figure, the depth-chart rank sets the range: a starter 76 to 84, a second-string player 64 to 75, a practice-squad player 48 to 63.

### Momentum: growth against peers

| Value | Meaning |
| --- | --- |
| 95 to 99 | Growth of 100% or more a year at scale, or share gains that lead the row. |
| 85 to 94 | Growth of 50% to 100%, or clear share gains. |
| 75 to 84 | Growth of 20% to 50%. |
| 65 to 74 | Growth below 20%. |
| 55 to 64 | Flat. |
| 40 to 54 | Shrinking, or losing share. |

Null when the Atlas gives no growth figure and no stated direction.

### Leverage: how much others depend on it

Leverage is partly calculated from the Atlas network and then adjusted by judgment.

1. **Network base.** Count the distinct companies that depend on this one, from three kinds of relationship:
   - `supply`: the `to` company depends on the `from` company (the buyer on its supplier);
   - `license`: the `from` company depends on the `to` company (the licensee on the licensor);
   - `dependency`: the `from` company depends on the `to` company.

   Alliances, rivalries, ownership and investment do not count, because capital and partnership are not dependence. Companies on the owners-and-backers island (sector `backers`) are left out entirely, so a fund that owns many companies does not inflate anyone's score. The base is `50 + 8 × dependents`, capped at 82.
2. **Judgment.** The stored `adjust` (from −15 to +45) moves the base for what the network cannot see, such as "the only maker of EUV machines" or "collects a royalty on most chips outside PCs". Its `reason` names that fact.

   The Atlas draws only the relationships a source states, about two dozen of them supply, licence or dependency lines, so on 2 November 2026 the base was 50 for 116 of the 132 rated companies, 58 for 9 and 66 for 7. The network therefore sets a floor and rewards stated dependence, and the cited judgment does most of the work. The range is wide enough that a chokepoint the network barely shows can still reach the top tier, and the reason must say why.

The final value is `base + adjust`, held between 40 and 99. In `atlas.json` Leverage stores `adjust`, `reason`, `evidence` and `status`, and the build fills `value`.

| Value | Meaning |
| --- | --- |
| 95 to 99 | A chokepoint: the row, and the rows that buy from it, cannot work without it. |
| 85 to 94 | Most of its row depends on it. |
| 75 to 84 | A key supplier or licensor to several companies. |
| 60 to 74 | Some companies depend on it. |
| 40 to 59 | No stated dependence on it. |

### Durability: resistance to concentration, debt and regulation (higher is safer)

| Value | Meaning |
| --- | --- |
| 95 to 99 | No named exposure, and a diversified business. |
| 85 to 94 | A minor named risk. |
| 75 to 84 | A named risk it can absorb, such as share pressure from a rival. |
| 65 to 74 | A meaningful concentration, legal case or regulatory review. |
| 55 to 64 | A single customer near half its business, heavy debt, or a deal that has not closed. |
| 40 to 54 | A risk that could end the business as it stands. |

The card's "what could change it" line is the usual evidence.

### Firepower: cash and balance sheet to spend or invest

| Value | Meaning |
| --- | --- |
| 95 to 99 | Stated commitments or investments of tens of billions of dollars. |
| 85 to 94 | Stated commitments of $10bn or more, or very large stated profit or cash. |
| 75 to 84 | A raise or stated investment of $1bn to $10bn. |
| 65 to 74 | A raise of $100m to $1bn. |
| 55 to 64 | A small raise. |
| 40 to 54 | Stated losses with a stated need for funding. |

Revenue alone is not Firepower. Null unless the Atlas states cash, a raise, profit, debt or a spending commitment.

### Deal Heat: likelihood of buying, selling or being bought soon

| Value | Meaning |
| --- | --- |
| 95 to 99 | An agreed deal that has not closed, or an announced takeover. |
| 85 to 94 | Reported talks, or an IPO filing. |
| 75 to 84 | Reported preparation: advisers, a planned listing, or a stated search for deals. |
| 60 to 74 | A deal closed recently, with more stated as likely. |

Null when the Atlas reports no deal activity. Null means "nothing reported", which is not the same as "cold".

## OVR

OVR is calculated, never typed in.

| Attribute | Weight |
| --- | --- |
| Dominance | 30% |
| Leverage | 25% |
| Momentum | 15% |
| Durability | 15% |
| Firepower | 15% |
| Deal Heat | 0% |

`OVR = 0.8 × weighted average + 0.2 × the higher of Dominance and Leverage`, rounded and held between 40 and 99.

**Why these weights.** OVR answers how much a company matters in its row today. Position (Dominance) and how much others need it (Leverage) answer that most directly, so they carry over half. Momentum, Durability and Firepower describe where the position is heading and how well it can be defended, so they share the rest equally. Deal Heat is shown on the card but weighted at zero, because being in play is a situation, not a strength: a company can be in play because it is strong or because it is struggling.

**Why the peak term.** A plain average squeezes the top. ASML, the only maker of EUV machines, would land near 88 because its growth is ordinary. In 2K an elite specialist outranks a player who is average at everything, and the 20% peak term does the same here: it lets a true chokepoint or a dominant leader reach the top tiers.

**Missing attributes.** When an attribute is unrated, the weights are rescaled over the rated ones. OVR needs Dominance, Leverage and Durability at the least, and is unrated without them. The card says how many of the six it rests on.

**Status.** OVR counts as a draft when any attribute it uses is a draft.

### Tiers

| OVR | Tier |
| --- | --- |
| 95 to 99 | Generational: a chokepoint the whole industry depends on |
| 90 to 94 | Superstar |
| 85 to 89 | All-Star |
| 80 to 84 | Starter |
| 75 to 79 | Rotation |
| 70 to 74 | Role player |
| 60 to 69 | Bench |
| 40 to 59 | Prospect, or unproven |

## Badges

| Badge | Rule | How it is set |
| --- | --- | --- |
| Chokepoint | Leverage of 92 or more | Calculated by the build |
| Kingmaker | Owns or backs three or more companies in the Atlas (`ownership` or `investment` from it) | Calculated by the build |
| Single-Customer Risk | The Atlas states one customer is about 25% or more of its revenue, backlog or contracted revenue | Stored in `badges`, with a reason and evidence |
| In Play | Reported deal talks, an agreed deal that has not closed, or an IPO filing or stated preparation | Stored in `badges`, with a reason and evidence |

Calculated badges follow from the data, so their status follows the attribute or relationships they come from.

## The fields

```json
"oracle": {
  "name": "Oracle",
  "description": "...",
  "sector": "cloud",
  "ovr_reason": "One headline sentence for the card.",
  "attributes": {
    "dominance":  {"value": 78, "reason": "...", "evidence": [{"url": "https://...", "trust": "sourced"}], "status": "draft"},
    "momentum":   {"value": 95, "reason": "...", "evidence": [...], "status": "draft"},
    "leverage":   {"adjust": 10, "reason": "...", "evidence": [...], "status": "draft"},
    "durability": {"value": 58, "reason": "...", "evidence": [...], "status": "draft"},
    "firepower":  {"value": null, "reason": "The Atlas states no cash, raise or commitment.", "evidence": [], "status": "draft"},
    "deal_heat":  {"value": null, "reason": "The Atlas reports no deal activity.", "evidence": [], "status": "draft"}
  },
  "badges": [
    {"id": "single_customer_risk", "reason": "...", "evidence": [...], "status": "draft"}
  ],
  "ovr_updated": "2026-11-02",
  "ovr_by": "Claude (draft)"
}
```

- Every rated attribute needs a one-sentence `reason` that names the fact or figure it rests on, and at least one `evidence` link with its trust tag (`sourced`, `reported` or `inferred`). An unrated one keeps a short reason saying what is missing.
- `ovr_reason` is the headline sentence under the OVR. House style applies to every reason: no em dashes, semicolons or question marks.
- Reserved for later: `ovr_history` (earlier ratings, each `{"ovr", "date", "by", "note"}`).

## Evidence rules

- Use only facts already in the Atlas: the card's key figure, why it leads, what could change it, the row's headline metric, and the company's relationships.
- Quote figures exactly as the Atlas states them, with their period.
- Never introduce a number that is not in the Atlas. To use a new fact, add it to the card first, with its source.

## Reviewing a draft

1. Read the reason and open the evidence link.
2. Change the value (or `adjust` for Leverage) if you disagree, and rewrite the reason so it still names the fact.
3. Set the attribute's `status` to `"reviewed"`. Do the same for each badge you agree with, and delete any you do not.
4. Set `ovr_by` to your name and `ovr_updated` to today. If a reviewed rating changes later, add the old OVR to `ovr_history` first.

## Teams

A team is an ecosystem: companies tied together by ownership, backing and major partnerships, usually across sectors. Teams are worked out by `content/atlas/atlas_teams.py` from the relationships already in the Atlas. They are never a judgment of quality.

### How a company joins a team

The rules run in this order:

1. **Captains.** Each team under `teams` names its captains, the companies it is built around. The first is the captain and any others are co-captains. A company can captain only one team.
2. **Overrides.** A company's own `team` field (a team id, or `independent`) settles its place, with a one-sentence `team_reason`. Captains cannot be moved.
3. **Ownership.** A company owned by a captain joins that captain's team. Ownership beats every other tie.
4. **Direct ties to captains.** Otherwise each direct tie to a captain scores points for that captain's team: backing from the captain (an `investment` line from it) 10, `supply` 3, `alliance` 3, `license` 2 and `dependency` 2. Rivalry scores nothing. Capital counts only for the company that receives it, so investing in a captain does not put a fund on its team. Ties to co-captains add up. The highest score wins.
5. **Once removed.** A company owned by a member placed by rules 1 to 4 joins its owner's team. The rule goes one step only.
6. **Independent.** Any other company is independent.

Only direct ties count. When ties were allowed to chain through members, almost every company ended up on one 23-company team, because the Atlas network is small and dense around a few hubs.

An even score between two teams, or owners on two teams, is a **tie**. `python3 scripts/validate_atlas.py` fails the build until the company has a `team` override, so a tie is always settled by a person with a written reason. A team also needs at least three members.

### The teams on 3 November 2026

| Team | Captains | Other members | Team OVR (draft) |
| --- | --- | --- | --- |
| Google | Google | Broadcom, Samsung, Wiz, Elementl Power | 86 |
| Nvidia | Nvidia | TSMC, Intel, VAST Data, Groq, Safe Superintelligence | 83 |
| Microsoft and OpenAI | Microsoft, OpenAI | CoreWeave, AMD, Shopify, Oracle, Nebius, Constellation, Cerebras | 81 |
| Amazon and Anthropic | Amazon, Anthropic | Cursor, X-energy, Talen | 75 |
| Meta | Meta | EssilorLuxottica, TerraPower, Oklo | 68 |

Settled by hand:

- **AMD** to Microsoft and OpenAI: its 6 GW supply agreement with OpenAI is larger than the up to 2 GW it agreed with Anthropic.
- **Broadcom** to Google: it builds Google's TPUs in volume under a long-term agreement, while its OpenAI accelerators rest on a term sheet.
- **Nebius** to Microsoft and OpenAI: its Microsoft contract of about $17.4bn is larger than the $12bn it agreed with Meta.
- **TikTok US** independent: Oracle's 15% stake would put it on Microsoft and OpenAI under rule 5, but ByteDance keeps the largest stated stake, 19.9%, and ByteDance is on no team.

TSMC joins Nvidia under rule 4, because Apple, its other large customer, captains no team. 115 of the 144 companies are independent, because the Atlas draws only the relationships a source states.

### Team OVR

Team OVR is the **starting five**: the five highest member OVRs, weighted 30%, 25%, 20%, 15% and 10%, rounded. A team with fewer than five rated members rescales the weights over the members it has. Unrated members do not count. It rewards depth, so a team with one superstar and a thin roster can score below a team of solid starters. Team OVR counts as a draft when any of its five rests on a draft.

## Sector standings

Each sector's standings page ranks the companies placed in it by OVR. Equal OVRs share a rank and are listed by name. A company placed in two rows of one sector appears once, at its best depth. Unrated companies are listed under the table, never ranked. The change column compares OVR with the last entry in `ovr_history`. It shows a dash until a company has one.

## Showing or hiding drafts

`SHOW_DRAFT_RATINGS` at the top of `content/atlas/atlas_data.py` controls the public site. When it is `False`, the build removes every draft attribute, every draft badge, any OVR that rests on a draft, and the headline sentence of any company left without a published rating, from both `tech-atlas.html` and `tech-atlas.json`. When it is `True`, drafts are published and labelled DRAFT.
