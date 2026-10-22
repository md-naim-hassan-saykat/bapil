# Markdown, link and metadata validation report

Checked on 22 October 2026 on branch `blueprint-v1.0` (local, not pushed). Internal record; not part of the publication.

## 1. Scope

32 hand-written Markdown files: the root files (`README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `REPRODUCIBILITY.md`, `DATA_AND_METHODOLOGY.md`, `RELEASE_NOTES.md`, `SECURITY.md`), `docs/`, `releases/README.md`, `blueprint/*.md` documentation, `blueprint/review/` and `blueprint/zenodo/`. Not checked here: the generated Markdown (assembled publications and table snippets, which are checked by the build), the published White Paper and Executive Summary sources in `reports/` (DOI-registered, not edited) and `research/`.

## 2. Tools

No Markdown linter or link checker could be installed (the package registries were not reachable from this environment). The checks below were run with short Python scripts written for this audit; they are not a substitute for `markdownlint` or `lychee`, which the author can run before release.

## 3. Structural checks

| Check | Result |
|---|---|
| Code fences closed | Pass (all files) |
| Heading levels do not skip (for example H2 to H4) | Pass (all files) |
| Exactly one H1 per file | Pass, except the two historical review reports (`BAPIL_Blueprint_Adversarial_Review.md`, `BAPIL_Blueprint_Audit_and_Revision_Report.md`), which use H1 for their numbered sections because they are also typeset as PDFs. Left unchanged |
| Every table row has the same number of columns as its header | Pass |
| No leftover placeholders (`TODO`, `TBD`, `FIXME`, template tokens) | Pass after one fix: the README said "PAGES_EN pages in English and PAGES_BN in Bangla"; now "139 pages in English and 134 in Bangla" |
| No old titles ("Revised", "Audit" in a publication title) | Pass |
| Intentional pending markers | `10.5281/zenodo.PENDING` appears only in `blueprint/src/metadata.json` and in documentation that explains it; no fake DOI is printed in any publication |

## 4. Relative links and anchors

102 relative links (files, directories and `#anchors`) were resolved against the working tree, with GitHub's anchor rules for headings.

| Result | Detail |
|---|---|
| Fixed | `README.md` table of contents: `#inspiration-related-initiatives` did not match GitHub's anchor for "Inspiration & Related Initiatives" (`#inspiration--related-initiatives`) |
| Fixed | `PROJECT_AUDIT_REPORT.md` linked to this report before it existed |
| Remaining broken links | None |

## 5. External links

38 distinct external URLs appear in the checked files. The shell of this environment cannot reach them (requests are refused by the network policy), so they could not all be tested automatically.

| URL group | Status |
|---|---|
| GitHub releases page; Zenodo records 21363967 (White Paper) and 21441172 (Executive Summary); concept DOI 21360565 | Opened on 22 October 2026: content as described |
| Sources of the corrections in this audit: The Financial Express (30 June and 16 July 2026), The Daily Observer (2 July 2026, reference [124]), Dhaka Tribune (30 June 2026), Bangladesh Law Digest (18 August 2026, reference [126]) | Opened on 22 October 2026: content matches the way the Blueprint cites it |
| Other references cited in `docs/legal-references.md` and the Blueprint | Access dates (21 and 22 October 2026) recorded in the reference list; not re-opened in this pass |
| README badges (shields.io, Zenodo DOI badge) | Not testable from here |
| README "tests" badge (`actions/workflows/tests.yml/badge.svg`) | Will show no status until the branch with `.github/workflows/tests.yml` is merged into `main` and the workflow has run |

## 6. Metadata files

| File | Check | Result |
|---|---|---|
| `CITATION.cff` | Validated against the Citation File Format 1.2.0 JSON schema | Valid (0 errors). Version 1.0 and release date 2026-07-14 describe the last real release; they are to be updated only when v1.1.0 is published |
| `blueprint/zenodo/zenodo_metadata.json` | JSON syntax; fields of the Zenodo deposit metadata | Valid JSON; no DOI, publication date or version beyond those that exist; licence marked as to be confirmed |
| `blueprint/src/metadata.json` | Drives titles, PDF metadata and the DOI text | Titles match the brief exactly; publication date "October 2026"; DOI pending |

## 7. Consistency of names, dates and versions

The English and Bangla titles, the publication month (October 2026, অক্টোবর ২০২৬), the document version (1.0), the planned repository release (v1.1.0, not yet created) and the DOI status (not yet assigned) were compared across `README.md`, `RELEASE_NOTES.md`, `CHANGELOG.md`, `CITATION.cff`, `docs/`, the Zenodo files and the PDF metadata. No disagreement remains apart from the author affiliation, which is listed in [`METADATA_TO_CONFIRM.md`](METADATA_TO_CONFIRM.md).
