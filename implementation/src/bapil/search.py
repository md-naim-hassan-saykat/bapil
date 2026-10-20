"""BM25 search over passages with bilingual query expansion.

BM25 follows Robertson and Zaragoza (2009). Query terms carry weights: original terms
weigh 1.0 and glossary expansions weigh ``expansion_weight`` (default 0.6), so that a
Bangla query can retrieve English passages and vice versa without overpowering exact
matches. The section heading is indexed with the passage text so that headings help
ranking.
"""
import math
from collections import Counter, defaultdict
from dataclasses import dataclass

from .corpus import corpus_version
from .text import expand_query, tokenize


@dataclass
class Hit:
    passage: object
    score: float
    matched: list

    def to_dict(self, doc_index=None):
        p = self.passage
        d = {"pid": p.pid, "doc_id": p.doc_id, "heading": p.heading, "lang": p.lang,
             "score": round(self.score, 4), "matched_terms": self.matched, "text": p.text}
        if doc_index and p.doc_id in doc_index:
            doc = doc_index[p.doc_id]
            d["provenance"] = {"path": doc.path, "sha256": doc.sha256, "data_class": doc.data_class}
        return d


class BM25Index:
    def __init__(self, docs, passages, k1=1.5, b=0.75, expansion_weight=0.6):
        self.docs = {d.doc_id: d for d in docs}
        self.passages = passages
        self.version = corpus_version(docs)
        self.k1, self.b, self.expansion_weight = k1, b, expansion_weight
        self.tf = []
        self.lengths = []
        self.df = Counter()
        self.postings = defaultdict(list)
        for i, p in enumerate(passages):
            toks = tokenize(p.heading) + tokenize(p.text)
            c = Counter(toks)
            self.tf.append(c)
            self.lengths.append(len(toks))
            for t in c:
                self.df[t] += 1
                self.postings[t].append(i)
        self.N = len(passages)
        self.avgdl = (sum(self.lengths) / self.N) if self.N else 0.0

    def idf(self, term):
        n = self.df.get(term, 0)
        return math.log(1 + (self.N - n + 0.5) / (n + 0.5))

    def query_weights(self, query, expand=True):
        weights = {}
        for t in tokenize(query):
            weights[t] = 1.0
        if expand:
            for t in expand_query(query):
                weights.setdefault(t, self.expansion_weight)
        return weights

    def search(self, query, k=10, lang=None, expand=True):
        weights = self.query_weights(query, expand=expand)
        scores = defaultdict(float)
        matched = defaultdict(list)
        for term, w in weights.items():
            if term not in self.postings:
                continue
            idf = self.idf(term)
            for i in self.postings[term]:
                f = self.tf[i][term]
                denom = f + self.k1 * (1 - self.b + self.b * self.lengths[i] / self.avgdl)
                scores[i] += w * idf * f * (self.k1 + 1) / denom
                matched[i].append(term)
        ranked = sorted(scores.items(), key=lambda kv: (-kv[1], self.passages[kv[0]].pid))
        hits = []
        for i, s in ranked:
            if lang and self.passages[i].lang != lang:
                continue
            hits.append(Hit(self.passages[i], s, sorted(set(matched[i]))))
            if len(hits) >= k:
                break
        return hits
