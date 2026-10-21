# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows Semantic Versioning where applicable.

---

## [Unreleased]

### Planned

- BanglaPolicyQA benchmark (version 0)
- Additional international AI governance studies
- Pilot P1 (Bangladesh Policy Search Engine) alpha

---

## [1.1.0] - Unreleased (prepared October 2026)

Prepared for repository release v1.1.0. The tag, the GitHub release and the Blueprint's Zenodo DOI have not been created yet.

### Added

- **Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint**, Version 1.0 (October 2026), in Bangla (বাংলাদেশ এআই পলিসি অ্যান্ড ইনোভেশন ল্যাব (BAPIL): টেকনিক্যাল ব্লুপ্রিন্ট) and English: five parts, 21 chapters, 22 annexes, 68 tables and 15 figures, including an indicative 36-month budget with scenarios, a strategic roadmap for 2026 to 2041 and beyond, and annexes on evidence status, budget reconciliation, evaluation protocol, governance status, preconditions, risk monitoring and unresolved items. PDFs: `releases/v1.1/BAPIL_Technical_Blueprint_bn.pdf` and `releases/v1.1/BAPIL_Technical_Blueprint_en.pdf`.
- Blueprint Summary, Version 1.0, in Bangla and English (`releases/v1.1/BAPIL_Blueprint_Summary_bn.pdf`, `..._en.pdf`).
- Editable source package in `blueprint/`: Markdown masters (`src/en/`, `src/bn/`), table data (`src/tables_*.py`), TikZ figure sources, the budget model with CSV outputs (`blueprint/data/`), LaTeX headers, Pandoc filter, metadata and a single build script, with a reproduction guide (`blueprint/README.md`), manifest with checksums, change log, quality-assurance report and source and licence note.
- Fifteen figures and sixty-eight tables as LaTeX, PDF and PNG (and Markdown for tables), in Bangla and English.
- Quotation-mark convention and check for all Blueprint sources (`blueprint/src/typography.py`), run on every build.
- Internal pre-publication review records in `blueprint/review/` (audit and revision report, adversarial review, change record); these are not part of the publication.
- Security policy (`SECURITY.md`).
- Reference implementation (`implementation/`, version 0.1.0): Bangla normalisation, bilingual BM25 search, cited extractive answers with abstention, risk tiers, AI system register and transparency export, evaluation metrics, hash-chained audit log, CLI and JSON API, with 49 unit tests (run locally on Python 3.10 to 3.13, Linux).
- JSON Schemas for policy-document metadata, AI system records and risk questionnaires; example records for pilots P1 to P6.
- Bilingual demonstration question set and evaluation report.
- GitHub Actions workflows for tests and for rebuilding the Blueprint PDFs.
- Zenodo metadata draft, description and release checklist for the Blueprint record.

### Changed

- README: Technical Blueprint section (titles in both languages, publication PDFs, editable sources, rebuild instructions, known limitations), versioning and release status, updated repository structure; the DOI badge points to the concept DOI image and link consistently.
- Research roadmap and project status updated.

### Fixed

- `reports/README.md`: missing closing backtick in the build-script entry.
- White Paper reference [38] is cited in the Blueprint with the correct co-author (A. Piktus); the White Paper source is unchanged.

---

## [1.0] - 2026-07-21

### Added

- Initial public release of the BAPIL repository.
- English White Paper (Version 1.0).
- Bangla White Paper (Version 1.0).
- English Executive Summary (Version 1.0).
- Bangla Executive Summary (Version 1.0).
- Zenodo DOI for the White Paper.
- Zenodo DOI for the Executive Summary.
- International AI governance research studies.
- Citation metadata (`CITATION.cff`).
- MIT License (`LICENSE`).
- Project documentation (`README.md`).
- Release documentation (`releases/README.md`).
- White Paper release package.
- Executive Summary release package.
- Figure assets for the White Paper.
- PDF build scripts and LaTeX configuration files.

### Changed

- Repository reorganized into a structured research project.
- Figure filenames standardized using leading zeros (`figure01`, `figure02`, ...).
- Repository documentation expanded and reorganized for improved consistency and navigation.
- Release directory updated to include standalone Executive Summary publications.

### Fixed

- Bangla White Paper PDF formatting and heading spacing.
- Bangla White Paper table of contents generation.
- Executive Summary PDF pagination and layout.
- Bangla Executive Summary figure caption rendering.
- Figure references and PDF generation workflow.
