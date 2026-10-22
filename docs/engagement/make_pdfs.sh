#!/usr/bin/env bash
# Typesets the engagement drafts as PDFs with the fonts and mixed Bangla/Latin handling of the
# Blueprint build. Usage (from the repository root): bash docs/engagement/make_pdfs.sh [OUTDIR]
# Requirements: pandoc 3.x, XeLaTeX, Noto Serif, Noto Sans, Noto Serif Bengali, Noto Sans Bengali.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="${1:-$ROOT/docs/engagement/pdf}"
mkdir -p "$OUT"
for f in "$ROOT"/docs/engagement/briefing-note_*.md "$ROOT"/docs/engagement/letter-*.md; do
  name="$(basename "$f" .md)"
  pandoc "$f" --from=markdown-smart \
    --lua-filter="$ROOT/blueprint/src/blueprint-filter.lua" \
    --include-in-header="$ROOT/blueprint/src/header-common.tex" \
    --include-in-header="$ROOT/docs/engagement/engagement-header.tex" \
    --pdf-engine=xelatex -V fontfamily=fontspec \
    -V mainfont="Noto Serif" -V sansfont="Noto Sans" \
    -o "$OUT/$name.pdf"
  echo "built $OUT/$name.pdf"
done
