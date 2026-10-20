import contextlib
import io
import os
import tempfile
import unittest

from _helpers import FIXTURES, ROOT
from bapil.cli import main


def run(*argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        main(list(argv))
    return buf.getvalue()


class CliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.log = os.path.join(self.tmp.name, "audit.jsonl")

    def tearDown(self):
        self.tmp.cleanup()

    def test_index_search_ask(self):
        idx = os.path.join(self.tmp.name, "corpus.json")
        self.assertIn("indexed 2 documents", run("index", "--corpus", FIXTURES, "--index", idx))
        out = run("search", "budget", "--index", idx, "--log", self.log)
        self.assertIn("policy_", out)
        out = run("ask", "Who won the football world cup in 2022?", "--index", idx, "--log", self.log)
        self.assertIn("ABSTAINED", out)
        self.assertIn("chain intact", run("verify-log", self.log))

    def test_assess_and_register(self):
        out = run("assess", os.path.join(ROOT, "examples", "risk", "risk_p1_policy_search.json"), "--log", self.log)
        self.assertIn("T2 Limited", out)
        export = os.path.join(self.tmp.name, "register.md")
        out = run("register", os.path.join(ROOT, "examples", "registry"), "--export", export, "--lang", "bn")
        self.assertIn("BAPIL-P6", out)
        with open(export, encoding="utf-8") as fh:
            self.assertIn("স্বচ্ছতা নিবন্ধন", fh.read())


if __name__ == "__main__":
    unittest.main()
