# Source-of-truth register

This register lists the canonical statements and values that every BAPIL deliverable must agree on. It controls consistency; it is not a substitute for the documents. When a value changes, change it in the authoritative source given here, rebuild, and update every document listed.

Last verified: 29 October 2026, in a project-wide audit (branch `blueprint-v1.0`, not yet pushed); dates in individual rows give when an external source was last checked. Verification status key: **Verified** (checked against a primary or official source, or recomputed), **Reported** (secondary sources only), **Design** (a proposal or recommendation by the author), **Pending** (not yet true; must not be stated as done), **To confirm** (the author must supply or decide).

Abbreviations for the documents: BP = Technical Blueprint (EN and BN), SUM = Blueprint Summary (EN and BN), WP = White Paper v1.0, ES = Executive Summary v1.0, REPO = README, CITATION.cff, CHANGELOG, RELEASE_NOTES and the Zenodo files.

## 1. Identity, publication and versioning

| Item | Canonical statement or value | Evidence or authoritative source | Status | Documents |
|---|---|---|---|---|
| Project name | Bangladesh AI Policy & Innovation Lab (BAPIL); Bangla: বাংলাদেশ এআই পলিসি অ্যান্ড ইনোভেশন ল্যাব | `blueprint/src/metadata.json` | Verified | all |
| Blueprint title (EN) | Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint | `metadata.json` `title_en`; title page; PDF metadata | Verified | BP, SUM, REPO |
| Blueprint title (BN) | বাংলাদেশ এআই পলিসি অ্যান্ড ইনোভেশন ল্যাব (BAPIL): টেকনিক্যাল ব্লুপ্রিন্ট | `metadata.json` `title_bn` | Verified | BP, SUM, REPO |
| Public PDF filenames | `BAPIL_Technical_Blueprint_en.pdf`, `BAPIL_Technical_Blueprint_bn.pdf` (Summary: `BAPIL_Blueprint_Summary_{en,bn}.pdf`) | `releases/v1.1/` | Verified | REPO, Zenodo files |
| Displayed publication date | October 2026 / অক্টোবর ২০২৬ (no day) | `metadata.json` `date_en`, `date_bn`; PDF dates `D:202610` | Verified | BP, SUM |
| Document version | 1.0 | `metadata.json` `version` | Verified | BP, SUM, REPO |
| Repository release | `v1.1.0`: **planned, not created**. Existing tags: `v1.0`, `v1.0.1` (checked on GitHub, 22 October 2026) | `git ls-remote --tags origin`; GitHub releases page | Pending | BP (Sections 1.4, 11.1, Annex D), REPO |
| Blueprint DOI | Technical Blueprint **10.5281/zenodo.23587901**; Blueprint Summary **10.5281/zenodo.23587919** (separate records). Reserved on Zenodo by the author; they resolve once the records are published. Printed on the title pages, document information, citation and Table 1; `metadata.json` keys `doi` and `summary_doi` | Author (23 October 2026); `metadata.json` | Reserved, not yet published | BP, SUM, REPO |
| White Paper DOI | 10.5281/zenodo.21363967 (record version v1.0.1, published 14 July 2026, licence recorded as MIT) | Zenodo record, checked 22 October 2026 | Verified | BP, REPO, CITATION.cff |
| Executive Summary DOI | 10.5281/zenodo.21441172 (version 1.0, published 21 July 2026, CC BY 4.0, languages English and Bengali) | Zenodo record, checked 22 October 2026 | Verified | BP, REPO, CITATION.cff |
| Concept DOI | 10.5281/zenodo.21360565, which currently resolves to the White Paper record | Zenodo, checked 22 October 2026 | Verified | REPO, CITATION.cff |
| Author | Md Naim Hassan Saykat, ORCID 0009-0007-5270-3970 | Zenodo records; `metadata.json` | Verified | all |
| Author affiliation | **"Independent Researcher, Bangladesh"** in the Blueprint, Summary, `metadata.json`, Zenodo metadata, `CITATION.cff` and the README author section (decided 29 October 2026). The two earlier Zenodo records (White Paper, Executive Summary) say Université Paris-Saclay, which was correct when they were published | Author’s decision; `metadata.json`; `CITATION.cff` | Verified | BP (avoids an affiliation), CITATION.cff, Zenodo metadata |
| Licence of the Blueprint documents, figures, tables and data | CC BY 4.0, as printed in the Blueprint; confirmed by the author on 29 October 2026 | `metadata.json`; `blueprint/SOURCES_AND_LICENCES.md` | Verified | BP, SUM, REPO, Zenodo files |
| Licence of the code | MIT (`LICENSE`) | `LICENSE` | Verified | REPO |

## 2. Institutional status and governance

| Item | Canonical statement | Evidence | Status | Documents |
|---|---|---|---|---|
| Institutional status | BAPIL is a **proposal**. No institution has been created, no host selected, no MoU signed, no funding requested or approved | No evidence of establishment found; Blueprint Table 65 | Design | BP (status table, 1.7, Ch. 5, 16), SUM, REPO |
| Proposed model | University-anchored lab under an MoU with the ICT Division (Option C) | BP Chapter 5 | Design | BP, SUM |
| Governance bodies | Steering Board, Ethics and Risk Review Committee (ERRC), Technical Architecture Board: **proposed, not constituted** | BP Annex S, Table 64 | Design | BP, SUM |
| ERRC veto | Binds BAPIL through the charter; binds the host only as far as the host’s statutes and the host agreement allow (unresolved item U15) | BP Section 5.3 | Design | BP, SUM |
| Decisions already made by any authority | None | No evidence of any decision | Verified (absence of evidence recorded) | BP |
| Decisions requested | D1 to D6 as in BP Table 57 (D2 includes committing or identifying Year 1 funding of about Tk 4.7 crore) | BP Table 57 | Design | BP, SUM |

## 3. Legal and policy references

The full verification table is in [`legal-references.md`](legal-references.md). Canonical treatment:

| Item | Canonical statement | Status | Documents |
|---|---|---|---|
| Personal Data Protection Act, 2026 | Act No. 63 of 2026, gazetted on 10 April 2026, replacing the 2025 Ordinance; deemed in force from 6 November 2025, except section 23 and sections 31 to 35 (by Gazette notification after 18 months). Consent is the principal basis for processing, with other specified grounds and broad exemptions (national security, public order, public interest). Rules to be confirmed | Verified (Act number, Gazette date, commencement: official sources); provisions read from the database text, counsel to confirm (U1) | BP Ch. 2, 8, 14, Table 42; SUM |
| National Data Management Act, 2026 | Act No. 80 of 2026, gazetted on 10 April 2026; deemed in force from 6 November 2025; NRDEX, the national code repository and chief data officers retained (U2 closed). Rules to be confirmed | Verified (official sources); provisions read from the database text, counsel to confirm (U1) | BP, SUM |
| Cyber Security Act, 2026 and amendment | Act No. 81 of 2026, gazetted on 10 April 2026. The Cyber Security (Amendment) Act, 2026 (Act No. 99), gazetted on 1 July 2026, omits only section 20 (online gambling); the earlier report that it concerned AI-generated content was not correct. A further amendment was still a proposal in September 2026 | Verified (enacted texts, L8 resolved); further amendment reported | BP Ch. 2, 14, Tables 42, 43, 60; SUM |
| National AI Policy | Draft 2026-2030 consulted on in January 2026; revised draft version 2.0 dated 9 February 2026 on aipolicy.gov.bd; formulation of a national AI policy announced in August 2026 to begin in Q4 2026; **not adopted** | Reported; official portal listing | BP Ch. 1, 2, 14, Tables 42, 60; SUM |
| BAPIL safeguards | Consent, DPIA and ERRC approval for any personal data, and no sensitive personal data, are **BAPIL’s own rules**, stricter than the law | Design | BP 8.12, SUM |

## 4. Technical design, evaluation and software

| Item | Canonical statement or value | Evidence | Status | Documents |
|---|---|---|---|---|
| Core service | Bilingual, citation-grounded search and answer service over officially published documents, **designed** to cite official sources or abstain | BP Ch. 9 to 11 | Design | BP, SUM |
| P1 exit criteria (proposed targets) | Recall@10 at least 0.85 and citation precision at least 0.95 on the private test split (Annex R protocol); mean usefulness rating at least 4.0 of 5 from at least 30 active users | BP Table 38, Section 12.3 | Design (targets, not results) | BP, SUM |
| Benchmark | BanglaPolicyQA: **not yet built**. Version 0 planned with 500 answerable and 200 out-of-scope questions in months 6 to 9 (Milestone MS3); 2,000 answerable questions by month 30 (MS8); about 11,800 questions in all by 2035 if the scale-up goes ahead (Table 46) | BP Section 9.4, Annex R, Table 46, budget model | Pending | BP, SUM, REPO |
| Demonstration evaluation | Development results only: 24 answerable and 6 out-of-scope questions written by the author over BAPIL’s own documents; corpus of 8 documents (about 1,800 passages); Recall@10 0.92 (22 of 24) at the latest build; 6 of 6 correct abstentions | `implementation/build/eval_report.json`, regenerated by every build | Verified (measured locally) | BP 11.5, Table 60 |
| Reference implementation | `bapil` package version 0.1.0, Python standard library only; a research prototype, not a deployed system; **to be issued in release v1.1.0** | `implementation/pyproject.toml` | Verified (version); Pending (release) | BP, SUM, REPO |
| Unit tests | 49 tests pass when run locally (Python 3.13 on Linux, 22 October 2026); earlier local runs: 3.10 to 3.12 pass except one optional schema test skipped without `jsonschema`. **No public CI record exists yet**: the workflows are in the unpushed branch | Local runs | Verified locally; no public record | BP 11.2, 11.7; REPO |
| Bangla model | No dedicated model is built in the first 36 months; Year 3 delivers a documented decision on domain adaptation, built only if Stage 1 is justified | BP Section 9.7 | Design | BP, SUM |

## 5. Budget and funding

All budget figures are computed by `blueprint/src/budget_model.py`; the workbook `blueprint/data/BAPIL_Budget_Model.xlsx` re-implements the model with formulas and agrees to within Tk 1.

| Item | Canonical value | Status | Documents |
|---|---|---|---|
| Base case, 36 months | Tk 20.43 crore (unrounded Tk 204,264,136; about USD 1.65 million) | Verified (recomputed) | BP Tables 50, 62; SUM |
| Annual totals, base case | Year 1 Tk 4.73 crore; Year 2 Tk 7.49 crore; Year 3 Tk 8.21 crore (rounded rows add to 4.74, 7.48, 8.22 and 20.42, which the Table 50 note explains) | Verified | BP, SUM |
| Low scenario | Tk 17.93 crore | Verified | BP Table 62, SUM |
| High scenario | Tk 25.25 crore | Verified | BP Table 62, SUM |
| Adjusted base case | Tk 22.24 crore (known omissions of Tk 15 lakh a year and 19 staff computers at USD 1,200 added, contingency raised to 10%) | Verified | BP Section 17.2, Table 62; SUM |
| Reconciliation | Initial planning estimate Tk 18.49 crore bridged to Tk 20.43 crore in five steps (Table 61) | Verified | BP |
| Conditional national scale-up, Years 4 to 8 | Tk 218.85 crore (25.50, 36.08, 45.26, 51.11, 60.90); about Tk 239 crore over eight years with the 36-month plan; about 118 direct posts by Year 8; applies only after Gate G4 and a positive final evaluation; not requested | Computed (planning assumption, U17) | BP Section 17.3, Annex W, Tables 69, 70; SUM; front matter |
| Phase 0 (preparatory, before Month 1) | About six months; Tk 0.44 crore (legal review 10 lakh, feasibility and costing study 20 lakh, host call and panel 4 lakh, custodian consultations 3 lakh, coordinator 2.7 lakh, 10% contingency); funded under Decision D5; not part of the 36-month budget | Computed (planning assumption) | BP 15.1, 17.2, Tables 57, 65, 71; SUM |
| Funding by source (indicative) | Year 1: government 70%, one development partner 30% (only sources that can commit before Month 1). 36-month plan: government Tk 9.63 crore (47%), grants 3.51, development partners 5.31, agency service agreements 0.57, industry and philanthropy 1.41; scale-up: government 108.15, grants 34.10, development partners 18.63, service agreements 40.46, industry 17.51 (Tk crore); shares inside Table 51 ranges | Computed (planning assumption) | BP Annex W, Table 72, Figure 16; SUM |
| Staff employment | Employed by the host on fixed-term contracts; salary, allowances, provident fund and festival bonus budgeted; no government pension by default; Universal Pension System available; permanent posts only if BAPIL becomes a foundation or statutory centre | Stated design | BP Section 6.3, Table 71; SUM |
| Jobs and skills | Direct posts 9, 15, 19 (Years 1 to 3), then 58, 88, 105, 114, 118 if scaled up; fellows 6, 10, 12, then 20, 30, 40, 40, 40; officials trained 500 by Year 3, about 5,500 by Year 8 | Computed | BP Table 69; SUM |
| Comparison with other programmes | KOICA-supported AI hub project Tk 192.66 crore (July 2026 to December 2029; 865 specialists to be trained, 80% employment target) (TBS, 13 June 2026); FY2026-27 budget proposed Tk 500 crore for AI, electronics and youth innovation (TBS, 11 June 2026) | Source-reported | BP Section 3.6, Annex W; SUM |
| Funding status | No funding requested, approved or committed; all figures are planning estimates | Verified (absence of evidence recorded) | all |

## 6. Timeline

| Item | Canonical statement | Status | Documents |
|---|---|---|---|
| Start | Decision D5 starts Phase 0 (about six months); Month 1 is the first month with the MoU, host agreement and Year 1 funding in place; indicative Month 1 July 2027 (start of FY2027-28) if D5 is taken in Q4 2026; Year 1 = FY2027-28 | Design | BP 15.1, Table 65 |
| Plan | Phase 0, then 36 months: a 12-month Phase 1 pilot and Phase 2, whose budget is updated at month 6 (Deliverable D1.3) from the Phase 0 study; strategic horizons to 2041 (foundation Q4 2026; 2027 to 2028; 2029 to 2030; 2031 to 2035; 2036 to 2041) | Design | BP, SUM |

## 7. Conventions

| Item | Convention |
|---|---|
| Citations | Numbered in order of first citation; the Blueprint uses one numbering for both editions (124 references; entry format of the White Paper, numeric with type codes such as [J], [M], [C], [R], [EB/OL], based on GB/T 7714-2015); the Summary numbers its own list; entries taken from the White Paper bibliography are marked with an asterisk. Sources cite stable keys (1 to 83 White Paper, 84 onwards `blueprint/src/refs_new.md`), mapped in `blueprint/review/REFERENCE_NUMBERS.md`; Bangla editions print the numbers in Bangla digits |
| Quotation marks | “ ” and ‘ ’ in prose, ’ for the English apostrophe; straight marks only in code, URLs, JSON and commands (`blueprint/src/typography.py`) |
| Dashes | No en or em dashes in body text; hyphens where needed; en dashes only in bibliographic page ranges |
| Numbers in Bangla | Bangla digits in the Bangla editions, except in code, identifiers and URLs |
| Language precedence | The English edition is authoritative; the Bangla edition is a full translation and must state the same facts |

## 8. Bilingual terminology register

| English | Bangla (as used in the Bangla editions) |
|---|---|
| Governance (institutional) | শাসন; শাসনব্যবস্থা |
| Host institution | স্বাগতিক প্রতিষ্ঠান |
| Steering Board | স্টিয়ারিং বোর্ড |
| Ethics and Risk Review Committee (ERRC) | নৈতিকতা ও ঝুঁকি পর্যালোচনা কমিটি (ERRC) |
| Technical Architecture Board | কারিগরি স্থাপত্য বোর্ড |
| External member or reviewer | বহিঃস্থ সদস্য বা পর্যালোচক |
| Data protection | উপাত্ত সুরক্ষা |
| Personal data | ব্যক্তিগত উপাত্ত (laws); ব্যক্তিগত ডেটা (BAPIL data classes) |
| Data protection impact assessment (DPIA) | DPIA (abbreviation kept); প্রভাব মূল্যায়ন |
| Research ethics | গবেষণা-নৈতিকতা |
| Accountability (including algorithmic accountability) | জবাবদিহি; no separate fixed term is used for algorithmic accountability |
| Retrieval-augmented generation (RAG) | উদ্ধার-সমৃদ্ধ উৎপাদন (RAG) |
| Benchmark | বেঞ্চমার্ক |
| Evaluation metric | মূল্যায়নের মাপকাঠি |
| Citation precision (accuracy) | উদ্ধৃতির নির্ভুলতা |
| Abstention | বিরতি (উত্তর থেকে বিরত থাকা) |
| Human oversight | মানব-তত্ত্বাবধান (corrected in October 2026 from মানবিক তত্ত্বাবধান, which means humane supervision) |
| Conflict of interest | স্বার্থের সংঘাত |
| Phase (of the delivery plan: Phase 0, Phase 1, Phase 2) | ধাপ (ধাপ ০, প্রথম ধাপ বা ধাপ ১, দ্বিতীয় ধাপ বা ধাপ ২); not পর্যায়, which is kept for the stages of the Bangla model (BPFM পর্যায় ০ থেকে ২) |
| Data classes DC0 to DC3 (renamed from P0 to P3 in October 2026 so that they are not confused with pilots P1 to P6) | ডেটা-শ্রেণি DC0 থেকে DC3 |
| Training programmes TR1 to TR6 (renamed from T1 to T6 so that they are not confused with risk tiers T0 to T3) | প্রশিক্ষণ কর্মসূচি TR1 থেকে TR6 |
| Contingency | আপৎকালীন সংস্থান |
| Proposed target | প্রস্তাবিত লক্ষ্য; লক্ষ্যমাত্রা |
| Verified (fact, sample) | যাচাইকৃত |
| Multi-factor authentication (MFA) | বহু-উপাদান প্রমাণীকরণ |
| NIST CSF functions Identify / Detect | চিহ্নিতকরণ / শনাক্তকরণ |
| Technical Blueprint | টেকনিক্যাল ব্লুপ্রিন্ট |
| Human factors | মানব-উপাদান বিবেচনা (Section 9.8 heading; corrected from মানবিক বিবেচনা) |
