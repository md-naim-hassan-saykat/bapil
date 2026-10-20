"""Bangla-aware text normalisation, tokenisation and bilingual query expansion.

Design notes
------------
* Unicode NFC is applied first. NFC *decomposes* the three Bangla nukta letters
  (U+09DC, U+09DD, U+09DF) because they are composition exclusions, so after NFC both
  spellings of a word such as "নিয়ম" become identical.
* The legacy khanda-ta sequence (TA + VIRAMA + ZWJ) is mapped to U+09CE before
  zero-width characters are removed.
* Bangla digits are folded to ASCII so that "২০২৬" matches "2026".
* Suffix stripping is deliberately light. Each word yields its surface form *and* its
  stem, so over-stripping cannot remove a match that exact matching would have found.
"""
import json
import os
import re
import unicodedata

BN_TO_ASCII = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
ASCII_TO_BN = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")

_ZERO_WIDTH = re.compile("[​‌‍⁠﻿­]")
_KHANDA_TA_LEGACY = "ত্‍"
_TOKEN = re.compile(r"[ঀ-৿]+|[a-z0-9]+(?:[.\-][a-z0-9]+)*")
_BENGALI_CHAR = re.compile(r"[ঀ-৿]")

# Conservative Bangla inflectional suffixes, longest first.
BN_SUFFIXES = sorted([
    "গুলোর", "গুলোতে", "গুলোকে", "গুলো", "গুলির", "গুলিতে", "গুলি",
    "সমূহের", "সমূহে", "সমূহ", "দেরকে", "দের", "টির", "টিকে", "টিতে", "টি", "টার", "টা",
    "য়ের", "েরা", "ের", "েই", "কে", "তে", "েতে", "ে", "র",
], key=len, reverse=True)
_BN_VOWEL_SIGNS = set("ািীুূৃেৈোৌ")

EN_STOP = set("""a an the and or of to in on for by with as at from is are was were be been being this that these
those it its into than then there their them they he she we you your our not no yes do does did can could would
should may might must shall will what which who whom whose why how when where also such any all each per via""".split())
BN_STOP = set("""ও এবং বা এর এই সেই যে যা যার কী কি কেন কীভাবে কোন কোনো করে করা হয় হবে হলে জন্য থেকে সঙ্গে সাথে না
নয় আছে ছিল এক একটি তার তাদের এটি এগুলো হিসেবে মধ্যে দ্বারা প্রতি পর্যন্ত আর তবে যদি""".split())


def normalize(text):
    """Return a canonical, lower-cased, digit-folded form of ``text``."""
    if not text:
        return ""
    s = unicodedata.normalize("NFC", text)
    s = s.replace(_KHANDA_TA_LEGACY, "ৎ")
    s = _ZERO_WIDTH.sub("", s)
    s = s.translate(BN_TO_ASCII)
    return s.lower()


def is_bangla(text, threshold=0.3):
    """True when at least ``threshold`` of the letters in ``text`` are Bangla."""
    letters = [c for c in text if c.isalpha() or _BENGALI_CHAR.match(c)]
    if not letters:
        return False
    bn = sum(1 for c in letters if _BENGALI_CHAR.match(c))
    return bn / len(letters) >= threshold


def detect_lang(text):
    return "bn" if is_bangla(text) else "en"


def bn_stem(word):
    """Strip one common Bangla suffix, keeping at least two base characters."""
    for suf in BN_SUFFIXES:
        if word.endswith(suf) and len(word) - len(suf) >= 2:
            base = word[: -len(suf)]
            if suf == "র" and (not base or base[-1] not in _BN_VOWEL_SIGNS):
                continue  # only strip a bare "র" after a vowel sign (নীতির -> নীতি)
            if suf == "ে" and len(base) < 3:
                continue
            return base
    return word


def en_stem(word):
    """Very light English stemming (plural forms only)."""
    if len(word) > 4 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 4 and word.endswith("s") and not word.endswith(("ss", "us", "is")):
        return word[:-1]
    return word


def raw_tokens(text):
    return _TOKEN.findall(normalize(text))


def tokenize(text, stem=True, drop_stopwords=True):
    """Tokenise text into search terms.

    Each word contributes its surface form and, when different, its stem.
    """
    out = []
    for tok in raw_tokens(text):
        bangla = bool(_BENGALI_CHAR.match(tok))
        if drop_stopwords and (tok in BN_STOP if bangla else tok in EN_STOP):
            continue
        if not bangla and len(tok) < 2:
            continue
        out.append(tok)
        if stem:
            st = bn_stem(tok) if bangla else en_stem(tok)
            if st != tok:
                out.append(st)
    return out


def content_terms(text):
    """Distinct stemmed content terms of a query (used for evidence coverage)."""
    terms = []
    for tok in raw_tokens(text):
        bangla = bool(_BENGALI_CHAR.match(tok))
        if (tok in BN_STOP) if bangla else (tok in EN_STOP or len(tok) < 2):
            continue
        st = bn_stem(tok) if bangla else en_stem(tok)
        if st not in terms:
            terms.append(st)
    return terms


# ------------------------------------------------------------------ glossary
_GLOSSARY = None


def load_glossary(path=None):
    """Load the bilingual glossary as a list of (english, bangla) phrase pairs."""
    global _GLOSSARY
    if path is None and _GLOSSARY is not None:
        return _GLOSSARY
    p = path or os.path.join(os.path.dirname(__file__), "data", "glossary_bn_en.json")
    with open(p, encoding="utf-8") as fh:
        data = json.load(fh)
    pairs = [(normalize(e["en"]), normalize(e["bn"])) for e in data["entries"]]
    if path is None:
        _GLOSSARY = pairs
    return pairs


def expand_query(text, glossary=None):
    """Return extra terms from the bilingual glossary for phrases found in ``text``.

    A phrase matches when all of its tokens occur in the query (in any order),
    which tolerates small differences in word order and inflection.
    """
    pairs = glossary if glossary is not None else load_glossary()
    q_terms = set(tokenize(text))
    extra = []
    for en, bn in pairs:
        for src, dst in ((en, bn), (bn, en)):
            src_terms = [bn_stem(t) if _BENGALI_CHAR.match(t) else en_stem(t) for t in tokenize(src, stem=False)]
            if src_terms and all(t in q_terms for t in src_terms):
                for t in tokenize(dst):
                    if t not in q_terms and t not in extra:
                        extra.append(t)
    return extra
