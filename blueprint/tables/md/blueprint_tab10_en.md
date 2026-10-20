**Table 10.** Core requirements (functional, non-functional and governance)

| ID | Requirement | Priority |
|---------|----------------------------------------------|---------|
| FR-01 | Bilingual (Bangla and English) search over policy documents, robust to spelling variants and to Bangla or ASCII digits | Must |
| FR-02 | Answers grounded only in retrieved sources, with passage-level citations; the system abstains when evidence is insufficient | Must |
| FR-03 | Ingestion records provenance for every document: source URL, publisher, date, checksum and reuse terms | Must |
| FR-04 | Indicator and budget dashboards with downloadable data and methods notes | Should |
| FR-05 | Aggregate analysis of consultation feedback (topics, sentiment) with no profiling of individuals | Should |
| FR-06 | Register of all AI systems with owner, purpose, risk tier, model card and status | Must |
| FR-07 | Risk-tier assessment applied before any build and at every lifecycle gate | Must |
| FR-08 | Evaluation harness with versioned benchmarks and reproducible reports | Must |
| FR-09 | Public transparency register generated from the AI system register | Should |
| FR-10 | Documented, versioned API for programmatic access | Should |
| NFR-01 | Language parity: Bangla quality within 5 points of English on core metrics | Must |
| NFR-02 | Data residency: P1 to P3 data hosted in Bangladesh in accredited facilities | Must |
| NFR-03 | Security by design aligned with NIST CSF 2.0 and zero-trust access | Must |
| NFR-04 | Availability of 99% for pilots (working hours) and 99.5% at scale | Should |
| NFR-05 | Accessibility to WCAG 2.2 level AA; usable on mobile and low-bandwidth connections | Must |
| NFR-06 | Open standards and open source by default; no single-vendor lock-in | Must |
| NFR-07 | Reproducibility: versioned code, data snapshots and evaluation reports archived with DOIs | Must |
| NFR-08 | Explainability: every output shows its sources, confidence and known limitations | Must |
| NFR-09 | Performance: search p95 at most 3 s; answers p95 at most 10 s | Should |
| NFR-10 | Cost transparency: cost per 1,000 queries reported each quarter | Could |
| GR-01 | Human review of consequential outputs; AI is never the final decision-maker | Must |
| GR-02 | No build without tier screening (G0) and no pilot without gate approval (G2) | Must |
| GR-03 | Data minimisation: public data first; DPIA before any P2 or P3 processing | Must |
| GR-04 | Tamper-evident audit logs of queries, sources consulted and outputs | Must |
| GR-05 | Incident reporting and response within defined time limits | Must |
| GR-06 | Prohibited uses (tier T0) excluded by the BAPIL charter | Must |

*Note.* Priority follows the MoSCoW convention (Must, Should, Could). Requirement IDs are traced to components, code modules and tests in Annex A.
