# Annex A: Requirements Traceability Matrix

<!-- TABLE:58 -->

Requirements not listed here are verified through pilot acceptance criteria (Table 38), security testing (Chapter 10) or governance review (Chapter 13).

\newpage

# Annex B: Risk-Tier Questionnaire

## B.1 Prohibited-Use Screening

Answer *yes* or *no*. Any *yes* places the system in tier T0, and work stops.

1. Does the system score or rank individuals for general social trustworthiness or behaviour (social scoring)?
2. Does it perform mass or indiscriminate biometric identification or surveillance?
3. Does it infer or profile individuals’ political opinions, religious beliefs or similar protected characteristics?
4. Does it generate deceptive synthetic media depicting real people?
5. Does it use manipulative techniques that exploit vulnerabilities such as age, disability or economic hardship?

## B.2 Scored Dimensions

<!-- TABLE:59 -->

## B.3 Tiering Rules

1. Any *yes* in B.1 gives **T0 Prohibited**.
2. Otherwise, the system is **T3 High** if the total score is 13 or more, or D1 = 3, or D2 = 3, or both D2 and D3 are 2 or more.
3. Otherwise, the system is **T2 Limited** if the total score is 6 or more, or D1 = 2, or D7 is 2 or more.
4. Otherwise, the system is **T1 Low**.

\looseness=-1 The rules are implemented in `bapil.risk` and tested against the examples in `implementation/examples/risk/`, including a prohibited social-scoring example (T0) and a benefit-eligibility example (T3).

## B.4 Worked Example: Pilot P1 in Class A Use

\enlargethispage{\baselineskip}
\looseness=-1 Scores: D1 = 2 (informs official decisions on policies), D2 = 0 (public documents), D3 = 0 (no individuals affected), D4 = 1, D5 = 1 (person reviews every output), D6 = 0 (no individuals affected), D7 = 1 (officials). Total = 5. No high-risk condition applies; because D1 = 2, the result is **T2 Limited**, requiring ERRC review, red-team testing, human review of every output and user training. The same system used only by BAPIL researchers (D1 = 1, D7 = 0) scores 3 and is **T1 Low**. This calculation is reproduced by `python -m bapil.cli assess examples/risk/risk_p1_policy_search.json`.

\newpage

# Annex C: Templates

## C.1 AI System Record (summary of fields)

| Field | Description |
|---|---|
| `system_id` | Unique identifier, for example `BAPIL-P1` |
| `name` | Name in English and Bangla |
| `purpose` | What the system is for and what it is not for |
| `owner` | Accountable person and unit; host-agency product owner if any |
| `maturity_class` | R, A or O |
| `risk_tier` | T0 to T3, with the date and reference of the latest assessment |
| `data_classes` | Data classes used (P0 to P3) |
| `models` | Models and versions, with links to model cards |
| `evaluation` | Benchmark version and headline results |
| `gate_status` | Latest gate passed and date |
| `oversight` | Human oversight patterns applied (Table 40) |
| `limitations` | Known limitations and failure modes |
| `contact` | How to report a problem or complaint |

The full JSON schema is `implementation/schemas/ai_system_record.schema.json`.

## C.2 Model Card (headings)

Model details; intended use and out-of-scope uses; training and adaptation data; evaluation data and results by language; fairness and robustness analysis; limitations and risks; ethical considerations; environmental and compute cost; versioning and contact [99].

## C.3 Datasheet for a Dataset (headings)

Motivation (why the dataset was created and by whom); composition (what it contains, data classes, languages, known gaps); collection process (sources, dates, reuse terms); preprocessing (extraction, OCR, normalisation, de-identification); uses (intended and not recommended); distribution (licence, DOI); maintenance (owner, update schedule, how errors are reported) [100].

## C.4 Incident Report (headings)

Reference number; date and time; system and version; reporter (optional); description; affected users or groups; severity (Table 34); immediate action; root cause; corrective action; ERRC review; public summary.

## C.5 Evaluation Report (headings)

System and version; benchmark version and split; metrics by language and document type (Table 28); comparison with the previous release and with thresholds; error analysis with examples; red-team and security results; known limitations; recommendation for the next gate.

\newpage

# Annex D: Publication, Versioning and DOI Policy

1. **Separate records per publication.** The White Paper, Executive Summary and this Blueprint each have their own Zenodo record and DOI. The Blueprint record contains the English and Bangla Blueprint and Summary, in PDF and Markdown, plus figures and tables in LaTeX, PDF and PNG.
2. **Related identifiers.** The Blueprint record declares that it *is supplement to* the White Paper (10.5281/zenodo.21363967), *references* the Executive Summary (10.5281/zenodo.21441172) and *is supplemented by* the GitHub repository release that contains the reference implementation.
3. **DOI reservation.** When the Zenodo record is created, its DOI is reserved before the record is published so that it can be printed in the documents; the PDFs are then rebuilt and uploaded. Until then the documents state that the DOI is to be assigned on publication.
4. **Repository releases.** Repository releases use semantic versioning. Release v1.1.0 adds the Blueprint and the reference implementation. The Zenodo record for this Blueprint is published only after that release is publicly listed at <https://github.com/md-naim-hassan-saykat/bapil/releases>, so that every artefact the documents refer to can be checked by readers.
5. **New versions.** Corrections produce a new version of the same Zenodo record (for example 1.0.1); substantive revisions produce Blueprint 2.0 (Milestone MS9).
6. **Licences.** Documents are CC BY 4.0; code is MIT.
7. **Language precedence.** The English edition is authoritative. Where the Bangla edition differs in interpretation, the English edition prevails.

\newpage

# Annex E: Draft BAPIL Charter

This draft is offered for adoption by the Steering Board at Milestone MS1, after consultation (Table 8). It is confirmed or amended after the independent legal review (Section 14.3), which is completed before Milestone MS2.

**Article 1. Name and status.** The Bangladesh AI Policy & Innovation Lab (BAPIL) is a research, policy-intelligence and capacity-building initiative hosted by [host institution] under a Memorandum of Understanding with the ICT Division.

**Article 2. Mission.** BAPIL helps Bangladesh use artificial intelligence for evidence-based policymaking, responsible AI governance, Bangla-language technology and public-sector innovation, through open research, tools, methods and training.

**Article 3. Boundaries.** BAPIL does not make policy, regulate, perform operational security functions or operate production government systems. It works with public data first, provides advice and not decisions, and never builds or supports surveillance.

**Article 4. Prohibited uses.** BAPIL will not build, pilot, evaluate for deployment or otherwise support any system for social scoring; mass or indiscriminate biometric identification or surveillance; profiling of political opinions, religious beliefs or similar protected characteristics; deceptive synthetic media depicting real people; or manipulation that exploits vulnerabilities.

**Article 5. Governance.** BAPIL is governed by a Steering Board, an independent Ethics and Risk Review Committee (ERRC) and a Technical Architecture Board, with the composition and powers set out in their terms of reference (Annexes F and G).

**Article 6. The ERRC veto.** No system of tier T2 or above may pass Gates G2 or G4 without the approval of the ERRC. ERRC decisions to refuse or suspend are binding and can be reversed only by the ERRC itself.

**Article 7. Registration and transparency.** Every AI system is registered before work begins. A public transparency register lists each system’s purpose, owner, tier, maturity class, data classes, evaluation summary, limitations and complaint contact.

**Article 8. Openness.** Code, benchmarks, evaluation reports and non-sensitive data are published openly with persistent identifiers. Exceptions for security or privacy are recorded in writing and reviewed annually.

**Article 9. Data protection.** BAPIL complies with the Personal Data Protection Act, 2026, the National Data Management Act, 2026 and related rules, and applies the data classification and safeguards of this Blueprint, which may be stricter than the law requires.

**Article 10. Independence and integrity.** Researchers decide methods and publish results. No funder may control research results or governance decisions. Conflicts of interest are declared and managed.

**Article 11. Transfer and withdrawal.** Tools that pass Gate G4 are transferred to agency ownership with documentation and support. BAPIL withdraws from any activity that conflicts with this charter.

**Article 12. Review and amendment.** The charter is reviewed at each strategic review (Table 48). Amendments require a two-thirds majority of the Steering Board after consultation with the ERRC; Articles 3, 4 and 6 can be weakened only after public consultation.

**Article 13. Precedence of law.** This charter operates within the law of Bangladesh and the rules of the host institution. Nothing in it overrides a statute, a regulator’s powers or the host’s legal obligations; where they conflict, the legal requirement prevails and the Steering Board amends the charter.

\newpage

# Annex F: Terms of Reference of the Ethics and Risk Review Committee

**Purpose.** To provide independent review of the ethical, legal and societal risks of BAPIL’s AI systems and research, and to hold a binding veto over tier T2 and T3 work.

**Composition.** Five to seven members, a majority external to BAPIL and the host institution, covering law and human rights, data protection, ethics, the relevant policy domains, Bangla language and civil society, with gender balance. The chair is an external member elected by the members. Members serve three-year terms, renewable once.

**Appointment and removal.** Members are selected through a published open call by an independent nominations panel (Annex S) and confirmed by the Steering Board, which may decline a nominee only with written reasons. Government bodies may propose candidates but may not hold a majority of seats. A member can be removed only for cause, by a two-thirds vote of the Steering Board after a hearing.

**Status.** The ERRC is created by the charter and the host agreement. Its decisions bind BAPIL by the charter and bind the host to the extent the host’s statutes allow and the host agreement provides (Section 5.3); it has no statutory powers and does not replace any regulator or the oversight committee proposed in the draft national AI policy.

**Responsibilities.**

* Review tier T2 and T3 systems at Gates G1, G2 and G4, and any reclassification of P2 data.
* Review serious incidents and decide on suspension.
* Approve research protocols involving people or sensitive topics, including P6.
* Advise the Steering Board on charter amendments and on the risk register.
* Publish summaries of its decisions within thirty days.

**Powers.** The ERRC may approve, approve with conditions, refuse or suspend. Refusal and suspension are binding. The ERRC may commission independent expert advice within its budget.

**Procedure.** The ERRC meets at least quarterly and as needed for gate reviews. A quorum is a majority of members including at least two external members. Decisions are taken by consensus where possible and otherwise by majority; dissenting opinions are recorded. Members declare conflicts and withdraw from related decisions.

**Resources.** The ERRC has a secretariat provided by the governance analyst and a budget for honoraria and expert advice, protected in the annual plan.

\newpage

# Annex G: Terms of Reference of the Steering Board and the Technical Architecture Board

## G.1 Steering Board

**Purpose.** To set BAPIL’s strategy, approve its plans and budgets, and hold its leadership to account.

**Composition.** Seven to nine members: the ICT Division (co-chair), the host institution (co-chair), the Planning Commission, a data custodian agency, an academic member from another university, a civil-society member and an industry member, with at least one member from outside Dhaka and with gender balance. The Director attends without a vote.

**Responsibilities.** Adopt the charter; approve the annual plan and budget; approve partnerships and senior appointments; take G4 adoption decisions jointly with host agencies; review the risk register quarterly; conduct the strategic reviews in Table 48.

**Procedure.** Meets quarterly; quorum of a majority including both co-chairs or their delegates; minutes published in summary.

## G.2 Technical Architecture Board

**Purpose.** To ensure that BAPIL’s systems are well designed, secure, interoperable and maintainable.

**Composition.** BAPIL’s lead engineers, the security lead and two external technical reviewers.

**Responsibilities.** Set architecture and security standards; approve designs at G1; approve models and major dependencies; maintain architecture decision records; review security test results.

**Procedure.** Meets monthly and as needed for design reviews; decisions recorded as ADRs in the repository.

\newpage

# Annex H: Data Protection Impact Assessment Template

A DPIA is required before any processing of P2 data and is recommended for any new use of P1 data.

1. **Description of processing.** Purpose; data subjects; categories of data; sources; recipients; retention; systems used.
2. **Lawful basis.** Basis under the Personal Data Protection Act, 2026; consent wording and records where consent is the basis.
3. **Necessity and proportionality.** Why the data is needed; why less sensitive data would not work; minimisation measures.
4. **Rights of data subjects.** How access, correction, deletion and objection are handled; confirmation that no automated decisions are made about individuals.
5. **Risks to individuals.** Re-identification, disclosure, misuse, discrimination, chilling effects; likelihood and severity of each.
6. **Measures.** De-identification method; aggregation thresholds; access control; encryption; retention and deletion; staff training.
7. **Residual risk and decision.** Remaining risks after measures; recommendation; approval by the governance analyst and the ERRC; review date.
8. **Consultation.** Views of the data custodian, the data protection officer of the host institution and, where appropriate, representatives of data subjects.

\newpage

# Annex I: Outline of a Data-Sharing Agreement

1. **Parties and contacts.**
2. **Purpose.** The specific research or pilot purpose; prohibition of other uses.
3. **Data description.** Datasets, fields, period, format, data class (Table 22).
4. **Legal basis.** Applicable provisions of the 2026 Acts and any rules; use of the national data exchange where available.
5. **Security.** Controls required (Table 32), hosting in Bangladesh, access list.
6. **Outputs.** Permitted outputs (for example, aggregate results only), review of outputs before publication, attribution.
7. **Retention and deletion.** Retention period (Table 26), deletion method and certificate.
8. **Audit and reporting.** Custodian’s right to audit; incident notification within 24 hours.
9. **Intellectual property and licensing.** Ownership of source data and of derived outputs; open licensing of BAPIL outputs where permitted.
10. **Term, review and termination.**
11. **Transparency.** Listing of the agreement, without confidential details, in the transparency register.

\newpage

# Annex J: Gate Checklists

## G0 Register and screen

* AI system record created in the register.
* Prohibited-use screening completed; no *yes* answers.
* Tier assessment completed (Annex B) and recorded.
* Owner and product owner named.

## G1 Design review

* Data plan with data classes and sources; reuse terms recorded.
* DPIA approved where P2 data is involved.
* Architecture reviewed and approved by the TAB; threat model includes AI-specific risks (Table 33).
* Evaluation plan with benchmark version and thresholds.
* ERRC review completed for tier T2 and T3.

## G2 Pre-pilot readiness

* Benchmark results meet the thresholds in Table 28.
* Red-team and security tests passed; findings resolved or accepted.
* Model card and datasheets published.
* User training materials ready; incident procedure in place.
* ERRC approval for tier T2.
* Single sign-on with MFA and roles, and the production audit store, in operation.

## G3 Pilot

* Pilot users enrolled and trained; human oversight patterns applied (Table 40).
* Monitoring and audit logging active; incidents reviewed monthly.
* User feedback and time-to-evidence data collected.
* Pilot report with results against exit criteria.

## G4 Adoption decision

* Independent evaluation completed and published.
* Host agency acceptance; agency legal review completed.
* Operating, support and funding arrangements agreed; transfer plan approved.
* Joint decision by the Steering Board and the host agency; ERRC approval for tier T2.

## G5 Update or retire

* Change assessed; re-evaluation completed on the current benchmark.
* Register and model card updated.
* For retirement: users informed, data retained or deleted per schedule, archive created.

\newpage

# Annex K: BanglaPolicyQA Annotation Guidelines (Summary)

1. **Question writing.** Questions are written by domain experts from real analyst tasks, in natural Bangla or English, including some romanised Bangla and variant spellings. Each answerable question should have a clear answer in the corpus. Out-of-scope questions, for testing abstention, are written as a separate set (200 in version 0) and need no gold passages.
2. **Gold passages.** A second annotator, who did not write the question, finds the passage or passages that answer it and records their identifiers. A passage is gold only if it alone supports the answer.
3. **Graded relevance.** Passages are marked 2 (fully answers), 1 (partly answers or provides necessary context) or 0 (not relevant).
4. **Adjudication.** Disagreements are resolved by a third annotator; agreement rates are reported in the datasheet.
5. **Balance.** The question set is balanced across languages, document types (laws, plans, budgets, statistics) and issuing bodies, and covers different periods.
6. **Quality control.** A random 10% of items is re-annotated each version; items with errors are corrected and logged.
7. **Ethics and licensing.** Annotators are paid fairly and credited; questions contain no personal data; the benchmark is released under CC BY 4.0 with source attribution.
8. **Splits and freezing.** Each version has a public development split and a private test split; versions are frozen and archived with a DOI.

\newpage

# Annex L: Glossary

| Term | Meaning in this Blueprint |
|---|---|
| Abstention | The system’s refusal to answer when the evidence is insufficient, with the closest sources and the reason shown |
| Adoption decision (G4) | The decision to transfer a tool to agency ownership as a class O system, or to stop |
| AI system register | The internal record of every AI system, from which the public transparency register is generated |
| BanglaPolicyQA | BAPIL’s open benchmark of policy questions in Bangla and English with gold passages |
| Citation precision | The share of answer sentences whose cited passage fully supports the sentence, as judged by trained annotators |
| Corpus version | An identifier of the exact set of documents and passages used for a result, enabling reproduction |
| Data class | The sensitivity class of data, from P0 (public) to P3 (sensitive personal data) |
| Extractive answer | An answer made of sentences selected from source passages, each with its citation |
| Gate | A documented decision point (G0 to G5) that a system must pass to move forward |
| Horizon | A period of the strategic roadmap (H0 to H4, and beyond 2041) |
| Maturity class | The status of a system: R (research), A (advisory) or O (operational, agency-owned) |
| Passage | A short section of a document, the unit of search and citation |
| Product owner | A named official in a host agency who defines needs and accepts or rejects a pilot |
| Risk tier | The level of risk of a system, from T0 (prohibited) to T3 (high), which sets the required controls |
| Transparency register | The public list of BAPIL’s AI systems with their purpose, tier, evaluation and limitations |

\newpage

# Annex M: Walkthrough of the Reference Implementation

This annex shows, step by step, what the reference implementation does with a question. It uses the two small test documents in `implementation/tests/fixtures/` (a sample policy note in English and its Bangla counterpart), so that the results are short, stable and can be reproduced exactly by anyone with the repository.

## M.1 A Cited Answer in English

```bash
python -m bapil.cli ask --corpus tests/fixtures --log build/audit.jsonl \
  "When is a data protection impact assessment required?"
```

```text
Q: When is a data protection impact assessment required?
Confidence: high
1. A data protection impact assessment is required before any processing
   of personal data at scale. [policy_en#p1]
2. বৃহৎ পরিসরে ব্যক্তিগত উপাত্ত প্রক্রিয়াকরণের আগে প্রভাব মূল্যায়ন আবশ্যিক। [policy_bn#p1]
3. Personal data may be processed only on a documented lawful basis.
   [policy_en#p1]
Sources:
  - [policy_en#p1] Sample Policy Note > Data Protection
  - [policy_bn#p1] নমুনা নীতি-নোট > উপাত্ত সুরক্ষা
```

Three features are visible. Every sentence carries the identifier of the passage it was taken from. The second sentence comes from the Bangla document, retrieved for an English question because the bilingual glossary links *data protection* with উপাত্ত সুরক্ষা and *impact assessment* with প্রভাব মূল্যায়ন. And the answer is extractive: each sentence appears word for word in the cited source.

## M.2 A Cited Answer in Bangla

```text
Q: বাজেট নথি কখন প্রকাশিত হয়?
Confidence: medium
1. প্রতি অর্থবছরে বাজেট নথি প্রকাশিত হয় যাতে নাগরিকেরা সরকারি ব্যয়
   অনুসরণ করতে পারেন। [policy_bn#p2]
2. জাতীয় বাজেটে মন্ত্রণালয়সমূহের জন্য অর্থ বরাদ্দ করা হয়। [policy_bn#p2]
3. ২০২৬ সালের বাজেটে নতুন বরাদ্দ রয়েছে। [policy_bn#p2]
Sources:
  - [policy_bn#p2] নমুনা নীতি-নোট > বাজেট স্বচ্ছতা
  - [policy_en#p2] Sample Policy Note > Budget Transparency
```

The Bangla question is answered from the Bangla passage, and the English passage on the same topic is listed among the sources. Confidence is reported as a band (high, medium or low) based on the evidence score and the share of query terms covered, not as a single number that could suggest false precision.

## M.3 Abstention

```text
Q: What is the boiling point of water in Kelvin?
ABSTAINED (no_matching_passages). Closest sources:
```

The question is outside the corpus, no passage matches, and the system says so instead of producing an answer. In the larger demonstration corpus, the system abstained correctly on all six out-of-scope questions (Section 11.5).

## M.4 The Machine-Readable Response

The same answer can be returned as JSON (option `--json`, or the `/v1/answer` endpoint of the API). An extract:

```text
{
 "question": "When is a data protection impact assessment required?",
 "abstained": false,
 "confidence": "high",
 "evidence": {"top_score": 7.881, "coverage": 1.0},
 "answer": [
  {"text": "A data protection impact assessment is required before ...",
   "citation": {"pid": "policy_en#p1", "doc_id": "policy_en",
                "heading": "Sample Policy Note > Data Protection"}},
  ...
 ],
 "sources": [
  {"pid": "policy_en#p1", "lang": "en", "score": 7.8812,
   "matched_terms": ["assessment", "data", "impact", "protection", "required"],
   "provenance": {"path": "tests/fixtures/policy_en.md",
                  "sha256": "b85002b0b751...", "data_class": "P0"}},
  ...
 ],
 "corpus_version": "3c204e06a617"
}
```

The response carries the evidence used to decide whether to answer, the terms that matched, the provenance of each source including its checksum and data class, and the corpus version. Together these allow any answer to be reproduced and audited later.

## M.5 The Audit Log

Each answer is written to an append-only log in which every record contains the hash of the previous one:

```text
{"hash":"760a77ff...","payload":{"abstained":false,
 "pids":["policy_en#p1","policy_bn#p1","policy_en#p1"],
 "q":"When is a data protection impact assessment required?"},
 "prev":"00000000...","ts":"...","type":"answer"}
```

```bash
python -m bapil.cli verify-log build/audit.jsonl
# build/audit.jsonl: 3 entries, chain intact
```

If any record is edited, deleted or reordered, verification fails and reports the first broken link. This is the mechanism behind requirement GR-04 and user story US-08.

## M.6 A Risk-Tier Assessment

```bash
python -m bapil.cli assess examples/risk/risk_p1_policy_search.json
```

```text
BAPIL-P1: T2 Limited (total 5)
  reason:   D1 = 2: informs official decisions on policies or programmes
  control:  All T1 controls
  control:  ERRC review
  control:  Red-team test
  control:  Human review of every output in use
  control:  User training
  control:  Incident procedure
  control:  Quarterly monitoring report
  approver: ERRC and Steering Board
```

The result reproduces the worked example in Annex B.4: the tier, the reason, the controls that become mandatory and the bodies that must approve.

\newpage

# Annex N: Contribution to the National AI Policy Elements

The draft National AI Policy 2026-2030 proposed several elements [88]. The table shows how BAPIL’s design could support each of them if they are retained in the final policy.

| Draft policy element | How BAPIL can contribute | Where in this Blueprint |
|---|---|---|
| Risk categories (prohibited, high, limited, low) | Operational tiering method with a questionnaire, rules and tested code | Chapter 13; Annex B |
| Algorithmic impact assessment for high-risk uses | Impact assessment template and worked examples; DPIA template | Annexes B and H |
| Independent oversight committee | Tested model of an ethics and risk committee with a binding veto and publication duty | Chapter 5; Annex F |
| Measures against false or misleading AI-generated content | Labelling (a BAPIL rule) and verification of generated text; research protocols for P6 | Section 13.8; Chapter 12 |
| Bangla-based national LLM | Open benchmark, governed corpus, evaluation protocol and an evidence-gated adaptation path | Chapter 9 |
| Centralised national compute | Modest pilot footprint and use of shared compute for adaptation | Chapter 10 |
| AI Innovation Fund | Open challenges and procurement clauses that keep markets open and fair | Chapter 17 |
| Skills and AI literacy | Competency framework, six training programmes and fellowships | Chapter 6 |
| Public-sector AI adoption | Gate-based path from pilot to agency ownership; transparency register | Chapters 12 and 13 |

\newpage

# Annex O: Indicative First-Year Work Plan for Pilot P1

| Months | Activities | Outputs | Gate |
|---|---|---|---|
| 1 to 2 | Appoint pilot lead and product owners; interview 15 to 20 analysts; register the system | User research summary; AI system record | G0 |
| 2 to 4 | Harvest laws, plans and budget documents; extraction and OCR; metadata and quality checks | Corpus release 0.1 with quality report | |
| 3 to 5 | Design review; threat model; evaluation plan; draft user interface in Bangla and English | Approved design; evaluation plan | G1 |
| 4 to 7 | Build search and answer services; bilingual glossary; portal; audit logging | Internal alpha | |
| 5 to 8 | Write and annotate BanglaPolicyQA v0 questions; baseline evaluation | Benchmark v0 (500 questions); baseline report | |
| 8 to 9 | Red-team and security tests; fix findings; train pilot users; ERRC review | Readiness evidence; model card | G2 |
| 9 to 12 | Pilot with 30 or more analysts in two to three agencies; monthly problem reviews; time-to-evidence study | Pilot report; user survey; Year 1 results | G3 |

\newpage

# Annex P: Evidence Status and Claim Verification

This annex records the evidence behind the Blueprint’s key factual claims, as checked on 21 and 22 October 2026, and how each claim is presented in the text. It uses nine status labels:

* **Verified fact:** confirmed against a primary or official source.
* **Source-reported fact:** reported by a credible secondary source but not independently confirmed against the primary text.
* **Research finding:** a result produced by the author’s own analysis or code, with its limits stated.
* **Author’s analysis:** a calculation or judgement by the author from stated inputs.
* **Design recommendation:** what the Blueprint proposes should be done.
* **Planning assumption:** an input to planning, such as a unit cost, to be replaced by better data.
* **Proposed target:** a value that a future measurement must reach.
* **Unverified claim:** a statement that could not be checked; marked “to be confirmed” in the text.
* **Future milestone:** something planned that has not yet happened.

<!-- TABLE:60 -->

**What was and was not checked.** The full English text, all tables and figures, the budget model and the reference implementation were reviewed, and the Bangla edition was compared with the English edition for numbers, dates, tables and cross-references. External claims were checked against the sources listed in the references, using official sources where they could be retrieved. The official Laws of Bangladesh database does not permit automated retrieval, so statutory texts, gazette notifications and commencement provisions were not read directly; the legal descriptions in Chapter 14 remain summaries of secondary sources and require confirmation by qualified Bangladesh counsel. The references taken from the White Paper bibliography (marked with an asterisk in the reference list) were re-checked against their sources on 22 October 2026; errors of title, year, DOI, authors or publisher in 13 of them were corrected in this Blueprint, a citation to the wrong edition of the Government AI Readiness Index was replaced, and the 2023 ranking was confirmed in the index report itself. Records of this evidence check are kept in the project repository.

\newpage

# Annex Q: Budget Reconciliation, Cost Types and Scenarios

The indicative budget in Chapter 17 (Table 50) is computed by `blueprint/src/budget_model.py` from the assumptions in Table 49. This annex reconciles it with the initial planning estimate made while the Blueprint was being drafted, separates one-time from recurring costs, and shows low, high and adjusted scenarios.

<!-- TABLE:61 -->

<!-- TABLE:62 -->

**Sensitivity.** Changing one assumption at a time from the base case: staff costs 20% higher or lower change the total by about Tk 2.0 crore; filling all Year 1 posts from month 1 adds about Tk 0.5 crore; equipment 25% dearer adds about Tk 0.7 crore; escalation of 10% instead of 8% adds about Tk 0.4 crore; and a taka 10% weaker against the US dollar adds about Tk 0.3 crore.

**Inputs still required.** The feasibility and costing study (Deliverable D1.3) should replace these assumptions with: the host’s salary scale, increment rules and overhead rate; quotations for servers, GPUs and storage; the host’s status for import duty and VAT; data-centre charges; confirmation of in-kind national compute; and agreed rates for annotators and trainers. Until then every figure here is an estimate, not approved funding.

\newpage

# Annex R: Evaluation Protocol and Release Gates

This annex turns the thresholds of Table 28 into a measurement procedure. It distinguishes what is measured automatically from what needs human judgement, states minimum sample sizes and the decision rule for each gate, and names who is responsible.

<!-- TABLE:63 -->

Five rules apply to every evaluation:

1. **Separate retrieval from answers.** Recall@10 measures whether the right passage was found; it says nothing about whether the answer is correct. Citation precision and the unsupported-claim rate measure answers, and are judged by people.
2. **Judge support, not presence.** A citation counts only if the cited passage, read on its own, fully supports the sentence. Annotators see the sentence and the passage, not the system version.
3. **Report uncertainty.** Every metric is reported with a 95% interval, by language and by document type. Differences smaller than the interval are not treated as improvements.
4. **Freeze and archive.** Each gate decision uses a frozen benchmark version, a recorded corpus version and configuration, and archived outputs that an independent evaluator can re-score.
5. **Fail safe.** If any safety measure (prompt injection, privacy, unsupported claims) misses its threshold, the system does not pass the gate, whatever its other results.

\newpage

# Annex S: Governance Bodies, Status and Safeguards

This annex sets out, for each proposed body, its status, how its members are appointed, its decision rights and their limits, how it reports and how its independence is protected. It also explains how BAPIL relates to existing institutions.

<!-- TABLE:64 -->

**Relationship with existing institutions.** Under the proposed model, BAPIL would be a research initiative inside a host institution with no regulatory role. The authorities created under the data-protection and data-management laws, the cyber-security authorities and the courts keep their full powers over BAPIL’s activities, as over any other organisation. The host institution’s own governing bodies, finance rules, audit arrangements and research ethics committee continue to apply. The independent oversight committee proposed in the draft national AI policy would be created by an Act of Parliament [88]; if it is established, BAPIL would register its systems with it and follow its decisions, and the ERRC would continue only as BAPIL’s internal review.

**Overlaps and how they are resolved.** The Steering Board and the host’s governing body both approve budgets: the host approves the financial framework and the Board approves the BAPIL plan within it. The ERRC and the host’s research ethics committee both review research with people: the ethics committee decides on research ethics, and the ERRC decides on system risk; neither may approve what the other has refused. Joint G4 decisions are shared between the Steering Board and the host agency because the agency carries the operational and legal responsibility for a tool it adopts.

\newpage

# Annex T: Preconditions, Authorisations and Work Packages

The 36-month clock cannot start until certain approvals, agreements and funds are in place. Table 65 lists them, with the instrument or authority each requires and its status. Table 66 then defines each work package with its owner, preconditions, acceptance tests, budget line, risks and decision gate.

<!-- TABLE:65 -->

**What does not need new legislation.** Phase 1 can proceed under an MoU, a host agreement, data-sharing agreements, the host’s procurement and ethics procedures and a funding agreement. **What would.** A statutory centre (an option for horizon H3), any power to require agencies to share data or adopt BAPIL’s methods, and the national oversight committee proposed in the draft policy would each need legislation or a formal government decision; none of them is assumed in the 36-month plan.

<!-- TABLE:66 -->

\newpage

# Annex U: Risk Monitoring

Table 55 lists the eighteen registered risks with their mitigations and owners. This annex adds what is needed to manage them in practice: an early-warning indicator that can be checked, a contingency if the risk occurs, the residual rating after mitigation and how often each risk is reviewed.

\begingroup\renewcommand{\bapiltablestretch}{1.10}

<!-- TABLE:67 -->

\endgroup

\newpage

# Annex V: Unresolved Items

This annex lists every item that could not be resolved with the evidence available at the time of writing, with its owner and how and when it will be resolved. Each item is also marked in the text where it applies.

<!-- TABLE:68 -->

\newpage

# Annex W: Jobs, Skills and Conditional National Scale-Up

The 36-month budget of about Tk 20.4 crore is often compared with much larger national programmes. This annex explains why the first stage is deliberately small, shows the jobs and skills that the plan creates, and sets out a costed national scale-up that would follow only if the pilots succeed.

## W.1 Why the First Stage Is Small

The 36-month budget is built from a staffing plan (Table 16) and unit costs (Table 49), not from a target amount. Its size reflects three constraints. First, the main cost and the main bottleneck is people: machine learning and Bangla language engineers are scarce, and a new lab can recruit only a few in its first year (Section 17.2). Second, nothing about the lab’s usefulness has yet been measured; staged funding lets the authorities pay for evidence before scale, with each further tranche following a gate decision (Table 48). Third, BAPIL should not duplicate larger programmes with different aims.

Three reference points are often cited. The draft national AI policy proposes an AI Innovation Fund of Tk 200 to 250 crore [88]; it is not an approved allocation, and BAPIL could apply to such a fund for specific pilots but is not a substitute for it. The KOICA-supported AI hub project (Tk 192.66 crore, July 2026 to December 2029) is a skills and startup programme: it aims to train 865 AI and digital technology specialists, with an 80% employment target, and to support 30 startups [35]. The proposed national budget for 2026-27 allocated Tk 500 crore to AI, electronics and youth innovation, mainly for startups and entrepreneurship [127]. BAPIL’s task is different: evidence and assurance for public policy. These programmes and BAPIL can reinforce each other. BAPIL’s posts and fellowships are a natural destination for graduates of national AI skills programmes, and BAPIL’s benchmarks, evaluation methods and transparency register can serve the AI tools those programmes help to build.

## W.2 Jobs and Skills

<!-- TABLE:69 -->

The 36-month plan creates 19 direct posts by Year 3, 28 graduate fellowship places and training for 500 officials. If the scale-up goes ahead, BAPIL would reach about 118 direct posts in Year 8, with 40 graduate fellows a year and about 5,500 officials trained in total. About a third of the scale-up posts are outside the central lab in Dhaka, in divisional university nodes and in adopting agencies, and about 30 are for Bangla language-data specialists. Contracts for annotation, OCR correction, hosting and events create further work that is not counted in Table 69. Employment is a benefit of the plan, not its objective: BAPIL is judged by the indicators in Table 54.

\newpage

## W.3 Conditional National Scale-Up (Years 4 to 8)

<!-- TABLE:70 -->

The scale-up extends what the pilots have shown to work. Its main components are a larger central lab (25 posts in Year 4, 45 in Year 8); four divisional university nodes, each with five posts, for regional training and research; analysts placed in adopting agencies (6 rising to 20); a Bangla language-data team of up to 33 staff for benchmarks, OCR correction and language resources; 20 to 40 graduate fellows a year; training for 5,000 officials; a national inference and search platform; and support for agencies joining federated search. The indicative cost is about Tk 218.9 crore over five years, rising from about Tk 25.5 crore in Year 4 to about Tk 60.9 crore in Year 8. With the 36-month plan, the eight-year total is about Tk 239 crore.

Four conditions apply. P1 and P2 must pass Gate G4; the independent final evaluation must be positive; the Steering Board and the authorities must decide to scale up at the strategic review (Table 48); and adopting agencies must agree to meet the operating costs of the tools they use, and possibly the cost of the analysts placed with them (Section 17.3). Possible sources are the government development budget, development partners and national AI innovation funds. The figures are planning estimates at the level of detail that is possible before the pilots; Blueprint 2.0 is to replace them with a costed plan.

## W.4 Integrated Institutional and Financial Pathway

Figure 16 and Tables 71 and 72 bring the institutional design (Chapter 5), the roadmap (Chapter 16), the budget (Chapter 17), the funding mix (Table 51) and the scale-up (Tables 69 and 70) into one view. For each stage they show who employs the staff, what the government does, how many posts exist, what it costs, who pays and what must happen before the next stage.

<!-- FIGURE:16 -->

<!-- TABLE:71 -->

\needspace{16\baselineskip}

<!-- TABLE:72 -->

Three points follow. First, government is involved from the start without BAPIL becoming a government department: the ICT Division signs the MoU and co-chairs the Steering Board, agencies own the tools they adopt, and government becomes the largest funder over time. Second, the government’s indicative share of the 36-month plan is about Tk 8.0 crore (39%), with the rest from research grants, development partners and industry; in the scale-up, government and agency service agreements together would provide about two-thirds. Third, every stage has a gate: money for the next stage follows evidence from the previous one.

\newpage

{{REFERENCES}}

\newpage

# Contact

**Md Naim Hassan Saykat**  
Independent Researcher, Bangladesh  
ORCID: <https://orcid.org/{{ORCID}}>

**GitHub:** <https://github.com/md-naim-hassan-saykat>  
**Repository:** <https://github.com/md-naim-hassan-saykat/bapil>

Comments, corrections and proposals for collaboration are welcome through the repository’s issue tracker.
