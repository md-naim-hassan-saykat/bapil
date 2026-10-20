**Table 36.** Reference implementation modules

| Module | What it does | Requirements | Tests |
|-----------------|------------------------------------|----------------|--------------|
| bapil.text | Unicode normalisation for Bangla, digit folding, light Bangla suffix stripping, bilingual glossary expansion | FR-01, NFR-01 | test_text |
| bapil.corpus | Loads Markdown documents, splits them into cited passages, records provenance and SHA-256 checksums | FR-03 | test_corpus |
| bapil.search | BM25 index over passages with language-aware tokenisation and cross-lingual query expansion | FR-01 | test_search |
| bapil.answer | Extractive answers in which every sentence carries a citation; abstains below an evidence threshold | FR-02, NFR-08 | test_answer |
| bapil.risk | Risk-tier questionnaire and scoring rules of Annex B, returning tier, reasons and required controls | FR-07, GR-02, GR-06 | test_risk |
| bapil.registry | AI system register validated against a JSON schema; exports the public transparency register | FR-06, FR-09 | test_registry |
| bapil.evaluate | Recall@k, MRR and nDCG over a versioned question set; JSON report | FR-08 | test_evaluate |
| bapil.audit | Hash-chained, tamper-evident JSONL audit log with verification | GR-04 | test_audit |
| bapil.api | Minimal JSON HTTP API (search, answer, risk) on the Python standard library | FR-10 | test_api |
| bapil.cli | Command line: index, search, ask, assess, evaluate, register, verify-log | All | test_cli |
