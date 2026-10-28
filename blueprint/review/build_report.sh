#!/usr/bin/env bash
# Build the review documents as PDF (XeLaTeX). Usage: build_report.sh [name ...]
set -euo pipefail
cd "$(dirname "$0")"
SRC=../src
names=("$@")
[[ ${#names[@]} -eq 0 ]] && names=(BAPIL_Blueprint_Audit_and_Revision_Report BAPIL_Blueprint_Adversarial_Review)
vars=(-V fontsize=10pt -V geometry:margin=0.7in -V colorlinks=true -V linkcolor=black -V urlcolor=black
      -V mainfont="Latin Modern Roman" -V sansfont="TeX Gyre Heros" -V monofont="DejaVu Sans Mono" -V toc-depth=2)
kpsewhich lmodern.sty >/dev/null 2>&1 || vars+=(-V fontfamily=fontspec)
for n in "${names[@]}"; do
  pandoc "$n.md" --from=markdown+raw_tex --standalone --toc \
    --include-in-header="$SRC/header-common.tex" --include-in-header=header-review.tex \
    --pdf-engine=xelatex "${vars[@]}" -o "$n.pdf"
  echo "built review/$n.pdf"
done
