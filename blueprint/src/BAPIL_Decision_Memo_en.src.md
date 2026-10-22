---
lang: en
---

# Decision Memo: A 12-Month Pilot of an AI Policy-Intelligence Capability for Bangladesh

**To:** Ministry of Posts, Telecommunications and Information Technology (ICT Division), and the Planning Commission, Finance Division, Legislative and Parliamentary Affairs Division, Bangladesh Bureau of Statistics, a2i and the National Data Management Authority  
**From:** Md Naim Hassan Saykat, author of the BAPIL Technical Blueprint · **Date:** {{DATE}}  
**Basis:** Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint, Version 1.0 ({{DOI_SHORT}}). This memo is a separate document and is not part of the Blueprint.

**Status.** Independent research proposal; not an official government document. No authority has taken any decision on BAPIL. No body described here has been constituted, no host institution has been selected and no funding has been requested or approved.

**Purpose.** To request six decisions that would allow a small, safe and open pilot of an AI capability that helps officials find and cite official evidence in Bangla and English.

**Why now.** (1) The government has announced that drafting of a national AI policy will begin in the fourth quarter of 2026 with a joint team [91], following the draft National AI Policy 2026-2030 consulted on in January 2026 and a revised draft dated February 2026 [88, 125]; a tested, openly licensed blueprint can inform that process. (2) As reported, the Personal Data Protection Act, 2026 and the National Data Management Act, 2026 now frame the use of public-sector data [85, 86]; which provisions are in force is still to be confirmed. (3) Laws, gazettes, budgets and plans are scattered across websites and formats, often as scanned Bangla PDFs, and there is no open Bangla benchmark for policy search.

**Proposal.** A university-anchored BAPIL lab under an MoU with the ICT Division, with a multi-stakeholder Steering Board and an independent Ethics and Risk Review Committee (ERRC) whose veto binds the host only as far as the host’s statutes and the host agreement allow. Year 1 would deliver: **P1**, a bilingual policy search tool designed to cite official sources or abstain, piloted with 30 or more analysts in two to three agencies; **P2**, five years of budget allocations as open data; version 0 of the open **BanglaPolicyQA** benchmark (500 questions); training for 100 officials; and a public transparency register. A small reference implementation (version 0.1.0, a tested research prototype, not a deployed system) is to be issued in repository release {{RELEASE}}.

**Safeguards (BAPIL’s own rules, stricter than the law requires).** Officially published data first; no personal data without consent, a DPIA and ERRC approval; no sensitive personal data. Advice, not decisions: a person reviews every output, and no system decides about individuals. No surveillance, social scoring or profiling of opinions. Risk tiers and lifecycle gates; hosting in Bangladesh; open publication of code and evaluations.

**Decisions requested** (identical to Table 57 of the Blueprint).

| No. | Decision | Responsible authority | Timing |
|----|------------------------------------------------|----------------------|------------|
| D1 | Accept the Blueprint as a technical input to the national AI policy drafting process | ICT Division | Q4 2026 |
| D2 | Approve a 12-month Phase 1 pilot, name a government focal point, agree an MoU with a host institution, and commit or identify Year 1 funding (about Tk 4.7 crore) | ICT Division and host institution | Within 90 days |
| D3 | Authorise structured bulk access to already-public document collections and nominate data custodians | Legislative and Parliamentary Affairs Division, Finance Division, Planning Commission, BBS, a2i | Within 120 days |
| D4 | Nominate Steering Board members, and agree that ERRC members are selected through an open call by an independent nominations panel | ICT Division and host institution; independent panel | Within 90 days |
| D5 | Commission the feasibility and costing study that sets the Phase 2 budget | ICT Division or a development partner | By month 6 |
| D6 | Confirm guardrails: no deployment beyond class A without a G4 decision, and no use in prohibited categories | Steering Board | At charter adoption |

**Decisions already made.** None by any authority. The institutional model, the public-data-first rule and the staged approach to Bangla model development are the author’s recommendations.

**Approvals and agreements required before month 1.** A host institution selected through an open call; the MoU with the ICT Division; a host agreement with a separate cost centre; Year 1 funding committed. Month 1 is the first month in which all of these are in place. January 2027 is possible only if funding is already available; through the development budget, the second half of 2027 is more realistic.

**Resources requested.** About 9 full-time equivalents in Year 1, rising to 19 by Year 3; two to three servers and two GPU inference servers (more in Year 2 for a recovery site). Indicative budget: about Tk 20.4 crore over 36 months (Tk 4.7 crore in Year 1), with low and high scenarios of about Tk 17.9 and Tk 25.3 crore. Including the known omitted costs and a 10% contingency gives an adjusted base case of about Tk 22.2 crore. These are planning estimates, not approved funding, and the month-6 costing study would refine them.

**Evidence required before implementation.** (1) Independent legal review of which provisions of the 2026 data-protection, data-management and cyber-security laws are in force (Blueprint unresolved items U1 to U3). (2) Confirmation that the selected host can accept a binding ERRC veto (U15). (3) Costing of the items not yet in the base case (U16). (4) Written reuse terms or bulk access for public documents (D3).

**Proposed targets for month 12** (targets, not results). P1 passes its gate with 30 or more active users, Recall@10 of at least 0.85 and citation precision of at least 0.95 on the benchmark’s private test set; 500 benchmark questions released; five fiscal years of budget allocations published as open data; 100 officials trained; every pilot listed in the transparency register with a model card; a public Year 1 report, including what did not work.

**Key risks and mitigations.** *Data access delays:* start with documents already online. *Wrong answers:* extractive answers with mandatory citations, abstention and human review. *Mission creep:* prohibited uses written into the charter and an independent veto. *Funding delay:* the start date follows the funding route; no work that commits public funds begins before D2. *Political change:* university host and alignment with the national AI policy process.

**Long-term path (Blueprint Chapter 16).** Pilots and governance proven with public data (2027 to 2028); tools adopted by agencies and aligned with the next national AI policy cycle (2029 to 2030); a national policy-intelligence network on shared standards (2031 to 2035); evidence services embedded in policy cycles by 2041, with charter renewal only if a 2041 review confirms public value.

**Links.** Blueprint: {{DOI_LINK}} · White Paper: <https://doi.org/10.5281/zenodo.21363967> · Repository: <https://github.com/md-naim-hassan-saykat/bapil>

*CC BY 4.0.*

{{REFERENCES}}
