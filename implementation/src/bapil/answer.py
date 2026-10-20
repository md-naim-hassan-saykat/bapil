"""Citation-grounded extractive answers with abstention ("no citation, no claim").

The answer is assembled only from sentences found in retrieved passages, and every
sentence carries the identifier of its source passage. If the evidence is weak (low
retrieval score or low coverage of the question's content terms), the function
abstains and returns the closest sources with the reason.

A generative model can be added behind ``Generator``; its output must then pass
``verify_citations`` before it is shown.
"""
import re

from .text import bn_stem, content_terms, en_stem, tokenize

_SENT_SPLIT = re.compile(r"(?<=[.!?।])\s+")


def split_sentences(text):
    return [s.strip() for s in _SENT_SPLIT.split(text) if len(s.strip().split()) >= 4]


def _stems(text):
    out = set()
    for t in tokenize(text):
        out.add(t)
        out.add(bn_stem(t))
        out.add(en_stem(t))
    return out


def coverage(question, passages):
    """Share of the question's content terms found in any of ``passages``."""
    terms = content_terms(question)
    if not terms:
        return 0.0
    vocab = set()
    for p in passages:
        vocab |= _stems(p.heading + " " + p.text)
    found = sum(1 for t in terms if t in vocab)
    return found / len(terms)


def answer(index, question, k=5, max_sentences=3, min_score=3.0, min_coverage=0.6):
    hits = index.search(question, k=k)
    sources = [h.to_dict(index.docs) for h in hits[:3]]
    if not hits:
        return {"question": question, "abstained": True, "reason": "no_matching_passages",
                "answer": [], "sources": [], "corpus_version": index.version}
    top = hits[0].score
    cov = coverage(question, [h.passage for h in hits[:3]])
    if top < min_score or cov < min_coverage:
        reason = "low_retrieval_score" if top < min_score else "low_term_coverage"
        return {"question": question, "abstained": True, "reason": reason,
                "evidence": {"top_score": round(top, 3), "coverage": round(cov, 3)},
                "answer": [], "sources": sources, "corpus_version": index.version}
    weights = index.query_weights(question)
    scored = []
    for rank, h in enumerate(hits[:3]):
        for j, sent in enumerate(split_sentences(h.passage.text)):
            st = _stems(sent)
            s = sum(w for t, w in weights.items() if t in st)
            if s > 0:
                # prefer higher-ranked passages and earlier sentences on ties
                scored.append((s - 0.01 * rank - 0.001 * j, sent, h.passage))
    scored.sort(key=lambda x: -x[0])
    chosen, seen = [], set()
    for s, sent, p in scored:
        key = sent.lower()
        if key in seen:
            continue
        seen.add(key)
        chosen.append({"text": sent, "citation": {"pid": p.pid, "doc_id": p.doc_id, "heading": p.heading}})
        if len(chosen) >= max_sentences:
            break
    if not chosen:
        return {"question": question, "abstained": True, "reason": "no_supporting_sentence",
                "answer": [], "sources": sources, "corpus_version": index.version}
    margin = top - (hits[1].score if len(hits) > 1 else 0.0)
    band = "high" if cov >= 0.9 and margin > 1.0 else ("medium" if cov >= 0.75 else "low")
    return {"question": question, "abstained": False, "confidence": band,
            "evidence": {"top_score": round(top, 3), "coverage": round(cov, 3)},
            "answer": chosen, "sources": sources, "corpus_version": index.version}


def verify_citations(answer_sentences, index, min_overlap=0.5):
    """Check that each generated sentence is supported by the passage it cites.

    ``answer_sentences`` is a list of {"text": ..., "citation": {"pid": ...}}. A sentence
    is supported when at least ``min_overlap`` of its content terms occur in the cited
    passage. Returns (all_supported, list_of_unsupported_texts).
    """
    by_id = {p.pid: p for p in index.passages}
    bad = []
    for s in answer_sentences:
        p = by_id.get(s.get("citation", {}).get("pid"))
        if p is None or coverage(s["text"], [p]) < min_overlap:
            bad.append(s["text"])
    return (not bad), bad


class Generator:
    """Interface for an optional language model that rephrases extracted evidence."""

    def rephrase(self, question, sentences):  # pragma: no cover - interface only
        raise NotImplementedError


def format_answer(result):
    """Plain-text rendering for the command line."""
    lines = ["Q: " + result["question"]]
    if result["abstained"]:
        lines.append("ABSTAINED (%s). Closest sources:" % result["reason"])
        for s in result["sources"]:
            lines.append("  - [%s] %s" % (s["pid"], s["heading"]))
        return "\n".join(lines)
    lines.append("Confidence: %s" % result["confidence"])
    for i, a in enumerate(result["answer"], 1):
        lines.append("%d. %s [%s]" % (i, a["text"], a["citation"]["pid"]))
    lines.append("Sources:")
    for s in result["sources"]:
        lines.append("  - [%s] %s" % (s["pid"], s["heading"]))
    return "\n".join(lines)
