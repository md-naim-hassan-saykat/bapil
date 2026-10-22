# GitHub-to-Zenodo release checklist: BAPIL Technical Blueprint, Version 1.0

Nothing in this list has been done yet. Each step is to be carried out by the author, or by someone the author authorises, with their own GitHub and Zenodo accounts. No credential is needed in any file of this repository.

Keep these concepts apart: document version **1.0**; source revision (a Git commit); Git tag **v1.1.0**; GitHub release **v1.1.0**; the Blueprint’s Zenodo record and DOI (new, separate from the White Paper and Executive Summary records). Blueprint Annex D requires that the Zenodo record is **published only after** the GitHub release it refers to exists.

## 0. Decide before anything is pushed

| Decision | Options | Recommendation |
|---|---|---|
| Licence of the Blueprint, Summary, Memo, tables, figures and data | CC BY 4.0 (as printed) or another licence | Confirm CC BY 4.0 (consistent with the Executive Summary record) |
| Affiliation in the metadata | Blueprint, `metadata.json` and `zenodo_metadata.json`: "Independent Researcher, Bangladesh" (chosen by the author). `CITATION.cff` and README author section: "Université Paris-Saclay" | Decide whether `CITATION.cff` and the README adopt the Blueprint affiliation for v1.1.0, so that GitHub, CFF and Zenodo agree |
| Zenodo GitHub integration for this repository | The earlier White Paper record (10.5281/zenodo.21363967) was archived from GitHub release v1.0.1, so the integration was switched on at that time. If it is still on, publishing GitHub release v1.1.0 will automatically create a **new version under the concept DOI 10.5281/zenodo.21360565** (which today resolves to the White Paper), with metadata taken from `CITATION.cff` (a `.zenodo.json` file would take precedence; the repository has none) | **Option A (recommended):** switch the repository off at <https://zenodo.org/account/settings/github/> before publishing the release, and create the Blueprint record manually (sections 1 to 6). **Option B:** leave it on, accept that the concept DOI then points to a repository snapshot, and set `version: "1.1.0"` and `date-released` in `CITATION.cff` in the commit that will be tagged, so that the automatic record is not labelled 1.0 |
| Include the Decision Memo in the Zenodo record | Yes or no | No by default: it is a separate document addressed to the authorities. It is attached to the GitHub release either way |

## 1. Reserve the DOI (Zenodo draft, not published)

1. Sign in at <https://zenodo.org> and choose **New upload**.
2. Under *Digital Object Identifier*, choose **Get a DOI now!** Copy the reserved DOI (`10.5281/zenodo.NNNNNNNN`).
3. Save the draft. **Do not publish.** A reserved DOI is not registered until the record is published.

## 2. Put the DOI into the documents and rebuild

1. In `blueprint/src/metadata.json` set `"doi": "10.5281/zenodo.NNNNNNNN"`. The DOI is then filled in automatically on the title pages, document information, citation and Table 1 of the Blueprint, in the Summary and in the Decision Memo.
2. Rebuild: `blueprint/build_blueprint.sh`; check the title pages of all PDFs.
3. Replace the "not yet assigned" lines in `README.md`, `RELEASE_NOTES.md`, `CHANGELOG.md`, `docs/source-of-truth.md` and, if a Blueprint entry is kept there, `CITATION.cff` (`references` section).
4. Run `blueprint/zenodo/make_zenodo_package.sh` and `sha256sum -c` inside `dist/zenodo/`.
5. Commit.

DOI insertion points, in full: `blueprint/src/metadata.json` (all PDFs), `README.md` (DOI and Citation sections), `CITATION.cff` (`references`), `RELEASE_NOTES.md`, `CHANGELOG.md`, `blueprint/zenodo/description.html` (not needed: Zenodo shows the DOI itself), `docs/source-of-truth.md`.

## 3. Push, tag and create the GitHub release

```bash
git push -u origin blueprint-v1.0
# open a pull request from blueprint-v1.0 into main and merge it, then:
git checkout main && git pull
git tag -a v1.1.0 -m "BAPIL Technical Blueprint, Version 1.0"
git push origin v1.1.0
```

Then create the GitHub release **v1.1.0** from the tag, paste `RELEASE_NOTES.md` as the description, and attach the six PDFs from `releases/v1.1/` (Blueprint, Summary and Decision Memo, English and Bangla). Confirm that the release appears at <https://github.com/md-naim-hassan-saykat/bapil/releases> and that the two GitHub Actions workflows ran.

## 4. Upload the files to the Zenodo draft

Upload everything in `dist/zenodo/`:

* 4 PDFs: Technical Blueprint and Blueprint Summary, English and Bangla
* 4 Markdown files (assembled editions)
* `BAPIL_Technical_Blueprint_figures.zip` and `BAPIL_Technical_Blueprint_tables.zip`
* `BAPIL_Technical_Blueprint_source.zip` (editable sources, budget model and workbook, documentation)
* `bapil-reference-implementation-0.1.0.zip`
* `SHA256SUMS.txt`

## 5. Metadata (from `zenodo_metadata.json` and `description.html`)

| Field | Value |
|---|---|
| Resource type | Publication / Report |
| Title | Bangladesh AI Policy & Innovation Lab (BAPIL): Technical Blueprint |
| Additional title (Bengali, type "Alternative title") | বাংলাদেশ এআই পলিসি অ্যান্ড ইনোভেশন ল্যাব (BAPIL): টেকনিক্যাল ব্লুপ্রিন্ট |
| Publication date | The day the record is published (Zenodo requires a full date; the documents show October 2026) |
| Creator | Saykat, Md Naim Hassan; ORCID 0009-0007-5270-3970; affiliation as decided in section 0 |
| Description | Paste `description.html` |
| Version | 1.0 |
| Languages | English, Bengali (one multilingual record; the English edition is authoritative) |
| Licence | As decided in section 0 (CC BY 4.0 recommended) |
| Keywords | See `zenodo_metadata.json` |
| Related works | *Is supplement to* 10.5281/zenodo.21363967 (White Paper); *References* 10.5281/zenodo.21441172 (Executive Summary); *Is supplemented by* https://github.com/md-naim-hassan-saykat/bapil/tree/v1.1.0 (software) |

## 6. Publish and check

1. Publish the Zenodo record only after section 3 is complete; confirm that the DOI resolves.
2. Confirm that the related works appear on the record page and that the record is **not** a new version of the White Paper or Executive Summary records.
3. Download the PDFs from Zenodo and check them against `SHA256SUMS.txt`.
4. If Option B was chosen, open the automatic repository record and check its title, version, licence and creators; correct them on Zenodo if needed (editing metadata does not change the DOI).
5. Record the release date and DOI in `CHANGELOG.md` (replace "Unreleased") and set `version` and `date-released` in `CITATION.cff`, in a follow-up commit.
