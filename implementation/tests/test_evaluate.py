import unittest

from _helpers import fixture_index
from bapil.evaluate import evaluate


class EvaluateTests(unittest.TestCase):
    def test_metrics_and_abstention(self):
        idx = fixture_index()
        qs = [
            {"id": "a", "lang": "en", "question": "data protection impact assessment",
             "relevant": [{"doc": "policy_en", "heading": "Data Protection"}]},
            {"id": "b", "lang": "bn", "question": "বাজেট নথি প্রকাশ",
             "relevant": [{"doc": "policy_bn", "heading": "বাজেট স্বচ্ছতা"}]},
            {"id": "u", "lang": "en", "question": "Who won the football world cup in 2022?", "answerable": False},
        ]
        r = evaluate(idx, qs)
        self.assertEqual(r["subsets"]["all"]["n"], 2)
        self.assertAlmostEqual(r["subsets"]["all"]["recall@1"], 1.0)
        self.assertAlmostEqual(r["subsets"]["all"]["mrr@10"], 1.0)
        self.assertLessEqual(r["subsets"]["all"]["ndcg@10"], 1.0)
        self.assertEqual(r["abstention"]["rate"], 1.0)

    def test_missing_gold_passage_is_an_error(self):
        idx = fixture_index()
        with self.assertRaises(ValueError):
            evaluate(idx, [{"id": "x", "question": "budget", "relevant": [{"doc": "nope", "heading": "x"}]}])


if __name__ == "__main__":
    unittest.main()
