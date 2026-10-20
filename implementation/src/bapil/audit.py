"""Tamper-evident audit log (Blueprint GR-04, component C10).

Each line is a JSON object holding the event, a UTC timestamp, the hash of the previous
entry and its own hash: ``sha256(prev_hash + canonical_json(entry_without_hash))``.
Changing, deleting or reordering any earlier line breaks every later hash, which
``verify`` detects.
"""
import datetime as _dt
import hashlib
import json
import os

GENESIS = "0" * 64


def _canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _last_hash(path):
    if not os.path.exists(path):
        return GENESIS
    last = None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                last = line
    return json.loads(last)["hash"] if last else GENESIS


class AuditLog:
    def __init__(self, path):
        self.path = path
        d = os.path.dirname(os.path.abspath(path))
        os.makedirs(d, exist_ok=True)

    def append(self, event_type, payload):
        prev = _last_hash(self.path)
        entry = {"ts": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
                 "type": event_type, "payload": payload, "prev": prev}
        entry["hash"] = hashlib.sha256((prev + _canonical(entry)).encode("utf-8")).hexdigest()
        with open(self.path, "a", encoding="utf-8") as fh:
            fh.write(_canonical(entry) + "\n")
        return entry["hash"]


def verify(path):
    """Return (ok, number_of_entries, first_bad_line_number_or_None)."""
    prev = GENESIS
    n = 0
    with open(path, encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            if not line.strip():
                continue
            n += 1
            try:
                entry = json.loads(line)
            except ValueError:
                return False, n, lineno
            h = entry.pop("hash", None)
            if entry.get("prev") != prev:
                return False, n, lineno
            calc = hashlib.sha256((prev + _canonical(entry)).encode("utf-8")).hexdigest()
            if calc != h:
                return False, n, lineno
            prev = h
    return True, n, None
