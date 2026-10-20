# BAPIL Technical Blueprint (Version 1.0)

This directory contains the **BAPIL Technical Blueprint**, which turns the BAPIL White Paper (Version 1.0) into a buildable plan: institutional design, reference architecture, data and AI design, governance and assurance, a tested reference implementation, a 36-month roadmap and the decisions requested from the relevant authorities.

## Publications

| File | Language | Description |
|---|---|---|
| `BAPIL_Technical_Blueprint_v1.md` | English | Full Technical Blueprint (authoritative edition) |
| `BAPIL_Technical_Blueprint_v1_bn.md` | Bangla | Full Technical Blueprint |
| `BAPIL_Blueprint_Summary_v1.md` | English | Blueprint Summary |
| `BAPIL_Blueprint_Summary_v1_bn.md` | Bangla | Blueprint Summary |
| `BAPIL_Decision_Memo_v1.md` | English | One-page Decision Memo for ministries and relevant authorities |
| `BAPIL_Decision_Memo_v1_bn.md` | Bangla | One-page Decision Memo |

The PDF editions are in [`../releases/v1.1/`](../releases/v1.1/). The Markdown files above are **generated** from the sources in `src/`; edit the sources, not the generated files.

## Figures and tables

Every figure and table is published in three formats, in English and Bangla:

| Directory | Contents |
|---|---|
| `figures/` | `blueprint_figNN.tex` (TikZ source), `.pdf` (vector), `.png` (300 dpi); `_bn` suffix for Bangla |
| `tables/` | `blueprint_tabNN.tex` (standalone LaTeX), `.pdf` (vector), `.png` (220 dpi); `_bn` suffix for Bangla |
| `tables/md/` | Markdown versions used inside the documents |

Fifteen figures: document family, stakeholder map, governance model, reference architecture, request sequence, data lifecycle, retrieval pipeline, foundation-model path, deployment zones, risk-tier flow, lifecycle gates, 36-month roadmap, strategic roadmap 2026 to 2041 and beyond, theory of change and risk heat map. Fifty-nine tables, from the document family (Table 1) to the risk-tier questionnaire (Table 59).

## Sources

| File | Purpose |
|---|---|
| `src/*.src.md` | Document sources with `<!-- TABLE:NN -->`, `<!-- FIGURE:NN -->` and `<!-- INCLUDE:file -->` markers |
| `src/en/`, `src/bn/` | The Technical Blueprint in parts (front matter, Parts I to V, annexes), English and Bangla |
| `src/tables_a.py` to `src/tables_e.py` | Single source for all tables (English and Bangla); `make_tables.py` maps the first-edition numbers to the final numbering |
| `src/figures_new.py` | TikZ sources of the figures added in the expanded edition |
| `src/budget_model.py` | Indicative 36-month budget model behind Tables 49 and 50 |
| `src/make_tables.py` | Generates table `.tex`, `.pdf`, `.png` and Markdown |
| `src/make_figures.py` | Generates TikZ figures and compiles them to `.pdf` and `.png` |
| `src/assemble.py` | Fills tables, figures, metadata, evaluation results and references into the final Markdown |
| `src/metadata.json` | Title, version, author, ORCID and **DOI** (set the reserved DOI here) |
| `src/refs_new.md` | References added by the Blueprint ([84] onwards); [1] to [83] are taken from the White Paper |
| `src/blueprint-filter.lua` | Pandoc filter: vector figures, numbered captions, table of contents |
| `src/header-*.tex` | XeLaTeX headers (shared, English, Bangla, memo) |
| `zenodo/` | Zenodo metadata, description and upload checklist |

## Building

```bash
blueprint/build_blueprint.sh                # everything: tables, figures, tests, evaluation, PDFs
blueprint/build_blueprint.sh --skip-assets  # documents only
blueprint/build_blueprint.sh --only BAPIL_Decision_Memo_v1
```

Requirements: Python 3.10+, pandoc 3.x, XeLaTeX (TeX Live), poppler (`pdftoppm`), and the fonts Latin Modern, TeX Gyre Heros, Noto Serif, Noto Sans, Noto Serif Bengali, Noto Sans Bengali and DejaVu Sans Mono. The build works on Linux and macOS; the GitHub Actions workflow `build-blueprint.yml` runs it on Ubuntu.

## Licence

Documents, figures and tables: CC BY 4.0. Code in `src/`: MIT.
