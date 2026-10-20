#!/usr/bin/env bash
# Build every BAPIL Blueprint output from source (Linux or macOS).
#   tables  : blueprint/tables/*.tex|pdf|png + md snippets
#   figures : blueprint/figures/*.tex|pdf|png
#   docs    : blueprint/*.md (assembled)  ->  releases/v1.1/*.pdf
# Requirements: python3 (3.10+), pandoc (3.x), XeLaTeX (TeX Live), pdftoppm (poppler),
#               fonts: Latin Modern, TeX Gyre Heros, Noto Serif, Noto Sans, Noto Serif Bengali,
#               Noto Sans Bengali, DejaVu Sans Mono.
# Usage: blueprint/build_blueprint.sh [--skip-assets] [--only NAME]
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
SRC="$ROOT/blueprint/src"
OUT="$ROOT/releases/v1.1"
SKIP_ASSETS=0
ONLY=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --skip-assets) SKIP_ASSETS=1 ;;
    --only) ONLY="$2"; shift ;;
  esac
  shift
done
mkdir -p "$OUT"

if [[ $SKIP_ASSETS -eq 0 ]]; then
  python3 "$SRC/make_tables.py"
  python3 "$SRC/make_figures.py"
fi

# Assemble once so the evaluation corpus contains the current documents
python3 "$SRC/assemble.py" >/dev/null

# Reference implementation: unit tests and demonstration results (feed Chapter 11)
TESTS_SUMMARY="see CI"
if ( cd implementation && python3 -m unittest discover -s tests > build_tests.log 2>&1 ); then
  N=$(grep -Eo 'Ran [0-9]+ tests' implementation/build_tests.log | grep -Eo '[0-9]+')
  TESTS_SUMMARY="${N} passed"
fi
rm -f implementation/build_tests.log
( cd implementation && PYTHONPATH=src python3 -m bapil.cli evaluate benchmarks/demo_questions.json \
    --corpus ../reports ../blueprint --json build/eval_report.json --tests "$TESTS_SUMMARY" >/dev/null ) || \
  echo "warning: evaluation step failed; Chapter 11 will show a placeholder"

python3 "$SRC/assemble.py"

build_pdf () {
  local name="$1" lang="$2" kind="$3"
  [[ -n "$ONLY" && "$ONLY" != "$name" ]] && return 0
  local headers=(--include-in-header="$SRC/header-common.tex")
  local vars=(-V colorlinks=true -V linkcolor=black -V urlcolor=black -V toccolor=black
              -V monofont="DejaVu Sans Mono" -V monofontoptions="Scale=0.84")
  if [[ "$kind" == "memo" ]]; then
    headers+=(--include-in-header="$SRC/header-memo.tex")
    vars+=(-V documentclass=extarticle -V fontsize=10pt -V geometry:margin=0.5in -V geometry:top=0.45in -V geometry:bottom=0.4in)
  else
    headers+=(--include-in-header="$SRC/header-$lang.tex")
    [[ "$name" == *Summary* ]] && headers+=(--include-in-header="$SRC/header-summary-$lang.tex")
    vars+=(-V fontsize=10pt -V geometry:margin=0.8in)
  fi
  # some minimal TeX installations lack lmodern.sty, which the pandoc template loads by default
  kpsewhich lmodern.sty >/dev/null 2>&1 || vars+=(-V fontfamily=fontspec)
  if [[ "$lang" == "bn" ]]; then
    vars+=(-V mainfont="Noto Serif" -V sansfont="Noto Sans")
  else
    vars+=(-V mainfont="Latin Modern Roman" -V sansfont="TeX Gyre Heros")
  fi
  # Bangla fonts lack curly quotes: keep straight quotes in Bangla editions
  local from="markdown+raw_tex-implicit_figures"
  [[ "$lang" == "bn" ]] && from="markdown+raw_tex-implicit_figures-smart"
  pandoc "blueprint/$name.md" \
    --from="$from" \
    --standalone \
    --lua-filter="$SRC/blueprint-filter.lua" \
    --resource-path="blueprint:." \
    "${headers[@]}" \
    --pdf-engine=xelatex \
    "${vars[@]}" \
    -o "$OUT/$name.pdf"
  echo "built releases/v1.1/$name.pdf"
}

build_pdf BAPIL_Technical_Blueprint_v1    en doc
build_pdf BAPIL_Technical_Blueprint_v1_bn bn doc
build_pdf BAPIL_Blueprint_Summary_v1      en doc
build_pdf BAPIL_Blueprint_Summary_v1_bn   bn doc
build_pdf BAPIL_Decision_Memo_v1          en memo
build_pdf BAPIL_Decision_Memo_v1_bn       bn memo
