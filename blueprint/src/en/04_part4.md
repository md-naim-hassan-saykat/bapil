# Part IV: Pilots and Assurance

*What BAPIL will pilot first, and the procedures and legal alignment that keep every system safe, lawful and accountable.*

# Chapter 12: Pilot Portfolio and Specifications

## 12.1 Selection Criteria

Pilots were chosen from the five illustrative projects in Appendix A of the White Paper plus information-integrity research, using four criteria: public value, feasibility with public data, low risk at the start, and reuse of shared components. Each pilot has a host-agency product owner, a risk tier, a minimum viable scope for the first 12 months and an exit criterion that decides whether it proceeds.

<!-- TABLE:38 -->

## 12.2 Sequencing

P1 and P2 start first because they use only P0 data, share the ingestion and search components, and deliver visible value within a year. P4 runs alongside P1 because it uses the same corpus and benchmark. P3 starts only after the DPIA is approved (Milestone MS5). P5 and P6 begin once the research team is in place. This order keeps risk low while the governance system matures. Each pilot reports monthly to the Director and quarterly to the Steering Board (Section 15.6), and can be stopped at any time by the Director, by the host agency’s product owner or, for tier T2 pilots, by the ERRC; stopping a pilot that does not work is a success of the governance system, not a failure.

## 12.3 Pilot P1: Bangladesh Policy Search Engine

**Problem.** Analysts spend hours finding and checking the authoritative text of laws, plans and budget documents in Bangla and English.

**Objective.** Reduce the time to find and cite authoritative evidence, with answers that always show their sources.

* **Corpus.** National laws (Bangla and English), the current five-year plan and perspective plan, and the last five years of budget speeches and key budget documents.
* **Functions.** Bilingual search; filters by document type, issuing body and year; passage view with link to the official source; extractive answers with citations; export of citations in a standard format.
* **Users.** Thirty or more analysts in two to three agencies, plus BAPIL researchers.
* **Risk tier.** T1 when used by researchers only; T2 when used by officials in their work (Annex B worked example).
* **Safeguards.** Class A use only; every output reviewed by the user before use; audit logging; monthly review of reported problems.
* **Evaluation.** Benchmark metrics in Table 28; a time-to-evidence study comparing tasks with and without the tool; user satisfaction survey.
* **Exit criterion.** Recall@10 of at least 0.85 and citation precision of at least 0.95, measured on the private test split under the protocol in Annex R, and a mean usefulness rating of at least 4.0 on a 5-point scale from at least 30 active users (Table 63). These are proposed targets; no results exist yet.
* **Path after the pilot.** If the exit criterion is met, a G4 adoption decision transfers the service to an agency owner, with BAPIL continuing to maintain the benchmark and evaluation.

## 12.4 Pilot P2: Budget Intelligence Dashboard

**Problem.** Budget allocations are published in PDF tables whose headings and structure change between years, which makes multi-year comparison slow and error-prone.

**Objective.** Publish five fiscal years of ministry-level allocations as consistent, machine-readable open data with a simple dashboard.

* **Data.** Published budget documents and the Annual Development Programme (P0).
* **Functions.** Reproducible extraction pipeline; a crosswalk of heading changes between years; CSV and Parquet downloads; a dashboard with comparisons by ministry, year and economic code; a methods note.
* **Users.** Finance and planning analysts, journalists and researchers.
* **Risk tier.** T1.
* **Evaluation.** Extraction accuracy on a hand-checked sample; user testing of the dashboard; downloads and reuse.
* **Exit criterion.** Extraction accuracy of at least 99% on the hand-checked sample and the dataset published with a DOI.

## 12.5 Pilot P3: Citizen Feedback Analyser

**Problem.** Public consultations can receive thousands of submissions, and owners struggle to read them all fairly, with a risk that minority views are missed.

**Objective.** Provide topic and sentiment summaries for one public consultation, in aggregate only, to help the owner read and respond to submissions.

* **Data.** Consented, de-identified submissions (P1 and P2) from one consultation chosen with the host agency.
* **Safeguards.** DPIA approved before any data is received; consent wording reviewed by the ERRC; de-identification before analysis; results reported only for groups of at least 20 submissions; every topic validated by people; no profiling of individuals.
* **Risk tier.** T2, with ERRC approval at G1 and G2.
* **Evaluation.** Agreement between human and automatic topic labels; coverage of minority views; owner feedback.
* **Exit criterion.** DPIA approved, topics validated by people and zero re-identification incidents.

## 12.6 Pilot P4: Bangla Policy Foundation Model, Stages 0 and 1

**Problem.** It is not known how well open models perform on Bangla policy text, or whether domain adaptation is worth its cost.

**Objective.** Establish baselines, publish BanglaPolicyQA and take an evidence-based decision on Stage 1 adaptation.

* **Data.** The governed public corpus (P0) and benchmark annotations.
* **Activities.** Model selection against Table 29; retrieval baselines; error analysis by document type and language; Stage 1 adaptation only if justified (Table 30).
* **Risk tier.** T1.
* **Exit criterion.** Benchmark published and Stage 1 decision documented.

## 12.7 Pilot P5: National AI Readiness Observatory

**Problem.** Decision-makers lack a consistent, national view of AI readiness across government, academia and industry.

**Objective.** Define an indicator framework and publish a first annual report with open data.

* **Data.** Public indicators and surveys (P0), including international indices interpreted with care because they measure different things [21, 26, 71].
* **Activities.** Indicator framework; data collection; annual report in Bangla and English; open dataset.
* **Risk tier.** T1.
* **Exit criterion.** First report published with open data.

## 12.8 Pilot P6: Information-Integrity Research

**Problem.** Misinformation and synthetic media in Bangla are growing concerns, but detection methods are rarely evaluated on Bangla content.

**Objective.** Review and benchmark methods for detecting Bangla misinformation and synthetic media, using public research datasets only.

* **Safeguards.** No monitoring of named individuals or groups; no operational content moderation; research protocol approved by the ERRC; respect for freedom of expression and privacy.
* **Risk tier.** T2 because of the sensitivity of the topic.
* **Exit criterion.** Methods paper published and ERRC approval of the research protocol.

## 12.9 What the Pilots Will Not Do

To prevent mission creep, the following are explicitly out of scope: monitoring of named individuals or groups on social media; prediction of individual behaviour; eligibility or enforcement decisions; and any system that publishes AI-generated text as official government communication.

\newpage

# Chapter 13: Responsible AI Assurance

## 13.1 From Principles to Procedure

The White Paper committed BAPIL to transparency, accountability, fairness, privacy, human oversight and safety. This chapter turns those commitments into a procedure that every system follows: a **risk tier** decides how much control is needed, and **lifecycle gates** decide when a system may move forward.

## 13.2 Risk Tiers

The tiering method combines the four categories of the draft national AI policy (prohibited, high, limited, low) [88] with the impact-level logic of Canada’s Algorithmic Impact Assessment [68, 69]. A short screening identifies prohibited uses; seven dimensions are then scored from 0 to 3 (Annex B). The rules are deliberately simple so that they can be applied consistently and audited.

<!-- FIGURE:10 -->

<!-- TABLE:39 -->

## 13.3 Lifecycle Gates

<!-- FIGURE:11 -->

* **G0 Register and screen.** Create the AI system record (Annex C), run the tier screening and confirm no prohibited use.
* **G1 Design review.** Approve the data plan, the DPIA where P2 data is involved, and the architecture (TAB).
* **G2 Pre-pilot readiness.** Show that benchmark thresholds are met and that red-team and security tests passed; ERRC approval for tier T2.
* **G3 Pilot.** Run with limited users, monitoring and an incident procedure; collect user feedback.
* **G4 Adoption decision.** Independent evaluation, acceptance by the host agency and legal review; transfer to class O under agency ownership, or stop.
* **G5 Update or retire.** Re-evaluate after any significant change; decommission responsibly and archive.

Checklists for each gate are provided in Annex J.

## 13.4 Human Oversight

Human oversight is not a single control but a set of patterns applied according to tier and use. The patterns below are combined for each system and recorded in its AI system record.

<!-- TABLE:40 -->

## 13.5 Documentation

Every system in the register has a model card [99] and, for each dataset, a datasheet [100]. The register is the single source for the public **transparency register**, generated automatically and published on the BAPIL website and in the repository (requirement FR-09). Each entry states the system’s purpose, owner, tier, maturity class, data classes, evaluation summary, known limitations and contact for complaints.

## 13.6 Incidents and Redress

An incident is any event in which a system produces or contributes to a harmful, misleading, discriminatory or insecure outcome, or in which a safeguard fails. Users and the public can report incidents through the portal. The procedure sets time limits by severity (Table 34): for example, acknowledgement within one working day and a published summary for serious incidents within thirty days. The ERRC reviews all serious incidents and may suspend a system.

Complaints follow the same channel. A complaint is acknowledged within one working day and answered within thirty days. A complainant who is not satisfied may ask the ERRC to review the decision; a complaint about the ERRC itself goes to the Steering Board co-chairs and is examined in the annual independent audit. These internal routes do not limit any legal remedy: complainants may also go to the authorities established under the data-protection and data-management laws or to the courts, and BAPIL cooperates with them.

## 13.7 Fairness and Language Equity

Fairness in BAPIL’s systems has a specific, measurable meaning: the systems must work as well in Bangla as in English, and as well for documents from different issuing bodies, regions and periods. Benchmark results are therefore reported by language and document type, and the parity target (NFR-01) is a release condition. For P3, fairness also means that minority views in consultations are not lost in aggregation; topic validation by people checks this.

## 13.8 Assurance for Generative Features

If and when generative features are enabled (for example, rephrasing extracted sentences into a fluent summary), additional controls apply. Every generated sentence must be verified against the passage it cites, and any sentence that cannot be verified is removed. The system prompt and model version are recorded in the audit log. Red-team tests cover prompt injection through documents, attempts to make the system produce content outside the corpus, and requests for prohibited outputs. Generated text is always labelled as such. This is BAPIL’s own rule; it is consistent with the draft national AI policy’s measures against false or misleading AI-generated content [89], but the draft, as reported, does not itself prescribe labelling. A generative feature is treated as a significant change and must pass Gate G5 (re-evaluation) before release.

## 13.9 Assurance for Procured and Third-Party AI

Not every AI system used in BAPIL’s pilots will be built by BAPIL. Where a component is procured or provided by a partner (for example, an OCR service, an embedding model or a hosted language model), it is subject to the same tier and gate procedure as BAPIL’s own components. The supplier must provide the documentation required by the procurement clauses in Chapter 17 (model cards, SBOMs and known limitations), BAPIL must be able to test the component on its own benchmark, and any change of version must be notified and re-evaluated. A third-party component that cannot be evaluated or documented cannot be used for data above class P0.

## 13.10 Independent Assurance and Audit

Self-assessment is necessary but not sufficient. Each year, an independent reviewer audits a sample of systems against their records, gate decisions and evaluation evidence, and checks that the audit logs verify. Before any G4 adoption decision, an independent evaluation is commissioned. Over time, the controls can support certification of the management system against ISO/IEC 42001 [92] and risk management guided by ISO/IEC 23894 [93].

## 13.11 Alignment with International Frameworks

The control areas map onto the main international frameworks, which helps partners and auditors understand the system.

<!-- TABLE:41 -->

\newpage

# Chapter 14: Legal and Policy Alignment in Bangladesh

## 14.1 A Changing Framework

Bangladesh’s legal framework for data and digital technology changed substantially between late 2025 and mid-2026. The Personal Data Protection Ordinance, 2025 and the National Data Management Ordinance, 2025 (called the National Data Governance Ordinance in some English reports) were gazetted in November 2025 [84, 106]. According to secondary legal commentary, the personal data protection ordinance came into force immediately except for its sections on chief data officers, complaints and offences [113], and an 18-month compliance window was described [114]. A Personal Data Protection (Amendment) Ordinance, 2026, which changed the ordinance’s data-residency provisions, was promulgated in February 2026 [115]; commentary describes localisation as limited to critical sectors such as banking and healthcare [122]. Parliament then passed bills to convert the ordinances into Acts: the National Data Management Bill, 2026 and the Cyber Security Bill, 2026 were reported passed on 10 April 2026 [86], and the Personal Data Protection Act, 2026 was reported enacted in April 2026 [85, 116]. Parliament passed a Cyber Security (Amendment) Bill, 2026 on 30 June 2026, but reports differ on its content: one report describes provisions for the rapid removal of harmful and defamatory AI-generated content from platforms [87], while others report that the bill removed a section on online gambling [123]. In July 2026 a cabinet committee was formed to review and finalise a draft Cyber Security (Amendment) Act, 2026 [124], so a further amendment may follow.

Three points of caution follow. First, these statements come from press reports and secondary commentary, which sometimes disagree; the gazetted texts were not reviewed for this edition because the official laws database does not permit automated retrieval. Second, enactment is not the same as commencement: whether each provision of the 2026 Acts is in force, and whether the deferred provisions of the ordinances were carried over, must be confirmed. Third, implementing rules may still be issued. Until the legal review confirms the position, BAPIL applies the stricter reading of each obligation.

<!-- TABLE:42 -->

## 14.2 Implications for BAPIL

* **Lawful basis and minimisation.** Because already-published documents carry low personal-data risk and need no new consent, the public-data-first policy is the main legal safeguard. Published personal data (for example names in gazette notices) is not aggregated or profiled. Any P2 processing requires a documented lawful basis and a DPIA.
* **Automated decisions.** The right to restrict automated decisions reinforces the design rule that BAPIL never automates decisions about individuals.
* **Data exchange.** If the national data exchange and the coordinating role of chief data officers operate under the Acts as described for the ordinances, they create a lawful route for data access agreements, which BAPIL should use.
* **Information integrity.** Research on misinformation must respect freedom of expression and privacy; reported proposals to require the rapid removal of harmful AI-generated content [87, 124] make clear, documented research protocols particularly important.
* **National AI policy.** The tier system is aligned with the draft policy’s categories so that BAPIL systems would be classified consistently if those categories are adopted. The Blueprint is offered as an input to the drafting process announced for the fourth quarter of 2026 [91], which follows the January and February 2026 drafts [88, 125].

## 14.3 Legal Review

Before Milestone MS2, the host institution should commission an independent legal review by qualified Bangladesh counsel. It should establish, from the gazetted texts: the enactment, publication and commencement dates of each relevant Act and amendment; which provisions are in force and which await notification or rules; whether BAPIL or its host is a data controller, processor or fiduciary for each pilot; the duties on custodians and on BAPIL for data access; and whether any element of the design needs a further approval. It should then review the charter, the data classification, the data-sharing agreement template and the DPIA template against those findings. The review is published, and Tables 42 and 43 are corrected accordingly.

## 14.4 Compliance Checklist

The checklist below turns the legal requirements, as currently reported, into BAPIL controls and the evidence that shows they are in place. It is updated after the legal review and whenever rules are issued.

<!-- TABLE:43 -->

## 14.5 Right to Information and Proactive Disclosure

The Right to Information Act, 2009 gives citizens a right to information held by public authorities and encourages proactive disclosure [105]. BAPIL supports this principle in two ways. First, by making already-published information easier to find and cite, it strengthens the practical value of proactive disclosure. Second, BAPIL itself practises openness: its transparency register, evaluation reports, ERRC decision summaries and annual financial summary are published without waiting for requests. Where BAPIL holds information on behalf of a public authority under a data-sharing agreement, requests for that information are referred to the authority that owns it.

## 14.6 Intellectual Property and Licensing

Government publications are generally reusable for research and public-interest purposes, but reuse terms differ between sources and are not always stated. BAPIL records the reuse terms of every source (Table 24), seeks written confirmation from custodians for bulk use, and respects any restrictions. BAPIL’s own outputs are licensed openly: documents and datasets under CC BY 4.0 and code under the MIT License. Benchmarks that contain extracts of official documents carry the source attribution required by the custodians.

## 14.7 Legal Status of BAPIL’s Own Arrangements

BAPIL’s charter, committees, tiers and gates are internal rules. They can bind BAPIL, its host and its partners only through the MoU, the host agreement, contracts and the charter; they cannot override a statute, the powers of a regulator or the host institution’s own legal obligations, and where these conflict the legal requirement prevails. Phase 1 needs no new legislation: it can proceed under an MoU, a host agreement, data-sharing agreements, the host’s procurement and ethics procedures and a funding agreement (Annex T, Table 65). Some long-term options would need more: a statutory centre (horizon H3) would need legislation, and any power to require agencies to share data or to follow BAPIL’s methods would have to come from law or from a government decision, not from BAPIL.

\newpage
