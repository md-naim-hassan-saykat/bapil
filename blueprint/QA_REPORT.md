# Quality-assurance report: BAPIL Technical Blueprint, Version 1.0

First checked on 22 October 2026 on the build of commit `0f74dc7`; checked again after the project-wide audit on the build of branch `blueprint-v1.0` (local, not pushed), section 7. Status key: **Pass**, **Fail**, **Open** (not resolved; recorded in the unresolved-items register, Table 68, or below).

## 1. Outputs checked

| File | Pages | Notes |
|---|---:|---|
| `releases/v1.1/BAPIL_Technical_Blueprint_en.pdf` | 145 | Letter size, PDF 1.5, all fonts embedded as subsets |
| `releases/v1.1/BAPIL_Technical_Blueprint_bn.pdf` | 142 | Same |
| `releases/v1.1/BAPIL_Blueprint_Summary_en.pdf` | 11 | Same |
| `releases/v1.1/BAPIL_Blueprint_Summary_bn.pdf` | 11 | Same |
| `releases/v1.1/BAPIL_Decision_Memo_en.pdf` | 2 | Separate document, not part of the Blueprint |
| `releases/v1.1/BAPIL_Decision_Memo_bn.pdf` | 2 | Same |

Sizes and SHA-256 checksums are in `MANIFEST.md`.

## 2. Quotation marks: diagnosis and correction

**What the reviewer saw.** A search for `'` and `"` in the previous PDFs found nothing in prose.

**What the files actually contained.**

| File (before) | Straight `"` | Straight `'` | “ | ” | ’ |
|---|---:|---:|---:|---:|---:|
| Audit and Revision Report PDF | 0 | 0 | 30 | 30 | 11 |
| Blueprint, Bangla | 116 (code only) | 12 | 0 | 18 | 4 |
| Blueprint, English | 116 (code only) | 0 | many | many | 155 |

**Root cause.** Typography in the build, not missing characters, encoding damage or a search limitation:

1. The English edition and the report were built with pandoc's `smart` extension, which writes typographic marks (“ ” ’). Searching for straight marks cannot find them.
2. The Bangla edition was built with `smart` switched off, so straight `"` reached XeLaTeX, but the font was loaded with the TeX ligature mapping (`Ligatures=TeX`, pandoc's default), which replaces every `"` with ” (U+201D). Opening quotes therefore printed as closing quotes, and the PDF contained no straight quotes in prose.
3. A second, separate search problem was found: Bangla words were extracted from the PDF with pre-base vowel signs (ে, ি, ৈ) out of order, so an ordinary search for a Bangla word could fail.

**Correction.**

* Convention: “ ” and ‘ ’ in prose and bibliography in both editions, ’ for the English apostrophe; straight marks only in code, URLs, JSON and command lines.
* Applied in the sources (not at output) with `src/typography.py`, which protects code, URLs, link targets, YAML, raw LaTeX and build markers; escaped quotes in table data fixed by hand; White Paper references normalised during assembly without editing the White Paper.
* Build: `smart` off and `Ligatures=TeXOff`, so the PDF holds exactly the source characters; `typography.py --check` runs on every build and stops it on a straight quote in prose.
* Bangla text extraction: `\XeTeXgenerateactualtext=1`.
* Font switching after a quote: typographic quotes assigned to the Latin character class (before this, a Bangla word directly after “ lost its glyphs).

**Result (after).**

| File | Straight `"` | Straight `'` | “ | ” | ‘ | ’ |
|---|---:|---:|---:|---:|---:|---:|
| Blueprint, Bangla | 116 (code only) | 0 | 9 | 9 | 0 | 16 |
| Blueprint, English | 116 (code only) | 0 | 8 | 8 | 0 | 164 |
| Summary, Bangla | 0 | 0 | 0 | 0 | 0 | 4 |
| Summary, English | 0 | 0 | 0 | 0 | 0 | 6 |

Opening and closing marks are balanced in every file. Searching the Bangla PDF for “নিশ্চিত করতে হবে” or for Bangla words containing pre-base vowels (for example হোয়াইট পেপার) finds them. Users who search with a straight `"` will not find typographic quotes; they should search for “ or for the words.

## 3. Checklist

### Identity and naming

| Item | Status | Evidence |
|---|---|---|
| Final title is correct | Pass | Title page, document information, copyright page, PDF metadata (BN: বাংলাদেশ এআই পলিসি অ্যান্ড ইনোভেশন ল্যাব (BAPIL): টেকনিক্যাল ব্লুপ্রিন্ট) |
| "Audit", "Revised", "Revision" absent from title, running headers and public filenames | Pass | Headers "BAPIL টেকনিক্যাল ব্লুপ্রিন্ট / সংস্করণ ১.০" and "BAPIL Technical Blueprint / Version 1.0"; filenames `BAPIL_Technical_Blueprint_bn.pdf`, `_en.pdf`. The publication no longer describes itself as revised (CHANGES.md, 1.3 to 1.5) |
| Publication date displayed is October 2026 | Pass | Title page, copyright page, document information; PDF dates `D:202610` |
| Necessary historical and legal dates remain accurate | Pass | Law, event, source and access dates unchanged; evidence-check dates (21 and 22 October 2026) kept as substantive |
| No one-page decision sheet inserted | Pass | Memo removed from the publication set, Figure 1, Table 1 and all references; Chapter 21 unchanged |

### Typography and search

| Item | Status | Evidence |
|---|---|---|
| Quotation-mark issue diagnosed | Pass | Section 2 |
| Quotation marks and apostrophes consistent | Pass | Source check passes; counts above |
| Ordinary search works for the characters used | Pass | Section 2 |
| No punctuation or meaning damaged by replacement | Pass | Every changed line reviewed in the diff; code, URLs and JSON untouched (116 straight quotes remain, all in code) |
| Bengali Unicode text renders correctly | Pass | No missing-glyph warnings in the build log; pages inspected |
| Fonts embedded | Pass | `pdffonts`: all fonts embedded and subset |

### Content

| Item | Status | Evidence |
|---|---|---|
| Material factual issues corrected or labelled unresolved | Pass | R-01 to R-25 applied (CHANGES.md, section 4); remaining items in Table 68 (U1 to U16) |
| Legal claims accurately qualified | Pass, with an open item | All legal statements are attributed to secondary sources; gazetted texts not reviewed (Open: U1 to U3, counsel required) |
| Technical targets distinguished from measured results | Pass | Targets labelled "proposed target"; Section 11.5 labelled development results |
| Budget totals checked | Pass | All budget tables computed by `budget_model.py`; totals 4.73, 7.49, 8.21 = 20.43; rounded rows 4.74, 7.48, 8.22, 20.42 explained; scenarios 17.93, 22.24 (adjusted), 25.25; bridge 18.49 to 20.43 reproduces |
| Tables agree with the narrative | Pass | Numbers compared section by section between text and tables and between the editions (no differences) |
| Citations and references checked to the extent possible | Pass, with an open item | References 84 to 122 checked; references 1 to 83 inherited from the White Paper not re-verified item by item (Open: U11) |
| No unsupported implementation or publication claims | Pass | Release, DOI and code-availability statements are conditional and verifiable |

### Layout

| Item | Status | Evidence |
|---|---|---|
| All pages inspected | Pass | Contact sheets of every page of both editions; key pages (title, Figure 1, Tables 60 to 68) at higher resolution |
| No text clipped | Pass | No overfull table cells or figure labels seen |
| Tables readable | Pass | |
| Figures and diagrams clear | Pass | Vector figures; labels legible at 100% zoom |
| Page numbers and cross-references correct | Pass | All 322 (BN) and 326 (EN) internal links resolve; every table 1 to 68 and figure 1 to 15 is cited; no reference above Table 68 |
| No unexpected blank pages or layout defects | Pass, minor (revised in section 7) | First pass: near-empty overflow pages removed by page enlargement. Section 7 found that several of those enlargements made body text overprint the page number; corrected |

### Source files

| Item | Status | Evidence |
|---|---|---|
| Editable master included | Pass | `src/en/`, `src/bn/` and `*.src.md` |
| Table and figure sources included | Pass | `src/tables_*.py`, `src/make_figures.py`, `src/figures_new.py` |
| Assets and dependencies accounted for | Pass | No raster assets; fonts and tools documented in `README.md` and `SOURCES_AND_LICENCES.md` |
| README and reproduction instructions included | Pass | `README.md` |
| Sufficient for future maintenance | Pass | Clean-clone rebuild (section 4) |
| No secrets or unauthorised third-party material | Pass | Repository searched for keys and tokens; no third-party images; fonts not redistributed |

### GitHub readiness

| Item | Status | Evidence |
|---|---|---|
| Repository structure and history inspected | Pass | Remote `main` at `4756cf9`; tags `v1.0`, `v1.0.1`; conventions `reports/` and `releases/vX/` followed |
| File naming consistent | Pass | |
| White Paper files and earlier releases intact | Pass | White Paper and Executive Summary sources and `releases/v1.0/` unchanged since `4756cf9` (verified with `git diff`); only `reports/README.md` received a one-character fix (a missing closing backtick) |
| Documentation identifies the actual deliverables | Pass | Root `README.md`, `releases/README.md`, `blueprint/README.md`, `MANIFEST.md` |
| No unperformed push or release claimed | Pass | All documents say the release and DOI do not exist yet |
| Commit and release instructions provided | Pass | `zenodo/UPLOAD_CHECKLIST.md` and the hand-over note |

## 4. Reproducibility test

The repository was cloned into an empty directory, all generated files (tables, figures, data, assembled Markdown, PDFs) were deleted, and `blueprint/build_blueprint.sh` was run (3 minutes). Result: all 408 table files (LaTeX, PDF, PNG), 136 Markdown tables, 90 figure files, the budget CSV files and the four assembled Markdown files were byte-identical to the committed ones. The four PDFs were identical in text, fonts and images; they differ only in the 16-byte PDF file identifier, which XeTeX derives from pandoc's randomly named temporary directory.

The 49 unit tests pass on Python 3.13; on Python 3.10, 3.11 and 3.12 all pass except one optional schema test, which is skipped because `jsonschema` is not installed (Linux only).

## 5. Accessibility

Not fully evaluated, and the PDFs are not tagged (no PDF/UA claim). What is in place: real text throughout (no page images), embedded fonts, correct Unicode extraction including Bangla, document language (`/Lang` bn or en), title metadata, bookmarks for chapters and sections, and clickable links.

## 6. Open items

* Independent professional copy-edit of the Bangla edition (U14).
* Legal confirmation of the 2025 and 2026 instruments by Bangladesh counsel (U1 to U3) and of the host's ability to accept the ERRC veto (U15).
* Costs not yet in the base case (U16).
* GitHub release v1.1.0 and the Blueprint DOI (U4).
* Affiliation: the author chose "Independent Researcher, Bangladesh" for the Blueprint; whether `CITATION.cff` and the README author section (Université Paris-Saclay) follow at release v1.1.0 is open (`review/METADATA_TO_CONFIRM.md`).
* Licence of the documents (CC BY 4.0 as printed) to be confirmed by the author.

## 7. Second pass after the project-wide audit (22 October 2026)

The audit corrected legal, institutional and technical statements in both editions and the Summary, restored the Decision Memo as a separate document and changed several layouts (`CHANGES.md`, section 9; `review/PROJECT_AUDIT_REPORT.md`). All six PDFs were rebuilt with `blueprint/build_blueprint.sh` and checked again.

| Check | Result | Evidence |
|---|---|---|
| Full build | Pass | Exit status 0; tables, figures, budget CSV, six PDFs, manifest |
| Unit tests | Pass | 49 of 49 (Python 3.13.16) |
| Demonstration evaluation agrees with Table 60 | Pass | Recall@10 0.875 (shown as 0.88, 21 of 24), 6 of 6 abstentions; the build stops on a mismatch |
| Quotation-mark convention in the sources | Pass | `typography.py --check` in the build |
| Missing Bangla or Latin glyphs | Pass | No "Missing character" in the build log |
| Fonts embedded | Pass | `pdffonts`: no font without embedding in any of the six PDFs |
| Titles and PDF metadata | Pass | Titles exactly as specified; creation and modification dates `D:202610`; subject and keywords set |
| Internal links | Pass | 326 (EN) and 322 (BN) internal links, all resolving to named destinations |
| Body text clear of page numbers | **Fail, then fixed** | A bounding-box check of every page found body text overprinting or touching the page number on seven pages, all caused by `\enlargethispage` of two or more lines (two of them from the first pass: English page 99 and the Bangla reference list). All such enlargements were removed; after the fix no page has body text within 8 pt of the page number |
| Short pages | Pass, minor | No page carries a single line or a single entry. Part title pages are intentionally sparse. Remaining short chapter or annex endings, accepted: Bangla page 74 (end of Chapter 14, three lines), Bangla page 100 and English page 104 (end of Annex B, two and three lines); English pages 64 and 92 and Bangla page 36 end chapters at half a page; the list of tables ends on a short page in both editions |
| Visual inspection | Pass | Title and copyright pages, Figure 3, Tables 37, 42 and 43, Chapters 20 and 21, Annex B and the reference lists of both editions; both Decision Memo pages in both languages; Summary pages 2 to 4 |
| Bangla Table 43 | Pass | Set in footnote size to keep Chapter 14 compact; legible at 100% zoom |
| Budget workbook | Pass | `make_budget_workbook.py --check`: low 17.93, base 20.43, adjusted 22.24, high 25.25 crore and every annual total identical to `budget_model.py`; no difference larger than Tk 1 |
| `CITATION.cff` | Pass | Valid against the CFF 1.2.0 schema |
| Markdown and links | Pass after fixes | `review/MARKDOWN_VALIDATION_REPORT.md` |
| Clean-clone rebuild | Pass | Commit `085dea3` cloned into an empty directory; all generated tables, figures, CSV files, assembled Markdown, PDFs and the evaluation report deleted; full build run (4 minutes). Tables, figures, CSV files and the six assembled Markdown files byte-identical to the committed ones; the six PDFs identical byte for byte apart from the 16-byte PDF file identifier (`/ID`) |
| Rebuild from the Zenodo source archive | Pass | `BAPIL_Technical_Blueprint_source.zip` and `bapil-reference-implementation-0.1.0.zip` (from `make_zenodo_package.sh`) unzipped into an empty directory; `blueprint/build_blueprint.sh` completed and produced the six PDFs, identical apart from `/ID`. Before this audit the archive lacked `make_manifest.py` and three of the four `reports/*.md` files used by the demonstration corpus, so it could not have reproduced the PDFs; both were added |

## 8. Third pass: reference numbering and Annex W (22 October 2026)

| Check | Result | Evidence |
|---|---|---|
| References sequential | Pass | In all six documents the citations, read in order, are 1, 2, 3 ... with no gaps, and every cited number is listed (after section 9: Blueprint 104 in both editions, Summary 10, Memo 5); the build stops if a citation exceeds the list or a Bangla edition cites a reference the English does not |
| Annex W figures | Pass | Tables 69 and 70 and every figure quoted in Section 17.3, the front matter, the Summary and the Memo come from `budget_model.py`; totals 25.50, 36.08, 45.26, 51.11, 60.90 = 218.85; posts 58 to 118 |
| English and Bangla numbers in Annex W and Section 17.3 | Pass | Multi-digit numbers identical (Bangla digits converted) |
| Full build, tests, evaluation | Pass | Exit 0; 49 tests; Recall@10 0.875 unchanged and consistent with Table 60 |
| Fonts, glyphs, links | Pass | All fonts embedded; no missing characters; 333 (EN) and 328 (BN) internal links resolve |
| Body text clear of page numbers | Pass | No page within 8 pt |
| Short pages | Pass, minor | As in section 7; the list of tables now ends with four entries in English |
| Visual inspection | Pass | Annex W and Tables 69 and 70 in both editions; reference list pages with the White Paper marks (now an asterisk) |

## 9. Fourth pass: references and Chapter 17 (22 October 2026)

| Check | Result | Evidence |
|---|---|---|
| New references verified | Pass | Each of the 20 new entries checked against the publisher page, DOI or official site (October 2026) |
| Citations sequential | Pass | Blueprint 104 (both editions), Summary 10, Memo 5; no gaps |
| Tranche and capital figures | Pass | 4.73, 7.49, 8.21; 23.1% by end of Year 1; capital 1.14, 1.02, 0.30 = 2.46 (12.0%); all from `budget_model.py` |
| Build, tests, evaluation, fonts, links, page numbers | Pass | Exit 0; 49 tests; Recall@10 0.875; all fonts embedded; no body text within 8 pt of a page number |
| Visual inspection | Pass | Section 17.2 and Table 62 in both editions |

## 10. Fifth pass: integrated pathway and employment terms (22 October 2026)

| Check | Result | Evidence |
|---|---|---|
| Funding shares inside Table 51 ranges and adding to 100% | Pass | `check_funding_shares` runs on every build |
| Pathway figures | Pass | Table 71, Table 72, Figure 16, Annex W.4 text and Summary all from `budget_model.py`: stages 4.73, 15.70, 218.85; posts 9, 19, 118; government 39% of the 36-month plan |
| New references verified | Pass | Six sources opened on 22 October 2026 (Civil Service World, Singapore government, BetaKit, IndiaAI notice, Cabinet Division letter as reproduced, The Daily Star) |
| Citations sequential | Pass | Blueprint 110 (both editions), Summary 10, Memo 5 |
| Build, tests, evaluation, fonts, page numbers | Pass | Exit 0; 49 tests; Recall@10 0.875; all fonts embedded; no body text within 8 pt of a page number |
| Visual inspection | Pass after fixes | Figure 16 (EN/BN): legend moved clear of the gate labels; Table 71: first column widened (a bold label touched the next column); Table 72 kept on one page |

## 11. Sixth pass: re-verification of the White Paper references (22 October 2026)

| Check | Result | Evidence |
|---|---|---|
| All 40 White Paper references checked at source | Pass | 34 opened directly or through the official PDF, 6 confirmed through search results where the site blocks automated access (`review/REFERENCE_VERIFICATION.md`) |
| Errors found and corrected | 13 entries | DOI, year, title, authors or publisher; applied through `WP_CORRECTIONS` in `assemble.py`, which stops the build if a corrected text is no longer found |
| Wrong edition cited | 1 citation fixed | Table 4 cited the 2025 index for a 2023 ranking; the 2023 report (rank 82, score 46.04) is now cited |
| Citations sequential | Pass | Blueprint 111 (both editions), Summary 10, Memo 5 |
| Build, tests, evaluation, fonts, page numbers | Pass | Exit 0; 49 tests; Recall@10 0.875; no body text within 8 pt of a page number |

## 12. Seventh pass: sourced unit costs, Bangla editorial pass, engagement pack (22 October 2026)

| Check | Result | Evidence |
|---|---|---|
| Unit costs checked against published sources | Done; base case unchanged | Seven sources opened on 22 October 2026 (keys 155 to 161). Staff, fellowship and hosting assumptions are consistent with them. Equipment sits at the lower end of 2026 prices; the list-price effect (+Tk 0.74 crore; +Tk 1.63 crore with duty and VAT) was computed with `budget_model.py` and is stated in Section 17.1 |
| Bangla spelling consistency | 76 standardisations and 4 rewordings | `review/BANGLA_EDITORIAL_LOG.md`; replacements matched Bangla word boundaries only, and no code, links or markers changed |
| English and Bangla number parity | Pass | No new differences. The remaining ones are layout values, units ("1 million" and "১০ লক্ষ") and numbers written as words, as before |
| Citations sequential | Pass | Blueprint 118 (both editions), Summary 10, Memo 5. Published numbers up to 98 are unchanged, so `docs/legal-references.md` needs no change |
| Short pages | Accepted set only | English 15, 31, 40, 64, 65, 78 and 105; Bangla 16, 31, 36, 40, 56, 64, 75, 76 and 101. These are part openers, or chapter or annex endings. A new two-line Bangla page before Annex A was removed by tightening Table 57 |
| Page numbers | Pass | No body text within 8 pt of a page number in any of the six PDFs |
| Build, tests, evaluation, fonts | Pass | Exit 0; 49 tests passed; Recall@10 0.875 (21 of 24), 6 of 6 abstentions; all fonts embedded; no missing glyphs; typography check passed |
| Engagement PDFs | Pass | `docs/engagement/make_pdfs.sh` builds all six. The briefing notes fit on one A4 page in English and in Bangla. Mixed Bangla and Latin text was checked visually |
| No en or em dashes in new text | Pass | Checked over the whole diff |
