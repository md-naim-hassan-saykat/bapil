import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
FIXTURES = os.path.join(HERE, "fixtures")
REPO = os.path.dirname(ROOT)


def fixture_index():
    from bapil.corpus import build_corpus
    from bapil.search import BM25Index
    docs, passages = build_corpus([FIXTURES])
    return BM25Index(docs, passages)
