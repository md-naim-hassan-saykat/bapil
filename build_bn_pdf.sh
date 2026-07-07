#!/bin/bash
set -e

ROOT="$(pwd)"
BUILDDIR="$ROOT/.build"
OUTDIR="$ROOT/releases/v1.0"

mkdir -p "$BUILDDIR" "$OUTDIR"

cat > "$BUILDDIR/toc-before-bn-chapter1.lua" <<'LUA'
local inserted = false
local before_chapter1 = true

function Header(el)
  local title = pandoc.utils.stringify(el)

  if title == "সূচিপত্র" or title == "সূচীপত্র" or title == "Contents" then
    return {}
  end

  if (not inserted) and (title:match("^অধ্যায়%s*১:") or title:match("^অধ্যায়%s*১:")) then
    inserted = true
    before_chapter1 = false
    return {
      pandoc.RawBlock("latex", "\\clearpage\n\\renewcommand{\\contentsname}{সূচিপত্র}\n\\tableofcontents\n\\clearpage"),
      el
    }
  end

  if before_chapter1 then
    el.classes:insert("unnumbered")
    el.classes:insert("unlisted")
  end

  return el
end
LUA

rm -rf "$BUILDDIR/figures"
cp -R "$ROOT/reports/figures" "$BUILDDIR/figures"

pandoc "$ROOT/reports/BAPIL_White_Paper_v1_bn.md" \
  --from=markdown+raw_tex+implicit_figures \
  --standalone \
  --lua-filter="$BUILDDIR/toc-before-bn-chapter1.lua" \
  --resource-path="$ROOT/reports:$ROOT/reports/figures:$ROOT" \
  --include-in-header="$ROOT/reports/bangla-pdf-header.tex" \
  -V fontsize=10pt \
  -V geometry:margin=0.7in \
  -V colorlinks=true \
  -V linkcolor=black \
  -V urlcolor=black \
  -V toccolor=black \
  -V toc-title="সূচিপত্র" \
  -o "$BUILDDIR/BAPIL_White_Paper_v1_bn.tex"

python3 - <<'PY'
from pathlib import Path
p = Path(".build/BAPIL_White_Paper_v1_bn.tex")
text = p.read_text(encoding="utf-8")

text = "\n".join(line for line in text.splitlines() if "selnolig" not in line)
text = text.replace("সূচীপত্র", "সূচিপত্র")

p.write_text(text + "\n", encoding="utf-8")
PY

cd "$BUILDDIR"

lualatex -interaction=nonstopmode -halt-on-error BAPIL_White_Paper_v1_bn.tex
lualatex -interaction=nonstopmode -halt-on-error BAPIL_White_Paper_v1_bn.tex

cp "$BUILDDIR/BAPIL_White_Paper_v1_bn.pdf" "$OUTDIR/BAPIL_White_Paper_v1_bn.pdf"

open "$OUTDIR/BAPIL_White_Paper_v1_bn.pdf"
mdls -name kMDItemNumberOfPages "$OUTDIR/BAPIL_White_Paper_v1_bn.pdf"
