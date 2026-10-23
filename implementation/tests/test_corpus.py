import os
import tempfile
import unittest

from _helpers import FIXTURES
from bapil.corpus import build_corpus, corpus_version, load_corpus, save_corpus


class CorpusTests(unittest.TestCase):
    def setUp(self):
        self.docs, self.passages = build_corpus([FIXTURES])

    def test_documents_and_provenance(self):
        ids = {d.doc_id for d in self.docs}
        self.assertEqual(ids, {"policy_en", "policy_bn"})
        for d in self.docs:
            self.assertEqual(len(d.sha256), 64)
            self.assertEqual(d.data_class, "DC0")

    def test_passages_have_ids_headings_and_language(self):
        p = [x for x in self.passages if x.doc_id == "policy_bn"][0]
        self.assertTrue(p.pid.startswith("policy_bn#p"))
        self.assertIn("নমুনা নীতি-নোট", p.heading)
        self.assertEqual(p.lang, "bn")

    def test_reference_sections_are_skipped(self):
        self.assertFalse(any("reference list entry" in p.text for p in self.passages))

    def test_list_items_are_separated(self):
        p = [x for x in self.passages if "minimisation" in x.text][0]
        self.assertIn("Data minimisation;", p.text)

    def test_save_and_load_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "c.json")
            v = save_corpus(path, self.docs, self.passages)
            docs, passages = load_corpus(path)
            self.assertEqual(v, corpus_version(docs))
            self.assertEqual(len(passages), len(self.passages))


if __name__ == "__main__":
    unittest.main()
