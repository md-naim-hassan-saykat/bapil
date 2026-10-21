#!/usr/bin/env bash
# Build the Audit and Revision Report PDF (XeLaTeX).
set -euo pipefail
cd "$(dirname "$0")"
SRC=../src
vars=(-V fontsize=10pt -V geometry:margin=0.7in -V colorlinks=true -V linkcolor=black -V urlcolor=black
      -V mainfont="Latin Modern Roman" -V sansfont="TeX Gyre Heros" -V monofont="DejaVu Sans Mono" -V toc-depth=2)
kpsewhich lmodern.sty >/dev/null 2>&1 || vars+=(-V fontfamily=fontspec)
pandoc BAPIL_Blueprint_Audit_and_Revision_Report.md --from=markdown+raw_tex --standalone --toc \
  --include-in-header="$SRC/header-common.tex" --include-in-header=header-review.tex \
  --pdf-engine=xelatex "${vars[@]}" -o BAPIL_Blueprint_Audit_and_Revision_Report.pdf
echo "built review/BAPIL_Blueprint_Audit_and_Revision_Report.pdf"
