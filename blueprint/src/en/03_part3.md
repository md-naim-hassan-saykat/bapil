# Part III: Technology

*The architecture, data, AI and language design, infrastructure and security of the platform, and the reference implementation that tests them.*

# Chapter 7: Reference Technical Architecture

## 7.1 From Six Layers to Twelve Components

The White Paper's six layers (data sources, data management, policy intelligence, knowledge management, decision support, governance and security) are refined here into twelve components grouped into four horizontal layers and one cross-cutting governance and security column.

<!-- FIGURE:04 -->

<!-- TABLE:19 -->

## 7.2 How a Request Flows

The core service is a cited answer to a policy question. The sequence below shows how a request passes through the components, and where controls are applied.

<!-- FIGURE:05 -->

Three properties of this flow matter for trust. First, the answer service never answers without evidence: if the top passages do not cover the query well enough, it abstains and shows the closest sources with the reason. Second, every answer sentence carries the identifier of the passage it came from, so a user can open and check the source. Third, every request, the passages retrieved and the response are written to a hash-chained audit log, so that what the system did can be verified later.

## 7.3 Interfaces and API Specification

The first public interface is a versioned REST API (`/v1`). The minimum endpoints are already implemented in the reference implementation (Chapter 11). Every response includes the corpus version and the identifiers of the passages used, so results can be reproduced later.

<!-- TABLE:20 -->

API rules: versions are part of the path; breaking changes are introduced only in a new version, with the old version kept for at least six months; all text is UTF-8; errors return a JSON object with a message; and request bodies are limited in size. In production the API sits behind the gateway (C8), which adds authentication, quotas and rate limits.

## 7.4 Architecture Decision Records

The Technical Architecture Board records each significant choice as an architecture decision record (ADR) in the repository, with its context, the decision, the alternatives considered and the consequences. The initial decisions are:

<!-- TABLE:21 -->

Lexical BM25 retrieval [101] is combined with dense multilingual embeddings [102] (ADR-004); lexical retrieval remains available as a transparent fallback. The portal meets WCAG 2.2 level AA [104] (ADR-007). ADRs are revisited when evidence changes, for example if a model selection review (Table 29) shows that a different approach performs better.

## 7.5 Accessibility and Inclusive Design

Many potential users work outside Dhaka, use mobile devices and face slow or unreliable connections; some have visual or other impairments. The portal is therefore designed to WCAG 2.2 level AA [104] from the first release, with these specific commitments:

* **Bangla first in the interface.** Menus, help texts and error messages are written in Bangla and English, and the user's language choice is remembered.
* **Light pages.** The search page stays under 500 KB and works on 3G connections (US-10); heavy features such as dashboards load only on request.
* **Screen-reader support.** Proper headings, labels and alternative text, and correct language tags so that screen readers pronounce Bangla and English text correctly.
* **Bangla input.** Search accepts Unicode Bangla typed with any common keyboard layout, as well as romanised Bangla, which is matched through transliteration candidates in later versions.
* **Plain language.** Answers and limitations are explained in plain words, and technical terms are linked to the glossary.

Accessibility is tested with automated tools at every release and with users, including users with disabilities, at least once in each pilot.

## 7.6 Technology Choices

The candidate technologies in Table 19 are open-source and widely used, which keeps costs low, supports local skills and avoids dependence on a single vendor. They are candidates, not commitments: the feasibility study (Deliverable D1.3) confirms choices against the host's infrastructure, skills and support arrangements. Where a commercial product is considered, it is assessed with the procurement clauses in Chapter 17, including the right to evaluate on BAPIL's benchmark and the right to exit with all data.

\newpage

# Chapter 8: Data Architecture and Data Governance

## 8.1 Public Data First

The safest and fastest route to value is to begin with information the state has already chosen to publish: laws, gazette notifications, budget documents, development plans, statistical releases and parliamentary papers. This material is large, important for policy work, under-used because it is scattered across sites and formats, and free of the privacy risks of personal data. The Right to Information Act, 2009 already establishes the principle of proactive disclosure [105].

## 8.2 The Data Lifecycle

<!-- FIGURE:06 -->

Each stage of the lifecycle has an owner and a control. Documents are **acquired** only from allow-listed sources whose reuse terms are recorded. They are **ingested** with text extraction, OCR where needed, and normalisation. They are **classified** into a data class and described with DCAT-aligned metadata. Originals are **stored** with checksums and version history. Text is **indexed** as passages for search. Data is **used** for search, answers and analytics under access control. Non-sensitive results are **published** as open data and benchmarks. Finally, records are **retained or disposed of** according to the retention schedule (Table 26).

## 8.3 Data Classification

<!-- TABLE:22 -->

The class of every dataset and document is recorded in the catalogue (component C3) and enforced at query time by the access-control layer (C9). A dataset takes the class of its most sensitive element. Moving a dataset to a lower class, for example by de-identification, requires a documented method and approval by the governance analyst and, for P2 data, by the ERRC.

## 8.4 Initial Source Inventory

<!-- TABLE:23 -->

## 8.5 Metadata, Provenance and Integrity

Each document in the corpus carries a metadata record aligned with the W3C Data Catalog Vocabulary (DCAT) version 3 [97] and the FAIR principles [98]. The fields are listed below; the JSON schema is published in the repository.

<!-- TABLE:24 -->

Integrity is protected in three ways: checksums detect any change to a stored original; a change log records every new version of a document; and the source allow-list (Chapter 10) limits where documents can come from.

## 8.6 Data Quality

Data quality is measured, not assumed. Each dimension below has a metric and a target for the pilot phase, and results are reported in the corpus release notes.

<!-- TABLE:25 -->

## 8.7 Bangla Text Quality

Much official Bangla text is published as scanned PDF. OCR errors, inconsistent Unicode encodings (for example, the letter য় written as one code point or as two) and mixed Bangla and ASCII digits all damage search quality. The ingestion component therefore (a) prefers born-digital sources, (b) applies Unicode normalisation and digit folding, (c) records an OCR quality score for every page, and (d) routes low-quality pages to a human correction queue. These corrections become a public dataset in their own right, useful to the wider Bangla NLP community [46, 48]. The detailed rules are set out in Chapter 9 (Table 27).

## 8.8 Data Roles

Clear roles make data governance work in practice:

* **Data custodians** are the agencies that publish or hold the source data. They decide on access and remain responsible for the authoritative version.
* **The BAPIL data lead** is accountable for the corpus, the catalogue, quality metrics and data agreements.
* **Data stewards** in each pilot team maintain metadata, check quality and handle correction queues.
* **The governance analyst** checks data classes, approves reclassification with the ERRC where required, and maintains the records of processing.
* **Chief data officers** in partner agencies, where appointed under the new data-management framework, coordinate agreements and the use of the national data exchange [84].

## 8.9 Retention and Disposal

<!-- TABLE:26 -->

## 8.10 Open Data Publication

Data that BAPIL creates from public sources (for example, the budget dataset from P2, corrected OCR text and the benchmark) is published as open data when quality checks are complete. Each release has a DOI, a datasheet, a licence (CC BY 4.0 unless the source requires otherwise), a methods note and a version number. Files are provided in open formats (CSV and Parquet for tables, JSON Lines for text and annotations), with a data dictionary in Bangla and English. Errors reported by users are logged publicly and fixed in the next version, and earlier versions remain available so that published analyses can be reproduced.

## 8.11 Data Access Agreements

Where data is not already public, access is governed by a written data-sharing agreement that states purpose, data class, retention, security controls, permitted outputs and audit rights (outline in Annex I). Where the national data exchange (NRDEX) provided for under the new data-management framework is available, BAPIL should use it rather than bilateral transfers [84]. Agreements are listed in the transparency register, without confidential details.

## 8.12 Personal Data

The Personal Data Protection Act, 2026 recognises citizens' rights over their personal data, requires consent and gives enhanced protection to sensitive and children's data; data subjects may restrict automated decisions based on their data [84, 85]. BAPIL's design responds conservatively: P2 data is used only in pilot P3, only with consent, only after a DPIA (template in Annex H), only in de-identified form and only for aggregate results; P3 data is never used. Commentators have argued that the new framework leaves broad room for state access to data [106]; BAPIL's own safeguards therefore do not rely on legal minimums alone.

\newpage

# Chapter 9: AI and Language Technology Design

## 9.1 Design Goal

The core technical goal is a **trustworthy bilingual question-answering and search service over official documents**: a user asks in Bangla or English and receives the most relevant passages and, where the evidence is sufficient, a short answer in which every sentence points to its source. When the evidence is insufficient, the service says so.

## 9.2 The Retrieval Pipeline

<!-- FIGURE:07 -->

The pipeline has six stages:

1. **Normalise.** Apply Unicode NFC; unify alternative encodings of Bangla letters; fold Bangla digits to ASCII for matching while keeping the original for display; remove zero-width characters that break matching; apply light stripping of common Bangla inflectional suffixes (for example -এর, -কে, -তে, -গুলো, -সমূহ) and simple English plural forms.
2. **Expand.** Add cross-lingual equivalents from a curated bilingual glossary of policy terms (for example *budget* and বাজেট, *data protection* and উপাত্ত সুরক্ষা), and spelling variants. The glossary is versioned, reviewed by language editors and published.
3. **Retrieve.** Score passages with BM25 [101] and, in the full system, with dense multilingual embeddings [102]; combine the two ranked lists.
4. **Check evidence.** Apply a calibrated score threshold and require that the top passages actually cover the query terms.
5. **Answer or abstain.** If the evidence is sufficient, select the most informative sentences from the top passages and attach a citation to each; optionally pass them to a language model that may only rephrase, with every output sentence verified against its cited passage. If the evidence is not sufficient, abstain and show the closest sources with the reason.
6. **Log.** Record the query, corpus version, passages, scores and output in the hash-chained audit log.

Retrieval-augmented generation is used because it grounds answers in external sources and makes them traceable [38]; extractive answering is the default because it removes the risk that a model invents content. Generation is enabled only after the citation-verification step passes the thresholds in Table 28.

## 9.3 Bangla Text Processing

Bangla text raises specific problems that general-purpose tools often handle poorly. The rules below are implemented in the reference implementation (module `bapil.text`) and extended in production.

<!-- TABLE:27 -->

Two principles guide these rules. First, normalisation is applied for **matching** but the original text is always kept for **display and citation**, so that users see exactly what the official document says. Second, every rule is tested with Bangla examples, and changes to the rules are evaluated on the benchmark before release.

## 9.4 Evaluation: the BanglaPolicyQA Benchmark

No responsible deployment is possible without measurement. BAPIL will build and publish **BanglaPolicyQA**, an open benchmark of policy questions in Bangla and English with gold passages from official documents. Annotation guidelines are given in Annex K.

* **Construction.** Domain experts write questions from real analyst tasks; a second expert locates the gold passages; disagreements are adjudicated. Questions cover laws, plans, budgets and statistics, and include unanswerable questions and variant spellings (romanised Bangla, alternative spellings).
* **Size.** Version 0 has 500 questions (Milestone MS3); version 1 has 2,000 (MS8).
* **Splits.** Each version has a public development set and a private held-out test set, so that results cannot be inflated by tuning to the test questions (risk R15).
* **Documentation.** The benchmark has a datasheet [100] describing sources, annotators, licences and known limitations.
* **Use.** Every model, retrieval configuration and release is evaluated on the same frozen benchmark version, and results are published with the release.

<!-- TABLE:28 -->

## 9.5 Evaluation Protocol

Results are only useful if they are comparable and honest. Every evaluation therefore follows the same protocol. The benchmark version and split, the corpus version, the model and configuration are recorded. Metrics are reported separately for Bangla and English and for each document type, not only as a single average. Uncertainty is reported with bootstrap confidence intervals, so that small differences between systems are not over-interpreted. A change is treated as an improvement only if it is better on the agreed primary metric without being worse on any safety threshold. Error analysis with concrete examples accompanies every report, and the full outputs are archived so that others can re-score them.

## 9.6 Model Selection

The Blueprint does not commit to a particular model vendor. Candidate models are open-weight, can run on infrastructure in Bangladesh, have documented Bangla capability and acceptable licences. Bangla-specific encoders such as BanglaBERT and generators such as BanglaT5 [46, 48] and Bangla-adapted open LLMs [49] are evaluated alongside multilingual models. Selection is made on BAPIL's own benchmark, not on public leaderboards, using the weighted criteria below. Every selected model receives a model card [99] and appears in the AI system register.

<!-- TABLE:29 -->

## 9.7 The Bangla Policy Foundation Model: a Staged Path

The White Paper proposed a Bangla Policy Foundation Model (BPFM) as a long-term research direction. Training a large model from scratch is expensive and, for many policy tasks, unnecessary. The Blueprint therefore sets out a staged path in which each step must be justified by evidence.

<!-- FIGURE:08 -->

* **Stage 0 (months 1 to 12).** Retrieval over existing open models; no training. Establish baselines on BanglaPolicyQA v0.
* **Stage 1 (months 13 to 30).** If the measured gap to the thresholds is material and governed data and compute are ready, apply parameter-efficient domain adaptation such as LoRA [103] on the governed public corpus, followed by instruction tuning on curated question-answer pairs. Publish a model card.
* **Stage 2 (after month 30, only if justified).** Continued pre-training on shared national compute, coordinated with any national Bangla LLM effort, with an independent audit before release.

<!-- TABLE:30 -->

At each gate the default is to remain at the current stage. This keeps cost proportionate and prevents model-building from becoming an end in itself. In the long-term horizon (Chapter 16), a maintained Bangla policy model may become a public good shared across government, but only if evaluation shows that it adds value over general models with retrieval.

## 9.8 Human Factors

Officials need to know when to trust an answer. The interface therefore always shows the source passages next to the answer, displays a confidence band rather than a single score, states known limitations of the corpus (for example, documents not yet ingested), and offers a one-click "report a problem" link that feeds the incident process. Training for pilot users covers how the system works, its failure modes and the duty to verify before relying on an output.

## 9.9 Environmental and Cost Footprint

AI computation consumes energy and money. BAPIL reduces both by preferring retrieval and small models, using quantised models for inference, reusing shared national compute for adaptation, and measuring the compute cost and estimated energy of each training run and release. Model cards report these figures so that decision-makers can weigh benefits against costs.

\newpage

# Chapter 10: Infrastructure, Hosting, Security and Continuity

## 10.1 Hosting

All services that handle data above class P0 are hosted in Bangladesh, at the National Data Center or another accredited facility, in line with requirement NFR-02 and with the draft national AI policy's intention to centralise national compute [88]. Development work on P0 data may use other environments, provided no P1 to P3 data is present.

## 10.2 Zones and Topology

<!-- FIGURE:09 -->

The deployment is divided into five zones. The **public zone** exposes only the portal and the API gateway behind a web application firewall with rate limits. The **application zone** runs the search, answer and analytics services. The **model zone** runs model inference on local GPUs and has no outbound internet access. The **data zone** holds the document store, the index and encrypted offline backups. The **management zone** holds identity, logging and security monitoring, the build pipeline with software bills of materials, and key management. All traffic between zones uses mutual TLS, consistent with zero-trust architecture [96].

## 10.3 Environments and Capacity

<!-- TABLE:31 -->

For the pilots, a modest footprint is sufficient: two to three general-purpose servers for the application and data zones, and one or two inference GPUs able to serve a quantised open model of roughly 7 to 14 billion parameters, plus around 10 to 20 TB of storage including backups. Stage 1 adaptation of the BPFM requires time-limited access to a larger GPU pool, which should come from shared national compute. These figures are planning assumptions for the feasibility study.

## 10.4 Security Framework

Security follows the six functions of NIST CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover) [14], in line with the national cyber-security law [86, 87]. The controls are mapped below.

<!-- TABLE:32 -->

## 10.5 AI-Specific Threats

AI systems add threats that conventional controls do not cover. The OWASP Top 10 for LLM Applications (2025) [95] and the NIST Generative AI Profile [94] are used as checklists.

<!-- TABLE:33 -->

## 10.6 Incident Management

Incidents are classified by severity, which sets the response time and who must be told. AI-specific incidents, such as systematically biased answers or a prompt-injection attack that changes behaviour, are handled in the same process as conventional security incidents, with ERRC review.

<!-- TABLE:34 -->

## 10.7 Business Continuity and Disaster Recovery

The July 2024 nationwide disruption showed how single points of failure can magnify the impact of an incident [108]. Bangladesh also faces floods and cyclones that can affect power and connectivity. BAPIL's services are not life-critical, but continuity matters for user trust and for the integrity of audit records. The targets below apply in the pilot phase and are tested in quarterly restore drills.

<!-- TABLE:35 -->

## 10.8 Supply Chain and Openness

Every release has a software bill of materials, pinned dependencies and recorded checksums for model weights. Code is published openly, which supports external review and aligns with the national source-code repository provided for in the new data-management framework [84]. Secrets never appear in code, prompts or logs.

\newpage

# Chapter 11: GitHub Reference Implementation

## 11.1 Purpose

A blueprint is more credible when its core ideas run. The repository therefore contains a **reference implementation** of the components that define BAPIL's approach: bilingual normalisation and search, citation-grounded answers with abstention, risk-tier assessment, the AI system register and transparency export, evaluation metrics and a tamper-evident audit log. It is a teaching and testing artefact, not a production system.

## 11.2 Design Choices

* **Python standard library only.** The package has no third-party dependencies, so it installs and runs offline on any machine with Python 3.10 or newer, including air-gapped government environments. Production components (Table 19) replace these modules behind the same interfaces.
* **Deterministic and inspectable.** BM25 scoring and extractive answering make every result explainable from the inputs.
* **Bilingual from the start.** Tests include Bangla and English queries, Bangla digits and alternative Unicode encodings.
* **Self-documenting corpus.** The demonstration corpus is BAPIL's own published documents, so it contains no third-party or personal data.

## 11.3 Repository Layout

```text
implementation/
├── pyproject.toml
├── README.md
├── src/bapil/
│   ├── text.py        # normalisation, tokenisation, glossary expansion
│   ├── corpus.py      # passages, provenance, checksums
│   ├── search.py      # BM25 index with bilingual expansion
│   ├── answer.py      # cited extractive answers and abstention
│   ├── risk.py        # risk tiers (Annex B)
│   ├── registry.py    # AI system register and transparency export
│   ├── evaluate.py    # Recall@k, MRR, nDCG
│   ├── audit.py       # hash-chained audit log
│   ├── api.py         # JSON HTTP API (standard library)
│   ├── cli.py         # command line interface
│   └── data/glossary_bn_en.json
├── schemas/           # JSON schemas: document, AI system record, risk assessment
├── examples/registry/ # AI system records for pilots P1 to P6
├── examples/risk/     # risk questionnaires, including the Annex B example
├── benchmarks/        # demonstration question set (bilingual)
└── tests/             # unit tests for every module
```

<!-- TABLE:36 -->

## 11.4 Running It

```bash
cd implementation
pip install -e .        # no third-party dependencies
python -m bapil.cli index --corpus ../reports ../blueprint
python -m bapil.cli search "data protection impact assessment"
python -m bapil.cli ask "বাংলা নীতি ফাউন্ডেশন মডেল কেন প্রয়োজন?"
python -m bapil.cli assess examples/risk/risk_p1_policy_search.json
python -m bapil.cli evaluate benchmarks/demo_questions.json
python -m bapil.cli register examples/registry --export build/register.md
python -m unittest discover -s tests
```

## 11.5 Demonstration Results

{{EVAL_RESULTS}}

These figures come from a small demonstration question set over BAPIL's own documents. They show that the evaluation harness works end to end; they are not evidence of performance on the national corpus, which will be measured on BanglaPolicyQA.

## 11.6 Testing Strategy

The unit tests cover every module and are organised by component: Bangla and English text processing (normalisation, digits, khanda ta, zero-width characters, suffixes and glossary expansion); corpus loading, passage splitting and provenance; bilingual search, including cross-lingual retrieval; cited answers and abstention; the risk-tier rules, including prohibited uses and high-risk conditions; the register and its schema validation; the evaluation metrics, including edge cases such as missing gold passages; the audit chain and detection of tampering; the HTTP API; and the command line. Tests use small fixture documents in both languages so that they run in seconds and give the same results on every machine. A test that fails blocks a release.

## 11.7 Continuous Integration

Two GitHub Actions workflows run on every change: one runs the unit tests on several Python versions; the other rebuilds the Blueprint tables, figures and PDFs with XeLaTeX and the Noto fonts, so that published documents can always be regenerated from source.

## 11.8 From Reference Implementation to Production

The reference implementation is deliberately small. The table below shows how each capability is replaced or extended for production, and when.

<!-- TABLE:37 -->

## 11.9 Versioning and Persistent Identifiers

Repository releases follow semantic versioning. Each publication in the BAPIL series receives its own Zenodo DOI, and related records are linked through Zenodo's related-identifier fields (for example, this Blueprint *is supplement to* the White Paper and *references* the Executive Summary). The policy is set out in Annex D.

\newpage
