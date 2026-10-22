# Part I: Foundations

*Why a blueprint is needed now, where Bangladesh stands, who must be involved, and what the system must do.*

# Chapter 1: Purpose, Scope and Method

## 1.1 Why a Blueprint Now

The BAPIL White Paper (Version 1.0) set out a vision: an independent research and policy-intelligence platform that helps Bangladesh use artificial intelligence (AI) for evidence-based policymaking, responsible AI governance, Bangla-language technology and public-sector innovation [1, 5, 7, 17, 21]. The Executive Summary condensed that vision for senior policymakers. Both documents deliberately stayed at the level of concepts, principles and illustrative pilots.

This Blueprint answers the next question: **what exactly would be built, by whom, under which rules, in what order, with what resources, and with what evidence of success?** It translates each element of the White Paper into requirements, institutional arrangements, technical components, data rules, assurance procedures, a delivery plan, a long-term strategy and decisions for the authorities.

The timing matters. During 2025 and 2026 Bangladesh adopted a new data-protection and data-management framework, first by ordinance and then, as reported, by Acts of Parliament, and revised its cyber-security law [84, 85, 86, 87]. Which provisions are in force, and from when, still has to be confirmed (Chapter 14). A draft National AI Policy 2026-2030 was released for public consultation in January 2026 [88, 89], and a revised draft (version 2.0, dated 9 February 2026) was posted on the official national AI policy portal [125]. In August 2026 the government announced that drafting of a national AI policy would begin in the fourth quarter of 2026 with a joint team from government, the private sector, academia and research [90, 91]; whether that process builds on the 2026 drafts has not been confirmed. A concrete, openly licensed blueprint with working code can serve as a technical input to that process, and a roadmap that looks to 2041 can help connect short pilots to the long-term goals of the Perspective Plan 2041 and the ICT Masterplan 2041 [29, 30].

## 1.2 The BAPIL Document Family

<!-- FIGURE:01 -->

<!-- TABLE:01 -->

## 1.3 Maturity Classes

To avoid confusion between experiments and government systems, the Blueprint uses three maturity classes. Each class has its own users, permitted data and approval route.

<!-- TABLE:02 -->

BAPIL builds systems of class R and class A. Class O systems are operated by agencies, never by BAPIL, and only after a G4 adoption decision with the agency’s own legal review.

## 1.4 What This Blueprint Adds to the White Paper

The White Paper described six architectural layers, a Policy Intelligence Dashboard, a Bangla Policy Foundation Model, a governance framework, a five-year roadmap and five illustrative pilots. This Blueprint adds:

1. **A situation analysis** with baseline indicators, a capability gap analysis and a SWOT assessment (Chapter 2).
2. **A stakeholder and engagement plan** (Chapter 3).
3. **Requirements** with identifiers, priorities, personas, user stories and traceability to code and tests (Chapter 4, Annex A).
4. **An institutional design** with an assessed operating model, governance bodies, decision rights and a responsibility matrix (Chapter 5, Annexes E to G).
5. **A people and capacity plan** with staffing, a competency framework and a training curriculum (Chapter 6).
6. **A reference architecture** of twelve named components, an API specification and architecture decision records (Chapter 7).
7. **Data rules**: a four-class data classification, a source inventory, metadata, quality, retention and a public-data-first policy (Chapter 8, Annex I).
8. **AI and language design**: a bilingual, citation-grounded retrieval pipeline, Bangla text rules, an evaluation benchmark, model selection criteria and a staged path for the Bangla Policy Foundation Model (Chapter 9, Annex K).
9. **Infrastructure, security and continuity** specifications (Chapter 10).
10. **A tested reference implementation** at research-prototype level, issued on GitHub with this Blueprint and archived with its Zenodo record once the release exists (Chapter 11; Annex D).
11. **Full pilot specifications** for six pilots (Chapter 12).
12. **An operational assurance system**: risk tiers, lifecycle gates, human oversight, documentation and a framework crosswalk (Chapter 13, Annexes B, C, H and J).
13. **Legal alignment** with the Bangladesh instruments in force or in preparation (Chapter 14).
14. **A 36-month delivery plan** and a **strategic roadmap for 2026 to 2041 and beyond** (Chapters 15 and 16).
15. **Financing, procurement, monitoring and evaluation, risk management and a research agenda** (Chapters 17 to 20).
16. **Six decisions** for the authorities (Chapter 21).
17. **Evidence and readiness annexes:** the status of every key claim, budget reconciliation and scenarios, the evaluation protocol, the status and limits of each governance body, the preconditions for starting, risk monitoring, and a register of unresolved items (Annexes P to V).

<!-- TABLE:03 -->

## 1.5 Scope and Boundaries

BAPIL remains a **research, policy-intelligence and capacity-building** initiative. It does not make policy, does not regulate, does not perform operational security functions and does not operate production government systems. Where a tool proves useful, ownership passes to the responsible agency through a documented adoption decision (Gate G4, Chapter 13).

Three boundaries are designed in from the start:

* **Public data first.** Pilots begin with documents and statistics that are already officially published. Personal data is excluded unless there is a lawful basis, a data protection impact assessment and ethics approval; sensitive personal data is excluded entirely (Chapter 8).
* **Advice, not decisions.** Every AI output is evidence for a person to weigh. No BAPIL system makes or automates decisions about individuals (Chapters 4 and 13).
* **No surveillance.** Social scoring, mass or indiscriminate biometric surveillance and the profiling of people’s political or religious opinions are prohibited by charter (tier T0, Chapter 13).

Within these boundaries, the Blueprint covers the full life of the capability: from the first briefing in late 2026, through a three-year pilot programme, to the long-term questions of scale, institutional form and sustainability that arise between 2030 and 2041.

## 1.6 Method

The Blueprint was prepared in six steps, each of which can be checked against the published sources and the repository:

1. **Review of the BAPIL series.** Every chapter of the White Paper and the Executive Summary was mapped to a design question and to the chapter of this Blueprint that answers it (Table 3).
2. **Review of the context.** The legal and policy changes of 2025 and 2026 were reviewed using official announcements and press reports, and indicators of digital government, cyber security and AI readiness were collected (Chapter 2). Because the gazetted texts of several 2026 Acts were not available in full at the time of writing, legal descriptions are marked as summaries to be confirmed.
3. **Design against reference frameworks.** Requirements and controls were derived from the OECD AI Principles, the UNESCO Recommendation, the NIST AI Risk Management Framework, ISO/IEC 42001, the EU AI Act and Canada’s Directive on Automated Decision-Making [1, 4, 5, 6, 7, 68, 92], and adapted to Bangladesh’s draft national AI policy categories [88].
4. **Implementation as a test of design.** The core ideas (bilingual search, cited answers with abstention, risk tiers, the register, evaluation and audit) were implemented and tested in code. Where implementation revealed a gap in the design, the design was corrected.
5. **Planning and review.** Delivery, resources, risks and long-term strategy were planned with explicit assumptions, so that each can be tested by the feasibility study and the strategic reviews.
6. **Evidence check.** In October 2026, before publication, external claims were checked against their sources, the budget was recomputed from its line items, and claims were classified by their evidence status (Annex P). Statutory texts on the official laws database could not be retrieved by automated means, so legal descriptions remain summaries to be confirmed by counsel.

## 1.7 Summary of the Design

In one paragraph: BAPIL would be established as a **university-anchored lab with a government MoU and a multi-stakeholder Steering Board**, an **independent Ethics and Risk Review Committee with a binding veto**, and a **Technical Architecture Board**. It would build an **open, modular platform** whose core is a **bilingual, citation-grounded policy search and answer service** over officially published documents. Six pilots would be run under **risk tiers and lifecycle gates** aligned with international frameworks and with Bangladesh’s new data laws. A **36-month plan** delivers a policy search pilot and an open budget dataset in Year 1, evaluated adoption decisions in Year 2, and in Year 3 a documented decision on Bangla domain adaptation (with an adapted model only if Stage 1 is justified) and Blueprint 2.0. A **strategic roadmap** then carries the capability through medium-term adoption (2029 to 2030), a national policy-intelligence network (2031 to 2035) and a mature, trusted institution by 2041. A small **reference implementation** of the core components is issued with this Blueprint; it is a tested research prototype, not a deployed system.

\newpage

# Chapter 2: Situation Analysis and Baseline

## 2.1 Purpose of the Analysis

A blueprint is only as good as its understanding of the starting point. This chapter summarises where Bangladesh stands on the capabilities BAPIL depends on: digital government, data, cyber security, AI readiness, Bangla language technology and the legal framework. It then identifies the gaps that BAPIL is designed to close and assesses the strengths, weaknesses, opportunities and threats that will shape delivery. The indicators also serve as a baseline for the long-term targets in Chapter 16.

## 2.2 Baseline Indicators

<!-- TABLE:04 -->

The indicators point in a consistent direction. Bangladesh has a substantial digital government foundation: the United Nations E-Government Survey 2024 placed the country 100th of 193, eleven places higher than in 2022 [21, 107, 120], and the national portal and electronic file system are in wide use [32, 83]. Cyber-security frameworks have been strengthened: Bangladesh was designated a Tier 1 role-model country in the ITU Global Cybersecurity Index 2024, although commentators note that the index measures the existence of frameworks more than their performance under stress [71, 108, 119]. AI readiness is lower: Bangladesh was reported as 82nd in the 2023 Government AI Readiness Index, and university AI departments report very limited GPU capacity [80]. The legal framework for data has just been renewed [85, 86], and the national AI policy is being drafted [88, 91].

## 2.3 Digital Government Foundations

BAPIL does not start from nothing. Over the past fifteen years Bangladesh has built a national portal that brings together the websites of ministries, divisions and field offices [83]; an electronic file and workflow system (e-Nothi) used across the administration [32]; a national data centre; an open data portal and regular statistical releases from the Bangladesh Bureau of Statistics [31, 33]; and a large network of digital service centres. These systems matter for BAPIL in three ways. They are the main **sources** of the official documents that P1 indexes. They provide **infrastructure** (hosting, identity, networks) that BAPIL should use rather than duplicate. And the people who built and run them form a community of practice with **experience** of digital change in government, which BAPIL’s pilots and training can draw on.

The same foundations also show where work is needed. Document formats and metadata vary between sites; many older documents exist only as scans; search functions on government websites are limited and rarely bilingual; and there is no single place where the current, authoritative version of a law or plan can be found and cited. These are exactly the gaps that a governed corpus and a cited search service address.

## 2.4 The Policy Evidence Problem

The problem BAPIL addresses first is practical and common. A policy analyst who needs to know what the law says on a topic, what the current five-year plan committed to, or how a budget line changed over five years must usually:

* search several government websites, each with its own structure and search function;
* open scanned PDF files whose text cannot be searched or copied reliably, especially in Bangla;
* check whether a document is the current version or has been amended or superseded;
* translate or reconcile terms between Bangla and English versions; and
* record the citation manually for a brief or a file note.

These steps take time and introduce errors. They also make it hard to build reliable AI tools, because those tools depend on clean, versioned, well-described text. Studies of public data in Bangladesh have pointed to inconsistent metadata, licences and quality across portals [78, 79]. The design response is therefore to begin with a governed corpus of official documents and a search service that always shows its sources, before attempting anything more ambitious.

## 2.5 Bangla Language Technology

Bangla is one of the most widely spoken languages in the world, but it remains under-resourced in AI. Research groups in Bangladesh and abroad have produced strong models and datasets, including BanglaBERT, BanglaT5, Bangla-adapted open LLMs and large sentiment corpora [46, 48, 49, 81]. What is missing for policy work is narrower and more specific: a benchmark built from real policy questions with answers grounded in official documents; consistent rules for normalising Bangla text from scanned and born-digital sources; and evaluation results that show how well open models perform on Bangla policy text compared with English. Chapter 9 and Annex K set out how BAPIL fills these gaps.

## 2.6 Legal and Policy Context

The legal framework is described in Chapter 14. In summary, and as reported in secondary sources, the Personal Data Protection Act, 2026 and the National Data Management Act, 2026 replaced the 2025 ordinances; they recognise citizens’ rights over personal data and, as described for the ordinances, provide for a national data management authority and a national data exchange [84, 85, 86, 116]. Under the 2025 ordinance some provisions did not commence immediately [113], so which duties are already operative must be confirmed. The cyber-security ordinance was converted into an Act in April 2026 and an amendment bill was passed in June 2026; reports differ on what that amendment contains, and a further draft amendment was under review in July 2026 [86, 87, 123, 124]. The draft national AI policy proposes risk categories, impact assessment, an independent oversight committee to be created by an Act of Parliament, a Bangla-based national LLM, centralised compute and an innovation fund [88]. Together these create both a legal basis for a public-data-first design and a policy window in which a tested blueprint can be useful.

## 2.7 Capability Gap Analysis

<!-- TABLE:05 -->

Three gaps are critical for BAPIL’s first phase. The **document access gap** prevents any reliable AI tool from being built on official text; the **evaluation gap** means there is no shared way to know whether a tool works in Bangla; and the **governance practice gap** means that, even with a draft policy, agencies lack a tested procedure for deciding when an AI system is safe to use. The first year of the roadmap is designed to close these three gaps on a small scale.

## 2.8 SWOT Assessment

<!-- TABLE:06 -->

The SWOT assessment leads to four strategic choices that run through the Blueprint:

1. **Build on strengths:** use the existing digital service experience and the new data laws rather than creating parallel structures.
2. **Address weaknesses directly:** treat document quality and Bangla text processing as core work, not as preparatory chores.
3. **Use the opportunity window:** offer the Blueprint as an input to national AI policy drafting from the fourth quarter of 2026.
4. **Guard against threats:** design for institutional change, misinformation risks and infrastructure disruption from the start, with an institution-neutral design, strict prohibited uses and continuity planning.

## 2.9 Lessons from International Practice

The White Paper reviewed AI and digital government strategies in Singapore, Korea, Estonia, the United Kingdom, Finland, the United Arab Emirates and Canada [51, 54, 57, 60, 61, 63, 65, 68]. Five lessons are applied in this Blueprint:

* **Start with a concrete service.** Successful programmes began with a specific, visible service rather than a general platform. BAPIL starts with policy search (P1) and open budget data (P2).
* **Make governance operational.** Principles become useful only when turned into procedures with owners and deadlines, such as Canada’s Algorithmic Impact Assessment [68, 69] and Singapore’s Model AI Governance Framework [51, 53]. BAPIL’s tiers and gates follow this approach.
* **Invest in shared infrastructure.** Estonia’s X-Road shows the value of a shared, secure data exchange layer [59]; BAPIL should use Bangladesh’s national data exchange rather than create its own.
* **Build literacy widely.** Finland’s Elements of AI course shows that broad AI literacy is achievable [64]; BAPIL’s training programme T1 to T6 applies the same principle to officials.
* **Publish and learn.** The UK’s AI Playbook and similar guidance documents are revised as experience grows [61]; BAPIL publishes its evaluations, including failures, and revises the Blueprint at fixed points.

\newpage

# Chapter 3: Stakeholders and Engagement

## 3.1 Why Engagement Is Part of the Design

AI tools for policy work succeed or fail on the trust and participation of the people who use, govern and are affected by them. Engagement is therefore treated as a design element with its own plan, owners and outputs, not as communication after the fact. The plan has three aims: to ensure that pilots answer real policy needs; to give those who could be affected a voice in governance; and to coordinate with other national programmes so that effort is not duplicated.

## 3.2 Stakeholder Map

<!-- FIGURE:02 -->

The map groups stakeholders by their influence over BAPIL’s success and their interest in its work. Those in the upper right quadrant, such as the ICT Division, the Planning Commission, the Finance Division and the Legislative and Parliamentary Affairs Division, are managed closely through the Steering Board, data agreements and product ownership. Those with high influence but less direct interest, such as the Cabinet Division and the data management authority, are kept satisfied through milestone briefings and consultation on data use. Universities, civil society and citizens have high interest and are kept informed and involved through fellowships, ERRC membership, open consultations and the public transparency register.

## 3.3 Stakeholder Register

<!-- TABLE:07 -->

## 3.4 Consultation and Engagement Plan

<!-- TABLE:08 -->

Engagement follows four principles:

* **Bilingual by default.** Consultation materials, summaries and reports are published in Bangla and English.
* **Reach beyond Dhaka.** At least one consultation in each phase is held outside Dhaka or online with participants from divisional universities and local administrations.
* **Inclusion.** Consultations seek a gender balance and include organisations representing persons with disabilities, minorities and young people.
* **Closing the loop.** Each consultation produces a published comment log that records what was raised and how BAPIL responded.

## 3.5 Engaging Citizens and Communities

Although BAPIL’s first users are officials and researchers, its ultimate beneficiaries are citizens, and some of its work (such as P3 on public consultations and P6 on information integrity) touches citizens directly. Citizen engagement therefore has three elements. First, **transparency**: the public register, plain-language summaries of every pilot in Bangla, and an annual public report. Second, **voice**: open consultations on the charter and on Blueprint 2.0, civil-society members on the ERRC, and a public channel for reporting problems and complaints. Third, **benefit**: open datasets such as the budget data from P2, and, in the long term, public-facing search over official documents so that citizens, journalists and civil-society organisations can find and cite the same authoritative texts as officials.

## 3.6 Coordination with National Programmes

BAPIL complements, and must not duplicate, existing programmes. A KOICA-supported project to build AI skills and an AI hub, to be implemented by the Bangladesh Hi-Tech Park Authority under the ICT Division, focuses on skills, startups and adoption: its technical assistance project proposal (Tk 192.66 crore) was awaiting government approval in June 2026, and a USD 13 million grant agreement for 2026 to 2029 was reported signed in August 2026 [35, 36, 117]. BAPIL focuses on policy intelligence, governance methods and open evaluation. The draft national AI policy envisages a Bangla-based national LLM, centralised compute at the National Data Center and an AI Innovation Fund [88]; BAPIL’s benchmark and governed corpus can serve those efforts, and BAPIL should use shared national compute rather than build its own large cluster. A short division-of-labour MoU between BAPIL, the AI Hub and other relevant programmes should be signed at Milestone MS2 and reviewed annually.

\newpage

# Chapter 4: From Vision to Requirements

## 4.1 Approach

Requirements were derived from three sources: the White Paper’s architecture, dashboard, foundation-model and governance chapters; the international frameworks the White Paper adopted as reference points [1, 4, 5, 6, 7, 68]; and the Bangladesh legal context summarised in Chapter 14. User needs were captured as personas and user stories. Each requirement is stated once, given an identifier and a priority, and traced to the components, code modules and tests that satisfy it (Annex A).

## 4.2 Users and Personas

Six personas represent the main user groups. They are composites built from the White Paper’s analysis and the stakeholder register; they will be validated and refined through co-design sessions in the first six months.

<!-- TABLE:09 -->

## 4.3 Core Requirements

Requirements are grouped as functional requirements (FR), non-functional requirements (NFR) and governance requirements (GR).

<!-- TABLE:10 -->

## 4.4 Priority User Stories

User stories express requirements from the user’s point of view and carry measurable acceptance criteria. They are the basis of the pilot backlogs and of the acceptance tests at gates G2 and G3.

<!-- TABLE:11 -->

## 4.5 Design Principles Applied

The White Paper’s principles (human-centred AI, transparency, responsibility, inclusiveness, evidence-based decision support and collaboration) become five engineering rules in this Blueprint:

1. **No citation, no claim.** A generated statement that cannot be traced to a retrieved passage is not shown (FR-02).
2. **Bangla is a first-class language.** Every feature is specified, tested and evaluated in Bangla and English, with a measured parity target (NFR-01).
3. **Open by default.** Code, benchmarks, evaluation reports and non-sensitive data are published with persistent identifiers; closed components need a written justification (NFR-06, NFR-07).
4. **Smallest data that works.** Each pilot uses the least sensitive data class that meets its purpose (GR-03).
5. **Gate before scale.** Nothing moves from experiment to advisory use, or from advisory to operational use, without passing a documented gate (GR-02).

## 4.6 Requirements Management

Requirements are kept in the repository as versioned text, alongside the code. A change to a requirement is proposed through an issue, reviewed by the Technical Architecture Board (and by the ERRC where it affects a governance requirement), and recorded in the change log. The traceability matrix in Annex A is regenerated at every release so that each requirement can be followed to the components, modules and tests that satisfy it.

\newpage
