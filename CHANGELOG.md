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

## [1.1.0] - 2026-10

### Added

- BAPIL Technical Blueprint, Version 1.0, in English and Bangla (`blueprint/`, PDFs in `releases/v1.1/`): five parts, 21 chapters and 22 annexes, including an indicative 36-month budget with scenarios, a strategic roadmap for 2026 to 2041 and beyond, and annexes on evidence status, evaluation protocol, governance status, preconditions, risk monitoring, revision history and unresolved items.
- Blueprint Summary, Version 1.0, in English and Bangla.
- One-page Decision Memo for ministries and relevant authorities, in English and Bangla.
- Fifteen Blueprint figures as TikZ (LaTeX), PDF and PNG, each in English and Bangla.
- Sixty-nine Blueprint tables as standalone LaTeX, PDF, PNG and Markdown, each in English and Bangla.
- Single-source build system for the Blueprint (`blueprint/build_blueprint.sh`, table and figure generators, Pandoc filter, XeLaTeX headers with automatic Bangla and Latin font switching, and Bangla numerals for page numbers, list numbers and citations in the Bangla editions).
- Audit and Revision Report for the Blueprint (`blueprint/review/`): issue register, claim verification, budget reconciliation, quality scores and publication checklist.
- Security policy (`SECURITY.md`).
- Reference implementation (`implementation/`, version 0.1.0): Bangla normalisation, bilingual BM25 search, cited extractive answers with abstention, risk tiers, AI system register and transparency export, evaluation metrics, hash-chained audit log, CLI and JSON API, with 49 unit tests.
- JSON Schemas for policy-document metadata, AI system records and risk questionnaires; example records for pilots P1 to P6.
- Bilingual demonstration question set and evaluation report.
- GitHub Actions workflows for tests and for rebuilding the Blueprint PDFs.
- Zenodo metadata, description and upload checklist for the Blueprint record.

### Changed

- README: Technical Blueprint and reference implementation sections, updated repository structure, DOI badge now points to the concept DOI image and link consistently.
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
