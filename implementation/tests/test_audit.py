import os
import tempfile
import unittest

from _helpers import ROOT  # noqa: F401
from bapil.audit import AuditLog, verify


class AuditTests(unittest.TestCase):
    def test_chain_verifies_and_detects_tampering(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "audit.jsonl")
            log = AuditLog(path)
            for i in range(5):
                log.append("search", {"q": "query %d" % i, "pids": ["d#p%d" % i]})
            self.assertEqual(verify(path), (True, 5, None))
            with open(path, encoding="utf-8") as fh:
                lines = fh.readlines()
            lines[2] = lines[2].replace("query 2", "query X")
            with open(path, "w", encoding="utf-8") as fh:
                fh.writelines(lines)
            ok, n, bad = verify(path)
            self.assertFalse(ok)
            self.assertEqual(bad, 3)

    def test_deleting_a_line_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "audit.jsonl")
            log = AuditLog(path)
            for i in range(3):
                log.append("answer", {"i": i})
            with open(path, encoding="utf-8") as fh:
                lines = fh.readlines()
            with open(path, "w", encoding="utf-8") as fh:
                fh.writelines([lines[0], lines[2]])
            self.assertFalse(verify(path)[0])


if __name__ == "__main__":
    unittest.main()
