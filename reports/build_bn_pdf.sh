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
local toc_inserted = false
local before_chapter1 = true

function Header(el)
  local title = pandoc.utils.stringify(el)

  -- Replace the Markdown TOC heading with the actual LaTeX TOC.
  -- Both common Bangla spellings are supported.
  if title == "সূচীপত্র" or title == "সূচিপত্র"
      or title == "Contents" or title == "Table of Contents" then
    if not toc_inserted then
      toc_inserted = true
      return pandoc.RawBlock("latex", "\\tableofcontents")
    end
    return {}
  end

  -- Chapter 1 remains in its original position.
  if title:match("^অধ্যায়%s*১:") or title:match("^অধ্যায়%s*১:") then
    before_chapter1 = false
    return el
  end

  -- Preliminary headings are excluded from numbering and the TOC.
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
  --pdf-engine=xelatex \
  -V fontsize=10pt \
  -V geometry:margin=0.7in \
  -V colorlinks=true \
  -V linkcolor=black \
  -V urlcolor=black \
  -V toccolor=black \
  -V mainfont="Noto Serif Bengali" \
  -V sansfont="Noto Sans Bengali" \
  -V monofont="Menlo" \
  -V mainfontoptions="Script=Bengali" \
  -V sansfontoptions="Script=Bengali" \
  -o "$OUTDIR/BAPIL_White_Paper_v1_bn.pdf"

open "$OUTDIR/BAPIL_White_Paper_v1_bn.pdf"
mdls -name kMDItemNumberOfPages "$OUTDIR/BAPIL_White_Paper_v1_bn.pdf" || true
