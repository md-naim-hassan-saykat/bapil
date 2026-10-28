# GitHub-to-Zenodo release checklist: BAPIL Technical Blueprint, Version 1.0

Nothing in this list has been done yet. Each step is to be carried out by the author, or by someone the author authorises, with their own GitHub and Zenodo accounts. No credential is needed in any file of this repository.

Keep these concepts apart: document version **1.0**; source revision (a Git commit); Git tag **v1.1.0**; GitHub release **v1.1.0**; the Blueprint’s Zenodo record and DOI (new, separate from the White Paper and Executive Summary records). Blueprint Annex D requires that the Zenodo record is **published only after** the GitHub release it refers to exists.

## 0. Decisions before anything is pushed (taken 29 October 2026)

| Decision | Choice | What remains to be done |
|---|---|---|
| Licence of the Blueprint, Summary, Memo, tables, figures and data | **CC BY 4.0**, as printed (consistent with the Executive Summary record); code stays MIT | Select CC BY 4.0 on both Zenodo records |
| Affiliation in the metadata | **"Independent Researcher, Bangladesh"** everywhere: Blueprint, Summary, `metadata.json`, `zenodo_metadata*.json`, `CITATION.cff` and the README author section | None |
| Zenodo GitHub integration for this repository | **Option A: switch it off.** The earlier White Paper record (10.5281/zenodo.21363967) was archived from GitHub release v1.0.1, so the integration was on at that time. If it is still on, publishing GitHub release v1.1.0 would automatically create a new version under the concept DOI 10.5281/zenodo.21360565 (which today resolves to the White Paper), with metadata from `CITATION.cff`, in addition to the two prepared records | **Author, before the GitHub release:** at <https://zenodo.org/account/settings/github/>, switch the toggle for `md-naim-hassan-saykat/bapil` off. This does not affect existing records or DOIs |
| Decision Memo in a Zenodo record | **No.** It is a separate document addressed to the authorities, not a research output; it is attached to the GitHub release | None |
| Licence of `research/` | **CC BY 4.0**, stated in `research/README.md` | None |
| Licence shown on the White Paper's Zenodo record (MIT, while the document says CC BY 4.0) | **Correct it to CC BY 4.0** (recommended; editing metadata keeps the DOI) | Author, on zenodo.org, at any time |
| Engagement drafts in the Zenodo source archive | **Keep them in**, as they are marked as unsent drafts and document the planned consultation | None |

## 1. Reserve the DOIs (Zenodo drafts, not published): done

Done by the author on 23 October 2026, as two records:

| Record | Reserved DOI | Contents (upload folder) |
|---|---|---|
| Technical Blueprint, Version 1.0 | 10.5281/zenodo.23587901 | `dist/zenodo/` |
| Blueprint Summary, Version 1.0 | 10.5281/zenodo.23587919 | `dist/zenodo-summary/` |

A reserved DOI is not registered until its record is published; until then doi.org does not resolve it.

## 2. Put the DOIs into the documents and rebuild: done

`blueprint/src/metadata.json` holds `"doi": "10.5281/zenodo.23587901"` and `"summary_doi": "10.5281/zenodo.23587919"`. The build prints them on the title pages, the document information and citation of the Blueprint, Table 1, both Summaries and the Decision Memo. They have also been entered in `README.md`, `RELEASE_NOTES.md`, `releases/README.md`, `CHANGELOG.md`, `CITATION.cff` (`references`), `docs/` and the Zenodo descriptions. To repackage, run `blueprint/zenodo/make_zenodo_package.sh`, then run `sha256sum -c SHA256SUMS.txt` inside each of the two folders.

## 3. Push, tag and create the GitHub release

```bash
git push -u origin blueprint-v1.0
# open a pull request from blueprint-v1.0 into main and merge it, then:
git checkout main && git pull
git tag -a v1.1.0 -m "BAPIL Technical Blueprint, Version 1.0"
git push origin v1.1.0
```

Then create the GitHub release **v1.1.0** from the tag, paste `RELEASE_NOTES.md` as the description, and attach the six PDFs from `releases/v1.1/` (Blueprint, Summary and Decision Memo, English and Bangla). Confirm that the release appears at <https://github.com/md-naim-hassan-saykat/bapil/releases> and that the two GitHub Actions workflows ran.

## 4. Upload the files to the Zenodo drafts

Blueprint record (10.5281/zenodo.23587901): upload everything in `dist/zenodo/`:

* 2 PDFs: Technical Blueprint, English and Bangla
* 2 Markdown files (assembled editions, English and Bangla)
* `BAPIL_Technical_Blueprint_figures.zip` and `BAPIL_Technical_Blueprint_tables.zip`
* `BAPIL_Technical_Blueprint_source.zip` (editable sources, budget model and workbook, documentation)
* `bapil-reference-implementation-0.1.0.zip`
* `SHA256SUMS.txt`

Summary record (10.5281/zenodo.23587919): upload everything in `dist/zenodo-summary/` (the English and Bangla Summary as PDF and Markdown, and `SHA256SUMS.txt`). Use `zenodo_metadata_summary.json` and `description_summary.html` for its metadata.

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
| Related works | *Is supplement to* 10.5281/zenodo.21363967 (White Paper); *References* 10.5281/zenodo.21441172 (Executive Summary); *Is supplemented by* 10.5281/zenodo.23587919 (Blueprint Summary); *Is supplemented by* https://github.com/md-naim-hassan-saykat/bapil/tree/v1.1.0 (software) |

Summary record: title "Bangladesh AI Policy & Innovation Lab (BAPIL): Blueprint Summary", alternative title "বাংলাদেশ এআই পলিসি অ্যান্ড ইনোভেশন ল্যাব (BAPIL): ব্লুপ্রিন্ট সারসংক্ষেপ", version 1.0, the same creator, languages and licence, and related works *Is supplement to* 10.5281/zenodo.23587901 (Technical Blueprint), *References* 10.5281/zenodo.21363967 and 10.5281/zenodo.21441172.

## 6. Publish and check

1. Publish the two Zenodo records only after section 3 is complete; confirm that both DOIs resolve.
2. Confirm that the related works appear on both record pages and that neither record is a new version of the White Paper or Executive Summary records.
3. Download the PDFs from both records and check them against the `SHA256SUMS.txt` of each folder.
4. If Option B was chosen, open the automatic repository record and check its title, version, licence and creators; correct them on Zenodo if needed (editing metadata does not change the DOI).
5. Record the release date and the publication of both records in `CHANGELOG.md` (replace "Unreleased") and set `version` and `date-released` in `CITATION.cff`, in a follow-up commit.
