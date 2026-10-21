---
title: "BAPIL Technical Blueprint, Version 1.0 (revised): Adversarial Review"
subtitle: "Severity-ranked defects, corrected passages, weighted score and readiness verdicts"
author: "Review of the revised build of 22 October 2026 (commit 2e69d96)"
date: "22 October 2026"
lang: en
---

# Scope and Independence

**Object reviewed.** The revised Technical Blueprint (English, 140 pages; Bangla, 134 pages), its Summary and Decision Memo, all 69 tables, the budget model, the reference implementation and the repository state on 22 October 2026.

**Stance.** The review assumes the document is wrong until shown otherwise. Each critical claim was re-tested against its source, every budget total and share was recomputed from the published tables and the model, and the plan was checked against itself (milestones, gates, owners, decisions, budget).

**Independence limitation.** This review was produced by the same AI system that revised the document, instructed to act as an adversarial reviewer. It is independent in method, not in institution. It does not replace review by qualified Bangladesh legal counsel, a public-finance specialist or an external evaluator, and its findings should be treated as a pre-submission check.

**Method notes.** Repository state was re-queried (`git ls-remote`): `main` at 4756cf9, tags v1.0 and v1.0.1 only. Budget tables were re-added from their printed (rounded) values and from the model. The official laws database (bdlaws) still refuses automated retrieval, so no statutory text was read; legal findings rest on the secondary sources cited.

# 1. Severity-Ranked Defect List

Severity: **Critical** (would mislead a decision-maker or is false today), **High** (material to a funding, legal or go/no-go decision), **Medium** (weakens credibility or creates an internal contradiction), **Low** (precision or presentation).

| ID | Sev. | Location | Defect | Evidence |
|----|------|--------|---------------------|--------------|
| R-01 | Critical | Title page; Document Information; Citation; Table 1 | "DOI to be assigned on publication (reserved on Zenodo)" states that a DOI has been reserved. None has been. | No Zenodo draft or reservation exists for the Blueprint; the build fills the text from a "PENDING" placeholder (`assemble.py`) |
| R-02 | Critical | Status table; Overview; Sect. 1.4 item 10; Sect. 11.1 | Present-tense claims that the code "is released in repository release v1.1.0" and "archived ... under a DOI". On 22 October 2026 neither is true, and Annex D's safeguard only works if the publication order is followed. | Remote tags: v1.0, v1.0.1; branch `blueprint-v1.0` not pushed |
| R-03 | High | Sect. 15.1; Table 65 note; Table 48 | "January 2027 is the earliest plausible start" understates the funding dependency. If Year 1 money comes through the government development budget, project approval can take many months: the document's own source shows the AI hub proposal submitted on 1 December 2025 still awaiting approval in June 2026. | [35] |
| R-04 | High | Table 57 (D2); Memo D2; Sect. 21.2 | No decision asks for money. D2 approves a pilot and an MoU, but Annex T makes Year 1 funding a condition of month 1. Section 21.2 then says the 90-day plan "can start immediately" after D1, D2 and D4, which contradicts Annex T. | Tables 57, 65; Sect. 21.2 |
| R-05 | High | Ch. 17; Tables 49, 50 | Costs omitted from the budget although the plan requires them: consultation and engagement events (Table 8, including events outside Dhaka in every phase), P5 survey data collection, staff travel outside training, open-access publication fees, and computers for 19 staff. | Tables 8, 18, 38, 49 |
| R-06 | High | Table 49; Sect. 17.1 | A 5% contingency is optimistic for a pre-feasibility estimate with no quotations, no host salary scale and no confirmed overhead rate. The document's own high scenario uses 10%. | Annex Q; Table 69 (U6) |
| R-07 | Medium | Sect. 8.12; Table 42 (BN and EN) | "A 2026 amendment to the ordinance added residency requirements for specified data" exceeds the source. Digital Policy Alert says only that the amendment changed data-residency provisions; TBS commentary describes localisation as limited to critical sectors such as banking and healthcare, which may be a narrowing. | [115]; TBS, 20 April 2026 |
| R-08 | Medium | Sect. 8.1; Sect. 14.2 | "Free of the privacy risks of personal data" and "public data ... carries no personal-data risk" are false. Gazettes and notifications routinely name individuals (appointments, transfers, land acquisition, court and disciplinary notices). | Nature of the P0 sources listed in Table 22 |
| R-09 | Medium | Sect. 5.3; Annex F; Table 64 | The ERRC veto is said to bind the host "by agreement". A host university's statutes may not allow its governing body to cede a binding veto to an external committee; the veto is binding only to the extent the host's statutes and the host agreement permit. | Not established by any source; requires counsel |
| R-10 | Medium | Table 37; Annex J | Identity (single sign-on, MFA, roles) and the production audit store are scheduled "Before G3". G3 is the pilot gate that closes at month 12, while the T2 pilot with officials starts after G2 at month 9. Officials would use the system for up to three months without production access control. | Tables 37, 44; Sect. 13.3 |
| R-11 | Medium | Sect. 7.5; Tables 28, 63 | Romanised Bangla matching is deferred to "later versions", yet Table 63 gates G2 on "variant-spelling and romanised" recall of at least 0.75. A gate depends on a feature not scheduled before it. | Sect. 7.5; Table 37 has no transliteration row |
| R-12 | Medium | Sect. 1.7 | "A 36-month plan delivers ... a governed Bangla domain model ... in Year 3" contradicts Sections 9.7 and 12.6, where a model is built only if Stage 1 is justified. | Sect. 9.7; Table 30; Table 44 (MS8 "if approved") |
| R-13 | Medium | Sect. 11.5 | The demonstration results are developer-set results and the text does not say so. The questions were written by the author over the author's own documents; gold headings were edited when the Blueprint was renumbered; and one corpus passage was changed during development after it caused a false answer to an out-of-scope test question. | Build history; Annex M |
| R-14 | Medium | Sect. 9.6; Table 29 | Model selection excludes hosted commercial models even as a reference point. For public (P0) data there is no residency barrier to benchmarking one, and without it the opportunity cost of adaptation (Stage 1) cannot be judged. | Sect. 10.1 permits P0 work in other environments |
| R-15 | Medium | Sect. 9.7; Table 30 | The cost of Stage 1 itself (staff time and compute) is not stated, so the Stage 1 decision has no cost side. | Table 49 bundles it into general ML staff |
| R-16 | Low | Table 44 (MS5); Table 66 (P3) | P3 passes G2 and G3 in the same month (15). G3 is the end of a pilot; it cannot coincide with pilot readiness. | Sect. 13.3 gate definitions |
| R-17 | Low | Table 44; Table 66 (P6) | P6 has no milestone or month for its protocol approval or methods paper. | Table 44 |
| R-18 | Low | Sect. 12.3; Table 38; Table 63 | Usefulness is defined three ways: "rating the tool useful", "rating it at least 4 of 5" (each user) and "mean rating at least 4.0". | Three passages |
| R-19 | Low | Sect. 11.2 | "Runs offline on any machine with Python 3.10 or newer" is untested beyond Python 3.13 on Linux; CI for 3.10 to 3.12 has never run. | Local run: Python 3.13.16 |
| R-20 | Low | Sect. 9.2 step 4 | "A calibrated score threshold": the prototype uses a fixed threshold; no calibration has been done. | `bapil.answer` |
| R-21 | Low | Sect. 17.3 | "About Tk 7.3 crore ... (Table 62)" cannot be read from Table 62, whose overhead row also covers one-time costs (6.35 x 1.15 = 7.30). | Table 62 |
| R-22 | Low | Sect. 17.5 | "Tk 500 an hour" is not derived. Grade 9 basic pay of Tk 44,000 over about 176 working hours is Tk 250; reaching Tk 500 needs allowances roughly equal to basic pay, which is not shown. | [109] |
| R-23 | Low | Table 50 | Rounded category rows add to 4.74, 7.48, 8.22 and 20.42 against printed totals of 4.73, 7.49, 8.21 and 20.43. The note covers this, but the printed column does not add. | Recalculation |
| R-24 | Low | NFR-04; Sect. 10.7 | 99% availability in Year 1 rests on a single production site; the recovery site arrives in Year 2, while flood and power risks (R18) are rated medium likelihood. | Tables 10, 31, 35 |
| R-25 | Low | Sect. 9.7 and title of P4 | "Bangla Policy Foundation Model" names, at most, a domain adaptation within 36 months; the name overstates the deliverable. | Table 30 |

**Recalculations that passed.** Table 50 shares add to 100%. Table 62 rows add to their totals in every year (4.73, 7.49, 8.21; 20.43). The reconciliation chain in Table 61 (18.49 to 20.43) reproduces exactly from the model. Text figures match the model: Tk 20.4 crore; Years 4.7, 7.5, 8.2; USD 1.65 million (20.43 crore / 124); people 52% (42.2% + 9.4%); compute 17%; one-time 21% of direct costs (3.67 / 17.77); low 17.9 and high 25.3; sensitivity +/-2.0, +0.5, +0.7, +0.4, +0.3 crore; time-saving value Tk 0.72 crore and under a tenth of Year 3 (8.5%). Sample-size intervals in Annex R recompute correctly (4.0, 5.7, 2.1, 4.8 and 0.6 points). Compute estimates in Section 9.7 recompute within the stated order of magnitude.

**Legal and government claims that held.** Ordinances gazetted in November 2025 [84]; National Data Management Bill and Cyber Security Bill reported passed on 10 April 2026 [86]; PDPA reported enacted in April 2026 [85, 116]; deferred commencement of PDPO sections 23 and 31 to 46 [113]; Cyber Security (Amendment) Bill reported passed by 30 June 2026 [87]; draft AI policy contents and the proposed fund [88, 89]; drafting from Q4 2026 [91]; AI hub proposal status and grant agreement [35, 117]; EGDI and GCI positions [119, 120]; exchange rate [110]. All remain secondary or press-reported except the last three, as the document already says.

# 2. Corrected Passages

Each correction replaces the passage named. English text is given; the Bangla edition needs the same changes.

**R-01 (title page, Document Information, Citation; `assemble.py`).**
Replace "DOI to be assigned on publication (reserved on Zenodo)" with: "DOI to be assigned on publication". In Table 1, replace "DOI reserved on Zenodo at publication" with: "DOI assigned at publication".

**R-02 (status table row; Overview; Sect. 1.4 item 10; Sect. 11.1).**
Status table: "Research prototype (package version 0.1.0) with 49 unit tests passing locally on Python 3.13. It is issued in repository release v1.1.0; readers can check that the release is listed at https://github.com/md-naim-hassan-saykat/bapil/releases. If it is not listed, the code is not yet public. Not a production system; not tested with users."
Overview, second sentence: "...is issued with this Blueprint in GitHub release v1.1.0 and archived with the Blueprint's Zenodo record, which is published only after that release exists (Annex D)."

**R-03 (Sect. 15.1).**
"Month 1 is the first month in which the MoU, the host agreement and Year 1 funding are all in place (Annex T, Table 65). How soon that can happen depends on the funding route. With grant, partner or host funding already available, January 2027 is the earliest plausible start. If Year 1 funding must come through the government development budget, project approval can take many months: a comparable technical-assistance proposal submitted in December 2025 was still awaiting approval in June 2026 [35]. On that route a start in the second half of 2027 is more realistic. A later start moves every date in this chapter by the same amount."

**R-04 (Table 57, D2; Memo; Sect. 21.2).**
D2: "Approve a 12-month Phase 1 pilot, name a government focal point, agree an MoU with a host institution, and commit or identify Year 1 funding (about Tk 4.7 crore, Table 50)".
Sect. 21.2, first sentence: "When decisions D1, D2 and D4 are taken and the MoU, host agreement and Year 1 funding are in place (Annex T), the 90-day plan in Section 15.4 can start."

**R-05 and R-06 (Sect. 17.2, new paragraph after the sensitivity paragraph; Table 49 contingency row).**
"Three limits of the base case should be noted. First, it does not yet include consultation and engagement events, survey data collection for P5, staff travel other than for training, open-access publication fees, or computers for staff. An allowance of about Tk 15 lakh a year for the first four items and about USD 1,200 per new staff member for computers (planning assumptions) would add about Tk 0.9 crore with overheads and contingency. Second, a 5% contingency is low for an estimate made before any quotation; with a 10% contingency and these allowances, the base case would be about Tk 22.2 crore. Third, the high scenario (Tk 25.3 crore) remains the prudent planning ceiling until the feasibility study replaces these assumptions."
Table 49, contingency row: "5% of direct costs in the base case; 10% recommended until quotations and the host's rates are known (high scenario)".

**R-07 (Sect. 8.12; Table 42 PDPA relevance cell).**
"...and a Personal Data Protection (Amendment) Ordinance, 2026 changed the ordinance's data-residency provisions [115]; commentary describes localisation as limited to critical sectors such as banking and healthcare [122]. The position under the 2026 Act is to be confirmed."
Add reference [122]: The Business Standard, "Personal Data Protection Ordinance: A law that protects you from everyone except the state", 20 April 2026, https://www.tbsnews.net/thoughts/personal-data-protection-ordinance-law-protects-you-everyone-except-state-1416106.

**R-08 (Sect. 8.1, Sect. 14.2).**
Sect. 8.1: "...under-used because it is scattered across sites and formats, and of low privacy risk. It is not free of personal data: gazettes and notifications name individuals, for example in appointment, transfer, land-acquisition and disciplinary notices. Such passages are indexed only as published, are never combined into profiles of individuals, and are excluded from analytics and model training."
Sect. 14.2, first bullet: "Because already-published documents carry low personal-data risk and need no new consent, the public-data-first policy is the main legal safeguard. Published personal data (for example names in gazette notices) is not aggregated or profiled. Any P2 processing requires a documented lawful basis and a DPIA."

**R-09 (Sect. 5.3; Annex F "Status"; Table 64 ERRC "Status and basis").**
"...its decisions bind BAPIL by the charter and bind the host to the extent the host's statutes allow and the host agreement provides. Whether the host's governing body can accept a binding external veto must be confirmed by the legal review (Section 14.3) before the host agreement is signed; if it cannot, the host agreement must provide that the host will not proceed with a tier T2 or T3 system that the ERRC has refused."

**R-10 (Table 37).**
Identity row, "When": "Before G2 (pilot start, month 9)". Audit log row, "When": "Before G2". Add to Annex J, G2 checklist: "Single sign-on with MFA and roles, and the production audit store, in operation."

**R-11 (Table 63, Robustness row; Table 37).**
Decision rule: "Variant spelling (Bangla script) at least 0.75 in v0; romanised and code-mixed queries reported in v0 and gated from v1, after transliteration is delivered." Add Table 37 row: "Transliteration of romanised Bangla | Not included | Transliteration candidates in query expansion | Months 12 to 18".

**R-12 (Sect. 1.7).**
"...evaluated adoption decisions in Year 2, and in Year 3 a documented decision on Bangla domain adaptation (with an adapted model only if Stage 1 is justified) and Blueprint 2.0."

**R-13 (Sect. 11.5, note after the results).**
"These figures are development results, not test results. The 24 questions were written by the author over BAPIL's own documents, which the author also wrote; gold headings were updated when the Blueprint was renumbered; and one corpus passage was rewritten during development after it caused a false answer to an out-of-scope question. They show that the evaluation harness works end to end. They say nothing about performance on the national corpus, which will be measured on the private test split of BanglaPolicyQA under Annex R."

**R-14 (Sect. 9.6, after the second sentence).**
"For public (P0) data only, at least one hosted commercial model is also evaluated as a reference point, so that the gap between open models and the best available system, and therefore the value of any adaptation, can be judged. Hosted models are never used for data above class P0."

**R-15 (Sect. 9.7, after the Stage 1 bullet).**
"Stage 1 is costed before it is approved: indicatively one to two machine-learning staff for about twelve months (Tk 0.3 to 0.5 crore within the core staff line) and up to USD 20,000 of compute if national compute is not available (high scenario). The Stage 1 decision compares this cost with the cost of improving retrieval, data and evaluation by the same amount."

**R-16 and R-17 (Table 44, MS5; Table 66).**
MS5 gate: "G2 (P3); P6 research protocol approved by the ERRC". Add to MS6 achievement: "P3 pilot results (G3)". Table 66, P3 gate: "G2 at month 15; G3 at month 18". P6 gate: "Protocol approval at MS5; methods paper by MS7; stop if the protocol is not approved."

**R-18 (Sect. 12.3; Table 38).**
"...and a mean usefulness rating of at least 4.0 on a 5-point scale from at least 30 active users (Table 63)."

**R-19 (Sect. 11.2).**
"...so it is designed to install and run offline with Python 3.10 or newer, including in air-gapped environments. It has been tested locally on Python 3.13 on Linux; the CI workflow will test Python 3.10 to 3.13 once the repository is updated."

**R-20 (Sect. 9.2 step 4).**
"Apply a score threshold, calibrated on the development split of the benchmark, and require that the top passages actually cover the query terms. The reference implementation uses a fixed threshold."

**R-21 (Sect. 17.3).**
"...recurring direct costs in Year 3 are Tk 6.35 crore (Table 62); with 15% overheads and contingency they are about Tk 7.3 crore at Year 3 prices, before further escalation."

**R-22 (Sect. 17.5).**
"Valuing an analyst's time at about Tk 500 an hour (a planning assumption: grade 9 basic pay of Tk 44,000 a month [109] is about Tk 250 an hour, and the assumption allows for allowances, benefits and overheads of about the same amount)..."

**R-23 (Table 50 note).**
Add: "Rounded category rows add to 4.74, 7.48, 8.22 and 20.42; the totals shown are computed from unrounded values."

**R-24 (Table 10, NFR-04).**
"Availability of 99% for pilots (working hours) once the recovery site is in place in Year 2; best effort with offline backups in Year 1; 99.5% at scale."

**R-25 (Sect. 9.7, first paragraph).**
Add: "The White Paper's name is kept for continuity; within the 36-month plan the most that would be built is a domain adaptation of an existing open model, not a new foundation model."

# 3. Claims Requiring External Confirmation

| Requires | Claims |
|---|---|
| Legal counsel | Enactment, publication and commencement of the PDPA 2026, NDMA 2026, Cyber Security Act 2026 and its amendment; whether NRDEX, the source-code repository and chief data officers survive in the Acts; the effect of the 2026 residency amendment; BAPIL's role as controller, processor or fiduciary; whether a university host can accept a binding external veto (R-09); data-sharing agreement template; the national oversight committee's future relation to BAPIL |
| Financial confirmation | All Table 49 unit costs; host salary scale, increment rules and overhead; equipment quotations; import duty and VAT status; data-centre charges; in-kind national compute; contingency level (R-06); the omitted cost items (R-05); the source and route of Year 1 funding (R-03, R-04) |
| Independent testing | Every Table 28 threshold (none measured); OCR error rates; latency and availability; prompt-injection resistance; privacy scans; security test of the prototype; independent re-scoring before G4 |
| Institutional approval | Decisions D1 to D6; host selection and governing-body resolution; MoU; charter; ERRC selection; data custodians' reuse terms; research ethics approvals; division of labour with the AI hub project |
| Author action | Publish GitHub release v1.1.0, then the Zenodo record; fix R-01 and R-02 wording before any circulation |

# 4. Weighted Score

| # | Criterion | Weight | Score | Basis |
|---|---|---|---|---|
| 1 | Strategic clarity and public value | 8 | 8.0 | Clear problem, proportionate model, explicit boundaries |
| 2 | Factual and legal accuracy | 12 | 6.5 | Mostly well hedged, but R-01 is false today and R-07 exceeds its source; legal base still secondary |
| 3 | Technical architecture | 8 | 7.5 | Sound design; R-10 and R-11 show gate and feature timing gaps |
| 4 | Evaluation and reproducibility | 10 | 7.5 | Strong protocol; demonstration results not disclosed as developer-set (R-13) |
| 5 | Responsible AI, privacy and security | 8 | 7.5 | Good controls; "no personal-data risk" for P0 is wrong (R-08) |
| 6 | Governance and accountability | 8 | 7.0 | Detailed, but veto bindingness and funding decision are open (R-04, R-09) |
| 7 | Financial transparency and feasibility | 10 | 6.5 | Transparent model and correct arithmetic; omitted costs and thin contingency (R-05, R-06) |
| 8 | Implementation readiness | 8 | 5.0 | Preconditions listed, but no host, funding or approvals; start date optimistic on the government route (R-03) |
| 9 | Research quality and citation integrity | 8 | 7.0 | Good source labelling; heavy reliance on press for law; refs 1 to 83 unverified |
| 10 | Internal consistency | 8 | 7.5 | Arithmetic consistent; several plan contradictions (R-04, R-12, R-16, R-18) |
| 11 | Bengali language and editorial quality | 6 | 8.0 | Consistent numerals and terminology; no full native copy-edit |
| 12 | Publication readiness | 6 | 6.0 | Clean bilingual build; two Critical wording defects block circulation |
| | **Weighted total** | **100** | **7.0** | |

The score is lower than the author-side assessment of 7.8 because this review found two statements that are false today (R-01, R-02), an unfunded start condition (R-03, R-04) and omitted costs (R-05). With R-01 to R-13 corrected, the release published and the DOI minted, about 7.8 would be defensible; above 8.5 requires the legal review and validated costs.

# 5. Readiness Verdicts

| Category | Verdict | Reasons |
|---|---|---|
| **A. Publication as a proposal** | **Yes, conditionally.** | Suitable once R-01 and R-02 are corrected and the GitHub release precedes the Zenodo record. The High defects (R-03 to R-06) should also be fixed, because a published proposal will be read by funders. The document is otherwise candid about its status. |
| **B. Formal government submission** | **No, not yet.** | Needs: the legal review of the 2026 Acts; a named host and sponsor; an explicit funding request through a stated route, with costs validated by quotations and the host's rates; and conversion into whatever format that funding route requires. Without these, a ministry cannot act on it. |
| **C. Limited pilot** | **No.** | No host, funding, governance bodies, legal review, benchmark or production access control exists. The prototype has no authentication, ingestion pipeline or OCR. A researcher-only trial on public documents (class R, tier T1) is technically possible now, but it would not be the government pilot this document proposes. |
| **D. Operational deployment** | **No.** | Ruled out by the document's own design: no system may become operational without a G4 decision, independent evaluation and agency ownership, none of which can occur before month 24. |
