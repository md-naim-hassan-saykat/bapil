# BAPIL Reference Implementation

Reference implementation of the core components described in the **BAPIL Technical Blueprint (Version 1.0)**, Chapter 11.

It is a small, tested, **dependency-free** Python package (standard library only, Python 3.10 or newer), so it installs and runs offline, including in air-gapped environments. It is a research and teaching artefact (maturity class **R**), not a production system.

## What it demonstrates

| Module | Blueprint requirement | What it does |
|---|---|---|
| `bapil.text` | FR-01, NFR-01 | Bangla Unicode normalisation (nukta letters, khanda ta, zero-width characters), Bangla/ASCII digit folding, light Bangla suffix stripping, bilingual glossary expansion |
| `bapil.corpus` | FR-03 | Splits Markdown documents into cited passages with heading paths, language and SHA-256 provenance |
| `bapil.search` | FR-01 | BM25 ranking with weighted cross-lingual query expansion |
| `bapil.answer` | FR-02, NFR-08 | Extractive answers where every sentence cites its passage; abstains when evidence is weak; citation verification for any future generator |
| `bapil.risk` | FR-07, GR-02, GR-06 | Risk tiers T0 to T3 from the Annex B questionnaire, with reasons, controls and approvers |
| `bapil.registry` | FR-06, FR-09 | AI system register validation and bilingual transparency-register export |
| `bapil.evaluate` | FR-08 | Recall@k, MRR@10, nDCG@10 and abstention rate on a question set |
| `bapil.audit` | GR-04 | Hash-chained, tamper-evident JSONL audit log with verification |
| `bapil.api` | FR-10 | JSON HTTP API: `/v1/health`, `/v1/search`, `/v1/answer`, `/v1/risk/assess` |
| `bapil.cli` | all | Command line interface |

## Quick start

```bash
cd implementation
pip install -e .            # no third-party dependencies
# or, without installing:  export PYTHONPATH=src

python -m bapil.cli index --corpus ../reports ../blueprint/BAPIL_*.md
python -m bapil.cli search "data protection impact assessment"
python -m bapil.cli ask "বাংলা নীতি ফাউন্ডেশন মডেল কেন প্রয়োজন?"
python -m bapil.cli ask "Who won the 2022 FIFA World Cup?"          # abstains: out of scope
python -m bapil.cli assess examples/risk/risk_p1_policy_search.json  # T2 Limited (Annex B.4)
python -m bapil.cli evaluate benchmarks/demo_questions.json --json build/eval_report.json
python -m bapil.cli register examples/registry --export build/transparency_register.md
python -m bapil.cli verify-log build/audit.jsonl
python -m bapil.cli serve --port 8080   # then open http://127.0.0.1:8080/v1/health
```

## Tests

```bash
python -m unittest discover -s tests
```

The tests cover Bangla normalisation, bilingual and cross-lingual retrieval, citation integrity, abstention, every risk-tier rule, register validation (and JSON Schema validation when `jsonschema` is installed), evaluation metrics, audit-log tamper detection, the HTTP API and the CLI.

## Layout

```text
src/bapil/          package source
src/bapil/data/     bilingual glossary (CC BY 4.0)
schemas/            JSON Schemas: policy document, AI system record, risk questionnaire
examples/registry/  AI system records for pilots P1 to P6
examples/risk/      risk questionnaires, including the Annex B worked example
benchmarks/         demonstration question set (bilingual, with unanswerable questions)
tests/              unit tests and fixtures
```

## Limits

* The demonstration corpus is BAPIL's own publications; it contains no third-party or personal data.
* BM25 and extractive answering are deliberately simple and transparent. The production design (Blueprint Chapters 4 and 6) adds dense multilingual retrieval, OCR, access control and optional, citation-verified generation behind the same interfaces.
* Demonstration metrics show that the evaluation harness works; they are not evidence of performance on the national corpus, which will be measured on the BanglaPolicyQA benchmark.

## Licence

Code: MIT (see the repository `LICENSE`). Glossary, examples and benchmark data: CC BY 4.0.
