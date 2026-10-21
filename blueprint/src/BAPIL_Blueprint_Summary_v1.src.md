---
lang: en
---

# Bangladesh AI Policy & Innovation Lab (BAPIL)

## Blueprint Summary

### Summary of the BAPIL Technical Blueprint (Version 1.0)

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

*This summary presents the main design choices, safeguards, delivery plan, strategic roadmap to 2041 and decisions set out in the BAPIL Technical Blueprint (five parts, 21 chapters, 21 annexes). Figure and table numbers follow the full Blueprint. The Blueprint, this summary and the one-page Decision Memo are independent research documents and do not represent any official position. BAPIL is a proposal: no institution has been created and no funding has been approved.*

\newpage

# 1. What BAPIL Is, and Why Now

The Bangladesh AI Policy & Innovation Lab (BAPIL) is a proposed independent research and policy-intelligence platform that helps Bangladesh use artificial intelligence for evidence-based policymaking, responsible AI governance, Bangla-language technology and public-sector innovation. The White Paper (Version 1.0) set out the vision; the Technical Blueprint turns it into a buildable plan.

The timing is favourable. As reported, Bangladesh converted its 2025 data ordinances into the Personal Data Protection Act, 2026 and the National Data Management Act, 2026 in April 2026 (which provisions are in force is still to be confirmed), revised its cyber-security law, released a draft National AI Policy 2026-2030 for consultation in January 2026, and announced that drafting of a national AI policy would begin in the fourth quarter of 2026 [85, 86, 87, 88, 91]. A concrete, open blueprint with working code can be a technical input to that process.

<!-- FIGURE:01 -->

# 2. What the Blueprint Specifies

1. **26 requirements** (functional, non-functional and governance), each traced to components, code and tests.
2. **An institution:** a university-anchored lab with a government MoU, a multi-stakeholder Steering Board, an independent Ethics and Risk Review Committee (ERRC) with a binding veto, and a Technical Architecture Board.
3. **A reference architecture** of twelve open, replaceable components.
4. **Data rules:** four data classes, a public-data-first policy and an inventory of official sources.
5. **A trustworthy AI design:** bilingual search and answers in which every sentence cites an official source, with abstention when evidence is weak.
6. **An open benchmark,** BanglaPolicyQA, and a staged, evidence-gated path to a Bangla Policy Foundation Model.
7. **Six pilots** with users, data, risk tier, scope and exit criteria.
8. **Security and hosting** in Bangladesh, with controls for AI-specific threats.
9. **An assurance system:** risk tiers T0 to T3, lifecycle gates G0 to G5, model cards and a public transparency register.
10. **A small, tested reference implementation** (a research prototype, not a production system) released on GitHub with the Blueprint, a 36-month delivery plan, staffing and training, financing and procurement clauses, a logical framework, KPIs, a risk register and a research agenda.
11. **A strategic roadmap for 2026 to 2041 and beyond,** with five horizons, indicative targets, scenarios and fixed review points.
12. **Six decisions** for the authorities.
13. **Evidence and readiness annexes:** the evidence status of every key claim, budget reconciliation and scenarios, an evaluation protocol with sample sizes, the status and limits of each governance body, the preconditions for starting, and risk monitoring.

\newpage

# 3. Institution and Governance

<!-- FIGURE:03 -->

A hybrid model (Option C in the Blueprint) combines academic independence with a direct channel to government. Successful tools are transferred to the responsible agency through a documented adoption decision; BAPIL never operates production government systems.

# 4. Architecture and AI Design

<!-- FIGURE:04 -->

The core service is a **bilingual, citation-grounded policy search and answer system** over officially published documents: laws, gazettes, budgets, plans and statistics. Text is normalised for Bangla, queries are expanded across Bangla and English, passages are retrieved and checked, and an answer is given only when evidence is sufficient. Every query, source and output is written to a tamper-evident audit log. Models are open-weight and, for any non-public data, hosted in Bangladesh.

\newpage

# 5. Pilot Portfolio

| Pilot | Data | Tier | First-year result |
|---|---|---|---|
| **P1** Bangladesh Policy Search Engine | Public documents | T1 or T2 | Pilot with 30 or more users in two to three agencies |
| **P2** Budget Intelligence Dashboard | Published budget documents | T1 | Five fiscal years of allocations as open data |
| **P3** Citizen Feedback Analyser | Consented, de-identified submissions | T2 | Aggregate summaries of one consultation after a DPIA |
| **P4** Bangla Policy Foundation Model, Stages 0 and 1 | Governed public corpus | T1 | BanglaPolicyQA benchmark v0 and baselines |
| **P5** National AI Readiness Observatory | Public indicators | T1 | Indicator framework and first report |
| **P6** Information-integrity research | Public research datasets | T2 | Methods review; no monitoring of individuals |

# 6. Safeguards

* **Public data first;** personal data only with consent, a DPIA and ERRC approval; sensitive personal data never.
* **Advice, not decisions;** a person reviews every output in advisory use, and no system decides about individuals.
* **No surveillance;** social scoring, mass biometric surveillance and profiling of political or religious opinions are prohibited by charter.
* **Risk tiers and gates** decide how much control a system needs and when it may move forward.
* **Openness:** code, benchmarks, evaluation reports and the transparency register are published.

<!-- TABLE:39 -->

\newpage

# 7. Delivery Plan (36 Months)

<!-- FIGURE:12 -->

* **Month 3:** MoU signed; Steering Board, ERRC and TAB in place; charter adopted.
* **Month 6:** feasibility and costing study; data access confirmed; benchmark protocol agreed.
* **Month 12:** P1 pilot running with 30 or more users; P2 open budget dataset published; 100 officials trained.
* **Month 24:** adoption decisions on P1 and P2 with host agencies; first AI readiness report; 300 officials trained.
* **Month 36:** final independent evaluation; sustainability plan; Blueprint 2.0.

\newpage

# 8. Strategic Roadmap 2026-2041 and Beyond

<!-- FIGURE:13 -->

The 36-month plan is the first step of a longer strategy that connects BAPIL's pilots to the national AI policy cycle and to the Perspective Plan 2041 and ICT Masterplan 2041 [29, 30, 88].

* **H0 Foundation (Q4 2026):** publish the Blueprint and code; brief the authorities; offer input to national AI policy drafting; select a host institution.
* **H1 Short term (2027 to 2028):** prove value with public data; P1 and P2 pass their pilot gates; about 300 officials trained; mid-term evaluation.
* **H2 Medium term (2029 to 2030):** agencies adopt successful tools; benchmark v1; Blueprint 2.0; contribution to the post-2030 national AI policy; about 1,000 officials trained.
* **H3 Long term (2031 to 2035):** a national policy-intelligence network on shared standards; common assurance methods across government; regional training hubs; decision on institutional form.
* **H4 Vision (2036 to 2041):** evidence services embedded in policy cycles; open Bangla language resources across domains; regional and South-South cooperation; independent review in 2041.
* **Beyond 2041:** the charter is renewed only if the 2041 review confirms continuing public value; otherwise BAPIL closes or merges, with open archives preserved.

Targets are indicative and revised at fixed reviews (2027, 2028, 2029, 2030, 2035 and 2041) and whenever a major event occurs. In every scenario, the core (governed corpus, cited search, benchmark and governance) is protected, and safeguards never weaken as BAPIL grows.

<!-- TABLE:45 -->

\newpage

# 9. People, Resources and Financing

The core team grows from about 9 to 19 full-time equivalents over three years. Pilot computing needs are modest (two to three servers and one or two inference GPUs), with any model adaptation using shared national compute. An indicative budget built from stated assumptions comes to about Tk 20.4 crore over 36 months (Tk 4.7, 7.5 and 8.2 crore in Years 1 to 3, about USD 1.65 million), including 8% annual escalation, host overheads and a 5% contingency, with people at about half of the total. Low and high scenarios give about Tk 17.9 and 25.3 crore. It is a planning estimate, not approved funding; the feasibility and costing study in month 6 confirms or replaces each assumption. Funding is diversified, with a growing share of core public funding and agency service agreements over time; no single non-government funder provides more than 30% of the budget. Model procurement clauses protect data, guarantee the right to evaluate and prevent lock-in.

# 10. Reference Implementation and Research

The repository contains a tested, dependency-free Python implementation of the core ideas: Bangla normalisation, bilingual BM25 search, cited extractive answers with abstention, risk-tier assessment, an AI system register with transparency export, evaluation metrics and a hash-chained audit log, with a command line and a small JSON API. Continuous-integration workflows are configured to run the tests and rebuild the published documents from source. It has not been deployed or tested with users; the evaluation thresholds in the Blueprint are proposed targets, with a measurement protocol, not results. A research agenda of six questions, from Bangla retrieval to institutional design, leads to open datasets, evaluation reports and peer-reviewed publications, starting with a journal manuscript on the framework planned for 2027.

\newpage

# 11. Decisions Requested

<!-- TABLE:57 -->

# Resources

**Technical Blueprint DOI:** {{DOI_LINK}}  
**White Paper DOI:** <https://doi.org/10.5281/zenodo.21363967>  
**Executive Summary DOI:** <https://doi.org/10.5281/zenodo.21441172>  
**GitHub Repository:** <https://github.com/md-naim-hassan-saykat/bapil>

{{REFERENCES}}

---

© 2026 Md Naim Hassan Saykat. Licensed under CC BY 4.0.
