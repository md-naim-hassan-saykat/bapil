# Change log: final production stage (October 2026)

This log records the corrections made while finalising the BAPIL Technical Blueprint, Version 1.0, for publication. The earlier audit and adversarial review are in `review/`. Each item gives the change and its justification. "EN/BN" means both editions were changed identically.

## 1. Identity, naming and date

| # | Change | Justification |
|---|---|---|
| 1.1 | Bangla title set to "বাংলাদেশ এআই পলিসি অ্যান্ড ইনোভেশন ল্যাব (BAPIL): টেকনিক্যাল ব্লুপ্রিন্ট"; the institution's Bangla name and "টেকনিক্যাল ব্লুপ্রিন্ট" used throughout the Bangla edition, running header, figures, standalone tables and PDF metadata | Final title instruction; consistent naming |
| 1.2 | Publication files renamed `BAPIL_Technical_Blueprint_bn.pdf` / `_en.pdf` (and Summary `_bn` / `_en`); sources and assembled Markdown renamed to match; build script, CI workflow, benchmark document identifiers, README files and Zenodo files updated | Final filename instruction |
| 1.3 | The publication no longer presents itself as a revised or audited document: the "Revision status" row became "Evidence status"; method step 6 became "Evidence check" (and the method now correctly says six steps, not five); Annex V became "Unresolved Items"; the draft's change-record table (old Table 68) moved to `review/BAPIL_Blueprint_Prepublication_Change_Record.md`; Table 69 renumbered 68; the table count became 68 (EN/BN) | Identity instruction; internal review artefacts kept separate but traceable |
| 1.4 | Table 60 (evidence status) rewritten to state each claim as it appears in the final text, with a column "How the text presents it" instead of "Action in this edition"; no claim, status or evidence was removed (EN/BN) | Same; substance preserved |
| 1.5 | Budget reconciliation (Table 61, Section 17.2, Annex Q) describes the starting point as "an initial planning estimate made while drafting" instead of "the draft before this review" (EN/BN; also `budget_model.py` labels) | Same |
| 1.6 | Only "October 2026" / "অক্টোবর ২০২৬" is displayed as the publication date; PDF creation and modification dates set to the month only (`D:202610`) | Date instruction |

## 2. Decision sheet

| # | Change | Justification |
|---|---|---|
| 2.1 | The one-page Decision Memo removed from the publication set: its sources, assembled files and PDFs deleted from the working tree (kept in Git history), its box removed from Figure 1, its row removed from Table 1, and references removed from "How to Read", Section 16.4, Section 21.3, Annex D, Table 60 and the Summary (EN/BN) | Instruction not to include a decision sheet; substantive content (Chapter 21, Table 57) unchanged |

## 3. Quotation marks and text extraction

| # | Change | Justification |
|---|---|---|
| 3.1 | Root cause identified: the Bangla edition was built with pandoc's `smart` extension switched off, so straight `"` reached XeLaTeX, whose TeX-ligature font mapping turned every `"` into a closing mark ” (opening quotes printed as closing quotes, and the PDF contained no straight quotes). The English edition used `smart`, so its PDF contained only “ ” and ’. The audit report PDF likewise contained only typographic marks. Searching for `'` or `"` therefore found nothing in prose; this was typography, not missing characters | Diagnosis requirement |
| 3.2 | Convention adopted for both editions: “ ” and ‘ ’ in prose and bibliography, ’ for the English apostrophe; straight marks only in code, URLs, JSON and command lines. Sources normalised with a context-aware script (`src/typography.py`) that protects code, URLs, link targets, YAML, raw LaTeX and build markers; about 100 lines changed in the Markdown sources, plus apostrophes and escaped quotes in the table data; White Paper references normalised at assembly without editing the White Paper | Consistent, searchable convention; no blind replacement |
| 3.3 | Build changed so that the PDF holds exactly the source characters: `smart` off for both editions and `Ligatures=TeXOff` on the main and sans fonts; `typography.py --check` runs on every build | Prevents recurrence |
| 3.4 | `\XeTeXgenerateactualtext=1` added, so that Bangla text copied or searched in the PDF keeps Unicode order (before, pre-base vowel signs such as ে and ি were extracted out of order, which broke ordinary search in Bangla) | Searchable text requirement |
| 3.5 | Typographic quotes and dashes assigned to the Latin character class, so that a Bangla word immediately after “ switches to the Bangla font (otherwise glyphs were missing); standalone tables and figures switched to the same group-free font switching | Found while verifying 3.2 |
| 3.6 | PDF metadata passed to pandoc through a UTF-8 YAML file; passing it on the command line garbled the Bangla title when the system locale was not UTF-8 | Correct Bangla title in PDF metadata |

## 4. Corrections from the adversarial review (R-01 to R-25), EN/BN

| ID | Change |
|---|---|
| R-01 | "DOI to be assigned on publication (reserved on Zenodo)" became "DOI to be assigned on publication"; Table 1 "DOI assigned at publication"; Annex D item 3 explains when a DOI is reserved |
| R-02 | Release claims made verifiable: the code is "to be issued in repository release v1.1.0"; readers are told where to check and that the Zenodo record is published only after the release exists (status table, Overview, Section 1.4, Section 1.7, Section 11.1, Table 1, Summary) |
| R-03 | Section 15.1: start date depends on the funding route; January 2027 only with funding already available; second half of 2027 more realistic through the development budget [35] |
| R-04 | Decision D2 now includes committing or identifying Year 1 funding (about Tk 4.7 crore); Section 21.2 no longer says the 90-day plan can start "immediately" |
| R-05, R-06 | Section 17.2: known omissions (engagement events, P5 survey data, travel, open-access fees, staff computers) and the low 5% contingency stated; adjusted base case of about Tk 22.2 crore computed by `budget_model.py` (new `adjusted` scenario) and added to Table 62; Table 49 contingency row recommends 10%; Summary updated; new unresolved item U16 |
| R-07 | Residency amendment described as changing data-residency provisions, with commentary that localisation is limited to critical sectors; new reference [122] (The Business Standard, 20 April 2026); Sections 8.12 and 14.1, Tables 42 and 43 |
| R-08 | Sections 8.1 and 14.2: public documents carry low, not zero, personal-data risk; names in gazettes are never profiled or used for analytics or training |
| R-09 | ERRC decisions bind the host only as far as its statutes and the host agreement allow; legal review before signing; fallback clause (Section 5.3, Annex F, Table 64); new unresolved item U15 |
| R-10 | Identity and production audit store due before G2 (Table 37); added to the G2 checklist (Annex J) |
| R-11 | Romanised and code-mixed queries reported in v0 and gated from v1 (Tables 28, 63); transliteration row added to Table 37 |
| R-12 | Section 1.7: Year 3 delivers a documented decision on domain adaptation, not a model |
| R-13 | Section 11.5: results described as development results with their limits |
| R-14 | Section 9.6: a hosted commercial model is evaluated on P0 data only, as a reference point |
| R-15 | Section 9.7: Stage 1 is costed before approval (one to two ML staff for about twelve months, Tk 0.3 to 0.5 crore; up to USD 20,000 of compute) |
| R-16, R-17 | P3 gates G2 at month 15 and G3 at month 18; P6 protocol approval at MS5 and methods paper by MS7 (Tables 44, 66) |
| R-18 | Usefulness defined once: mean rating at least 4.0 of 5 from at least 30 active users (Section 12.3, Table 38) |
| R-19 | Section 11.2: Python claim limited to what was tested. The unit tests were then run locally on Python 3.10, 3.11, 3.12 and 3.13 (Linux): all 49 pass on 3.13; on 3.10 to 3.12 one optional schema test is skipped because `jsonschema` is not installed |
| R-20 | Section 9.2: threshold calibrated on the development split; the prototype uses a fixed threshold |
| R-21 | Section 17.3: Tk 7.3 crore derived explicitly from Tk 6.35 crore of recurring direct costs plus 15% |
| R-22 | Section 17.5: basis of Tk 500 an hour stated as a planning assumption |
| R-23 | Table 50 note gives the sums of the rounded rows (4.74, 7.48, 8.22, 20.42), computed by the build |
| R-24 | NFR-04: 99% availability once the recovery site exists in Year 2; Table 63 availability rule changed to match (reported in Year 1, at least 99% from Year 2), which the review had not covered |
| R-25 | Section 9.7: the White Paper's model name is kept for continuity; within 36 months at most a domain adaptation is built |

## 5. Other substantive corrections

| # | Change | Justification |
|---|---|---|
| 5.1 | Table 60: the demonstration corpus is now 8 documents (was 10), because the Decision Memo is no longer in the corpus; Recall@10 0.92 and 6 of 6 abstentions are unchanged (build evaluation report) | Consistency with the rebuilt evaluation |
| 5.2 | Unresolved item U14 reworded: the author's editorial review of the Bangla edition is done; an independent professional copy-edit is still outstanding | Accurate status |

## 6. Bangla editorial review

* "আয়োজক" (organiser) replaced by "স্বাগতিক" for the host institution and host agency throughout text, tables and figures; Annex E Article 1 reworded ("[স্বাগতিক প্রতিষ্ঠান]-এ স্থাপিত").
* "বহিরাগত"/"বহিস্থ" unified as "বহিঃস্থ" (external members and reviewers).
* "কিনা" corrected to "কি না" where it is the question particle.
* MFA rendered as "বহু-উপাদান প্রমাণীকরণ" (was "বহু-স্তর").
* NIST CSF functions disambiguated: চিহ্নিতকরণ (Identify) and শনাক্তকরণ (Detect), with the English names in the Table 32 labels; "সনাক্তকরণ" (misspelling) removed.
* Affiliation label in the document information table: "অধিভুক্তি".
* Sentences reworded for grammar or clarity: Section 2.6 (year adjacency), Section 11.9 and Annex D item 2 (related-identifier relations), Section 21.4 (last sentence), Annex D item 3 (aligned with the English).
* Numbers, dates, table and figure references compared section by section with the English edition; all sections match.

## 7. Layout

* Bangla PDF: overflow pages removed after the acronym table, Section 14.7, Table 66 and Annex M (row spacing, page enlargement or a shorter note); the Bangla edition is now 132 pages, the English 140.
* English PDF: overflow page after Table 67 removed.

## 8. Build and package

* Budget model can write its outputs as CSV (`data/`); the build does so.
* `SOURCE_DATE_EPOCH` fixed for reproducible builds.
* Documentation added: `README.md` (reproduction guide), `MANIFEST.md`, `QA_REPORT.md`, `SOURCES_AND_LICENCES.md`, `review/README.md`; Zenodo checklist rewritten in the required order (release before publication of the record).
* `CITATION.cff`: version and release date left at the last published release (1.0); the earlier change to 1.1.0 and to a release date that has not happened was reverted, and the author's affiliation line restored.
