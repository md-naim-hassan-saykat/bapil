# Zenodo upload checklist: BAPIL Technical Blueprint v1.0

The Blueprint gets its **own Zenodo record** (like the Executive Summary), linked to the White Paper and Executive Summary records.

## 1. Reserve the DOI (before building the final PDFs)

1. Sign in at <https://zenodo.org> and choose **New upload**.
2. Under *Digital Object Identifier*, choose **Get a DOI now!** (reserve DOI). Copy the DOI, for example `10.5281/zenodo.NNNNNNNN`.
3. Save the draft. Do not publish yet.

## 2. Put the DOI into the documents

1. Edit `blueprint/src/metadata.json` and set `"doi": "10.5281/zenodo.NNNNNNNN"`.
2. Rebuild: `blueprint/build_blueprint.sh` (the DOI appears on the title pages, document information, citation, Table 1 and the Decision Memo).
3. Package: `blueprint/zenodo/make_zenodo_package.sh` (creates `dist/zenodo/`).

## 3. Upload files (from `dist/zenodo/`)

* 6 PDFs: Technical Blueprint, Blueprint Summary, Decision Memo (English and Bangla)
* 6 Markdown sources
* `BAPIL_Blueprint_v1_figures.zip` and `BAPIL_Blueprint_v1_tables.zip` (LaTeX, PDF, PNG; English and Bangla)
* `bapil-reference-implementation-0.1.0.zip`
* `SHA256SUMS.txt`

## 4. Metadata (copy from `zenodo_metadata.json` and `description.html`)

| Field | Value |
|---|---|
| Resource type | Publication / Report |
| Title | Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint |
| Publication date | Date of publication |
| Creator | Saykat, Md Naim Hassan; ORCID 0009-0007-5270-3970; affiliation as chosen |
| Description | Paste `description.html` |
| Version | 1.0 |
| Languages | English, Bengali |
| Licence | Creative Commons Attribution 4.0 International |
| Keywords | See `zenodo_metadata.json` |
| Related works | *Is supplement to* 10.5281/zenodo.21363967; *References* 10.5281/zenodo.21441172; *Is supplemented by* https://github.com/md-naim-hassan-saykat/bapil/tree/v1.1.0 |

## 5. GitHub release

Tag `v1.1.0` on GitHub with the six PDFs attached. If Zenodo's GitHub integration is switched on for this repository, a release also creates a new *version* of the repository's own Zenodo record; that is separate from the Blueprint record above and is expected.

## 6. Publish and check

1. Publish the Zenodo record; confirm the DOI resolves.
2. Confirm the related works appear on the record page.
3. Update the README DOI table if anything changed.
