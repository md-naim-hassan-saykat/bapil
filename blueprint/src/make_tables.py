#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate every Blueprint table in four formats from one source.

Outputs (for each table NN and language L in {en, bn}):
  blueprint/tables/blueprint_tabNN[_bn].tex   standalone LaTeX source (XeLaTeX)
  blueprint/tables/blueprint_tabNN[_bn].pdf   compiled vector PDF
  blueprint/tables/blueprint_tabNN[_bn].png   raster image (220 dpi)
  blueprint/tables/md/blueprint_tabNN_L.md    Markdown snippet used by the documents

Usage: python3 make_tables.py [--no-compile] [--doi 10.5281/zenodo.NNNN]
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tables_a import TABLES_A  # noqa: E402
from tables_b import TABLES_B  # noqa: E402
from tables_c import TABLES_C  # noqa: E402
from tables_d import TABLES_D  # noqa: E402
from tables_e import TABLES_E, RISK_EXTRA  # noqa: E402

# The first edition numbered its tables 01 to 22. The expanded edition keeps those
# definitions in tables_a.py and tables_b.py and renumbers them here.
RENUMBER = {"01": "01", "02": "02", "03": "10", "04": "12", "05": "14", "06": "19",
            "07": "22", "08": "23", "09": "28", "10": "38", "11": "33", "12": "39",
            "13": "41", "14": "42", "15": "36", "16": "44", "17": "16", "18": "54",
            "19": "55", "20": "57", "21": "58", "22": "59"}


def _all_tables():
    import copy
    out = []
    for t in TABLES_A + TABLES_B:
        t = copy.deepcopy(t)
        old = t["id"]
        t["id"] = RENUMBER[old]
        if old == "19":
            for lang in ("en", "bn"):
                t["rows"][lang] = t["rows"][lang] + RISK_EXTRA[lang]
        out.append(t)
    out += TABLES_C + TABLES_D + TABLES_E
    ids = [t["id"] for t in out]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        raise SystemExit("duplicate table ids: %s" % sorted(dup))
    return sorted(out, key=lambda t: int(t["id"]))


TABLES = _all_tables()
ROOT = os.path.dirname(HERE)  # blueprint/
OUT = os.path.join(ROOT, "tables")
MD_OUT = os.path.join(OUT, "md")

BN_DIGITS = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")


def bn_num(n):
    return str(n).translate(BN_DIGITS)


def load_meta():
    with open(os.path.join(HERE, "metadata.json"), encoding="utf-8") as fh:
        return json.load(fh)


def doi_text(meta, lang):
    doi = meta.get("doi", "")
    if doi and "PENDING" not in doi:
        return doi
    return "DOI reserved on Zenodo at publication" if lang == "en" else "প্রকাশের সময় Zenodo-তে সংরক্ষিত DOI"


# ------------------------------------------------------------------ LaTeX
LATEX_SPECIALS = {
    "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
    "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
}


def tex_escape(s):
    out = "".join(LATEX_SPECIALS.get(c, c) for c in s)
    out = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", out)
    # allow breaks after slashes and dots in long identifiers
    out = out.replace("/", "/\\allowbreak{}")
    return out


PREAMBLE_EN = r"""\documentclass[border=10pt]{standalone}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\newfontfamily\bengalifont{Noto Serif Bengali}[Script=Bengali]
\usepackage[Latin,Bengali]{ucharclasses}
\setTransitionsFor{Bengali}{\begingroup\bengalifont}{\endgroup}
"""

PREAMBLE_BN = r"""\documentclass[border=10pt]{standalone}
\usepackage{fontspec}
\setmainfont{Noto Serif}
\newfontfamily\bengalifont{Noto Serif Bengali}[Script=Bengali]
\usepackage[Latin,Bengali]{ucharclasses}
\setTransitionsFor{Bengali}{\begingroup\bengalifont}{\endgroup}
\usepackage{newunicodechar}
\newunicodechar{।}{{\bengalifont\char"0964}}
\newunicodechar{॥}{{\bengalifont\char"0965}}
"""

COMMON = r"""\usepackage[table]{xcolor}
\usepackage{booktabs,tabularx,array}
\definecolor{bapilrule}{HTML}{1F2937}
\definecolor{bapilstripe}{HTML}{F3F4F6}
\renewcommand{\arraystretch}{1.28}
\setlength{\tabcolsep}{5pt}
"""


def colspec(widths):
    n = len(widths)
    total = float(sum(widths))
    parts = []
    for w in widths:
        h = w * n / total
        parts.append(r">{\hsize=%.3f\hsize\raggedright\arraybackslash}X" % h)
    return "@{}" + "".join(parts) + "@{}"


def tex_table(t, lang, meta):
    n = len(t["widths"])
    width_cm = 17 if n <= 5 else 22
    label = ("Table %s." % int(t["id"])) if lang == "en" else ("সারণি %s।" % bn_num(int(t["id"])))
    title = tex_escape(t["title"][lang])
    head = " & ".join(r"\textbf{%s}" % tex_escape(c) for c in t["cols"][lang]) + r" \\"
    body = []
    for row in t["rows"][lang]:
        cells = [tex_escape(c.replace("{{DOI}}", doi_text(meta, lang))) for c in row]
        body.append(" & ".join(cells) + r" \\")
    note = t.get("note", {}).get(lang)
    src = ("Source: BAPIL Technical Blueprint, Version 1.0 (2026). CC BY 4.0." if lang == "en"
           else "উৎস: BAPIL কারিগরি ব্লুপ্রিন্ট, সংস্করণ ১.০ (২০২৬)। CC BY 4.0।")
    parts = [PREAMBLE_EN if lang == "en" else PREAMBLE_BN, COMMON, r"\begin{document}",
             r"\begin{minipage}{%dcm}" % width_cm,
             r"{\large\bfseries %s}\ {\large %s}\par\vspace{7pt}" % (tex_escape(label), title),
             r"\small",
             r"\rowcolors{2}{bapilstripe}{white}",
             r"\begin{tabularx}{\linewidth}{%s}" % colspec(t["widths"]),
             r"\arrayrulecolor{bapilrule}\toprule",
             r"\rowcolor{white}" + head,
             r"\midrule"]
    parts += body
    parts += [r"\bottomrule", r"\end{tabularx}"]
    if note:
        parts.append(r"\par\vspace{5pt}{\footnotesize\itshape %s}" % tex_escape(note))
    parts.append(r"\par\vspace{3pt}{\scriptsize\color{gray} %s}" % tex_escape(src))
    parts += [r"\end{minipage}", r"\end{document}", ""]
    return "\n".join(parts)


# ------------------------------------------------------------------ Markdown
def md_cell(s):
    return s.replace("|", "/").strip()


def md_table(t, lang, meta):
    label = ("Table %s." % int(t["id"])) if lang == "en" else ("সারণি %s।" % bn_num(int(t["id"])))
    lines = ["**%s** %s" % (label, t["title"][lang]), ""]
    lines.append("| " + " | ".join(md_cell(c) for c in t["cols"][lang]) + " |")
    lines.append("|" + "|".join("-" * max(3, int(round(w * 10))) for w in t["widths"]) + "|")
    for row in t["rows"][lang]:
        lines.append("| " + " | ".join(md_cell(c.replace("{{DOI}}", doi_text(meta, lang))) for c in row) + " |")
    note = t.get("note", {}).get(lang)
    if note:
        lines += ["", "*%s* %s" % ("Note." if lang == "en" else "টীকা।", note)]
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------------ build
def compile_tex(tex_path, pdf_out, png_out):
    with tempfile.TemporaryDirectory() as tmp:
        base = os.path.basename(tex_path)
        shutil.copy(tex_path, os.path.join(tmp, base))
        r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", base],
                           cwd=tmp, capture_output=True, text=True)
        log = os.path.join(tmp, base[:-4] + ".log")
        missing = []
        if os.path.exists(log):
            with open(log, encoding="utf-8", errors="replace") as fh:
                missing = [l.strip() for l in fh if "Missing character" in l]
        if r.returncode != 0:
            sys.stderr.write(r.stdout[-3000:])
            raise SystemExit("xelatex failed for %s" % tex_path)
        if missing:
            sys.stderr.write("WARNING %s: %s\n" % (base, missing[:3]))
        shutil.copy(os.path.join(tmp, base[:-4] + ".pdf"), pdf_out)
    subprocess.run(["pdftoppm", "-r", "220", "-png", "-singlefile", pdf_out, png_out[:-4]], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-compile", action="store_true")
    ap.add_argument("--only", default="")
    args = ap.parse_args()
    meta = load_meta()
    os.makedirs(MD_OUT, exist_ok=True)
    for t in TABLES:
        if args.only and t["id"] not in args.only.split(","):
            continue
        for lang in ("en", "bn"):
            suffix = "" if lang == "en" else "_bn"
            stem = "blueprint_tab%s%s" % (t["id"], suffix)
            tex_path = os.path.join(OUT, stem + ".tex")
            with open(tex_path, "w", encoding="utf-8") as fh:
                fh.write(tex_table(t, lang, meta))
            with open(os.path.join(MD_OUT, "blueprint_tab%s_%s.md" % (t["id"], lang)), "w", encoding="utf-8") as fh:
                fh.write(md_table(t, lang, meta))
            if not args.no_compile:
                compile_tex(tex_path, os.path.join(OUT, stem + ".pdf"), os.path.join(OUT, stem + ".png"))
        print("table", t["id"], "done")


if __name__ == "__main__":
    main()
