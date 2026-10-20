**Table 28.** Evaluation metrics and proposed pilot exit thresholds

| Dimension | Metric | Definition | Proposed threshold |
|---------------|-----------------------|--------------------------------|----------------|
| Retrieval | Recall@10 | Share of questions whose gold passage appears in the top 10 results | at least 0.85 |
| Retrieval | MRR@10 | Mean reciprocal rank of the first relevant passage | at least 0.70 |
| Retrieval | nDCG@10 | Rank-weighted relevance against graded judgements | at least 0.75 |
| Grounding | Citation precision | Share of cited passages that support the claim they are attached to | at least 0.95 |
| Grounding | Unsupported-claim rate | Share of answer sentences with no supporting citation | at most 2% |
| Abstention | Correct abstention | Share of unanswerable questions on which the system declines to answer | at least 0.90 |
| Language parity | Bangla and English gap | Difference in Recall@10 between Bangla and English question sets | at most 5 points |
| Robustness | Variant spelling recall | Recall@10 on romanised and variant-spelling Bangla queries | at least 0.75 |
| Safety | Prompt-injection success | Share of red-team injection attempts that change system behaviour | at most 5% |
| Human evaluation | Usefulness and fluency | Mean rating by pilot users and Bangla editors on a 5-point scale | at least 4.0 |
| Efficiency | Latency p95 | 95th-percentile response time for search and for answers | 3 s and 10 s |

*Note.* Thresholds are proposals for Gate G2 and G3 decisions; the ERRC and TAB may tighten them for specific uses.
