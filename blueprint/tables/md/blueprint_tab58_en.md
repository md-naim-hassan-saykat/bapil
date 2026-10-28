**Table 58.** Requirements traceability matrix

| Requirement | Summary | Component | Code module | Verification |
|----------|------------------------------|----------|-------------------|----------------|
| FR-01 | Bilingual search | C2, C4 | bapil.text, bapil.search | test_text, test_search |
| FR-02 | Cited answers and abstention | C5 | bapil.answer | test_answer |
| FR-03 | Provenance at ingestion | C2, C3 | bapil.corpus | test_corpus |
| FR-04 | Dashboards | C6, C7 | Specified only | Pilot P2 acceptance |
| FR-05 | Aggregate feedback analysis | C6 | Specified only | Pilot P3 DPIA and acceptance |
| FR-06 | AI system register | C12 | bapil.registry | test_registry |
| FR-07 | Risk-tier assessment | C12 | bapil.risk | test_risk |
| FR-08 | Evaluation harness | C11 | bapil.evaluate | test_evaluate |
| FR-09 | Transparency register | C12 | bapil.registry (export) | test_registry |
| FR-10 | Versioned API | C8 | bapil.api | test_api |
| NFR-01 | Language parity | C2, C4 | bapil.text glossary and normaliser | test_text; benchmark |
| NFR-07 | Reproducibility | All | CI workflow; no external dependencies | GitHub Actions |
| NFR-08 | Explainability | C5 | bapil.answer (sources and scores) | test_answer |
| GR-02 | Gate before build | C12 | bapil.risk | test_risk |
| GR-04 | Tamper-evident logs | C10 | bapil.audit | test_audit |
| GR-06 | Prohibited uses | C12 | bapil.risk (T0 screen) | test_risk |
