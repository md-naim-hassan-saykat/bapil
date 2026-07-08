#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/.."

mkdir -p releases/v1.0

rm -f build_bn.tex build_bn.pdf build_bn.aux build_bn.log build_bn.out build_bn.toc

pandoc reports/BAPIL_White_Paper_v1_bn.md \
  --from=markdown+raw_tex \
  --standalone \
  --toc \
  --toc-depth=2 \
  --resource-path=reports:reports/figures:. \
  --include-in-header=reports/bangla-pdf-header.tex \
  --lua-filter=reports/fix-runin-headings.lua \
  -V mainfont="Noto Serif Bengali" \
  -V sansfont="Noto Sans Bengali" \
  -V monofont="Menlo" \
  -V mainfontoptions="Renderer=HarfBuzz,Script=Bengali" \
  -V sansfontoptions="Renderer=HarfBuzz,Script=Bengali" \
  -o build_bn.tex

lualatex -interaction=nonstopmode build_bn.tex
lualatex -interaction=nonstopmode build_bn.tex

mv build_bn.pdf releases/v1.0/BAPIL_White_Paper_v1_bn.pdf

open releases/v1.0/BAPIL_White_Paper_v1_bn.pdf
