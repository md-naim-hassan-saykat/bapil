#!/usr/bin/env bash
# Collect the files for the Technical Blueprint's Zenodo record into dist/zenodo/
# (run after blueprint/build_blueprint.sh). Internal review records (blueprint/review/) and the separate
# Decision Memo are not included (see UPLOAD_CHECKLIST.md, section 0).
set -euo pipefail
cd "$(dirname "$0")/../.."
OUT=dist/zenodo
rm -rf "$OUT"; mkdir -p "$OUT"
cp releases/v1.1/BAPIL_Technical_Blueprint_{en,bn}.pdf releases/v1.1/BAPIL_Blueprint_Summary_{en,bn}.pdf "$OUT/"
cp blueprint/BAPIL_Technical_Blueprint_{en,bn}.md blueprint/BAPIL_Blueprint_Summary_{en,bn}.md "$OUT/"
( cd blueprint && zip -qry "../$OUT/BAPIL_Technical_Blueprint_figures.zip" figures -x '*.aux' '*.log' )
( cd blueprint && zip -qry "../$OUT/BAPIL_Technical_Blueprint_tables.zip" tables -x '*.aux' '*.log' )
# editable source package: masters, table data, figure sources, budget model and CSV, templates, build, docs
zip -qry "$OUT/BAPIL_Technical_Blueprint_source.zip" \
  blueprint/src blueprint/data blueprint/build_blueprint.sh blueprint/README.md blueprint/MANIFEST.md \
  blueprint/CHANGES.md blueprint/QA_REPORT.md blueprint/SOURCES_AND_LICENCES.md \
  reports/BAPIL_White_Paper_v1.md LICENSE README.md CITATION.cff CHANGELOG.md RELEASE_NOTES.md \
  REPRODUCIBILITY.md DATA_AND_METHODOLOGY.md CONTRIBUTING.md docs \
  -x '*/__pycache__/*' '*.pyc'
zip -qry "$OUT/bapil-reference-implementation-0.1.0.zip" implementation -x 'implementation/build/*' '*/__pycache__/*' '*.egg-info/*'
( cd "$OUT" && sha256sum * > SHA256SUMS.txt )
ls -la "$OUT"
