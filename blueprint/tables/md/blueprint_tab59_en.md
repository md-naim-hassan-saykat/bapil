**Table 59.** Risk-tier questionnaire: scored dimensions (Annex B)

| Code | Dimension | Score 0 | Score 1 | Score 2 | Score 3 |
|------|-------------------|---------------|---------------|---------------|---------------|
| D1 | Influence on decisions | Research only | Informs analysts | Informs official decisions on policies or programmes | Informs or automates decisions about specific people or entities |
| D2 | Data sensitivity | P0 public | P1 internal, non-personal | P2 personal | P3 sensitive personal or restricted |
| D3 | People potentially affected | None or internal | Fewer than 10,000 | 10,000 to 1 million | More than 1 million |
| D4 | Reversibility of harm | Trivially reversible | Reversible with effort | Hard to reverse | Irreversible |
| D5 | Degree of automation | Suggestions on request | Person reviews every output | Person reviews samples | Fully automated |
| D6 | Vulnerability of affected groups | No affected individuals | General public | Includes vulnerable groups | Targets vulnerable groups |
| D7 | Exposure | Internal researchers | Officials | Public information | Public guidance with consequences |

*Note.* Tier rules: any prohibited-use flag gives T0. Otherwise T3 if total at least 13, or D1 = 3, or D2 = 3, or both D2 and D3 at least 2; T2 if total at least 6, or D1 = 2, or D7 at least 2; else T1. Implemented in bapil.risk.
