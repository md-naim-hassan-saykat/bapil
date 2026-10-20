**Table 11.** Priority user stories with acceptance criteria

| ID | User story | Acceptance criteria | Req. |
|-------|----------------------------------|----------------------------------|---------|
| US-01 | As a policy analyst, I search in Bangla and get relevant English and Bangla passages | Top 10 results include the gold passage for at least 85% of benchmark questions in both languages | FR-01 |
| US-02 | As an analyst, I get a short answer where every sentence links to its source | 100% of answer sentences carry a passage identifier; citation precision at least 0.95 | FR-02 |
| US-03 | As an analyst, I am told when the system does not know | At least 90% correct abstention on unanswerable questions; reason shown | FR-02 |
| US-04 | As a reviewer, I can see where a document came from and whether it changed | Every passage resolves to source URL, date, checksum; checksum mismatch raises an alert | FR-03 |
| US-05 | As a budget analyst, I download five years of allocations in one file | CSV and Parquet downloads with a methods note; values match source on a 99% sample | FR-04 |
| US-06 | As a consultation owner, I see topics without exposing individuals | Outputs aggregate at least 20 submissions per topic; no names or contact data in outputs | FR-05 |
| US-07 | As the ERRC, I see every AI system, its tier and gate status | Register lists 100% of systems; export generated automatically each release | FR-06, FR-09 |
| US-08 | As an auditor, I can verify that logs were not altered | Hash-chain verification passes; any edit, deletion or reordering is detected | GR-04 |
| US-09 | As a developer, I call a documented API | Versioned endpoints with examples; breaking changes only in a new version | FR-10 |
| US-10 | As a mobile user on a slow connection, I can still search | Search page under 500 KB; usable on 3G; WCAG 2.2 AA checks pass | NFR-05 |
