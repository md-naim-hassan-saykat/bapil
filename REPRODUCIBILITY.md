# Reproducibility

How to rebuild the BAPIL Technical Blueprint and Blueprint Summary from source, and what has and has not been tested. Details of the build internals are in [`blueprint/README.md`](blueprint/README.md).

## 1. Tested environment

Every command marked **tested** below was run on 22 October 2026 in this environment:

| Component | Version |
|---|---|
| Operating system | Ubuntu 24.04.5 LTS (Linux, x86-64) |
| Python | 3.13.16 (standard library only for the build and the reference implementation) |
| pandoc | 3.1.3 |
| XeLaTeX | XeTeX 3.141592653-2.6-0.999995 (TeX Live 2023, Debian packages) |
| poppler | 24.02.0 (`pdftoppm`, `pdffonts`, `pdfinfo`) |
| Fonts | Noto Serif, Noto Sans, Noto Serif Bengali, Noto Sans Bengali; Latin Modern Roman; TeX Gyre Heros; DejaVu Sans Mono |
| Optional: LibreOffice | 24.2.7.2 (only to recalculate the budget workbook) |
| Optional: openpyxl | 3.1.5 (only to write the budget workbook) |

Not tested: macOS, Windows, other Linux distributions, other pandoc or TeX Live versions. The reference implementation’s unit tests were also run earlier on Python 3.10, 3.11 and 3.12 (Linux); one optional schema test is skipped there when `jsonschema` is not installed.

## 2. Install the dependencies (Ubuntu 24.04)

```bash
sudo apt-get install -y --no-install-recommends pandoc texlive-xetex texlive-latex-extra \
  texlive-fonts-recommended texlive-fonts-extra texlive-pictures lmodern poppler-utils \
  fonts-noto-core fonts-noto-extra fonts-dejavu-core fonts-texgyre
fc-list | grep -i "Noto Serif Bengali"     # must print at least one font
```

This is the package list used by the GitHub Actions workflow `build-blueprint.yml`. The workflow itself has **not yet run on GitHub** (the branch has not been pushed), so the package list is tested only in the environment above.

## 3. Build

From the repository root:

| Command | What it does | Tested |
|---|---|---|
| `blueprint/build_blueprint.sh` | Tables, figures, budget CSV, unit tests, demonstration evaluation, assembly, quotation-mark check, the four PDFs, manifest (about 4 minutes) | Yes |
| `blueprint/build_blueprint.sh --skip-assets` | Documents only, using existing tables and figures | Yes (earlier in October 2026) |
| `blueprint/build_blueprint.sh --only BAPIL_Technical_Blueprint_bn` | One document | Yes (earlier in October 2026) |
| `cd implementation && python3 -m unittest discover -s tests` | 49 unit tests | Yes: 49 pass (Python 3.13) |
| `python3 blueprint/src/typography.py --check blueprint/src/en/*.md blueprint/src/bn/*.md blueprint/src/*.src.md blueprint/src/refs_new.md` | Quotation-mark convention | Yes |
| `python3 blueprint/src/make_budget_workbook.py blueprint/data/BAPIL_Budget_Model.xlsx` then recalculate in LibreOffice, then `python3 blueprint/src/make_budget_workbook.py --check blueprint/data/BAPIL_Budget_Model.xlsx` | Writes the budget workbook and compares it with the Python model | Yes (differences larger than Tk 1: none) |
| `blueprint/zenodo/make_zenodo_package.sh` | Collects the files for the two Zenodo records into `dist/zenodo/` (Technical Blueprint, 10.5281/zenodo.23587901) and `dist/zenodo-summary/` (Blueprint Summary, 10.5281/zenodo.23587919), each with SHA-256 checksums | Yes |
| `pandoc blueprint/BAPIL_Technical_Blueprint_bn.md --resource-path=blueprint -o out.docx` | Optional word-processor copy for review | Not tested in this audit |

## 4. Expected outputs

| Output | Location |
|---|---|
| Technical Blueprint, EN and BN | `releases/v1.1/BAPIL_Technical_Blueprint_en.pdf`, `..._bn.pdf` |
| Blueprint Summary, EN and BN | `releases/v1.1/BAPIL_Blueprint_Summary_en.pdf`, `..._bn.pdf` |
| Assembled Markdown | `blueprint/BAPIL_*_{en,bn}.md` |
| Tables and figures | `blueprint/tables/`, `blueprint/tables/md/`, `blueprint/figures/` |
| Budget CSV | `blueprint/data/budget_*.csv` |
| Manifest with checksums | `blueprint/MANIFEST.md` |

## 5. How reproducible the outputs are

A clean-clone rebuild of commit `085dea3` (22 October 2026, after the corrections of the project-wide audit) produced byte-identical tables, figures, CSV files and assembled Markdown. The PDFs were identical byte for byte except for the 16-byte file identifier, which XeTeX derives from pandoc’s randomly named temporary directory. PDF creation and modification dates are fixed to the publication month (`D:202610`) and `SOURCE_DATE_EPOCH` is fixed in `blueprint/src/metadata.json`.

The Zenodo source archive was tested the same way: `BAPIL_Technical_Blueprint_source.zip` and `bapil-reference-implementation-0.1.0.zip` unzipped together into an empty directory rebuild the PDFs, identical apart from the file identifier.

Two things are recomputed on every build and change when the documents change: the demonstration evaluation in Section 11.5 (the build stops if Table 60 no longer quotes the current Recall@10) and the manifest checksums.

## 6. Validation after a build

1. `pdffonts` on each PDF: every font embedded.
2. Look at the rendered pages (for example `pdftoppm -r 50 -png`), especially Bangla pages, tables and figures.
3. Check that the build log shows no missing-character warnings.
4. Check the PDF metadata with `pdfinfo` (title, author, dates `D:202610`).
5. Compare the numbers between the English and Bangla editions (the build does not do this automatically).

## 7. Known limitations

* The PDFs are not tagged PDF (no PDF/UA claim); accessibility has not been fully evaluated.
* Bangla line breaking follows XeLaTeX defaults; some loose lines remain.
* The Bangla font has no italic; emphasised Bangla text is set upright.
* The budget workbook’s cached values come from LibreOffice; the workbook is not regenerated by the main build.
