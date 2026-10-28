"""AI system register and public transparency register (Blueprint FR-06, FR-09, Annex C).

Records are JSON files that follow ``schemas/ai_system_record.schema.json``. Validation
here is a dependency-free subset of that schema (required fields, enumerations and
types), so the register can be checked anywhere; the full schema can also be used with
any JSON Schema validator.
"""
import json
import os

REQUIRED = ["system_id", "name", "purpose", "owner", "maturity_class", "risk_tier", "data_classes",
            "gate_status", "limitations", "contact"]
ENUMS = {
    "maturity_class": {"R", "A", "O"},
    "risk_tier": {"T0", "T1", "T2", "T3"},
}
DATA_CLASSES = {"DC0", "DC1", "DC2", "DC3"}
GATES = {"G0", "G1", "G2", "G3", "G4", "G5"}


def validate(record):
    """Return a list of validation errors (empty when the record is valid)."""
    errs = []
    for f in REQUIRED:
        if f not in record:
            errs.append("missing field: %s" % f)
    for f, allowed in ENUMS.items():
        if f in record and record[f] not in allowed:
            errs.append("%s must be one of %s" % (f, sorted(allowed)))
    name = record.get("name", {})
    if not isinstance(name, dict) or not name.get("en"):
        errs.append("name must contain at least an 'en' value")
    dc = record.get("data_classes", [])
    if not isinstance(dc, list) or not dc or any(c not in DATA_CLASSES for c in dc):
        errs.append("data_classes must be a non-empty list of DC0..DC3")
    gs = record.get("gate_status", {})
    if not isinstance(gs, dict) or gs.get("gate") not in GATES or not gs.get("date"):
        errs.append("gate_status needs 'gate' (G0..G5) and 'date'")
    if record.get("risk_tier") == "T0":
        errs.append("tier T0 systems are prohibited and cannot be registered")
    if record.get("risk_tier") == "T3" and record.get("maturity_class") != "R":
        errs.append("tier T3 systems may only exist as research prototypes (class R)")
    if "DC3" in dc:
        errs.append("data class DC3 is excluded from BAPIL work")
    return errs


def load_records(path):
    files = [path] if os.path.isfile(path) else sorted(
        os.path.join(path, f) for f in os.listdir(path) if f.endswith(".json"))
    records = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            records.append(json.load(fh))
    return records


def transparency_register(records, lang="en"):
    """Render the public transparency register as Markdown."""
    if lang == "bn":
        head = ("# এআই ব্যবস্থার স্বচ্ছতা নিবন্ধন\n\n"
                "| আইডি | নাম | উদ্দেশ্য | শ্রেণি | স্তর | ডেটা | সর্বশেষ গেট | সীমাবদ্ধতা | যোগাযোগ |\n"
                "|---|---|---|---|---|---|---|---|---|\n")
    else:
        head = ("# AI System Transparency Register\n\n"
                "| ID | Name | Purpose | Class | Tier | Data | Latest gate | Limitations | Contact |\n"
                "|---|---|---|---|---|---|---|---|---|\n")
    rows = []
    for r in sorted(records, key=lambda x: x["system_id"]):
        name = r["name"].get(lang) or r["name"]["en"]
        purpose = r["purpose"].get(lang) if isinstance(r["purpose"], dict) else r["purpose"]
        purpose = purpose or (r["purpose"]["en"] if isinstance(r["purpose"], dict) else "")
        lim = r["limitations"].get(lang) if isinstance(r["limitations"], dict) else r["limitations"]
        lim = lim or (r["limitations"]["en"] if isinstance(r["limitations"], dict) else "")
        gate = "%s (%s)" % (r["gate_status"]["gate"], r["gate_status"]["date"])
        cells = [r["system_id"], name, purpose, r["maturity_class"], r["risk_tier"],
                 ", ".join(r["data_classes"]), gate, lim, r["contact"]]
        rows.append("| " + " | ".join(str(c).replace("|", "/") for c in cells) + " |")
    return head + "\n".join(rows) + "\n"
