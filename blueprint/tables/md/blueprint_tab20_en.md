**Table 20.** API specification (version 1)

| Endpoint | Method | Parameters | Response | Errors |
|-------------------|-------|--------------------|--------------------------|--------------|
| /v1/health | GET | None | status, version, corpus_version, documents, passages | None |
| /v1/search | GET | q (1 to 500 characters); k (1 to 50, default 10) | query, corpus_version, results: pid, doc_id, heading, lang, score, matched_terms, text, provenance | 400 missing or invalid parameter |
| /v1/answer | GET | q (1 to 500 characters) | abstained; confidence; evidence (top_score, coverage); answer sentences with citation; sources; corpus_version | 400 missing parameter |
| /v1/risk/assess | POST | JSON questionnaire (Annex B schema) | system_id, tier, tier_name, total, reasons, controls, approver | 400 invalid questionnaire; 400 body over 64 KB |
| All endpoints |  |  | JSON in UTF-8; every request logged in the audit chain | 404 unknown path |
