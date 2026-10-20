import unittest

from _helpers import fixture_index
from bapil.answer import answer, split_sentences, verify_citations


class AnswerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.idx = fixture_index()

    def test_answer_has_a_citation_for_every_sentence(self):
        res = answer(self.idx, "When is a data protection impact assessment required?", min_score=0.5)
        self.assertFalse(res["abstained"])
        for s in res["answer"]:
            self.assertIn("pid", s["citation"])
            self.assertTrue(s["citation"]["pid"].startswith("policy_"))

    def test_cited_sentences_are_verbatim_from_the_source(self):
        res = answer(self.idx, "When is a data protection impact assessment required?", min_score=0.5)
        by_id = {p.pid: p for p in self.idx.passages}
        for s in res["answer"]:
            self.assertIn(s["text"], by_id[s["citation"]["pid"]].text)
        ok, bad = verify_citations(res["answer"], self.idx)
        self.assertTrue(ok, bad)

    def test_abstains_out_of_scope(self):
        res = answer(self.idx, "Who won the football world cup in 2022?")
        self.assertTrue(res["abstained"])
        self.assertEqual(res["answer"], [])

    def test_bangla_answer(self):
        res = answer(self.idx, "বাজেট নথি কখন প্রকাশিত হয়?", min_score=0.5)
        self.assertFalse(res["abstained"])
        self.assertEqual(res["answer"][0]["citation"]["doc_id"], "policy_bn")

    def test_verify_citations_rejects_unsupported_text(self):
        pid = self.idx.passages[0].pid
        ok, bad = verify_citations([{"text": "Cricket scores rose sharply in Chattogram stadium.",
                                     "citation": {"pid": pid}}], self.idx)
        self.assertFalse(ok)

    def test_sentence_split_handles_danda(self):
        self.assertEqual(len(split_sentences("এটি প্রথম বাক্য এখানে। এটি দ্বিতীয় বাক্য এখানে।")), 2)


if __name__ == "__main__":
    unittest.main()
