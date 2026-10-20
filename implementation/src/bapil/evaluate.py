"""Retrieval and abstention evaluation (Blueprint FR-08, Table 28).

Question file format (JSON)::

    {"name": ..., "version": ..., "questions": [
        {"id": "q01", "lang": "en", "question": "...",
         "relevant": [{"doc": "BAPIL_White_Paper_v1", "heading": "Retrieval-Augmented Generation"}]},
        {"id": "u01", "lang": "en", "question": "...", "answerable": false}
    ]}

A passage is relevant when its document identifier equals ``doc`` and its heading path
contains ``heading`` (case-insensitive). Metrics use binary relevance.
"""
import json
import math

from .answer import answer


def _is_rel(passage, rel):
    if passage.doc_id != rel["doc"]:
        return False
    return rel.get("heading", "").lower() in passage.heading.lower()


def rank_of_first_relevant(hits, rels):
    for i, h in enumerate(hits, 1):
        if any(_is_rel(h.passage, r) for r in rels):
            return i
    return None


def ndcg_at_k(hits, rels, n_relevant, k=10):
    """Binary nDCG@k; ``n_relevant`` is the number of relevant passages in the whole corpus."""
    gains = [1.0 if any(_is_rel(h.passage, r) for r in rels) else 0.0 for h in hits[:k]]
    dcg = sum(g / math.log2(i + 2) for i, g in enumerate(gains))
    ideal = sum(1.0 / math.log2(i + 2) for i in range(min(k, max(1, n_relevant))))
    return dcg / ideal if ideal else 0.0


def evaluate(index, questions, k=10):
    per = []
    abst = []
    for q in questions:
        if q.get("answerable", True) is False:
            res = answer(index, q["question"])
            abst.append({"id": q["id"], "lang": q.get("lang"), "abstained": res["abstained"]})
            continue
        hits = index.search(q["question"], k=k)
        r = rank_of_first_relevant(hits, q["relevant"])
        n_rel = sum(1 for p in index.passages if any(_is_rel(p, rel) for rel in q["relevant"]))
        if n_rel == 0:
            raise ValueError("question %s has no relevant passage in the corpus" % q["id"])
        per.append({"id": q["id"], "lang": q.get("lang", "en"), "rank": r, "n_relevant": n_rel,
                    "ndcg@10": ndcg_at_k(hits, q["relevant"], n_rel, 10)})

    def summarise(rows):
        n = len(rows)
        if not n:
            return None
        rec = lambda kk: sum(1 for x in rows if x["rank"] and x["rank"] <= kk) / n  # noqa: E731
        mrr = sum((1.0 / x["rank"]) if x["rank"] and x["rank"] <= 10 else 0.0 for x in rows) / n
        return {"n": n, "recall@1": rec(1), "recall@5": rec(5), "recall@10": rec(10), "mrr@10": mrr,
                "ndcg@10": sum(x["ndcg@10"] for x in rows) / n}

    report = {
        "corpus": {"version": index.version, "documents": len(index.docs), "passages": len(index.passages)},
        "subsets": {"all": summarise(per),
                    "en": summarise([x for x in per if x["lang"] == "en"]),
                    "bn": summarise([x for x in per if x["lang"] == "bn"])},
        "abstention": {"n": len(abst), "rate": (sum(1 for a in abst if a["abstained"]) / len(abst)) if abst else 0.0},
        "per_question": per + [{"id": a["id"], "lang": a["lang"], "abstained": a["abstained"]} for a in abst],
    }
    return report


def load_questions(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return data["questions"] if isinstance(data, dict) else data
