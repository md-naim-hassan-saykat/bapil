"""Risk-tier assessment (Blueprint Chapter 13, Annex B and Table 39).

Rules
-----
* Any prohibited-use flag -> T0 (Prohibited).
* Otherwise T3 (High) if the total score is at least 13, or D1 = 3, or D2 = 3,
  or both D2 and D3 are at least 2.
* Otherwise T2 (Limited) if the total is at least 6, or D1 = 2, or D7 is at least 2.
* Otherwise T1 (Low).
"""
from dataclasses import asdict, dataclass, field

PROHIBITED = {
    "social_scoring": "Scores or ranks individuals for general social trustworthiness or behaviour",
    "mass_biometric_surveillance": "Mass or indiscriminate biometric identification or surveillance",
    "opinion_profiling": "Infers or profiles political opinions, religious beliefs or similar characteristics",
    "deceptive_synthetic_media": "Generates deceptive synthetic media depicting real people",
    "manipulation_of_vulnerabilities": "Uses manipulative techniques exploiting age, disability or hardship",
}

DIMENSIONS = {
    "D1": "Influence on decisions",
    "D2": "Data sensitivity",
    "D3": "People potentially affected",
    "D4": "Reversibility of harm",
    "D5": "Degree of automation",
    "D6": "Vulnerability of affected groups",
    "D7": "Exposure",
}

TIER_NAMES = {"T0": "Prohibited", "T1": "Low", "T2": "Limited", "T3": "High"}

CONTROLS = {
    "T0": ["Not built, not piloted, not supported by BAPIL under any arrangement"],
    "T1": ["AI system record", "Model or data card", "Evaluation report", "Audit logging",
           "Public listing in the transparency register"],
    "T2": ["All T1 controls", "ERRC review", "Red-team test", "Human review of every output in use",
           "User training", "Incident procedure", "Quarterly monitoring report"],
    "T3": ["Research only: BAPIL does not build T3 operational systems", "DPIA", "Legal review",
           "Independent audit", "ERRC approval (binding)", "Published impact assessment"],
}

APPROVERS = {"T0": "Excluded by charter", "T1": "Unit lead and TAB", "T2": "ERRC and Steering Board",
             "T3": "ERRC (binding) and host-agency legal review"}


class AssessmentError(ValueError):
    pass


@dataclass
class Assessment:
    system_id: str
    tier: str
    tier_name: str
    total: int
    scores: dict
    reasons: list = field(default_factory=list)
    controls: list = field(default_factory=list)
    approver: str = ""

    def to_dict(self):
        return asdict(self)


def assess(questionnaire):
    """Assess a questionnaire dict: {"system_id", "prohibited": {...}, "scores": {"D1": 0..3, ...}}."""
    sid = questionnaire.get("system_id", "UNSPECIFIED")
    flags = questionnaire.get("prohibited", {}) or {}
    unknown = set(flags) - set(PROHIBITED)
    if unknown:
        raise AssessmentError("unknown prohibited-use flags: %s" % sorted(unknown))
    raised = [k for k, v in flags.items() if v]
    scores = questionnaire.get("scores", {}) or {}
    missing = [d for d in DIMENSIONS if d not in scores]
    if raised:
        reasons = ["Prohibited use: %s" % PROHIBITED[k] for k in raised]
        return Assessment(sid, "T0", TIER_NAMES["T0"], sum(int(v) for v in scores.values()),
                          scores, reasons, CONTROLS["T0"], APPROVERS["T0"])
    if missing:
        raise AssessmentError("missing scores for: %s" % missing)
    for d, v in scores.items():
        if d not in DIMENSIONS:
            raise AssessmentError("unknown dimension %s" % d)
        if not isinstance(v, int) or not 0 <= v <= 3:
            raise AssessmentError("%s must be an integer from 0 to 3" % d)
    s = scores
    total = sum(s.values())
    reasons = []
    if total >= 13:
        reasons.append("Total score %d is at least 13" % total)
    if s["D1"] == 3:
        reasons.append("D1 = 3: informs or automates decisions about specific people or entities")
    if s["D2"] == 3:
        reasons.append("D2 = 3: sensitive personal or restricted data")
    if s["D2"] >= 2 and s["D3"] >= 2:
        reasons.append("D2 and D3 at least 2: personal data at scale")
    if reasons:
        tier = "T3"
    else:
        if total >= 6:
            reasons.append("Total score %d is at least 6" % total)
        if s["D1"] == 2:
            reasons.append("D1 = 2: informs official decisions on policies or programmes")
        if s["D7"] >= 2:
            reasons.append("D7 at least 2: public-facing")
        tier = "T2" if reasons else "T1"
        if tier == "T1":
            reasons.append("No limited or high-risk condition applies (total %d)" % total)
    return Assessment(sid, tier, TIER_NAMES[tier], total, scores, reasons, CONTROLS[tier], APPROVERS[tier])
