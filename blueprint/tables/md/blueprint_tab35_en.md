**Table 35.** Business continuity and disaster recovery targets (pilot phase)

| Service | Recovery point (RPO) | Recovery time (RTO) | Method |
|-------------------------|--------------|--------------|--------------------------|
| Portal and API | Not applicable (stateless) | 8 hours | Redeploy containers from version control |
| Document store and catalogue | 24 hours | 24 hours | Nightly encrypted backups; offline copy weekly |
| Search index | Rebuildable | 48 hours | Rebuild from document store |
| Audit log | 1 hour | 24 hours | Continuous replication; hash-chain verification after restore |
| AI system register and governance records | 24 hours | 24 hours | Versioned in a repository with offline mirror |
