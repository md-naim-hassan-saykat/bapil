# Independent review of the Technical Blueprint and the response: 22 to 23 October 2026

This is an internal record and is not part of the publication.

**How the review was done.** A separate agent that had not seen how the documents were produced read the English Blueprint, the Summary, the Decision Memo and the budget model. It read them as three readers at once: a senior ICT Division official, a development-partner programme officer, and a journal peer reviewer. It changed no files.

**The reviewer's overall score was 6.5 out of 10.** It found the following strengths:
- the documents are candid about evidence and status;
- the budget arithmetic is correct and reconciles across tables;
- funding is staged and gated;
- the evaluation design and its confidence intervals are sound;
- the compute estimate for a Bangla model is correct;
- the governance instruments can be reused.

It asked for three main changes:
- put the legal review and costing before any commitment;
- fix the verified contradictions;
- correct the political framing and the colliding codes.

**What the author decided** (22 October 2026):
- add a preparatory Phase 0;
- do not produce a separate decision volume now;
- rename two code clashes: data classes P0 to P3 become DC0 to DC3, and training programmes T1 to T6 become TR1 to TR6.

**One note on timing.** The review read the build of commit `52ae353`. Separately, uncommitted edits made outside this session between 17:44 and 18:00 had already added the gazette texts of the 2026 Acts. Those edits also corrected the Annex P price row and closed U13, which settles part of R-14.

## Findings and response

In the Kind column, V marks a verified contradiction or arithmetic error, and J marks a judgement call.

| ID | Severity | Kind | Finding (short) | Response | Status |
|---|---|---|---|---|---|
| R-01 | Critical | V | The legal review was due before MS2 (month 6), but it had to happen before the host agreement, which comes at month 1 | Phase 0 added (Section 15.1). The legal review is commissioned under D5 and finished before the host agreement is signed (Section 14.3; Table 65; U1, U15) | Fixed |
| R-02 | Critical | V/J | The feasibility and costing study came after the money and had no owner or budget; equipment was bought before it | The Phase 0 study is costed at Tk 20 lakh and owned through D5 by the ICT Division or a development partner. D1.3 becomes the updated Phase 2 work plan. Procurement uses the Phase 0 quotations | Fixed |
| R-03 | Major | V | It was unclear who funds Year 1; competitive grants cannot be committed before the lab exists | Year 1 is funded 70% by government and 30% by one development partner (Table 51 has a new Year 1 column; Tables 65 and 72; Section 17.4). The 36-month government share becomes 47% | Fixed |
| R-04 | Major | V | Gazettes that name individuals were in class P0, contrary to the Blueprint's own "most sensitive element" rule | A defined exception now covers published administrative notices, with restrictions: no search, listing or profiling of individuals, and exclusion from analytics and training. P1 completes a DPIA screening before G2 (Section 8.3). The Memo and Summary wording is corrected | Fixed |
| R-05 | Major | V | The "first 12 months" column covered pilots that start after month 12 | The Table 38 header now reads "first 12 months of each pilot", and the Summary gives the month of each first result | Fixed |
| R-06 | Major | V | BPFM Stage 1 had several dates and decision-makers | One rule: the Steering Board decides at month 18 (MS6) on the advice of the TAB and the ERRC, informed by the mid-term evaluation; work runs in months 19 to 30. Sections 1.7, 9.7 and 16.5 and Table 31 are aligned | Fixed |
| R-07 | Major | V | The veto was stated "binding" without qualification in several places, and the Board could weaken it | The veto is qualified everywhere, including Table 14 and Annex F. Charter Article 12 now protects Article 6 and the rules for ERRC appointments with the ERRC's consent. The code's T2 approver is aligned with Table 39 and the RACI: "ERRC (Steering Board consulted)" | Fixed |
| R-08 | Major | J | The Year 1 workload did not fit the team, and Year 1 has only about three months of live P1 use | Phase 0 moves the legal review, costing and host selection out of Year 1. The month-12 KPIs are now realistic (Table 54). Annex O writes the benchmark after the protocol and notes the live-use period. Staff numbers are unchanged, because that is a budget decision for the Phase 0 study | Partly |
| R-09 | Major | J | The 2041 roadmap was anchored to plans branded by the previous government | The plans are now described as "existing long-term plans, subject to revision" (Sections 16.1, 16.8 and 16.11; Table 45; Summary). The 2041 review uses "national development goals in force at that time" | Fixed |
| R-10 | Major | J | July 2024 was framed as a technical disruption | It is now described as "the nationwide internet shutdown of July 2024" (Section 10.7, Table 4) | Fixed |
| R-11 | Major | J | The draft AI policy was described from newspapers | The wording now says "categories reported for the draft policy" and "compatible with" (Sections 13.2, 14.2). New item U18 records that the official v2.0 text still has to be read | Partly (U18) |
| R-12 | Major | J | The data Acts were presented as a settled legal basis | They are now "legal context". The reuse of published documents rests on the RTI Act and custodians' reuse terms (Table 4, Section 16.11) | Fixed |
| R-13 | Major | J | The staff-cost basis was weak and might not fit a public host's rules | Section 17.1 now states the public-host cap (with the low scenario as a proxy) and the Director-cost caution. Full salary regimes are for the Phase 0 study | Partly |
| R-14 | Major | V | The evidence register contradicted itself (L40S price, U13, closed items) | The Annex P price row and U13 were already corrected in the sources. Annex V now explains why closed items are kept. The 2023 index stays as the baseline because that edition contains the cited rank | Fixed |
| R-15 | Major | V | Letter codes collided | Data classes are renamed DC0 to DC3 and training programmes TR1 to TR6 in both editions, the code, the schemas, the examples and the tests. The other codes are kept, as the author decided | Fixed (as decided) |
| R-16 | Major | J | The document's length hides the decisions | Not done. The author decided the 11-page Summary and 2-page Memo serve this purpose for now | Not changed |
| R-17 | Major | J | G4 at month 24 ignored the July to June budget cycle | The agency now requests the operating cost around month 12. G4 is a decision in principle, with transfer at the start of the next fiscal year (Section 5.8). Year 1 is FY2027-28 | Fixed |
| R-18 | Major | J | The laws database blocks automated retrieval, which undermines the corpus fallback | The fallback is now assisted manual download and university law libraries, and Phase 0 costs it (Section 21.2; risk R2 in Tables 55 and 67; Memo) | Fixed |
| R-19 | Major | J | BAPIL graded its own work, and the pass rule was lenient | At G4 the lower confidence bound must meet the threshold. Safety thresholds are judged on the upper bound. An independent custodian holds the test split, and thresholds are pre-registered (Section 9.5, Annex R) | Fixed |
| R-20 | Minor | V | The Phase 2 funding trigger came after Phase 2 starts | R8 now triggers if Tranche 2 is not committed by month 9 | Fixed |
| R-21 | Minor | V | Table 61 called the initial estimate "constant prices" | Now "Year 2 and 3 amounts with implicit price growth" | Fixed |
| R-22 | Minor | V | Targets did not match the plan | Table 46 now reads: 2,300 questions by 2030; 5,500 officials by 2035; 50 users in 2028; the language gap measured from v1. Figure 13 and Section 16.7 are aligned | Fixed |
| R-23 | Minor | V | Calendar slips | Fiscal-year calendar: Phase 0 in the first half of 2027, Month 1 in July 2027. Tables 44, 45, 48, 71 and 72, Figures 12, 13 and 16, Sections 16.5, 16.6 and 17.3 and the Figure 12 caption are corrected | Fixed |
| R-24 | Minor | V | P2 had two owners | Table 7 now lists the Planning Commission as host agency for P1 and co-owner of P2 with the Finance Division | Fixed |
| R-25 | Minor | J | The Memo read like an internal government instruction | The Memo now says "For the consideration of" and "Proposed responsible body" and "Proposed timing", and the unconstituted Authority is removed. The MoU status is now "Proposed in this Blueprint; not decided". The TR1 audience is "senior officials" | Fixed |
| R-26 | Minor | J | Gaps: UGC approval, foreign-funds clearance, host exit, legal personality | Section 5.2 now covers all of these, and a note on the RACI table states that the host signs agreements | Fixed |
| R-27 | Minor | V/J | Citation context problems | Section 1.1 is reworded. Section 10.4 already cited the Act [165, 166]. The NDMA code repository was confirmed (U2) | Fixed |
| R-28 | Minor | V/J | Small consistency points | The Memo adds the usefulness target, and the Table 54 G3 indicator now counts user-facing pilots. The risk-score scales in Annex B are unchanged: D1 and D3 measure different things and are consistent as defined | Partly |
| R-29 | Minor | V | Stale reference numbers in the budget model comments | Clarified as source keys of `refs_new.md` | Fixed |
| R-30 | Minor | J | Affiliation differs from the earlier Zenodo records | This is the author's decision (`METADATA_TO_CONFIRM.md`, item 1) | Not changed |

## Effect on the main figures

| Figure | Before | After |
|---|---|---|
| 36-month budget | Tk 20.43 crore | Unchanged |
| Phase 0 | n/a | Tk 0.44 crore (new; before Month 1) |
| Government share of the 36-month plan | Tk 7.97 crore (39%) | Tk 9.63 crore (47%) |
| Year 1 funding mix | 35 / 25 / 30 / 0 / 10 | 70 / 0 / 30 / 0 / 0 (government / grants / development partners / agencies / industry) |
| Indicative Month 1 | January 2027 | July 2027 (FY2027-28) |
| Demonstration Recall@10 (regenerated) | 0.875 | 0.92 (22 of 24); it changes as the documents change |
