**Table 55.** Risk register

| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|------|-------------------------|----------|--------|---------------------------------|--------------|
| R1 | Political or institutional change shifts priorities | M | H | Institution-neutral design; university host; alignment with the national AI policy process; cross-party briefings | Director, Steering Board |
| R2 | Delays in data access, including bulk document export | H | H | Confirm access in Phase 0; start with documents already public, by assisted manual download where automated retrieval is not permitted and through university law libraries; NRDEX agreements; RTI requests as fallback | Data lead |
| R3 | Poor text quality from scanned Bangla PDFs | H | M | OCR evaluation; human correction loops; prioritise born-digital sources | ML lead |
| R4 | Incorrect answers mislead officials | M | H | Extractive-first answers; mandatory citations; abstention; training; classes R and A only | ML lead, ERRC |
| R5 | Privacy breach or misuse of personal data | L | H | DC0-first; DPIA; access control; independent audits | Security lead, governance analyst |
| R6 | Mission creep toward surveillance | L | H | T0 list in charter; ERRC veto; public transparency register | ERRC |
| R7 | Talent shortage or loss of staff | H | M | Fellowships; diaspora partnerships; competitive terms; remote collaboration | Director |
| R8 | Funding gaps between phases | M | H | Diversified funding (White Paper Appendix C); phased commitments | Steering Board |
| R9 | Duplication with the AI Hub or other initiatives | M | M | MoU on division of labour; shared benchmarks and data | Director |
| R10 | Vendor or model lock-in | M | M | Open standards; open-weight models; portable containers; code in national repository | Platform lead |
| R11 | Cyber attack on the platform | M | H | NIST CSF 2.0 controls; penetration tests; offline backups and restore drills | Security lead |
| R12 | Low adoption by officials | M | H | Co-design with users; training; measure time saved; product owners in agencies | Policy lead |
| R13 | Legal uncertainty while implementing rules are issued | M | M | Legal review; conservative data scope; update procedures as rules are published | Governance analyst |
| R14 | Tools or outputs misused for misinformation or partisan purposes | L | H | Access control for official tools; no synthetic media generation; usage policy; audit logs; public register | ERRC |
| R15 | Benchmark contamination or overfitting to the test set | M | M | Private held-out test split; versioned freezing; periodic refresh; report on several sets | ML lead |
| R16 | Dependence on a few key people | H | H | Documentation and open code; deputies for key roles; succession plan; shared ownership with the host | Steering Board |
| R17 | Technology obsolescence over the long horizon | M | M | Modular design and ADRs; model re-selection at reviews; investment in data and evaluation rather than one model | TAB |
| R18 | Floods, cyclones, power or network outages affecting hosting | M | H | Disaster-recovery site; offline backups; recovery targets of Table 35; low-bandwidth design | Platform lead |

*Note.* L = low, M = medium, H = high. The register is reviewed quarterly by the Steering Board. Early-warning indicators, contingencies, residual ratings and review frequencies are given in Annex U (Table 67).
