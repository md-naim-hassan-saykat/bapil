#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write the BAPIL budget model as an editable Excel workbook with live formulas.

The workbook re-implements the calculation in budget_model.py with spreadsheet formulas,
so that a reader can change an assumption and see every total update, and so that the
Python model can be checked against an independent implementation (see --check).

Usage:
    python3 make_budget_workbook.py OUT.xlsx           # write the workbook (formulas, no cached values)
    python3 make_budget_workbook.py --check OUT.xlsx   # compare recalculated values with budget_model.py

Writing needs openpyxl. Cached values are added by recalculating the file in a spreadsheet
program (for example LibreOffice); --check needs a recalculated file.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import budget_model as bm  # noqa: E402

SCEN = ["low", "base", "adjusted", "high"]
SCEN_LABEL = {"low": "Low", "base": "Base", "adjusted": "Adjusted base", "high": "High"}
CALC = {s: "Calc_" + SCEN_LABEL[s].split()[0] for s in SCEN}       # Calc_Low, Calc_Base, Calc_Adjusted, Calc_High
PARAMS = [  # key, label, format
    ("usd_to_bdt", "Exchange rate (Tk per USD)", "#,##0.00"),
    ("escalation", "Annual escalation of taka costs (Years 2 and 3)", "0.0%"),
    ("ramp_y1", "Average share of Year 1 posts filled", "0.0%"),
    ("staff_factor", "Multiplier on staff costs", "0.00"),
    ("equipment_factor", "Multiplier on equipment prices", "0.00"),
    ("overhead_rate", "Host overhead on direct costs", "0.0%"),
    ("contingency_rate", "Contingency on direct costs", "0.0%"),
    ("adaptation_compute_usd", "Stage 1 adaptation compute, Year 2 (USD)", "#,##0"),
    ("omitted_items", "Include known omissions (1 = yes, 0 = no)", "0"),
]
TK = '#,##0;(#,##0);"-"'
CR = '0.00;(0.00);"-"'


def build(path):
    from openpyxl import Workbook
    from openpyxl.comments import Comment
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter

    F = "Arial"
    blue = Font(name=F, color="0000FF")
    black = Font(name=F)
    green = Font(name=F, color="008000")
    bold = Font(name=F, bold=True)
    title = Font(name=F, bold=True, size=13)
    head = Font(name=F, bold=True, color="FFFFFF")
    headfill = PatternFill("solid", fgColor="1F3864")
    keyfill = PatternFill("solid", fgColor="FFFF00")
    wb = Workbook()

    def header(ws, row, labels, widths=None):
        for i, lab in enumerate(labels, 1):
            c = ws.cell(row=row, column=i, value=lab)
            c.font, c.fill = head, headfill
            c.alignment = Alignment(wrap_text=True, vertical="center")
        for i, w in enumerate(widths or [], 1):
            ws.column_dimensions[get_column_letter(i)].width = w

    # ------------------------------------------------------------------ README
    ws = wb.active
    ws.title = "README"
    text = [
        ("BAPIL Technical Blueprint: indicative 36-month budget model", title),
        ("Version 1.0, October 2026. Planning estimate only: not a quotation, not an approved budget and not secured funding.", bold),
        ("", black),
        ("What this workbook is", bold),
        ("A spreadsheet version of blueprint/src/budget_model.py, which produces Tables 49, 50, 61 and 62 of the Blueprint.", black),
        ("The formulas re-implement the Python model independently; the build checks that both give the same results.", black),
        ("", black),
        ("How to use it", bold),
        ("Change the blue cells on the Assumptions sheet. Every Calc_ sheet and the Summary sheet update automatically.", black),
        ("Scenario levers are in the Low, Base, Adjusted base and High columns of the Assumptions sheet (yellow cells are the key ones).", black),
        ("If you change an assumption, change it in budget_model.py too, so that the published tables stay in step.", black),
        ("", black),
        ("Colour legend", bold),
        ("Blue text: input or assumption.  Black text: formula.  Green text: link to another sheet.  Yellow fill: key scenario lever.", black),
        ("", black),
        ("Units", bold),
        ("Amounts are in Bangladeshi taka (Tk) unless a column says Tk crore. 1 crore = 10,000,000; 1 lakh = 100,000.", black),
        ("Equipment and staff computers are priced in US dollars and converted at the exchange rate; they are not escalated.", black),
        ("", black),
        ("Not modelled here", bold),
        ("The reconciliation with the initial planning estimate (Table 61) and the sensitivity tests are computed only in budget_model.py", black),
        ("(see data/budget_bridge.csv and data/budget_sensitivity.csv).", black),
        ("", black),
        ("Sources of the assumptions", bold),
        ("Exchange rate: Bangladesh Bank weighted average rate, Tk 123.65 per USD on 19 October 2026 (rounded to 124).", black),
        ("Escalation: point-to-point CPI inflation of 8.34% in September 2026 (BBS, as reported by the Dhaka Tribune).", black),
        ("Staff costs: planning assumptions above the Ninth National Pay Scale (2026) equivalents; see Section 17.5 of the Blueprint.", black),
        ("All other quantities and unit costs are planning assumptions stated in Chapter 17 and Annex Q of the Blueprint.", black),
        ("", black),
        ("Licence: CC BY 4.0. Generated by blueprint/src/make_budget_workbook.py.", black),
    ]
    for i, (t, f) in enumerate(text, 1):
        ws.cell(row=i, column=1, value=t).font = f
    ws.column_dimensions["A"].width = 130

    # ------------------------------------------------------------------ Assumptions
    wa = wb.create_sheet("Assumptions")
    wa["A1"] = "Scenario levers"
    wa["A1"].font = title
    header(wa, 2, ["Parameter", "Low", "Base", "Adjusted base", "High", "Note"], [52, 14, 14, 14, 14, 70])
    notes = {
        "usd_to_bdt": "Base: Bangladesh Bank weighted average rate, 19 October 2026 (Tk 123.65), rounded",
        "escalation": "Base: September 2026 CPI inflation 8.34% (BBS, as reported), rounded",
        "omitted_items": "Engagement events, P5 survey data, travel, open-access fees and staff computers (Section 17.2)",
        "contingency_rate": "Adjusted base and High use 10%, as recommended in Table 49",
        "adaptation_compute_usd": "High case only: compute for Stage 1 adaptation if national compute is unavailable",
    }
    P = {}  # parameter key -> row
    for r, (key, label, fmt) in enumerate(PARAMS, 3):
        wa.cell(row=r, column=1, value=label).font = black
        for j, s in enumerate(SCEN, 2):
            v = bm.SCENARIOS[s][key]
            c = wa.cell(row=r, column=j, value=int(v) if isinstance(v, bool) else v)
            c.font, c.number_format = blue, fmt
            if key in ("staff_factor", "equipment_factor", "escalation", "usd_to_bdt", "contingency_rate"):
                c.fill = keyfill
        wa.cell(row=r, column=6, value=notes.get(key, "")).font = black
        P[key] = r
    scol = {s: get_column_letter(j) for j, s in enumerate(SCEN, 2)}

    # unit inputs shared by all scenarios
    r = len(PARAMS) + 5
    wa.cell(row=r, column=1, value="Unit inputs (same in every scenario; Year 1 prices)").font = title
    r += 1
    header(wa, r, ["Input", "Year 1", "Year 2", "Year 3", "Unit", "Note"])
    U = {}

    def unit(key, label, vals, unit_lab, note="", fmt=TK):
        nonlocal r
        r += 1
        wa.cell(row=r, column=1, value=label).font = black
        if not isinstance(vals, (tuple, list)):
            vals = (vals,)
        for j, v in enumerate(vals, 2):
            c = wa.cell(row=r, column=j, value=v)
            c.font, c.number_format = blue, fmt
        wa.cell(row=r, column=5, value=unit_lab).font = black
        wa.cell(row=r, column=6, value=note).font = black
        U[key] = r

    for role in bm.MONTHLY_COST:
        unit("mc:" + role, "Monthly cost per FTE: " + role, bm.MONTHLY_COST[role], "Tk per month", "Fully loaded")
    for role in bm.FTE:
        unit("fte:" + role, "FTE: " + role, bm.FTE[role], "FTE", "Table 16", "0.0")
    unit("editors", "Part-time Bangla language editors", bm.LANGUAGE_EDITORS, "Tk per year")
    unit("fellows", "Graduate fellows", bm.FELLOWS, "persons", "", "0")
    unit("stipend", "Fellowship stipend", bm.FELLOW_STIPEND_MONTHLY, "Tk per month")
    unit("equip", "Equipment (servers, GPU inference servers, storage)", bm.EQUIPMENT_USD, "USD",
         "Y1: 3 servers, 2 GPU servers, 20 TB storage; Y2: staging and recovery; Y3: replacement and storage", "#,##0")
    unit("hosting", "Hosting, power, bandwidth and licences", bm.HOSTING_OPS, "Tk per year")
    unit("bench", "Benchmark questions with gold passages", bm.BENCHMARK_ITEMS, "questions", "", "#,##0")
    unit("bench_cost", "Cost per benchmark question", bm.COST_PER_ITEM, "Tk")
    unit("oos", "Out-of-scope questions for abstention tests", bm.OUT_OF_SCOPE_ITEMS, "questions", "", "#,##0")
    unit("oos_cost", "Cost per out-of-scope question", bm.COST_PER_OUT_OF_SCOPE, "Tk")
    unit("cit", "Citation-support judgements", bm.CITATION_JUDGEMENTS, "judgements", "", "#,##0")
    unit("cit_cost", "Cost per judgement", bm.COST_PER_JUDGEMENT, "Tk")
    unit("ocr", "OCR correction", bm.OCR_CORRECTION, "Tk per year")
    unit("agree", "Data agreements and custodian liaison", bm.DATA_AGREEMENTS, "Tk per year")
    unit("trained", "Officials trained", bm.OFFICIALS_TRAINED, "persons", "", "#,##0")
    unit("per_part", "Cost per participant", bm.COST_PER_PARTICIPANT, "Tk")
    unit("spec", "Specialist courses and bilingual materials", bm.SPECIALIST_COURSES, "Tk per year")
    gov_items = sorted({k for g in bm.GOVERNANCE for k in g})
    for k in gov_items:
        unit("gov:" + k, k + (" (one-time)" if k in bm.ONE_TIME_GOVERNANCE else ""),
             tuple(bm.GOVERNANCE[y].get(k, 0) for y in range(3)), "Tk")
    unit("omit", "Allowance for known omissions (events, survey data, travel, open-access fees)", bm.OMITTED_ALLOWANCE, "Tk per year")
    unit("newstaff", "New staff needing a computer", bm.NEW_STAFF, "persons", "", "0")
    unit("computer", "Computer per new staff member", bm.COMPUTER_USD, "USD", "", "#,##0")
    wa.freeze_panes = "B3"

    def A(key, col):  # absolute reference to a unit input
        return "Assumptions!$%s$%d" % (col, U[key])

    def S(key, s):    # absolute reference to a scenario lever
        return "Assumptions!$%s$%d" % (scol[s], P[key])

    # ------------------------------------------------------------------ Calc sheets
    ycols = ["B", "C", "D"]
    totals_ref = {}
    for s in SCEN:
        wc = wb.create_sheet(CALC[s])
        wc["A1"] = "%s scenario: line items (Tk)" % SCEN_LABEL[s]
        wc["A1"].font = title
        header(wc, 2, ["Line item", "Year 1", "Year 2", "Year 3", "Total", "Category", "One-time"], [58, 16, 16, 16, 17, 34, 10])
        row = 2
        cat_rows = {c: [] for c in bm.CATEGORIES}

        def esc(y):
            return "(1+%s)^%d" % (S("escalation", s), y)

        def line(cat, label, formulas, one_time):
            nonlocal row
            row += 1
            wc.cell(row=row, column=1, value=label).font = black
            for j, f in enumerate(formulas):
                c = wc.cell(row=row, column=2 + j, value="=" + f)
                c.font, c.number_format = green, TK
            c = wc.cell(row=row, column=5, value="=SUM(B%d:D%d)" % (row, row))
            c.font, c.number_format = black, TK
            wc.cell(row=row, column=6, value=cat).font = black
            wc.cell(row=row, column=7, value="yes" if one_time else "no").font = black
            cat_rows[cat].append(row)

        staff = []
        for y, col in enumerate(ycols):
            terms = "+".join("%s*12*%s" % (A("mc:" + rr, "B"), A("fte:" + rr, col)) for rr in bm.FTE)
            f = "(%s)*%s*%s" % (terms, S("staff_factor", s), esc(y))
            if y == 0:
                f += "*%s" % S("ramp_y1", s)
            staff.append(f)
        line("Core staff", "Core staff salaries and on-costs", staff, False)
        line("Language editors and fellowships", "Part-time Bangla language editors",
             ["%s*%s" % (A("editors", c), esc(y)) for y, c in enumerate(ycols)], False)
        line("Language editors and fellowships", "Graduate fellowships",
             ["%s*%s*12*%s" % (A("fellows", c), A("stipend", "B"), esc(y)) for y, c in enumerate(ycols)], False)
        line("Compute and hosting", "Servers, GPUs and storage",
             ["%s*%s*%s" % (A("equip", c), S("equipment_factor", s), S("usd_to_bdt", s)) for c in ycols], True)
        line("Compute and hosting", "Hosting, power, bandwidth and licences",
             ["%s*%s" % (A("hosting", c), esc(y)) for y, c in enumerate(ycols)], False)
        line("Compute and hosting", "Stage 1 adaptation compute (if no national compute)",
             ["0", "%s*%s" % (S("adaptation_compute_usd", s), S("usd_to_bdt", s)), "0"], True)
        line("Compute and hosting", "Staff computers (known omission)",
             ["%s*%s*%s*%s" % (S("omitted_items", s), A("newstaff", c), A("computer", "B"), S("usd_to_bdt", s)) for c in ycols], True)
        line("Data and annotation", "Benchmark questions and gold passages",
             ["%s*%s*%s" % (A("bench", c), A("bench_cost", "B"), esc(y)) for y, c in enumerate(ycols)], True)
        line("Data and annotation", "Out-of-scope questions for abstention tests",
             ["%s*%s*%s" % (A("oos", c), A("oos_cost", "B"), esc(y)) for y, c in enumerate(ycols)], True)
        line("Data and annotation", "Citation-support judgements",
             ["%s*%s*%s" % (A("cit", c), A("cit_cost", "B"), esc(y)) for y, c in enumerate(ycols)], False)
        line("Data and annotation", "OCR correction",
             ["%s*%s" % (A("ocr", c), esc(y)) for y, c in enumerate(ycols)], False)
        line("Data and annotation", "Data agreements and custodian liaison",
             ["%s*%s" % (A("agree", c), esc(y)) for y, c in enumerate(ycols)], False)
        line("Training and outreach", "Training of officials",
             ["%s*%s*%s" % (A("trained", c), A("per_part", "B"), esc(y)) for y, c in enumerate(ycols)], False)
        line("Training and outreach", "Specialist courses and bilingual materials",
             ["%s*%s" % (A("spec", c), esc(y)) for y, c in enumerate(ycols)], False)
        line("Training and outreach", "Engagement events, P5 survey data, travel and open-access fees (known omission)",
             ["%s*%s*%s" % (S("omitted_items", s), A("omit", "B"), esc(y)) for y in range(3)], False)
        for k in gov_items:
            line("Governance, audit and evaluation", k,
                 ["%s*%s" % (A("gov:" + k, c), esc(y)) for y, c in enumerate(ycols)], k in bm.ONE_TIME_GOVERNANCE)

        row += 2
        wc.cell(row=row, column=1, value="Summary by category").font = bold
        header(wc, row + 1, ["Row", "Year 1", "Year 2", "Year 3", "Total", "Share of total"])
        row += 1
        first = row + 1
        crow = {}
        for cat in bm.CATEGORIES:
            row += 1
            wc.cell(row=row, column=1, value=cat).font = black
            for j, col in enumerate(ycols + ["E"]):
                cells = ",".join("%s%d" % (col, rr) for rr in cat_rows[cat])
                c = wc.cell(row=row, column=2 + j, value="=SUM(%s)" % cells)
                c.font, c.number_format = black, TK
            crow[cat] = row
        row += 1
        direct = row
        wc.cell(row=row, column=1, value="Direct costs").font = bold
        for j, col in enumerate(ycols + ["E"]):
            c = wc.cell(row=row, column=2 + j, value="=SUM(%s%d:%s%d)" % (col, first, col, row - 1))
            c.font, c.number_format = bold, TK
        row += 1
        wc.cell(row=row, column=1, value="Host overheads").font = black
        for j, col in enumerate(ycols):
            c = wc.cell(row=row, column=2 + j, value="=%s%d*%s" % (col, direct, S("overhead_rate", s)))
            c.font, c.number_format = green, TK
        wc.cell(row=row, column=5, value="=SUM(B%d:D%d)" % (row, row)).number_format = TK
        over = row
        row += 1
        wc.cell(row=row, column=1, value="Contingency").font = black
        for j, col in enumerate(ycols):
            c = wc.cell(row=row, column=2 + j, value="=%s%d*%s" % (col, direct, S("contingency_rate", s)))
            c.font, c.number_format = green, TK
        wc.cell(row=row, column=5, value="=SUM(B%d:D%d)" % (row, row)).number_format = TK
        cont = row
        row += 1
        tot = row
        wc.cell(row=row, column=1, value="Total").font = bold
        for j, col in enumerate(ycols + ["E"]):
            c = wc.cell(row=row, column=2 + j, value="=%s%d+%s%d+%s%d" % (col, direct, col, over, col, cont))
            c.font, c.number_format = bold, TK
        for rr in list(crow.values()) + [direct, over, cont, tot]:
            c = wc.cell(row=rr, column=6, value="=IF($E$%d=0,0,E%d/$E$%d)" % (tot, rr, tot))
            c.number_format = "0.0%"
        totals_ref[s] = {"cat": crow, "over": over, "cont": cont, "direct": direct, "total": tot}
        wc.freeze_panes = "B3"

    # ------------------------------------------------------------------ Summary
    wsu = wb.create_sheet("Summary", 1)
    wsu["A1"] = "Summary (Tk crore)"
    wsu["A1"].font = title
    wsu["A2"] = "All values are formulas linked to the Calc_ sheets. Planning estimates, not approved funding."
    header(wsu, 4, ["Base case by category (Table 50)", "Year 1", "Year 2", "Year 3", "Total"], [60, 14, 14, 14, 14])
    b = totals_ref["base"]
    rr = 4
    rows = [(c, b["cat"][c]) for c in bm.CATEGORIES] + [("Host overheads", b["over"]), ("Contingency", b["cont"]), ("Total", b["total"])]
    for lab, src in rows:
        rr += 1
        wsu.cell(row=rr, column=1, value=lab).font = bold if lab == "Total" else black
        for j, col in enumerate(["B", "C", "D", "E"]):
            c = wsu.cell(row=rr, column=2 + j, value="=%s!%s%d/10000000" % (CALC["base"], col, src))
            c.font, c.number_format = green, CR
    rr += 2
    header(wsu, rr, ["Scenarios (Table 62)", "Year 1", "Year 2", "Year 3", "Total"])
    for s in SCEN:
        rr += 1
        wsu.cell(row=rr, column=1, value=SCEN_LABEL[s]).font = black
        for j, col in enumerate(["B", "C", "D", "E"]):
            c = wsu.cell(row=rr, column=2 + j, value="=%s!%s%d/10000000" % (CALC[s], col, totals_ref[s]["total"]))
            c.font, c.number_format = green, CR
    rr += 2
    header(wsu, rr, ["Check against the published Blueprint (rounded to 0.01 crore)", "Model", "Published", "Difference", ""])
    published = [("Base case, 36-month total (Table 50)", "base", 20.43), ("Low scenario total (Table 62)", "low", 17.93),
                 ("Adjusted base case total (Table 62)", "adjusted", 22.24), ("High scenario total (Table 62)", "high", 25.25)]
    for lab, s, val in published:
        rr += 1
        wsu.cell(row=rr, column=1, value=lab).font = black
        c = wsu.cell(row=rr, column=2, value="=ROUND(%s!E%d/10000000,2)" % (CALC[s], totals_ref[s]["total"]))
        c.font, c.number_format = green, CR
        c = wsu.cell(row=rr, column=3, value=val)
        c.font, c.number_format = blue, CR
        c.comment = Comment("Value printed in the Blueprint, Version 1.0 (October 2026)", "BAPIL")
        c = wsu.cell(row=rr, column=4, value="=B%d-C%d" % (rr, rr))
        c.font, c.number_format = black, CR
    wb.save(path)
    print("wrote", path)


def check(path):
    """Compare the recalculated workbook with budget_model.py (tolerance Tk 1)."""
    from openpyxl import load_workbook
    wb = load_workbook(path, data_only=True)
    bad = 0
    for s in SCEN:
        ws = wb[CALC[s]]
        tot_row = max(r for r in range(1, ws.max_row + 1) if ws.cell(row=r, column=1).value == "Total")
        model_y, model_t = bm.totals(bm.SCENARIOS[s])
        got = [ws.cell(row=tot_row, column=c).value for c in (2, 3, 4, 5)]
        if any(v is None for v in got):
            sys.exit("no cached values: recalculate %s first" % path)
        for g, m in zip(got, list(model_y) + [model_t]):
            if abs(g - m) > 1:
                bad += 1
        print("%-9s workbook %s | model %s" % (s, ["%.2f" % (g / bm.CRORE) for g in got],
                                               ["%.2f" % (m / bm.CRORE) for m in list(model_y) + [model_t]]))
    ws = wb[CALC["base"]]
    rows = bm.budget()
    for r in range(1, ws.max_row + 1):
        lab = ws.cell(row=r, column=1).value
        if lab in rows:
            for y in range(3):
                if abs(ws.cell(row=r, column=2 + y).value - rows[lab][y]) > 1:
                    bad += 1
                    print("mismatch", lab, y)
    print("differences larger than Tk 1:", bad)
    return bad


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--check":
        sys.exit(1 if check(sys.argv[2]) else 0)
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    build(sys.argv[1])
