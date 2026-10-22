# Contributing to BAPIL

Thank you for helping to improve BAPIL. This is an independent research project maintained by one author. There is no formal review board yet; contributions are reviewed by the author as time allows, and no response time is promised. The governance bodies described in the Technical Blueprint are proposals and do not review contributions.

## Ways to contribute

| You want to | Do this |
|---|---|
| Report a factual error | Open an issue with the document, page or section, the statement, what is wrong, and a source (link and access date) |
| Correct a legal reference | As above, citing the gazetted text, an official source or a named legal commentary, with the act number and section where possible. Say whether the provision is in force. Corrections are applied to the English and Bangla editions together |
| Propose an improvement | Open an issue describing the problem and the change; for larger changes, discuss before writing a pull request |
| Submit a technical change | Pull request with tests (`cd implementation && python3 -m unittest discover -s tests`); standard library only unless a dependency is agreed |
| Improve the Bangla translation | Pull request against `blueprint/src/bn/` (and `tables_*.py` for tables), keeping numbers, dates, legal citations and thresholds unchanged unless the English source changes too. Use the terms in [`docs/source-of-truth.md`](docs/source-of-truth.md#8-bilingual-terminology-register) |
| Report an accessibility or rendering problem | Open an issue with the file, page, the viewer and version you used, and a screenshot if possible |
| Report a security vulnerability | Follow [`SECURITY.md`](SECURITY.md); do not open a public issue |

## Editing the publications

* Edit the **sources**, never the generated files: `blueprint/src/en/`, `blueprint/src/bn/`, `blueprint/src/*.src.md`, `blueprint/src/tables_*.py`, `blueprint/src/make_figures.py`, `blueprint/src/budget_model.py`, `blueprint/src/refs_new.md` and `blueprint/src/metadata.json`.
* Rebuild with `blueprint/build_blueprint.sh` (see [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md)) and commit the regenerated files with the source change.
* Keep the two editions factually identical. The English edition is authoritative; if you change a fact, change it in both.
* Change budget figures only through assumptions in `budget_model.py`; never type a total by hand.
* The published White Paper and Executive Summary (`reports/`, `releases/v1.0/`) have DOIs and are not edited; report problems in them as issues.

## Evidence and citation standards

* Every factual claim needs a source with a URL (where one exists) and an access date, in the existing bibliography style (`blueprint/src/refs_new.md`).
* Prefer official sources; label press reports and commentary as reported; say so when sources disagree.
* Keep proposals, targets and estimates clearly distinguished from facts and measured results. Do not describe anything as established, approved, funded, released or measured without evidence.
* Use “ ” and ‘ ’ in prose and ’ for the English apostrophe; straight quotes only in code. The build checks this.
* Do not use en or em dashes in body text.

## Licences of contributions

By contributing you agree that code is licensed under the MIT License (`LICENSE`) and documentation, tables, figures and data under CC BY 4.0, as described in [`docs/licensing-and-asset-rights.md`](docs/licensing-and-asset-rights.md). Do not submit material you do not have the right to share, personal data or credentials.
