#!/usr/bin/env python3
"""Check content/atlas/atlas.json before it is built.

    python3 scripts/validate_atlas.py

Prints every problem and exits 1 if there is one. build.py runs the same
checks, so a bad edit turns the GitHub build red instead of reaching the site.
"""
import json, pathlib, re, sys

ATLAS = pathlib.Path(__file__).resolve().parent.parent / "content" / "atlas" / "atlas.json"

TIERS = {"end", "platform", "stack"}
RANKS = {"starter", "second_string", "practice_squad"}
CARD_TRUST = {"sourced", "reported"}
LINE_TRUST = {"sourced", "reported", "inferred"}
TYPES = {"alliance", "supply", "license", "dependency", "rivalry", "ownership", "investment"}
# these read the same in either direction, so B-A duplicates A-B
SYMMETRIC = {"alliance", "rivalry"}
STATUSES = {"draft", "reviewed"}
# a company with no card lives on the backers island of the map
BACKERS = "backers"

COMPANY_KEYS = {"name", "description", "sector"}
RATING_KEYS = {"ovr_status", "ovr_reason", "ovr_evidence", "ovr_updated", "ovr_by"}
# room to grow: allowed now, used later
RESERVED_KEYS = {"attributes", "badges", "ovr_history"}
PLACEMENT_KEYS = {"company", "sector", "row", "rank", "label", "key_figure", "why", "could_change", "source", "trust"}
LINE_KEYS = {"from", "to", "type", "text", "source", "trust", "date", "added"}

# Lines a review found wrong or too loose to draw (2026-10-23). They stay out.
REJECTED = {("thoma_bravo", "salesforce"), ("sk_hynix", "samsung"), ("apple", "lenovo"),
            ("byd", "tesla"), ("china_robots", "amazon"), ("google", "wasabi"),
            ("silver_lake", "workday"), ("stripe", "paypal"), ("advent", "paypal"),
            ("block", "paypal"), ("spacex", "cursor")}

ID = re.compile(r"^[a-z0-9_]+$")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# a full stop followed by a new sentence, but not the point in $89.0bn
SECOND_SENTENCE = re.compile(r"\.\s+[A-Z]")
PROSE_FIELDS = {"blurb", "metric", "description", "key_figure", "why", "could_change", "text", "ovr_reason"}
BANNED = {"—": "an em dash", ";": "a semicolon", "?": "a question mark"}


def _https(url):
    return isinstance(url, str) and url.startswith("https://")


def _prose(where, field, value, errors):
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{where}: {field} is empty")
        return
    for ch, name in BANNED.items():
        if ch in value:
            errors.append(f"{where}: {field} contains {name}")


def _sectors(d, errors):
    rows = {}
    for s in d.get("sectors", []):
        sid = s.get("id")
        if sid in rows:
            errors.append(f"sector {sid}: duplicate id")
        if s.get("tier") not in TIERS:
            errors.append(f"sector {sid}: tier must be one of {sorted(TIERS)}")
        _prose(f"sector {sid}", "blurb", s.get("blurb"), errors)
        ids = [r.get("id") for r in s.get("rows", [])]
        if len(ids) != len(set(ids)):
            errors.append(f"sector {sid}: duplicate row id")
        for r in s.get("rows", []):
            _prose(f"row {sid}/{r.get('id')}", "metric", r.get("metric"), errors)
            if not _https(r.get("metric_source")):
                errors.append(f"row {sid}/{r.get('id')}: metric_source must be an https link")
        rows[sid] = set(ids)
    return rows


def _placements(d, rows, errors):
    seen, plays_in = set(), {}
    for i, p in enumerate(d.get("placements", [])):
        where = f"card {i} ({p.get('company')} in {p.get('sector')}/{p.get('row')})"
        for k in set(p) - PLACEMENT_KEYS:
            errors.append(f"{where}: unknown field {k}")
        if p.get("company") not in d.get("companies", {}):
            errors.append(f"{where}: company {p.get('company')} does not exist")
        if p.get("sector") not in rows:
            errors.append(f"{where}: sector does not exist")
        elif p.get("row") not in rows[p["sector"]]:
            errors.append(f"{where}: row does not exist in that sector")
        if p.get("rank") not in RANKS:
            errors.append(f"{where}: rank must be one of {sorted(RANKS)}")
        if p.get("trust") not in CARD_TRUST:
            errors.append(f"{where}: trust must be one of {sorted(CARD_TRUST)}")
        if not _https(p.get("source")):
            errors.append(f"{where}: source must be an https link")
        for f in ("key_figure", "why", "could_change"):
            _prose(where, f, p.get(f), errors)
        key = (p.get("company"), p.get("sector"), p.get("row"))
        if key in seen:
            errors.append(f"{where}: duplicate card")
        seen.add(key)
        plays_in.setdefault(p.get("company"), set()).add(p.get("sector"))
    return plays_in


def _rating(cid, c, errors):
    where = f"company {cid}"
    ovr = c.get("ovr")
    if ovr is None:
        extra = sorted(k for k in RATING_KEYS if c.get(k) not in (None, "", []))
        if extra:
            errors.append(f"{where}: unrated (ovr is null) but carries {', '.join(extra)}")
        return
    if type(ovr) is not int or not 40 <= ovr <= 99:
        errors.append(f"{where}: ovr must be a whole number from 40 to 99, or null")
    if c.get("ovr_status") not in STATUSES:
        errors.append(f"{where}: ovr_status must be draft or reviewed")
    reason = c.get("ovr_reason")
    _prose(where, "ovr_reason", reason, errors)
    if isinstance(reason, str) and (not reason.endswith(".") or SECOND_SENTENCE.search(reason)):
        errors.append(f"{where}: ovr_reason must be one sentence ending in a full stop")
    ev = c.get("ovr_evidence")
    if not isinstance(ev, list) or not ev:
        errors.append(f"{where}: ovr_evidence needs at least one link")
    else:
        for e in ev:
            if not isinstance(e, dict) or not _https(e.get("url")) or e.get("trust") not in LINE_TRUST:
                errors.append(f"{where}: each ovr_evidence item needs an https url and a trust of {sorted(LINE_TRUST)}")
    if not ISO_DATE.match(str(c.get("ovr_updated", ""))):
        errors.append(f"{where}: ovr_updated must be a date like 2026-11-02")
    if not c.get("ovr_by"):
        errors.append(f"{where}: ovr_by is empty")


def _companies(d, plays_in, linked, errors, warnings):
    sectors = {s.get("id") for s in d.get("sectors", [])}
    for cid, c in d.get("companies", {}).items():
        where = f"company {cid}"
        if not ID.match(cid):
            errors.append(f"{where}: id must be lower case letters, digits and underscores")
        for k in set(c) - COMPANY_KEYS - RATING_KEYS - RESERVED_KEYS - {"ovr"}:
            errors.append(f"{where}: unknown field {k}")
        if not c.get("name"):
            errors.append(f"{where}: name is empty")
        _prose(where, "description", c.get("description"), errors)
        sec = c.get("sector")
        if not sec:
            errors.append(f"{where}: has no sector")
        elif cid in plays_in and sec not in plays_in[cid]:
            errors.append(f"{where}: sector {sec} is not one it has a card in ({', '.join(sorted(plays_in[cid]))})")
        elif cid not in plays_in and sec != BACKERS:
            errors.append(f"{where}: has no card, so its sector must be {BACKERS}")
        elif sec not in sectors | {BACKERS}:
            errors.append(f"{where}: sector {sec} does not exist")
        if cid not in plays_in and cid not in linked:
            warnings.append(f"{where}: appears on no card and in no relationship")
        _rating(cid, c, errors)


def _relationships(d, errors):
    companies = d.get("companies", {})
    seen, linked = set(), set()
    for i, r in enumerate(d.get("relationships", [])):
        a, b, t = r.get("from"), r.get("to"), r.get("type")
        where = f"relationship {i} ({a} -> {b})"
        for k in set(r) - LINE_KEYS:
            errors.append(f"{where}: unknown field {k}")
        for end in (a, b):
            if end not in companies:
                errors.append(f"{where}: company {end} does not exist")
        if a == b:
            errors.append(f"{where}: points at itself")
        if t not in TYPES:
            errors.append(f"{where}: type must be one of {sorted(TYPES)}")
        if r.get("trust") not in LINE_TRUST:
            errors.append(f"{where}: trust must be one of {sorted(LINE_TRUST)}")
        elif r["trust"] == "inferred" and t != "ownership":
            errors.append(f"{where}: only ownership may be drawn from an inferred source")
        if not _https(r.get("source")):
            errors.append(f"{where}: source must be an https link")
        if not r.get("date"):
            errors.append(f"{where}: date is empty")
        if not ISO_DATE.match(str(r.get("added", ""))):
            errors.append(f"{where}: added must be a date like 2026-10-23")
        _prose(where, "text", r.get("text"), errors)
        if (a, b) in REJECTED:
            errors.append(f"{where}: this line was rejected in review on 2026-10-23")
        key = (frozenset((a, b)), t) if t in SYMMETRIC else (a, b, t)
        if key in seen:
            errors.append(f"{where}: duplicate relationship")
        seen.add(key)
        linked.update((a, b))
    return linked


def validate(d):
    """Return (errors, warnings) for the parsed atlas.json. Reads, never changes, d."""
    errors, warnings = [], []
    for k in ("asof", "sectors", "companies", "placements", "relationships"):
        if k not in d:
            errors.append(f"atlas.json is missing {k}")
    if errors:
        return errors, warnings
    rows = _sectors(d, errors)
    plays_in = _placements(d, rows, errors)
    linked = _relationships(d, errors)
    _companies(d, plays_in, linked, errors, warnings)
    return errors, warnings


def main():
    try:
        d = json.loads(ATLAS.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"Cannot read {ATLAS}: {e}")
        return 1
    errors, warnings = validate(d)
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("error:", e)
    rated = [c for c in d["companies"].values() if c.get("ovr") is not None]
    drafts = sum(1 for c in rated if c.get("ovr_status") == "draft")
    print(f"{len(d['sectors'])} sectors, {len(d['companies'])} companies, {len(d['placements'])} cards, "
          f"{len(d['relationships'])} relationships, {len(rated)} rated ({drafts} drafts): "
          f"{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
