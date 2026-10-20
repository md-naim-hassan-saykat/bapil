"""Minimal JSON HTTP API on the Python standard library (Blueprint FR-10, Section 7.3).

Endpoints
---------
GET  /v1/health                 service status and corpus version
GET  /v1/search?q=...&k=10      ranked passages with provenance
GET  /v1/answer?q=...           cited extractive answer or a reasoned abstention
POST /v1/risk/assess            risk-tier assessment of a JSON questionnaire

Every search, answer and assessment is written to the hash-chained audit log.
This server is for demonstration and testing; production deployments sit behind the
API gateway, identity and rate-limiting components described in the Blueprint.
"""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from . import __version__
from .answer import answer
from .audit import AuditLog
from .risk import AssessmentError, assess

MAX_BODY = 64 * 1024


def make_handler(index, audit_path):
    log = AuditLog(audit_path) if audit_path else None

    class Handler(BaseHTTPRequestHandler):
        server_version = "BAPIL-ref/" + __version__

        def log_message(self, fmt, *args):  # keep test output quiet
            pass

        def _send(self, code, obj):
            body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            u = urlparse(self.path)
            qs = parse_qs(u.query)
            q = (qs.get("q") or [""])[0].strip()
            if u.path == "/v1/health":
                return self._send(200, {"status": "ok", "version": __version__, "corpus_version": index.version,
                                        "documents": len(index.docs), "passages": len(index.passages)})
            if u.path in ("/v1/search", "/v1/answer"):
                if not q or len(q) > 500:
                    return self._send(400, {"error": "parameter q is required (1 to 500 characters)"})
                if u.path == "/v1/search":
                    try:
                        k = max(1, min(50, int((qs.get("k") or ["10"])[0])))
                    except ValueError:
                        return self._send(400, {"error": "k must be an integer"})
                    hits = [h.to_dict(index.docs) for h in index.search(q, k=k)]
                    out = {"query": q, "corpus_version": index.version, "results": hits}
                    if log:
                        log.append("search", {"q": q, "k": k, "pids": [h["pid"] for h in hits]})
                    return self._send(200, out)
                res = answer(index, q)
                if log:
                    log.append("answer", {"q": q, "abstained": res["abstained"],
                                          "pids": [a["citation"]["pid"] for a in res["answer"]]})
                return self._send(200, res)
            return self._send(404, {"error": "not found"})

        def do_POST(self):
            u = urlparse(self.path)
            if u.path != "/v1/risk/assess":
                return self._send(404, {"error": "not found"})
            n = int(self.headers.get("Content-Length") or 0)
            if n <= 0 or n > MAX_BODY:
                return self._send(400, {"error": "request body required (at most 64 KB)"})
            try:
                data = json.loads(self.rfile.read(n).decode("utf-8"))
                res = assess(data).to_dict()
            except (ValueError, AssessmentError) as e:
                return self._send(400, {"error": str(e)})
            if log:
                log.append("risk_assessment", {"system_id": res["system_id"], "tier": res["tier"]})
            return self._send(200, res)

    return Handler


def make_server(index, host="127.0.0.1", port=8080, audit_path="build/audit.jsonl"):
    return ThreadingHTTPServer((host, port), make_handler(index, audit_path))
