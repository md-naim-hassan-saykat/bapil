**Table 24.** Document metadata fields (policy_document schema)

| Field | Description | Required | Example |
|----------------|-----------------------------------|---------|------------------------|
| id | Persistent identifier inside the corpus | Yes | bd-act-2009-20 |
| title | Title in Bangla and English where available | Yes | Right to Information Act, 2009 |
| publisher | Organisation that published the document | Yes | Legislative and Parliamentary Affairs Division |
| issuing_body | Body that issued the instrument | No | Parliament |
| document_type | Act, ordinance, rule, gazette, budget, plan, statistics, parliamentary paper, policy, report | Yes | act |
| date_issued | Date of issue | Yes | 2009-04-06 |
| version | Version or amendment state | No | as amended to 2026 |
| language | Languages of the text | Yes | bn, en |
| source_url | Where the original was obtained | Yes | http://bdlaws.minlaw.gov.bd/... |
| retrieved | Date retrieved | Yes | 2027-02-01 |
| reuse_terms | Licence or reuse conditions | No | Government publication; terms confirmed |
| data_class | DC0, DC1 or DC2 | Yes | DC0 |
| sha256 | Checksum of the original file | Yes | 64 hexadecimal characters |
| extraction | Method (born digital or OCR), quality score, tool | Yes | ocr, 0.93, tesseract 5 |
| supersedes | Identifier of an earlier version | No | bd-act-2009-20-v1 |

*Note.* Examples are illustrative. The machine-readable schema is implementation/schemas/policy_document.schema.json.
