# Legal and policy references: verification table

Checked on 21 and 22 October 2026. This is not legal advice. Every statement about Bangladesh law in the BAPIL documents rests on press reports and secondary legal commentary: the gazetted texts were not reviewed, because the official laws database (bdlaws.minlaw.gov.bd) does not allow automated retrieval and the national AI policy portal (aipolicy.gov.bd) blocks automated reading of its documents. The Blueprint therefore labels these statements as reported, applies the stricter reading of each obligation, and requires an independent review by qualified Bangladesh counsel before milestone MS2 (Blueprint Section 14.3; unresolved items U1 to U3 and U15).

Reference numbers are those printed in the Technical Blueprint, which numbers its references in order of first citation; [`blueprint/review/REFERENCE_NUMBERS.md`](../blueprint/review/REFERENCE_NUMBERS.md) maps them to the source keys. The Summary and the Decision Memo number their own short reference lists.

## 1. Verification table

| # | Claim in the documents | Source | Provision | Status | Correction made | Documents affected |
|---|---|---|---|---|---|---|
| L1 | The Personal Data Protection Ordinance, 2025 and the National Data Management Ordinance, 2025 were gazetted in November 2025 | TBS [6]; commentary [65] | Whole instruments | Reported | None needed | BP 14.1, Table 42 |
| L2 | Under the 2025 Ordinance, the sections on chief data officers, complaints and offences did not commence immediately; an 18-month compliance window was described | Greenleaf and Al Razi [39]; Khan [77] | Commencement provisions | Reported (two independent commentaries) | None needed; the documents already state that commencement under the 2026 Act must be confirmed | BP 2.6, 8.4, 14.1, Table 42 |
| L3 | A Personal Data Protection (Amendment) Ordinance, 2026 (Ordinance No. 23 of 2026), promulgated in February 2026, changed the data-residency provisions; localisation is described as limited to critical sectors | Digital Policy Alert [63]; TBS [64] | Data residency | Reported | None needed | BP 8.12, 14.1, Table 42 |
| L4 | The Personal Data Protection Act, 2026 was enacted in April 2026, replacing the Ordinance (reported as Act 63 of 2026) | Securiti [7]; Azam [38] | Whole Act | Reported | None needed; the act number is attributed to [7] | BP 2.6, 14.1, Table 42; SUM; MEMO |
| L5 | The personal data framework "requires consent" | Previously cited to [6, 7] | Lawful grounds | **Incorrect as worded.** Securiti [7] states that processing may also take place on other specified grounds; Bangladesh Law Digest [62] describes a section under which consent is set aside where processing is necessary for national security, defence, public order or the public interest | **Corrected** (EN and BN): consent is the principal basis, with other specified grounds and broad exemptions; BAPIL’s consent rule is labelled as its own safeguard, not a statutory requirement. The test fixture that said "Personal data must be processed only with consent" was rewritten and labelled fictitious, and the Annex M example output regenerated | BP 8.12, Annex M; SUM (safeguards line); MEMO; `implementation/tests/fixtures/` |
| L6 | Data subjects may restrict automated decisions | TBS [6]; Securiti [7] | Data-subject rights | Partly verified: [7] mentions withdrawal of consent covering automated decision-making; the scope of any standalone right is not confirmed | Wording kept as "as reported"; covered by U1 | BP 8.12, 14.2, Table 42 |
| L7 | The National Data Management Bill, 2026 and the Cyber Security Bill, 2026 were passed on 10 April 2026 | Daily Sun [8] | Whole instruments | Reported | None needed | BP 14.1, Table 42 |
| L8 | A Cyber Security (Amendment) Bill, 2026 "aimed at the removal of harmful AI-generated content" was passed by 30 June 2026 | Dhaka Tribune [9] | Amendment content | **Sources disagree.** The bill was passed on 30 June 2026, but The Financial Express [40] (and bdnews24) report that it removed Section 20 on online gambling; the Dhaka Tribune report links it to removal of harmful AI-generated content. On 2 July 2026 a cabinet committee was formed to review and finalise a draft Cyber Security (Amendment) Act, 2026 [41], which suggests a further amendment | **Corrected** (EN and BN): passage date stated, the disagreement disclosed, the July 2026 draft added; the information-integrity implication now refers to "reported proposals"; Tables 42, 43 and 60 and unresolved item U1 updated | BP 2.6, 14.1, 14.2, Tables 42, 43, 60, 68; SUM |
| L9 | A draft National AI Policy 2026-2030 was released for public consultation in January 2026 | The Daily Star [10]; The Financial Express [11] | Policy draft | Reported | Kept | BP 1.1, 2.6, Tables 42, 60; SUM; MEMO |
| L10 | (New) A revised draft, version 2.0, dated 9 February 2026, was published on the official portal | aipolicy.gov.bd document listing [12] | Policy draft | Verified that the document is listed with this title and date; its content was **not** reviewed (automated access blocked) | **Added** so that the Q4 2026 process is not presented as the first drafting exercise; the documents now say it is not confirmed whether the new process builds on the 2026 drafts | BP 1.1, 14.2, Tables 42, 60; SUM; MEMO |
| L11 | Formulation of a national AI policy will begin in the fourth quarter (of 2026) with a joint team of government, private sector, academia and researchers | The Daily Observer, 10 August 2026 [14]; 19 July 2026 [13] | Policy process | Reported. The article does not name the year; the fourth quarter of 2026 is the natural reading of an August 2026 statement | Kept | BP 1.1, 14.2, Ch. 21, Table 60; SUM; MEMO |
| L12 | The draft national AI policy proposes risk categories, impact assessment, an independent oversight committee created by an Act of Parliament, a Bangla-based national LLM, national compute and an innovation fund | The Daily Star [10]; The Financial Express [11] | Policy content | Reported (January draft only); version 2.0 not reviewed | Kept, attributed to the draft | BP 2.6, Annex N, Table 42 |
| L13 | Right to Information Act, 2009 in force | Reference [59] | Proactive disclosure | Long-standing law; not re-checked in this audit | None | BP Table 42 |
| L14 | The White Paper (v1.0, July 2026) cites the Cyber Security Act, 2023 | White Paper reference list | Superseded instrument | The 2023 Act was replaced by the 2025 Ordinance and the 2026 Act. The White Paper is a published, DOI-registered record and was **not** edited | Recorded as a known limitation of the White Paper; the Blueprint uses the current framework | WP (not changed) |

## 2. Statutory requirements and BAPIL’s own safeguards

| Topic | What the law requires (as reported) | BAPIL’s own, stricter rule |
|---|---|---|
| Lawful basis | Consent as the principal basis, other specified grounds, broad state exemptions | Personal data only in pilot P3, only with consent, only after a DPIA and ERRC approval, only de-identified and only for aggregate results |
| Sensitive data | Specific consent or another legal condition | Never used |
| Automated decisions | Some rights over automated decision-making (scope to confirm) | No system decides about individuals; a person reviews every output |
| Data residency | Limited to critical sectors, as reported | All services handling data above class P0 hosted in Bangladesh (NFR-02) |
| Harmful content | Content-removal duties reported or proposed | No generation of synthetic media; information-integrity research only under an ERRC-approved protocol, with no monitoring of individuals |

## 3. What qualified counsel must confirm

1. Commencement of each provision of the Personal Data Protection Act, 2026, the National Data Management Act, 2026 and the Cyber Security Act, 2026, and any rules issued (U1).
2. The exact content of the June 2026 cyber-security amendment and of any further amendment (U1).
3. The lawful grounds, exemptions and data-subject rights in the enacted text of the Personal Data Protection Act, 2026, including the section numbers cited by commentators (U1, U2).
4. The reuse terms of government publications used in the P0 corpus (U3).
5. Whether the selected host institution can accept a binding ERRC veto under its statutes (U15).
6. The status of the national AI policy (draft version 2.0 and the process announced for the fourth quarter of 2026).

## 4. Sources consulted in this verification

* [7] Securiti, An Overview of Bangladesh’s Personal Data Protection Act, 2026: <https://securiti.ai/bangladesh-personal-data-protection-act-overview/>
* [9] Dhaka Tribune, 30 June 2026: <https://www.dhakatribune.com/bangladesh/parliament/414016/cyber-security-amendment-bill-2026-passes-in>
* [14] The Daily Observer, 10 August 2026: <https://observerbd.com/news/587314>
* [40] The Financial Express, 30 June 2026: <https://thefinancialexpress.com.bd/sci-tech/bangladesh-amends-cybersecurity-law-drops-online-gambling-clause>
* [41] The Daily Observer, 2 July 2026: <https://observerbd.com/news/581694>
* [12] aipolicy.gov.bd, Draft v2 (listed): <https://aipolicy.gov.bd/docs/national-ai-policy-bangladesh-2026-2030-draft-v2.0.pdf>
* [62] Bangladesh Law Digest, 18 August 2026: <https://bdlawdigest.org/personal-data-protection-act-2026-bangladesh.html>
* bdnews24.com, report on the June 2026 amendment: <https://bdnews24.com/bangladesh/97045f1ac1ec>
* The Financial Express, 16 July 2026, cabinet committee review: <https://thefinancialexpress.com.bd/national/cabinet-committee-reviews-draft-cyber-security-amendment-act>
