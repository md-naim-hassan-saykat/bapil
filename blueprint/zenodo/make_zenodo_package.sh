#!/usr/bin/env bash
# Collect the files for the Zenodo record into dist/zenodo/ (run after build_blueprint.sh).
set -euo pipefail
cd "$(dirname "$0")/../.."
OUT=dist/zenodo
rm -rf "$OUT"; mkdir -p "$OUT"
cp releases/v1.1/BAPIL_*.pdf "$OUT/"
cp blueprint/BAPIL_*.md "$OUT/"
( cd blueprint && zip -qry "../$OUT/BAPIL_Blueprint_v1_figures.zip" figures -x '*.aux' '*.log' )
( cd blueprint && zip -qry "../$OUT/BAPIL_Blueprint_v1_tables.zip" tables -x '*.aux' '*.log' )
zip -qry "$OUT/bapil-reference-implementation-0.1.0.zip" implementation -x 'implementation/build/*' '*/__pycache__/*' '*.egg-info/*'
( cd "$OUT" && sha256sum * > SHA256SUMS.txt )
ls -la "$OUT"
