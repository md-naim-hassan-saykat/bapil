#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Indicative 36-month budget model for the BAPIL Technical Blueprint (Chapter 17).

Every figure in Tables 49 and 50 of the Blueprint is computed here from the stated
assumptions, so that the feasibility study (Deliverable D1.3) can change an assumption
and regenerate the budget. Amounts are in Bangladeshi taka (Tk); 1 crore = 10,000,000 and
1 lakh = 100,000. Run: python3 budget_model.py
"""

USD_TO_BDT = 124  # Bangladesh Bank weighted average rate was Tk 123.65 on 19 October 2026

# Fully loaded monthly cost per full-time equivalent (salary, allowances, provident fund,
# festival bonus and recruitment), in Tk. The Ninth National Pay Scale (2026) sets basic pay
# from Tk 20,000 (grade 20) to Tk 156,000 (grade 1); research contracts for scarce AI skills
# are assumed to pay above the equivalent grade.
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

LANGUAGE_EDITORS = (1_200_000, 1_500_000, 1_500_000)      # part-time Bangla editors per year
FELLOWS = (6, 10, 12)                                       # graduate fellows per year
FELLOW_STIPEND_MONTHLY = 40_000

# Compute and hosting, in US dollars (equipment) and Tk (operations)
EQUIPMENT_USD = (
    3 * 12_000 + 2 * 25_000 + 6_000,  # Year 1: 3 servers, 2 GPU inference servers (L40S class), 20 TB storage
    2 * 12_000 + 2 * 25_000 + 8_000,  # Year 2: staging and disaster-recovery capacity, 2 more GPU servers
    1 * 12_000 + 12_000,              # Year 3: replacement and storage growth
)
HOSTING_OPS = (2_500_000, 3_500_000, 4_500_000)  # data-centre space, power, bandwidth, licences, development cloud

# Data and annotation
BENCHMARK_ITEMS = (500, 800, 700)        # BanglaPolicyQA questions written and adjudicated per year (2,000 by month 30)
COST_PER_ITEM = 2_500                    # writing, gold-passage search and adjudication
OCR_CORRECTION = (2_000_000, 2_000_000, 1_500_000)
DATA_AGREEMENTS = (500_000, 400_000, 300_000)

# Training (Table 18): officials trained per year and average cost per participant
OFFICIALS_TRAINED = (100, 200, 200)     # 500 by month 36 (Table 54)
COST_PER_PARTICIPANT = 15_000           # venue, materials, travel for programmes outside Dhaka
SPECIALIST_COURSES = (800_000, 1_200_000, 1_200_000)   # T3 to T5 cohorts and materials in two languages

# Governance, audit and evaluation
GOVERNANCE = (
    {"ERRC and board honoraria": 800_000, "Legal review": 800_000, "Penetration test and red team": 600_000, "Baseline study": 600_000},
    {"ERRC and board honoraria": 900_000, "Penetration test and red team": 700_000, "Independent mid-term evaluation": 2_000_000},
    {"ERRC and board honoraria": 900_000, "Penetration test and red team": 700_000, "Independent final evaluation": 2_500_000},
)

OVERHEAD_RATE = 0.10  # host overheads and contingency on all other costs

CRORE = 10_000_000


def budget():
    years = range(3)
    staff = [sum(MONTHLY_COST[r] * 12 * FTE[r][y] for r in FTE) for y in years]
    people_other = [LANGUAGE_EDITORS[y] + FELLOWS[y] * FELLOW_STIPEND_MONTHLY * 12 for y in years]
    compute = [EQUIPMENT_USD[y] * USD_TO_BDT + HOSTING_OPS[y] for y in years]
    data = [BENCHMARK_ITEMS[y] * COST_PER_ITEM + OCR_CORRECTION[y] + DATA_AGREEMENTS[y] for y in years]
    training = [OFFICIALS_TRAINED[y] * COST_PER_PARTICIPANT + SPECIALIST_COURSES[y] for y in years]
    governance = [sum(GOVERNANCE[y].values()) for y in years]
    rows = {
        "Core staff": staff,
        "Language editors and fellowships": people_other,
        "Compute and hosting": compute,
        "Data and annotation": data,
        "Training and outreach": training,
        "Governance, audit and evaluation": governance,
    }
    subtotal = [sum(v[y] for v in rows.values()) for y in years]
    rows["Overheads and contingency (10%)"] = [subtotal[y] * OVERHEAD_RATE for y in years]
    return rows


def main():
    rows = budget()
    total_all = sum(sum(v) for v in rows.values())
    print("%-36s %8s %8s %8s %9s %6s" % ("Category (Tk crore)", "Year 1", "Year 2", "Year 3", "Total", "Share"))
    for k, v in rows.items():
        t = sum(v)
        print("%-36s %8.2f %8.2f %8.2f %9.2f %5.0f%%" % (k, v[0] / CRORE, v[1] / CRORE, v[2] / CRORE, t / CRORE, 100 * t / total_all))
    totals = [sum(v[y] for v in rows.values()) for y in range(3)]
    print("%-36s %8.2f %8.2f %8.2f %9.2f" % ("Total", totals[0] / CRORE, totals[1] / CRORE, totals[2] / CRORE, total_all / CRORE))
    print("Total in US dollars: %.2f million" % (total_all / USD_TO_BDT / 1e6))


if __name__ == "__main__":
    main()
