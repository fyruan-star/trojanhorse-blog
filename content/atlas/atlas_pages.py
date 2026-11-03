"""Tech Atlas pages: a profile for every company, standings for every sector, and teams.

build.py calls write_all() with its page templates. Every page lives in
_site/atlas/, one folder down, so links climb with ../. All Atlas text is
escaped here, because atlas.json holds plain text.
"""
import html, math, re
from dataclasses import dataclass

import atlas_teams as TM

SITE = "https://trojanhorse.blog"
SHORT = (("dominance", "DOM"), ("momentum", "MOM"), ("leverage", "LEV"),
         ("durability", "DUR"), ("firepower", "FIRE"), ("deal_heat", "HEAT"))
RANK_NAME = {"starter": "Starter", "second_string": "Second string", "practice_squad": "Practice squad"}
WHY_LABEL = {"starter": "Why it leads", "second_string": "Why it may rise", "practice_squad": "Why it matters"}
GROUP_LABEL = {"allies": "Allies and partners", "rivals": "Rivals", "backers": "Owners and backers"}
VERB = {"ownership": ("owns", "owned by"), "investment": ("funds", "funded by")}
ROLE_LABEL = {"captain": "Captain", "co-captain": "Co-captain", "owned": "Owned by {via}", "backed": "Backed by {via}",
              "supplier": "Supplier to {via}", "customer": "Customer of {via}", "licensee": "Licenses from {via}",
              "licensor": "Licensor to {via}", "dependent": "Depends on {via}", "relied-on": "Relied on by {via}",
              "partner": "Partner of {via}", "override": "Placed by hand"}
BIO_LABEL = (("ticker", "Ticker"), ("listed", "Listed"), ("hq", "HQ"), ("founded", "Founded"), ("ceo", "CEO"))
RADAR_FLOOR = 0.12
MAX_STATS = 4
# an amount worth a headline: money, a percentage or a quantity with its unit
AMOUNT = re.compile(r"(?:[-+−]?[$€£]\d[\d,]*(?:\.\d+)?(?:\s?(?:bn|tn|m|k))?"
                    r"|\d[\d,]*(?:\.\d+)?\s?(?:%|GW|MW|bn|tn))")
SENTENCE = re.compile(r"(?<=\.)\s+(?=[A-Z])")


def esc(s):
    return html.escape(str(s), quote=True)


def host(url):
    h = re.sub(r"^https?://(www\.)?", "", url).split("/")[0]
    return h or "source"


@dataclass(frozen=True)
class Context:
    """Everything the pages read, gathered once from atlas_data."""
    head: str
    foot: str
    data: dict
    companies: dict
    resolved: dict
    sector_name: dict
    sector_blurb: dict
    row_name: dict
    placements: dict
    edges: list
    group: dict
    members: dict
    rosters: list
    team_name: dict
    standings: dict
    on_map: frozenset
    tiers: tuple


def context(AD, head, foot):
    data = AD.DATA
    sectors = data["sectors"]
    placements = {}
    for p in data["placements"]:
        placements.setdefault(p["company"], []).append(p)
    # the home sector's card comes first
    for cid, ps in placements.items():
        home = data["companies"][cid]["sector"]
        ps.sort(key=lambda p: p["sector"] != home)
    ovr_of = lambda k: AD.RESOLVED.get(k, {}).get("ovr")
    status_of = lambda k: AD.RESOLVED.get(k, {}).get("ovr_status")
    rosters = TM.rosters(data, ovr_of, status_of)
    return Context(
        head=head, foot=foot, data=data, companies=dict(data["companies"]), resolved=AD.RESOLVED,
        sector_name={**{s["id"]: s["name"] for s in sectors}, "backers": "Owners and backers"},
        sector_blurb={s["id"]: s["blurb"] for s in sectors},
        row_name={(s["id"], r["id"]): r["name"] for s in sectors for r in s["rows"]},
        placements=placements, edges=AD.EDGES, group=AD.GROUP, members=TM.assign(data)["members"],
        rosters=rosters, team_name={t["id"]: t["name"] for t in rosters},
        standings={s["id"]: TM.standings(data, s["id"], ovr_of) for s in sectors},
        on_map=frozenset(set(AD.HOME) | set(AD.BACKERS)), tiers=tuple(AD.OVR_TIERS))


# ------------------------------------------------------------------ small parts
def initials(name):
    """Two letters for a monogram, the same rule as the map's (atlas-map-core.js)."""
    words = [w for w in re.split(r"[\s&]+", re.sub(r"\(.*?\)", " ", name)) if w]
    s = words[0][0] + words[1][0] if len(words) > 1 else words[0][:2]
    return s.upper()


def logo_html(ctx, cid, size, alt=""):
    """The company's official mark in a round badge, or its initials in the sector colour."""
    c = ctx.companies[cid]
    logo = c.get("logo")
    if logo:
        ground = "lg--dark" if logo.get("ground") == "dark" else "lg--light"
        return (f'<span class="lg lg--{size} {ground}"><img src="../logos/{esc(logo["file"])}" alt="{esc(alt)}" '
                f'loading="lazy" decoding="async"></span>')
    label = f' role="img" aria-label="{esc(alt)}"' if alt else ' aria-hidden="true"'
    return f'<span class="lg lg--{size} lg--mono c-{esc(c["sector"])}"{label}>{esc(initials(c["name"]))}</span>'


def headline_stats(p):
    """Three or four headline numbers: the written `stats`, or the first amount in each sentence of the key figure."""
    if p.get("stats"):
        return list(p["stats"])[:MAX_STATS]
    out = []
    for sentence in SENTENCE.split(p.get("key_figure", "")):
        m = AMOUNT.search(sentence)
        if not m:
            continue
        label = (sentence[:m.start()] + sentence[m.end():]).strip()
        label = re.sub(r"\s+([,.])", r"\1", re.sub(r"\s{2,}", " ", label)).strip(" ,.")
        if label:
            out.append({"label": label[0].upper() + label[1:], "value": m.group().strip()})
    return out[:MAX_STATS]


def tier(ctx, ovr):
    if ovr is None:
        return "Unrated"
    return next(label for floor, label in ctx.tiers if ovr >= floor)


def team_line(ctx, cid):
    m = ctx.members.get(cid)
    if not m:
        return "Independent"
    return ctx.team_name[m["team"]]


def role_text(ctx, m):
    via = ctx.companies[m["via"]]["name"] if m.get("via") else ""
    return ROLE_LABEL[m["role"]].format(via=via)


def _value(r, key):
    return (r.get("attributes", {}).get(key) or {}).get("value")


# ------------------------------------------------------------------ page frame
def page(ctx, path, title, desc, body, crumbs=""):
    head = ctx.head.format(title=esc(title), desc=esc(desc)).replace('href="site.css"', 'href="../site.css"')
    extra = (f'<link rel="canonical" href="{SITE}/atlas/{path}">\n<link rel="stylesheet" href="../atlas.css">\n'
             f'<link rel="stylesheet" href="../atlas-pages.css">\n</head>')
    nav = f'<nav class="pg__nav" aria-label="Atlas"><a class="pg__back" href="../tech-atlas.html">&larr; The Tech Atlas</a>{crumbs}</nav>'
    return head.replace("</head>", extra, 1) + f'\n<main class="pg">\n{nav}\n{body}\n</main>\n' + ctx.foot


def sector_nav(ctx, current=None):
    links = "".join(f'<a href="sector-{sid}.html"{" aria-current=\"page\"" if sid == current else ""}>{esc(name)}</a>'
                    for sid, name in ctx.sector_name.items() if sid != "backers")
    teams = f'<a href="teams.html"{" aria-current=\"page\"" if current == "teams" else ""}>Teams</a>'
    return f'<nav class="pg__sectors" aria-label="Standings">{links}{teams}</nav>'


def radar_svg(values, labels):
    """The six-spoke radar, first spoke straight up. An unrated spoke sits at the floor."""
    R, pad = 80, 54
    def pt(v, i, r=R):
        f = RADAR_FLOOR if v is None else RADAR_FLOOR + (1 - RADAR_FLOOR) * (min(99, max(40, v)) - 40) / 59
        a = -math.pi / 2 + i * math.pi / 3
        return round(math.cos(a) * r * f, 1), round(math.sin(a) * r * f, 1)
    grid = "".join(f'<polygon class="rd__grid" points="{" ".join("%s,%s" % pt(99, i, R * k) for i in range(6))}"/>'
                   for k in (1, 0.66, 0.33))
    spokes = "".join(f'<line class="rd__grid" x1="0" y1="0" x2="{pt(99, i)[0]}" y2="{pt(99, i)[1]}"/>' for i in range(6))
    shape = f'<polygon class="rd__shape" points="{" ".join("%s,%s" % pt(v, i) for i, v in enumerate(values))}"/>'
    text = []
    for i, (lab, v) in enumerate(zip(labels, values)):
        x, y = pt(99, i)
        anchor = "middle" if abs(x) < 1 else "start" if x > 0 else "end"
        text.append(f'<text class="rd__l{"" if v is not None else " rd__l--none"}" x="{round(x * 1.18, 1)}" '
                    f'y="{round(y * 1.14 + 4, 1)}" text-anchor="{anchor}">{esc(lab)} {v if v is not None else "&ndash;"}</text>')
    aria = ", ".join(f"{l} {v if v is not None else 'unrated'}" for l, v in zip(labels, values))
    box = f"{-R - pad} {-R - pad + 14} {2 * (R + pad)} {2 * (R + pad) - 28}"
    return (f'<svg class="pf__radar" viewBox="{box}" role="img" aria-label="Attribute radar: {esc(aria)}">'
            f'{grid}{spokes}{shape}{"".join(text)}</svg>')


def source_link(url, trust=None):
    t = f'<span class="conf conf--{esc(trust)}">{esc(trust)}</span> ' if trust else ""
    return f'<span class="pf__src">{t}<a href="{esc(url)}">{esc(host(url))}</a></span>'


# ------------------------------------------------------------------ profile
def _hero(ctx, cid, r):
    c, ps = ctx.companies[cid], ctx.placements.get(cid, [])
    home = ps[0] if ps else None
    bits = [ctx.sector_name[c["sector"]]]
    if home:
        bits.append(RANK_NAME[home["rank"]])
    bits.append(f"Team {team_line(ctx, cid)}" if cid in ctx.members else "Independent")
    ovr = r.get("ovr")
    t = tier(ctx, ovr)
    note = ""
    if ovr is not None:
        note = f'<small>{"Draft &middot; " if r["ovr_status"] == "draft" else ""}rated on {r["ovr_from"]} of 6</small>'
    return f"""<section class="pf__hero" id="hero">
  <div class="pf__id c-{esc(c["sector"])}">{logo_html(ctx, cid, "xl", alt=c["name"] + " logo")}
    <div><p class="pf__k">{" &middot; ".join(esc(b) for b in bits)}</p>
    <h1 class="pf__name">{esc(c["name"])}</h1>
    <p class="pf__desc">{esc(c["description"])}</p></div>
  </div>
  <div class="pf__ovr" data-tier="{esc(t)}"><b>{ovr if ovr is not None else "NR"}</b><span>{"OVR" if ovr is not None else "Not rated"}</span><em>{esc(t)}</em>{note}</div>
</section>"""


def _ratings(ctx, cid, r):
    attrs = r.get("attributes", {})
    labels = [a for a, _ in SHORT]
    rows = []
    for key, _ in SHORT:
        a = attrs.get(key)
        v = a.get("value") if a else None
        t = tier(ctx, v)
        width = 0 if v is None else round((v - 30) / 69 * 100)
        why = ""
        if a:
            ev = "".join(source_link(e["url"], e["trust"]) for e in a.get("evidence", []))
            lev = f'<p class="pf__note">Network base {a["base"]}, judgment {a["adjust"]:+d}.</p>' if key == "leverage" and v is not None else ""
            why = f'<p>{esc(a["reason"])}</p>{ev}{lev}'
        draft = '<span class="pf__dr">draft</span>' if a and a.get("status") == "draft" and v is not None else ""
        rows.append(f'<li data-tier="{esc(t)}"><details><summary><span class="pf__bn">{_label(key)}</span>'
                    f'<span class="pf__bt"><i style="width:{width}%"></i></span><b>{v if v is not None else "unrated"}</b>{draft}</summary>'
                    f'{why or "<p>Not rated yet.</p>"}</details></li>')
    values = [(attrs.get(k) or {}).get("value") for k in labels]
    lede = f'<p class="pf__lede">{esc(r["ovr_reason"])}</p>' if r.get("ovr_reason") else ""
    badges = ""
    if r.get("badges"):
        items = "".join(f'<li class="pf__badge pf__badge--{esc(b["id"])}"><b>{esc(b["label"])}</b>'
                        f'{" <span class=\"pf__dr\">draft</span>" if b.get("status") == "draft" else ""}<p>{esc(b["reason"])}</p></li>'
                        for b in r["badges"])
        badges = f'<h3 class="pf__h3">Badges</h3><ul class="pf__badges">{items}</ul>'
    empty = "" if attrs else '<p class="pf__note">No published ratings for this company yet.</p>'
    return f"""<section class="pf__ratings" id="ratings" aria-labelledby="h-ratings">
  <h2 class="pf__h" id="h-ratings">Ratings</h2>{lede}{empty}
  <div class="pf__rgrid"><ul class="pf__bars">{"".join(rows)}</ul>
  <figure class="pf__fig">{radar_svg(values, [s for _, s in SHORT])}</figure></div>
  {badges}
</section>"""


def _label(key):
    return {"dominance": "Dominance", "momentum": "Momentum", "leverage": "Leverage", "durability": "Durability",
            "firepower": "Firepower", "deal_heat": "Deal Heat"}[key]


def _figures(ctx, cid):
    ps = ctx.placements.get(cid, [])
    if not ps:
        return ""
    stats = headline_stats(ps[0])
    if not stats:
        return ""
    src = ps[0]["source"]
    cells = "".join(f'<a class="pf__figc" href="{esc(src)}"><b>{esc(s["value"])}</b><span>{esc(s["label"])}</span></a>' for s in stats)
    return f"""<section class="pf__figures" id="figures" aria-labelledby="h-figures">
  <h2 class="pf__h" id="h-figures">Key figures</h2>
  <div class="pf__figs pf__figs--{len(stats)}">{cells}</div>
  <p class="pf__note">From the Atlas key figure: {esc(ps[0]["key_figure"])} Source: <a href="{esc(src)}">{esc(host(src))}</a>.</p>
</section>"""


def _bio(ctx, cid):
    bio = ctx.companies[cid].get("bio") or {}
    src = bio.get("sources", {})
    cells = "".join(f'<div class="pf__cell"><span>{label}</span><b><a href="{esc(src[k])}">{esc(bio[k])}</a></b></div>'
                    for k, label in BIO_LABEL if bio.get(k))
    if not cells:
        return ""
    return f'<section class="pf__bio" id="bio" aria-label="Company facts">{cells}</section>'


def _profile(ctx, cid):
    ps = ctx.placements.get(cid, [])
    if not ps:
        return f"""<section class="pf__profile" id="profile" aria-labelledby="h-profile">
  <h2 class="pf__h" id="h-profile">Profile</h2>
  <p>{esc(ctx.companies[cid]["description"])}</p>
  <p class="pf__note">An owner or investor that appears in the Atlas only through its relationships.</p>
</section>"""
    arts = []
    for p in ps:
        where = f'{esc(ctx.sector_name[p["sector"]])} &middot; {esc(ctx.row_name[(p["sector"], p["row"])])} &middot; {RANK_NAME[p["rank"]]}'
        arts.append(f"""<article class="pf__place"><h3 class="pf__h3">{where}</h3>
    <p><b>Key figure</b> {esc(p["key_figure"])}</p>
    <p><b>{WHY_LABEL[p["rank"]]}</b> {esc(p["why"])}</p>
    <p><b>What could change it</b> {esc(p["could_change"])}</p>
    {source_link(p["source"], p["trust"])}</article>""")
    return f"""<section class="pf__profile" id="profile" aria-labelledby="h-profile">
  <h2 class="pf__h" id="h-profile">Profile</h2>
  <p class="pf__desc2">{esc(ctx.companies[cid]["description"])}</p>
  {"".join(arts)}
</section>"""


def _connections(ctx, cid):
    groups = {"allies": [], "rivals": [], "backers": []}
    for e in ctx.edges:
        if cid not in (e["a"], e["b"]):
            continue
        other = e["b"] if e["a"] == cid else e["a"]
        g = ctx.group[e["type"]]
        verb = ""
        if e["type"] in VERB:
            verb = f'<span class="pf__verb">{VERB[e["type"]][0 if e["a"] == cid else 1]}</span> '
        oh = ctx.companies[other]["sector"]
        where = f' <span class="pf__in">in {esc(ctx.sector_name[oh])}</span>' if oh != ctx.companies[cid]["sector"] else ""
        on_map = f'<a class="pf__map" href="../tech-atlas.html#c-{esc(other)}">On the map</a>' if other in ctx.on_map else ""
        groups[g].append(f'<li>{logo_html(ctx, other, "sm")}<div>{verb}<a class="pf__go" href="{esc(other)}.html">'
                         f'{esc(ctx.companies[other]["name"])}</a>{where}<p>{esc(e["text"])} '
                         f'<a href="{esc(e["src"])}">{esc(host(e["src"]))}</a></p>{on_map}</div></li>')
    blocks = "".join(f'<div class="pf__rel pf__rel--{g}"><h3 class="pf__h3">{GROUP_LABEL[g]}</h3><ul>{"".join(items)}</ul></div>'
                     for g, items in groups.items() if items)
    return f"""<section class="pf__connections" id="connections" aria-labelledby="h-conn">
  <h2 class="pf__h" id="h-conn">Connections</h2>
  {blocks or '<p class="pf__note">The Atlas draws no relationships for this company yet.</p>'}
  <p class="pf__mapall"><a href="../tech-atlas.html#c-{esc(cid)}">See {esc(ctx.companies[cid]["name"])} and its connections on the map &rarr;</a></p>
</section>"""


def _standing(ctx, cid):
    ps = ctx.placements.get(cid, [])
    if not ps:
        return ""
    blocks = []
    for p in ps:
        st = ctx.standings[p["sector"]]
        name = esc(ctx.sector_name[p["sector"]])
        mine = next((r for r in st["ranked"] if r["company"] == cid), None)
        if not mine:
            blocks.append(f'<div class="pf__sblock"><p>Not rated, so not ranked in <a href="sector-{p["sector"]}.html">{name}</a>.</p></div>')
            continue
        i = st["ranked"].index(mine)
        lo = max(0, min(i - 2, len(st["ranked"]) - 5))
        near = st["ranked"][lo:lo + 5]
        rows = "".join(f'<li{" class=\"is-me\"" if r["company"] == cid else ""}><span class="pf__sn">{r["rank"]}</span>'
                       f'<a href="{esc(r["company"])}.html">{esc(ctx.companies[r["company"]]["name"])}</a><b>{r["ovr"]}</b></li>'
                       for r in near)
        blocks.append(f'<div class="pf__sblock"><p><b class="pf__big">No. {mine["rank"]}</b> of {len(st["ranked"])} rated in '
                      f'<a href="sector-{p["sector"]}.html">{name}</a></p><ol class="pf__near">{rows}</ol></div>')
    return f"""<section class="pf__standing" id="standing" aria-labelledby="h-standing">
  <h2 class="pf__h" id="h-standing">Sector standing</h2>
  <div class="pf__sgrid">{"".join(blocks)}</div>
</section>"""


def _credits(ctx, cid, r):
    c = ctx.companies[cid]
    bits = []
    if r.get("attributes") and c.get("ovr_by"):
        bits.append(f'Ratings by {esc(c["ovr_by"])}, {esc(c.get("ovr_updated", ""))}, read from the Atlas data under '
                    f'the <a href="https://github.com/fyruan-star/trojanhorse-blog/blob/main/docs/ratings-rubric.md">ratings rubric</a>.')
    logo = c.get("logo")
    if logo:
        bits.append(f'Logo: <a href="{esc(logo["source"])}">{esc(host(logo["source"]))}</a>. {esc(logo["license"])}')
    return f'<p class="pf__credits">{" ".join(bits)}</p>' if bits else ""


def profile_page(ctx, cid):
    c = ctx.companies[cid]
    r = ctx.resolved.get(cid, {})
    body = "\n".join(x for x in (_hero(ctx, cid, r), _ratings(ctx, cid, r), _figures(ctx, cid), _bio(ctx, cid),
                                 _profile(ctx, cid), _connections(ctx, cid), _standing(ctx, cid), _credits(ctx, cid, r)) if x)
    ovr = r.get("ovr")
    title = f'{c["name"]}: Tech Atlas profile | The Trojan Horse'
    desc = f'{c["name"]} in the Tech Atlas' + (f", OVR {ovr}" if ovr is not None else "") + f'. {c["description"]}'
    return page(ctx, f"{cid}.html", title, desc, f'<div class="pf">{body}</div>')


# ------------------------------------------------------------------ standings
def standings_page(ctx, sid):
    st = ctx.standings[sid]
    head = "".join(f"<th scope=\"col\" class=\"st__a\" title=\"{_label(k)}\">{s}</th>" for k, s in SHORT)
    rows = []
    for r in st["ranked"]:
        cid, res = r["company"], ctx.resolved.get(r["company"], {})
        cells = "".join(f'<td class="st__a">{_value(res, k) if _value(res, k) is not None else "&ndash;"}</td>' for k, _ in SHORT)
        ch = r["change"]
        change = "&ndash;" if ch is None else ("&#9650;" + str(ch) if ch > 0 else "&#9660;" + str(-ch) if ch < 0 else "=")
        cls = "" if ch is None or ch == 0 else (" st__ch--up" if ch > 0 else " st__ch--down")
        rows.append(f'<tr><td class="st__n">{r["rank"]}</td><td class="st__co"><a href="{esc(cid)}.html">{logo_html(ctx, cid, "sm")}'
                    f'<span>{esc(ctx.companies[cid]["name"])}</span></a><small>{RANK_NAME[r["depth"]]} &middot; '
                    f'{esc(ctx.row_name[(sid, r["row"])])}</small></td><td class="st__tm">{esc(team_line(ctx, cid))}</td>'
                    f'<td class="st__ch{cls}" aria-label="change since the last rating">{change}</td>'
                    f'<td class="st__o" data-tier="{esc(tier(ctx, r["ovr"]))}">{r["ovr"]}</td>{cells}</tr>')
    unrated = ""
    if st["unrated"]:
        names = ", ".join(f'<a href="{esc(r["company"])}.html">{esc(ctx.companies[r["company"]]["name"])}</a>' for r in st["unrated"])
        unrated = f'<p class="pg__note">Not yet rated, so not ranked: {names}.</p>'
    body = f"""<header class="pg__head"><p class="pg__k">Sector standings</p><h1 class="pg__t">{esc(ctx.sector_name[sid])}</h1>
<p class="pg__lede">{esc(ctx.sector_blurb[sid])}</p>{sector_nav(ctx, sid)}</header>
<div class="st__wrap"><table class="st">
<caption>{esc(ctx.sector_name[sid])} companies ranked by OVR. Change compares with the last recorded rating.</caption>
<thead><tr><th scope="col" class="st__n">#</th><th scope="col">Company</th><th scope="col">Team</th><th scope="col" class="st__ch">&plusmn;</th><th scope="col" class="st__o">OVR</th>{head}</tr></thead>
<tbody>{"".join(rows)}</tbody></table></div>
{unrated}
<p class="pg__note"><a href="../tech-atlas.html#s-{esc(sid)}">See {esc(ctx.sector_name[sid])} on the map &rarr;</a></p>"""
    return page(ctx, f"sector-{sid}.html", f'{ctx.sector_name[sid]} standings: Tech Atlas | The Trojan Horse',
                f'Every {ctx.sector_name[sid]} company in the Tech Atlas, ranked by OVR, with its team and six attributes.', body)


# ------------------------------------------------------------------ teams
def team_page(ctx, team):
    five = {m["company"] for m in sorted((m for m in team["members"] if ctx.resolved.get(m["company"], {}).get("ovr") is not None),
                                         key=lambda m: -ctx.resolved[m["company"]]["ovr"])[:len(TM.STARTING_FIVE)]}
    rows = []
    for m in team["members"]:
        cid = m["company"]
        ovr = ctx.resolved.get(cid, {}).get("ovr")
        reason = ctx.companies[cid].get("team_reason") if m["role"] == "override" else ""
        role = esc(role_text(ctx, m)) + (f'<small>{esc(reason)}</small>' if reason else "")
        rows.append(f'<tr{" class=\"is-five\"" if cid in five else ""}><td class="st__co"><a href="{esc(cid)}.html">{logo_html(ctx, cid, "sm")}'
                    f'<span>{esc(ctx.companies[cid]["name"])}</span></a></td><td>{esc(ctx.sector_name[ctx.companies[cid]["sector"]])}</td>'
                    f'<td class="tm__role">{role}</td><td class="st__o" data-tier="{esc(tier(ctx, ovr))}">{ovr if ovr is not None else "&ndash;"}</td></tr>')
    caps = " and ".join(esc(ctx.companies[c]["name"]) for c in team["captains"])
    logos = "".join(logo_html(ctx, c, "lg", alt=ctx.companies[c]["name"] + " logo") for c in team["captains"])
    ovr = team["ovr"]
    draft = " &middot; draft" if team["ovr_status"] == "draft" else ""
    body = f"""<header class="pg__head tm__head"><div class="tm__id">{logos}<div><p class="pg__k">Team</p><h1 class="pg__t">{esc(team["name"])}</h1>
<p class="pg__lede">Captain{"s" if len(team["captains"]) > 1 else ""}: {caps}. {len(team["members"])} members across {len({ctx.companies[m["company"]]["sector"] for m in team["members"]})} sectors.</p></div></div>
<div class="pf__ovr" data-tier="{esc(tier(ctx, ovr))}"><b>{ovr if ovr is not None else "NR"}</b><span>Team OVR</span><em>{esc(tier(ctx, ovr))}</em><small>starting five{draft}</small></div>
{sector_nav(ctx, "teams")}</header>
<div class="st__wrap"><table class="st tm">
<caption>The roster. Highlighted rows are the starting five that set the team OVR.</caption>
<thead><tr><th scope="col">Company</th><th scope="col">Sector</th><th scope="col">Role</th><th scope="col" class="st__o">OVR</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table></div>
<p class="pg__note">Team OVR is the best five member OVRs weighted 30, 25, 20, 15 and 10, rescaled when a team has fewer rated members. <a href="teams.html">How teams are formed</a>.</p>
<p class="pg__note"><a href="../tech-atlas.html#t-{esc(team["id"])}">Highlight {esc(team["name"])} on the map &rarr;</a></p>"""
    return page(ctx, f"team-{team['id']}.html", f'Team {team["name"]}: Tech Atlas | The Trojan Horse',
                f'The {team["name"]} ecosystem in the Tech Atlas: its captain, roster, roles and team OVR.', body)


def teams_page(ctx):
    cards = "".join(
        f'<a class="tm__card" href="team-{esc(t["id"])}.html"><span class="tm__logos">{"".join(logo_html(ctx, c, "md") for c in t["captains"])}</span>'
        f'<span class="tm__n">{esc(t["name"])}</span><span class="tm__m">{len(t["members"])} members</span>'
        f'<span class="tm__o" data-tier="{esc(tier(ctx, t["ovr"]))}">{t["ovr"] if t["ovr"] is not None else "NR"}</span></a>'
        for t in sorted(ctx.rosters, key=lambda t: -(t["ovr"] or 0)))
    by_sector = {}
    for cid, c in ctx.companies.items():
        if cid not in ctx.members:
            by_sector.setdefault(c["sector"], []).append(cid)
    indep = "".join(
        f'<div><h3 class="pf__h3">{esc(ctx.sector_name[sid])}</h3><p>' +
        ", ".join(f'<a href="{esc(k)}.html">{esc(ctx.companies[k]["name"])}</a>' for k in sorted(ids, key=lambda k: ctx.companies[k]["name"])) +
        "</p></div>" for sid, ids in sorted(by_sector.items(), key=lambda x: list(ctx.sector_name).index(x[0])))
    body = f"""<header class="pg__head"><p class="pg__k">The Tech Atlas</p><h1 class="pg__t">Teams</h1>
<p class="pg__lede">A team is an ecosystem: companies tied together by ownership, backing and major partnerships, usually across sectors.</p>{sector_nav(ctx, "teams")}</header>
<div class="tm__grid">{cards}</div>
<section class="pg__rules"><h2 class="pf__h">How a company joins a team</h2><ol>
<li>Each team names its captains, the companies it is built around.</li>
<li>A company owned by a captain joins that captain's team.</li>
<li>Otherwise each direct tie to a captain scores: backing from the captain 10, supply 3, alliance 3, licence 2, dependency 2. Rivalry scores nothing. The highest-scoring team wins.</li>
<li>A company owned by a member placed that way joins its owner's team.</li>
<li>An even score is settled by hand, with the reason written down, and the build fails until it is.</li>
<li>Anyone else is independent. Most companies are, because the Atlas draws only the relationships a source states.</li>
</ol></section>
<section class="pg__indep"><h2 class="pf__h">Independents</h2>{indep}</section>"""
    return page(ctx, "teams.html", "Teams: Tech Atlas | The Trojan Horse",
                "The ecosystems of the Tech Atlas: who leads each team, who is on it and how strong it is.", body)


def write_all(ctx, root):
    """Write every Atlas page into root/atlas/. Returns the number of pages."""
    out = root / "atlas"
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    for cid in ctx.companies:
        (out / f"{cid}.html").write_text(profile_page(ctx, cid), encoding="utf-8"); n += 1
    for sid in ctx.standings:
        (out / f"sector-{sid}.html").write_text(standings_page(ctx, sid), encoding="utf-8"); n += 1
    for t in ctx.rosters:
        (out / f"team-{t['id']}.html").write_text(team_page(ctx, t), encoding="utf-8"); n += 1
    (out / "teams.html").write_text(teams_page(ctx), encoding="utf-8")
    return n + 1
