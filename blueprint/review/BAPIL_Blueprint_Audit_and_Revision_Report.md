---
title: "BAPIL Technical Blueprint, Version 1.0: Audit and Revision Report"
subtitle: "Evidence check, issue register, budget reconciliation, quality scores and publication checklist"
author: "Prepared for Md Naim Hassan Saykat (Independent Researcher, Bangladesh)"
date: "22 October 2026"
lang: en
---

# About This Report

This report records an audit of the pre-publication draft of the *Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint, Version 1.0* (English and Bangla builds of 21 October 2026, 117 and 116 pages), and the revision that followed. The revised Blueprint (137 pages in English, 131 in Bangla) is Deliverable 6 of the review mandate and is not reproduced here; this report contains the other deliverables: the executive review (Section 1), the issue register (Section 2), the claim verification matrix (Section 3), the technical and financial validation (Section 4), the governance and implementation redesign (Section 5), the change log (Section 6), the final quality assessment (Section 7) and the publication readiness checklist (Section 8).

**Who carried out the audit.** The audit was carried out with the assistance of an AI model (Claude), working to a multidisciplinary review mandate supplied by the author. It is not an independent external review by a panel of human experts, and it does not replace review by qualified Bangladesh legal counsel, a public-finance specialist or an independent evaluator. Where this report says a claim was "verified", it means the claim was checked against the source named, on the date given.

**What was reviewed.** The full English text; all 59 original tables and 15 figures; the budget model (`blueprint/src/budget_model.py`); the reference implementation, its tests and its evaluation output; the GitHub repository and its release page; the two existing Zenodo records; and the Bangla edition, compared with the English edition for numbers, dates, tables, headings and cross-references (by an automated section-by-section comparison and by reading the revised passages).

**What was not reviewed.** (1) Statutory texts. The official Laws of Bangladesh database (bdlaws.minlaw.gov.bd) refuses automated retrieval, so the gazetted texts and commencement sections of the 2025 ordinances and 2026 Acts could not be read; legal statements rely on press reports and secondary legal commentary, and are marked accordingly. (2) References 1 to 83, inherited from the White Paper, were not re-verified one by one; only those that support claims examined here were checked. (3) No full copy-edit of the Bangla prose was made; Bangla changes were limited to the revised passages, numerals and terminology consistency. (4) The reference implementation was not security-tested.

# 1. Executive Review

## 1.1 Overall assessment

The draft was a strong, unusually complete policy-design document: a clear problem, a credible institutional model, a careful public-data-first stance, an operational risk-tier and gate system, a working (if small) reference implementation, a long-term roadmap and a costed plan. Its weaknesses were not of concept but of evidence and status. It described several things as existing that did not yet exist (a public GitHub release and DOI-archived code), stated legal positions more firmly than its sources allowed (enactment treated as commencement; features of the 2025 ordinances attributed to the 2026 Acts; a labelling requirement attributed to the draft AI policy that the cited sources do not contain), described a proposed project as "under implementation", and presented a budget without escalation, separate contingency, recruitment ramp or scenarios. Its evaluation targets were sound but lacked sample sizes, decision rules and a precise definition of citation support. The plan lacked a list of the approvals and agreements that must precede month 1.

**Score of the draft: 6.2 out of 10** (weighted; Section 7). **Score after revision: 7.8 out of 10.** A score of 9 or 10 is not justified while the statutory texts remain unreviewed, no institutional approval or funding exists, the benchmark has not been built and the budget inputs have not been validated. These are not writing problems; they need external action (Section 8).

## 1.2 Five strongest aspects

1. **A coherent, proportionate design.** Public data first, advice not decisions, no surveillance; small pilots before scale; a clear handover route to agencies (G4).
2. **Operational responsible-AI controls.** Risk tiers with explicit rules, implemented and tested in code; lifecycle gates with checklists; a transparency register; an ethics committee with a binding veto.
3. **A working reference implementation.** Dependency-free Python with 49 passing unit tests, cited extractive answers with abstention, a hash-chained audit log and reproducible evaluation; documents are rebuilt from source.
4. **Bilingual by design.** Bangla treated as a first-class language in requirements, evaluation, normalisation rules and publication, with a full Bangla edition.
5. **Honest about limits in places.** The draft already labelled demonstration results as non-generalisable, called thresholds proposals and warned that legal texts needed confirmation; the revision extends that discipline to the whole document.

## 1.3 Ten most important weaknesses (by severity)

| # | Weakness | Severity |
|--|--------------------------|----|
| 1 | Reference implementation described as "published on GitHub and archived on Zenodo" in release v1.1.0, which did not exist publicly (the public repository shows releases v1.0 and v1.0.1 only) | Critical |
| 2 | Legal status overstated: enactment treated as commencement; Ordinance provisions (NRDEX, national source-code repository) attributed to the Acts; chief data officers attributed to the wrong instrument; the deferred commencement of some ordinance provisions not mentioned | Critical |
| 3 | AI Hub project described as "under implementation" with a "reported cost" of Tk 192.66 crore; the source describes a proposal awaiting approval | High |
| 4 | Budget: no escalation, no separate contingency, full staffing from month 1, no scenarios, no one-time and recurring split, no tax treatment; annual totals that appear not to add (rounding) | High |
| 5 | No list of preconditions and authorisations before month 1; January 2027 start presented without dependencies | High |
| 6 | Evaluation targets without sample sizes, confidence rules, out-of-scope test set or a precise definition of citation support | High |
| 7 | Draft national AI policy said to emphasise labelling of AI-generated content; the cited sources do not say so | Medium |
| 8 | Governance bodies described without legal status, appointment and removal rules, or relation to statutory bodies; ERRC members nominated by the ICT Division (independence risk) | Medium |
| 9 | Foundation-model path not explicit about the retrieval and reranking steps before adaptation, and no feasibility reasoning against training from scratch | Medium |
| 10 | Risk register without early-warning indicators, contingencies, residual ratings or review frequencies; no complaint and appeal route | Medium |

## 1.4 Principal obstacles to credibility

* **Government:** no approvals, no funding and no host institution yet; legal obligations unconfirmed.
* **Academic:** evaluation targets not yet measured; reliance on press reports for legal facts.
* **Technical:** the reference implementation is a prototype; dense retrieval, the portal, authentication and OCR exist only as design.
* **Funding:** the budget is a model with plausible but unvalidated inputs (salaries, quotations, overhead, duty status).

## 1.5 Recommendation

**Revise (done), then publish as a proposal; pilot only after approvals.** Publication is appropriate once three conditions hold: the GitHub release v1.1.0 is public, the Zenodo DOI is minted and printed in the PDFs, and the documents carry the status statements added in this revision. Implementation should not be described as ready until the preconditions in Annex T are met.

# 2. Issue Register

Severity: Critical (misleads on project status or legal position), High (material to a decision), Medium (weakens credibility), Low (presentation). Status: Resolved (fixed in the revision), Partly resolved (fixed as far as evidence allows), Open (needs external action).

| ID | Location (draft) | Issue | Category | Severity | Evidence | Correction | Status |
|----|---------|--------------|------|-----|-------------|------------|-----|
| I-01 | Front matter "What already exists"; 1.4 item 10; 1.7; 11.1; 16.4; 21.4; Table 1 | Code described as published on GitHub and archived with a DOI; release v1.1.0 not public | Implementation status | Critical | GitHub releases page and remote tags on 22 Oct 2026: v1.0 and v1.0.1 only; code exists on local branch `blueprint-v1.0` | Reworded as "released with this Blueprint"; status table added; Annex D rule that the DOI record is published only after the release exists | Partly resolved (needs push and release) |
| I-02 | 1.7; 21.4 | "Core ideas already work" | Overclaim | High | Demonstration over 10 documents and 24 questions only | Reworded: mechanisms can be built and tested on a small scale; pilot tests usefulness | Resolved |
| I-03 | 11.7 | CI "runs on every change" | Implementation status | Medium | Workflows exist locally; never run on GitHub | "Configured to run once the repository is updated" | Resolved |
| I-04 | 11.x | No maturity vocabulary | Clarity | Medium | Prompt requirement; terms used loosely | Definitions of conceptual design, prototype, reference implementation, tested release, production added (Section 11.1) | Resolved |
| I-05 | Repository | No security policy; dependency practice undocumented | Security | Low | No `SECURITY.md` in repository | `SECURITY.md` added; dependency rules stated in 11.7 | Resolved |
| I-06 | 2.6; 14.1; Table 42 | Enactment treated as commencement | Legal | Critical | PL&B (June 2026): Ordinance in force except ss. 23 and 31 to 46 [113]; 18-month window [114] | Enactment and commencement separated; "to be confirmed" and "stricter reading" rules | Partly resolved (needs counsel) |
| I-07 | 8.11; 10.8; Tables 42, 43 | NRDEX and national source-code repository attributed to the 2026 Act | Legal attribution | High | Only the 2025 Ordinance description supports them [84] | Attributed to the Ordinance; "to be confirmed in the Act" | Resolved |
| I-08 | 8.8; Table 42 | Chief data officers attributed to the data-management framework | Legal attribution | Medium | PL&B: CDO is s. 23 of the personal data protection ordinance, deferred [113]; TBS article does not mention CDOs | Re-attributed; deferral noted | Resolved |
| I-09 | 14.1 | Ordinance named "National Data Governance Ordinance" | Accuracy | Low | Official database title: জাতীয় উপাত্ত ব্যবস্থাপনা অধ্যাদেশ, ২০২৫ (National Data Management); TBS uses "Governance" | Both names given | Resolved |
| I-10 | 14.1 | February 2026 data-residency amendment ordinance omitted | Completeness | Medium | Digital Policy Alert: promulgated 5 Feb 2026 [115] | Added to 8.12, 14.1, Tables 42 and 43 | Resolved |
| I-11 | Table 42 | PDPA passage cited to [86], which does not name it | Citation | Medium | Daily Sun lists NDM Bill and Cyber Security Bill, not PDPA | PDPA cited to [85, 116] | Resolved |
| I-12 | 13.8; Table 41; Annex N | Labelling of AI content attributed to the draft AI policy | Misattribution | Medium | [88], [89] mention measures against false or misleading AI content, not labelling | Labelling presented as BAPIL's own rule | Resolved |
| I-13 | 3.6; 17.2; Table 42; Summary; Memo | AI Hub "under implementation", "reported cost" Tk 192.66 crore | Government initiative status | High | TBS 13 Jun 2026: proposal awaiting approval [35]; Observer 26 Aug 2026: USD 13 m grant agreement signed [117] | Status corrected; comparison only for scale, with caveat | Resolved |
| I-14 | Table 4; 2.2 | 2023 AI readiness rank cited to [26], the 2025 index | Citation | Low | Rank 82 (2023) is from [80] | Cited to [80] | Resolved |
| I-15 | Table 4; 2.2 | GCI "top tier" vague | Precision | Low | BGD e-GOV CIRT: Tier 1 role-model country [119] | Wording specific; official source added | Resolved |
| I-16 | Chapter 17; Table 50 | 18.49 total vs annual figures adding to 18.50 | Arithmetic | Medium | Unrounded draft total Tk 18.4868 crore; independent rounding | Explained; note on rounding; reconciliation Table 61 | Resolved |
| I-17 | Chapter 17 | No escalation in Years 2 and 3 | Financial | High | CPI 8.34% (Sep 2026) [118] | 8% escalation on taka costs | Resolved |
| I-18 | Chapter 17 | Contingency merged with overhead (10%) | Financial | High | Overhead pays the host; contingency covers estimating risk; merging them hides the risk allowance | 10% overhead plus 5% contingency | Resolved |
| I-19 | Chapter 17 | Full staffing assumed from month 1 | Financial | Medium | Director appointed in months 1 to 3 (15.4) | 75% average Year 1 occupancy | Resolved |
| I-20 | Chapter 17 | No scenarios, one-time and recurring split, or tax treatment | Financial | High | Not present | Table 62 (low, base, high; cost types); duty and VAT flagged as input | Resolved |
| I-21 | Chapter 17 | Budget inputs not validated | Financial | High | No quotations, host salary scale or overhead rate | Inputs required listed (Annex Q) | Open |
| I-22 | Table 28; 9.4; 9.5 | No sample sizes or decision rule; citation metric loosely defined; no out-of-scope set; recall could be read as answer quality | Evaluation | High | Not present | Annex R (Table 63); 9.4, 9.5 revised; Table 28 definitions | Resolved |
| I-23 | 9.4 | Language parity gated on a set too small to resolve 5 points | Evaluation | Medium | About 150 per language in v0: interval about plus or minus 6 points | Parity reported in v0, gated from v1 | Resolved |
| I-24 | 9.7; Table 30 | Foundation-model ladder implicit; no feasibility reasoning | Technical | Medium | Not present | Five-step ladder; compute and data estimates; minimum viable scope | Resolved |
| I-25 | Chapter 5; Annex F; Table 57 D4 | ERRC appointment by government nominees; no removal rule; legal status unclear | Governance | Medium | Independence risk | Independent nominations panel; removal for cause; status statements; Annex S | Resolved |
| I-26 | Chapter 5; Annex E | Charter could be read as overriding law | Governance | Medium | No precedence clause | Article 13 and Section 14.7 | Resolved |
| I-27 | 13.6 | No complaint and appeal route; statutory remedies not mentioned | Accountability | Medium | Not present | Complaint, appeal and external routes added | Resolved |
| I-28 | Chapter 15 | No preconditions or authorisations before month 1 | Implementation | High | Not present | Annex T (Tables 65 and 66); 15.1 revised | Resolved (content); Open (approvals) |
| I-29 | Chapter 19 | Risk register lacks indicators, contingencies, residual ratings and review frequency | Risk | Medium | Not present | Annex U (Table 67) | Resolved |
| I-30 | Front matter | No statement of what exists versus what is proposed | Clarity | High | Not present | Status table; disclaimer extended | Resolved |
| I-31 | Bangla edition | ASCII digits in lists, citations and quarter labels | Editorial | Low | Author's request | Bangla numerals via babel; citations converted; Gantt labels | Resolved |
| I-32 | Zenodo record 21363967 | Record licence shows MIT while the White Paper text states CC BY 4.0; affiliation shows Université Paris-Saclay | Metadata (outside the Blueprint) | Low | Zenodo record page, 22 Oct 2026 | Recommend correcting the record metadata | Open |
| I-33 | Statutory texts | Gazetted texts, commencement and rules not reviewed | Legal | Critical | bdlaws refuses automated retrieval | Legal review scope defined (14.3) | Open (needs counsel) |
| I-34 | References 1 to 83 | Not re-verified item by item | Citation | Medium | Inherited from the White Paper | Stated in Annex P | Open |

# 3. Claim Verification Matrix

Sources were consulted on 21 and 22 October 2026. "Corrected wording" is the substance now used in the Blueprint.

| Claim (draft) | Location | Best available source and date | Status | Explanation | Corrected wording | Further verification |
|----------|------|-------------|-----|----------|----------|------|
| PDPA 2026 enacted April 2026 | 1.1, 2.6, 14.1, Tables 4, 42 | Securiti, 29 Jun 2026 (Law 63 of 2026) [85]; Azam, SSRN, 14 Sep 2026 [116]; ConsentStack (enacted 10 Apr 2026; some provisions delayed 18 months) | Source-reported | No primary text seen; one aggregator gives 10 April and a deferred commencement | "Reported as enacted in April 2026 (Act 63 of 2026) ... commencement to be confirmed" | Gazette and section 1 of the Act |
| NDMA 2026 passed April 2026 | Same | Daily Sun, 10 Apr 2026 [86]; Azam [116] | Source-reported | Bill passed on the final day of the session, 10 Apr 2026 | "Bill reported passed on 10 April 2026" | Gazette; commencement |
| Ordinance commencement | New | Greenleaf and Al Razi, PL&B, 1 Jun 2026 [113]; Khan (SCL), 23 Apr 2026 [114] | Source-reported | PDPO in force immediately except ss. 23 and 31 to 46; 18-month window from 6 Nov 2025 described | Added | Whether carried into the Act |
| NRDEX, national source-code repository | 8.11, 10.8, Tables 42, 43 | TBS, 10 Nov 2025 [84] | Verified for the 2025 Ordinance only | Act text not seen | "As described for the 2025 Ordinance; to be confirmed in the Act" | Act text |
| Data residency amendment | New | Digital Policy Alert [115]; TBS, 20 Apr 2026 | Source-reported | Ordinance No. 23 of 2026, 5 Feb 2026 | Added | Status after the Act |
| Cyber Security Bill passed 10 Apr 2026 | 14.1 | Daily Sun [86] | Source-reported | Listed among 24 bills | Kept, qualified | Gazette |
| AI-content amendment passed 30 Jun 2026 | 14.1 | Dhaka Tribune, 30 Jun 2026 [87] | Source-reported | Passed by voice vote; exact day not stated | "Reported passed by 30 June 2026" | Gazette |
| Draft AI policy: categories, oversight committee, fund Tk 200 to 250 crore | 2.6, 17.2, Table 42 | Daily Star, 26 Jan 2026 [88] | Source-reported | Confirmed; oversight committee to be created by an Act of Parliament | Kept; Act detail added | Final policy text |
| Draft AI policy emphasises labelling | 13.8, Table 41, Annex N | [88], [89] | Not supported | Sources mention measures against false or misleading AI content | Labelling is BAPIL's rule | None |
| Drafting from Q4 2026 by joint team | 1.1, 14.2 | Daily Observer, 10 Aug 2026 [91] | Source-reported | Year inferred from article date | Kept | None |
| AI Hub Tk 192.66 crore, under implementation | 3.6, 17.2, Table 42 | TBS, 13 Jun 2026 [35]; Daily Observer, 26 Aug 2026 [117] | Partly incorrect | Proposal awaiting approval; grant agreement (USD 13 m, 2026 to 2029) later signed | Status corrected | Planning Commission approval |
| EGDI 2024 rank 100, 0.657 | 2.2, Table 4 | UN DESA country data [120] | Verified | 0.65696; 111 in 2022 | Kept | None |
| GCI 2024 top tier | 2.2, Table 4 | BGD e-GOV CIRT [119] | Verified (official) | Tier 1 role model | Specific wording | None |
| GAIRI 2023 rank 82 | 2.2, Table 4 | Sultana et al. 2026 [80] | Source-reported | Index report not checked | Cited to [80] | Index report |
| GPUs per department 2 to 55 | Table 4 | [80], Table 2 | Verified against source | Estimates for five departments | Kept | None |
| Exchange rate Tk 123.65 | Table 49 | Bangladesh Bank, 19 Oct 2026 [110] | Verified | Weighted average rate | Kept | Update at costing study |
| Pay scale grade 9 Tk 44,000 | 17.5, Table 49 | Financial Express, 31 Aug 2026 [109] | Source-reported | Cabinet approval; gazette not seen | Kept, status noted | Gazette |
| Inflation 8.34% (Sep 2026) | Table 49 | Dhaka Tribune, 7 Oct 2026 [118] | Source-reported | BBS release reported | Added | BBS release |
| L40S about USD 7,500; 4-GPU server USD 47,000 to 49,000 | Table 49 | Modal, 12 Aug 2025 [111] | Source-reported (vendor) | Used as basis for USD 25,000 per 2-GPU server | Kept | Local quotations |
| Reference implementation published (v1.1.0) | Front, 1.4, 11, 16.4 | GitHub, 22 Oct 2026 | Future milestone | Not yet public | "Released with this Blueprint" plus Annex D rule | Confirm after push |
| Demonstration Recall@10 0.92; abstention 6 of 6; 49 tests | 11.5 | Build output, 22 Oct 2026 | Research finding | 10 documents, about 1,700 passages, 24 questions | Kept with limits | None |

# 4. Technical and Financial Validation

## 4.1 Architecture review

The twelve-component architecture is sound and proportionate: a governed corpus, hybrid retrieval, an answer service that cites or abstains, an audit log and a governance workspace, with zero-trust zoning and hosting in Bangladesh for any non-public data. Three points were clarified in the revision rather than redesigned. First, the boundary between what is implemented (the prototype) and what is design (dense retrieval, portal, authentication, OCR, production security) is now stated in Section 11.1 and Table 37. Second, the evaluation rules now separate retrieval from answer quality, so the architecture's trust properties are measured rather than assumed. Third, the foundation-model path now begins with retrieval improvements before any adaptation. No change to the component model was needed.

## 4.2 Benchmark methodology and acceptance criteria

The revised protocol (Annex R, Table 63) fixes: BanglaPolicyQA v0 at 500 answerable questions split 40% public development and 60% private test, plus 200 out-of-scope questions; a decision rule (a threshold is met when the point estimate meets it and the 95% interval is no wider than plus or minus 5 points); citation precision judged at sentence level by two blinded annotators with reported agreement; and minimum samples for each measure. The arithmetic behind the sample sizes:

| Measure | Expected value | Sample | Approximate 95% half-width |
|---|---|---|---|
| Recall@10, all test questions | 0.85 | 300 | 4.0 points |
| Recall@10, one language | 0.85 | 150 | 5.7 points |
| Citation precision | 0.95 | 400 sentences | 2.1 points |
| Correct abstention | 0.90 | 150 | 4.8 points |
| P2 extraction accuracy | 0.99 | 1,000 cells | 0.6 points |

Language parity therefore cannot be decided in v0 and becomes a release condition from v1 (about 600 test questions per language). The thresholds themselves (Recall@10 of at least 0.85, citation precision of at least 0.95) were not changed: they are reasonable for an advisory search tool, and nothing in the evidence justified moving them.

## 4.3 Implementation maturity

| Element | Maturity |
|---|---|
| Bangla normalisation, BM25 search with bilingual expansion, cited extractive answers with abstention, risk tiers, register, evaluation metrics, audit log, CLI, JSON API | Reference implementation (research prototype), tested software release 0.1.0 with 49 unit tests; not deployed |
| Dense retrieval, reranking, generative rephrasing with verification | Conceptual design |
| Portal, authentication, OCR pipeline, production security controls | Conceptual design |
| BanglaPolicyQA | Protocol and guidelines only |
| Pilots P1 to P6 | Proposed |

## 4.4 Budget reconciliation

The draft total of Tk 18.49 crore and the displayed annual totals (4.96, 6.71 and 6.83, which add to 18.50) differed only through rounding: the unrounded draft total was Tk 18.4868 crore. The draft did, however, omit escalation and a separate contingency and assumed full staffing from month 1. The revised base case is computed by the same published model:

| Step | 36-month total (Tk crore) | Change |
|---|---|---|
| Draft budget before this review | 18.49 | |
| Year 2 and 3 amounts restated at Year 1 prices | 18.29 | -0.20 |
| Explicit escalation of taka costs (8% a year) | 19.79 | +1.50 |
| Year 1 recruitment ramp (75% of posts filled on average) | 19.29 | -0.50 |
| Evaluation items added (out-of-scope set, citation judgements, annual system audit) | 19.54 | +0.25 |
| Separate contingency of 5% of direct costs = revised base case | 20.43 | +0.89 |

The revised base case is Tk 4.73, 7.49 and 8.21 crore in Years 1 to 3 (Tk 20.43 crore, about USD 1.65 million). About 21% of direct costs are one-time. Scenarios: low Tk 17.93 crore, high Tk 25.25 crore. Single-factor sensitivity: staff costs plus or minus 20% change the total by about Tk 1.98 crore; full Year 1 staffing adds Tk 0.52 crore; equipment 25% dearer adds Tk 0.71 crore; 10% escalation instead of 8% adds Tk 0.41 crore; a 10% weaker taka adds Tk 0.28 crore.

## 4.5 Financial assumptions and missing inputs

All figures are calculations from stated planning assumptions, not quotations. Inputs still needed before any figure can be called a cost estimate in the procurement sense: the host's salary scale, increment rules and overhead rate; quotations for servers, GPUs and storage; the host's import duty and VAT status; data-centre charges; confirmation of in-kind national compute; agreed rates for annotators and trainers. No funding has been requested, approved or committed.

# 5. Governance and Implementation Redesign

The revision keeps the original institutional model (a university-anchored lab under an MoU, a Steering Board, an ERRC with a binding veto and a TAB) and makes it operationally specific:

* **Status and limits (Annex S, Table 64).** For each body: legal or administrative basis, membership and appointment, chair and secretariat, decision rights and their limits, reporting and transparency, and conflict-of-interest safeguards. None has statutory power; internal rules never override the law (charter Article 13; Section 14.7).
* **ERRC independence.** Members are selected through an open call by an independent nominations panel and confirmed by the Steering Board; government may propose candidates but not hold a majority; removal only for cause by two thirds of the Board after a hearing. Decision D4 was revised accordingly.
* **Relation to statutory bodies.** The ERRC is not the oversight committee proposed in the draft AI policy (to be created by an Act of Parliament); statutory authorities and courts keep their powers; overlaps with the host's governing body and ethics committee are resolved explicitly.
* **Accountability.** A complaint and appeal route with time limits, external remedies preserved; annual independent audit of systems.
* **Implementation readiness (Annex T, Tables 65 and 66).** Thirteen preconditions with the instrument or authority each needs and its current status; a definition of month 1; ten work packages with owners, preconditions, acceptance tests, budget lines, risks and gates; what needs legislation and what does not.
* **Risk management (Annex U, Table 67).** For all eighteen risks: an early-warning indicator, a contingency, a residual rating and a review frequency.
* **Monitoring and evaluation.** KPIs are labelled as proposed targets; quality indicators follow Annex R; independent evaluations at months 18 and 36 are retained.

# 6. Change Log

| Location | Change | Reason | Source or calculation | Impact | Remaining uncertainty |
|--------|---------------|-----|--------|-----|------|
| Front matter | Status table; disclaimer and Overview revised; budget line added; document counts 21 annexes and 67 tables | Separate what exists from what is proposed | GitHub check; Annex P | Meaning: lowers claimed maturity | None |
| 1.1, 1.4, 1.6, 1.7 | Legal timing qualified; item 17 and method step 6 added; implementation wording | I-01, I-06 | [84, 85, 86, 113] | Meaning | Commencement |
| 2.2, 2.6, Table 4 | EGDI and GCI sources; GAIRI citation; legal summary rewritten | I-14, I-15, I-06 | [80, 119, 120] | Accuracy | None |
| 3.6 | AI Hub status | I-13 | [35, 117] | Accuracy | Approval status |
| 5.3, 5.5 | Legal status of bodies; precedence of law | I-25, I-26 | Design | Governance | None |
| 8.8, 8.11, 8.12, 10.8 | Attribution of CDO, NRDEX, source-code repository; residency amendment; stricter-reading rule | I-07, I-08, I-10 | [84, 113, 115] | Legal | Act text |
| 9.4, 9.5, Table 28 | Benchmark composition, splits, statistical rationale, decision rule; refined metric definitions; answer coverage and availability rows | I-22, I-23 | Wilson intervals | Evaluation; small cost increase | None |
| 9.7, Table 30 | Five-step ladder; feasibility estimate; minimum viable scope | I-24 | 6ND approximation [121] | Technical | Governed Bangla text volume |
| 11.1, 11.7; SECURITY.md | Maturity terms; CI wording; security and dependency practice | I-03, I-04, I-05 | Repository | Status | None |
| 12.3 | Exit criterion tied to protocol; labelled as target | I-22 | Annex R | Evaluation | None |
| 13.6, 13.8 | Complaints and appeals; labelling attribution | I-27, I-12 | [89] | Accountability | None |
| 14.1, 14.2, 14.3, new 14.7; Tables 41 to 43 | Legal chronology, cautions, legal review scope, status of BAPIL's arrangements | I-06 to I-12 | [84 to 89, 106, 113 to 116] | Legal | Needs counsel |
| 15.1 | Definition of month 1 | I-28 | Annex T | Schedule | Decision dates |
| 16.4 | Publication in future tense | I-01 | GitHub | Status | None |
| 17.1 to 17.5; Tables 49, 50 | Budget revised (Tk 18.49 to 20.43 crore), features, scenarios, sensitivity, rounding note, scale comparison caveated | I-16 to I-21 | budget_model.py; [118] | Cost +Tk 1.94 crore | Inputs unvalidated |
| 18.3, 19.2 | KPIs as targets; link to Annex U | I-29 | Design | M&E | None |
| 21.4; Table 57 | Conclusion wording; D4 revised; note on authorisations | I-02, I-25 | Design | Governance | None |
| Annexes D, E, F, K, L, N | Release rule; Article 13; ERRC appointment and status; out-of-scope set; glossary; labelling row | I-01, I-25, I-26, I-22, I-12 | Design | Various | None |
| New Annexes P to U; Tables 60 to 67 | Evidence status; budget reconciliation and scenarios; evaluation protocol; governance status; preconditions and work packages; risk monitoring | Prompt deliverables | As listed | Adds about 20 pages | As listed |
| References | [113] to [121] added | New evidence | As listed | Citation | None |
| Summary and Memo (EN, BN) | Status lines; legal qualification; budget figures; D4; targets wording | Consistency | Body | Consistency | None |
| Bangla edition | All revisions translated; Bangla numerals in lists, citations, quarter labels; acronyms KOICA and VAT | I-31; consistency | Automated EN and BN number comparison | Editorial | Full copy-edit not done |

**Material deletions.** None of substance. The unsupported phrases ("under implementation", "core ideas already work", "published on GitHub and archived with a DOI", the labelling attribution) were replaced, not silently removed.

# 7. Final Quality Assessment

## 7.1 Scores by category

Weights reflect what decision-makers and funders most need from a blueprint: accuracy, evaluation and finance carry the most weight. The overall score is the weighted mean.

| # | Category | Weight | Draft | Revised | Evidence for the revised score | Remaining limitations |
|--|----------|---|---|---|------------|----------|
| 1 | Strategic clarity and public value | 8 | 8.0 | 8.5 | Clear problem, model and theory of change; status statements | Value not yet demonstrated with users |
| 2 | Factual and legal accuracy | 12 | 5.0 | 7.0 | Misattributions corrected; enactment and commencement separated; Annex P | Statutory texts unreviewed; secondary sources |
| 3 | Technical architecture | 8 | 7.5 | 8.0 | Boundaries of implemented versus designed stated; ladder for models | Most components are design only |
| 4 | Evaluation and reproducibility | 10 | 6.0 | 8.5 | Protocol with samples, rules, blinded judging; reproducible build | No benchmark exists yet |
| 5 | Responsible AI, privacy and security | 8 | 7.5 | 8.0 | Tiers, gates, complaints, stricter-reading rule, security policy | Controls untested in operation |
| 6 | Governance and accountability | 8 | 6.5 | 8.0 | Annex S; independent ERRC selection; precedence of law | Bodies not constituted |
| 7 | Financial transparency and feasibility | 10 | 5.5 | 8.0 | Model, reconciliation, scenarios, sensitivity, cost types | Inputs unvalidated; no funding |
| 8 | Implementation readiness | 8 | 4.5 | 6.0 | Preconditions, month 1 definition, work packages | No approvals, host or funding |
| 9 | Research quality and citation integrity | 8 | 6.0 | 7.5 | Claim matrix; citations corrected; primary sources where possible | Refs 1 to 83 not re-verified; press sources for law |
| 10 | Internal consistency | 8 | 6.5 | 8.5 | Automated EN and BN comparison; totals and cross-references checked | Minor wording differences between editions |
| 11 | Bengali language and editorial quality | 6 | 7.5 | 8.5 | Bangla numerals; terminology aligned; new content translated | No full native copy-edit |
| 12 | Publication readiness | 6 | 5.0 | 7.0 | Builds clean; status explicit; Annex D rule | Release, DOI and counsel pending |
| | **Weighted overall** | **100** | **6.2** | **7.8** | | |

## 7.2 Separate dimensions

| Dimension | Assessment after revision |
|---|---|
| Conceptual quality | High (8.5): coherent, proportionate, well argued |
| Research and factual accuracy | Moderate to good (7): corrected, but legal facts rest on secondary sources |
| Technical design quality | Good (8): sound architecture and evaluation design; small prototype |
| Institutional feasibility | Uncertain (6): plausible model, no host, sponsor or approvals yet |
| Financial feasibility | Plausible (7): modest, transparent, scenario-tested; inputs unvalidated |
| Operational readiness | Low (4): nothing can start before the Annex T preconditions |
| Publication quality | Good (8): consistent bilingual build in LaTeX, PDF, PNG and Markdown |

## 7.3 Why not 10

A 10 would require a document that is evidence-backed, independently verifiable and ready for its purpose. Four things prevent that today, and none can be fixed by editing: (1) the statutory texts and commencement provisions have not been reviewed by qualified counsel; (2) the reference implementation, release and DOI are not yet public; (3) no host, sponsor, approval or funding exists, so implementation readiness is necessarily low; (4) the budget inputs have not been validated against quotations and the host's rules. With (1), (2) and (4) done, a score of about 9 would be defensible for the document as a publication-ready proposal; (3) concerns the project, not the document.

# 8. Publication Readiness Checklist

**Resolved in this revision**

* Status of every artefact stated; maturity terms defined; claims classified (Annex P).
* Legal misattributions corrected; enactment and commencement separated; stricter-reading rule.
* AI Hub status corrected; labelling attribution corrected; citations corrected.
* Budget reconciled, revised and scenario-tested; rounding explained.
* Evaluation protocol with samples and decision rules.
* Governance status, appointment and limits; complaints and appeals; precedence of law.
* Preconditions, work packages and risk monitoring.
* Bilingual consistency checked; Bangla numerals; documents rebuilt; tests pass (49).

**Partly resolved**

* Reference implementation status: wording now accurate at publication, provided the release is published first.
* Bangla editorial quality: revised passages and numerals done; full copy-edit not done.

**Requires external confirmation**

* Push the branch and publish GitHub release v1.1.0; confirm it appears on the releases page.
* Reserve the Zenodo DOI, rebuild the PDFs with it, then publish the record (after the release).
* Correct the White Paper Zenodo record's licence field (MIT shown; text says CC BY 4.0) if that was unintended.

**Requires legal counsel**

* Read the gazetted PDPA 2026, NDMA 2026, Cyber Security Act 2026 and amendment, and the 2026 amendment ordinance; confirm enactment, publication and commencement dates, provisions in force, rules issued, and BAPIL's role (controller, processor or fiduciary). Then correct Tables 42 and 43.

**Requires technical testing**

* Build BanglaPolicyQA v0 and run the Annex R protocol; security-test the prototype before any use beyond demonstration.

**Requires institutional approval**

* Decisions D1 to D6; host selection and governing-body resolution; MoU; charter adoption; ERRC selection.

**Requires funding or procurement confirmation**

* Year 1 funding commitment; host salary scale and overhead rate; equipment quotations and duty status; national compute confirmation.

**What remains before the Blueprint can credibly be called publication-ready:** the GitHub release and the Zenodo DOI. **Before it can be called implementation-ready:** legal review, approvals, a host and funding, as listed in Annex T.

# Sources Consulted for This Audit

The full references are in the Blueprint. Sources consulted for verification on 21 and 22 October 2026 include:

* GitHub repository and releases page: <https://github.com/md-naim-hassan-saykat/bapil/releases>
* Zenodo records: <https://zenodo.org/records/21363967>, <https://zenodo.org/records/21441172>
* Securiti, PDPA 2026 overview: <https://securiti.ai/bangladesh-personal-data-protection-act-overview/>
* Greenleaf and Al Razi, Privacy Laws & Business, June 2026: <https://www.privacylaws.com/reports-gateway/articles/int201/int201bangladesh/>
* Khan, Sovereign Chambers of Law, April 2026: <https://bd-scl.com/insights/personal-data-protection-ordinance-2025-compliance.html>
* Azam, SSRN, September 2026: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7436740>
* Digital Policy Alert, amendment ordinance 2026: <https://digitalpolicyalert.org/change/18757-personal-data-protection-amendment-ordinance-2026-ordinance-no-23-of-2026>
* The Business Standard, ordinances gazetted (Nov 2025): <https://www.tbsnews.net/node/1281356>
* Daily Sun, bills passed (10 Apr 2026): <https://www.daily-sun.com/bangladesh/868072/91-bills-passed-in-parliament-to-convert-ordinances-into-laws>
* Dhaka Tribune, cyber security amendment (30 Jun 2026): <https://www.dhakatribune.com/bangladesh/parliament/414016/cyber-security-amendment-bill-2026-passes-in>
* The Daily Star, draft AI policy (26 Jan 2026): <https://www.thedailystar.net/business/economy/news/draft-ai-policy-targets-innovation-better-public-services-4090431>
* The Financial Express, draft AI policy (29 Jan 2026): <https://thefinancialexpress.com.bd/national/draft-ai-policy-tightens-state-oversight>
* The Daily Observer, AI policy drafting (10 Aug 2026): <https://observerbd.com/news/587314>
* The Business Standard, AI hub proposal (13 Jun 2026): <https://www.tbsnews.net/tech/govt-establish-ai-hub-tk19266cr-project-backed-koica-1462206>
* The Daily Observer, KOICA grant agreement (26 Aug 2026): <https://observerbd.com/news/590061>
* UN DESA E-Government Knowledgebase, Bangladesh: <https://publicadministration.un.org/egovkb/en-us/Data/Country-Information/id/14-Bangladesh>
* BGD e-GOV CIRT: <https://cirt.gov.bd/who-we-are>
* Bangladesh Bank exchange rate: <https://www.bb.org.bd/en/index.php/econdata/exchangerate>
* Dhaka Tribune, inflation September 2026: <https://www.dhakatribune.com/business/421534/inflation-rises-in-september>
* The Financial Express, 2026 pay scale: <https://thefinancialexpress.com.bd/national/cabinet-approves-2026-pay-scale-sets-basic-salaries-from-tk-20000-to-tk-156000>
* Modal, L40S prices: <https://modal.com/blog/nvidia-l40s-price-article>
