# Cross-document reconciliation report: October 2026

Compares what each BAPIL deliverable says on the topics that must agree, records the discrepancies found on 22 October 2026 and how each was resolved. The canonical values are in [`docs/source-of-truth.md`](../../docs/source-of-truth.md).

Columns: **BP-EN** and **BP-BN** = Technical Blueprint editions; **SUM** = Blueprint Summary (EN and BN); **MEMO** = Decision Memo (EN and BN, separate document); **REPO** = README, CITATION.cff, CHANGELOG, RELEASE_NOTES, Zenodo files; **WP/ES** = published White Paper and Executive Summary v1.0 (not edited). "Agrees" means the underlying claim is the same, not only the wording.

## 1. Reconciliation matrix

| # | Topic | BP-EN | BP-BN | SUM | MEMO | REPO | Discrepancy found | Canonical resolution |
|---|---|---|---|---|---|---|---|---|
| 1 | Project name and institutional status | Proposal (status table) but 1.7 said "is established" | Proposal; 1.7 conditional | Proposal | Old draft: proposal, but no "decisions already made" | README: "active initiative", no status line | EN 1.7 contradicted BN and the status table; README silent | Proposal everywhere; EN 1.7, 16.x, 20.x and Annex sentence made conditional; status line in README and Memo |
| 2 | Purpose and scope | Policy-intelligence research and capacity building; no policymaking, regulation or operational security | Same | Same | Same | Same | None | Unchanged |
| 3 | Governance structure | Steering Board, ERRC (veto within host statutes), TAB: proposed | Same | Same | Old draft: "binding veto" without the host limit | Same as BP | Memo overstated the veto | Memo states the host limit (U15) |
| 4 | Legal references | Consent "required"; cyber amendment on AI content | Same | Cyber law "revised" | "now set the rules" | Not detailed | Overstated relative to sources | Corrected in BP-EN, BP-BN, SUM; Memo says "frame"; verification table in `docs/legal-references.md` |
| 5 | Technical architecture | Twelve components, four layers | Same | Same in brief | Same in brief | `docs/technical-architecture.md` | None | Unchanged |
| 6 | Evaluation metrics | Recall@10 ≥ 0.85, citation precision ≥ 0.95, usefulness ≥ 4.0 from ≥ 30 users: proposed targets | Same | Same | Old draft: Recall@10 only | Same | Memo incomplete | Memo lists all three, labelled as targets |
| 7 | Benchmark status | BanglaPolicyQA planned (500 questions in v0) | Same | Same | Old draft: "500 questions released" as a target | README: "the open BanglaPolicyQA benchmark" among what the Blueprint specifies | Phrasing could be read as existing | Zenodo description and docs say "planned, not built"; Memo "version 0 (500 questions)" as a Year 1 deliverable |
| 8 | Software and release status | Code "to be issued in release v1.1.0"; tests run locally | Same | Same | Old draft: "released with the Blueprint" | README implied running CI | Memo and README overstated | Memo: "to be issued in repository release v1.1.0"; README: local test runs, CI not yet run |
| 9 | Budget totals | 20.43 base; 22.24 adjusted; 17.93 to 25.25 | Same (Bangla digits) | Same | Old draft: no adjusted case | README and docs: same | Memo incomplete | Memo includes adjusted case and 10% contingency |
| 10 | Annual costs | 4.73, 7.49, 8.21 | Same | Same | Year 1 about Tk 4.7 crore | Same | None | Unchanged |
| 11 | Timeline and milestones | Month 1 when MoU, host agreement and funding exist; January 2027 only with funds available; H2 2027 more realistic | Same | Same | Old draft: silent | Same | Memo silent on start-date dependency | Memo states it |
| 12 | Funding assumptions | No funding requested or approved; D2 includes committing or identifying Year 1 funding | Same | Same | Old draft D2 without funding | Same | Memo D2 outdated | Memo table identical to Table 57 |
| 13 | Risk register | Chapter 19, Annex U | Same | Key risks | Key risks (funding delay added) | n/a | Memo lacked funding risk | Added |
| 14 | Recommendations and decisions | D1 to D6 (Table 57) | Same | Same | Same after update | Same | See 12 | Resolved |
| 15 | Publication date | October 2026 | অক্টোবর ২০২৬ | Same | Same (from metadata) | Same; release date pending | None | Unchanged |
| 16 | Version number | Document 1.0; release v1.1.0 planned | Same | Same | Same | CITATION.cff 1.0 (last real release) | None (intentional difference explained in CITATION.cff comments) | Unchanged |
| 17 | Citation and reference details | [1] to [83] from WP; [84] to [126] new | Same (Bangla digits) | Same | Cites [85], [86], [88], [91], [125] with its own reference list | CITATION.cff valid | References [123] to [126] added | Resolved |
| 18 | Limitations and unresolved dependencies | Annex V (U1 to U16) | Same | Summary limitations | "Evidence required before implementation" (U1 to U3, U15, U16, D3) | README known limitations; RELEASE_NOTES | Memo lacked evidence needs | Added |
| 19 | National AI policy status | Jan 2026 draft; Q4 2026 drafting | Same | Same | Same | n/a | Draft v2.0 omitted everywhere | Added in BP, SUM, MEMO |
| 20 | Licences | CC BY 4.0 printed | Same | Same | Same | README: "may be CC"; WP Zenodo record MIT | Inconsistent records | Documented; author decision (`METADATA_TO_CONFIRM.md`) |
| 21 | Author affiliation | Independent Researcher, Bangladesh | স্বাধীন গবেষক, বাংলাদেশ | Same as BP | None stated | CITATION.cff, README author section and earlier Zenodo records: Université Paris-Saclay | Inconsistent | Author chose "Independent Researcher, Bangladesh" for the Blueprint; CITATION.cff and README at release: author decision |

## 2. English and Bangla editions

* **Method:** every multi-digit number (dates, amounts, thresholds, counts, citation numbers) was extracted from each chapter of the assembled English and Bangla files, Bangla digits converted, and the two sets compared chapter by chapter; tables are generated from the same Python data for both languages.
* **Result for the Blueprint:** one real difference found and fixed (the Bangla 14.2 bullet lacked the sentence on the January and February 2026 drafts). The remaining differences are layout values in raw LaTeX (row-spacing factors), numbers written as words in one language and as digits in the other ("Thirty" and "৩০"), and the version number repeated in the Bangla front matter.
* **Result for the Summary and the Decision Memo:** no differences in multi-digit numbers.
* **Legal corrections** were translated with the same scope and limitations, including "as reported", the disagreement between sources and "to be confirmed".
* **Terminology:** see the bilingual register in `docs/source-of-truth.md`; "মানবিক তত্ত্বাবধান" was corrected to "মানব-তত্ত্বাবধান".

## 3. White Paper and Executive Summary

The published White Paper and Executive Summary (v1.0, July 2026) are DOI-registered records and were not edited. Where the Blueprint refines or supersedes them, the Blueprint says so (Table 3 maps every White Paper chapter to the Blueprint). Known differences that readers should be aware of:

| Topic | White Paper / Executive Summary | Blueprint (canonical from October 2026) |
|---|---|---|
| Cyber-security law | Cites the Cyber Security Act, 2023 | Cyber Security Ordinance, 2025 converted into an Act in 2026, with amendments |
| Bangla foundation model | Proposed as a pilot (BPFM) | Staged; no model in 36 months unless Stage 1 is justified; Year 3 decision |
| Budget | No costed budget | Indicative 36-month budget with scenarios |
| Phasing | Four indicative phases (Executive Summary) | 36-month plan (a 12-month Phase 1 pilot, then Phase 2) implementing Phases 2 to 4 of the White Paper’s roadmap, plus a strategic roadmap to 2041 |
| Licence on Zenodo | White Paper record shows MIT (document says CC BY 4.0) | CC BY 4.0, to be confirmed |

## 4. Repository documentation

README, CITATION.cff, CHANGELOG, RELEASE_NOTES, the Zenodo description and metadata, and `docs/` were checked against the register. They describe the release, DOI, CI and benchmark as planned, the budget as an estimate and BAPIL as a proposal.
