# Data and methodology

This file explains where the claims in the BAPIL Technical Blueprint come from, how they were checked, and what is measured versus proposed. It does not introduce any dataset, survey or evaluation that does not exist.

## 1. Method of the Blueprint

The Blueprint was produced in six steps (Blueprint Section 1.6): review of the BAPIL series (each White Paper chapter mapped to a design question); review of the legal, policy and indicator context; design against reference frameworks (OECD AI Principles, UNESCO Recommendation, NIST AI RMF, ISO/IEC 42001, the EU AI Act and Canada’s Directive on Automated Decision-Making); implementation of the core ideas in code as a test of the design; planning and review with explicit assumptions; and an evidence check in October 2026, whose results are in Annex P (Table 60) and the unresolved-items register (Annex V, Table 68).

No primary data was collected: there were no interviews, surveys, focus groups or user studies, and no personal data was processed.

## 2. Source selection and evidence verification

* **Preference used in the October 2026 evidence check:** official sources where they could be read (several official legal and policy sites block automated retrieval), then international organisations, peer-reviewed or institutional publications, established news media and specialist commentary.
* **Recording:** every source has a URL and an access date in the bibliography (new references in `blueprint/src/refs_new.md`; the 40 entries taken from the White Paper bibliography, `reports/BAPIL_White_Paper_v1.md`, are marked with an asterisk in the Blueprint’s reference list).
* **Classification:** each important claim is classed in Table 60 as a verified fact, source-reported fact, research finding, design recommendation, assumption or estimate, with the evidence and how the text presents it.
* **Disagreement:** where sources disagree (for example on the content of the June 2026 cyber-security amendment), the documents say so rather than choose one.
* **Limits:** all references were checked in October 2026: the new references when they were added, and the 40 entries taken from the White Paper on 22 October 2026, when 13 were corrected (`blueprint/review/REFERENCE_VERIFICATION.md`). The Act numbers, Gazette dates and commencement of the 2026 laws were confirmed from official sources, but their provisions could be read only through database texts, not the Gazette texts; confirmation by counsel is still open (unresolved items U1 to U3).

## 3. Legal research

The numbers, titles and Gazette dates of the 2026 Acts were confirmed from official sources (the Legislative Division's list of Acts and the Gazette copies published by the ICT Division). Their provisions were read through the official laws database texts, because the Gazette copies use a legacy font encoding that could not be read automatically. Enactment is distinguished from commencement, statutory requirements are distinguished from BAPIL’s own safeguards, and an independent review by qualified Bangladesh counsel is required in Phase 0, before the host agreement is signed. See [`docs/legal-references.md`](docs/legal-references.md).

## 4. Budget

The budget is a planning estimate built from stated assumptions (exchange rate, inflation, pay levels, quantities and unit costs) in `blueprint/src/budget_model.py`; every printed figure is computed, not typed. An independent spreadsheet implementation (`blueprint/data/BAPIL_Budget_Model.xlsx`) agrees to within Tk 1. Known omissions are listed and costed in an adjusted scenario. See [`docs/financial-model.md`](docs/financial-model.md).

## 5. Evaluation

| | Status |
|---|---|
| Metric definitions, thresholds, sample sizes, annotation and decision rules | Proposed in Table 28, Annex R (Table 63) and Annex K |
| BanglaPolicyQA benchmark | **Planned, not built** |
| Pilot results | **None**; no pilot exists |
| Demonstration evaluation | Measured locally at every build on 24 answerable and 6 out-of-scope questions written by the author over BAPIL’s own documents; development results only |
| Unit tests | 49 tests, passing locally; no public CI record yet |

See [`docs/evaluation-methodology.md`](docs/evaluation-methodology.md).

## 6. Data used by the reference implementation

| Data | Origin | Personal data | Licence |
|---|---|---|---|
| Demonstration corpus | The White Paper, Executive Summary, Blueprint and Summary (Markdown) | No (author’s name only) | CC BY 4.0 |
| Test fixtures | Short fictitious sample notes written for the tests | No | MIT (with the code) |
| Demonstration questions | Written by the author | No | CC BY 4.0 |
| Example registry and risk records | Illustrative records for the planned pilots P1 to P6 and hypothetical risk cases | No | MIT (with the code) |

The planned pilots would start with documents the state has already published (data class DC0). Any use of personal data would require a documented lawful basis, a DPIA and ERRC approval, and is limited to pilot P3 in de-identified, aggregate form.

## 7. Reproducibility

All tables, figures, budget outputs and documents are regenerated from source by one script; see [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).
