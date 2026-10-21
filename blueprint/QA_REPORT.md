# Quality-assurance report: BAPIL Technical Blueprint, Version 1.0

Checked on 22 October 2026 on the build of commit `0f74dc7` (branch `blueprint-v1.0`, not pushed). Status key: **Pass**, **Fail**, **Open** (not resolved; recorded in the unresolved-items register, Table 68, or below).

## 1. Outputs checked

| File | Pages | Notes |
|---|---:|---|
| `releases/v1.1/BAPIL_Technical_Blueprint_bn.pdf` | 132 | Letter size, PDF 1.5, all fonts embedded as subsets |
| `releases/v1.1/BAPIL_Technical_Blueprint_en.pdf` | 140 | Same |
| `releases/v1.1/BAPIL_Blueprint_Summary_bn.pdf` | 11 | Same |
| `releases/v1.1/BAPIL_Blueprint_Summary_en.pdf` | 12 | Same |

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
| No unexpected blank pages or layout defects | Pass, minor | Near-empty overflow pages removed. Remaining: the English list of tables ends with two entries on page 14; part title pages are intentionally sparse |

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
* `CITATION.cff` gives the author's affiliation as Université Paris-Saclay, while the Blueprint gives "Independent Researcher, Bangladesh"; the author should choose one before release.
