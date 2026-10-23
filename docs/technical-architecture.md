# Technical architecture

A short guide to the proposed BAPIL architecture and to what exists in code today. The authoritative description is the Technical Blueprint, Chapters 7 to 11 (Figure 4, Tables 19 to 33); this page does not replace it.

## 1. Design principles

* **Public data first.** The first corpus is documents the state has already published (data class DC0). Higher data classes need agreements, a DPIA and ERRC approval; class P3 is never used.
* **Retrieve, cite or abstain.** Answers are built from retrieved passages, every sentence carries a citation to an official source, and the service declines to answer when the evidence is weak. This is a design rule and an acceptance criterion measured by citation precision (target at least 0.95), not a guarantee.
* **Advice, not decisions.** No system decides about individuals; a person reviews every output.
* **Open and modular.** Open-source components where possible, hosting in Bangladesh for data above class DC0, open publication of code and evaluations.
* **Gate before scale.** Nothing moves from research to advisory or operational use without passing a documented lifecycle gate (G0 to G5).

## 2. Components (Blueprint Table 19)

| ID | Component | In the reference implementation |
|---|---|---|
| C1 | Source connectors | Planned |
| C2 | Ingestion and normalisation (PDF and HTML text, Bangla OCR, Unicode normalisation, chunking) | `bapil.text`, `bapil.corpus` (Markdown only; no OCR) |
| C3 | Document store and catalogue | JSON corpus with SHA-256 checksums |
| C4 | Search index (BM25, later hybrid with dense vectors) | `bapil.search` (bilingual BM25) |
| C5 | Answer service (retrieve, cite, abstain; optional generation with citation verification) | `bapil.answer` (extractive, cited) |
| C6 | Analytics engine | Planned |
| C7 | Portal and dashboards | Planned |
| C8 | API gateway | `bapil.api` (standard library HTTP server) |
| C9 | Identity and access | Planned |
| C10 | Audit and observability | `bapil.audit` (hash-chained JSONL log) |
| C11 | Model registry and evaluation | `bapil.evaluate` |
| C12 | Governance workbench | `bapil.risk`, `bapil.registry` |

Technologies named in the Blueprint are candidates; the Technical Architecture Board makes final choices against the requirements.

## 3. Retrieval and language technology

Stage 0 starts with lexical and metadata search (also the transparent fallback), then adds multilingual dense retrieval and reranking only if they improve Recall@10 or nDCG@10 by more than the confidence interval with no safety metric worse. Bangla normalisation is applied for matching while the original text is kept for display and citation. Generative features, if enabled, must verify every generated sentence against its cited passage and label generated text. Whether a Bangla domain-adapted model is worth building is decided in Year 3 on evidence (Section 9.7); existing open models with Bangla-aware retrieval, OCR, embeddings and reranking are evaluated first.

## 4. Security, hosting and logging

Security follows the six NIST CSF 2.0 functions; requirements cover hosting in Bangladesh for data above DC0 (NFR-02), availability of at least 99% once the recovery site exists in Year 2 (NFR-04), tamper-evident audit logs, role-based access with multi-factor authentication, software bills of materials and pinned dependencies (Chapter 10).

## 5. The reference implementation

`implementation/` holds `bapil` version 0.1.0, a small research prototype in standard-library Python. It is **not** a deployed system and has not been used by any agency. Its 49 unit tests pass when run locally; two GitHub Actions workflows (tests on Python 3.10 to 3.13, and a full rebuild of the Blueprint) are included but have not yet run on GitHub, because the branch has not been pushed. See [`implementation/README.md`](../implementation/README.md) and Blueprint Chapter 11 and Annex M.
