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

Prepared for repository release v1.1.0. The tag, the GitHub release and the Blueprint's Zenodo DOI have not been created yet; the release date will be added when the release is published.

### Added

- **Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint**, Version 1.0 (October 2026), in English (authoritative) and Bangla (বাংলাদেশ এআই পলিসি অ্যান্ড ইনোভেশন ল্যাব (BAPIL): টেকনিক্যাল ব্লুপ্রিন্ট): five parts, 21 chapters, 23 annexes, 72 tables and 16 figures. PDFs: `releases/v1.1/BAPIL_Technical_Blueprint_en.pdf` and `releases/v1.1/BAPIL_Technical_Blueprint_bn.pdf`.
- Blueprint Summary, Version 1.0, in English and Bangla (`releases/v1.1/BAPIL_Blueprint_Summary_en.pdf`, `..._bn.pdf`).
- Decision Memo to the authorities, in English and Bangla (`releases/v1.1/BAPIL_Decision_Memo_en.pdf`, `..._bn.pdf`), a separate document that is not part of the Blueprint.
- Editable source package in `blueprint/`: Markdown masters, table data, TikZ figure sources, the budget model with CSV outputs and an editable workbook with formulas (`blueprint/data/BAPIL_Budget_Model.xlsx`), LaTeX headers, Pandoc filter, metadata and one build script.
- Sixteen figures and seventy-two tables as LaTeX, PDF and PNG (and Markdown for tables), in English and Bangla.
- Reference implementation (`implementation/`, version 0.1.0): Bangla normalisation, bilingual BM25 search, cited extractive answers with abstention, risk tiers, AI system register and transparency export, evaluation metrics, hash-chained audit log, CLI and JSON API, with 49 unit tests (run locally; no public CI record yet).
- JSON Schemas for policy-document metadata, AI system records and risk questionnaires; example records for pilots P1 to P6.
- Bilingual demonstration question set and evaluation report (development results only).
- GitHub Actions workflows for tests and for rebuilding the Blueprint PDFs (not yet run on GitHub).
- Zenodo metadata draft, description and GitHub-to-Zenodo release checklist for the Blueprint record.
- Security policy (`SECURITY.md`).
- Internal review records in `blueprint/review/` (earlier audit and adversarial review, change record, October 2026 project audit, cross-document reconciliation, Markdown validation); these are not part of the publication.
- Annex W of the Blueprint (Tables 69 and 70): jobs and skills created by the 36-month plan, and a costed, conditional national scale-up for Years 4 to 8 (about Tk 218.9 crore; about 118 direct posts by Year 8), shown for information and not requested; summarised in Section 17.3, the front matter, the Summary and the Decision Memo.
- References numbered in order of first citation in every document (previously the White Paper numbers 1 to 83 were kept, so the list jumped, for example from 1 to 4); entries from the White Paper bibliography are marked with a dagger; `blueprint/review/REFERENCE_NUMBERS.md` maps the new numbers to the source keys.

### Corrected

- Personal data: the Blueprint and Summary no longer say that the data-protection framework simply "requires consent"; consent is described as the principal basis, with other grounds and broad exemptions, and BAPIL's consent rule is labelled as its own safeguard.
- Cyber security: the June 2026 amendment is no longer described as an amendment on AI-generated content; the passage date is given and the disagreement between sources is disclosed, with the further draft amendment under review from July 2026.
- National AI policy: the revised draft version 2.0 (9 February 2026) is recorded, so that the drafting announced for the fourth quarter of 2026 is not presented as a first draft.
- Institutional status: remaining present-tense descriptions of BAPIL as established were made conditional.
- Bangla terminology: "মানবিক তত্ত্বাবধান" (humane supervision) corrected to "মানব-তত্ত্বাবধান" (human oversight) throughout.
- Table 60 now quotes the current demonstration result (Recall@10 0.88); the build stops if they diverge.
- White Paper reference [38] is cited in the Blueprint with the correct co-author (A. Piktus); the White Paper source is unchanged.

### Documentation

- `README.md`: verified project status, Decision Memo, documentation index, repository structure, licensing of documents versus code, release status and the Zenodo GitHub integration decision.
- New: `CONTRIBUTING.md`, `REPRODUCIBILITY.md`, `DATA_AND_METHODOLOGY.md`, `RELEASE_NOTES.md` (draft) and `docs/` (overview, inventory, architecture, governance, evaluation, legal references, financial model, licensing and asset rights, publication and archiving, source-of-truth register with bilingual terminology).
- `reports/README.md`: missing closing backtick in the build-script entry.

### Build and reproducibility

- One script (`blueprint/build_blueprint.sh`) regenerates tables, figures, budget CSV, assembled Markdown and all six PDFs; fixed PDF dates and `SOURCE_DATE_EPOCH`; quotation-mark check on every build.
- The demonstration evaluation corpus is restricted to the White Paper, Executive Summary, Blueprint and Summary.

### Unchanged

- The White Paper and Executive Summary (Version 1.0), their sources and `releases/v1.0/`.

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
