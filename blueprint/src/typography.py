#!/usr/bin/env python3
"""Quotation-mark convention for the BAPIL Blueprint sources.

Convention (English and Bangla editions alike):
  * prose and bibliography use typographic marks: “double”, ‘single’, and ’ for
    the English apostrophe (BAPIL’s, don’t, ’19);
  * straight marks (" and ') are kept only where they are literal characters:
    fenced and inline code, URLs and link targets, HTML comments, YAML, raw LaTeX,
    JSON and command lines.

The sources are normalised once and then checked on every build, so the PDF holds
exactly the characters in the source (the build also switches off TeX ligatures,
which used to turn every straight " into a closing mark ”).

Usage:
  python3 typography.py --check  FILE...   # report straight marks left in prose (exit 1 if any)
  python3 typography.py --fix    FILE...   # rewrite files in place
The function `normalise(text)` is also used by assemble.py for text taken from
other sources (the White Paper reference list), which are not edited.
"""
import re
import sys

# Spans that must never be touched, in order of precedence.
PROTECT = re.compile(
    r"(?ms)"
    r"^```.*?^```[^\n]*$"            # fenced code blocks
    r"|\A---\n.*?\n---$"             # YAML front matter (start of file only)
    r"|<!--.*?-->"                   # HTML comments and build markers
    r"|`[^`\n]+`"                    # inline code
    r"|\]\([^)\s]*\)"                # link targets
    r"|<https?://[^>]+>"             # autolinks
    r"|https?://[^\s)>\]]+"          # bare URLs
    r"|\{\{[^}]*\}\}"                # build placeholders
    r"|\\[A-Za-z]+(?:\[[^\]]*\])?(?:\{[^}]*\})*"  # raw LaTeX commands
)

OPENERS = set(" \t\n([{/–—- ") | {""}


def _fix_prose(s: str, prev: str = "") -> str:
    out = []
    for i, ch in enumerate(s):
        before = s[i - 1] if i > 0 else prev
        after = s[i + 1] if i + 1 < len(s) else ""
        if ch == '"':
            out.append("“" if before in OPENERS else "”")
        elif ch == "'":
            if before.isalnum() and (after.isalpha() or after == ""):
                out.append("’")                      # apostrophe: BAPIL’s, nat’l
            elif before in OPENERS and after.isdigit():
                out.append("’")                      # elided year: ’19
            elif before in "sS" and (after in " \t\n,.;:)" or after == ""):
                out.append("’")                      # plural possessive: employers’
            elif before in OPENERS and after.isalpha():
                out.append("‘")                      # opening single quote
            else:
                out.append("’")                      # closing single quote
        else:
            out.append(ch)
    return "".join(out)


def normalise(text: str) -> str:
    """Return text with straight quotes in prose replaced by typographic marks."""
    out, pos = [], 0
    for m in PROTECT.finditer(text):
        prose = text[pos:m.start()]
        out.append(_fix_prose(prose, text[pos - 1] if pos else ""))
        out.append(m.group(0))
        pos = m.end()
    out.append(_fix_prose(text[pos:], text[pos - 1] if pos else ""))
    return "".join(out)


def straight_in_prose(text: str):
    """Yield (line number, line) for lines whose prose still has straight quotes."""
    masked = PROTECT.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)
    for n, (line, orig) in enumerate(zip(masked.split("\n"), text.split("\n")), 1):
        if '"' in line or "'" in line:
            yield n, orig


def main(argv):
    if len(argv) < 2 or argv[0] not in ("--check", "--fix"):
        print(__doc__)
        return 2
    mode, files, bad = argv[0], argv[1:], 0
    for f in files:
        with open(f, encoding="utf-8") as fh:
            text = fh.read()
        if mode == "--fix":
            new = normalise(text)
            if new != text:
                with open(f, "w", encoding="utf-8") as fh:
                    fh.write(new)
                print(f"normalised {f}")
        else:
            for n, line in straight_in_prose(text):
                bad += 1
                print(f"{f}:{n}: straight quote in prose: {line.strip()[:100]}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
