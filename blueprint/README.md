# BAPIL Technical Blueprint (Version 1.0)

**Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint**  
**বাংলাদেশ এআই পলিসি অ্যান্ড ইনোভেশন ল্যাব (BAPIL): টেকনিক্যাল ব্লুপ্রিন্ট**  
Version 1.0, October 2026. Author: Md Naim Hassan Saykat (ORCID 0009-0007-5270-3970).

The Technical Blueprint turns the BAPIL White Paper (Version 1.0) into a buildable plan: institutional design, reference architecture, data and AI design, governance and assurance, a tested reference implementation, a 36-month delivery plan, a strategic roadmap to 2041 and the decisions requested from the relevant authorities. The English edition is authoritative; the Bangla edition is a full translation. A short Blueprint Summary is published in both languages.

This directory holds the editable sources and everything needed to rebuild the publication. It is organised to fit the existing repository: the White Paper sources live in `../reports/` and its PDFs in `../releases/v1.0/`; the Blueprint sources live here and its PDFs in `../releases/v1.1/`.

## 1. Deliverables

| Deliverable | Path | Kind |
|---|---|---|
| Technical Blueprint, Bangla (publication PDF) | `../releases/v1.1/BAPIL_Technical_Blueprint_bn.pdf` | generated |
| Technical Blueprint, English (publication PDF) | `../releases/v1.1/BAPIL_Technical_Blueprint_en.pdf` | generated |
| Blueprint Summary, Bangla and English (PDF) | `../releases/v1.1/BAPIL_Blueprint_Summary_bn.pdf`, `..._en.pdf` | generated |
| Editable master, Bangla | `src/BAPIL_Technical_Blueprint_bn.src.md` with chapters in `src/bn/` | source |
| Editable master, English | `src/BAPIL_Technical_Blueprint_en.src.md` with chapters in `src/en/` | source |
| Assembled Markdown (one file per edition) | `BAPIL_Technical_Blueprint_bn.md`, `BAPIL_Technical_Blueprint_en.md` | generated |
| Table data (72 tables, EN and BN) | `src/tables_a.py` to `src/tables_f.py` | source |
| Tables as LaTeX, PDF, PNG and Markdown | `tables/`, `tables/md/` | generated |
| Figure sources (15 TikZ figures, EN and BN) | `src/make_figures.py`, `src/figures_new.py` | source |
| Figures as TikZ, PDF and PNG | `figures/` | generated |
| Budget model and its data | `src/budget_model.py`; CSV outputs in `data/` | source; generated |
| Bibliography | `src/refs_new.md` (source keys 84 to 168); source keys 1 to 83 are read from `../reports/BAPIL_White_Paper_v1.md`; the documents renumber all references in order of first citation | source |
| Layout templates and configuration | `src/header-*.tex`, `src/blueprint-filter.lua`, `src/metadata.json` | source |
| Quotation-mark convention and check | `src/typography.py` | source |
| Build script | `build_blueprint.sh` | source |
| Manifest with checksums | `MANIFEST.md` (written by `make_manifest.py` at the end of each build) | generated |
| Change log for this release stage | `CHANGES.md` | documentation |
| Quality-assurance report | `QA_REPORT.md` | documentation |
| Source and licence note | `SOURCES_AND_LICENCES.md` | documentation |
| Zenodo metadata draft and checklist | `zenodo/` | documentation |
| Internal review records (not part of the publication) | `review/` | records |

Generated files are committed so that readers can use them without building, but they are never edited by hand: change the sources and rebuild.

## 2. How the sources fit together

```text
src/BAPIL_Technical_Blueprint_bn.src.md      <!-- INCLUDE:bn/00_front.md --> ... <!-- INCLUDE:bn/06_annexes.md -->
  src/bn/00_front.md ... 06_annexes.md        prose, with <!-- TABLE:NN --> and <!-- FIGURE:NN --> markers
src/tables_*.py      --make_tables.py-->      tables/blueprint_tabNN[_bn].{tex,pdf,png} and tables/md/*.md
src/make_figures.py  --(TikZ, XeLaTeX)-->     figures/blueprint_figNN[_bn].{tex,pdf,png}
src/budget_model.py  ---------------->        Tables 49, 50, 61, 62 (via tables_e.py, tables_f.py) and data/*.csv
src/assemble.py      ---------------->        BAPIL_Technical_Blueprint_{en,bn}.md (tables, figures, metadata,
                                               evaluation results, references and Bangla citation numerals filled in)
pandoc + XeLaTeX     ---------------->        ../releases/v1.1/BAPIL_Technical_Blueprint_{en,bn}.pdf
```

`src/metadata.json` holds the title (both languages), version, publication month, author, ORCID, licence, PDF subject and keywords, and the DOIs (`doi` for the Blueprint, `summary_doi` for the Summary). While a DOI is `10.5281/zenodo.PENDING`, the documents print "DOI to be assigned on publication".

## 3. Reproducing the PDFs

### Requirements (versions used for this build)

| Tool | Version used | Notes |
|---|---|---|
| Python | 3.13.16 | 3.10 or newer; standard library only |
| pandoc | 3.1.3 | 3.x |
| XeLaTeX | TeX Live 2023 (XeTeX 3.141592653-2.6-0.999995) | packages: fontspec, babel (Bengali), ucharclasses, newunicodechar, titlesec, tocloft, fancyhdr, caption, xcolor, booktabs, tabularx, xurl, enumitem, tikz |
| poppler | 24.02.0 | `pdftoppm` for PNG previews |
| Fonts | Noto Serif, Noto Sans, Noto Serif Bengali and Noto Sans Bengali 3.000; Latin Modern Roman; TeX Gyre Heros; DejaVu Sans Mono | all under the SIL Open Font License or GUST/Bitstream-Vera-style free licences; not redistributed here (see `SOURCES_AND_LICENCES.md`) |

On Ubuntu 24.04 the following packages provide everything (this is what the GitHub Actions workflow installs):

```bash
sudo apt-get install -y --no-install-recommends pandoc texlive-xetex texlive-latex-extra \
  texlive-fonts-recommended texlive-fonts-extra texlive-pictures lmodern poppler-utils \
  fonts-noto-core fonts-noto-extra fonts-dejavu-core fonts-texgyre
```

The Noto fonts can also be downloaded from Google Fonts or the Noto project on GitHub. Check that `fc-list | grep -i "Noto Serif Bengali"` finds the Bangla font before building.

### Commands

From the repository root:

```bash
blueprint/build_blueprint.sh                 # tables, figures, budget CSV, tests, evaluation, all PDFs
blueprint/build_blueprint.sh --skip-assets   # documents only (tables and figures already built)
blueprint/build_blueprint.sh --only BAPIL_Technical_Blueprint_bn   # one document
```

The full build takes about four minutes. It:

1. generates every table and figure in English and Bangla (`make_tables.py`, `make_figures.py`) and writes the budget CSV files;
2. runs the 49 unit tests of the reference implementation and the demonstration evaluation, whose results are printed in Section 11.5;
3. assembles the Markdown editions (`assemble.py`);
4. checks the quotation-mark convention in all sources (`typography.py --check`); the build stops if a straight quote appears in prose;
5. converts each edition with pandoc and XeLaTeX into `releases/v1.1/`;
6. writes `blueprint/MANIFEST.md` with the size and SHA-256 of every deliverable.

### Export settings

* Pandoc input format `markdown+raw_tex-implicit_figures-smart`; Lua filter `src/blueprint-filter.lua` (parts, numbered captions, lists of figures and tables).
* XeLaTeX with `Ligatures=TeXOff` on the main and sans fonts, so that the PDF contains exactly the characters of the source, and `\XeTeXgenerateactualtext=1`, so that copied or searched Bangla text keeps Unicode order.
* Bangla and Latin fonts switch automatically by Unicode block (`ucharclasses`); typographic quotes and dashes are assigned to the Latin class so that a Bangla word after “ is set in the Bangla font.
* Bangla editions: babel `bengali` with Bangla digits for page numbers, list numbers and footnotes; citation numbers are converted to Bangla digits during assembly.
* PDF metadata (title, author, subject, keywords, language) is taken from `src/metadata.json`. The PDF creation and modification dates are set to the publication month only (`D:202610`), and `SOURCE_DATE_EPOCH` is fixed so that rebuilding unchanged sources gives the same files.

### Optional editable word-processor copy

The Markdown masters are the editable source. If a word-processor copy is needed for review, pandoc can produce one (tables and figures are included as images and Markdown tables; the layout is not the publication layout):

```bash
pandoc blueprint/BAPIL_Technical_Blueprint_bn.md --resource-path=blueprint -o BAPIL_Technical_Blueprint_bn.docx
```

Changes made in such a copy must be carried back into `src/bn/` by hand.

## 4. Editing rules

* **Text:** edit `src/en/*.md` and `src/bn/*.md`. Keep the two editions in step; every number, date, table and figure reference must match.
* **Quotation marks:** use “ ” and ‘ ’ in prose and ’ for the English apostrophe; straight quotes only in code, URLs, JSON and command lines. `python3 src/typography.py --check src/en/*.md src/bn/*.md` reports violations and `--fix` repairs them.
* **Tables:** edit the dictionaries in `src/tables_*.py`; table numbers are the `id` fields. Budget tables are computed by `src/budget_model.py`: change an assumption there, not the printed numbers.
* **Figures:** edit the TikZ in `src/make_figures.py` or `src/figures_new.py`; labels are given separately for each language.
* **References:** add new entries to `src/refs_new.md` in the existing style; only cited references are printed.
* **Metadata and DOIs:** edit `src/metadata.json` (`doi`: Technical Blueprint, now 10.5281/zenodo.23587901; `summary_doi`: Blueprint Summary, now 10.5281/zenodo.23587919) and rebuild.
* **No en or em dashes** in body text; a hyphen is used where a dash is needed (en dashes remain correct in bibliographic page ranges).

## 5. Known limitations of the build

* Bangla line breaking follows XeLaTeX defaults; occasional loose lines remain.
* PDF accessibility has not been evaluated: the PDFs carry searchable text, embedded fonts, a document language and bookmarks, but they are not tagged PDF (PDF/UA).
* The Bangla font has no italic; emphasised Bangla text is set upright.
* The demonstration results in Section 11.5 are recomputed at every build and can change slightly if the corpus documents change.

## 6. Versioning

Document version 1.0 (October 2026). The files are prepared for repository release `v1.1.0`, which has not yet been created; the existing tags are `v1.0` and `v1.0.1`. The Blueprint will receive its own Zenodo record and DOI only after the GitHub release exists (Annex D). See `zenodo/UPLOAD_CHECKLIST.md`.

## 7. Licence

Documents, figures, tables and data: CC BY 4.0. Code (`src/*.py`, `build_blueprint.sh`, headers and filter): MIT. Details and third-party components: `SOURCES_AND_LICENCES.md`.
