#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the publishable Markdown documents from the source templates.

Fills in tables, figures, metadata, demonstration results and the reference list,
then writes the final Markdown files to blueprint/.

Markers in *.src.md:
  <!-- TABLE:NN -->    replaced by tables/md/blueprint_tabNN_<lang>.md
  <!-- FIGURE:NN -->   replaced by the figure image and its numbered caption
  {{DATE}} {{ORCID}} {{DOI_LINK}} {{DOI_SHORT}} {{SUMMARY_DOI_LINK}} {{RELEASE}} {{EVAL_RESULTS}} {{REFERENCES}}
"""
import json
import os
import re
import sys

from typography import normalise
import refnum

HERE = os.path.dirname(os.path.abspath(__file__))
BP = os.path.dirname(HERE)            # blueprint/
REPO = os.path.dirname(BP)            # repository root
BN_DIGITS = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")

DOCS = [
    ("BAPIL_Technical_Blueprint_en", "en"),
    ("BAPIL_Technical_Blueprint_bn", "bn"),
    ("BAPIL_Blueprint_Summary_en", "en"),
    ("BAPIL_Blueprint_Summary_bn", "bn"),
]

CAPTIONS = {
    "01": {"en": "The BAPIL document family: from the White Paper to a tested implementation and controlled pilots.",
           "bn": "BAPIL নথি-পরিবার: হোয়াইট পেপার থেকে পরীক্ষিত বাস্তবায়ন ও নিয়ন্ত্রিত পাইলট পর্যন্ত।"},
    "02": {"en": "Indicative stakeholder map by influence and interest, used to plan engagement.",
           "bn": "প্রভাব ও আগ্রহভিত্তিক নির্দেশক অংশীজন-মানচিত্র, যা সম্পৃক্ততা পরিকল্পনায় ব্যবহৃত।"},
    "03": {"en": "Proposed institutional and governance model (Option C: university-anchored lab with a government MoU).",
           "bn": "প্রস্তাবিত প্রাতিষ্ঠানিক ও শাসন-মডেল (বিকল্প গ: সরকারি সমঝোতা স্মারকসহ বিশ্ববিদ্যালয়-ভিত্তিক ল্যাব)।"},
    "04": {"en": "BAPIL reference architecture: twelve components in four layers, with cross-cutting governance and security.",
           "bn": "BAPIL রেফারেন্স স্থাপত্য: চার স্তরে বারোটি উপাদান, সঙ্গে সর্বস্তরীয় শাসন ও নিরাপত্তা।"},
    "05": {"en": "Request sequence for a cited answer, from the user’s query to the audit record.",
           "bn": "উদ্ধৃতিযুক্ত উত্তরের অনুরোধ-ক্রম: ব্যবহারকারীর প্রশ্ন থেকে নিরীক্ষা-রেকর্ড পর্যন্ত।"},
    "06": {"en": "Data lifecycle under data governance, from acquisition to retention or disposal.",
           "bn": "ডেটা শাসনের অধীনে ডেটার জীবনচক্র: সংগ্রহ থেকে সংরক্ষণ বা নিষ্পত্তি পর্যন্ত।"},
    "07": {"en": "Bilingual, citation-grounded retrieval pipeline: the system answers with citations or abstains.",
           "bn": "দ্বিভাষিক, উদ্ধৃতিভিত্তিক উদ্ধার-প্রক্রিয়া: ব্যবস্থা উদ্ধৃতিসহ উত্তর দেয় অথবা বিরত থাকে।"},
    "08": {"en": "Staged, evidence-gated development path for the Bangla Policy Foundation Model (BPFM).",
           "bn": "বাংলা নীতি ফাউন্ডেশন মডেলের (BPFM) প্রমাণনির্ভর, পর্যায়ভিত্তিক উন্নয়ন-পথ।"},
    "09": {"en": "Indicative deployment topology and security zones, hosted in Bangladesh.",
           "bn": "বাংলাদেশে হোস্টকৃত নির্দেশক প্রয়োগ-বিন্যাস ও নিরাপত্তা অঞ্চল।"},
    "10": {"en": "Risk-tier decision flow, applied at Gate G0 and repeated at every gate.",
           "bn": "ঝুঁকি-স্তর নির্ধারণের প্রবাহ, গেট G0-তে প্রয়োগ এবং প্রতিটি গেটে পুনরাবৃত্তি।"},
    "11": {"en": "Lifecycle gates G0 to G5 and the evidence required at each gate.",
           "bn": "জীবনচক্র-গেট G0 থেকে G5 এবং প্রতিটি গেটে প্রয়োজনীয় প্রমাণ।"},
    "12": {"en": "Indicative 36-month delivery roadmap (Month 1 is the first month in which the MoU, the host agreement and Year 1 funding are all in place, after Phase 0; indicative Month 1: July 2027).",
           "bn": "নির্দেশক ৩৬ মাসের বাস্তবায়ন রোডম্যাপ (ধাপ ০-এর পরে সমঝোতা স্মারক, স্বাগতিক-চুক্তি ও প্রথম বছরের অর্থায়ন তিনটিই নিশ্চিত হওয়ার প্রথম মাসই মাস ১; নির্দেশক মাস ১: জুলাই ২০২৭)।"},
    "13": {"en": "Strategic roadmap, 2026 to 2041 and beyond: horizons, workstreams and review points.",
           "bn": "কৌশলগত রোডম্যাপ, ২০২৬ থেকে ২০৪১ ও তার পরে: দিগন্ত, কর্মধারা ও পর্যালোচনা-বিন্দু।"},
    "14": {"en": "Theory of change: from inputs to impact, with key assumptions and a learning loop.",
           "bn": "পরিবর্তনের তত্ত্ব: উপকরণ থেকে প্রভাব পর্যন্ত, মূল অনুমান ও শিক্ষণ-চক্রসহ।"},
    "15": {"en": "Risk heat map of the eighteen registered risks by likelihood and impact.",
           "bn": "সম্ভাবনা ও প্রভাব অনুযায়ী নিবন্ধিত আঠারোটি ঝুঁকির তাপ-মানচিত্র।"},
    "16": {"en": "Integrated institutional and financial pathway: form, government role, posts, budget and funding mix by stage, with the gates between stages. A preparatory Phase 0 (about Tk 0.44 crore) precedes Year 1 (Table 71).",
           "bn": "সমন্বিত প্রাতিষ্ঠানিক ও আর্থিক পথনকশা: পর্যায়ভিত্তিক রূপ, সরকারের ভূমিকা, পদ, বাজেট ও অর্থায়নের মিশ্রণ, পর্যায়গুলোর মধ্যকার গেটসহ। বছর ১-এর আগে একটি প্রস্তুতিমূলক ধাপ ০ (প্রায় ০.৪৪ কোটি টাকা) রয়েছে (সারণি ৭১)।"},
}


def load(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def bn(n):
    return str(n).translate(BN_DIGITS)


def doi_values(meta, lang, key="doi"):
    doi = meta.get(key, "10.5281/zenodo.PENDING")
    if "PENDING" in doi:
        link = ("DOI to be assigned on publication" if lang == "en"
                else "প্রকাশের সময় নির্ধারিত হবে")
        return link, ("DOI pending" if lang == "en" else "DOI প্রক্রিয়াধীন")
    return "<https://doi.org/%s>" % doi, doi


def eval_block(lang):
    path = os.path.join(REPO, "implementation", "build", "eval_report.json")
    if not os.path.exists(path):
        return ("*Results are generated by `bapil.cli evaluate` during the build.*" if lang == "en"
                else "*ফলাফল বিল্ডের সময় `bapil.cli evaluate` দ্বারা তৈরি হয়।*")
    r = json.load(open(path, encoding="utf-8"))
    rows = []
    if lang == "en":
        hdr = "| Question set | Questions | Recall@5 | Recall@10 | MRR@10 | nDCG@10 |\n|---|---|---|---|---|---|"
        names = {"all": "All questions", "en": "English questions", "bn": "Bangla questions"}
    else:
        hdr = "| প্রশ্নসেট | প্রশ্ন | Recall@5 | Recall@10 | MRR@10 | nDCG@10 |\n|---|---|---|---|---|---|"
        names = {"all": "সব প্রশ্ন", "en": "ইংরেজি প্রশ্ন", "bn": "বাংলা প্রশ্ন"}
    for key in ("all", "en", "bn"):
        m = r["subsets"].get(key)
        if not m:
            continue
        vals = [m["n"], m["recall@5"], m["recall@10"], m["mrr@10"], m["ndcg@10"]]
        cells = [str(vals[0])] + ["%.2f" % v for v in vals[1:]]
        if lang == "bn":
            cells = [bn(c) for c in cells]
        rows.append("| %s | %s |" % (names[key], " | ".join(cells)))
    ab = r.get("abstention", {})
    if lang == "en":
        intro = ("Running `python -m bapil.cli evaluate benchmarks/demo_questions.json` over a corpus of %s passages "
                 "from %d BAPIL documents gives the following results (corpus version `%s`):"
                 % ("{:,}".format(r["corpus"]["passages"]), r["corpus"]["documents"], r["corpus"]["version"]))
        tail = ("Correct abstention on %d out-of-scope questions: %.2f. Unit tests: %s."
                % (ab.get("n", 0), ab.get("rate", 0.0), r.get("tests", "see CI")))
    else:
        intro = ("`python -m bapil.cli evaluate benchmarks/demo_questions.json` কমান্ডটি %sটি BAPIL নথির %sটি অনুচ্ছেদের কর্পাসে "
                 "চালালে নিচের ফলাফল পাওয়া যায় (কর্পাস সংস্করণ `%s`):"
                 % (bn(r["corpus"]["documents"]), bn("{:,}".format(r["corpus"]["passages"])), r["corpus"]["version"]))
        tail = ("আওতাবহির্ভূত %sটি প্রশ্নে সঠিক বিরতির হার: %s। ইউনিট পরীক্ষা: %s।"
                % (bn(ab.get("n", 0)), bn("%.2f" % ab.get("rate", 0.0)), _tests_bn(r.get("tests", ""))))
    return intro + "\n\n" + hdr + "\n" + "\n".join(rows) + "\n\n" + tail


def _tests_bn(t):
    m = re.match(r"(\d+) passed", t or "")
    return ("%sটি পরীক্ষা উত্তীর্ণ" % bn(m.group(1))) if m else "CI দেখুন"


# Corrections to White Paper references found when each cited entry was re-checked against its source
# on 22 October 2026 (see blueprint/review/REFERENCE_VERIFICATION.md).
WP_CORRECTIONS = {
    1: [("Paris: OECD, 2019[", "Paris: OECD, 2019 (amended 2023 and 2024)[")],
    21: [("DOI: 10.18356/237d52b2-en.", "DOI: 10.18356/9789211067286.")],
    29: [("Perspective Plan of Bangladesh 2021–2041: Making Vision 2041 a Reality[EB/OL].",
          "Making Vision 2041 a Reality: Perspective Plan of Bangladesh 2021–2041[EB/OL]."),
         ("Government of Bangladesh, 2021[", "Government of Bangladesh, 2020[")],
    30: [("Smart Bangladesh: ICT Master Plan 2041[EB/OL].", "Smart Bangladesh: ICT Master Plan 2041 (Draft)[EB/OL]."),
         ("Government of the People’s Republic of Bangladesh, 2024[", "Government of the People’s Republic of Bangladesh, undated[")],
    31: [("Statistical Yearbook of Bangladesh 2024[EB/OL].", "Bangladesh Statistical Yearbook 2024 (44th edition)[EB/OL].")],
    32: [("e-Nothi Impact Study[R/OL].", "Impact and Institutionalization of the e-Nothi System in Bangladesh[R/OL]."),
         ("Aspire to Innovate (a2i), 2025[", "Aspire to Innovate (a2i), ICT Division and UNDP, 2024[")],
    36: [("Koica and ICT Division launch $28.5 million AI innovation project in Bangladesh[EB/OL].",
          "KOICA and ICT Division launch $28.5million AI innovation project[EB/OL]."),
         ("The Business Standard, 2025[", "The Business Standard, 2025-01-09[")],
    49: [("ZEHADY A K, MAMUN S A, ISLAM N, et al.", "ZEHADY A K, DIPTA S R, ISLAM N, et al."),
         ("BongLLaMA: LLaMA for Bangla Language[R/OL].", "BanglaLlama: LLaMA for Bangla Language (first version titled BongLLaMA)[R/OL]."),
         ("Dhaka: BanglaLLM Research Initiative, 2024[", "Ithaca, NY: arXiv, 2024 (revised 2025)[")],
    50: [("The Foundation Model Transparency Index v1.1: May 2024[R/OL].",
          "The 2024 Foundation Model Transparency Index (first version titled The Foundation Model Transparency Index v1.1: May 2024)[R/OL].")],
    57: [("E-ESTONIA BRIEFING CENTRE.", "ESTONIAN BUSINESS AND INNOVATION AGENCY (e-Estonia)."),
         ("Tallinn: e-Estonia Briefing Centre, 2024[", "Tallinn: Estonian Business and Innovation Agency, 2024[")],
    59: [("E-ESTONIA BRIEFING CENTRE.", "ESTONIAN BUSINESS AND INNOVATION AGENCY (e-Estonia)."),
         ("Tallinn: e-Estonia Briefing Centre, 2024[", "Tallinn: Estonian Business and Innovation Agency, 2024[")],
    63: [("Leading the Way into the Era of Artificial Intelligence: Final Report of Finland’s Artificial Intelligence Programme[R/OL].",
          "Leading the Way into the Age of Artificial Intelligence: Final Report of Finland’s Artificial Intelligence Programme 2019[R/OL].")],
    64: [("UNIVERSITY OF HELSINKI, REAKTOR.", "UNIVERSITY OF HELSINKI, MINNALEARN."),
         ("Helsinki: University of Helsinki and Reaktor, 2024[", "Helsinki: University of Helsinki and MinnaLearn, 2024[")],
    # 23 October 2026: "(TBS)" dropped, because the reference lists also use TBS for The Business Standard
    # 23 October 2026: the May 2024 PDF address now returns 404 (the publisher moved the file); the entry
    # cites the framework's page on the publisher's site, which links the current PDF
    53: [("<https://aiverifyfoundation.sg/wp-content/uploads/2024/05/Model-AI-Governance-Framework-for-Generative-AI-May-2024-1-1.pdf>",
          "<https://aiverifyfoundation.sg/resources/mgf-gen-ai/>"),
         ("2024[2026-06-18]", "2024[2026-10-23]")],
    68: [("TREASURY BOARD OF CANADA SECRETARIAT (TBS).", "TREASURY BOARD OF CANADA SECRETARIAT.")],
    69: [("TREASURY BOARD OF CANADA SECRETARIAT (TBS).", "TREASURY BOARD OF CANADA SECRETARIAT."),
         ("Algorithmic Impact Assessment (AIA) Tool[EB/OL].", "Algorithmic Impact Assessment[EB/OL]."),
         ("Ottawa: Government of Canada, 2026[", "Ottawa: Government of Canada, 2026-09-15[")],
}
# Entries whose source page was opened and checked on 22 October 2026 (access date updated)
WP_VERIFIED_20261022 = {4, 6, 7, 14, 17, 21, 23, 26, 29, 30, 31, 32, 33, 35, 36, 38, 46, 48, 49, 50, 51, 53, 54,
                        57, 59, 60, 61, 64, 65, 69, 71, 78, 79, 80, 83}


def wp_references():
    """Parse the White Paper reference list into {number: text}."""
    text = load(os.path.join(REPO, "reports", "BAPIL_White_Paper_v1.md"))
    sec = text.split("\n# References", 1)[1].split("\n# Contact", 1)[0]
    refs = {}
    for block in re.split(r"\n(?=\[\d+\] )", sec):
        m = re.match(r"\[(\d+)\] ", block.strip())
        if m:
            body = block.strip()
            body = re.sub(r"\n#+ .*", "", body).strip()
            # drop layout commands that follow the last entry in the White Paper source
            body = re.sub(r"\n\s*(\\newpage|\\clearpage|---)\s*$", "", body).strip()
            refs[int(m.group(1))] = body
    # correction: co-author of the RAG paper [38] is A. Piktus
    if 38 in refs:
        refs[38] = refs[38].replace("POYIADZI E", "PIKTUS A")
    # quotation-mark convention of the Blueprint (the White Paper source is not edited)
    refs = {n: normalise(body) for n, body in refs.items()}
    # corrections from the re-verification of 22 October 2026 (the White Paper source is not edited)
    for key, pairs in WP_CORRECTIONS.items():
        if key in refs:
            for a, b in pairs:
                if a not in refs[key]:
                    raise SystemExit("White Paper reference [%d]: text to correct not found: %r" % (key, a))
                refs[key] = refs[key].replace(a, b)
    for key in WP_VERIFIED_20261022:
        if key in refs:
            refs[key] = re.sub(r"\[2026-0[67]-\d\d\]", "[2026-10-22]", refs[key])
    return refs


def new_references():
    refs = {}
    for block in re.split(r"\n\s*\n", load(os.path.join(HERE, "refs_new.md")).strip()):
        m = re.match(r"\[(\d+)\] ", block.strip())
        if m:
            refs[int(m.group(1))] = block.strip()
    return refs


def all_references():
    refs = wp_references()
    refs.update(new_references())
    return refs


def reference_mapping(name, lang, text):
    """{source key: published number}; see refnum.py."""
    allrefs = all_references()
    body = text.split("{{REFERENCES}}")[0]
    order = refnum.first_citation_order(body)
    missing = sorted(k for k in order if k not in allrefs)
    if missing:
        raise SystemExit("%s: cited but undefined reference keys: %s" % (name, missing))
    if name.startswith("BAPIL_Technical_Blueprint"):
        mapping = refnum.blueprint_map()
        extra = sorted(set(order) - set(mapping))
        if extra:
            raise SystemExit("%s cites references the English edition does not: %s" % (name, extra))
        return mapping
    return refnum.make_map(order)


def reference_section(mapping, lang):
    allrefs = all_references()
    wp = any(k <= refnum.WP_LAST for k in mapping)
    if lang == "en":
        head = ("# References\n\nReferences are numbered in the order in which they are first cited, and only references "
                "cited in this document are listed.%s\n" % (" Entries marked with an asterisk (\\*) are taken from the bibliography of the BAPIL "
                "White Paper (Version 1.0)." if wp else ""))
    else:
        head = ("# তথ্যসূত্র\n\nতথ্যসূত্রগুলো প্রথম উদ্ধৃতির ক্রমে নম্বরযুক্ত, এবং শুধু এই নথিতে উদ্ধৃত তথ্যসূত্র তালিকাভুক্ত করা হয়েছে। "
                "%sআন্তর্জাতিক ব্যবহারের সুবিধার্থে তথ্যসূত্রগুলো মূল ভাষায় রাখা হয়েছে।\n"
                % ("তারকাচিহ্ন (\\*) দেওয়া তথ্যসূত্রগুলো BAPIL হোয়াইট পেপারের (সংস্করণ ১.০) তথ্যসূত্র-তালিকা থেকে নেওয়া। " if wp else ""))
    head += "\n\\bapilrealspaces\n"   # real space characters in the PDF text layer (header-common.tex)
    entries = []
    for key, num in sorted(mapping.items(), key=lambda kv: kv[1]):
        body = re.sub(r"^\[\d+\]\s*", "", allrefs[key])
        mark = "\\* " if key <= refnum.WP_LAST else ""   # asterisk, escaped for Markdown
        entries.append("[%d] %s%s" % (num, mark, body))
    if len(entries) > 40:   # the Blueprint only: tighter spacing between entries keeps the long list compact
        head += "\n\\setlength{\\parskip}{2pt plus 1pt minus 1pt}\n"
    return head + "\n" + "\n\n".join(entries) + "\n"


CITE_RE = re.compile(r"(?<![!\w\]])\[(\d[\d,\s\-]*)\](?![(\[])")


def bn_citations(text):
    """Bangla editions: write citation numbers such as [84, 85] and the reference
    labels in Bangla digits. Code blocks and inline code are left untouched."""
    parts = re.split(r"(```.*?```|`[^`\n]*`)", text, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = CITE_RE.sub(lambda m: "[%s]" % bn(m.group(1)), parts[i])
    return "".join(parts)


def figure_md(fid, lang, width=None):
    suffix = "" if lang == "en" else "_bn"
    label = ("Figure %d." % int(fid)) if lang == "en" else ("চিত্র %s।" % bn(int(fid)))
    attr = "{width=%s}" % width if width else ""   # optional, e.g. <!-- FIGURE:01 width=85% -->
    return "![](figures/blueprint_fig%s%s.png)%s\n\n*%s %s*" % (fid, suffix, attr, label, CAPTIONS[fid][lang])


def expand_includes(text, depth=0):
    """Replace <!-- INCLUDE:path --> (relative to src/) with the file's content."""
    if depth > 3:
        raise SystemExit("INCLUDE nested too deeply")
    return re.sub(r"<!-- INCLUDE:([\w./-]+) -->",
                  lambda m: expand_includes(load(os.path.join(HERE, m.group(1))).strip("\n"), depth + 1),
                  text)


def check_coverage(text, name):
    """Every generated table and figure should appear exactly once in the Blueprint."""
    tabs = re.findall(r"<!-- TABLE:(\d\d) -->", text)
    figs = re.findall(r"<!-- FIGURE:(\d\d)(?: width=\d+%)? -->", text)
    have_t = sorted(f[13:15] for f in os.listdir(os.path.join(BP, "tables", "md")) if f.endswith("_en.md"))
    for label, used, have in (("table", tabs, have_t), ("figure", figs, sorted(CAPTIONS))):
        dup = sorted({x for x in used if used.count(x) > 1})
        miss = [x for x in have if x not in used]
        order = [int(x) for x in used] != sorted(int(x) for x in used)
        if dup or miss or order:
            sys.stderr.write("WARNING %s: %s duplicates %s, missing %s, out of order %s\n" % (name, label, dup, miss, order))


def check_eval_claim(lang):
    """Table 60 quotes the demonstration Recall@10; stop if it no longer matches the evaluation report."""
    path = os.path.join(REPO, "implementation", "build", "eval_report.json")
    if not os.path.exists(path):
        return
    r10 = "%.2f" % json.load(open(path, encoding="utf-8"))["subsets"]["all"]["recall@10"]
    if lang == "bn":
        r10 = r10.translate(BN_DIGITS)
    table = load(os.path.join(BP, "tables", "md", "blueprint_tab60_%s.md" % lang))
    if ("Recall@10 of %s" % r10 if lang == "en" else "Recall@10 %s" % r10) not in table:
        raise SystemExit("Table 60 (%s) does not quote the current demonstration Recall@10 (%s); update src/tables_f.py"
                         % (lang, r10))


def assemble(name, lang, meta):
    src = os.path.join(HERE, name + ".src.md")
    if not os.path.exists(src):
        sys.stderr.write("skip (no source): %s\n" % src)
        return None
    text = expand_includes(load(src))
    if name.startswith("BAPIL_Technical_Blueprint"):
        check_coverage(text, name)
    # sequential reference numbers: citations in the text are rewritten here; the Blueprint's tables
    # were renumbered by make_tables.py with the same mapping, so they are inserted afterwards
    mapping = reference_mapping(name, lang, text)
    text = refnum.apply_map(text, mapping)
    text = re.sub(r"<!-- TABLE:(\d\d) -->",
                  lambda m: load(os.path.join(BP, "tables", "md", "blueprint_tab%s_%s.md" % (m.group(1), lang))).strip(),
                  text)
    text = re.sub(r"<!-- FIGURE:(\d\d)(?: width=(\d+%))? -->", lambda m: figure_md(m.group(1), lang, m.group(2)), text)
    link, short = doi_values(meta, lang)
    text = (text.replace("{{DATE}}", meta["date_" + lang]).replace("{{ORCID}}", meta["orcid"])
                .replace("{{DOI_LINK}}", link).replace("{{DOI_SHORT}}", short)
                .replace("{{SUMMARY_DOI_LINK}}", doi_values(meta, lang, "summary_doi")[0])
                .replace("{{RELEASE}}", meta["repo_release"]))
    if "{{EVAL_RESULTS}}" in text:
        text = text.replace("{{EVAL_RESULTS}}", eval_block(lang))
        check_eval_claim(lang)
    if "{{REFERENCES}}" in text:
        n = len(mapping)
        body = text.split("{{REFERENCES}}")[0]
        bad = sorted(k for k in refnum.first_citation_order(body) if k > n)
        if bad:
            raise SystemExit("%s: citation numbers beyond the reference list: %s" % (name, bad))
        text = text.replace("{{REFERENCES}}", reference_section(mapping, lang))
    if lang == "bn":
        text = bn_citations(text)
    leftover = re.findall(r"\{\{[A-Z_]+\}\}|<!-- (?:TABLE|FIGURE):", text)
    if leftover:
        raise SystemExit("unfilled markers in %s: %s" % (name, leftover[:5]))
    out = os.path.join(BP, name + ".md")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    return out


def main():
    meta = json.load(open(os.path.join(HERE, "metadata.json"), encoding="utf-8"))
    for name, lang in DOCS:
        out = assemble(name, lang, meta)
        if out:
            print("assembled", os.path.relpath(out, REPO))


if __name__ == "__main__":
    main()
