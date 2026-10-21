#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Indicative 36-month budget model for the BAPIL Technical Blueprint (Chapter 17, Annex Q).

Every figure in Tables 49, 50, 61 and 62 of the Blueprint is computed here from stated
assumptions, so that the feasibility and costing study (Deliverable D1.3) can change an
assumption and regenerate the budget. Amounts are in Bangladeshi taka (Tk);
1 crore = 10,000,000 and 1 lakh = 100,000. All figures are planning estimates, not
quotations and not approved funding.

Run: python3 budget_model.py              # print the budget, scenarios, bridge and sensitivity
     python3 budget_model.py --csv DIR    # also write the same figures as CSV files to DIR
"""
import csv
import os
import sys

CRORE = 10_000_000

# ----------------------------------------------------------------- base-case assumptions
BASE = {
    # Bangladesh Bank weighted average rate was Tk 123.65 per USD on 19 October 2026
    "usd_to_bdt": 124,
    # Annual escalation of taka costs in Years 2 and 3. Point-to-point CPI inflation was
    # 8.34% in September 2026 (BBS, as reported); the host's increment rules may differ.
    "escalation": 0.08,
    # Average share of Year 1 staff positions filled (recruitment takes place in months 1 to 6)
    "ramp_y1": 0.75,
    # Multiplier on the fully loaded staff costs below (1.0 = base case)
    "staff_factor": 1.0,
    # Multiplier on equipment prices (1.0 = base case, before any import duty or VAT)
    "equipment_factor": 1.0,
    # Host institution overhead on direct costs, and a separate contingency on direct costs
    "overhead_rate": 0.10,
    "contingency_rate": 0.05,
    # Compute for Stage 1 model adaptation if shared national compute is not available (USD, Year 2)
    "adaptation_compute_usd": 0,
    # Switches used only to reconcile with the initial planning estimate (Annex Q, Table 61)
    "legacy_amounts": False,     # Year 2 and 3 amounts as in the initial estimate (implicit price growth)
    "new_eval_items": True,      # out-of-scope set, citation judgements and annual system audit
    # Known omissions (Section 17.2): off in the base case, on in the adjusted case
    "omitted_items": False,
}

# Year 2 and 3 amounts used in the initial planning estimate, which included implicit price growth
LEGACY = {
    "LANGUAGE_EDITORS": (1_200_000, 1_500_000, 1_500_000),
    "HOSTING_OPS": (2_500_000, 3_500_000, 4_500_000),
    "SPECIALIST_COURSES": (800_000, 1_200_000, 1_200_000),
    "ERRC and board honoraria": (800_000, 900_000, 900_000),
    "Penetration test and red team": (600_000, 700_000, 700_000),
}

# Fully loaded monthly cost per full-time equivalent (salary, allowances, provident fund,
# festival bonus and recruitment), in Tk, at Year 1 prices. The Ninth National Pay Scale (2026)
# sets basic pay from Tk 20,000 (grade 20) to Tk 156,000 (grade 1); research contracts for
# scarce AI skills are assumed to pay above the equivalent grade.
MONTHLY_COST = {
    "Director and principal investigator": 300_000,
    "Policy research lead and analysts": 150_000,
    "Machine learning and Bangla NLP engineers": 200_000,
    "Data engineers": 150_000,
    "Software and platform (DevSecOps) engineers": 150_000,
    "Security engineer": 180_000,
    "Governance, legal and ethics analysts": 125_000,
    "User experience and accessibility designer": 125_000,
    "Programme and partnership coordinator": 90_000,
    "Training and outreach officers": 80_000,
}

# Full-time equivalents by year (Table 16)
FTE = {
    "Director and principal investigator": (1, 1, 1),
    "Policy research lead and analysts": (1, 2, 3),
    "Machine learning and Bangla NLP engineers": (2, 3, 4),
    "Data engineers": (1, 2, 2),
    "Software and platform (DevSecOps) engineers": (1, 2, 2),
    "Security engineer": (0.5, 1, 1),
    "Governance, legal and ethics analysts": (1, 1, 2),
    "User experience and accessibility designer": (0.5, 1, 1),
    "Programme and partnership coordinator": (1, 1, 1),
    "Training and outreach officers": (0, 1, 2),
}

LANGUAGE_EDITORS = (1_200_000, 1_400_000, 1_400_000)   # part-time Bangla editors, Year 1 prices
FELLOWS = (6, 10, 12)                                  # graduate fellows per year
FELLOW_STIPEND_MONTHLY = 40_000

# Equipment in US dollars (one-time): servers, GPU inference servers (L40S class), storage
EQUIPMENT_USD = (
    3 * 12_000 + 2 * 25_000 + 6_000,  # Year 1: 3 servers, 2 GPU inference servers, 20 TB storage
    2 * 12_000 + 2 * 25_000 + 8_000,  # Year 2: staging and disaster-recovery capacity
    1 * 12_000 + 12_000,              # Year 3: replacement and storage growth
)
HOSTING_OPS = (2_500_000, 3_200_000, 3_800_000)  # data-centre space, power, bandwidth, licences, development cloud

# Data and annotation
BENCHMARK_ITEMS = (500, 800, 700)       # answerable BanglaPolicyQA questions per year (2,000 by month 30)
COST_PER_ITEM = 2_500                   # question writing, gold-passage search and adjudication
OUT_OF_SCOPE_ITEMS = (200, 100, 0)      # out-of-scope questions for abstention testing (no gold passages)
COST_PER_OUT_OF_SCOPE = 600
CITATION_JUDGEMENTS = (400, 800, 800)   # answer sentences judged by two annotators for citation support
COST_PER_JUDGEMENT = 500
OCR_CORRECTION = (2_000_000, 2_000_000, 1_500_000)
DATA_AGREEMENTS = (500_000, 400_000, 300_000)

# Training (Table 18): officials trained per year and average cost per participant
OFFICIALS_TRAINED = (100, 200, 200)     # 500 by month 36 (Table 54)
COST_PER_PARTICIPANT = 15_000           # venue, materials, travel for programmes outside Dhaka
SPECIALIST_COURSES = (800_000, 1_100_000, 1_100_000)

# Governance, audit and evaluation (one-time items are marked in ONE_TIME_GOVERNANCE)
GOVERNANCE = (
    {"ERRC and board honoraria": 800_000, "Legal review": 800_000, "Penetration test and red team": 600_000,
     "Baseline study": 600_000, "Annual independent audit of systems": 300_000},
    {"ERRC and board honoraria": 800_000, "Penetration test and red team": 600_000,
     "Independent mid-term evaluation": 2_000_000, "Annual independent audit of systems": 300_000},
    {"ERRC and board honoraria": 800_000, "Penetration test and red team": 600_000,
     "Independent final evaluation": 2_500_000, "Annual independent audit of systems": 300_000},
)
ONE_TIME_GOVERNANCE = {"Legal review", "Baseline study", "Independent mid-term evaluation", "Independent final evaluation"}

# Known omissions from the base case (Section 17.2; Table 68, U16), planning assumptions:
# consultation and engagement events, P5 survey data collection, staff travel other than for
# training and open-access fees (Tk 15 lakh a year at Year 1 prices), and a computer for each
# new staff member (USD 1,200; 10, 5 and 4 new staff in Years 1 to 3, 19 in all).
OMITTED_ALLOWANCE = 1_500_000
NEW_STAFF = (10, 5, 4)
COMPUTER_USD = 1_200

CATEGORIES = [
    "Core staff",
    "Language editors and fellowships",
    "Compute and hosting",
    "Data and annotation",
    "Training and outreach",
    "Governance, audit and evaluation",
]

SCENARIOS = {
    "low": dict(BASE, staff_factor=0.85, escalation=0.06, equipment_factor=0.80, usd_to_bdt=120),
    "base": dict(BASE),
    # Base case plus the known omissions and a 10% contingency (Section 17.2)
    "adjusted": dict(BASE, omitted_items=True, contingency_rate=0.10),
    "high": dict(BASE, staff_factor=1.20, escalation=0.10, equipment_factor=1.25, usd_to_bdt=135,
                 contingency_rate=0.10, adaptation_compute_usd=20_000),
}


def _esc(p, y):
    """Price index for year y (0, 1, 2) relative to Year 1 prices."""
    return (1 + p["escalation"]) ** y


def lines(p=None):
    """Return {category: [(item, one_time, (y1, y2, y3)), ...]} in Tk."""
    p = dict(BASE, **(p or {}))
    out = {c: [] for c in CATEGORIES}
    years = range(3)
    staff = []
    for y in years:
        cost = sum(MONTHLY_COST[r] * 12 * FTE[r][y] for r in FTE) * p["staff_factor"] * _esc(p, y)
        if y == 0:
            cost *= p["ramp_y1"]
        staff.append(cost)
    out["Core staff"].append(("Core staff salaries and on-costs", False, tuple(staff)))
    ed = LEGACY["LANGUAGE_EDITORS"] if p["legacy_amounts"] else LANGUAGE_EDITORS
    host = LEGACY["HOSTING_OPS"] if p["legacy_amounts"] else HOSTING_OPS
    spec = LEGACY["SPECIALIST_COURSES"] if p["legacy_amounts"] else SPECIALIST_COURSES
    out["Language editors and fellowships"] += [
        ("Part-time Bangla language editors", False, tuple(ed[y] * _esc(p, y) for y in years)),
        ("Graduate fellowships", False, tuple(FELLOWS[y] * FELLOW_STIPEND_MONTHLY * 12 * _esc(p, y) for y in years)),
    ]
    equip = [EQUIPMENT_USD[y] * p["equipment_factor"] * p["usd_to_bdt"] for y in years]
    out["Compute and hosting"] += [
        ("Servers, GPUs and storage", True, tuple(equip)),
        ("Hosting, power, bandwidth and licences", False, tuple(host[y] * _esc(p, y) for y in years)),
    ]
    if p["adaptation_compute_usd"]:
        out["Compute and hosting"].append(
            ("Stage 1 adaptation compute (if no national compute)", True, (0, p["adaptation_compute_usd"] * p["usd_to_bdt"], 0)))
    new = 1 if p["new_eval_items"] else 0
    out["Data and annotation"] += [
        ("Benchmark questions and gold passages", True, tuple(BENCHMARK_ITEMS[y] * COST_PER_ITEM * _esc(p, y) for y in years)),
        ("Out-of-scope questions for abstention tests", True, tuple(new * OUT_OF_SCOPE_ITEMS[y] * COST_PER_OUT_OF_SCOPE * _esc(p, y) for y in years)),
        ("Citation-support judgements", False, tuple(new * CITATION_JUDGEMENTS[y] * COST_PER_JUDGEMENT * _esc(p, y) for y in years)),
        ("OCR correction", False, tuple(OCR_CORRECTION[y] * _esc(p, y) for y in years)),
        ("Data agreements and custodian liaison", False, tuple(DATA_AGREEMENTS[y] * _esc(p, y) for y in years)),
    ]
    out["Training and outreach"] += [
        ("Training of officials", False, tuple(OFFICIALS_TRAINED[y] * COST_PER_PARTICIPANT * _esc(p, y) for y in years)),
        ("Specialist courses and bilingual materials", False, tuple(spec[y] * _esc(p, y) for y in years)),
    ]
    if p["omitted_items"]:
        out["Training and outreach"].append(
            ("Engagement events, P5 survey data, travel and open-access fees", False,
             tuple(OMITTED_ALLOWANCE * _esc(p, y) for y in years)))
        out["Compute and hosting"].append(
            ("Staff computers", True, tuple(NEW_STAFF[y] * COMPUTER_USD * p["usd_to_bdt"] for y in years)))
    items = sorted({k for g in GOVERNANCE for k in g})
    for k in items:
        amounts = [GOVERNANCE[y].get(k, 0) for y in years]
        if p["legacy_amounts"] and k in LEGACY:
            amounts = list(LEGACY[k])
        if not p["new_eval_items"] and k == "Annual independent audit of systems":
            amounts = [0, 0, 0]
        out["Governance, audit and evaluation"].append(
            (k, k in ONE_TIME_GOVERNANCE, tuple(amounts[y] * _esc(p, y) for y in years)))
    return out, p


def budget(p=None):
    """Category totals by year, plus overhead and contingency rows, in Tk."""
    ls, p = lines(p)
    rows = {c: [sum(v[2][y] for v in ls[c]) for y in range(3)] for c in CATEGORIES}
    direct = [sum(rows[c][y] for c in CATEGORIES) for y in range(3)]
    rows["Host overheads (%d%%)" % round(100 * p["overhead_rate"])] = [d * p["overhead_rate"] for d in direct]
    rows["Contingency (%d%%)" % round(100 * p["contingency_rate"])] = [d * p["contingency_rate"] for d in direct]
    return rows


def totals(p=None):
    rows = budget(p)
    by_year = [sum(v[y] for v in rows.values()) for y in range(3)]
    return by_year, sum(by_year)


def one_time_recurring(p=None):
    """Direct costs split into one-time and recurring, by year (Tk), before overheads and contingency."""
    ls, p = lines(p)
    one = [0.0, 0.0, 0.0]
    rec = [0.0, 0.0, 0.0]
    for c in CATEGORIES:
        for _, is_one, vals in ls[c]:
            for y in range(3):
                (one if is_one else rec)[y] += vals[y]
    return one, rec


def sensitivity():
    """Change in the 36-month total (Tk) for single-factor changes from the base case."""
    _, base = totals()
    cases = {
        "Staff costs 20% higher": dict(staff_factor=1.2),
        "Staff costs 20% lower": dict(staff_factor=0.8),
        "Exchange rate Tk 136 (10% weaker taka)": dict(usd_to_bdt=124 * 1.1),
        "Escalation 10% a year instead of 8%": dict(escalation=0.10),
        "Year 1 recruitment complete from month 1": dict(ramp_y1=1.0),
        "Equipment 25% dearer (duties, VAT or prices)": dict(equipment_factor=1.25),
    }
    return {k: totals(v)[1] - base for k, v in cases.items()}


def bridge():
    """Step-by-step reconciliation from the initial planning estimate (Tk 18.49 crore) to the base case."""
    steps = [
        ("Initial planning estimate made while drafting (constant prices, full staffing from month 1, no separate contingency)",
         dict(legacy_amounts=True, new_eval_items=False, escalation=0.0, ramp_y1=1.0, contingency_rate=0.0)),
        ("Year 2 and 3 amounts restated at Year 1 prices",
         dict(new_eval_items=False, escalation=0.0, ramp_y1=1.0, contingency_rate=0.0)),
        ("Explicit escalation of taka costs (8% a year)",
         dict(new_eval_items=False, ramp_y1=1.0, contingency_rate=0.0)),
        ("Year 1 recruitment ramp (75% of positions filled on average)",
         dict(new_eval_items=False, contingency_rate=0.0)),
        ("Evaluation items added (out-of-scope set, citation judgements, annual system audit)",
         dict(contingency_rate=0.0)),
        ("Separate contingency of 5% of direct costs", dict()),
    ]
    out = []
    prev = None
    for label, p in steps:
        t = totals(p)[1]
        out.append((label, t, None if prev is None else t - prev))
        prev = t
    return out


def crore(x):
    return x / CRORE


def main():
    rows = budget()
    by_year, total = totals()
    print("%-36s %8s %8s %8s %9s %6s" % ("Category (Tk crore)", "Year 1", "Year 2", "Year 3", "Total", "Share"))
    for k, v in rows.items():
        t = sum(v)
        print("%-36s %8.2f %8.2f %8.2f %9.2f %5.0f%%" % (k, crore(v[0]), crore(v[1]), crore(v[2]), crore(t), 100 * t / total))
    print("%-36s %8.2f %8.2f %8.2f %9.2f" % ("Total", crore(by_year[0]), crore(by_year[1]), crore(by_year[2]), crore(total)))
    print("Unrounded total: Tk %s; sum of rounded annual totals: %.2f crore"
          % (format(round(total), ","), sum(round(crore(x), 2) for x in by_year)))
    print("Total in US dollars: %.2f million" % (total / BASE["usd_to_bdt"] / 1e6))
    one, rec = one_time_recurring()
    print("One-time direct:  ", [round(crore(x), 2) for x in one], round(crore(sum(one)), 2))
    print("Recurring direct: ", [round(crore(x), 2) for x in rec], round(crore(sum(rec)), 2))
    for name, p in SCENARIOS.items():
        y, t = totals(p)
        print("Scenario %-5s: %s total %.2f" % (name, [round(crore(x), 2) for x in y], crore(t)))
    _, base_t = totals()
    om_t = totals(dict(omitted_items=True))[1]
    print("Known omissions with overheads and contingency: %+.2f crore" % crore(om_t - base_t))
    for label, t, d in bridge():
        print("Bridge: %-80s %6.2f %s" % (label, crore(t), "" if d is None else "%+.2f" % crore(d)))
    for k, d in sensitivity().items():
        print("Sensitivity: %-46s %+.2f crore" % (k, crore(d)))


def write_csv(outdir):
    """Write the budget model outputs as CSV (Tk, unrounded) for use in spreadsheets."""
    os.makedirs(outdir, exist_ok=True)

    def w(name, header, rows):
        with open(os.path.join(outdir, name), "w", newline="", encoding="utf-8") as fh:
            cw = csv.writer(fh)
            cw.writerow(header)
            cw.writerows(rows)

    ls, p = lines()
    w("budget_line_items.csv", ["category", "item", "one_time", "year1_tk", "year2_tk", "year3_tk", "total_tk"],
      [[c, item, "yes" if one else "no"] + [round(v, 2) for v in vals] + [round(sum(vals), 2)]
       for c in CATEGORIES for item, one, vals in ls[c]])
    rows = budget()
    w("budget_by_category.csv", ["row", "year1_tk", "year2_tk", "year3_tk", "total_tk"],
      [[k] + [round(x, 2) for x in v] + [round(sum(v), 2)] for k, v in rows.items()]
      + [["Total"] + [round(x, 2) for x in totals()[0]] + [round(totals()[1], 2)]])
    w("budget_scenarios.csv", ["scenario", "year1_tk", "year2_tk", "year3_tk", "total_tk"],
      [[name] + [round(x, 2) for x in totals(sp)[0]] + [round(totals(sp)[1], 2)] for name, sp in SCENARIOS.items()])
    w("budget_bridge.csv", ["step", "total_tk", "change_tk"],
      [[label, round(t, 2), "" if d is None else round(d, 2)] for label, t, d in bridge()])
    w("budget_sensitivity.csv", ["case", "change_in_total_tk"],
      [[k, round(d, 2)] for k, d in sensitivity().items()])
    w("budget_assumptions.csv", ["assumption", "value"], [[k, v] for k, v in BASE.items()])


if __name__ == "__main__":
    main()
    if len(sys.argv) == 3 and sys.argv[1] == "--csv":
        write_csv(sys.argv[2])
        print("CSV files written to", sys.argv[2])
