import json
import os
import tempfile
import threading
import unittest
import urllib.error
import urllib.request

from _helpers import fixture_index
from bapil.api import make_server
from bapil.audit import verify


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.log = os.path.join(cls.tmp.name, "audit.jsonl")
        cls.srv = make_server(fixture_index(), "127.0.0.1", 0, cls.log)
        cls.base = "http://127.0.0.1:%d" % cls.srv.server_port
        cls.thread = threading.Thread(target=cls.srv.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()
        cls.srv.server_close()
        cls.tmp.cleanup()

    def get(self, path):
        with urllib.request.urlopen(self.base + path, timeout=10) as r:
            return r.status, json.loads(r.read().decode("utf-8"))

    def test_health(self):
        code, body = self.get("/v1/health")
        self.assertEqual(code, 200)
        self.assertEqual(body["status"], "ok")

    def test_search_bangla(self):
        q = urllib.request.quote("বাজেট নথি")
        code, body = self.get("/v1/search?q=%s&k=2" % q)
        self.assertEqual(code, 200)
        self.assertEqual(body["results"][0]["doc_id"], "policy_bn")

    def test_answer_and_audit(self):
        q = urllib.request.quote("Who won the football world cup in 2022?")
        code, body = self.get("/v1/answer?q=%s" % q)
        self.assertTrue(body["abstained"])
        self.assertTrue(verify(self.log)[0])

    def test_risk_endpoint(self):
        payload = {"system_id": "X", "prohibited": {},
                   "scores": {"D1": 2, "D2": 0, "D3": 0, "D4": 1, "D5": 1, "D6": 0, "D7": 1}}
        req = urllib.request.Request(self.base + "/v1/risk/assess", data=json.dumps(payload).encode(),
                                     headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=10) as r:
            self.assertEqual(json.loads(r.read())["tier"], "T2")

    def test_bad_requests(self):
        with self.assertRaises(urllib.error.HTTPError) as cm:
            self.get("/v1/search")
        self.assertEqual(cm.exception.code, 400)
        with self.assertRaises(urllib.error.HTTPError) as cm:
            self.get("/nope")
        self.assertEqual(cm.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
