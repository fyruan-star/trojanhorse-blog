#!/usr/bin/env python3
"""Refresh a company page's financials from the SEC.

    python3 scripts/fetch_company.py nvidia 1045810
    python3 scripts/fetch_company.py arista 1596532

Downloads the company's XBRL facts and filing index from data.sec.gov and
writes content/companies/<slug>.json, which build.py turns into
company-<slug>.html. The build never calls the SEC, so the site only changes
when someone runs this and commits the JSON.

Rules the numbers follow:
- Each period takes the value from the most recent filing that reports it, so
  restatements win.
- Fiscal-year rows come from 10-K annual facts. Quarter rows use the three-month
  figure when a filing reports one. Otherwise the quarter is worked out as the
  year-to-date figure less the previous year-to-date figure (always the case for
  the fourth quarter and for cash flow), and the row is marked derived.
- The row label is the calendar year the fiscal year ends in, which is how
  both companies name their years.
"""
import datetime as dt
import json
import pathlib
import subprocess
import sys
import urllib.error
import urllib.request

UA = {"User-Agent": "trojanhorse.blog research"}
OUT = pathlib.Path(__file__).resolve().parent.parent / "content" / "companies"

# metric -> XBRL tags that can carry it (companies switch tags over the years)
METRICS = {
    "revenue": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"],
    "gross_profit": ["GrossProfit"],
    "rnd": ["ResearchAndDevelopmentExpense"],
    "op_income": ["OperatingIncomeLoss"],
    "net_income": ["NetIncomeLoss"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities"],
    "buybacks": ["PaymentsForRepurchaseOfCommonStock"],
}
YEARS = 9          # fiscal-year rows kept
QUARTERS = 8       # quarter rows kept


def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
            return json.load(r)
    except urllib.error.URLError:
        # the python.org installer on macOS ships without certificates, curl has them
        out = subprocess.run(["curl", "-sf", "-A", UA["User-Agent"], url], capture_output=True, check=True)
        return json.loads(out.stdout)


def d(s):
    return dt.date.fromisoformat(s)


def facts_for(gaap, tags):
    """{(start, end): (value, accession, filed, form)} keeping the latest filing."""
    out = {}
    for tag in tags:
        for x in (gaap.get(tag, {}).get("units", {}).get("USD") or []):
            if "start" not in x or x.get("form") not in ("10-K", "10-Q", "10-K/A", "10-Q/A"):
                continue
            key = (x["start"], x["end"])
            if key in out and out[key][2] >= x["filed"]:
                continue
            out[key] = (x["val"], x["accn"], x["filed"], x["form"])
    return out


def first_filed(gaap, tags):
    """{end: (accession, form)} for the earliest filing reporting a period ending then."""
    out = {}
    for tag in tags:
        for x in (gaap.get(tag, {}).get("units", {}).get("USD") or []):
            if x.get("form") in ("10-K", "10-Q") and (x["end"] not in out or x["filed"] < out[x["end"]][2]):
                out[x["end"]] = (x["accn"], x["form"], x["filed"])
    return out


def main(slug, cik):
    cik10 = f"{int(cik):010d}"
    facts = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik10}.json")["facts"]["us-gaap"]
    sub = get(f"https://data.sec.gov/submissions/CIK{cik10}.json")
    series = {m: facts_for(facts, tags) for m, tags in METRICS.items()}
    rev = series["revenue"]
    first = first_filed(facts, METRICS["revenue"])

    # fiscal years: annual revenue periods, newest last
    years = sorted({(s, e) for (s, e) in rev if 340 < (d(e) - d(s)).days < 380}, key=lambda p: p[1])

    def value(metric, start, end, fy_start=None, prev_end=None):
        """A period's value, and whether it had to be worked out."""
        s = series[metric]
        if (start, end) in s:
            return s[(start, end)][0], False
        if fy_start and prev_end and (fy_start, end) in s and (fy_start, prev_end) in s:
            return s[(fy_start, end)][0] - s[(fy_start, prev_end)][0], True
        if fy_start and start == fy_start and (fy_start, end) in s:
            return s[(fy_start, end)][0], False
        return None, False

    # quarters inside each fiscal year, using reported three-month revenue
    q_ends = sorted({e for (s, e) in rev if 80 < (d(e) - d(s)).days < 100})
    quarters = []
    fy_list = years + []
    last_fy_end = years[-1][1]
    # the open fiscal year, if 10-Qs exist after the last 10-K
    open_q = [e for e in q_ends if e > last_fy_end]
    if open_q:
        fy_list.append((str(d(last_fy_end) + dt.timedelta(days=1)), None))
    for fs, fe in fy_list:
        inside = [e for e in q_ends if fs < e and (fe is None or e < fe)]
        ends = inside + ([fe] if fe else [])
        prev = None
        for i, qe in enumerate(ends):
            qs = fs if prev is None else str(d(prev) + dt.timedelta(days=1))
            row = {"start": qs, "end": qe, "fy_end": fe, "q": i + 1, "derived": [], "v": {}}
            for m in METRICS:
                val, derived = value(m, qs, qe, fs, prev)
                row["v"][m] = val
                if derived:
                    row["derived"].append(m)
            quarters.append(row)
            prev = qe

    def label_fy(end):
        return f"FY{d(end).year}"

    annual = []
    for fs, fe in years[-YEARS:]:
        k = first.get(fe)
        annual.append({"label": label_fy(fe), "start": fs, "end": fe,
                       "accn": k[0] if k else None, "form": "10-K",
                       "v": {m: value(m, fs, fe)[0] for m in METRICS}})
    # year-over-year growth needs the year before the first kept row
    prior = {e: value("revenue", s, e)[0] for s, e in years}
    for r in annual:
        prev_end = max((e for e in prior if e < r["end"]), default=None)
        r["v"]["revenue_prior"] = prior.get(prev_end)

    # the open year so far, like a season in progress
    ytd = None
    if open_q:
        fs = str(d(last_fy_end) + dt.timedelta(days=1))
        qs = [q for q in quarters if q["fy_end"] is None]
        n = len(qs)
        last = qs[-1]
        ly = [q for q in quarters if q["fy_end"] == last_fy_end][:n]
        ytd = {"label": f"FY{d(last_fy_end).year + 1} YTD", "quarters": n, "start": fs, "end": last["end"],
               "v": {m: (sum(q["v"][m] for q in qs) if all(q["v"][m] is not None for q in qs) else None)
                     for m in METRICS}}
        ytd["v"]["revenue_prior"] = sum(q["v"]["revenue"] for q in ly) if len(ly) == n else None
        ytd["accn"] = first[last["end"]][0] if last["end"] in first else None
        ytd["form"] = "10-Q"

    for q in quarters:
        same = [p for p in quarters if p["q"] == q["q"] and p["fy_end"] != q["fy_end"] and p["end"] < q["end"]]
        q["v"]["revenue_prior"] = same[-1]["v"]["revenue"] if same and (d(q["end"]) - d(same[-1]["end"])).days < 380 else None
        fe = q["fy_end"]
        q["label"] = f"Q{q['q']} FY{(d(fe).year if fe else d(last_fy_end).year + 1)}"
        k = first.get(q["end"])
        q["accn"], q["form"] = (k[0], k[1]) if k else (None, None)

    out = {
        "slug": slug, "cik": int(cik), "name": sub["name"], "tickers": sub["tickers"],
        "exchanges": sub["exchanges"], "fiscal_year_end": sub["fiscalYearEnd"],
        "city": sub["addresses"]["business"]["city"], "state": sub["addresses"]["business"]["stateOrCountry"],
        "fetched": dt.date.today().isoformat(),
        "annual": list(reversed(annual)), "ytd": ytd,
        "quarters": list(reversed(quarters[-QUARTERS:])),
    }
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{slug}.json"
    path.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print("wrote", path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
