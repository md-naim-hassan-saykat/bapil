import unittest

from _helpers import ROOT  # noqa: F401  (adds src to sys.path)
from bapil.text import bn_stem, content_terms, detect_lang, expand_query, normalize, tokenize


class TextTests(unittest.TestCase):
    def test_digits_fold_to_ascii(self):
        self.assertEqual(normalize("২০২৬"), "2026")

    def test_nukta_letters_unify(self):
        # precomposed U+09DF and decomposed U+09AF U+09BC must normalise identically
        self.assertEqual(normalize("নিয়ম"), normalize("নিয়ম"))

    def test_zero_width_removed_and_khanda_ta(self):
        self.assertEqual(normalize("উৎ"), normalize("উত্‍"))
        self.assertNotIn("‌", normalize("নীতি‌"))

    def test_bangla_suffix_stripping(self):
        self.assertEqual(bn_stem("নীতির"), "নীতি")
        self.assertEqual(bn_stem("মন্ত্রণালয়সমূহের"), "মন্ত্রণালয়")
        self.assertEqual(bn_stem("সরকারের"), "সরকার")

    def test_tokenize_keeps_surface_and_stem(self):
        toks = tokenize("নীতির বাজেট")
        self.assertIn("নীতির", toks)
        self.assertIn("নীতি", toks)
        self.assertIn("বাজেট", toks)

    def test_stopwords_removed(self):
        self.assertNotIn("the", tokenize("the budget"))
        self.assertNotIn("এবং", tokenize("বাজেট এবং নীতি"))

    def test_language_detection(self):
        self.assertEqual(detect_lang("বাংলাদেশের জাতীয় বাজেট"), "bn")
        self.assertEqual(detect_lang("national budget of Bangladesh"), "en")

    def test_glossary_expansion_both_ways(self):
        self.assertIn("বাজেট", expand_query("national budget"))
        self.assertIn("budget", expand_query("জাতীয় বাজেট"))
        self.assertTrue(set(expand_query("data protection")) & {"উপাত্ত", "সুরক্ষা"})

    def test_content_terms(self):
        self.assertEqual(content_terms("What is the budget?"), ["budget"])


if __name__ == "__main__":
    unittest.main()
