**Table 37.** From reference implementation to production

| Capability | Reference implementation | Production replacement | When |
|-------------------|----------------------|-----------------------------|-------------|
| Corpus storage | JSON file | PostgreSQL catalogue and S3-compatible object store | Months 1 to 6 |
| Ingestion | Markdown loader | PDF and HTML extraction with Bangla OCR and quality scoring | Months 1 to 9 |
| Lexical search | In-memory BM25 | OpenSearch or PostgreSQL full-text search | Months 4 to 9 |
| Dense retrieval | Not included | Multilingual embeddings in a vector index; hybrid ranking | Months 6 to 12 |
| Transliteration of romanised Bangla | Not included | Transliteration candidates in query expansion | Months 12 to 18 |
| Answers | Extractive with citations | Extractive first; optional open-weight LLM rephrasing behind citation verification | After G2 evidence |
| API | Standard-library HTTP server | API gateway with authentication, quotas and versioning | Months 6 to 9 |
| Identity | None | Single sign-on with MFA and roles | Before G2 (pilot start, month 9) |
| Audit log | Hash-chained JSONL file | Append-only store with replication and external anchoring | Before G2 |
| Register and risk tool | CLI and JSON files | Governance workbench web application | Months 9 to 15 |
