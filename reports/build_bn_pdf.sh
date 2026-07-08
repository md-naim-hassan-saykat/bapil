#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/.."

ROOT="$(pwd)"
BUILDDIR="$ROOT/.build/bn"
OUTDIR="$ROOT/releases/v1.0"

rm -rf "$BUILDDIR"
mkdir -p "$BUILDDIR" "$OUTDIR"

cp -R "$ROOT/reports/figures" "$BUILDDIR/figures"

cat > "$BUILDDIR/toc-before-bn-chapter1.lua" <<'LUA'
local inserted = false
local before_chapter1 = true

function Header(el)
  local title = pandoc.utils.stringify(el)

  if title == "সূচিপত্র" or title == "Contents" then
    return {}
  end

  if (not inserted) and (title:match("^অধ্যায়%s*১:") or title:match("^অধ্যায়%s*১:")) then
    inserted = true
    before_chapter1 = false
    return {
      pandoc.RawBlock("latex", "\\clearpage\n\\tableofcontents\n\\clearpage"),
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

pandoc reports/BAPIL_White_Paper_v1_bn.md \
  --from=markdown+raw_tex+implicit_figures \
  --standalone \
  --lua-filter="$BUILDDIR/toc-before-bn-chapter1.lua" \
  --lua-filter=reports/fix-runin-headings.lua \
  --resource-path=reports:reports/figures:. \
  --include-in-header=reports/bangla-pdf-header.tex \
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

p = Path(".build/bn/BAPIL_White_Paper_v1_bn.tex")
text = p.read_text(encoding="utf-8")
text = "\n".join(line for line in text.splitlines() if "selnolig" not in line)
p.write_text(text + "\n", encoding="utf-8")
PY

cd "$BUILDDIR"

lualatex -interaction=nonstopmode -halt-on-error BAPIL_White_Paper_v1_bn.tex
lualatex -interaction=nonstopmode -halt-on-error BAPIL_White_Paper_v1_bn.tex

cp "$BUILDDIR/BAPIL_White_Paper_v1_bn.pdf" "$OUTDIR/BAPIL_White_Paper_v1_bn.pdf"

open "$OUTDIR/BAPIL_White_Paper_v1_bn.pdf"
mdls -name kMDItemNumberOfPages "$OUTDIR/BAPIL_White_Paper_v1_bn.pdf" || true
