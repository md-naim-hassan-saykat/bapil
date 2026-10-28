# Legal and policy references: verification table

This document was checked on 21 to 23 October 2026. It is not legal advice.

On 22 October 2026 the numbers, titles and Gazette dates of the 2026 Acts were confirmed from official sources:
- the Legislative Division's list of Acts enacted in 2026;
- the Gazette copies published by the ICT Division.

Their provisions were read through the texts in the official laws database, using a public mirror. That route was needed for two reasons: bdlaws.minlaw.gov.bd does not permit automated retrieval, and the Gazette copies use a legacy Bangla font encoding that cannot be read automatically.

Statements about the content of provisions are therefore labelled as read from database texts. The Blueprint applies the stricter reading of each obligation. It also requires an independent review by qualified Bangladesh counsel in Phase 0, before the host agreement is signed (Blueprint Section 14.3; unresolved items U1 to U3 and U15; [`docs/engagement/counsel-checklist.md`](engagement/counsel-checklist.md)).

**Reference numbers** are those printed in the Technical Blueprint at the build of 23 October 2026. The Blueprint numbers its references in order of first citation, so the numbers change when citations are added. [`blueprint/review/REFERENCE_NUMBERS.md`](../blueprint/review/REFERENCE_NUMBERS.md) maps them to the stable source keys. The Summary and the Decision Memo number their own short reference lists.

## 1. Verification table

| # | Claim in the documents | Source | Provision | Status | Correction made | Documents affected |
|---|---|---|---|---|---|---|
| L1 | The Personal Data Protection Ordinance, 2025 and the National Data Management Ordinance, 2025 were gazetted in November 2025 | TBS [6]; commentary [80] | Whole instruments | Reported; consistent with the deemed commencement of the 2026 Acts from 6 November 2025 [42] | None needed | BP 14.1, Table 42 |
| L2 | Under the 2025 Ordinance, the sections on chief data officers, complaints and offences did not commence immediately; an 18-month window was described | Greenleaf and Al Razi [100]; Khan [101] | Commencement | **Superseded by the Act.** The Personal Data Protection Act, 2026 is deemed in force from 6 November 2025, except section 23 (chief data officers) and sections 31 to 35. Those come into force on a date notified in the Gazette after an 18-month period [42] | Section 14.1 and Table 42 now state the Act's commencement provision | BP 2.6, 8.12, 14.1, Table 42; SUM |
| L3 | A Personal Data Protection (Amendment) Ordinance, 2026 (Ordinance No. 23 of 2026), promulgated in February 2026, changed the data-residency provisions; localisation is described as limited to critical sectors | Digital Policy Alert [78]; TBS [79] | Data residency | **Read in the database text of the Ordinance (entry 1616, via the unofficial index):** section 2 replaced section 29(7)(kha) of the 2025 Ordinance. For restricted personal data and for critical information infrastructure, at least one synchronised, real-time copy of data held in the cloud must be kept in Bangladesh. The database records that the Ordinance was repealed by the Personal Data Protection Act, 2026 (Act No. 63). No localisation section was found in the database text of the Act that was read, but that text was incomplete. Whether the Act carries the rule over is open (U3) | None needed; U3 records the open question | BP 8.12, 14.1, Table 42 |
| L4 | The Personal Data Protection Act, 2026 is Act No. 63 of 2026, replacing the Ordinance | Legislative Division list [7]; Gazette copy [8]; Securiti [32] | Whole Act | **Verified (official sources):** Act No. 63 of 2026, Gazette of 10 April 2026 | Act number and Gazette date now cited to official sources | BP 1.1, 2.6, 14.1, Table 42; SUM; MEMO |
| L5 | The personal data framework "requires consent" | Previously cited to TBS and Securiti | Lawful grounds | **Incorrect as worded.** In the Act, section 5 makes consent the principal basis and allows processing without consent on specified grounds. These include a contract, legal claims, vital interests, employment and social security, and data the subject made public [42]. Commentary describes broad state exemptions [77] | **Corrected** (EN and BN). BAPIL's consent rule is labelled as its own safeguard, not a statutory requirement | BP 8.12, Annex M; SUM; MEMO; `implementation/tests/fixtures/` |
| L6 | Data subjects may restrict automated decisions | Act text [42]; Securiti [32] | Data-subject rights | **Read in the database text:** section 13 allows withdrawal of consent to automated decisions, and access copies must explain the logic of automated decisions (section 11). No general right to object to profiling was found | Wording kept as "withdraw from automated decisions (section 13)" | BP 8.12, 14.2, Table 42 |
| L7 | The National Data Management Act, 2026 and the Cyber Security Act, 2026 were enacted in April 2026 | Legislative Division list [7]; Gazette copies [9, 10]; Daily Sun [33] | Whole instruments | **Verified (official sources):** Act No. 80 and Act No. 81 of 2026, both gazetted on 10 April 2026. The Bangla title of Act No. 81 is সাইবার সুরক্ষা আইন, ২০২৬ | Now cited to official sources; the Bangla edition uses the official title | BP 1.1, 14.1, Table 42 |
| L8 | The June 2026 Cyber Security (Amendment) Act was about removing harmful AI-generated content | Earlier: Dhaka Tribune [102] | Amendment content | **Resolved from the enacted text:** the Cyber Security (Amendment) Act, 2026 (Act No. 99), gazetted on 1 July 2026 with immediate effect, omits only section 20 of Act No. 81, the online-gambling provision [11, 42, 43]. The earlier report is not borne out | **Corrected** (EN and BN); Table 42 and U1 updated | BP 2.6, 14.1, 14.2, Tables 42, 43, 60, 68; SUM |
| L9 | A further amendment to the cyber-security law is being prepared | The Daily Observer [103]; BLAST [44] | Draft amendment | Reported. A cabinet committee reviewed a draft from July 2026, and the draft was published for consultation in September 2026 and was still a proposal then | Stated as a proposal | BP 14.1, 14.2 |
| L10 | A draft National AI Policy 2026-2030 was released for public consultation in January 2026; a revised draft, version 2.0, dated 9 February 2026, is listed on the official portal | The Daily Star [12]; The Financial Express [13]; aipolicy.gov.bd listing [14] | Policy draft | Reported. Version 2.0 is listed with this title and date, but its content was **not** reviewed because automated access is blocked (new item U18) | The tier system is now described as "compatible with the categories reported for the draft policy" | BP 1.1, 13.2, 14.2, Tables 42, 60; SUM; MEMO |
| L11 | Formulation of a national AI policy will begin in the fourth quarter of 2026 with a joint team | The Daily Observer, 10 August 2026 [16]; 19 July 2026 [15] | Policy process | Reported. The article does not name the year; the fourth quarter of 2026 is the natural reading | Kept | BP 1.1, 14.2, Ch. 21, Table 60; SUM; MEMO |
| L12 | The draft national AI policy proposes risk categories, impact assessment, an independent oversight committee, a Bangla national LLM, national compute and an innovation fund | The Daily Star [12]; The Financial Express [13] | Policy content | Reported (January draft only) | Kept, attributed to the draft as reported (U18) | BP 2.6, Annex N, Table 42 |
| L13 | Right to Information Act, 2009 in force | Reference [74] | Proactive disclosure | Long-standing law (database entry 1011). It is now also named as the basis for reusing published documents, together with custodians' reuse terms. The database also lists a Right to Information (Amendment) Ordinance, 2026 (Ordinance No. 30 of 2026, 9 February 2026, entry 1623), which would have widened the definition of information and the proactive-disclosure duties. The database notes that it lapsed under Article 93(2) of the Constitution, so the 2009 Act applies as enacted. The unofficial index labels the 2009 Act "Repealed" without naming a repealing law; no repeal was found, and the label is treated as unreliable. Counsel to confirm (U1) | None | BP Table 4, Sect. 8.1, 14.5 and 16.11, Tables 42 and 43 |
| L14 | The White Paper (v1.0, July 2026) cites the Cyber Security Act, 2023 | White Paper reference list | Superseded instrument | The 2023 Act was replaced by the 2025 Ordinance and Act No. 81 of 2026. The White Paper is a DOI-registered record and was **not** edited | Recorded as a known limitation of the White Paper | WP (not changed) |

Azam's commentary, which earlier supported L4, is no longer cited in the Blueprint, because the official sources now support the same facts.

## 2. Statutory requirements and BAPIL's own safeguards

| Topic | What the law requires (as read) | BAPIL's own, stricter rule |
|---|---|---|
| Lawful basis | Consent as the principal basis, other specified grounds, broad state exemptions (section 5 and Chapter 5) | Personal data only in pilot P3, only with consent, only after a DPIA and ERRC approval, only de-identified and only for aggregate results. Names that appear in published Gazette notices are searchable only as part of those documents and are never profiled (Section 8.3) |
| Sensitive data | Explicit consent or another listed condition (section 7) | Never used |
| Automated decisions | Withdrawal of consent to automated decisions; logic explained on access (sections 11, 13) | No system decides about individuals; a person reviews every output |
| Data residency | Limited to critical sectors, as reported for the 2026 amendment ordinance (U3) | All services handling data above class DC0 hosted in Bangladesh (NFR-02) |
| Harmful content | Content removal or blocking under the Cyber Security Act, with Tribunal approval within three days; a further amendment proposed | No generation of synthetic media; information-integrity research only under an ERRC-approved protocol, with no monitoring of individuals |

## 3. What qualified counsel must confirm

See [`docs/engagement/counsel-checklist.md`](engagement/counsel-checklist.md). In short:

1. The provisions above against the Gazette texts (U1).
2. Whether the deferred sections of the Personal Data Protection Act have been notified, and whether any rules have been issued (U1).
3. Whether the 2026 data-residency changes survive in the Act (U3).
4. The content and status of the further cyber-security amendment (U1).
5. The reuse terms of government publications used in the DC0 corpus.
6. Whether the selected host can accept the ERRC veto under its statutes (U15).

## 4. Sources consulted in this verification

* [7] Legislative and Parliamentary Affairs Division, list of Acts enacted in 2026: <https://legislativediv.gov.bd/pages/static-pages/69df4f84e252a315b7e6b8db>
* [8] to [11] Gazette copies of Acts No. 63, 80, 81 and 99 of 2026, published by the ICT Division; listed at <https://ictd.gov.bd/pages/laws>
* [42] Laws of Bangladesh database texts (entries 1692, 1709, 1710 and 1728; each linked in the reference), read through laws.sayed.app, an unofficial index built from the database
* [32] Securiti, An Overview of Bangladesh's Personal Data Protection Act, 2026: <https://securiti.ai/bangladesh-personal-data-protection-act-overview/>
* [102] Dhaka Tribune, 30 June 2026: <https://www.dhakatribune.com/bangladesh/parliament/414016/cyber-security-amendment-bill-2026-passes-in>
* [43] The Financial Express, 30 June 2026: <https://thefinancialexpress.com.bd/sci-tech/bangladesh-amends-cybersecurity-law-drops-online-gambling-clause>
* [103] The Daily Observer, 2 July 2026: <https://observerbd.com/news/581694>
* [44] Bangladesh Legal Aid and Services Trust, 14 September 2026: <https://blast.org.bd/2026/09/14/8937/>
* [16] The Daily Observer, 10 August 2026: <https://observerbd.com/news/587314>
* [14] aipolicy.gov.bd, Draft v2 (listed): <https://aipolicy.gov.bd/docs/national-ai-policy-bangladesh-2026-2030-draft-v2.0.pdf>
* [77] Bangladesh Law Digest, 18 August 2026: <https://bdlawdigest.org/personal-data-protection-act-2026-bangladesh.html>
