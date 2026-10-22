# Licensing and asset rights

The repository `LICENSE` (MIT) covers the **software**. It does not automatically cover the publications, data or third-party material. This page records what applies to each kind of file, where the evidence is, and which decisions the author still has to confirm before release v1.1.0. It is not legal advice.

## 1. What applies to what

| Content | Licence | Evidence | Status |
|---|---|---|---|
| Software: `implementation/`, `blueprint/src/*.py`, `blueprint/build_blueprint.sh`, `blueprint/make_manifest.py`, LaTeX headers, Lua filter, `reports/*.sh`, `.github/` | MIT | `LICENSE`; `implementation/pyproject.toml` | Verified |
| White Paper v1.0 (EN, BN) | CC BY 4.0, as stated in the document | `reports/BAPIL_White_Paper_v1.md`, "Copyright & License" | Stated in the document. **Discrepancy:** its Zenodo record (10.5281/zenodo.21363967) lists the MIT License, because it was archived from a GitHub release |
| Executive Summary v1.0 (EN, BN) | CC BY 4.0 | Document; Zenodo record 10.5281/zenodo.21441172 | Verified (document and record agree) |
| Technical Blueprint, Blueprint Summary and Decision Memo (texts, PDFs, assembled Markdown) | CC BY 4.0, as printed in the documents | `blueprint/src/metadata.json`; copyright pages | Stated; **author to confirm before release** |
| Blueprint tables and figures (`blueprint/tables/`, `blueprint/figures/`) | CC BY 4.0 | `blueprint/SOURCES_AND_LICENCES.md` | Original TikZ drawings and tables by the author; no third-party images |
| Budget data and workbook (`blueprint/data/`) | CC BY 4.0 | `blueprint/SOURCES_AND_LICENCES.md` | Generated from the author’s assumptions |
| White Paper figures (`reports/figures/`) | As the White Paper (CC BY 4.0) | White Paper | Created for the White Paper; not re-examined in this audit |
| Research studies (`research/`) | Not stated in the files | None | **To confirm.** Without a statement, readers may assume the MIT licence of the repository applies, which is unsuitable for prose; recommend stating CC BY 4.0 if the author agrees |
| Demonstration questions (`implementation/benchmarks/demo_questions.json`) | CC BY 4.0 (declared in the file) | File header | Verified |
| Planned BanglaPolicyQA benchmark | CC BY 4.0 with source attribution (planned) | Blueprint Annex K | Not yet created |

## 2. Third-party material

| Material | How it is used | Rights position |
|---|---|---|
| Government documents (laws, gazettes, budgets, plans) | Cited; future P0 corpus | Reuse terms differ and are not always stated; written confirmation from custodians is a precondition (Decision D3; unresolved item U3) |
| Press reports and commentary | Cited with URLs and access dates | Facts and titles only; no substantial text reproduced |
| Fonts (Noto family, Latin Modern, TeX Gyre Heros, DejaVu Sans Mono) | Embedded as subsets in the PDFs | SIL OFL 1.1, GUST and Bitstream Vera-derived licences allow embedding; the fonts are not redistributed |
| Build tools (pandoc, TeX Live, poppler, Python) | Used, not distributed | Their own licences |

No logos, photographs, maps or other third-party images are included in the Blueprint package.

## 3. Decisions for the author before release

1. Confirm CC BY 4.0 for the Blueprint, Summary, Decision Memo, tables, figures and data.
2. Decide whether to correct the licence shown on the White Paper’s Zenodo record (MIT) to the CC BY 4.0 stated in the document. Editing a record’s metadata on Zenodo does not change its DOI.
3. Decide the licence for `research/` and add a statement to those files or to `research/README.md`.
4. Keep `LICENSE` as MIT for software, and keep the statement in the README that documents are licensed separately.
