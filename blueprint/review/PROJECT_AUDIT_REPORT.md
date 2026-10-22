# BAPIL project audit and reconciliation: October 2026

Audit of the whole BAPIL project (publications, sources, data, code, documentation and publication metadata), carried out on 22 October 2026 on branch `blueprint-v1.0` of the local clone. Nothing was pushed, tagged, released or deposited. This report is an internal record and is not part of the publication.

Companion records: [`CROSS_DOCUMENT_RECONCILIATION.md`](CROSS_DOCUMENT_RECONCILIATION.md), [`METADATA_TO_CONFIRM.md`](METADATA_TO_CONFIRM.md), [`MARKDOWN_VALIDATION_REPORT.md`](MARKDOWN_VALIDATION_REPORT.md), the QA report [`../QA_REPORT.md`](../QA_REPORT.md); the inventory is [`docs/document-inventory.md`](../../docs/document-inventory.md), the source-of-truth register [`docs/source-of-truth.md`](../../docs/source-of-truth.md) and the legal verification table [`docs/legal-references.md`](../../docs/legal-references.md).

## 1. Scope and method

1. **Inventory** of the working tree, Git history, branches and tags, and of the public repository (releases page, landing page) and the three Zenodo records.
2. **Source-of-truth register** of canonical values (titles, status, legal statements, targets, budget, versions, DOIs).
3. **Audit** of the English and Bangla Blueprint, the Summary, the earlier Decision Memo draft, the README, CITATION.cff, CHANGELOG, Zenodo files, budget model and code.
4. **External verification:** GitHub (releases, tags), Zenodo (records 21363967, 21441172, 21360565), the national AI policy portal listing, press reports and legal commentary on the 2026 laws (Section 5).
5. **Corrections** in the sources, applied to both languages; **rebuild** of all outputs; **text and visual checks**; **reconciliation** across documents.

Limits: gazetted legal texts and the content of the national AI policy draft version 2.0 could not be read (automated access is blocked); the GitHub API was not available to this session, so the repository was checked through its public web pages and `git ls-remote`; Zenodo’s GitHub-integration setting for the repository cannot be seen from outside.

## 2. Highest-priority risks found

| # | Risk | Why it matters | Treatment |
|---|---|---|---|
| 1 | Publishing GitHub release v1.1.0 while the Zenodo GitHub integration is still switched on | Zenodo would automatically add a new version under the concept DOI that today resolves to the White Paper, with metadata from `CITATION.cff` (type software, licence MIT, version 1.0): a misleading duplicate record | Decision added to the release checklist (section 0) with a recommended option; documented in README and `docs/publication-and-archiving.md` |
| 2 | Legal statements that went beyond their sources | The June 2026 cyber-security amendment was described as an AI-content law although sources disagree; the data-protection framework was said to "require consent" | Corrected in both editions, Summary and tables; new references [123] to [126]; counsel review remains required |
| 3 | Institutional status | The English Section 1.7 said "BAPIL is established", while the Bangla edition and the status table said it is a proposal | Corrected; three further present-tense status sentences made conditional |
| 4 | Licence and affiliation metadata inconsistent across records | The White Paper’s Zenodo record shows MIT while the document says CC BY 4.0; the affiliation differs between the Blueprint and CITATION.cff/Zenodo | Not changed without the author: listed in `METADATA_TO_CONFIRM.md` |
| 5 | Decision Memo missing as a separate deliverable | The memo had been removed entirely; the brief requires it as a separate document with decisions, approvals, resources, risks and evidence needs | Restored, rewritten and reconciled; kept out of the Blueprint |

## 3. Issue register

Severity: **Critical**, **Major**, **Moderate**, **Minor** (definitions in the audit brief). Status: **Fixed** (in this branch, rebuilt and checked), **Open** (needs the author, counsel or a later stage), **Recorded** (documented; no change possible or appropriate).

| ID | File | Page or section | Issue | Severity | Evidence | Correction | Status |
|---|---|---|---|---|---|---|---|
| A-01 | Blueprint EN | Section 1.7 | "BAPIL is established as a university-anchored lab..." presents the proposed institution as existing; the Bangla text says "will be established" | Critical | Status table (nothing approved or constituted); BN 1.7 | "would be established", "would build", "would be run" | Fixed |
| A-02 | Blueprint EN/BN, Summary EN/BN | 2.6, 14.1, 14.2, Tables 42, 43, 60; Summary "Why now" | The Cyber Security (Amendment) Bill, 2026 was described as aimed at removal of harmful AI-generated content, "reported passed by 30 June 2026" | Major | The Financial Express and bdnews24 (30 June and 1 July 2026): the bill removed Section 20 on online gambling; Dhaka Tribune links it to AI content; a cabinet committee was formed on 2 July 2026 to finalise a further draft amendment | Passage date stated, disagreement disclosed, July 2026 draft added, implications reworded, U1 extended | Fixed |
| A-03 | Blueprint EN/BN | 8.12 | The data-protection framework "requires consent" | Major | Securiti [85]: other legitimate grounds; Bangladesh Law Digest [126]: consent set aside for national security, defence, public order, public interest | Consent described as the principal basis with other grounds and exemptions; BAPIL’s consent rule labelled as its own safeguard | Fixed |
| A-04 | Test fixture; Blueprint Annex M | `implementation/tests/fixtures/policy_{en,bn}.md`; M.1 | Sample text "Personal data must be processed only with consent" reproduced as example output | Moderate | Same as A-03 | Fixture rewritten and labelled fictitious; example output regenerated by running the CLI | Fixed |
| A-05 | Blueprint EN/BN, Summary, Memo | 1.1, 14.2, Tables 42, 60 | Revised draft National AI Policy (version 2.0, 9 February 2026) not mentioned; the Q4 2026 process could be read as a first draft | Moderate | aipolicy.gov.bd document listing | Added with the note that its content was not reviewed and that the link between processes is unconfirmed | Fixed |
| A-06 | Blueprint EN/BN | 16.x short term; 20.x; Annex "Relationship with existing institutions" | Present-tense statements of institutional existence | Moderate | Status table | Made conditional | Fixed |
| A-07 | Blueprint EN/BN | Overview ("What is built first") | "answers always cite official sources or abstain" stated as a guarantee | Moderate | Design rule; citation precision target 0.95 | "designed so that its answers cite official sources or abstain, with citation precision measured against a target of at least 0.95" | Fixed |
| A-08 | Blueprint EN/BN | 11.7 | "published documents can always be regenerated" | Minor | CI never run on GitHub | "any failure to regenerate... is detected" | Fixed |
| A-09 | Decision Memo | separate document | Removed from the project; the earlier draft also lacked the Year 1 funding commitment in D2, the adjusted budget, release status, citation-precision target, decisions already made, approvals and evidence required | Major | Blueprint Table 57, 17.2, Table 65 | Restored as `BAPIL_Decision_Memo_{en,bn}` (two pages each), reconciled with the Blueprint, not inserted into it | Fixed |
| A-10 | Release process | `blueprint/zenodo/UPLOAD_CHECKLIST.md` | The checklist called the automatic Zenodo version "expected" without noting that it would become the concept DOI’s latest version with CITATION.cff metadata | Major | White Paper record archived from GitHub release v1.0.1; Zenodo documentation: enabled repositories archive every release | Decision step added with options and a recommendation | Fixed (decision Open) |
| A-11 | Zenodo record 10.5281/zenodo.21363967 | Licence field | Shows MIT; the White Paper says CC BY 4.0 | Moderate | Record page, 22 October 2026; White Paper "Copyright & License" | Cannot be changed from here; documented for the author | Open |
| A-12 | `metadata.json` vs `CITATION.cff`, Zenodo, README | Affiliation | "Independent Researcher, Bangladesh" vs "Université Paris-Saclay" | Moderate | Files and records | The author chose "Independent Researcher, Bangladesh" for the Blueprint; whether `CITATION.cff` and the README author section follow at release v1.1.0 is listed for decision; Memo avoids an affiliation | Partly resolved |
| A-13 | Blueprint, Summary, Memo, data | Licence | CC BY 4.0 printed but never confirmed by the author for this release | Moderate | `metadata.json` | Listed for confirmation | Open |
| A-14 | `research/` | all files | No licence statement; the repository MIT licence is unsuitable for prose | Minor | Files | Listed for decision | Open |
| A-15 | README | Current status | "Reference implementation with tests and continuous integration" implied running CI | Moderate | Workflows not on GitHub | Wording changed; local-only test runs stated | Fixed |
| A-16 | Blueprint EN/BN | Table 60 | Hard-coded demonstration Recall@10 of 0.92; after the legal corrections the build measures 0.88 (21 of 24) | Moderate | `implementation/build/eval_report.json` | Table updated; the build now stops if Table 60 and the evaluation report disagree; gold labels deliberately not changed | Fixed |
| A-17 | Blueprint BN | 1.x, 4.x, 5.x, Annexes, Tables 41, 44, 53 | "মানবিক তত্ত্বাবধান" (humane supervision) used for human oversight; "মানবিক:" for human capital; "মানবিক বিচার" | Moderate | Terminology | "মানব-তত্ত্বাবধান", "মানবসম্পদ:", "মানব-বিচার" (12 occurrences) | Fixed |
| A-18 | Blueprint BN | Section 9.8 heading | "মানবিক বিবেচনা" for Human Factors | Minor | Terminology | "মানব-উপাদান বিবেচনা" | Fixed |
| A-19 | Blueprint BN | 14.2, national AI policy bullet | English sentence about the January and February drafts had no Bangla counterpart | Minor | Number-parity check | Translated | Fixed |
| A-20 | Blueprint EN | page 100 (old numbering) | A single line ("required for pilot P6.") alone on a page; missed by the previous QA | Minor | Sparse-page scan | Page enlarged at Section 20.4 | Fixed |
| A-21 | Blueprint BN | pages after 11.9, 14.7 and the references | New overflow pages caused by the longer corrected text | Minor | Sparse-page scan | Tighter row spacing for Tables 37 and 43, page enlargement at 14.7 and in the reference list | Fixed |
| A-22 | Build | evaluation corpus | The glob `blueprint/BAPIL_*.md` would have added the Memo to the demonstration corpus | Minor | Build script | Corpus restricted to Blueprint and Summary (also in CI, CLI help, README, Section 11) | Fixed |
| A-23 | `zenodo_metadata.json` | related identifiers | Relation "isDocumentedBy" the repository was semantically inverted | Minor | Zenodo relation vocabulary | Removed; tagged tree kept as *isSupplementedBy* | Fixed |
| A-24 | `SOURCES_AND_LICENCES.md` | Not included | Said the decision sheet was "planned as a separate, later publication" | Minor | A-09 | Updated | Fixed |
| A-25 | White Paper v1.0 | references | Cites the Cyber Security Act, 2023, which the 2025 Ordinance and the 2026 Act replaced | Moderate | Legal sources | Published record not edited; recorded in `docs/legal-references.md` (L14) | Recorded |
| A-26 | All legal statements | Ch. 2, 8, 14 | Gazetted texts not reviewed | Major | Official database blocks automated retrieval | Labelled "as reported"; counsel review before MS2 (U1 to U3, U15) | Open |
| A-27 | Blueprint references 1 to 83 | bibliography | Inherited from the White Paper and not re-verified item by item | Moderate | Previous QA | Unresolved item U11 | Open |
| A-28 | Blueprint BN | whole edition | No independent professional copy-edit yet | Moderate | U14 | Author’s editorial review done; terminology fixes in this audit | Open |
| A-29 | README | table of contents | Anchors such as `#inspiration-related-initiatives` may not match GitHub’s generated anchors | Minor | Link check | See `MARKDOWN_VALIDATION_REPORT.md` | See report |

## 4. Verified claim register

| Claim | Evidence (checked 21 or 22 October 2026) | Status | Files |
|---|---|---|---|
| Release v1.1.0 exists | GitHub releases page lists only v1.0.1 and v1.0; `git ls-remote --tags` shows `v1.0`, `v1.0.1` | **False today**; every document describes it as planned | README, RELEASE_NOTES, CHANGELOG, Blueprint 1.4, 11.1, Annex D, Memo |
| The Blueprint has a DOI | No Zenodo record found; documents print "DOI to be assigned on publication" | **False today**; correctly described | all |
| White Paper DOI 10.5281/zenodo.21363967 | Zenodo record (v1.0.1, 14 July 2026) | Verified | README, CITATION.cff, Blueprint |
| Executive Summary DOI 10.5281/zenodo.21441172 | Zenodo record (1.0, 21 July 2026, CC BY 4.0, English and Bengali) | Verified | same |
| Concept DOI 10.5281/zenodo.21360565 | Resolves to the White Paper record | Verified | README, CITATION.cff |
| Prototype version 0.1.0 | `implementation/pyproject.toml`, `bapil/__init__.py` | Verified | Blueprint, README, Memo |
| 49 unit tests pass | Local run, Python 3.13.16, 22 October 2026: `Ran 49 tests ... OK` | Verified locally; **no public CI record** (stated as such) | Blueprint 11.2, README, REPRODUCIBILITY |
| Source code publicly available | The prototype is only in the unpushed branch; the public `main` does not contain `implementation/` | **Not yet**; documents say it is "to be issued in release v1.1.0" | Blueprint, README, Memo |
| Reproducible evaluation | The demonstration evaluation is regenerated by every build; clean-clone rebuild matched earlier in October | Verified locally (development results only) | Blueprint 11.5, Table 60 |
| BanglaPolicyQA benchmark complete | No benchmark questions written | **Not built**; described as planned | all |
| Base case Tk 20.43 crore; low 17.93; adjusted 22.24; high 25.25 | `budget_model.py`; independent spreadsheet implementation agrees to within Tk 1 | Verified (recomputed) | Blueprint, Summary, Memo, docs |
| Annual totals 4.73, 7.49, 8.21 | Same; rounded rows add to 4.74, 7.48, 8.22 (explained in the Table 50 note) | Verified | Blueprint Table 50 |
| BAPIL is established, funded or has constituted bodies | No evidence; Blueprint Table 65 shows every precondition "not started" or "requested" | **No**; all documents now say it is a proposal | all |
| PDPA 2026 enacted in April 2026 (Act 63 of 2026) | Securiti [85], Azam [116] | Reported | Blueprint, Summary, Memo |
| Cyber Security (Amendment) Bill passed 30 June 2026 | FE [123], bdnews24, Dhaka Tribune [87] | Verified as reported (date); content disputed | Blueprint, Summary |
| National AI Policy draft v2.0 dated 9 February 2026 | aipolicy.gov.bd document listing [125] | Listing verified; content not reviewed | Blueprint, Summary, Memo |
| Drafting of a national AI policy to begin in Q4 (2026) | The Daily Observer, 10 August 2026 [91] | Reported | Blueprint, Summary, Memo |

## 5. Corrections applied (summary)

All substantive corrections are listed in [`blueprint/CHANGES.md`](../CHANGES.md), section 9, and in the issue register above. Every correction was made in the source files, in both languages where the text exists in both, and the outputs were rebuilt with `blueprint/build_blueprint.sh`.

## 6. Checks run after the corrections

| Check | Result |
|---|---|
| Full build | Passed; six PDFs, tables, figures, CSV, manifest |
| Unit tests | 49 passed (Python 3.13) |
| Quotation-mark check on all sources | Passed |
| Table 60 vs evaluation report | Consistent (Recall@10 0.88) |
| Budget workbook vs Python model | 0 differences above Tk 1; 612 formulas, 0 errors |
| Number parity EN vs BN (multi-digit numbers, by chapter) | Blueprint: remaining differences are layout values and numbers written as words in one language; Summary and Memo: none (see reconciliation report) |
| Sparse-page scan and visual inspection | See `blueprint/QA_REPORT.md` |
| CITATION.cff against the CFF 1.2.0 JSON schema | Valid (0 errors) |
| Markdown links | See `MARKDOWN_VALIDATION_REPORT.md` |

## 7. Files prepared for future publication

GitHub release v1.1.0 (to attach): `releases/v1.1/BAPIL_Technical_Blueprint_en.pdf`, `BAPIL_Technical_Blueprint_bn.pdf`, `BAPIL_Blueprint_Summary_en.pdf`, `BAPIL_Blueprint_Summary_bn.pdf`, `BAPIL_Decision_Memo_en.pdf`, `BAPIL_Decision_Memo_bn.pdf`; release text `RELEASE_NOTES.md`.

Zenodo record (to upload, generated by `blueprint/zenodo/make_zenodo_package.sh` into `dist/zenodo/`): the four Blueprint and Summary PDFs and Markdown files, the figure and table archives, the editable source archive (including the budget workbook and documentation), the reference implementation archive, `SHA256SUMS.txt`; metadata from `blueprint/zenodo/zenodo_metadata.json` and `description.html`.

Repository (to merge into `main`): everything on branch `blueprint-v1.0`.
