import unittest

from _helpers import fixture_index


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.idx = fixture_index()

    def test_english_query_finds_english_passage(self):
        hit = self.idx.search("impact assessment for personal data", k=1)[0]
        self.assertEqual(hit.passage.doc_id, "policy_en")
        self.assertIn("Data Protection", hit.passage.heading)

    def test_bangla_query_finds_bangla_passage(self):
        hit = self.idx.search("বাজেট নথি প্রকাশ", k=1)[0]
        self.assertEqual(hit.passage.doc_id, "policy_bn")

    def test_cross_lingual_expansion(self):
        # English query, restricted to Bangla passages, still finds the Bangla budget section
        hits = self.idx.search("budget", k=3, lang="bn")
        self.assertTrue(hits)
        self.assertIn("বাজেট", hits[0].passage.heading)

    def test_bangla_digits_match_ascii(self):
        hits = self.idx.search("2026 বাজেট", k=1)
        self.assertEqual(hits[0].passage.doc_id, "policy_bn")

    def test_results_carry_provenance(self):
        d = self.idx.search("budget", k=1)[0].to_dict(self.idx.docs)
        self.assertIn("sha256", d["provenance"])

    def test_deterministic_ranking(self):
        a = [h.passage.pid for h in self.idx.search("budget ministries", k=5)]
        b = [h.passage.pid for h in self.idx.search("budget ministries", k=5)]
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
