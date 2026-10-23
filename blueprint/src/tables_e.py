# -*- coding: utf-8 -*-
"""Blueprint tables added in the expanded edition: Part V (roadmap 2026-2041, financing, M&E, research)."""

import budget_model as _bm

_BN = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")
_CAT_BN = {
    "Core staff": "মূল জনবল",
    "Language editors and fellowships": "ভাষা-সম্পাদক ও ফেলোশিপ",
    "Compute and hosting": "কম্পিউটিং ও হোস্টিং",
    "Data and annotation": "ডেটা ও টীকাকরণ",
    "Training and outreach": "প্রশিক্ষণ ও সম্প্রসারণ",
    "Governance, audit and evaluation": "শাসন, নিরীক্ষা ও মূল্যায়ন",
    "Host overheads (10%)": "স্বাগতিকের পরোক্ষ ব্যয় (১০%)",
    "Contingency (5%)": "আপৎকালীন সংস্থান (৫%)",
}


def _budget_rows():
    rows = _bm.budget()
    by_year, total = _bm.totals()
    en, bn = [], []
    for k, v in rows.items():
        cells = ["%.2f" % _bm.crore(x) for x in v] + ["%.2f" % _bm.crore(sum(v)), "%.0f%%" % (100 * sum(v) / total)]
        en.append([k] + cells)
        bn.append([_CAT_BN[k]] + [c.translate(_BN) for c in cells])
    tot = ["**%.2f**" % _bm.crore(x) for x in by_year] + ["**%.2f**" % _bm.crore(total), "**100%**"]
    en.append(["**Total**"] + tot)
    bn.append(["**মোট**"] + [c.translate(_BN) for c in tot])
    return en, bn


_B_EN, _B_BN = _budget_rows()
_B_TOTAL = _bm.totals()[1]
_B_ROUNDED = sum(round(_bm.crore(x), 2) for x in _bm.totals()[0])
_B_UNROUNDED = format(round(_B_TOTAL), ",")


def _lakh(n):
    """Indian digit grouping (2,04,26,68,96) for the Bangla edition."""
    s = str(int(round(n)))
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts + [tail]) if parts else tail


_B_UNROUNDED_BN = _lakh(_B_TOTAL)
_B_USD = _B_TOTAL / _bm.BASE["usd_to_bdt"] / 1e6
_B_ROWS = _bm.budget()
# column sums of the rounded rows as printed (Years 1 to 3 and total)
_B_COLSUMS = tuple([sum(round(_bm.crore(v[y]), 2) for v in _B_ROWS.values()) for y in range(3)]
                   + [sum(round(_bm.crore(sum(v)), 2) for v in _B_ROWS.values())])

TABLES_E = [
    # ------------------------------------------------------------------ 45
    {
        "id": "45",
        "widths": [1.35, 1.05, 2.2, 3.4, 1.9, 2.1],
        "title": {"en": "Strategic horizons, 2026 to 2041 and beyond", "bn": "কৌশলগত দিগন্ত, ২০২৬ থেকে ২০৪১ ও তার পরে"},
        "cols": {"en": ["Horizon", "Period", "Strategic aim", "Priority actions", "Institutional form", "Signal to move on"],
                 "bn": ["দিগন্ত", "সময়কাল", "কৌশলগত লক্ষ্য", "অগ্রাধিকারমূলক পদক্ষেপ", "প্রাতিষ্ঠানিক রূপ", "পরবর্তী ধাপে যাওয়ার সংকেত"]},
        "rows": {
            "en": [
                ["**H0** Foundation", "Q4 2026", "Prepare a safe, open start", "Publish this Blueprint and code; brief the ICT Division and custodians; offer input to national AI policy drafting; fund Phase 0", "Independent research initiative", "Decisions D1 and D5 taken"],
                ["**H1** Short term", "2027 to 2028", "Prove value with public data", "Phase 0 (first half of 2027): host selection, legal review and costing; then charter, ERRC and register; P1 and P2 pilots; BanglaPolicyQA v0; 200 officials trained; mid-term evaluation", "University-anchored lab under MoU (Option C)", "P1 and P2 pass G3; positive mid-term evaluation"],
                ["**H2** Medium term", "2029 to 2030", "Adopt, scale and align with national policy", "G4 adoption of P1 and P2 by agencies; BPFM Stage 1 if justified; benchmark v1; Blueprint 2.0; align with the national AI policy cycle ending 2030", "Lab with multi-year core funding; agency service agreements", "Tools in operational use; sustained funding agreed"],
                ["**H3** Long term", "2031 to 2035", "Build a national policy-intelligence network", "Federated search across ministries and divisions; Bangla policy model maintained as a public good; standard assurance used across government; regional training hubs", "Consider an independent public-interest foundation (Option D) or statutory centre", "Assurance methods used beyond BAPIL; network in most ministries"],
                ["**H4** Vision", "2036 to 2041", "Trusted AI-enabled policy system for a knowledge economy", "Evidence services embedded in policy cycles; open Bangla language resources across domains; regional and South-South cooperation; contribution to Bangladesh’s long-term development goals and the SDGs", "Mature national institution with international partnerships", "Independent review at 2041 confirms public value"],
                ["**Beyond 2041**", "After 2041", "Keep the capability adaptive and accountable", "Periodic renewal of mission and charter; sunset or merger if the function is fully absorbed by government; preserve open archives", "Determined by the 2041 review", "Charter renewal decision"],
            ],
            "bn": [
                ["**H0** ভিত্তি", "চতুর্থ ত্রৈমাসিক ২০২৬", "নিরাপদ ও উন্মুক্ত সূচনার প্রস্তুতি", "এই ব্লুপ্রিন্ট ও কোড প্রকাশ; আইসিটি বিভাগ ও ডেটা-রক্ষকদের অবহিতকরণ; জাতীয় এআই নীতি প্রণয়নে উপকরণ প্রদান; ধাপ ০-এর অর্থায়ন", "স্বাধীন গবেষণা উদ্যোগ", "সিদ্ধান্ত D1 ও D5 গৃহীত"],
                ["**H1** স্বল্পমেয়াদি", "২০২৭ থেকে ২০২৮", "উন্মুক্ত ডেটা দিয়ে মূল্য প্রমাণ", "ধাপ ০ (২০২৭-এর প্রথমার্ধ): স্বাগতিক নির্বাচন, আইনি পর্যালোচনা ও ব্যয়-নিরূপণ; তারপর সনদ, ERRC ও নিবন্ধন; P1 ও P2 পাইলট; BanglaPolicyQA v0; ২০০ কর্মকর্তা প্রশিক্ষিত; মধ্যমেয়াদি মূল্যায়ন", "সমঝোতা স্মারকের অধীনে বিশ্ববিদ্যালয়-ভিত্তিক ল্যাব (বিকল্প গ)", "P1 ও P2 G3 উত্তীর্ণ; ইতিবাচক মধ্যমেয়াদি মূল্যায়ন"],
                ["**H2** মধ্যমেয়াদি", "২০২৯ থেকে ২০৩০", "গ্রহণ, সম্প্রসারণ ও জাতীয় নীতির সঙ্গে সামঞ্জস্য", "সংস্থাগুলোর দ্বারা P1 ও P2-এর G4 গ্রহণ; যৌক্তিক হলে BPFM পর্যায় ১; বেঞ্চমার্ক v1; ব্লুপ্রিন্ট ২.০; ২০৩০-এ সমাপ্য জাতীয় এআই নীতিচক্রের সঙ্গে সামঞ্জস্য", "বহুবর্ষী মূল অর্থায়নসহ ল্যাব; সংস্থার সঙ্গে সেবা-চুক্তি", "সরঞ্জাম পরিচালনাগত ব্যবহারে; টেকসই অর্থায়ন সম্মত"],
                ["**H3** দীর্ঘমেয়াদি", "২০৩১ থেকে ২০৩৫", "জাতীয় নীতি-বুদ্ধিমত্তা নেটওয়ার্ক গঠন", "মন্ত্রণালয় ও বিভাগজুড়ে সমন্বিত অনুসন্ধান; জনসম্পদ হিসেবে রক্ষিত বাংলা নীতি মডেল; সরকারজুড়ে প্রমিত আশ্বাস-পদ্ধতি; আঞ্চলিক প্রশিক্ষণ কেন্দ্র", "স্বাধীন জনস্বার্থ ফাউন্ডেশন (বিকল্প ঘ) বা সংবিধিবদ্ধ কেন্দ্র বিবেচনা", "BAPIL-এর বাইরেও আশ্বাস-পদ্ধতির ব্যবহার; অধিকাংশ মন্ত্রণালয়ে নেটওয়ার্ক"],
                ["**H4** রূপকল্প", "২০৩৬ থেকে ২০৪১", "জ্ঞানভিত্তিক অর্থনীতির জন্য আস্থাভাজন এআই-সমর্থিত নীতি-ব্যবস্থা", "নীতিচক্রে প্রমাণ-সেবার অন্তর্ভুক্তি; বিভিন্ন ক্ষেত্রে উন্মুক্ত বাংলা ভাষা-সম্পদ; আঞ্চলিক ও দক্ষিণ-দক্ষিণ সহযোগিতা; বাংলাদেশের দীর্ঘমেয়াদি উন্নয়ন-লক্ষ্য ও SDG-তে অবদান", "আন্তর্জাতিক অংশীদারত্বসহ পরিণত জাতীয় প্রতিষ্ঠান", "২০৪১-এর স্বাধীন পর্যালোচনায় জনমূল্য নিশ্চিত"],
                ["**২০৪১-এর পরে**", "২০৪১-এর পর", "সক্ষমতাকে অভিযোজনক্ষম ও জবাবদিহিমূলক রাখা", "মিশন ও সনদের পর্যায়ক্রমিক নবায়ন; কাজটি সরকারে পুরোপুরি আত্তীকৃত হলে সমাপ্তি বা একীভবন; উন্মুক্ত সংরক্ষণাগার রক্ষা", "২০৪১-এর পর্যালোচনায় নির্ধারিত", "সনদ নবায়নের সিদ্ধান্ত"],
            ],
        },
        "note": {"en": "Horizons H1 and H2 correspond to the 36-month roadmap of Chapter 15 (Phase 0 in the first half of 2027; indicative Month 1 in July 2027). Later horizons are strategic intentions, reviewed at the points in Table 48.",
                 "bn": "দিগন্ত H1 ও H2 অধ্যায় ১৫-এর ৩৬ মাসের রোডম্যাপের সঙ্গে সংগতিপূর্ণ (২০২৭-এর প্রথমার্ধে ধাপ ০; নির্দেশক মাস ১ জুলাই ২০২৭)। পরবর্তী দিগন্তগুলো কৌশলগত অভিপ্রায়, যা সারণি ৪৮-এর পর্যালোচনা-বিন্দুতে পুনর্বিবেচিত হবে।"},
    },
    # ------------------------------------------------------------------ 46
    {
        "id": "46",
        "widths": [3.0, 1.0, 1.1, 1.1, 1.2, 1.6],
        "title": {"en": "Indicative long-term targets by horizon", "bn": "দিগন্তভিত্তিক নির্দেশক দীর্ঘমেয়াদি লক্ষ্য"},
        "cols": {"en": ["Indicator", "2026", "2028", "2030", "2035", "2041"],
                 "bn": ["সূচক", "২০২৬", "২০২৮", "২০৩০", "২০৩৫", "২০৪১"]},
        "rows": {
            "en": [
                ["Public documents indexed with full provenance", "0", "15,000", "30,000", "100,000", "All public instruments in force"],
                ["Share of national laws in force searchable in Bangla and English with citations", "0%", "50%", "90%", "100%", "100%, updated within 7 days"],
                ["BanglaPolicyQA questions (all versions)", "0", "1,000", "2,300", "6,000", "Multi-domain, maintained"],
                ["Officials trained (cumulative)", "0", "200", "1,000", "5,500", "Part of public-service training"],
                ["Agencies using BAPIL tools or methods", "0", "3", "10", "30", "Most ministries and divisions"],
                ["Monthly active users of policy search", "0", "50", "500", "3,000", "Routine use across government"],
                ["Bangla and English Recall@10 gap (points)", "n/a", "Measured from v1 (month 30)", "5 or less", "3 or less", "2 or less"],
                ["AI systems listed in a public transparency register", "0", "6", "15", "Public-sector-wide register proposed", "Standard practice"],
                ["Independent evaluations published", "0", "1", "3", "8", "Every 5 years at least"],
                ["Open releases archived with a DOI", "3", "8", "15", "40", "Continuous"],
            ],
            "bn": [
                ["পূর্ণ উৎস-তথ্যসহ সূচিবদ্ধ উন্মুক্ত নথি", "০", "১৫,০০০", "৩০,০০০", "১,০০,০০০", "বলবৎ সব উন্মুক্ত দলিল"],
                ["বলবৎ জাতীয় আইনের যে অংশ উদ্ধৃতিসহ বাংলা ও ইংরেজিতে অনুসন্ধানযোগ্য", "০%", "৫০%", "৯০%", "১০০%", "১০০%, ৭ দিনের মধ্যে হালনাগাদ"],
                ["BanglaPolicyQA প্রশ্ন (সব সংস্করণ)", "০", "১,০০০", "২,৩০০", "৬,০০০", "বহু-ক্ষেত্রভিত্তিক, রক্ষিত"],
                ["প্রশিক্ষিত কর্মকর্তা (ক্রমপুঞ্জিত)", "০", "২০০", "১,০০০", "৫,৫০০", "জনপ্রশাসন প্রশিক্ষণের অংশ"],
                ["BAPIL-এর সরঞ্জাম বা পদ্ধতি ব্যবহারকারী সংস্থা", "০", "৩", "১০", "৩০", "অধিকাংশ মন্ত্রণালয় ও বিভাগ"],
                ["নীতি অনুসন্ধানের মাসিক সক্রিয় ব্যবহারকারী", "০", "৫০", "৫০০", "৩,০০০", "সরকারজুড়ে নিয়মিত ব্যবহার"],
                ["বাংলা ও ইংরেজির Recall@10 ব্যবধান (পয়েন্ট)", "প্রযোজ্য নয়", "v1 থেকে পরিমাপ (মাস ৩০)", "৫ বা কম", "৩ বা কম", "২ বা কম"],
                ["জনসমক্ষে স্বচ্ছতা নিবন্ধনে তালিকাভুক্ত এআই ব্যবস্থা", "০", "৬", "১৫", "সরকারি খাতজুড়ে নিবন্ধন প্রস্তাবিত", "প্রমিত চর্চা"],
                ["প্রকাশিত স্বাধীন মূল্যায়ন", "০", "১", "৩", "৮", "অন্তত প্রতি ৫ বছরে"],
                ["DOI-সহ সংরক্ষিত উন্মুক্ত প্রকাশ", "৩", "৮", "১৫", "৪০", "নিরবচ্ছিন্ন"],
            ],
        },
        "note": {"en": "Planning targets, not commitments. They assume the baseline scenario of Table 47, Phase 0 in the first half of 2027 and Month 1 in July 2027, and are reset at every strategic review.",
                 "bn": "পরিকল্পনা-লক্ষ্য, প্রতিশ্রুতি নয়। এগুলো সারণি ৪৭-এর ভিত্তি-দৃশ্যকল্প, ২০২৭-এর প্রথমার্ধে ধাপ ০ এবং জুলাই ২০২৭-এ মাস ১ ধরে নেয় এবং প্রতিটি কৌশলগত পর্যালোচনায় পুনর্নির্ধারিত হয়।"},
    },
    # ------------------------------------------------------------------ 47
    {
        "id": "47",
        "widths": [1.6, 2.6, 2.3, 2.9],
        "title": {"en": "Strategic scenarios and responses", "bn": "কৌশলগত দৃশ্যকল্প ও করণীয়"},
        "cols": {"en": ["Scenario", "Description", "Early signals", "Strategic response"],
                 "bn": ["দৃশ্যকল্প", "বিবরণ", "প্রাথমিক সংকেত", "কৌশলগত করণীয়"]},
        "rows": {
            "en": [
                ["**Accelerated**", "Strong political sponsorship, national compute and data exchange arrive early", "AI policy adopted with funding; NRDEX operational; agencies request tools", "Bring forward H2 adoption; expand to more ministries; keep gates unchanged so that speed does not erode safeguards"],
                ["**Baseline**", "Steady progress with normal delays in data access and funding", "Milestones met within about two quarters", "Follow the roadmap; use reviews to adjust scope"],
                ["**Constrained**", "Funding cuts, slow data agreements or loss of sponsorship", "Missed MS2 or MS4; budget delays; staff turnover", "Protect the core (P1, benchmark, governance); pause P3, P5 and P6; seek research grants; publish what exists"],
                ["**Technology shift**", "Much stronger or cheaper models change what is possible", "Open models exceed thresholds without adaptation; costs fall sharply", "Re-run model selection (Table 29); skip BPFM stages that are no longer needed; invest in evaluation and data"],
                ["**Governance shock**", "A serious AI incident in Bangladesh or abroad reduces public trust", "Media coverage; new restrictions; complaints", "Pause affected systems; independent review; publish findings; strengthen controls; communicate openly"],
            ],
            "bn": [
                ["**ত্বরান্বিত**", "শক্তিশালী রাজনৈতিক পৃষ্ঠপোষকতা, জাতীয় কম্পিউটিং ও ডেটা-বিনিময় আগেভাগে উপলব্ধ", "অর্থায়নসহ এআই নীতি গৃহীত; NRDEX চালু; সংস্থাগুলোর সরঞ্জাম চাহিদা", "H2-এর গ্রহণ এগিয়ে আনা; আরও মন্ত্রণালয়ে সম্প্রসারণ; গতির কারণে সুরক্ষা যেন না কমে তাই গেট অপরিবর্তিত"],
                ["**ভিত্তি**", "ডেটা প্রবেশাধিকার ও অর্থায়নে স্বাভাবিক বিলম্বসহ স্থির অগ্রগতি", "প্রায় দুই ত্রৈমাসিকের মধ্যে মাইলফলক অর্জিত", "রোডম্যাপ অনুসরণ; পর্যালোচনার মাধ্যমে পরিধি সমন্বয়"],
                ["**সীমিত**", "অর্থায়ন হ্রাস, ধীর ডেটা-চুক্তি বা পৃষ্ঠপোষকতা হারানো", "MS2 বা MS4 অনর্জিত; বাজেট বিলম্ব; কর্মী বদল", "মূল অংশ রক্ষা (P1, বেঞ্চমার্ক, শাসন); P3, P5 ও P6 স্থগিত; গবেষণা অনুদান সন্ধান; যা আছে তা প্রকাশ"],
                ["**প্রযুক্তিগত পরিবর্তন**", "অনেক শক্তিশালী বা সস্তা মডেল সম্ভাবনার পরিধি বদলে দেয়", "অভিযোজন ছাড়াই উন্মুক্ত মডেল সীমা অতিক্রম করে; ব্যয় দ্রুত কমে", "মডেল নির্বাচন পুনরায় (সারণি ২৯); অপ্রয়োজনীয় BPFM পর্যায় বাদ; মূল্যায়ন ও ডেটায় বিনিয়োগ"],
                ["**শাসনগত ধাক্কা**", "বাংলাদেশে বা বিদেশে গুরুতর এআই ঘটনায় জন-আস্থা হ্রাস", "সংবাদমাধ্যমে প্রচার; নতুন বিধিনিষেধ; অভিযোগ", "প্রভাবিত ব্যবস্থা স্থগিত; স্বাধীন পর্যালোচনা; ফলাফল প্রকাশ; নিয়ন্ত্রণ জোরদার; উন্মুক্ত যোগাযোগ"],
            ],
        },
    },
    # ------------------------------------------------------------------ 48
    {
        "id": "48",
        "widths": [1.1, 2.0, 3.0, 2.8],
        "title": {"en": "Strategic review points and triggers", "bn": "কৌশলগত পর্যালোচনা-বিন্দু ও উদ্দীপক"},
        "cols": {"en": ["When", "Review", "Key questions", "Possible decisions"],
                 "bn": ["কখন", "পর্যালোচনা", "মূল প্রশ্ন", "সম্ভাব্য সিদ্ধান্ত"]},
        "rows": {
            "en": [
                ["Mid 2028", "Year 1 review (MS4)", "Did P1 and P2 deliver value with public data? Is governance working?", "Continue, adjust scope or stop pilots; confirm Phase 2 budget"],
                ["End 2028", "Independent mid-term evaluation (MS6)", "Value for money; adoption; quality of assurance", "BPFM Stage 1 decision; staffing for Phase 2"],
                ["Mid 2030", "Final evaluation of the 36-month plan (MS9)", "Which tools should agencies own? Is the institutional form right?", "G4 transfers; Blueprint 2.0; choice between Options C and D"],
                ["2030", "Alignment with the next national AI policy cycle", "How should BAPIL support the post-2030 policy?", "Revised mission and targets for H3"],
                ["2035", "Long-term strategic review", "Is a national network justified? Are methods used beyond BAPIL?", "Network expansion, consolidation or narrowing of scope"],
                ["2041", "Vision review", "Has BAPIL delivered public value aligned with national long-term goals?", "Renew charter, merge into government or close with archives preserved"],
                ["Any time", "Event triggers", "New law or rules; serious incident; major technology shift; loss of funding", "Extraordinary Steering Board review within 30 days"],
            ],
            "bn": [
                ["২০২৮-এর মাঝামাঝি", "প্রথম বছরের পর্যালোচনা (MS4)", "উন্মুক্ত ডেটা দিয়ে P1 ও P2 কি মূল্য সৃষ্টি করেছে? শাসন কি কাজ করছে?", "পাইলট অব্যাহত, পরিধি সমন্বয় বা বন্ধ; দ্বিতীয় ধাপের বাজেট নিশ্চিত"],
                ["২০২৮-এর শেষে", "স্বাধীন মধ্যমেয়াদি মূল্যায়ন (MS6)", "অর্থের যথার্থ ব্যবহার; গ্রহণ; আশ্বাসের মান", "BPFM পর্যায় ১-এর সিদ্ধান্ত; দ্বিতীয় ধাপের জনবল"],
                ["২০৩০-এর মাঝামাঝি", "৩৬ মাসের পরিকল্পনার চূড়ান্ত মূল্যায়ন (MS9)", "কোন সরঞ্জাম সংস্থাগুলোর মালিকানায় যাবে? প্রাতিষ্ঠানিক রূপ কি যথাযথ?", "G4 হস্তান্তর; ব্লুপ্রিন্ট ২.০; বিকল্প গ ও ঘ-এর মধ্যে নির্বাচন"],
                ["২০৩০", "পরবর্তী জাতীয় এআই নীতিচক্রের সঙ্গে সামঞ্জস্য", "২০৩০-পরবর্তী নীতিতে BAPIL কীভাবে সহায়তা করবে?", "H3-এর জন্য সংশোধিত মিশন ও লক্ষ্য"],
                ["২০৩৫", "দীর্ঘমেয়াদি কৌশলগত পর্যালোচনা", "জাতীয় নেটওয়ার্ক কি যৌক্তিক? পদ্ধতিগুলো কি BAPIL-এর বাইরে ব্যবহৃত হচ্ছে?", "নেটওয়ার্ক সম্প্রসারণ, একীকরণ বা পরিধি সংকোচন"],
                ["২০৪১", "রূপকল্প পর্যালোচনা", "BAPIL কি জাতীয় দীর্ঘমেয়াদি লক্ষ্যের সঙ্গে সংগতিপূর্ণ জনমূল্য সৃষ্টি করেছে?", "সনদ নবায়ন, সরকারে একীভবন বা সংরক্ষণাগার রক্ষা করে সমাপ্তি"],
                ["যেকোনো সময়", "ঘটনাভিত্তিক উদ্দীপক", "নতুন আইন বা বিধি; গুরুতর ঘটনা; বড় প্রযুক্তিগত পরিবর্তন; অর্থায়ন হারানো", "৩০ দিনের মধ্যে স্টিয়ারিং বোর্ডের বিশেষ পর্যালোচনা"],
            ],
        },
        "note": {"en": "Calendar dates assume that Phase 0 runs in the first half of 2027 and Month 1 is July 2027; if the plan starts later, the first three reviews move with it (Annex T).",
                 "bn": "ক্যালেন্ডারের তারিখগুলো ২০২৭-এর প্রথমার্ধে ধাপ ০ এবং মাস ১ জুলাই ২০২৭ ধরে নির্ধারিত; পরিকল্পনা দেরিতে শুরু হলে প্রথম তিনটি পর্যালোচনাও সেই অনুযায়ী পিছিয়ে যাবে (সংযুক্তি ন)।"},
    },
    # ------------------------------------------------------------------ 49
    {
        "id": "49",
        "widths": [1.9, 3.6, 2.9],
        "title": {"en": "Planning assumptions for the indicative budget", "bn": "নির্দেশক বাজেটের পরিকল্পনা-অনুমান"},
        "cols": {"en": ["Item", "Assumption", "Basis"], "bn": ["বিষয়", "অনুমান", "ভিত্তি"]},
        "rows": {
            "en": [
                ["Exchange rate", "Tk 124 per US dollar", "Bangladesh Bank weighted average rate of Tk 123.65 on 19 October 2026 [110]"],
                ["Core staff", "9, 15 and 19 full-time equivalents in Years 1, 2 and 3", "Staffing plan (Table 16)"],
                ["Year 1 recruitment", "75% of Year 1 positions filled on average", "Director appointed in months 1 to 3; other posts filled in months 2 to 6 (Section 15.4)"],
                ["Staff cost", "Fully loaded monthly cost per FTE at Year 1 prices: Director Tk 3.0 lakh; ML and Bangla NLP engineers Tk 2.0 lakh; security engineer Tk 1.8 lakh; policy, data and platform staff Tk 1.5 lakh; governance and UX staff Tk 1.25 lakh; coordinator Tk 0.9 lakh; training officers Tk 0.8 lakh", "Above the basic pay of the Ninth National Pay Scale 2026 (Tk 20,000 to Tk 156,000 a month; Tk 44,000 at grade 9, the entry grade for BCS officers), approved by the Cabinet in August 2026 [109], to compete for scarce AI skills. Reported market pay for AI and ML engineers in Dhaka: Tk 0.7 to 1.1 lakh a month at mid level and Tk 1.2 to 2.0 lakh at senior level, before provident fund and bonuses [160]"],
                ["Escalation", "8% a year on taka costs in Years 2 and 3", "Point-to-point inflation of 8.34% in September 2026, as reported [118]; the host’s increment rules may differ"],
                ["Language editors and fellows", "Part-time editors Tk 12 to 14 lakh a year; 6, 10 and 12 fellows at Tk 40,000 a month (Year 1 prices)", "Fellowship programme (Section 6.6); the stipend equals the PhD fellowship of a public university [161]"],
                ["Equipment", "General-purpose servers USD 12,000 each; GPU inference servers (L40S class) USD 25,000 each; storage USD 6,000 to 12,000 a year", "L40S card about USD 7,100 (lowest marketplace average, September 2026) to USD 8,050 (retail listing) [156, 157]: two cards and a GPU-capable host of about USD 10,000 make one inference server. Dell list price of a base two-socket server about USD 16,000 in August 2026 [158]; memory prices rose sharply in 2025 and 2026 [159]. At list prices equipment costs about 26% more, about Tk 0.7 crore (Section 17.1)"],
                ["Import duty and VAT on equipment", "Not included in the base case; 25% added in the high scenario", "Depends on the host’s exemption status; input required from the host’s procurement office"],
                ["Hosting and operations", "Tk 25 lakh rising to Tk 38 lakh a year (Year 1 prices)", "Colocation of one standard 2 to 7 kW rack in a domestic facility about Tk 1.0 to 1.6 lakh a month, as reported in July 2026 [155]; the balance covers bandwidth, licences and a development cloud, and a second (disaster-recovery) site from Year 2"],
                ["Model adaptation compute", "In kind from shared national compute; USD 20,000 of cloud GPU time on public (DC0) data in the high scenario", "Table 31; draft national AI policy [88]; cloud prices in [111]"],
                ["Benchmark and evaluation data", "2,000 answerable questions by month 30 at Tk 2,500; 300 out-of-scope questions at Tk 600; 2,000 citation-support judgements at Tk 500", "BanglaPolicyQA plan (Section 9.4); evaluation protocol (Annex R)"],
                ["Training", "500 officials by month 36 at Tk 15,000 per participant, plus specialist courses", "Training curriculum (Table 18)"],
                ["Evaluation and assurance", "Legal review Tk 8 lakh; baseline study Tk 6 lakh; mid-term evaluation Tk 20 lakh; final evaluation Tk 25 lakh; annual penetration test and red team Tk 6 lakh; annual independent audit of systems Tk 3 lakh", "Chapters 13, 14 and 18"],
                ["Host overheads", "10% of direct costs", "To be confirmed against the host institution’s policy"],
                ["Contingency", "5% of direct costs in the base case, released only by Steering Board decision; 10% recommended until quotations and the host’s rates are known (adjusted base case and high scenario)", "Allowance for estimating uncertainty; scenarios in Annex Q"],
            ],
            "bn": [
                ["বিনিময় হার", "প্রতি মার্কিন ডলারে ১২৪ টাকা", "১৯ অক্টোবর ২০২৬-এ বাংলাদেশ ব্যাংকের ভারিত গড় হার ১২৩.৬৫ টাকা [110]"],
                ["মূল জনবল", "প্রথম, দ্বিতীয় ও তৃতীয় বছরে ৯, ১৫ ও ১৯ পূর্ণকালীন সমতুল্য", "জনবল পরিকল্পনা (সারণি ১৬)"],
                ["প্রথম বছরের নিয়োগ", "প্রথম বছরে গড়ে ৭৫% পদ পূরণ", "মাস ১ থেকে ৩-এ পরিচালক নিয়োগ; মাস ২ থেকে ৬-এ অন্যান্য পদ পূরণ (অনুচ্ছেদ ১৫.৪)"],
                ["জনবলের ব্যয়", "প্রথম বছরের মূল্যে প্রতি পূর্ণকালীন সমতুল্যের পূর্ণ মাসিক ব্যয়: পরিচালক ৩.০ লাখ টাকা; ML ও বাংলা NLP প্রকৌশলী ২.০ লাখ; নিরাপত্তা প্রকৌশলী ১.৮ লাখ; নীতি, ডেটা ও প্ল্যাটফর্ম কর্মী ১.৫ লাখ; শাসন ও UX কর্মী ১.২৫ লাখ; সমন্বয়ক ০.৯ লাখ; প্রশিক্ষণ কর্মকর্তা ০.৮ লাখ", "দুর্লভ এআই দক্ষতার প্রতিযোগিতায় নবম জাতীয় বেতন স্কেল ২০২৬-এর (আগস্ট ২০২৬-এ মন্ত্রিসভায় অনুমোদিত) মূল বেতনের (মাসিক ২০,০০০ থেকে ১,৫৬,০০০ টাকা; বিসিএস কর্মকর্তাদের প্রবেশ-গ্রেড ৯-এ ৪৪,০০০ টাকা) ওপরে [109]। ঢাকায় এআই ও ML প্রকৌশলীদের প্রতিবেদিত বাজার-বেতন: মধ্য স্তরে মাসিক ০.৭ থেকে ১.১ লাখ এবং জ্যেষ্ঠ স্তরে ১.২ থেকে ২.০ লাখ টাকা, ভবিষ্য তহবিল ও উৎসব-ভাতা ছাড়া [160]"],
                ["মূল্যবৃদ্ধি", "দ্বিতীয় ও তৃতীয় বছরে টাকায় পরিশোধ্য ব্যয়ে বছরে ৮%", "সেপ্টেম্বর ২০২৬-এ পয়েন্ট-টু-পয়েন্ট মূল্যস্ফীতি ৮.৩৪% বলে প্রতিবেদিত [118]; স্বাগতিকের বেতনবৃদ্ধির নিয়ম ভিন্ন হতে পারে"],
                ["ভাষা-সম্পাদক ও ফেলো", "খণ্ডকালীন সম্পাদক বছরে ১২ থেকে ১৪ লাখ টাকা; মাসিক ৪০,০০০ টাকায় ৬, ১০ ও ১২ জন ফেলো (প্রথম বছরের মূল্যে)", "ফেলোশিপ কর্মসূচি (অনুচ্ছেদ ৬.৬); ভাতাটি একটি সরকারি বিশ্ববিদ্যালয়ের পিএইচডি ফেলোশিপের সমান [161]"],
                ["যন্ত্রপাতি", "সাধারণ-উদ্দেশ্য সার্ভার প্রতিটি ১২,০০০ মার্কিন ডলার; GPU ইনফারেন্স সার্ভার (L40S শ্রেণি) প্রতিটি ২৫,০০০ মার্কিন ডলার; সংরক্ষণক্ষমতা বছরে ৬,০০০ থেকে ১২,০০০ মার্কিন ডলার", "একটি L40S কার্ড প্রায় ৭,১০০ মার্কিন ডলার (সেপ্টেম্বর ২০২৬-এ বাজারের সর্বনিম্ন গড়) থেকে ৮,০৫০ মার্কিন ডলার (খুচরা তালিকা) [156, 157]: দুটি কার্ড ও প্রায় ১০,০০০ মার্কিন ডলারের একটি GPU-সক্ষম হোস্ট মিলে একটি ইনফারেন্স সার্ভার। আগস্ট ২০২৬-এ একটি মৌলিক দুই-সকেট সার্ভারের ডেল তালিকা-মূল্য প্রায় ১৬,০০০ মার্কিন ডলার [158]; ২০২৫ ও ২০২৬ সালে মেমরির দাম তীব্রভাবে বেড়েছে [159]। তালিকা-মূল্যে যন্ত্রপাতির ব্যয় প্রায় ২৬% বেশি, প্রায় ০.৭ কোটি টাকা (অনুচ্ছেদ ১৭.১)"],
                ["যন্ত্রপাতির আমদানি শুল্ক ও ভ্যাট", "মূল হিসাবে অন্তর্ভুক্ত নয়; উচ্চ পরিস্থিতিতে ২৫% যোগ", "স্বাগতিকের অব্যাহতির অবস্থার ওপর নির্ভরশীল; স্বাগতিকের ক্রয় দপ্তর থেকে তথ্য প্রয়োজন"],
                ["হোস্টিং ও পরিচালনা", "বছরে ২৫ লাখ থেকে ৩৮ লাখ টাকা (প্রথম বছরের মূল্যে)", "দেশীয় একটি ডেটা সেন্টারে ২ থেকে ৭ কিলোওয়াটের একটি সাধারণ র‍্যাকের কোলোকেশন মাসে প্রায় ১.০ থেকে ১.৬ লাখ টাকা, জুলাই ২০২৬-এর প্রতিবেদন অনুযায়ী [155]; বাকিটা ব্যান্ডউইথ, লাইসেন্স ও উন্নয়ন-ক্লাউডের জন্য, এবং দ্বিতীয় বছর থেকে একটি পুনরুদ্ধার-সাইট"],
                ["মডেল অভিযোজনের কম্পিউটিং", "যৌথ জাতীয় কম্পিউটিং থেকে বস্তুগত সহায়তা; উচ্চ পরিস্থিতিতে উন্মুক্ত (DC0) ডেটায় ২০,০০০ মার্কিন ডলারের ক্লাউড GPU সময়", "সারণি ৩১; খসড়া জাতীয় এআই নীতি [88]; ক্লাউডের মূল্য [111]"],
                ["বেঞ্চমার্ক ও মূল্যায়ন-ডেটা", "মাস ৩০-এর মধ্যে ২,৫০০ টাকা দরে ২,০০০ উত্তরযোগ্য প্রশ্ন; ৬০০ টাকা দরে ৩০০ আওতাবহির্ভূত প্রশ্ন; ৫০০ টাকা দরে ২,০০০ উদ্ধৃতি-সমর্থন বিচার", "BanglaPolicyQA পরিকল্পনা (অনুচ্ছেদ ৯.৪); মূল্যায়ন প্রটোকল (সংযুক্তি দ)"],
                ["প্রশিক্ষণ", "মাস ৩৬-এর মধ্যে ৫০০ কর্মকর্তা, অংশগ্রহণকারীপ্রতি ১৫,০০০ টাকা, সঙ্গে বিশেষায়িত কোর্স", "প্রশিক্ষণ পাঠ্যক্রম (সারণি ১৮)"],
                ["মূল্যায়ন ও আশ্বাস", "আইনি পর্যালোচনা ৮ লাখ টাকা; ভিত্তি সমীক্ষা ৬ লাখ; মধ্যমেয়াদি মূল্যায়ন ২০ লাখ; চূড়ান্ত মূল্যায়ন ২৫ লাখ; বার্ষিক অনুপ্রবেশ পরীক্ষা ও রেড-টিম ৬ লাখ; ব্যবস্থাগুলোর বার্ষিক স্বাধীন নিরীক্ষা ৩ লাখ", "অধ্যায় ১৩, ১৪ ও ১৮"],
                ["স্বাগতিকের পরোক্ষ ব্যয়", "প্রত্যক্ষ ব্যয়ের ১০%", "স্বাগতিক প্রতিষ্ঠানের নীতির সঙ্গে মিলিয়ে নিশ্চিত করতে হবে"],
                ["আপৎকালীন সংস্থান", "মূল হিসাবে প্রত্যক্ষ ব্যয়ের ৫%, শুধু স্টিয়ারিং বোর্ডের সিদ্ধান্তে ব্যবহারযোগ্য; দরপত্র ও স্বাগতিকের হার জানা না যাওয়া পর্যন্ত ১০% সুপারিশকৃত (সমন্বিত মূল হিসাব ও উচ্চ পরিস্থিতি)", "প্রাক্কলনের অনিশ্চয়তার জন্য সংস্থান; পরিস্থিতি বিশ্লেষণ সংযুক্তি থ-তে"],
            ],
        },
        "note": {"en": "Planning assumptions for the Phase 0 costing study (Section 15.1), not quotations. The model is published as blueprint/src/budget_model.py so that any assumption can be changed and the budget regenerated.",
                 "bn": "ধাপ ০-এর ব্যয়-নিরূপণ সমীক্ষার (অনুচ্ছেদ ১৫.১) পরিকল্পনা-অনুমান, দরপত্র নয়। মডেলটি blueprint/src/budget_model.py হিসেবে প্রকাশিত, যাতে যেকোনো অনুমান বদলে বাজেট পুনরায় হিসাব করা যায়।"},
    },
    # ------------------------------------------------------------------ 50
    {
        "id": "50",
        "widths": [3.0, 1.0, 1.0, 1.0, 1.0, 0.9],
        "title": {"en": "Indicative 36-month budget (Tk crore)", "bn": "নির্দেশক ৩৬ মাসের বাজেট (কোটি টাকা)"},
        "cols": {"en": ["Category", "Year 1", "Year 2", "Year 3", "Total", "Share"],
                 "bn": ["খাত", "বছর ১", "বছর ২", "বছর ৩", "মোট", "অংশ"]},
        "rows": {
            "en": _B_EN,
            "bn": _B_BN,
        },
        "note": {"en": "Computed from the assumptions in Table 49 by blueprint/src/budget_model.py. Figures are rounded independently, so rows and columns may not add exactly: the unrounded total is Tk %s (Tk %.2f crore), while the rounded annual totals add to Tk %.2f crore. Rounded rows add to %.2f, %.2f, %.2f and %.2f; the totals shown are computed from unrounded values. Equivalent to about USD %.2f million. A planning estimate: no funds have been approved or committed." % ((_B_UNROUNDED, _bm.crore(_B_TOTAL), _B_ROUNDED) + _B_COLSUMS + (_B_USD,)),
                 "bn": ("blueprint/src/budget_model.py দ্বারা সারণি ৪৯-এর অনুমান থেকে হিসাবকৃত। প্রতিটি অঙ্ক আলাদাভাবে আসন্নীকৃত, তাই সারি ও কলামের যোগফল হুবহু না-ও মিলতে পারে: আসন্নীকরণের আগের মোট %s টাকা (%.2f কোটি টাকা), আর আসন্নীকৃত বার্ষিক মোটের যোগফল %.2f কোটি টাকা। আসন্নীকৃত সারিগুলোর যোগফল %.2f, %.2f, %.2f ও %.2f; দেখানো মোট অঙ্কগুলো আসন্নীকরণের আগের মান থেকে হিসাবকৃত। প্রায় %.2f মিলিয়ন মার্কিন ডলারের সমতুল্য। এটি পরিকল্পনা-প্রাক্কলন: কোনো অর্থ অনুমোদিত বা প্রতিশ্রুত হয়নি।" % ((_B_UNROUNDED_BN, _bm.crore(_B_TOTAL), _B_ROUNDED) + _B_COLSUMS + (_B_USD,))).translate(_BN)},
    },
    # ------------------------------------------------------------------ 51
    {
        "id": "51",
        "widths": [2.5, 1.2, 1.3, 1.3, 1.3, 1.3],
        "title": {"en": "Indicative funding mix by horizon", "bn": "দিগন্তভিত্তিক নির্দেশক অর্থায়ন-মিশ্রণ"},
        "cols": {"en": ["Source", "Year 1 (Phase 1)", "H1 from Year 2", "H2 2029 to 2030", "H3 2031 to 2035", "H4 2036 to 2041"],
                 "bn": ["উৎস", "বছর ১ (ধাপ ১)", "H1, বছর ২ থেকে", "H2 ২০২৯ থেকে ২০৩০", "H3 ২০৩১ থেকে ২০৩৫", "H4 ২০৩৬ থেকে ২০৪১"]},
        "rows": {
            "en": [
                ["Government core contribution (MoU, development budget)", "70 to 75%", "30 to 40%", "40 to 50%", "45 to 55%", "50 to 60%"],
                ["Competitive research grants", "0%", "20 to 30%", "15 to 25%", "10 to 20%", "10 to 15%"],
                ["Development partners (pilot-specific)", "25 to 30%", "20 to 30%", "15 to 20%", "5 to 10%", "0 to 5%"],
                ["Service agreements with agencies (cost recovery)", "0%", "0%", "5 to 10%", "15 to 25%", "20 to 30%"],
                ["Industry and philanthropy (open benchmarks, fellowships)", "0%", "5 to 10%", "5 to 10%", "5 to 10%", "5 to 10%"],
            ],
            "bn": [
                ["সরকারের মূল অবদান (সমঝোতা স্মারক, উন্নয়ন বাজেট)", "৭০ থেকে ৭৫%", "৩০ থেকে ৪০%", "৪০ থেকে ৫০%", "৪৫ থেকে ৫৫%", "৫০ থেকে ৬০%"],
                ["প্রতিযোগিতামূলক গবেষণা অনুদান", "০%", "২০ থেকে ৩০%", "১৫ থেকে ২৫%", "১০ থেকে ২০%", "১০ থেকে ১৫%"],
                ["উন্নয়ন সহযোগী (পাইলটভিত্তিক)", "২৫ থেকে ৩০%", "২০ থেকে ৩০%", "১৫ থেকে ২০%", "৫ থেকে ১০%", "০ থেকে ৫%"],
                ["সংস্থার সঙ্গে সেবা-চুক্তি (ব্যয় পুনরুদ্ধার)", "০%", "০%", "৫ থেকে ১০%", "১৫ থেকে ২৫%", "২০ থেকে ৩০%"],
                ["শিল্প ও জনহিতৈষী সহায়তা (উন্মুক্ত বেঞ্চমার্ক, ফেলোশিপ)", "০%", "৫ থেকে ১০%", "৫ থেকে ১০%", "৫ থেকে ১০%", "৫ থেকে ১০%"],
            ],
        },
        "note": {"en": "Year 1 relies on sources that can be committed before Month 1: the government budget and one development partner. Research grants and industry funds follow once the lab exists. No single non-government funder should provide more than 30% of the budget in any year, and industry support never buys influence over research results or governance decisions.",
                 "bn": "প্রথম বছর এমন উৎসের ওপর নির্ভর করে, যা মাস ১-এর আগে প্রতিশ্রুত হতে পারে: সরকারি বাজেট ও একটি উন্নয়ন সহযোগী। ল্যাব গঠিত হওয়ার পর গবেষণা অনুদান ও শিল্পখাতের অর্থ আসে। কোনো বছরে সরকার-বহির্ভূত কোনো একক অর্থদাতা বাজেটের ৩০%-এর বেশি দেবেন না, এবং শিল্পখাতের সহায়তা কখনো গবেষণার ফলাফল বা শাসনগত সিদ্ধান্তে প্রভাব কিনতে পারবে না।"},
    },
    # ------------------------------------------------------------------ 52
    {
        "id": "52",
        "widths": [2.0, 3.6, 2.6],
        "title": {"en": "Model clauses for procuring AI products and services", "bn": "এআই পণ্য ও সেবা ক্রয়ের আদর্শ শর্ত"},
        "cols": {"en": ["Clause", "Requirement", "Purpose"], "bn": ["শর্ত", "প্রয়োজনীয়তা", "উদ্দেশ্য"]},
        "rows": {
            "en": [
                ["Data residency and ownership", "Government data stays in Bangladesh and remains government property; no use for vendor model training", "Protect data and sovereignty (NFR-02)"],
                ["Right to evaluate", "Buyer may test the product on BanglaPolicyQA and red-team tests before and after award", "Decisions based on evidence, not claims"],
                ["Bangla performance acceptance", "Acceptance requires meeting agreed Bangla and English thresholds", "Bangla as a first-class language"],
                ["Documentation", "Model cards, datasheets, SBOM and known limitations delivered with each version", "Transparency and audit"],
                ["Portability and exit", "Open formats; export of all data and configurations; transition support at contract end", "Avoid lock-in (R10)"],
                ["Source code", "Open source where possible; otherwise escrow and the right to audit", "Long-term maintainability"],
                ["Security and incidents", "Compliance with Table 32 controls; vulnerability disclosure; incident notification within 24 hours", "Security and accountability"],
                ["Change control", "Notice and re-evaluation before any model or major dependency change", "Stable, assessed behaviour (G5)"],
                ["Accessibility", "WCAG 2.2 level AA conformance with evidence", "Inclusion (NFR-05)"],
                ["Integrity", "Declaration of conflicts of interest; no influence over evaluation or governance", "Independence"],
            ],
            "bn": [
                ["ডেটা-অবস্থান ও মালিকানা", "সরকারি ডেটা বাংলাদেশে থাকবে ও সরকারের সম্পত্তি থাকবে; বিক্রেতার মডেল প্রশিক্ষণে ব্যবহার নয়", "ডেটা ও সার্বভৌমত্ব সুরক্ষা (NFR-02)"],
                ["মূল্যায়নের অধিকার", "চুক্তির আগে ও পরে ক্রেতা BanglaPolicyQA ও রেড-টিম পরীক্ষায় পণ্য যাচাই করতে পারবেন", "দাবির নয়, প্রমাণের ভিত্তিতে সিদ্ধান্ত"],
                ["বাংলা কর্মদক্ষতার গ্রহণযোগ্যতা", "গ্রহণের শর্ত সম্মত বাংলা ও ইংরেজি সীমা অর্জন", "বাংলা প্রথম শ্রেণির ভাষা"],
                ["নথিভুক্তি", "প্রতিটি সংস্করণের সঙ্গে মডেল কার্ড, ডেটাশিট, SBOM ও জ্ঞাত সীমাবদ্ধতা প্রদান", "স্বচ্ছতা ও নিরীক্ষা"],
                ["স্থানান্তরযোগ্যতা ও প্রস্থান", "উন্মুক্ত ফরম্যাট; সব ডেটা ও কনফিগারেশন রপ্তানি; চুক্তি শেষে রূপান্তর-সহায়তা", "নির্ভরশীলতা এড়ানো (R10)"],
                ["সোর্স কোড", "সম্ভব হলে উন্মুক্ত সোর্স; অন্যথায় এসক্রো ও নিরীক্ষার অধিকার", "দীর্ঘমেয়াদি রক্ষণাবেক্ষণযোগ্যতা"],
                ["নিরাপত্তা ও ঘটনা", "সারণি ৩২-এর নিয়ন্ত্রণ মেনে চলা; দুর্বলতা প্রকাশ; ২৪ ঘণ্টার মধ্যে ঘটনার বিজ্ঞপ্তি", "নিরাপত্তা ও জবাবদিহি"],
                ["পরিবর্তন নিয়ন্ত্রণ", "মডেল বা বড় নির্ভরতা পরিবর্তনের আগে নোটিশ ও পুনর্মূল্যায়ন", "স্থিতিশীল ও মূল্যায়িত আচরণ (G5)"],
                ["প্রবেশযোগ্যতা", "প্রমাণসহ WCAG 2.2 লেভেল AA সামঞ্জস্য", "অন্তর্ভুক্তি (NFR-05)"],
                ["সততা", "স্বার্থের সংঘাত ঘোষণা; মূল্যায়ন বা শাসনে কোনো প্রভাব নয়", "স্বাধীনতা"],
            ],
        },
    },
    # ------------------------------------------------------------------ 53
    {
        "id": "53",
        "widths": [1.25, 2.6, 2.6, 1.9, 2.2],
        "title": {"en": "Logical framework (36-month programme)", "bn": "লজিক্যাল ফ্রেমওয়ার্ক (৩৬ মাসের কর্মসূচি)"},
        "cols": {"en": ["Level", "Narrative summary", "Indicators", "Means of verification", "Assumptions"],
                 "bn": ["স্তর", "সংক্ষিপ্ত বিবরণ", "সূচক", "যাচাইয়ের উপায়", "অনুমান"]},
        "rows": {
            "en": [
                ["**Impact**", "Public policy in Bangladesh is better grounded in evidence, and AI in the public sector is trusted and well governed", "Official documents citing BAPIL evidence; trust measures in user surveys", "Document analysis; independent evaluation", "Political commitment to evidence-based policy continues"],
                ["**Outcome 1**", "Officials and researchers find and cite authoritative evidence faster and more reliably", "Time saved on evidence search; monthly active users", "Time-to-evidence studies; usage logs", "Agencies release staff time for pilots"],
                ["**Outcome 2**", "AI systems in BAPIL’s scope are governed transparently and safely", "100% registered; serious incidents handled in time", "Transparency register; incident records", "ERRC remains independent and resourced"],
                ["**Outcome 3**", "National capacity in Bangla policy AI grows", "Officials trained; fellows; open datasets reused", "Training records; download and citation counts", "Trained staff stay in relevant posts"],
                ["**Output 1**", "Policy search and budget dataset piloted with users", "Pilots passing G3; Recall@10", "Gate records; benchmark reports", "Data access granted on time"],
                ["**Output 2**", "Open benchmark, corpus and evaluation methods published", "Benchmark questions; releases with DOIs", "Zenodo and GitHub records", "Annotators available"],
                ["**Output 3**", "Governance system operational", "Charter adopted; ERRC decisions published", "Board minutes; register", "Members nominated on time"],
                ["**Output 4**", "Officials and specialists trained", "Officials trained by programme", "Attendance and assessment records", "Agencies nominate participants"],
                ["**Activities**", "Workplan of Chapter 15 and the work packages of the pilots", "Milestones MS1 to MS9", "Progress reports", "Funding released as planned"],
            ],
            "bn": [
                ["**প্রভাব**", "বাংলাদেশের জননীতি প্রমাণে আরও দৃঢ়ভাবে ভিত্তিস্থাপিত, এবং সরকারি খাতে এআই আস্থাভাজন ও সুশাসিত", "BAPIL-এর প্রমাণ উদ্ধৃতকারী সরকারি নথি; ব্যবহারকারী জরিপে আস্থার মাপ", "নথি বিশ্লেষণ; স্বাধীন মূল্যায়ন", "প্রমাণভিত্তিক নীতির প্রতি রাজনৈতিক অঙ্গীকার অব্যাহত"],
                ["**ফলাফল ১**", "কর্মকর্তা ও গবেষকেরা দ্রুত ও নির্ভরযোগ্যভাবে প্রামাণ্য প্রমাণ খুঁজে পান ও উদ্ধৃত করেন", "প্রমাণ অনুসন্ধানে সাশ্রয়কৃত সময়; মাসিক সক্রিয় ব্যবহারকারী", "প্রমাণ-প্রাপ্তির সময় সমীক্ষা; ব্যবহার-লগ", "সংস্থাগুলো পাইলটের জন্য কর্মীদের সময় দেয়"],
                ["**ফলাফল ২**", "BAPIL-এর পরিধিভুক্ত এআই ব্যবস্থা স্বচ্ছ ও নিরাপদভাবে নিয়ন্ত্রিত", "১০০% নিবন্ধিত; গুরুতর ঘটনা সময়মতো নিষ্পন্ন", "স্বচ্ছতা নিবন্ধন; ঘটনার রেকর্ড", "ERRC স্বাধীন ও সম্পদসমৃদ্ধ থাকে"],
                ["**ফলাফল ৩**", "বাংলা নীতি-এআই-তে জাতীয় সক্ষমতা বৃদ্ধি", "প্রশিক্ষিত কর্মকর্তা; ফেলো; পুনর্ব্যবহৃত উন্মুক্ত ডেটাসেট", "প্রশিক্ষণ রেকর্ড; ডাউনলোড ও উদ্ধৃতির সংখ্যা", "প্রশিক্ষিত কর্মীরা প্রাসঙ্গিক পদে থাকেন"],
                ["**উৎপাদ ১**", "ব্যবহারকারীদের সঙ্গে নীতি অনুসন্ধান ও বাজেট ডেটাসেটের পাইলট", "G3 উত্তীর্ণ পাইলট; Recall@10", "গেট রেকর্ড; বেঞ্চমার্ক প্রতিবেদন", "সময়মতো ডেটা প্রবেশাধিকার প্রদান"],
                ["**উৎপাদ ২**", "উন্মুক্ত বেঞ্চমার্ক, কর্পাস ও মূল্যায়ন-পদ্ধতি প্রকাশিত", "বেঞ্চমার্ক প্রশ্ন; DOI-সহ প্রকাশ", "Zenodo ও GitHub রেকর্ড", "টীকাকার উপলব্ধ"],
                ["**উৎপাদ ৩**", "শাসনব্যবস্থা কার্যকর", "সনদ গৃহীত; ERRC-এর সিদ্ধান্ত প্রকাশিত", "বোর্ডের কার্যবিবরণী; নিবন্ধন", "সময়মতো সদস্য মনোনয়ন"],
                ["**উৎপাদ ৪**", "কর্মকর্তা ও বিশেষজ্ঞ প্রশিক্ষিত", "কর্মসূচিভিত্তিক প্রশিক্ষিত কর্মকর্তা", "উপস্থিতি ও মূল্যায়নের রেকর্ড", "সংস্থাগুলো অংশগ্রহণকারী মনোনয়ন দেয়"],
                ["**কার্যক্রম**", "অধ্যায় ১৫-এর কর্মপরিকল্পনা ও পাইলটগুলোর কাজের প্যাকেজ", "মাইলফলক MS1 থেকে MS9", "অগ্রগতি প্রতিবেদন", "পরিকল্পনামাফিক অর্থছাড়"],
            ],
        },
    },
    # ------------------------------------------------------------------ 56
    {
        "id": "56",
        "widths": [0.7, 3.0, 2.2, 2.4, 1.1],
        "title": {"en": "Research agenda and planned knowledge outputs", "bn": "গবেষণা-কর্মসূচি ও পরিকল্পিত জ্ঞান-উৎপাদ"},
        "cols": {"en": ["ID", "Research question", "Method", "Planned output", "Timing"],
                 "bn": ["আইডি", "গবেষণা প্রশ্ন", "পদ্ধতি", "পরিকল্পিত উৎপাদ", "সময়"]},
        "rows": {
            "en": [
                ["RQ1", "How well do lexical, dense and hybrid retrieval perform on Bangla and English policy text, and what closes the gap between the two languages?", "Benchmark experiments on BanglaPolicyQA; ablations of normalisation and glossary expansion", "Benchmark and methods paper; open code and data", "2027 to 2028"],
                ["RQ2", "Can abstention and citation verification be calibrated so that officials see few unsupported claims without losing useful answers?", "Threshold studies; human judgement of faithfulness", "Evaluation paper; calibration guidance", "2027 to 2029"],
                ["RQ3", "Do cited-search tools change the speed and quality of policy analysis?", "Matched-task studies with pilot users; interviews", "Empirical study of time-to-evidence and quality", "2028 to 2029"],
                ["RQ4", "How can risk tiering, gates and transparency registers be made to work in a public administration with new data laws?", "Design science and case study of BAPIL governance", "Peer-reviewed journal article on the Blueprint framework; policy brief", "Manuscript 2027"],
                ["RQ5", "How do OCR quality and Unicode normalisation affect downstream retrieval in Bangla?", "Controlled experiments on scanned and born-digital documents", "Dataset of corrected text with datasheet; short paper", "2028"],
                ["RQ6", "What institutional form sustains a public-interest AI policy lab in a lower-middle-income country?", "Comparative institutional analysis; evaluation evidence", "Institutional review for Blueprint 2.0", "2029"],
            ],
            "bn": [
                ["RQ1", "বাংলা ও ইংরেজি নীতি-টেক্সটে শব্দভিত্তিক, ঘন ও মিশ্র উদ্ধার কতটা কার্যকর, এবং দুই ভাষার ব্যবধান কীসে কমে?", "BanglaPolicyQA-তে বেঞ্চমার্ক পরীক্ষা; প্রমিতকরণ ও শব্দকোষ সম্প্রসারণের প্রভাব বিশ্লেষণ", "বেঞ্চমার্ক ও পদ্ধতি-প্রবন্ধ; উন্মুক্ত কোড ও ডেটা", "২০২৭ থেকে ২০২৮"],
                ["RQ2", "বিরতি ও উদ্ধৃতি-যাচাই কি এমনভাবে নির্ধারণ করা যায় যাতে কর্মকর্তারা কম অসমর্থিত দাবি দেখেন অথচ উপকারী উত্তর না হারান?", "সীমা-নির্ধারণ সমীক্ষা; বিশ্বস্ততার মানব-বিচার", "মূল্যায়ন-প্রবন্ধ; নির্ধারণ-নির্দেশিকা", "২০২৭ থেকে ২০২৯"],
                ["RQ3", "উদ্ধৃতিযুক্ত অনুসন্ধান সরঞ্জাম কি নীতি-বিশ্লেষণের গতি ও মান বদলায়?", "পাইলট ব্যবহারকারীদের সঙ্গে মিলিত-কাজ সমীক্ষা; সাক্ষাৎকার", "প্রমাণ-প্রাপ্তির সময় ও মানের অভিজ্ঞতাভিত্তিক সমীক্ষা", "২০২৮ থেকে ২০২৯"],
                ["RQ4", "নতুন ডেটা আইনের অধীনে একটি জনপ্রশাসনে ঝুঁকি-স্তর, গেট ও স্বচ্ছতা নিবন্ধন কীভাবে কার্যকর করা যায়?", "ডিজাইন সায়েন্স ও BAPIL শাসনের কেস স্টাডি", "ব্লুপ্রিন্টের কাঠামো বিষয়ে পিয়ার-রিভিউড জার্নাল প্রবন্ধ; নীতি-সংক্ষেপ", "পাণ্ডুলিপি ২০২৭"],
                ["RQ5", "OCR-এর মান ও ইউনিকোড প্রমিতকরণ বাংলায় পরবর্তী উদ্ধারকে কীভাবে প্রভাবিত করে?", "স্ক্যানকৃত ও জন্মগতভাবে ডিজিটাল নথিতে নিয়ন্ত্রিত পরীক্ষা", "ডেটাশিটসহ সংশোধিত টেক্সটের ডেটাসেট; সংক্ষিপ্ত প্রবন্ধ", "২০২৮"],
                ["RQ6", "নিম্ন-মধ্যম আয়ের দেশে কোন প্রাতিষ্ঠানিক রূপ জনস্বার্থমূলক এআই নীতি ল্যাবকে টেকসই রাখে?", "তুলনামূলক প্রাতিষ্ঠানিক বিশ্লেষণ; মূল্যায়নের প্রমাণ", "ব্লুপ্রিন্ট ২.০-এর জন্য প্রাতিষ্ঠানিক পর্যালোচনা", "২০২৯"],
            ],
        },
        "note": {"en": "Outputs are published open access with DOIs. Journal choice follows scope, open-access options and peer-review quality; no outcome of peer review is assumed.",
                 "bn": "উৎপাদগুলো DOI-সহ উন্মুক্ত-প্রবেশাধিকারে প্রকাশিত হবে। জার্নাল নির্বাচন পরিধি, উন্মুক্ত-প্রবেশাধিকারের সুযোগ ও পিয়ার রিভিউয়ের মান অনুযায়ী; পিয়ার রিভিউয়ের কোনো ফলাফল পূর্বানুমান করা হয় না।"},
    },
]

# Extra rows appended to the risk register (old table 19, new Table 55).
RISK_EXTRA = {
    "en": [
        ["R14", "Tools or outputs misused for misinformation or partisan purposes", "L", "H", "Access control for official tools; no synthetic media generation; usage policy; audit logs; public register", "ERRC"],
        ["R15", "Benchmark contamination or overfitting to the test set", "M", "M", "Private held-out test split; versioned freezing; periodic refresh; report on several sets", "ML lead"],
        ["R16", "Dependence on a few key people", "H", "H", "Documentation and open code; deputies for key roles; succession plan; shared ownership with the host", "Steering Board"],
        ["R17", "Technology obsolescence over the long horizon", "M", "M", "Modular design and ADRs; model re-selection at reviews; investment in data and evaluation rather than one model", "TAB"],
        ["R18", "Floods, cyclones, power or network outages affecting hosting", "M", "H", "Disaster-recovery site; offline backups; recovery targets of Table 35; low-bandwidth design", "Platform lead"],
    ],
    "bn": [
        ["R14", "ভুল তথ্য বা দলীয় উদ্দেশ্যে সরঞ্জাম বা ফলাফলের অপব্যবহার", "নি", "উ", "সরকারি সরঞ্জামে প্রবেশ নিয়ন্ত্রণ; কৃত্রিম মিডিয়া তৈরি নয়; ব্যবহার-নীতি; নিরীক্ষা লগ; জনসমক্ষে নিবন্ধন", "ERRC"],
        ["R15", "বেঞ্চমার্ক দূষণ বা পরীক্ষা-সেটে অতিমানানসই", "মা", "মা", "গোপন সংরক্ষিত পরীক্ষা-অংশ; সংস্করণভিত্তিক স্থিরকরণ; পর্যায়ক্রমিক হালনাগাদ; একাধিক সেটে প্রতিবেদন", "ML প্রধান"],
        ["R16", "কয়েকজন মূল ব্যক্তির ওপর নির্ভরতা", "উ", "উ", "নথিভুক্তি ও উন্মুক্ত কোড; মূল পদে সহকারী; উত্তরাধিকার পরিকল্পনা; স্বাগতিকের সঙ্গে যৌথ মালিকানা", "স্টিয়ারিং বোর্ড"],
        ["R17", "দীর্ঘ মেয়াদে প্রযুক্তির অপ্রচলন", "মা", "মা", "মডুলার নকশা ও ADR; পর্যালোচনায় মডেল পুনর্নির্বাচন; একক মডেলের বদলে ডেটা ও মূল্যায়নে বিনিয়োগ", "TAB"],
        ["R18", "বন্যা, ঘূর্ণিঝড়, বিদ্যুৎ বা নেটওয়ার্ক বিপর্যয়ে হোস্টিং ক্ষতিগ্রস্ত", "মা", "উ", "দুর্যোগ-পুনরুদ্ধার সাইট; অফলাইন ব্যাকআপ; সারণি ৩৫-এর পুনরুদ্ধার-লক্ষ্য; স্বল্প-ব্যান্ডউইথ নকশা", "প্ল্যাটফর্ম প্রধান"],
    ],
}
