"""Command line interface for the BAPIL reference implementation.

Examples (run from the ``implementation`` directory after ``pip install -e .``)::

    python -m bapil.cli index --corpus ../reports ../blueprint
    python -m bapil.cli search "data protection impact assessment"
    python -m bapil.cli ask "বাংলা নীতি ফাউন্ডেশন মডেল কী?"
    python -m bapil.cli assess examples/risk/risk_p1_policy_search.json
    python -m bapil.cli evaluate benchmarks/demo_questions.json
    python -m bapil.cli register examples/registry --export build/transparency_register.md
    python -m bapil.cli verify-log build/audit.jsonl
    python -m bapil.cli serve --port 8080
"""
import argparse
import json
import os
import sys

from . import __version__
from .answer import answer, format_answer
from .audit import AuditLog, verify
from .corpus import build_corpus, load_corpus, save_corpus
from .evaluate import evaluate, load_questions
from .registry import load_records, transparency_register, validate
from .risk import AssessmentError, assess
from .search import BM25Index

DEFAULT_CORPUS = ["../reports", "../blueprint"]
DEFAULT_INDEX = "build/corpus.json"
DEFAULT_LOG = "build/audit.jsonl"


def _load_index(args):
    corpus = getattr(args, "corpus", None)
    if corpus:
        docs, passages = build_corpus(corpus)
    elif os.path.exists(args.index):
        docs, passages = load_corpus(args.index)
    else:
        docs, passages = build_corpus(DEFAULT_CORPUS)
    if not passages:
        sys.exit("no passages found; pass --corpus with directories of Markdown files")
    return BM25Index(docs, passages)


def cmd_index(args):
    docs, passages = build_corpus(args.corpus or DEFAULT_CORPUS)
    version = save_corpus(args.index, docs, passages)
    print("indexed %d documents, %d passages, corpus version %s -> %s"
          % (len(docs), len(passages), version, args.index))


def cmd_search(args):
    idx = _load_index(args)
    hits = idx.search(args.query, k=args.k)
    if args.json:
        print(json.dumps([h.to_dict(idx.docs) for h in hits], ensure_ascii=False, indent=1))
    else:
        for i, h in enumerate(hits, 1):
            print("%2d. %.3f  [%s]  %s" % (i, h.score, h.passage.pid, h.passage.heading))
            print("    " + h.passage.text[:220] + ("..." if len(h.passage.text) > 220 else ""))
    AuditLog(args.log).append("search", {"q": args.query, "k": args.k, "pids": [h.passage.pid for h in hits]})


def cmd_ask(args):
    idx = _load_index(args)
    res = answer(idx, args.question)
    print(json.dumps(res, ensure_ascii=False, indent=1) if args.json else format_answer(res))
    AuditLog(args.log).append("answer", {"q": args.question, "abstained": res["abstained"],
                                         "pids": [a["citation"]["pid"] for a in res["answer"]]})


def cmd_assess(args):
    with open(args.file, encoding="utf-8") as fh:
        q = json.load(fh)
    try:
        res = assess(q)
    except AssessmentError as e:
        sys.exit("invalid questionnaire: %s" % e)
    if args.json:
        print(json.dumps(res.to_dict(), ensure_ascii=False, indent=1))
    else:
        print("%s: %s %s (total %d)" % (res.system_id, res.tier, res.tier_name, res.total))
        for r in res.reasons:
            print("  reason:   " + r)
        for c in res.controls:
            print("  control:  " + c)
        print("  approver: " + res.approver)
    AuditLog(args.log).append("risk_assessment", {"system_id": res.system_id, "tier": res.tier})


def cmd_evaluate(args):
    idx = _load_index(args)
    report = evaluate(idx, load_questions(args.questions))
    if args.tests:
        report["tests"] = args.tests
    if args.json:
        os.makedirs(os.path.dirname(os.path.abspath(args.json)), exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(report, fh, ensure_ascii=False, indent=1)
    c = report["corpus"]
    print("corpus %s: %d documents, %d passages" % (c["version"], c["documents"], c["passages"]))
    for name, m in report["subsets"].items():
        if m:
            print("%-4s n=%-3d R@1=%.2f R@5=%.2f R@10=%.2f MRR@10=%.2f nDCG@10=%.2f"
                  % (name, m["n"], m["recall@1"], m["recall@5"], m["recall@10"], m["mrr@10"], m["ndcg@10"]))
    a = report["abstention"]
    print("abstention on unanswerable questions: %d/%d = %.2f" % (round(a["rate"] * a["n"]), a["n"], a["rate"]))


def cmd_register(args):
    records = load_records(args.path)
    bad = 0
    for r in records:
        errs = validate(r)
        status = "ok" if not errs else "INVALID: " + "; ".join(errs)
        bad += bool(errs)
        print("%-10s %s" % (r.get("system_id", "?"), status))
    if args.export:
        os.makedirs(os.path.dirname(os.path.abspath(args.export)), exist_ok=True)
        valid = [r for r in records if not validate(r)]
        with open(args.export, "w", encoding="utf-8") as fh:
            fh.write(transparency_register(valid, args.lang))
        print("transparency register (%s) -> %s" % (args.lang, args.export))
    if bad:
        sys.exit(1)


def cmd_verify_log(args):
    ok, n, bad = verify(args.path)
    print("%s: %d entries, %s" % (args.path, n, "chain intact" if ok else "BROKEN at line %s" % bad))
    if not ok:
        sys.exit(1)


def cmd_serve(args):
    from .api import make_server
    idx = _load_index(args)
    srv = make_server(idx, args.host, args.port, args.log)
    print("BAPIL reference API on http://%s:%d (corpus %s); Ctrl+C to stop" % (args.host, srv.server_port, idx.version))
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


def build_parser():
    p = argparse.ArgumentParser(prog="bapil", description="BAPIL reference implementation v" + __version__)
    p.add_argument("--version", action="version", version=__version__)
    sub = p.add_subparsers(dest="cmd", required=True)

    def with_corpus(sp):
        sp.add_argument("--corpus", nargs="+", help="directories or Markdown files to index")
        sp.add_argument("--index", default=DEFAULT_INDEX, help="saved corpus file (default %(default)s)")

    s = sub.add_parser("index", help="build and save the passage corpus")
    with_corpus(s); s.set_defaults(func=cmd_index)
    s = sub.add_parser("search", help="bilingual BM25 search")
    s.add_argument("query"); s.add_argument("-k", type=int, default=5); s.add_argument("--json", action="store_true")
    s.add_argument("--log", default=DEFAULT_LOG); with_corpus(s); s.set_defaults(func=cmd_search)
    s = sub.add_parser("ask", help="cited extractive answer or abstention")
    s.add_argument("question"); s.add_argument("--json", action="store_true")
    s.add_argument("--log", default=DEFAULT_LOG); with_corpus(s); s.set_defaults(func=cmd_ask)
    s = sub.add_parser("assess", help="risk-tier assessment of a questionnaire")
    s.add_argument("file"); s.add_argument("--json", action="store_true")
    s.add_argument("--log", default=DEFAULT_LOG); s.set_defaults(func=cmd_assess)
    s = sub.add_parser("evaluate", help="Recall@k, MRR, nDCG and abstention on a question set")
    s.add_argument("questions"); s.add_argument("--json", help="write the report to this file")
    s.add_argument("--tests", help="test summary to include in the report"); with_corpus(s)
    s.set_defaults(func=cmd_evaluate)
    s = sub.add_parser("register", help="validate AI system records; export the transparency register")
    s.add_argument("path"); s.add_argument("--export"); s.add_argument("--lang", choices=["en", "bn"], default="en")
    s.set_defaults(func=cmd_register)
    s = sub.add_parser("verify-log", help="verify the hash chain of an audit log")
    s.add_argument("path"); s.set_defaults(func=cmd_verify_log)
    s = sub.add_parser("serve", help="run the JSON HTTP API")
    s.add_argument("--host", default="127.0.0.1"); s.add_argument("--port", type=int, default=8080)
    s.add_argument("--log", default=DEFAULT_LOG); with_corpus(s); s.set_defaults(func=cmd_serve)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
