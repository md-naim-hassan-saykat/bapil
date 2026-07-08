#!/bin/bash
set -e

ROOT="$(pwd)"
BUILDDIR="$ROOT/.build"
OUTDIR="$ROOT/releases/v1.0"

rm -rf "$BUILDDIR"
mkdir -p "$BUILDDIR" "$OUTDIR"

cp -R "$ROOT/reports/figures" "$BUILDDIR/figures"

perl -pi -e 's/সূচীপত্র/সূচিপত্র/g' "$ROOT/reports/BAPIL_White_Paper_v1_bn.md"

pandoc "$ROOT/reports/BAPIL_White_Paper_v1_bn.md" \
  --from=markdown+raw_tex+implicit_figures \
  --standalone \
  --toc \
  --toc-depth=2 \
  --resource-path="$ROOT/reports:$ROOT/reports/figures:$BUILDDIR:$BUILDDIR/figures:$ROOT" \
  --include-in-header="$ROOT/reports/bangla-pdf-header.tex" \
  -V fontsize=10pt \
  -V geometry:margin=0.7in \
  -V colorlinks=true \
  -V linkcolor=black \
  -V urlcolor=black \
  -V toccolor=black \
  -V mainfont="Noto Serif Bengali" \
  -V sansfont="Noto Sans Bengali" \
  -V monofont="Menlo" \
  -V mainfontoptions="Renderer=HarfBuzz,Script=Bengali" \
  -V sansfontoptions="Renderer=HarfBuzz,Script=Bengali" \
  -o "$BUILDDIR/BAPIL_White_Paper_v1_bn.tex"

python3 - <<'PY'
from pathlib import Path
p = Path(".build/BAPIL_White_Paper_v1_bn.tex")
text = p.read_text(encoding="utf-8")
text = "\n".join(line for line in text.splitlines() if "selnolig" not in line)
p.write_text(text + "\n", encoding="utf-8")
PY

cd "$BUILDDIR"

lualatex -interaction=nonstopmode -halt-on-error BAPIL_White_Paper_v1_bn.tex
lualatex -interaction=nonstopmode -halt-on-error BAPIL_White_Paper_v1_bn.tex
lualatex -interaction=nonstopmode -halt-on-error BAPIL_White_Paper_v1_bn.tex
lualatex -interaction=nonstopmode -halt-on-error BAPIL_White_Paper_v1_bn.tex

cp "$BUILDDIR/BAPIL_White_Paper_v1_bn.pdf" "$OUTDIR/BAPIL_White_Paper_v1_bn.pdf"
