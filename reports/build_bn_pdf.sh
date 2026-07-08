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
