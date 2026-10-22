---
lang: en
---

# Bangladesh AI Policy & Innovation Lab (BAPIL)

## TECHNICAL BLUEPRINT

### From Framework to Implementation: Institutional Design, Reference Architecture, Governance, Delivery Plan and Strategic Roadmap to 2041 for an AI Policy-Intelligence Capability in Bangladesh

**Version 1.0**

**Md Naim Hassan Saykat**

Independent Researcher, Bangladesh  
ORCID: <https://orcid.org/{{ORCID}}>

{{DATE}}

**Blueprint DOI:** {{DOI_LINK}}  
**White Paper DOI:** <https://doi.org/10.5281/zenodo.21363967>  
**Executive Summary DOI:** <https://doi.org/10.5281/zenodo.21441172>  
**Repository:** <https://github.com/md-naim-hassan-saykat/bapil>

---

*This Technical Blueprint turns the BAPIL White Paper (Version 1.0) into a buildable plan. It specifies the institution, the people and skills, the reference architecture, the data and AI design, the governance and assurance system, a tested reference implementation on GitHub, a 36-month delivery plan, a strategic roadmap for 2026 to 2041 and beyond, and the decisions required from the relevant authorities. It is written for ministries, government agencies, technical teams, universities, civil society and development partners.*

\newpage

# Copyright & License

**Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint**

**Version:** 1.0  
**Publication Date:** {{DATE}}

© 2026 Md Naim Hassan Saykat.

Except where otherwise noted, this document is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** License. You are free to share and adapt it for any purpose, including commercial use, provided appropriate attribution is given, a link to the license is included, and any modifications are indicated.

License: <https://creativecommons.org/licenses/by/4.0/>

The source code of the reference implementation described in Chapter 11 is licensed under the MIT License, as stated in the repository `LICENSE` file. Figures and tables are generated from source files in the repository and are available in LaTeX, PDF and PNG formats under the same CC BY 4.0 licence.

\newpage

# Document Information

| Item | Information |
|---|---|
| **Document Title** | Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint |
| **Version** | 1.0 |
| **Publication Date** | {{DATE}} |
| **Author** | Md Naim Hassan Saykat |
| **Affiliation** | Independent Researcher, Bangladesh |
| **ORCID** | <https://orcid.org/{{ORCID}}> |
| **Language** | English (a Bangla edition is published alongside) |
| **Document Type** | Technical Blueprint |
| **Structure** | Five parts, 21 chapters, 23 annexes, 72 tables and 16 figures |
| **Evidence status** | Key claims checked against their sources in October 2026 (Annex P); unresolved items in Annex V |
| **License** | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| **Blueprint DOI** | {{DOI_LINK}} |
| **Builds on** | White Paper, Version 1.0: <https://doi.org/10.5281/zenodo.21363967> |
| **Companion** | Executive Summary, Version 1.0: <https://doi.org/10.5281/zenodo.21441172> |
| **Repository** | <https://github.com/md-naim-hassan-saykat/bapil> (release {{RELEASE}}) |

## Citation

Saykat, M. N. H. (2026). *Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint* (Version 1.0). Zenodo. {{DOI_LINK}}

## Disclaimer

This Blueprint is an independent research and policy-design document prepared by the author in an individual capacity. It does not represent the official position of the Government of Bangladesh, any ministry, agency, university or other organisation. Institutions, laws and programmes are named only to describe the context in which BAPIL would operate; naming them does not imply endorsement, partnership or agreement. Legal descriptions are summaries for planning purposes and are not legal advice. Cost, staffing and long-term targets are indicative planning assumptions to be validated by a feasibility study and revised at each strategic review. No funding has been requested, approved or committed, and none of the governance bodies described here has been constituted.

## How to Read This Blueprint

The Blueprint is organised in five parts. Readers with limited time can use the following routes:

* **Decision-makers:** the Overview at a Glance, Chapter 16 (strategic roadmap to 2041) and Chapter 21 (decisions).
* **Programme managers:** add Chapters 3, 5, 6, 12, 15, 17, 18 and 19.
* **Technical teams:** Part III (Chapters 7 to 11) with Annexes A, C, K, M and R.
* **Legal, governance and ethics specialists:** Chapters 8, 13 and 14 with Annexes B, E, F, H, I, J, S and T.
* **Researchers and universities:** Chapters 9, 11 and 20 with Annex K.
* **Development partners and finance reviewers:** Chapters 2, 16, 17 and 18 with Annexes Q, T and W.
* **Reviewers checking the evidence:** Annex P, which states the status of every key claim, and Annex V, which lists the unresolved items.

The words **must**, **should** and **may** carry their usual normative meaning: a requirement marked *must* is a condition of the design, *should* is a strong recommendation, and *may* is optional.

## Status of This Blueprint and Its Artefacts

This Blueprint is a proposal. To avoid confusing what exists with what is planned, the table states the status of each element at the time of writing. Claims in the text are classified in the same way in Annex P, using the labels defined there (verified fact, source-reported fact, research finding, author’s analysis, design recommendation, planning assumption, proposed target, unverified claim and future milestone).

| Element | Status at the time of writing (October 2026) |
|---|---|
| Institution, Steering Board, ERRC and TAB | Design recommendation. Nothing has been approved, constituted or funded |
| Legal analysis | Summary based on press reports and secondary legal commentary. The gazetted texts and their commencement provisions have not been reviewed; confirmation by qualified Bangladesh counsel is required |
| Reference implementation | Research prototype (package version 0.1.0) with 49 unit tests passing locally on Python 3.13. It is to be issued in repository release v1.1.0 with this Blueprint; readers can check whether the release is listed at <https://github.com/md-naim-hassan-saykat/bapil/releases>. If it is not listed, the code is not yet public. Not a production system; not tested with users |
| BanglaPolicyQA benchmark | Planned. Protocol and annotation guidelines exist; no questions have been written |
| Evaluation thresholds | Proposed targets. No pilot results exist |
| Pilots P1 to P6 | Proposed |
| Budget | Planning estimate computed from stated assumptions; not a quotation and not approved funding |
| Long-term targets (2028 to 2041) | Proposed targets, revised at each strategic review |

Items that remain unresolved, with their owners and how they will be resolved, are listed in Annex V (Table 68).

\newpage

# Overview at a Glance

**The problem.** Bangladesh’s laws, gazettes, budgets, plans and statistics are published across many websites and formats, often as scanned Bangla PDFs. Officials and researchers spend a large share of their time finding, checking and citing these sources. At the same time, the country is putting in place a new legal framework for data and a national AI policy, but has no operational method for governing AI systems in the public sector and no open Bangla benchmark for policy search.

**The proposal.** The Bangladesh AI Policy & Innovation Lab (BAPIL) is a university-anchored lab under a Memorandum of Understanding (MoU) with the ICT Division. It builds open, bilingual tools that help officials find and cite official evidence, develops and publishes the methods needed to govern public-sector AI safely, and trains people to use both.

**What is built first.** In its first year BAPIL delivers a bilingual policy search tool designed so that its answers cite official sources or abstain, with citation precision measured against a target of at least 0.95 (pilot P1), five years of budget allocations as open data (P2), the open BanglaPolicyQA benchmark (P4), a charter with an independent Ethics and Risk Review Committee, a public transparency register of AI systems, and training for 100 officials.

**How risk is controlled.** Public data first; advice, not decisions; no surveillance. Every system is placed in a risk tier (T0 prohibited to T3 high) and must pass lifecycle gates (G0 to G5) before it moves forward. The Ethics and Risk Review Committee has a binding veto over tier T2 and T3 work.

**What already exists, and what does not.** A small, tested reference implementation of the core components (bilingual normalisation and search, cited answers with abstention, risk-tier assessment, the AI system register, evaluation and a tamper-evident audit log) is issued with this Blueprint in GitHub release v1.1.0 and archived with the Blueprint’s Zenodo record, which is published only after that release exists (Annex D). It is a research prototype, not a production system. The institution, the pilots, the benchmark and the funding do not yet exist; they are what this Blueprint proposes.

**The long view.** A strategic roadmap sets five horizons: foundation (Q4 2026), short term (2027 to 2028), medium term (2029 to 2030), long term (2031 to 2035) and vision (2036 to 2041), followed by a charter renewal decision after 2041. It is aligned with the national AI policy cycle and with the 2041 national plans, and it is reviewed at fixed points and whenever major events occur.

**What it would cost.** An indicative budget, built from stated assumptions, is about Tk 20.4 crore over 36 months (Tk 17.9 to 25.3 crore across low and high scenarios). It is a planning estimate for a feasibility study to confirm, not approved funding (Chapter 17 and Annex Q). It deliberately funds a first stage only: if the pilots succeed, a costed national scale-up in Years 4 to 8 (about Tk 218.9 crore, rising to about 118 direct posts) is set out in Annex W; it is not requested now.

**What is asked of the authorities.** Six decisions (Chapter 21): accept the Blueprint as a technical input to national AI policy drafting; approve a 12-month Phase 1 pilot; authorise bulk access to already-public documents; nominate Steering Board members and agree an independent selection process for the ethics committee; commission a feasibility and costing study; and confirm the guardrails.

\newpage

## Acronyms

| Acronym | Meaning |
|----------|----------|
| ADP | Annual Development Programme |
| ADR | Architecture Decision Record |
| AIA | Algorithmic Impact Assessment |
| API | Application Programming Interface |
| BAPIL | Bangladesh AI Policy & Innovation Lab |
| BBS | Bangladesh Bureau of Statistics |
| BCC | Bangladesh Computer Council |
| BM25 | Okapi Best Matching 25 ranking function |
| BPFM | Bangla Policy Foundation Model |
| CI | Continuous Integration |
| CSF | Cybersecurity Framework (NIST) |
| DCAT | Data Catalog Vocabulary (W3C) |
| DOI | Digital Object Identifier |
| DPIA | Data Protection Impact Assessment |
| EGDI | E-Government Development Index |
| ERRC | Ethics and Risk Review Committee |
| FTE | Full-Time Equivalent |
| GPU | Graphics Processing Unit |
| KOICA | Korea International Cooperation Agency |
| KPI | Key Performance Indicator |
| LLM | Large Language Model |
| LoRA | Low-Rank Adaptation |
| MFA | Multi-Factor Authentication |
| MoU | Memorandum of Understanding |
| MRR | Mean Reciprocal Rank |
| nDCG | Normalised Discounted Cumulative Gain |
| NDMA | National Data Management Act, 2026 |
| NLP | Natural Language Processing |
| NRDEX | National Responsible Data Exchange |
| OCR | Optical Character Recognition |
| PDPA | Personal Data Protection Act, 2026 |
| RACI | Responsible, Accountable, Consulted, Informed |
| RAG | Retrieval-Augmented Generation |
| RPO | Recovery Point Objective |
| RTI | Right to Information |
| RTO | Recovery Time Objective |
| SBOM | Software Bill of Materials |
| SSO | Single Sign-On |
| SWOT | Strengths, Weaknesses, Opportunities, Threats |
| TAB | Technical Architecture Board |
| VAT | Value Added Tax |
| WCAG | Web Content Accessibility Guidelines |

\newpage

# Contents

\newpage

# List of Figures

# List of Tables

\newpage
