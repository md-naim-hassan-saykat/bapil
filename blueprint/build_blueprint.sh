#!/usr/bin/env bash
# Build every BAPIL Blueprint output from source (Linux or macOS).
#   tables  : blueprint/tables/*.tex|pdf|png + md snippets
#   figures : blueprint/figures/*.tex|pdf|png
#   data    : blueprint/data/budget_*.csv (from src/budget_model.py)
#   docs    : blueprint/*.md (assembled)  ->  releases/v1.1/BAPIL_Technical_Blueprint_{en,bn}.pdf
#             BAPIL_Blueprint_Summary_{en,bn}.pdf and the separate BAPIL_Decision_Memo_{en,bn}.pdf
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
# fixed timestamps in every generated PDF (reproducible builds); see metadata.json
export FORCE_SOURCE_DATE=1   # TeX uses SOURCE_DATE_EPOCH for its own time stamps too
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-$(python3 -c "import json;print(json.load(open('$SRC/metadata.json'))['source_date_epoch'])")}"

if [[ $SKIP_ASSETS -eq 0 ]]; then
  python3 "$SRC/make_tables.py"
  python3 "$SRC/make_figures.py"
  python3 "$SRC/budget_model.py" --csv "$ROOT/blueprint/data" >/dev/null   # budget as CSV
fi

# Assemble once so the evaluation corpus contains the current documents. The previous evaluation
# report is removed first, so the corpus never contains its own earlier results (deterministic builds).
rm -f implementation/build/eval_report.json
python3 "$SRC/assemble.py" >/dev/null

# Reference implementation: unit tests and demonstration results (feed Chapter 11)
TESTS_SUMMARY="see CI"
if ( cd implementation && python3 -m unittest discover -s tests > build_tests.log 2>&1 ); then
  N=$(grep -Eo 'Ran [0-9]+ tests' implementation/build_tests.log | grep -Eo '[0-9]+')
  TESTS_SUMMARY="${N} passed"
fi
rm -f implementation/build_tests.log
( cd implementation && PYTHONPATH=src python3 -m bapil.cli evaluate benchmarks/demo_questions.json \
    --corpus ../reports ../blueprint/BAPIL_Technical_Blueprint_*.md ../blueprint/BAPIL_Blueprint_Summary_*.md --json build/eval_report.json --tests "$TESTS_SUMMARY" >/dev/null ) || \
  echo "warning: evaluation step failed; Chapter 11 will show a placeholder"

python3 "$SRC/assemble.py"
# key -> published reference number, for records that cite the source keys
python3 "$SRC/refnum.py" --key-table "$ROOT/blueprint/review/REFERENCE_NUMBERS.md"

# PDF metadata (title, author, subject, keywords) from blueprint/src/metadata.json, written to a
# small YAML file: pandoc always reads files as UTF-8, whereas command-line values depend on the locale.
META_DIR="$(mktemp -d)"
trap 'rm -rf "$META_DIR"' EXIT
# The PDF info dictionary shows only the publication month (no day), and a fixed
# SOURCE_DATE_EPOCH makes repeated builds reproducible.
python3 - "$SRC/metadata.json" "$META_DIR/pubdate.tex" <<'PY'
import json, sys
m = json.load(open(sys.argv[1], encoding="utf-8"))
open(sys.argv[2], "w", encoding="utf-8").write(
    "\\AtBeginDocument{\\hypersetup{pdfcreationdate={%s},pdfmoddate={%s}}}\n" % (m["pdf_date"], m["pdf_date"]))
PY
pdf_meta () {  # pdf_meta <titlekey> <lang>  ->  path of a YAML metadata file
  python3 - "$SRC/metadata.json" "$1" "$2" "$META_DIR/$1_$2.yaml" <<'PY'
import json, sys
m = json.load(open(sys.argv[1], encoding="utf-8"))
key, lang, out = sys.argv[2], sys.argv[3], sys.argv[4]
q = lambda s: json.dumps(s, ensure_ascii=False)   # JSON strings are valid YAML scalars
# each Zenodo publication carries its own DOI in the PDF keywords (the Memo has no DOI of its own)
doi = {"title": m.get("doi", ""), "summary_title": m.get("summary_doi", "")}.get(key, "")
kw = m["keywords"] + (["doi:" + doi] if doi and "PENDING" not in doi else [])
with open(out, "w", encoding="utf-8") as fh:
    fh.write("title-meta: %s\nauthor-meta: %s\nsubject: %s\nkeywords: %s\n" % (
        q(m[key + "_" + lang]), q(m["author"]), q(m["subject_" + lang]), q(", ".join(kw))))
PY
  echo "$META_DIR/$1_$2.yaml"
}

build_pdf () {
  local name="$1" lang="$2" titlekey="$3"
  [[ -n "$ONLY" && "$ONLY" != "$name" ]] && return 0
  local headers=(--include-in-header="$SRC/header-common.tex" --include-in-header="$SRC/header-$lang.tex"
                 --include-in-header="$META_DIR/pubdate.tex")
  [[ "$name" == *Summary* ]] && headers+=(--include-in-header="$SRC/header-summary-$lang.tex")
  [[ "$name" == *Memo* ]] && headers+=(--include-in-header="$SRC/header-memo.tex")
  local vars=(-V colorlinks=true -V linkcolor=black -V urlcolor=black -V toccolor=black
              -V monofont="DejaVu Sans Mono" -V monofontoptions="Scale=0.84"
              -V fontsize=10pt -V geometry:margin=0.8in
              --metadata-file="$(pdf_meta "$titlekey" "$lang")")
  # some minimal TeX installations lack lmodern.sty, which the pandoc template loads by default
  kpsewhich lmodern.sty >/dev/null 2>&1 || vars+=(-V fontfamily=fontspec)
  # Quotation marks: the sources already hold the final characters (“ ” ‘ ’, see src/typography.py).
  # Pandoc's smart extension and the TeX ligature mapping are both switched off, so the PDF text
  # contains exactly the characters of the source (with TeX ligatures, a straight " used to print as ”).
  if [[ "$lang" == "bn" ]]; then
    headers+=(--include-in-header="$SRC/header-bn-num.tex")
    vars+=(-V mainfont="Noto Serif" -V sansfont="Noto Sans")
  else
    vars+=(-V mainfont="Latin Modern Roman" -V sansfont="TeX Gyre Heros")
  fi
  vars+=(-V mainfontoptions="Ligatures=TeXOff" -V sansfontoptions="Ligatures=TeXOff")
  pandoc "blueprint/$name.md" \
    --from="markdown+raw_tex-implicit_figures-smart" \
    --standalone \
    --lua-filter="$SRC/blueprint-filter.lua" \
    --resource-path="blueprint:." \
    "${headers[@]}" \
    --pdf-engine=xelatex \
    "${vars[@]}" \
    -o "$OUT/$name.pdf"
  echo "built releases/v1.1/$name.pdf"
}

# Check the quotation-mark convention in the sources (fails the build on straight quotes in prose)
python3 "$SRC/typography.py" --check "$SRC"/en/*.md "$SRC"/bn/*.md "$SRC"/*.src.md "$SRC"/refs_new.md

build_pdf BAPIL_Technical_Blueprint_en en title
build_pdf BAPIL_Technical_Blueprint_bn bn title
build_pdf BAPIL_Blueprint_Summary_en   en summary_title
build_pdf BAPIL_Blueprint_Summary_bn   bn summary_title
# The Decision Memo is a separate deliverable addressed to the authorities; it is not part of the Blueprint.
build_pdf BAPIL_Decision_Memo_en       en memo_title
build_pdf BAPIL_Decision_Memo_bn       bn memo_title

# Manifest of all deliverables with checksums
python3 "$ROOT/blueprint/make_manifest.py"
