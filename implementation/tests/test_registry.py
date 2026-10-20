import json
import os
import unittest

from _helpers import ROOT
from bapil.registry import load_records, transparency_register, validate

REG = os.path.join(ROOT, "examples", "registry")


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.records = load_records(REG)

    def test_examples_are_valid(self):
        self.assertEqual(len(self.records), 6)
        for r in self.records:
            self.assertEqual(validate(r), [], r["system_id"])

    def test_rules_reject_prohibited_and_unsafe_records(self):
        r = dict(self.records[0])
        r["risk_tier"] = "T0"
        self.assertTrue(validate(r))
        r = dict(self.records[0], risk_tier="T3", maturity_class="A")
        self.assertTrue(any("T3" in e for e in validate(r)))
        r = dict(self.records[0], data_classes=["P3"])
        self.assertTrue(any("P3" in e for e in validate(r)))

    def test_transparency_register_bilingual(self):
        en = transparency_register(self.records, "en")
        bn = transparency_register(self.records, "bn")
        self.assertIn("BAPIL-P1", en)
        self.assertIn("Bangladesh Policy Search Engine", en)
        self.assertIn("বাংলাদেশ নীতি অনুসন্ধান ইঞ্জিন", bn)

    def test_examples_match_json_schema_when_validator_available(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema not installed (optional)")
        with open(os.path.join(ROOT, "schemas", "ai_system_record.schema.json"), encoding="utf-8") as fh:
            schema = json.load(fh)
        for r in self.records:
            jsonschema.validate(r, schema)


if __name__ == "__main__":
    unittest.main()
