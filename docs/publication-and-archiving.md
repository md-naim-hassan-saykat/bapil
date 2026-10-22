# Publication and archiving

How the BAPIL publications move from this repository to a GitHub release and a Zenodo record, and what the current state is. The step-by-step checklist, with commands and metadata, is [`blueprint/zenodo/UPLOAD_CHECKLIST.md`](../blueprint/zenodo/UPLOAD_CHECKLIST.md).

## 1. Current state (checked 22 October 2026)

| Item | State |
|---|---|
| GitHub releases | `v1.0` and `v1.0.1` (White Paper and Executive Summary, July 2026). **No v1.1.0** |
| Tags | `v1.0`, `v1.0.1` |
| Remote `main` | Commit `4756cf9`. The Blueprint work is on the local branch `blueprint-v1.0` and **has not been pushed** |
| Zenodo records | White Paper 10.5281/zenodo.21363967 (record version v1.0.1, archived from the GitHub release; licence shown as MIT); Executive Summary 10.5281/zenodo.21441172 (CC BY 4.0); concept DOI 10.5281/zenodo.21360565 resolves to the White Paper record |
| Blueprint DOI | **None.** The documents print "DOI to be assigned on publication" |
| GitHub Actions | Workflows prepared in the branch; never run on GitHub |

## 2. Recommended arrangement of records

* **One multilingual Zenodo record** for the Technical Blueprint, holding the English and Bangla editions together with the Blueprint Summary, the figures, tables, editable sources and a source archive of the reference implementation. The two editions are the same work in two languages, so separate records would create duplicate citations. The English edition is authoritative.
* **Linked, not versioned:** the Blueprint record is a new record, related to the White Paper (*is supplement to*) and the Executive Summary (*references*), not a new version of either.
* **The Decision Memo** is a separate document addressed to the authorities; it is attached to the GitHub release but, by default, not deposited with the Blueprint.
* **The repository snapshot** (tag `v1.1.0`) is referenced from the record (*is supplemented by*).

## 3. Release workflow

1. Finalise and validate the documents (done locally; see `blueprint/QA_REPORT.md`).
2. Rebuild and inspect the PDFs (`blueprint/build_blueprint.sh`).
3. Validate the Markdown and metadata files (`blueprint/review/MARKDOWN_VALIDATION_REPORT.md`; `cffconvert --validate`).
4. Confirm the version, licence and affiliation (checklist, section 0).
5. Decide how to handle the Zenodo GitHub integration (checklist, section 0): if it is still switched on, publishing a GitHub release automatically creates a new version under the concept DOI, with metadata from `CITATION.cff`.
6. Reserve the Blueprint DOI on Zenodo (draft, not published), put it in `blueprint/src/metadata.json`, rebuild and commit.
7. Push the branch, merge into `main`, create and push tag `v1.1.0`.
8. Publish GitHub release v1.1.0 with `RELEASE_NOTES.md` and the six PDFs.
9. Upload `dist/zenodo/` to the Zenodo draft and publish it.
10. Check that the DOI resolves, the related identifiers appear and the files match `SHA256SUMS.txt`.
11. Update `README.md`, `CITATION.cff`, `CHANGELOG.md` and `docs/source-of-truth.md` with the real DOI and release date.
12. Record the release and archival information in `CHANGELOG.md`.

## 4. Rules

* Never insert a DOI that Zenodo has not issued. A reserved DOI may go into the documents only together with the commitment to publish that record.
* Never describe a release, tag or DOI as existing before it does. All current documents describe them as planned.
* Do not archive an intermediate draft as the final publication; the Zenodo record must contain the files built from the tagged commit.
* A previous version’s DOI (White Paper, Executive Summary) does not identify the Blueprint.
