**Table 28.** Evaluation metrics and proposed pilot exit thresholds

| Dimension | Metric | Definition | Proposed threshold |
|---------------|-----------------------|--------------------------------|----------------|
| Retrieval | Recall@10 | Share of answerable test questions with at least one gold passage in the top 10 results [82] | at least 0.85 |
| Retrieval | MRR@10 | Mean reciprocal rank of the first relevant passage [83] | at least 0.70 |
| Retrieval | nDCG@10 | Rank-weighted relevance against graded judgements [84] | at least 0.75 |
| Grounding | Citation precision | Share of answer sentences whose cited passage fully supports the sentence, judged by two trained annotators | at least 0.95 |
| Grounding | Unsupported-claim rate | Share of answer sentences not supported by any retrieved passage, judged on the same sample | at most 2% |
| Abstention | Correct abstention | Share of out-of-scope questions on which the system declines to answer | at least 0.90 |
| Abstention | Answer coverage | Share of answerable questions that are answered rather than abstained | at least 0.80 |
| Language parity | Bangla and English gap | Difference in Recall@10 between Bangla and English question sets, reported with its confidence interval | at most 5 points |
| Robustness | Variant spelling recall | Recall@10 on variant-spelling Bangla queries in Bangla script (romanised queries reported in v0 and gated from v1) | at least 0.75 |
| Safety | Prompt-injection success | Share of red-team injection attempts that change system behaviour | at most 5% |
| Human evaluation | Usefulness and fluency | Mean rating by pilot users and Bangla editors on a 5-point scale | at least 4.0 |
| Efficiency | Latency p95 | 95th-percentile response time for search and for answers under pilot load | 3 s and 10 s |
| Reliability | Availability | Share of working hours in which search is available during the pilot | at least 99% |

*Note.* All values are proposed targets, not measured results. They are measured on the private test split with the sample sizes, judging procedure and decision rule in Annex R (Table 63); the ERRC and TAB may tighten them for specific uses.
