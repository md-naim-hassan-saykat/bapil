# Reports

This directory contains the source files, references, figures, and build resources for the **Bangladesh AI Policy & Innovation Lab (BAPIL) White Paper**.

## Contents

| File/Directory | Description |
|---------------|-------------|
| `BAPIL_White_Paper_v1.md` | English White Paper source (Version 1.0) |
| `BAPIL_White_Paper_v1_bn.md` | Bangla White Paper source (Version 1.0) |
| `references.bib` | Bibliographic references used in the White Paper |
| `figures/` | Figures and graphics used throughout the White Paper |
| `build_bn_pdf.sh` | Build script for generating the Bangla PDF |
| `bangla-pdf-header.tex` | Pandoc/LaTeX header configuration for Bangla PDF generation |
| `bangla-page-numbers.tex` | Bangla page numbering configuration |
| `fix-*.tex` | LaTeX formatting helper files |
| `fix-runin-headings.lua` | Pandoc Lua filter for heading formatting |

## Notes

- The editable source documents are maintained in Markdown format.
- Official released PDF versions are available in the [`../releases/`](../releases/) directory.
- Figures should be stored in the `figures/` directory using the repository's naming convention (for example, `figure01`, `figure02`, ...).
