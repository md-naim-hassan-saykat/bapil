# Evaluation methodology

This page summarises how BAPIL proposes to measure its systems and what has actually been measured so far. The authoritative text is the Technical Blueprint: Table 28 (metrics and proposed thresholds), Section 9.4 and Annex R with Table 63 (evaluation protocol and release gates), and Annex K (annotation guidelines).

## 1. Status

| Item | Status (October 2026) |
|---|---|
| BanglaPolicyQA benchmark | **Not built.** No benchmark question has been written for it. Version 0 (500 answerable and 200 out-of-scope questions) is planned for months 6 to 9 of the delivery plan (Milestone MS3) |
| Pilot evaluations (P1 to P6) | **Not started.** No pilot exists |
| Thresholds such as Recall@10 at least 0.85 and citation precision at least 0.95 | **Proposed targets**, not results |
| Demonstration evaluation | **Development results only** (Section 3 below), measured locally by the build |
| Independent evaluation | Planned at the mid-term (month 18) and final evaluations, and before Gate G4 |

## 2. Proposed metrics and how they will be computed

| Metric | Definition | Computed by | Proposed threshold |
|---|---|---|---|
| Recall@10 | Mean over answerable test questions of a hit (1 if any gold passage is among the top 10 results, else 0) | Automatic scoring script (`bapil.evaluate`) | at least 0.85 |
| MRR@10, nDCG@10 | Mean reciprocal rank of the first relevant passage; rank-weighted relevance against graded judgements | Automatic | at least 0.70; at least 0.75 |
| Citation precision | Share of sampled answer sentences whose cited passage, read on its own, fully supports the sentence (only "supported" counts) | Two trained annotators blind to the system version; a third adjudicates; Cohen’s kappa reported (target 0.70) | at least 0.95 |
| Unsupported-claim rate | Share of sampled sentences supported by no retrieved passage | Same annotators | at most 2% |
| Correct abstention; answer coverage | Declines on out-of-scope questions; answers on answerable questions | Automatic | at least 0.90; at least 0.80 |
| Language parity | Recall@10 (English) minus Recall@10 (Bangla), with a bootstrap interval | Automatic | reported in v0; at most 5 points from v1 |
| Robustness | Recall@10 on Bangla variant spellings (gated), romanised, OCR-derived and code-mixed queries (reported in v0) | Automatic | at least 0.75 for Bangla-script variants |
| Usefulness | Mean rating on a 5-point scale | At least 30 pilot users; at least 100 answers rated by Bangla editors | at least 4.0 |

Every metric is reported with a 95% interval, by language and by document type; differences smaller than the interval are not treated as improvements. If any safety measure misses its threshold, the system fails the gate whatever its other results (Annex R).

## 3. How benchmark questions will be created and checked

1. Domain experts write questions from real analyst tasks, in natural Bangla or English, including some romanised Bangla and variant spellings, balanced across languages, document types, issuing bodies and periods; out-of-scope questions are written as a separate set (Annex K).
2. A second annotator, who did not write the question, finds the passage or passages that answer it and records their identifiers.
3. Passages are graded 2 (fully answers), 1 (partly answers) or 0; disagreements are resolved by a third annotator, and agreement rates are published in the benchmark datasheet. Annotators are paid and credited; questions contain no personal data.
4. A random 10% of items is re-annotated in each version; errors are corrected and logged.
5. The split is 40% public development and 60% private test. The private test split is held by the evaluation team and used only for gate decisions.
6. Each gate decision uses a frozen benchmark version, a recorded corpus version and configuration, and archived outputs that an independent evaluator can re-score; re-scored metrics must be within 1 point of those reported.

## 4. What has been measured: the demonstration evaluation

The reference implementation includes a small bilingual question set (`implementation/benchmarks/demo_questions.json`: 24 answerable and 6 out-of-scope questions) that the build runs against a corpus of the White Paper, the Executive Summary, the Blueprint and the Summary (8 documents, about 1,800 passages). The latest build gave Recall@10 of 0.92 (22 of 24) and 6 of 6 correct abstentions; the exact figures are regenerated at every build and printed in Blueprint Section 11.5.

These are development results, not test results: the author wrote both the questions and the documents, gold headings were updated when the Blueprint was renumbered, and one passage was rewritten during development after it caused a false answer. They show that the evaluation harness works end to end; they say nothing about performance on the national corpus. The result changes when the documents change: in October 2026 it moved from 0.92 to 0.88 after corrections to the legal text and back to 0.92 after the review revisions, and the gold labels were deliberately not adjusted.

## 5. Is a dedicated Bangla model needed?

The Blueprint does not commit to building a Bangla foundation model. Its staged approach (Section 9.7) first evaluates existing open models with Bangla-aware retrieval, OCR, normalisation, embeddings and reranking (Stage 0), then allows a costed, limited domain adaptation (Stage 1: one to two ML staff for about twelve months, Tk 0.3 to 0.5 crore, up to USD 20,000 of compute) only if Stage 0 results justify it. Within 36 months at most a domain adaptation is built; Year 3 delivers a documented decision, not a model.
