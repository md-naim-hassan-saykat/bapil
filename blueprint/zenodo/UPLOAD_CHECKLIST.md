# Release and Zenodo checklist: BAPIL Technical Blueprint, Version 1.0

The Technical Blueprint gets its **own Zenodo record** (like the Executive Summary), linked to the White Paper and Executive Summary records. Annex D of the Blueprint requires that the Zenodo record is **published only after** the GitHub release it refers to exists. Nothing in this list has been done yet.

Keep these concepts apart: document version **1.0**; source revision (a Git commit); Git tag **v1.1.0**; GitHub release **v1.1.0**; Zenodo record and DOI (new, separate from the White Paper and Executive Summary records).

## 1. Reserve the DOI (Zenodo draft, not published)

1. Sign in at <https://zenodo.org> and choose **New upload**.
2. Under *Digital Object Identifier*, choose **Get a DOI now!** Copy the reserved DOI (`10.5281/zenodo.NNNNNNNN`).
3. Save the draft. **Do not publish.**

## 2. Put the DOI into the documents and rebuild

1. In `blueprint/src/metadata.json` set `"doi": "10.5281/zenodo.NNNNNNNN"`.
2. In `blueprint/src/en/00_front.md` and `blueprint/src/bn/00_front.md` nothing needs editing: the DOI is filled in automatically on the title page, document information, citation and Table 1.
3. Rebuild: `blueprint/build_blueprint.sh`, then check the title pages of both PDFs.
4. Update the DOI lines in `README.md`, `CITATION.cff` (if a Blueprint entry is added) and `CHANGELOG.md`.
5. Commit.

## 3. Push, tag and create the GitHub release

1. Push the branch and merge it into `main` (pull request recommended).
2. Tag `v1.1.0` on the merge commit and push the tag.
3. Create the GitHub release **v1.1.0** and attach the four PDFs from `releases/v1.1/`.
4. If Zenodo's GitHub integration is switched on for this repository, the release also creates a new version of the repository's own Zenodo record; that is separate from the Blueprint record and expected.
5. Confirm that the release is listed at <https://github.com/md-naim-hassan-saykat/bapil/releases>.

## 4. Upload the files to the Zenodo draft

Run `blueprint/zenodo/make_zenodo_package.sh` and upload everything in `dist/zenodo/`:

* 4 PDFs: Technical Blueprint and Blueprint Summary, English and Bangla
* 4 Markdown files (assembled editions)
* `BAPIL_Technical_Blueprint_figures.zip` and `BAPIL_Technical_Blueprint_tables.zip`
* `BAPIL_Technical_Blueprint_source.zip` (editable source package)
* `bapil-reference-implementation-0.1.0.zip`
* `SHA256SUMS.txt`

## 5. Metadata (from `zenodo_metadata.json` and `description.html`)

| Field | Value |
|---|---|
| Resource type | Publication / Report |
| Title | Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint |
| Additional title (Bengali) | বাংলাদেশ এআই পলিসি অ্যান্ড ইনোভেশন ল্যাব (BAPIL): টেকনিক্যাল ব্লুপ্রিন্ট |
| Publication date | The day the record is published |
| Creator | Saykat, Md Naim Hassan; ORCID 0009-0007-5270-3970; affiliation as chosen by the author |
| Description | Paste `description.html` |
| Version | 1.0 |
| Languages | English, Bengali |
| Licence | Creative Commons Attribution 4.0 International |
| Keywords | See `zenodo_metadata.json` |
| Related works | *Is supplement to* 10.5281/zenodo.21363967; *References* 10.5281/zenodo.21441172; *Is supplemented by* https://github.com/md-naim-hassan-saykat/bapil/tree/v1.1.0 |

## 6. Publish and check

1. Publish the Zenodo record only after step 3 is complete; confirm that the DOI resolves.
2. Confirm that the related works appear on the record page.
3. Confirm that the PDFs downloaded from Zenodo match `SHA256SUMS.txt`.
