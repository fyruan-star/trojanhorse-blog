"""Tech Atlas ratings: Leverage from the network, OVR from six attributes, and badges.

The rules are written out in docs/ratings-rubric.md. atlas_data.py calls
resolve() once per build, with SHOW_DRAFT_RATINGS, and build.py publishes what
comes back. Nothing here changes the data it is given.
"""

ATTRS = ("dominance", "momentum", "leverage", "durability", "firepower", "deal_heat")
ATTR_LABEL = {"dominance": "Dominance", "momentum": "Momentum", "leverage": "Leverage",
              "durability": "Durability", "firepower": "Firepower", "deal_heat": "Deal Heat"}
WEIGHTS = {"dominance": 0.30, "leverage": 0.25, "momentum": 0.15, "durability": 0.15,
           "firepower": 0.15, "deal_heat": 0.0}
REQUIRED = ("dominance", "leverage", "durability")
PEAK = 0.2              # share of OVR taken from the higher of Dominance and Leverage
LO, HI = 40, 99

LEVERAGE_BASE, LEVERAGE_STEP, LEVERAGE_CAP = 50, 8, 82
ADJUST_MIN, ADJUST_MAX = -15, 45
BACKERS = "backers"

CHOKEPOINT_MIN = 92
KINGMAKER_MIN = 3
BADGE_LABEL = {"chokepoint": "Chokepoint", "kingmaker": "Kingmaker",
               "single_customer_risk": "Single-Customer Risk", "in_play": "In Play"}
STORED_BADGES = ("single_customer_risk", "in_play")
CALCULATED_BADGES = ("chokepoint", "kingmaker")


def _clamp(v):
    return max(LO, min(HI, v))


def ovr(values):
    """OVR from attribute values (None = unrated), or None without the required three."""
    if any(values.get(k) is None for k in REQUIRED):
        return None
    rated = {k: v for k, v in values.items() if v is not None and WEIGHTS.get(k)}
    mean = sum(WEIGHTS[k] * v for k, v in rated.items()) / sum(WEIGHTS[k] for k in rated)
    peak = max(values["dominance"], values["leverage"])
    return _clamp(round((1 - PEAK) * mean + PEAK * peak))


def leverage_base(dependents):
    return min(LEVERAGE_CAP, LEVERAGE_BASE + LEVERAGE_STEP * dependents)


def leverage_value(base, adjust):
    return _clamp(base + adjust)


def dependents(data):
    """For each company not on the backers island, the set of companies that depend on it."""
    companies = data["companies"]
    out = {k: set() for k, c in companies.items() if c["sector"] != BACKERS}
    for r in data["relationships"]:
        if r["type"] == "supply":
            on, who = r["from"], r["to"]
        elif r["type"] in ("license", "dependency"):
            on, who = r["to"], r["from"]
        else:
            continue
        if on in out and who in out and on != who:
            out[on].add(who)
    return out


def _backed(data):
    counts = {}
    for r in data["relationships"]:
        if r["type"] in ("ownership", "investment"):
            counts.setdefault(r["from"], set()).add(r["to"])
    return counts


def _attributes(c, base, show_drafts):
    """Published attributes: drafts dropped when hidden, Leverage's value filled in."""
    out = {}
    for k, a in (c.get("attributes") or {}).items():
        if a.get("status") != "reviewed" and not show_drafts:
            continue
        pub = {"reason": a["reason"], "evidence": a.get("evidence", []), "status": a["status"]}
        if k == "leverage":
            adj = a.get("adjust")
            pub.update(base=base, adjust=adj, value=None if adj is None else leverage_value(base, adj))
        else:
            pub["value"] = a.get("value")
        out[k] = pub
    return out


def resolve(data, show_drafts):
    """What each company publishes: attributes, OVR, its status and badges."""
    deps = dependents(data)
    backed = _backed(data)
    out = {}
    for cid, c in data["companies"].items():
        attrs = _attributes(c, leverage_base(len(deps.get(cid, ()))), show_drafts)
        values = {k: attrs.get(k, {}).get("value") for k in ATTRS}
        score = ovr(values)
        used = [k for k in ATTRS if values[k] is not None and WEIGHTS[k]]
        status = None
        if score is not None:
            status = "draft" if any(attrs[k]["status"] == "draft" for k in used) else "reviewed"
        badges = []
        lev = attrs.get("leverage", {})
        if lev.get("value") is not None and lev["value"] >= CHOKEPOINT_MIN:
            badges.append({"id": "chokepoint", "label": BADGE_LABEL["chokepoint"], "status": lev["status"],
                           "reason": f"Leverage of {lev['value']}, at or above {CHOKEPOINT_MIN}.", "evidence": lev["evidence"]})
        n_backed = len(backed.get(cid, ()))
        if n_backed >= KINGMAKER_MIN:
            badges.append({"id": "kingmaker", "label": BADGE_LABEL["kingmaker"], "status": "calculated",
                           "reason": f"Owns or backs {n_backed} companies in the Atlas.", "evidence": []})
        for b in c.get("badges") or []:
            if b.get("status") == "reviewed" or show_drafts:
                badges.append({**b, "label": BADGE_LABEL[b["id"]]})
        rec = {"attributes": attrs, "ovr": score, "ovr_status": status, "ovr_from": len(used) if score else 0,
               "badges": badges}
        if score is not None and c.get("ovr_reason"):
            rec["ovr_reason"] = c["ovr_reason"]
        out[cid] = rec
    return out
