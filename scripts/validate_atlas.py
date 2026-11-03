#!/usr/bin/env python3
"""Check content/atlas/atlas.json before it is built.

    python3 scripts/validate_atlas.py

Prints every problem and exits 1 if there is one. build.py runs the same
checks, so a bad edit turns the GitHub build red instead of reaching the site.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ATLAS = ROOT / "content" / "atlas" / "atlas.json"
sys.path.insert(0, str(ROOT / "content" / "atlas"))
import atlas_ratings as R

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
RATING_KEYS = {"attributes", "badges", "ovr_reason", "ovr_updated", "ovr_by"}
# room to grow: allowed now, used later
RESERVED_KEYS = {"ovr_history"}
# calculated by the build, so never stored
CALCULATED_KEYS = {"ovr", "ovr_status", "ovr_evidence"}
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


def _evidence(where, ev, errors, required):
    if not isinstance(ev, list) or (required and not ev):
        errors.append(f"{where}: evidence needs at least one link")
        return
    for e in ev:
        if not isinstance(e, dict) or not _https(e.get("url")) or e.get("trust") not in LINE_TRUST:
            errors.append(f"{where}: each evidence item needs an https url and a trust of {sorted(LINE_TRUST)}")


def _one_sentence(where, field, text, errors):
    _prose(where, field, text, errors)
    if isinstance(text, str) and (not text.endswith(".") or SECOND_SENTENCE.search(text)):
        errors.append(f"{where}: {field} must be one sentence ending in a full stop")


def _attribute(where, key, a, errors):
    if not isinstance(a, dict):
        errors.append(f"{where}: must be an object")
        return
    if a.get("status") not in STATUSES:
        errors.append(f"{where}: status must be draft or reviewed")
    _one_sentence(where, "reason", a.get("reason"), errors)
    if key == "leverage":
        if "value" in a:
            errors.append(f"{where}: Leverage stores adjust, and the build calculates its value")
        adj = a.get("adjust")
        if adj is not None and (type(adj) is not int or not R.ADJUST_MIN <= adj <= R.ADJUST_MAX):
            errors.append(f"{where}: adjust must be a whole number from {R.ADJUST_MIN} to {R.ADJUST_MAX}, or null")
        rated = adj is not None
    else:
        v = a.get("value")
        if v is not None and (type(v) is not int or not 40 <= v <= 99):
            errors.append(f"{where}: value must be a whole number from 40 to 99, or null")
        rated = v is not None
    _evidence(where, a.get("evidence"), errors, required=rated)


def _rating(cid, c, has_card, errors):
    where = f"company {cid}"
    for k in sorted(CALCULATED_KEYS & set(c)):
        errors.append(f"{where}: {k} is calculated by the build, so remove it")
    if not has_card and (c.get("attributes") or c.get("badges")):
        errors.append(f"{where}: only companies with a card are rated")
    attrs = c.get("attributes")
    if attrs is not None:
        if not isinstance(attrs, dict):
            errors.append(f"{where}: attributes must be an object")
        else:
            for k, a in attrs.items():
                if k not in R.ATTRS:
                    errors.append(f"{where}: unknown attribute {k}")
                else:
                    _attribute(f"{where} {k}", k, a, errors)
    seen = set()
    for b in c.get("badges") or []:
        bw = f"{where} badge {b.get('id') if isinstance(b, dict) else b}"
        if not isinstance(b, dict) or b.get("id") not in R.STORED_BADGES:
            errors.append(f"{bw}: stored badges are {', '.join(R.STORED_BADGES)} (the others are calculated)")
            continue
        if b["id"] in seen:
            errors.append(f"{bw}: listed twice")
        seen.add(b["id"])
        if b.get("status") not in STATUSES:
            errors.append(f"{bw}: status must be draft or reviewed")
        _one_sentence(bw, "reason", b.get("reason"), errors)
        _evidence(bw, b.get("evidence"), errors, required=True)
    if c.get("ovr_reason") is not None:
        _one_sentence(where, "ovr_reason", c["ovr_reason"], errors)
    if c.get("ovr_updated") is not None and not ISO_DATE.match(str(c["ovr_updated"])):
        errors.append(f"{where}: ovr_updated must be a date like 2026-11-02")


def _companies(d, plays_in, linked, errors, warnings):
    sectors = {s.get("id") for s in d.get("sectors", [])}
    for cid, c in d.get("companies", {}).items():
        where = f"company {cid}"
        if not ID.match(cid):
            errors.append(f"{where}: id must be lower case letters, digits and underscores")
        for k in set(c) - COMPANY_KEYS - RATING_KEYS - RESERVED_KEYS - CALCULATED_KEYS:
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
        _rating(cid, c, cid in plays_in, errors)


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
    out = R.resolve(d, show_drafts=True) if not errors else {}
    rated = [r for r in out.values() if r["ovr"] is not None]
    drafts = sum(1 for r in rated if r["ovr_status"] == "draft")
    unrated = sum(1 for r in out.values() for k in R.ATTRS if k in r["attributes"] and r["attributes"][k]["value"] is None)
    print(f"{len(d['sectors'])} sectors, {len(d['companies'])} companies, {len(d['placements'])} cards, "
          f"{len(d['relationships'])} relationships, {len(rated)} with an OVR ({drafts} drafts), "
          f"{unrated} attributes unrated: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
