**Table 21.** Initial architecture decision records

| ADR | Decision | Rationale | Alternatives considered |
|---------|----------------------|-----------------------------|------------------------|
| 001 | Modular services with open interfaces | Components can be replaced without rewriting others; avoids lock-in | Monolithic application; single vendor suite |
| 002 | Retrieval before generation | Answers stay traceable to official text; reduces invented content | Pure generative assistant; fine-tuned model without retrieval |
| 003 | Open-weight models hosted in Bangladesh | Data residency; control over versions; no data sent abroad | Commercial API models for all data classes |
| 004 | Hybrid lexical and dense retrieval | Lexical search is transparent and strong on exact terms; dense search handles paraphrase | Dense only; lexical only |
| 005 | Append-only, hash-chained audit log | Independent verification of what the system did | Ordinary application logs |
| 006 | Containers and infrastructure as code | Reproducible, auditable environments | Manually configured servers |
| 007 | Accessibility and low bandwidth first | Reach users outside Dhaka and on mobile | Desktop-first interface |
| 008 | Public data first (P0) | Value without privacy risk while governance matures | Start with administrative records |
