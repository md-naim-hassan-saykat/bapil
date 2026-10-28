# Release notes: BAPIL repository release v1.1.0

Released on 29 October 2026. The Technical Blueprint (10.5281/zenodo.23587901) and the Blueprint Summary (10.5281/zenodo.23587919) each have their own Zenodo record, deposited from this release. The Decision Memo is attached to this release only.

## Publications in this release

| Title | Version | Languages | Files |
|---|---|---|---|
| Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint | 1.0 (October 2026) | English (authoritative); Bangla: বাংলাদেশ এআই পলিসি অ্যান্ড ইনোভেশন ল্যাব (BAPIL): টেকনিক্যাল ব্লুপ্রিন্ট | `releases/v1.1/BAPIL_Technical_Blueprint_en.pdf`, `..._bn.pdf` |
| Bangladesh AI Policy & Innovation Lab (BAPIL): Blueprint Summary | 1.0 (October 2026) | English, Bangla | `releases/v1.1/BAPIL_Blueprint_Summary_en.pdf`, `..._bn.pdf` |
| Decision Memo: A 12-Month Pilot of an AI Policy-Intelligence Capability for Bangladesh | October 2026 | English, Bangla | `releases/v1.1/BAPIL_Decision_Memo_en.pdf`, `..._bn.pdf` (a separate document, not part of the Blueprint) |
| Reference implementation `bapil` | 0.1.0 | Python | `implementation/` |

## Scope

The Technical Blueprint turns the BAPIL White Paper (Version 1.0) into a buildable plan: institutional design, reference architecture, data and AI design, governance and assurance, a tested reference implementation, a 36-month delivery plan with an indicative budget, a strategic roadmap to 2041 and six decisions requested from the authorities. Five parts, 21 chapters, 23 annexes, 72 tables and 16 figures.

BAPIL is a proposal. No institution has been established, no governance body constituted and no funding approved; all quality thresholds are proposed targets.

## Main contents and changes since v1.0.1

* New: Technical Blueprint, Blueprint Summary and Decision Memo in English and Bangla, with editable sources, tables and figures in LaTeX, PDF and PNG, a budget model with CSV outputs and an editable workbook, and one build script.
* New: reference implementation 0.1.0 (bilingual search, cited extractive answers with abstention, risk tiers, AI system register, evaluation metrics, audit log), 49 unit tests, JSON Schemas and examples.
* New: repository documentation (`CONTRIBUTING.md`, `REPRODUCIBILITY.md`, `DATA_AND_METHODOLOGY.md`, `docs/`), security policy and GitHub Actions workflows.
* The White Paper and Executive Summary (v1.0) are unchanged.

Full details: [`CHANGELOG.md`](CHANGELOG.md) and [`blueprint/CHANGES.md`](blueprint/CHANGES.md).

## Known limitations

* The numbers and Gazette dates of the 2026 data-protection, data-management and cyber-security Acts are confirmed from official sources; their provisions were read through the laws database texts and need confirmation by qualified Bangladesh counsel (planned in Phase 0). The draft national AI policy is described from press reports.
* The budget is a planning estimate: Tk 20.43 crore (base), Tk 22.24 crore (adjusted, with known omissions and 10% contingency), Tk 17.93 to 25.25 crore (low and high scenarios). A conditional national scale-up for Years 4 to 8 (about Tk 218.9 crore, about 118 direct posts by Year 8) is shown in Annex W but not requested. No funding is approved or committed.
* The BanglaPolicyQA benchmark does not exist yet; the demonstration evaluation (Recall@10 0.92 on 24 questions at the latest build; it changes as the documents change) is a development result only.
* The reference implementation is a research prototype, tested only on Linux. The unit tests pass locally; the CI workflows run for the first time when the release branch is pushed.
* The Bangla edition has had a systematic editorial pass (`blueprint/review/BANGLA_EDITORIAL_LOG.md`) but not an independent professional copy-edit.
* Unit costs were checked against published prices and pay data, but no quotations or host salary scale exist yet (Annex V, U6).
* The PDFs are not tagged for accessibility.
* Open items are listed in Blueprint Annex V (Table 68).

## Source package and reproducibility

Everything needed to rebuild the PDFs is in `blueprint/` (sources, table data, figure sources, budget model, templates, build script) together with `reports/BAPIL_White_Paper_v1.md` (references 1 to 83). `blueprint/build_blueprint.sh` rebuilds all outputs in about four minutes on Ubuntu 24.04 with pandoc 3.1.3 and TeX Live 2023; see [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md).

## Citation

Please cite the publications:

> Saykat, M. N. H. (2026). *Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint* (Version 1.0). Zenodo. https://doi.org/10.5281/zenodo.23587901
>
> Saykat, M. N. H. (2026). *Bangladesh AI Policy & Innovation Lab (BAPIL): Blueprint Summary* (Version 1.0). Zenodo. https://doi.org/10.5281/zenodo.23587919
