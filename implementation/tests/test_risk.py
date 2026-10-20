import json
import os
import unittest

from _helpers import ROOT
from bapil.risk import AssessmentError, assess

BASE = {"D1": 0, "D2": 0, "D3": 0, "D4": 0, "D5": 0, "D6": 0, "D7": 0}


def q(**scores):
    s = dict(BASE)
    s.update(scores)
    return {"system_id": "X", "prohibited": {}, "scores": s}


class RiskTests(unittest.TestCase):
    def test_prohibited_use_gives_t0(self):
        r = assess({"system_id": "X", "prohibited": {"social_scoring": True}, "scores": BASE})
        self.assertEqual(r.tier, "T0")

    def test_low(self):
        self.assertEqual(assess(q(D1=1, D4=1, D5=1)).tier, "T1")

    def test_limited_by_total(self):
        self.assertEqual(assess(q(D1=1, D3=1, D4=1, D5=1, D6=1, D7=1)).tier, "T2")

    def test_limited_by_d1_or_d7(self):
        self.assertEqual(assess(q(D1=2)).tier, "T2")
        self.assertEqual(assess(q(D7=2)).tier, "T2")

    def test_high_conditions(self):
        self.assertEqual(assess(q(D1=3)).tier, "T3")
        self.assertEqual(assess(q(D2=3)).tier, "T3")
        self.assertEqual(assess(q(D2=2, D3=2)).tier, "T3")
        self.assertEqual(assess(q(D1=2, D2=1, D3=1, D4=2, D5=2, D6=2, D7=2)).tier, "T2")  # total 12
        self.assertEqual(assess(q(D1=2, D2=1, D3=1, D4=3, D5=2, D6=2, D7=2)).tier, "T3")  # total 13

    def test_validation(self):
        with self.assertRaises(AssessmentError):
            assess({"system_id": "X", "prohibited": {}, "scores": {"D1": 1}})
        with self.assertRaises(AssessmentError):
            assess(q(D1=4))
        with self.assertRaises(AssessmentError):
            assess({"system_id": "X", "prohibited": {"unknown_flag": True}, "scores": BASE})

    def test_annex_b_worked_example(self):
        with open(os.path.join(ROOT, "examples", "risk", "risk_p1_policy_search.json"), encoding="utf-8") as fh:
            r = assess(json.load(fh))
        self.assertEqual((r.tier, r.total), ("T2", 5))
        with open(os.path.join(ROOT, "examples", "risk", "risk_p1_research_only.json"), encoding="utf-8") as fh:
            r = assess(json.load(fh))
        self.assertEqual((r.tier, r.total), ("T1", 3))

    def test_controls_present(self):
        self.assertIn("ERRC review", assess(q(D1=2)).controls)


if __name__ == "__main__":
    unittest.main()
