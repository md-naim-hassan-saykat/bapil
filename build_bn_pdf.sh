#!/bin/bash
set -e

ROOT="$(pwd)"
BUILDDIR="$ROOT/.build"
OUTDIR="$ROOT/releases/v1.0"

rm -rf "$BUILDDIR"
mkdir -p "$BUILDDIR" "$OUTDIR"

python3 - <<'PY'
from pathlib import Path
import re

path = Path("reports/BAPIL_White_Paper_v1_bn.md")
text = path.read_text(encoding="utf-8")

text = text.replace("সূচীপত্র", "সূচিপত্র")

text = re.sub(
    r"\[([0-9০-৯]+[–-][0-9۰-۹]+),\s*([0-9۰-۹]+[–-][0-9۰-۹]+)\]",
    r"[\1, \2]",
    text
)

citation = r"\[[0-9۰-۹,\s,\-–—]+\]"
text = re.sub(rf"({citation})(?=\[)", r"\1 ", text)
text = re.sub(rf"({citation})(?=[A-Za-z0-9\u0980-\u09FF])", r"\1 ", text)

path.write_text(text, encoding="utf-8")
PY

cat > reports/bangla-pdf-header.tex <<'TEX'
\usepackage{xurl}
\usepackage{ragged2e}
\usepackage{seqsplit}
\usepackage{titlesec}
\usepackage{tocloft}
\usepackage{setspace}

\linespread{1.03}

\renewcommand{\contentsname}{সূচিপত্র}

\setlength{\cftbeforesecskip}{0.55em}
\setlength{\cftbeforesubsecskip}{0.08em}

\renewcommand{\cftsecfont}{\bfseries}
\renewcommand{\cftsecpagefont}{\bfseries}

\renewcommand{\cftsubsecfont}{\normalfont}
\renewcommand{\cftsubsecpagefont}{\normalfont}

\setlength{\cftsecindent}{0pt}
\setlength{\cftsubsecindent}{1.8em}

\titleformat{\section}
  {\normalfont\Large\bfseries}
  {}
  {0pt}
  {}

\titlespacing*{\section}
  {0pt}
  {2.2em}
  {1.1em}

\titleformat{\subsection}
  {\normalfont\large\bfseries}
  {}
  {0pt}
  {}

\titlespacing*{\subsection}
  {0pt}
  {1.4em}
  {0.7em}

\titleformat{\paragraph}
  {\normalfont\normalsize\bfseries}
  {}
  {0pt}
  {}

\titlespacing*{\paragraph}
  {0pt}
  {1.2em}
  {0.6em}
TEX

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

rm -f *.aux *.toc *.out *.log

lualatex -interaction=nonstopmode -halt-on-error BAPIL_White_Paper_v1_bn.tex
lualatex -interaction=nonstopmode -halt-on-error BAPIL_White_Paper_v1_bn.tex
lualatex -interaction=nonstopmode -halt-on-error BAPIL_White_Paper_v1_bn.tex

cp "$BUILDDIR/BAPIL_White_Paper_v1_bn.pdf" "$OUTDIR/BAPIL_White_Paper_v1_bn.pdf"

open "$OUTDIR/BAPIL_White_Paper_v1_bn.pdf"
mdls -name kMDItemNumberOfPages "$OUTDIR/BAPIL_White_Paper_v1_bn.pdf"
