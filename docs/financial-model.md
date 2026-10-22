# Financial model

The indicative 36-month budget of the Technical Blueprint (Chapter 17, Tables 49, 50, 61 and 62, Annex Q) is a **planning estimate**. It is not a quotation, not an approved budget and not secured funding: no funding has been requested, approved or committed.

## 1. Files

| File | Role |
|---|---|
| [`blueprint/src/budget_model.py`](../blueprint/src/budget_model.py) | Canonical model. Every budget figure printed in the Blueprint is computed here from stated assumptions |
| [`blueprint/data/*.csv`](../blueprint/data/) | Model outputs written by the build: line items, categories, scenarios, bridge, sensitivity, assumptions |
| [`blueprint/data/BAPIL_Budget_Model.xlsx`](../blueprint/data/BAPIL_Budget_Model.xlsx) | Editable workbook with live formulas (612 formulas, four scenario sheets). It re-implements the model independently; inputs are in blue on the Assumptions sheet |
| [`blueprint/src/make_budget_workbook.py`](../blueprint/src/make_budget_workbook.py) | Writes the workbook and checks it against the Python model (`--check`) |

To change an assumption, edit `budget_model.py` and rebuild; the published tables, CSV files and Summary follow. Then regenerate the workbook (`python3 blueprint/src/make_budget_workbook.py blueprint/data/BAPIL_Budget_Model.xlsx`), recalculate it in LibreOffice or Excel, and run the check.

## 2. Results (recalculated 22 October 2026)

| Tk crore | Year 1 | Year 2 | Year 3 | Total |
|---|---:|---:|---:|---:|
| Base case | 4.73 | 7.49 | 8.21 | 20.43 |
| Low scenario | 4.20 | 6.58 | 7.16 | 17.93 |
| Adjusted base case (known omissions, 10% contingency) | 5.29 | 8.10 | 8.85 | 22.24 |
| High scenario | 5.76 | 9.46 | 10.03 | 25.25 |

The base case is Tk 204,264,136 unrounded (about USD 1.65 million at Tk 124 per USD). Independently rounded rows of Table 50 add to 4.74, 7.48, 8.22 and 20.42; the difference from the printed totals is rounding only, and the Table 50 note says so.

## 3. Independent check

The workbook formulas were written separately from the Python code and recalculated in LibreOffice (612 formulas, no errors). For all four scenarios the annual totals and 36-month totals agree with `budget_model.py` to within Tk 1, and every base-case category row agrees by year. The figures quoted in the Blueprint, the Summary and the Decision Memo (Tk 20.4, 17.9, 22.2 and 25.3 crore; Tk 4.7 crore in Year 1) are roundings of these values.

## 4. Main assumptions

| Assumption | Base value | Source or basis |
|---|---|---|
| Exchange rate | Tk 124 per USD | Bangladesh Bank weighted average, Tk 123.65 on 19 October 2026 |
| Escalation of taka costs | 8% a year in Years 2 and 3 | September 2026 CPI inflation of 8.34% (BBS, as reported) |
| Year 1 staffing | 75% of posts filled on average | Recruitment in months 1 to 6 |
| Staff | About 9 FTE in Year 1, 19 by Year 3; fully loaded monthly costs above the 2026 pay-scale equivalents | Planning assumption (Section 17.5) |
| Overheads; contingency | 10%; 5% of direct costs (10% recommended, adjusted case) | Planning assumption |
| Equipment | Servers, two GPU inference servers and storage, priced in USD, not escalated | Planning assumption; quotations needed |

Taxes and duties are not modelled separately: equipment is priced before any import duty or VAT, and the sensitivity test "equipment 25% dearer" (+Tk 0.71 crore) covers them. Known omissions (engagement events, P5 survey data, travel, open-access fees, staff computers) are excluded from the base case and included in the adjusted case (unresolved item U16). The month-6 feasibility and costing study (Decision D5) is meant to replace these assumptions with the host’s salary scale, quotations and agreed rates.

## 5. Conditional national scale-up and jobs (Years 4 to 8)

Added on 22 October 2026 at the author's request, after a comparison with the Tk 192.66 crore KOICA-supported AI hub project. The 36-month budget is unchanged; the scale-up is a separate, conditional envelope that applies only if the pilots pass Gate G4, the final evaluation is positive and the authorities decide to scale up (Blueprint Section 17.3, Annex W, Tables 69 and 70). It is not part of the funding requested.

| Tk crore | Year 4 | Year 5 | Year 6 | Year 7 | Year 8 | Total |
|---|---:|---:|---:|---:|---:|---:|
| Scale-up total | 25.50 | 36.08 | 45.26 | 51.11 | 60.90 | 218.85 |

With the 36-month plan (20.43), the eight-year total is about Tk 239 crore. Direct posts (full-time equivalents) rise from 9, 15 and 19 in Years 1 to 3 to 58, 88, 105, 114 and 118 in Years 4 to 8; graduate fellows from 6, 10 and 12 to 20, 30 and then 40 a year; officials trained reach about 5,500 in total.

Method: the same fully loaded unit costs as the 36-month model (Table 49), escalated by 8% a year from Year 1; 10% host overheads and a 10% contingency. Components and quantities (central lab 25 to 45 posts, four divisional university nodes of five posts plus Tk 25 lakh running costs each, 6 to 20 analysts placed in agencies, up to 30 annotators at Tk 45,000 a month with supervisors, national inference platform hardware priced in USD, Tk 50 lakh per agency joining federated search, governance and two independent evaluations) are set in `blueprint/src/budget_model.py` (`SU_*` constants, functions `scaleup` and `jobs`) and exported to `blueprint/data/scaleup_by_category.csv` and `jobs_and_skills.csv`. They are planning assumptions made before any pilot result (unresolved item U17); the Excel workbook covers the 36-month model only.
