# -*- coding: utf-8 -*-
"""Blueprint tables added by the October 2026 audit and revision (Annexes P to U, Tables 60 to 67)."""

import budget_model as _bm

_BN = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")


def _c(x):
    return "%.2f" % _bm.crore(x)


def _b(s):
    return s.translate(_BN)


# ------------------------------------------------------------------ Table 61: reconciliation
_BRIDGE_BN = {
    "Pre-audit draft budget (October 2026)": "পর্যালোচনার আগের খসড়া বাজেট (অক্টোবর ২০২৬)",
    "Year 2 and 3 amounts restated at Year 1 prices": "দ্বিতীয় ও তৃতীয় বছরের অঙ্ক প্রথম বছরের মূল্যে পুনর্নির্ধারণ",
    "Explicit escalation of taka costs (8% a year)": "টাকায় পরিশোধ্য ব্যয়ে সুস্পষ্ট মূল্যবৃদ্ধি (বছরে ৮%)",
    "Year 1 recruitment ramp (75% of positions filled on average)": "প্রথম বছরের ধাপে ধাপে নিয়োগ (গড়ে ৭৫% পদ পূরণ)",
    "Evaluation items added (out-of-scope set, citation judgements, annual system audit)": "মূল্যায়নের নতুন উপাদান (আওতাবহির্ভূত প্রশ্নসেট, উদ্ধৃতি-বিচার, ব্যবস্থাগুলোর বার্ষিক নিরীক্ষা)",
    "Separate contingency of 5% of direct costs": "প্রত্যক্ষ ব্যয়ের ৫% পৃথক আপৎকালীন সংস্থান",
}


def _bridge_rows():
    en, bn = [], []
    for label, total, delta in _bm.bridge():
        d = "" if delta is None else ("%+.2f" % _bm.crore(delta))
        en.append([label, _c(total), d or "Starting point"])
        bn.append([_BRIDGE_BN[label], _b(_c(total)), _b(d) if d else "সূচনাবিন্দু"])
    en[-1] = ["**" + en[-1][0] + " = revised base case**", "**" + en[-1][1] + "**", en[-1][2]]
    bn[-1] = ["**" + bn[-1][0] + " = সংশোধিত মূল হিসাব**", "**" + bn[-1][1] + "**", bn[-1][2]]
    return en, bn


# ------------------------------------------------------------------ Table 62: cost types and scenarios
def _type_rows():
    one, rec = _bm.one_time_recurring()
    rows = _bm.budget()
    oc = [sum(v[y] for k, v in rows.items() if k.startswith("Host") or k.startswith("Contingency")) for y in range(3)]
    base_y, base_t = _bm.totals()
    low_y, low_t = _bm.totals(_bm.SCENARIOS["low"])
    high_y, high_t = _bm.totals(_bm.SCENARIOS["high"])

    def r(label_en, label_bn, ys, bold=False):
        cells = [_c(x) for x in ys] + [_c(sum(ys))]
        if bold:
            cells = ["**%s**" % c for c in cells]
            label_en, label_bn = "**%s**" % label_en, "**%s**" % label_bn
        return [label_en] + cells, [label_bn] + [_b(c) for c in cells]

    pairs = [
        r("One-time direct costs (equipment, benchmark creation, studies and evaluations)", "এককালীন প্রত্যক্ষ ব্যয় (যন্ত্রপাতি, বেঞ্চমার্ক তৈরি, সমীক্ষা ও মূল্যায়ন)", one),
        r("Recurring direct costs (staff, editors, fellows, hosting, OCR, training, assurance)", "পুনরাবৃত্ত প্রত্যক্ষ ব্যয় (জনবল, সম্পাদক, ফেলো, হোস্টিং, OCR, প্রশিক্ষণ, আশ্বাস)", rec),
        r("Host overheads and contingency", "আয়োজকের পরোক্ষ ব্যয় ও আপৎকালীন সংস্থান", oc),
        r("Base case total", "মূল হিসাবের মোট", base_y, bold=True),
        r("Low scenario total", "নিম্ন পরিস্থিতির মোট", low_y),
        r("High scenario total", "উচ্চ পরিস্থিতির মোট", high_y),
    ]
    return [p[0] for p in pairs], [p[1] for p in pairs]


_BR_EN, _BR_BN = _bridge_rows()
_TY_EN, _TY_BN = _type_rows()

TABLES_F = [
    # ------------------------------------------------------------------ 60
    {
        "id": "60",
        "widths": [2.6, 1.3, 1.5, 2.6, 2.2],
        "title": {"en": "Evidence status of key claims (verified on 21 to 22 October 2026)",
                  "bn": "প্রধান দাবিগুলোর প্রমাণগত অবস্থা (২১ থেকে ২২ অক্টোবর ২০২৬-এ যাচাইকৃত)"},
        "cols": {"en": ["Claim", "Where", "Status", "Best available evidence", "Action in this edition"],
                 "bn": ["দাবি", "কোথায়", "অবস্থা", "সর্বোত্তম প্রাপ্ত প্রমাণ", "এই সংস্করণে পদক্ষেপ"]},
        "rows": {
            "en": [
                ["Bangladesh ranked 100 of 193 in the UN EGDI 2024, value 0.657 (111 in 2022)", "Ch. 2; Table 4", "Verified fact", "UN DESA E-Government Knowledgebase country data [120]; [21, 107]", "Kept; primary source added"],
                ["Bangladesh in the top tier of the ITU Global Cybersecurity Index 2024", "Ch. 2; Table 4", "Verified fact (official national source)", "BGD e-GOV CIRT: designated a Tier 1 role-model country [119]", "Wording made specific"],
                ["Ranked 82nd in the 2023 Government AI Readiness Index", "Ch. 2; Table 4", "Source-reported fact", "Sultana et al., 2026 [80]; the index report itself was not re-checked", "Citation corrected to [80]"],
                ["Personal Data Protection Act, 2026 enacted in April 2026", "Ch. 1, 2, 14; Tables 4, 42", "Source-reported fact, independently unverified", "Securiti, June 2026 [85]; Azam, September 2026 [116]; title listed on the official laws database (text not reviewed)", "Enactment and commencement separated; commencement marked to be confirmed"],
                ["National Data Management Bill, 2026 passed on 10 April 2026", "Ch. 2, 14; Table 42", "Source-reported fact", "Daily Sun, 10 April 2026 [86]", "Ordinance name corrected; features attributed to the 2025 Ordinance"],
                ["Under the 2025 Ordinance, the sections on chief data officers, complaints and offences did not commence immediately", "Ch. 8, 14; Table 42", "Source-reported fact (secondary legal commentary)", "Greenleaf and Al Razi, June 2026 [113]; 18-month compliance window reported [114]", "Added; position under the Act referred to legal counsel"],
                ["Cyber Security Bill, 2026 passed on 10 April 2026; amendment on AI-generated content passed by 30 June 2026", "Ch. 14; Table 42", "Source-reported fact", "[86], [87]", "Wording qualified; commencement to be confirmed"],
                ["Draft National AI Policy 2026-2030 released for consultation in January 2026", "Ch. 1, 2, 14", "Source-reported fact", "The Daily Star, 26 January 2026 [88]; The Financial Express, 29 January 2026 [89]", "Kept"],
                ["The draft policy proposes labelling of AI-generated content", "Sect. 13.8; Table 41; Annex N", "Not supported by the cited sources", "[88] and [89] describe measures against false or misleading AI-generated content", "Corrected; labelling is now presented as BAPIL's own rule"],
                ["National AI policy drafting to begin in Q4 2026 with a joint team", "Ch. 1, 14, 21", "Source-reported fact", "The Daily Observer, 10 August 2026 [91]", "Kept"],
                ["AI Hub project cost Tk 192.66 crore; project under implementation", "Ch. 3, 17; Table 42", "Partly incorrect", "Proposal awaiting approval in June 2026 [35]; USD 13 million grant agreement signed in August 2026 [117]", "Status corrected; comparison kept for scale only"],
                ["Reference implementation published on GitHub and archived on Zenodo (release v1.1.0)", "Front matter; Ch. 1, 11, 16, 21; Table 1", "Future milestone at the time of writing", "Code with 49 passing unit tests exists in the repository's working branch; release v1.1.0 and the Blueprint DOI were not yet public on 22 October 2026", "Reworded as issued with this Blueprint; the DOI record is published only after the release exists (Annex D)"],
                ["Demonstration Recall@10 of 0.92 and 6 of 6 correct abstentions", "Sect. 11.5", "Research finding (small demonstration)", "Evaluation report generated by the build: 10 documents, about 1,700 passages, 24 questions", "Kept with its limitation"],
                ["Recall@10 at least 0.85 and citation precision at least 0.95", "Ch. 9, 12; Tables 28, 38", "Proposed target", "Not yet measured", "Labelled as targets; measurement protocol added (Annex R)"],
                ["Budget of Tk 18.49 crore; annual totals 4.96, 6.71 and 6.83", "Ch. 17; Tables 49, 50; Summary; Memo", "Planning assumption; rounding difference", "Unrounded total Tk 18.4868 crore; annual figures rounded independently", "Budget revised with escalation, recruitment ramp and contingency; reconciled in Table 61"],
                ["Grade 9 basic pay of Tk 44,000 in the Ninth National Pay Scale", "Sect. 17.5; Table 49", "Source-reported fact (Cabinet approval)", "The Financial Express, 31 August 2026 [109]; gazette not seen", "Kept; status noted"],
                ["Exchange rate of Tk 123.65 per US dollar on 19 October 2026", "Table 49", "Verified fact", "Bangladesh Bank [110]", "Kept"],
                ["Inflation of 8.34% in September 2026", "Table 49", "Source-reported fact", "Dhaka Tribune, 7 October 2026, reporting BBS data [118]", "Added as the basis for escalation"],
                ["L40S GPU card about USD 7,500", "Table 49", "Source-reported fact (vendor publication)", "Modal, August 2025 [111]", "Kept as a price basis; quotations required"],
                ["Analyst time saved worth about Tk 0.7 crore a year", "Sect. 17.5", "Author's analysis", "Calculation from [109] and assumed usage", "Kept and labelled as illustrative"],
                ["Steering Board, ERRC and TAB with stated powers", "Ch. 5; Annexes E to G", "Design recommendation", "No body has been constituted or approved", "Status, appointment and limits set out in Annex S"],
                ["Long-term targets for 2028 to 2041", "Ch. 16; Table 46", "Proposed target", "Not applicable", "Kept; revised at strategic reviews"],
            ],
            "bn": [
                ["জাতিসংঘের EGDI ২০২৪-এ বাংলাদেশ ১৯৩ দেশের মধ্যে ১০০তম, মান ০.৬৫৭ (২০২২ সালে ১১১তম)", "অধ্যায় ২; সারণি ৪", "যাচাইকৃত তথ্য", "জাতিসংঘের ই-সরকার জ্ঞানভান্ডারের দেশভিত্তিক তথ্য [120]; [21, 107]", "বহাল; প্রাথমিক উৎস যুক্ত"],
                ["আইটিইউ গ্লোবাল সাইবার সিকিউরিটি ইনডেক্স ২০২৪-এ বাংলাদেশ শীর্ষ স্তরে", "অধ্যায় ২; সারণি ৪", "যাচাইকৃত তথ্য (সরকারি জাতীয় উৎস)", "বিজিডি ই-গভ সার্ট: টিয়ার ১ রোল-মডেল দেশ হিসেবে চিহ্নিত [119]", "ভাষা সুনির্দিষ্ট করা হয়েছে"],
                ["২০২৩ সালের সরকারি এআই প্রস্তুতি সূচকে ৮২তম", "অধ্যায় ২; সারণি ৪", "উৎস-প্রতিবেদিত তথ্য", "সুলতানা ও সহলেখক, ২০২৬ [80]; সূচকের মূল প্রতিবেদন পুনরায় যাচাই করা হয়নি", "তথ্যসূত্র সংশোধন করে [80]"],
                ["এপ্রিল ২০২৬-এ ব্যক্তিগত উপাত্ত সুরক্ষা আইন, ২০২৬ প্রণীত", "অধ্যায় ১, ২, ১৪; সারণি ৪, ৪২", "উৎস-প্রতিবেদিত তথ্য, স্বাধীনভাবে অযাচাইকৃত", "সিকিউরিটি, জুন ২০২৬ [85]; আজম, সেপ্টেম্বর ২০২৬ [116]; সরকারি আইন-ডেটাবেসে শিরোনাম তালিকাভুক্ত (পাঠ পর্যালোচিত নয়)", "প্রণয়ন ও কার্যকারিতা আলাদা করা হয়েছে; কার্যকারিতা নিশ্চিতকরণসাপেক্ষ"],
                ["১০ এপ্রিল ২০২৬-এ জাতীয় উপাত্ত ব্যবস্থাপনা বিল, ২০২৬ পাস", "অধ্যায় ২, ১৪; সারণি ৪২", "উৎস-প্রতিবেদিত তথ্য", "ডেইলি সান, ১০ এপ্রিল ২০২৬ [86]", "অধ্যাদেশের নাম সংশোধিত; বৈশিষ্ট্যগুলো ২০২৫ সালের অধ্যাদেশের বলে উল্লিখিত"],
                ["২০২৫ সালের অধ্যাদেশে প্রধান ডেটা কর্মকর্তা, অভিযোগ ও অপরাধ-সংক্রান্ত ধারা তাৎক্ষণিকভাবে কার্যকর হয়নি", "অধ্যায় ৮, ১৪; সারণি ৪২", "উৎস-প্রতিবেদিত তথ্য (মাধ্যমিক আইনি ভাষ্য)", "গ্রিনলিফ ও আল রাজী, জুন ২০২৬ [113]; ১৮ মাসের সম্মতি-সময়সীমা প্রতিবেদিত [114]", "যুক্ত; আইনের অধীনে অবস্থান আইনজীবীর কাছে প্রেরিত"],
                ["১০ এপ্রিল ২০২৬-এ সাইবার নিরাপত্তা বিল, ২০২৬ পাস; এআই-সৃষ্ট কনটেন্ট-সংক্রান্ত সংশোধনী ৩০ জুন ২০২৬-এর মধ্যে পাস", "অধ্যায় ১৪; সারণি ৪২", "উৎস-প্রতিবেদিত তথ্য", "[86], [87]", "ভাষা শর্তযুক্ত; কার্যকারিতা নিশ্চিতকরণসাপেক্ষ"],
                ["জানুয়ারি ২০২৬-এ খসড়া জাতীয় এআই নীতি ২০২৬-২০৩০ জন-পরামর্শে প্রকাশিত", "অধ্যায় ১, ২, ১৪", "উৎস-প্রতিবেদিত তথ্য", "দ্য ডেইলি স্টার, ২৬ জানুয়ারি ২০২৬ [88]; দ্য ফাইন্যান্সিয়াল এক্সপ্রেস, ২৯ জানুয়ারি ২০২৬ [89]", "বহাল"],
                ["খসড়া নীতি এআই-সৃষ্ট কনটেন্টে লেবেল প্রস্তাব করে", "অনুচ্ছেদ ১৩.৮; সারণি ৪১; সংযুক্তি ঢ", "উদ্ধৃত উৎসে সমর্থিত নয়", "[88] ও [89]-এ এআই-সৃষ্ট মিথ্যা বা বিভ্রান্তিকর কনটেন্ট প্রতিরোধের ব্যবস্থার বর্ণনা আছে", "সংশোধিত; লেবেল এখন BAPIL-এর নিজস্ব নিয়ম হিসেবে উপস্থাপিত"],
                ["একটি যৌথ দলের মাধ্যমে ২০২৬-এর চতুর্থ ত্রৈমাসিকে জাতীয় এআই নীতি প্রণয়ন শুরু", "অধ্যায় ১, ১৪, ২১", "উৎস-প্রতিবেদিত তথ্য", "দ্য ডেইলি অবজারভার, ১০ আগস্ট ২০২৬ [91]", "বহাল"],
                ["এআই হাব প্রকল্পের ব্যয় ১৯২.৬৬ কোটি টাকা; প্রকল্প বাস্তবায়নাধীন", "অধ্যায় ৩, ১৭; সারণি ৪২", "আংশিক ভুল", "জুন ২০২৬-এ প্রস্তাবটি অনুমোদনের অপেক্ষায় [35]; আগস্ট ২০২৬-এ ১৩ মিলিয়ন মার্কিন ডলারের অনুদান-চুক্তি স্বাক্ষরিত [117]", "অবস্থা সংশোধিত; তুলনা শুধু মাত্রা বোঝাতে রাখা হয়েছে"],
                ["রেফারেন্স বাস্তবায়ন গিটহাবে প্রকাশিত ও Zenodo-তে সংরক্ষিত (রিলিজ v1.1.0)", "সূচনা-অংশ; অধ্যায় ১, ১১, ১৬, ২১; সারণি ১", "রচনার সময় ভবিষ্যৎ মাইলফলক", "রিপোজিটরির কর্ম-শাখায় ৪৯টি উত্তীর্ণ ইউনিট পরীক্ষাসহ কোড বিদ্যমান; ২২ অক্টোবর ২০২৬ পর্যন্ত রিলিজ v1.1.0 ও ব্লুপ্রিন্টের DOI প্রকাশ্য হয়নি", "এই ব্লুপ্রিন্টের সঙ্গে প্রকাশিত বলে পুনর্লিখিত; রিলিজ প্রকাশের পরই DOI রেকর্ড প্রকাশিত হবে (সংযুক্তি ঘ)"],
                ["প্রদর্শনীতে Recall@10 ০.৯২ এবং ৬টির মধ্যে ৬টি সঠিক বিরতি", "অনুচ্ছেদ ১১.৫", "গবেষণা-ফলাফল (ক্ষুদ্র প্রদর্শনী)", "বিল্ডে তৈরি মূল্যায়ন প্রতিবেদন: ১০টি নথি, প্রায় ১,৭০০টি অনুচ্ছেদ, ২৪টি প্রশ্ন", "সীমাবদ্ধতাসহ বহাল"],
                ["Recall@10 কমপক্ষে ০.৮৫ ও উদ্ধৃতির নির্ভুলতা কমপক্ষে ০.৯৫", "অধ্যায় ৯, ১২; সারণি ২৮, ৩৮", "প্রস্তাবিত লক্ষ্য", "এখনো পরিমাপ করা হয়নি", "লক্ষ্য হিসেবে চিহ্নিত; পরিমাপ-প্রটোকল যুক্ত (সংযুক্তি দ)"],
                ["বাজেট ১৮.৪৯ কোটি টাকা; বার্ষিক মোট ৪.৯৬, ৬.৭১ ও ৬.৮৩", "অধ্যায় ১৭; সারণি ৪৯, ৫০; সারসংক্ষেপ; স্মারক", "পরিকল্পনা-অনুমান; আসন্নীকরণজনিত পার্থক্য", "আসন্নীকরণের আগের মোট ১৮.৪৮৬৮ কোটি টাকা; বার্ষিক অঙ্কগুলো আলাদাভাবে আসন্নীকৃত", "মূল্যবৃদ্ধি, ধাপে ধাপে নিয়োগ ও আপৎকালীন সংস্থানসহ বাজেট সংশোধিত; সারণি ৬১-এ মিলকরণ"],
                ["নবম জাতীয় বেতন স্কেলে গ্রেড ৯-এর মূল বেতন ৪৪,০০০ টাকা", "অনুচ্ছেদ ১৭.৫; সারণি ৪৯", "উৎস-প্রতিবেদিত তথ্য (মন্ত্রিসভার অনুমোদন)", "দ্য ফাইন্যান্সিয়াল এক্সপ্রেস, ৩১ আগস্ট ২০২৬ [109]; গেজেট দেখা হয়নি", "বহাল; অবস্থা উল্লিখিত"],
                ["১৯ অক্টোবর ২০২৬-এ বিনিময় হার প্রতি মার্কিন ডলারে ১২৩.৬৫ টাকা", "সারণি ৪৯", "যাচাইকৃত তথ্য", "বাংলাদেশ ব্যাংক [110]", "বহাল"],
                ["সেপ্টেম্বর ২০২৬-এ মূল্যস্ফীতি ৮.৩৪%", "সারণি ৪৯", "উৎস-প্রতিবেদিত তথ্য", "ঢাকা ট্রিবিউন, ৭ অক্টোবর ২০২৬, বিবিএস-এর তথ্য উদ্ধৃত করে [118]", "মূল্যবৃদ্ধির ভিত্তি হিসেবে যুক্ত"],
                ["একটি L40S GPU কার্ড প্রায় ৭,৫০০ মার্কিন ডলার", "সারণি ৪৯", "উৎস-প্রতিবেদিত তথ্য (বিক্রেতার প্রকাশনা)", "মোডাল, আগস্ট ২০২৫ [111]", "মূল্যের ভিত্তি হিসেবে বহাল; দরপত্র প্রয়োজন"],
                ["বিশ্লেষকদের সাশ্রয়কৃত সময়ের মূল্য বছরে প্রায় ০.৭ কোটি টাকা", "অনুচ্ছেদ ১৭.৫", "লেখকের বিশ্লেষণ", "[109] ও অনুমিত ব্যবহারের ভিত্তিতে হিসাব", "বহাল ও দৃষ্টান্তমূলক হিসেবে চিহ্নিত"],
                ["উল্লিখিত ক্ষমতাসহ স্টিয়ারিং বোর্ড, ERRC ও TAB", "অধ্যায় ৫; সংযুক্তি ঙ থেকে ছ", "নকশাগত সুপারিশ", "কোনো সংস্থা গঠিত বা অনুমোদিত হয়নি", "অবস্থা, নিয়োগ ও সীমা সংযুক্তি ধ-তে বর্ণিত"],
                ["২০২৮ থেকে ২০৪১ পর্যন্ত দীর্ঘমেয়াদি লক্ষ্য", "অধ্যায় ১৬; সারণি ৪৬", "প্রস্তাবিত লক্ষ্য", "প্রযোজ্য নয়", "বহাল; কৌশলগত পর্যালোচনায় সংশোধিত হবে"],
            ],
        },
        "note": {"en": "Status labels are defined in Annex P. Web sources were consulted on 21 and 22 October 2026. The official Laws of Bangladesh database does not permit automated retrieval, so statutory texts were not reviewed directly.",
                 "bn": "অবস্থা-নির্দেশক লেবেলগুলোর সংজ্ঞা সংযুক্তি ত-তে দেওয়া আছে। ওয়েব উৎসগুলো ২১ ও ২২ অক্টোবর ২০২৬-এ দেখা হয়েছে। সরকারি আইন-ডেটাবেস স্বয়ংক্রিয় সংগ্রহের অনুমতি দেয় না, তাই আইনের পাঠ সরাসরি পর্যালোচনা করা হয়নি।"},
    },
    # ------------------------------------------------------------------ 61
    {
        "id": "61",
        "widths": [5.0, 1.3, 1.3],
        "title": {"en": "Reconciliation of the indicative budget with the draft before this review (Tk crore, 36 months)",
                  "bn": "এই পর্যালোচনার আগের খসড়ার সঙ্গে নির্দেশক বাজেটের মিলকরণ (কোটি টাকা, ৩৬ মাস)"},
        "cols": {"en": ["Step", "36-month total", "Change"], "bn": ["ধাপ", "৩৬ মাসের মোট", "পরিবর্তন"]},
        "rows": {"en": _BR_EN, "bn": _BR_BN},
        "note": {"en": "Each step is computed by blueprint/src/budget_model.py (function bridge) by switching one assumption at a time. The draft's annual totals (4.96, 6.71 and 6.83) added to 18.50 only because each was rounded separately; the unrounded draft total was Tk 18.4868 crore.",
                 "bn": "প্রতিটি ধাপ blueprint/src/budget_model.py (bridge ফাংশন) দ্বারা একবারে একটি অনুমান বদলে হিসাব করা হয়েছে। খসড়ার বার্ষিক মোট (৪.৯৬, ৬.৭১ ও ৬.৮৩) যোগ করলে ১৮.৫০ হতো কেবল প্রতিটি আলাদাভাবে আসন্নীকৃত হওয়ায়; আসন্নীকরণের আগে খসড়ার মোট ছিল ১৮.৪৮৬৮ কোটি টাকা।"},
    },
    # ------------------------------------------------------------------ 62
    {
        "id": "62",
        "widths": [4.2, 1.0, 1.0, 1.0, 1.1],
        "title": {"en": "Budget by cost type, with low, base and high scenarios (Tk crore)",
                  "bn": "ব্যয়ের ধরনভিত্তিক বাজেট, নিম্ন, মূল ও উচ্চ পরিস্থিতিসহ (কোটি টাকা)"},
        "cols": {"en": ["Item", "Year 1", "Year 2", "Year 3", "Total"], "bn": ["বিষয়", "বছর ১", "বছর ২", "বছর ৩", "মোট"]},
        "rows": {"en": _TY_EN, "bn": _TY_BN},
        "note": {"en": "Low scenario: staff costs 15% lower, escalation 6%, equipment 20% cheaper, Tk 120 per US dollar. High scenario: staff costs 20% higher, escalation 10%, equipment 25% dearer (for example import duty and VAT), Tk 135 per US dollar, contingency 10% and USD 20,000 of cloud compute for Stage 1 adaptation. Figures are rounded independently.",
                 "bn": "নিম্ন পরিস্থিতি: জনবল-ব্যয় ১৫% কম, মূল্যবৃদ্ধি ৬%, যন্ত্রপাতি ২০% সস্তা, প্রতি মার্কিন ডলারে ১২০ টাকা। উচ্চ পরিস্থিতি: জনবল-ব্যয় ২০% বেশি, মূল্যবৃদ্ধি ১০%, যন্ত্রপাতি ২৫% বেশি দামি (যেমন আমদানি শুল্ক ও ভ্যাট), প্রতি মার্কিন ডলারে ১৩৫ টাকা, আপৎকালীন সংস্থান ১০% এবং পর্যায় ১ অভিযোজনের জন্য ২০,০০০ মার্কিন ডলারের ক্লাউড কম্পিউটিং। প্রতিটি অঙ্ক আলাদাভাবে আসন্নীকৃত।"},
    },
    # ------------------------------------------------------------------ 63
    {
        "id": "63",
        "widths": [1.5, 2.6, 2.2, 2.0, 2.2],
        "title": {"en": "Evaluation protocol and release-gate rules",
                  "bn": "মূল্যায়ন প্রটোকল ও রিলিজ-গেটের নিয়ম"},
        "cols": {"en": ["Measure", "Definition", "Test set and sample", "Method and responsibility", "Decision rule"],
                 "bn": ["পরিমাপ", "সংজ্ঞা", "পরীক্ষা-সেট ও নমুনা", "পদ্ধতি ও দায়িত্ব", "সিদ্ধান্ত-নিয়ম"]},
        "rows": {
            "en": [
                ["Recall@10, MRR@10, nDCG@10", "For each answerable question, a hit if any gold passage is in the top 10; Recall@10 is the mean of hits. MRR and nDCG as in Table 28", "Private test split: at least 300 answerable questions in v0 (about 150 per language) and 1,200 in v1", "Automatic scoring by the evaluation team; script, outputs, configuration and corpus version archived", "Threshold met if the point estimate meets it and the 95% interval is no wider than plus or minus 5 points (about 4 points at n = 300); otherwise annotate more items before deciding"],
                ["Citation precision", "Share of sampled answer sentences whose cited passage fully supports the sentence (supported, partly supported or not supported; only supported counts)", "400 answer sentences drawn at random from test answers, at least 200 per language", "Two trained annotators who do not know the system version; a third adjudicates; Cohen's kappa reported (target 0.70 or more)", "Point estimate at least 0.95 (interval about plus or minus 2 points at n = 400)"],
                ["Unsupported-claim rate", "Share of sampled sentences not supported by any retrieved passage", "Same sample as citation precision", "Same annotators", "Point estimate at most 2%"],
                ["Correct abstention and answer coverage", "Abstentions on out-of-scope questions; answers on answerable questions", "150 out-of-scope test questions in v0 (200 written: 50 development, 150 test); all answerable test questions", "Automatic", "Abstention at least 0.90 (interval about plus or minus 5 points); coverage at least 0.80"],
                ["Language parity", "Recall@10 for English minus Recall@10 for Bangla, with a bootstrap interval", "Per-language test subsets", "Automatic", "Reported in v0, where the interval is too wide to decide; release condition from v1 onwards"],
                ["Robustness", "Recall@10 on variant-spelling and romanised queries, on questions answered in OCR-derived documents, and on code-mixed queries", "At least 100, 100 and 50 test items respectively", "Automatic", "Variant spelling at least 0.75; the other two reported with no gate in v0"],
                ["Prompt injection and prohibited outputs", "Share of red-team attempts (instructions hidden in documents or queries) that change behaviour; requests for prohibited outputs", "At least 100 attempts, refreshed at each release", "Security lead and an external red team", "At most 5%; any leak of non-public data is a failure"],
                ["Privacy", "Presence of P2 or P3 data in logs, outputs or evaluation sets; access-control tests", "Log samples and automated scans", "Governance analyst; annual independent audit", "Zero findings"],
                ["Latency and availability", "p95 response time; share of working hours available", "Load test with 30 concurrent users at G2; monitoring during G3", "Platform lead", "3 s for search and 10 s for answers; at least 99%"],
                ["Usefulness", "Mean rating on a 5-point scale", "At least 30 pilot users; at least 100 answers rated by Bangla editors", "Product owner and evaluation team", "At least 4.0"],
                ["P2 extraction accuracy", "Share of extracted table cells that match the source document", "Stratified random sample of at least 1,000 cells across years and ministries", "Two independent checkers", "At least 99% (interval about plus or minus 0.6 points)"],
                ["Time to evidence", "Median time to find and cite authoritative evidence on matched tasks, with and without the tool", "At least 20 analysts, 6 tasks each, crossover design", "Evaluation team; independent evaluator at month 18", "Effect and interval reported; informs G4, no pass mark at G3"],
                ["Reproducibility", "Re-scoring of archived outputs on the private split", "Every release used for a gate decision", "Independent evaluator before G4", "Re-scored metrics within 1 point of those reported"],
            ],
            "bn": [
                ["Recall@10, MRR@10, nDCG@10", "প্রতিটি উত্তরযোগ্য প্রশ্নে কোনো সঠিক অনুচ্ছেদ প্রথম ১০টিতে থাকলে সফল; সফলতার গড়ই Recall@10। MRR ও nDCG সারণি ২৮ অনুযায়ী", "ব্যক্তিগত পরীক্ষা-অংশ: v0-তে কমপক্ষে ৩০০টি উত্তরযোগ্য প্রশ্ন (প্রতি ভাষায় প্রায় ১৫০টি) এবং v1-এ ১,২০০টি", "মূল্যায়ন দলের স্বয়ংক্রিয় স্কোরিং; স্ক্রিপ্ট, ফলাফল, কনফিগারেশন ও কর্পাস সংস্করণ সংরক্ষিত", "বিন্দু-প্রাক্কলন সীমা অর্জন করলে এবং ৯৫% ব্যবধান ধনাত্মক-ঋণাত্মক ৫ পয়েন্টের বেশি চওড়া না হলে সীমা অর্জিত (n = ৩০০-এ প্রায় ৪ পয়েন্ট); অন্যথায় সিদ্ধান্তের আগে আরও প্রশ্ন টীকাকরণ"],
                ["উদ্ধৃতির নির্ভুলতা", "নমুনাভুক্ত উত্তর-বাক্যের মধ্যে যেগুলোর উদ্ধৃত অনুচ্ছেদ বাক্যটিকে পুরোপুরি সমর্থন করে তার অনুপাত (সমর্থিত, আংশিক সমর্থিত বা অসমর্থিত; শুধু সমর্থিত গণ্য)", "পরীক্ষা-উত্তর থেকে দৈবভাবে নেওয়া ৪০০টি উত্তর-বাক্য, প্রতি ভাষায় কমপক্ষে ২০০টি", "ব্যবস্থার সংস্করণ না জানা দুজন প্রশিক্ষিত টীকাকার; তৃতীয়জন নিষ্পত্তি করেন; কোহেনের কাপ্পা প্রতিবেদিত (লক্ষ্য ০.৭০ বা তার বেশি)", "বিন্দু-প্রাক্কলন কমপক্ষে ০.৯৫ (n = ৪০০-এ ব্যবধান প্রায় ধনাত্মক-ঋণাত্মক ২ পয়েন্ট)"],
                ["অসমর্থিত দাবির হার", "নমুনাভুক্ত বাক্যের মধ্যে যেগুলো কোনো উদ্ধারকৃত অনুচ্ছেদ দ্বারা সমর্থিত নয় তার অনুপাত", "উদ্ধৃতির নির্ভুলতার একই নমুনা", "একই টীকাকার", "বিন্দু-প্রাক্কলন সর্বোচ্চ ২%"],
                ["সঠিক বিরতি ও উত্তর-আওতা", "আওতাবহির্ভূত প্রশ্নে বিরতি; উত্তরযোগ্য প্রশ্নে উত্তর", "v0-তে ১৫০টি আওতাবহির্ভূত পরীক্ষা-প্রশ্ন (রচিত ২০০টি: উন্নয়নে ৫০, পরীক্ষায় ১৫০); সব উত্তরযোগ্য পরীক্ষা-প্রশ্ন", "স্বয়ংক্রিয়", "বিরতি কমপক্ষে ০.৯০ (ব্যবধান প্রায় ধনাত্মক-ঋণাত্মক ৫ পয়েন্ট); আওতা কমপক্ষে ০.৮০"],
                ["ভাষাগত সমতা", "ইংরেজির Recall@10 বিয়োগ বাংলার Recall@10, বুটস্ট্র্যাপ ব্যবধানসহ", "ভাষাভিত্তিক পরীক্ষা-উপসেট", "স্বয়ংক্রিয়", "v0-তে প্রতিবেদিত, কারণ ব্যবধান সিদ্ধান্তের জন্য বেশি চওড়া; v1 থেকে রিলিজের শর্ত"],
                ["স্থিতিশীলতা", "ভিন্ন বানান ও রোমান হরফের প্রশ্নে, OCR-নির্ভর নথিতে উত্তরযুক্ত প্রশ্নে এবং মিশ্র-ভাষার প্রশ্নে Recall@10", "যথাক্রমে কমপক্ষে ১০০, ১০০ ও ৫০টি পরীক্ষা-প্রশ্ন", "স্বয়ংক্রিয়", "ভিন্ন বানানে কমপক্ষে ০.৭৫; বাকি দুটি v0-তে গেট ছাড়া প্রতিবেদিত"],
                ["প্রম্পট-ইনজেকশন ও নিষিদ্ধ ফলাফল", "রেড-টিমের প্রচেষ্টার (নথি বা প্রশ্নে লুকানো নির্দেশ) মধ্যে যেগুলো আচরণ বদলায় তার অনুপাত; নিষিদ্ধ ফলাফলের অনুরোধ", "কমপক্ষে ১০০টি প্রচেষ্টা, প্রতি রিলিজে হালনাগাদ", "নিরাপত্তা প্রধান ও একটি বহিস্থ রেড-টিম", "সর্বোচ্চ ৫%; অ-উন্মুক্ত ডেটার যেকোনো ফাঁস অনুত্তীর্ণ"],
                ["গোপনীয়তা", "লগ, ফলাফল বা মূল্যায়ন-সেটে P2 বা P3 ডেটার উপস্থিতি; প্রবেশাধিকার-নিয়ন্ত্রণ পরীক্ষা", "লগের নমুনা ও স্বয়ংক্রিয় স্ক্যান", "শাসন বিশ্লেষক; বার্ষিক স্বাধীন নিরীক্ষা", "শূন্য অনুসন্ধান-ফল"],
                ["লেটেন্সি ও প্রাপ্যতা", "p95 প্রতিক্রিয়া-সময়; কর্মঘণ্টার যে অংশে সেবা চালু", "G2-তে ৩০ জন একযোগে ব্যবহারকারীসহ চাপ-পরীক্ষা; G3 চলাকালে পর্যবেক্ষণ", "প্ল্যাটফর্ম প্রধান", "অনুসন্ধানে ৩ সেকেন্ড ও উত্তরে ১০ সেকেন্ড; কমপক্ষে ৯৯%"],
                ["উপযোগিতা", "৫-পয়েন্ট স্কেলে গড় মূল্যায়ন", "কমপক্ষে ৩০ জন পাইলট ব্যবহারকারী; বাংলা সম্পাদকদের মূল্যায়িত কমপক্ষে ১০০টি উত্তর", "প্রোডাক্ট ওনার ও মূল্যায়ন দল", "কমপক্ষে ৪.০"],
                ["P2 নিষ্কাশনের নির্ভুলতা", "নিষ্কাশিত সারণি-ঘরের মধ্যে যেগুলো মূল নথির সঙ্গে মেলে তার অনুপাত", "বছর ও মন্ত্রণালয়জুড়ে স্তরভিত্তিক দৈবচয়িত কমপক্ষে ১,০০০টি ঘর", "দুজন স্বাধীন যাচাইকারী", "কমপক্ষে ৯৯% (ব্যবধান প্রায় ধনাত্মক-ঋণাত্মক ০.৬ পয়েন্ট)"],
                ["প্রমাণ-প্রাপ্তির সময়", "সমতুল্য কাজে সরঞ্জামসহ ও সরঞ্জাম ছাড়া প্রামাণ্য প্রমাণ খুঁজে উদ্ধৃত করার মধ্যক সময়", "কমপক্ষে ২০ জন বিশ্লেষক, প্রত্যেকে ৬টি কাজ, ক্রসওভার নকশা", "মূল্যায়ন দল; মাস ১৮-এ স্বাধীন মূল্যায়নকারী", "প্রভাব ও ব্যবধান প্রতিবেদিত; G4-কে তথ্য দেয়, G3-তে উত্তীর্ণ-নম্বর নেই"],
                ["পুনরুৎপাদনযোগ্যতা", "ব্যক্তিগত অংশে সংরক্ষিত ফলাফলের পুনঃস্কোরিং", "গেট-সিদ্ধান্তে ব্যবহৃত প্রতিটি রিলিজ", "G4-এর আগে স্বাধীন মূল্যায়নকারী", "পুনঃস্কোরকৃত মাপকাঠি প্রতিবেদিত মানের ১ পয়েন্টের মধ্যে"],
            ],
        },
        "note": {"en": "Intervals are 95% Wilson or bootstrap intervals. BanglaPolicyQA v0 has 500 answerable questions (40% public development, 60% private test) and 200 out-of-scope questions. Sample sizes are minimums; the ERRC and TAB may require more for tier T2 uses.",
                 "bn": "ব্যবধানগুলো ৯৫% উইলসন বা বুটস্ট্র্যাপ ব্যবধান। BanglaPolicyQA v0-তে ৫০০টি উত্তরযোগ্য প্রশ্ন (৪০% উন্মুক্ত উন্নয়ন-অংশ, ৬০% ব্যক্তিগত পরীক্ষা-অংশ) ও ২০০টি আওতাবহির্ভূত প্রশ্ন আছে। নমুনার আকার ন্যূনতম; T2 স্তরের ব্যবহারে ERRC ও TAB আরও বেশি চাইতে পারে।"},
    },
    # ------------------------------------------------------------------ 64
    {
        "id": "64",
        "widths": [1.9, 1.8, 2.2, 1.3, 2.2, 1.6, 1.9],
        "title": {"en": "Governance bodies: status, appointment, decision rights and safeguards",
                  "bn": "শাসন-সংস্থা: অবস্থা, নিয়োগ, সিদ্ধান্তের অধিকার ও সুরক্ষা"},
        "cols": {"en": ["Body", "Status and basis", "Membership and appointment", "Chair and secretariat", "Decision rights and limits", "Reporting and transparency", "Independence and conflicts"],
                 "bn": ["সংস্থা", "অবস্থা ও ভিত্তি", "সদস্যপদ ও নিয়োগ", "সভাপতি ও সচিবালয়", "সিদ্ধান্তের অধিকার ও সীমা", "প্রতিবেদন ও স্বচ্ছতা", "স্বাধীনতা ও স্বার্থের দ্বন্দ্ব"]},
        "rows": {
            "en": [
                ["**Steering Board**", "Proposed; created by the MoU and the host agreement; no statutory power", "7 to 9 members nominated by their organisations; academic and civil-society members chosen by open call; 3-year terms", "Co-chairs from the ICT Division and the host; secretariat in the Director's office", "Approves plans, budgets, partnerships and senior appointments; joint G4 decisions with agencies; cannot override an ERRC refusal or the law", "Meets quarterly; decisions and minutes published in summary; annual report", "Annual declarations; recusal; the industry member does not vote on procurement in its sector"],
                ["**Ethics and Risk Review Committee (ERRC)**", "Proposed; established by the charter; binding inside BAPIL through the charter and host agreement, not by statute", "5 to 7 members, a majority external, selected through an open call by the independent nominations panel and confirmed by the Steering Board; 3-year terms, renewable once; removal only for cause by two thirds of the Board after a hearing", "External chair elected by members; secretariat provided by the governance analyst", "Approves, approves with conditions, refuses or suspends tier T2 and T3 work at G1, G2 and G4; refusal is binding; cannot authorise what the law or the host forbids", "Decision summaries within 30 days; dissent recorded; annual report", "Majority external; no member employed by a supplier under evaluation; protected budget; staff may raise concerns directly"],
                ["**Technical Architecture Board (TAB)**", "Proposed; internal technical body under the Director", "Lead engineers, the security lead and two external reviewers appointed by the Director with Board approval", "Chief engineer; secretariat in the platform team", "Approves designs at G1, models and major dependencies; maintains ADRs", "ADRs public in the repository; meets monthly", "External reviewers declare commercial interests and do not review their employers' products"],
                ["**International Advisory Panel**", "Proposed; advisory only", "Invited by the Steering Board; personal capacity; 2-year terms", "Chair chosen by members; secretariat in the Director's office", "None; gives advice on methods, benchmarks and governance", "Annual note published", "Declarations of interest"],
                ["**Director**", "Proposed post; employee of the host institution", "Appointed by the host through open competition and confirmed by the Steering Board", "Not applicable", "Operational decisions within approved plans and budgets; may stop any pilot", "Monthly reports to the Board", "Host employment rules; declarations"],
                ["**Host-agency product owners**", "Officials designated in writing by their agencies", "Designated by the agency head", "Not applicable", "Define needs; accept or reject pilots at G3 and G4 in their agency", "Pilot reports", "Act under agency rules; receive no payment from BAPIL"],
                ["**Independent nominations panel**", "Proposed; convened once for each ERRC term", "Three people of standing in law, ethics and civil society, invited by the host institution's research ethics committee", "Members choose a convener", "Shortlists and recommends ERRC members", "Publishes the call and selection criteria", "Members may not serve on the ERRC they select"],
            ],
            "bn": [
                ["**স্টিয়ারিং বোর্ড**", "প্রস্তাবিত; সমঝোতা স্মারক ও আয়োজক-চুক্তির মাধ্যমে গঠিত; কোনো সংবিধিবদ্ধ ক্ষমতা নেই", "নিজ নিজ প্রতিষ্ঠানের মনোনীত ৭ থেকে ৯ জন সদস্য; একাডেমিক ও নাগরিক সমাজের সদস্য উন্মুক্ত আহ্বানে নির্বাচিত; মেয়াদ ৩ বছর", "আইসিটি বিভাগ ও আয়োজক প্রতিষ্ঠান থেকে যুগ্ম সভাপতি; পরিচালকের দপ্তরে সচিবালয়", "পরিকল্পনা, বাজেট, অংশীদারত্ব ও জ্যেষ্ঠ নিয়োগ অনুমোদন; সংস্থার সঙ্গে যৌথ G4 সিদ্ধান্ত; ERRC-এর প্রত্যাখ্যান বা আইন অগ্রাহ্য করতে পারে না", "ত্রৈমাসিক সভা; সিদ্ধান্ত ও কার্যবিবরণী সংক্ষেপে প্রকাশিত; বার্ষিক প্রতিবেদন", "বার্ষিক ঘোষণা; সংশ্লিষ্ট সিদ্ধান্ত থেকে বিরত থাকা; শিল্পখাতের সদস্য নিজ খাতের ক্রয়ে ভোট দেন না"],
                ["**নৈতিকতা ও ঝুঁকি পর্যালোচনা কমিটি (ERRC)**", "প্রস্তাবিত; সনদ দ্বারা গঠিত; সনদ ও আয়োজক-চুক্তির মাধ্যমে BAPIL-এর ভেতরে বাধ্যতামূলক, আইন দ্বারা নয়", "৫ থেকে ৭ জন সদস্য, অধিকাংশ বহিস্থ; স্বাধীন মনোনয়ন প্যানেলের উন্মুক্ত আহ্বানে নির্বাচিত ও স্টিয়ারিং বোর্ড কর্তৃক নিশ্চিত; মেয়াদ ৩ বছর, একবার নবায়নযোগ্য; শুনানির পর বোর্ডের দুই-তৃতীয়াংশের সিদ্ধান্তে কেবল যুক্তিসংগত কারণে অপসারণ", "সদস্যদের নির্বাচিত বহিস্থ সভাপতি; শাসন বিশ্লেষক সচিবালয়ের দায়িত্বে", "G1, G2 ও G4-এ T2 ও T3 স্তরের কাজ অনুমোদন, শর্তসাপেক্ষ অনুমোদন, প্রত্যাখ্যান বা স্থগিত; প্রত্যাখ্যান বাধ্যতামূলক; আইন বা আয়োজক যা নিষেধ করে তা অনুমোদন করতে পারে না", "৩০ দিনের মধ্যে সিদ্ধান্তের সারাংশ; ভিন্নমত লিপিবদ্ধ; বার্ষিক প্রতিবেদন", "অধিকাংশ বহিস্থ; মূল্যায়নাধীন সরবরাহকারীর কোনো কর্মী সদস্য নন; সুরক্ষিত বাজেট; কর্মীরা সরাসরি উদ্বেগ জানাতে পারেন"],
                ["**কারিগরি স্থাপত্য বোর্ড (TAB)**", "প্রস্তাবিত; পরিচালকের অধীন অভ্যন্তরীণ কারিগরি সংস্থা", "প্রধান প্রকৌশলীবৃন্দ, নিরাপত্তা প্রধান এবং বোর্ডের অনুমোদনে পরিচালক কর্তৃক নিযুক্ত দুজন বহিস্থ পর্যালোচক", "প্রধান প্রকৌশলী; প্ল্যাটফর্ম দলে সচিবালয়", "G1-এ নকশা, মডেল ও প্রধান নির্ভরতা অনুমোদন; ADR রক্ষণাবেক্ষণ", "রিপোজিটরিতে ADR উন্মুক্ত; মাসিক সভা", "বহিস্থ পর্যালোচকেরা বাণিজ্যিক স্বার্থ ঘোষণা করেন এবং নিজ নিয়োগকর্তার পণ্য পর্যালোচনা করেন না"],
                ["**আন্তর্জাতিক উপদেষ্টা প্যানেল**", "প্রস্তাবিত; শুধু পরামর্শমূলক", "স্টিয়ারিং বোর্ডের আমন্ত্রণে; ব্যক্তিগত সক্ষমতায়; মেয়াদ ২ বছর", "সদস্যদের বাছাই করা সভাপতি; পরিচালকের দপ্তরে সচিবালয়", "কোনো সিদ্ধান্ত-ক্ষমতা নেই; পদ্ধতি, বেঞ্চমার্ক ও শাসন বিষয়ে পরামর্শ দেয়", "বার্ষিক নোট প্রকাশিত", "স্বার্থ ঘোষণা"],
                ["**পরিচালক**", "প্রস্তাবিত পদ; আয়োজক প্রতিষ্ঠানের কর্মী", "উন্মুক্ত প্রতিযোগিতার মাধ্যমে আয়োজক কর্তৃক নিযুক্ত ও স্টিয়ারিং বোর্ড কর্তৃক নিশ্চিত", "প্রযোজ্য নয়", "অনুমোদিত পরিকল্পনা ও বাজেটের মধ্যে পরিচালনাগত সিদ্ধান্ত; যেকোনো পাইলট বন্ধ করতে পারেন", "বোর্ডের কাছে মাসিক প্রতিবেদন", "আয়োজকের চাকরিবিধি; ঘোষণা"],
                ["**আয়োজক সংস্থার প্রোডাক্ট ওনার**", "নিজ সংস্থা কর্তৃক লিখিতভাবে মনোনীত কর্মকর্তা", "সংস্থাপ্রধান কর্তৃক মনোনীত", "প্রযোজ্য নয়", "চাহিদা নির্ধারণ; নিজ সংস্থায় G3 ও G4-এ পাইলট গ্রহণ বা প্রত্যাখ্যান", "পাইলট প্রতিবেদন", "সংস্থার বিধি অনুযায়ী কাজ করেন; BAPIL থেকে কোনো পারিশ্রমিক নেন না"],
                ["**স্বাধীন মনোনয়ন প্যানেল**", "প্রস্তাবিত; প্রতিটি ERRC মেয়াদের জন্য একবার আহূত", "আইন, নৈতিকতা ও নাগরিক সমাজে স্বীকৃত তিনজন ব্যক্তি, আয়োজক প্রতিষ্ঠানের গবেষণা-নৈতিকতা কমিটির আমন্ত্রণে", "সদস্যরা একজন আহ্বায়ক বাছাই করেন", "ERRC সদস্যদের সংক্ষিপ্ত তালিকা ও সুপারিশ", "আহ্বান ও নির্বাচনের মানদণ্ড প্রকাশ", "সদস্যরা নিজেদের বাছাই করা ERRC-তে কাজ করতে পারেন না"],
            ],
        },
        "note": {"en": "None of these bodies exists yet. BAPIL's internal rules apply in addition to the law and never in place of it; where the law, a regulator or the host institution requires otherwise, the legal requirement prevails.",
                 "bn": "এসব সংস্থার কোনোটিই এখনো গঠিত হয়নি। BAPIL-এর অভ্যন্তরীণ নিয়ম আইনের পাশাপাশি প্রযোজ্য, কখনো আইনের বিকল্প নয়; আইন, কোনো নিয়ন্ত্রক বা আয়োজক প্রতিষ্ঠান ভিন্ন কিছু চাইলে আইনগত প্রয়োজনীয়তাই প্রাধান্য পাবে।"},
    },
    # ------------------------------------------------------------------ 65
    {
        "id": "65",
        "widths": [2.2, 1.9, 2.6, 1.5, 1.2],
        "title": {"en": "Preconditions and authorisations before and early in the 36-month plan",
                  "bn": "৩৬ মাসের পরিকল্পনার আগে ও শুরুতে প্রয়োজনীয় পূর্বশর্ত ও অনুমোদন"},
        "cols": {"en": ["Precondition", "Why it is needed", "Instrument or authority", "Status (October 2026)", "Needed by"],
                 "bn": ["পূর্বশর্ত", "কেন প্রয়োজন", "দলিল বা কর্তৃপক্ষ", "অবস্থা (অক্টোবর ২০২৬)", "কখন প্রয়োজন"]},
        "rows": {
            "en": [
                ["Host institution selected", "Legal home for staff, funds and data", "Open call (Section 5.2); resolution of the host's governing body", "Not started", "Before month 1"],
                ["MoU with the ICT Division", "Policy channel, data access and transfer route", "MoU signed under the ICT Division's own approval procedures (Decision D2)", "Requested; not decided", "Month 1 (starts the clock)"],
                ["Year 1 funding committed", "Salaries, equipment and studies", "Government budget allocation under the applicable project-approval procedures, a research grant or a development-partner agreement (foreign grants through the Economic Relations Division)", "No funding requested or approved", "Month 1"],
                ["Host agreement and separate cost centre", "Financial governance (Section 17.8)", "Host finance rules", "Not started", "Month 1"],
                ["Director appointed", "Single point of accountability", "Host recruitment rules; Steering Board confirmation", "Not started", "Month 3"],
                ["Steering Board and ERRC constituted; charter adopted", "Decision rights and safeguards", "Nominations (Decision D4); charter (Annex E)", "Draft charter only", "Month 3 (MS1)"],
                ["Reuse terms and bulk access for public documents", "P1 corpus", "Written confirmation from custodians (Decision D3); Right to Information requests as a fallback", "Not started", "Months 2 to 6"],
                ["Independent legal review", "Confirm which obligations apply and from when", "Counsel engaged by the host (Section 14.3)", "Not started", "Before MS2"],
                ["Hosting in Bangladesh", "Requirement NFR-02", "Agreement with the National Data Center or the host's data centre", "Not started", "Month 4"],
                ["Equipment procurement", "Pilot infrastructure", "Host's public procurement rules; confirmation of any duty and VAT exemption", "Not started", "Months 3 to 6"],
                ["Research ethics approval", "User studies, P3 and P6", "Host research ethics committee; ERRC", "Not started", "Before each study"],
                ["Data-sharing agreements for non-public data", "P3", "Agreement (Annex I); DPIA (Annex H); NRDEX where available", "Not started", "Month 12 onwards"],
                ["Division-of-labour note with the AI Hub project", "Avoid duplication", "Letter or MoU with the ICT Division and the Bangladesh Hi-Tech Park Authority", "Not started", "MS2"],
            ],
            "bn": [
                ["আয়োজক প্রতিষ্ঠান নির্বাচন", "জনবল, অর্থ ও ডেটার আইনগত আবাস", "উন্মুক্ত আহ্বান (অনুচ্ছেদ ৫.২); আয়োজকের পরিচালনা পর্ষদের সিদ্ধান্ত", "শুরু হয়নি", "মাস ১-এর আগে"],
                ["আইসিটি বিভাগের সঙ্গে সমঝোতা স্মারক", "নীতি-যোগাযোগ, ডেটা প্রবেশাধিকার ও হস্তান্তরের পথ", "আইসিটি বিভাগের নিজস্ব অনুমোদন-প্রক্রিয়ায় স্বাক্ষরিত সমঝোতা স্মারক (সিদ্ধান্ত D2)", "অনুরোধ করা হয়েছে; সিদ্ধান্ত হয়নি", "মাস ১ (সময়গণনা শুরু)"],
                ["প্রথম বছরের অর্থায়ন নিশ্চিত", "বেতন, যন্ত্রপাতি ও সমীক্ষা", "প্রযোজ্য প্রকল্প-অনুমোদন প্রক্রিয়ায় সরকারি বাজেট বরাদ্দ, গবেষণা অনুদান বা উন্নয়ন সহযোগীর চুক্তি (বিদেশি অনুদান অর্থনৈতিক সম্পর্ক বিভাগের মাধ্যমে)", "কোনো অর্থ চাওয়া বা অনুমোদিত হয়নি", "মাস ১"],
                ["আয়োজক-চুক্তি ও পৃথক ব্যয়কেন্দ্র", "আর্থিক শাসন (অনুচ্ছেদ ১৭.৮)", "আয়োজকের আর্থিক বিধি", "শুরু হয়নি", "মাস ১"],
                ["পরিচালক নিয়োগ", "জবাবদিহির একক কেন্দ্র", "আয়োজকের নিয়োগবিধি; স্টিয়ারিং বোর্ডের নিশ্চিতকরণ", "শুরু হয়নি", "মাস ৩"],
                ["স্টিয়ারিং বোর্ড ও ERRC গঠন; সনদ গ্রহণ", "সিদ্ধান্তের অধিকার ও সুরক্ষাব্যবস্থা", "মনোনয়ন (সিদ্ধান্ত D4); সনদ (সংযুক্তি ঙ)", "শুধু খসড়া সনদ", "মাস ৩ (MS1)"],
                ["উন্মুক্ত নথির পুনর্ব্যবহারের শর্ত ও একসঙ্গে প্রবেশাধিকার", "P1 কর্পাস", "ডেটা-রক্ষকদের লিখিত নিশ্চয়তা (সিদ্ধান্ত D3); বিকল্প হিসেবে তথ্য অধিকার আবেদন", "শুরু হয়নি", "মাস ২ থেকে ৬"],
                ["স্বাধীন আইনি পর্যালোচনা", "কোন দায়িত্ব কবে থেকে প্রযোজ্য তা নিশ্চিত করা", "আয়োজক কর্তৃক নিযুক্ত আইনজীবী (অনুচ্ছেদ ১৪.৩)", "শুরু হয়নি", "MS2-এর আগে"],
                ["বাংলাদেশে হোস্টিং", "প্রয়োজনীয়তা NFR-02", "জাতীয় ডেটা সেন্টার বা আয়োজকের ডেটা সেন্টারের সঙ্গে চুক্তি", "শুরু হয়নি", "মাস ৪"],
                ["যন্ত্রপাতি ক্রয়", "পাইলট অবকাঠামো", "আয়োজকের সরকারি ক্রয়বিধি; শুল্ক ও ভ্যাট অব্যাহতি থাকলে তার নিশ্চিতকরণ", "শুরু হয়নি", "মাস ৩ থেকে ৬"],
                ["গবেষণা-নৈতিকতার অনুমোদন", "ব্যবহারকারী-সমীক্ষা, P3 ও P6", "আয়োজকের গবেষণা-নৈতিকতা কমিটি; ERRC", "শুরু হয়নি", "প্রতিটি সমীক্ষার আগে"],
                ["অ-উন্মুক্ত ডেটার জন্য ডেটা-বিনিময় চুক্তি", "P3", "চুক্তি (সংযুক্তি ঝ); DPIA (সংযুক্তি জ); সম্ভব হলে NRDEX", "শুরু হয়নি", "মাস ১২ থেকে"],
                ["এআই হাব প্রকল্পের সঙ্গে কর্মবিভাজন-নোট", "দ্বৈততা এড়ানো", "আইসিটি বিভাগ ও বাংলাদেশ হাই-টেক পার্ক কর্তৃপক্ষের সঙ্গে পত্র বা সমঝোতা স্মারক", "শুরু হয়নি", "MS2"],
            ],
        },
        "note": {"en": "Month 1 of the plan is the first month in which the MoU, the host agreement and Year 1 funding are all in place. January 2027 is the earliest plausible start if decisions D1, D2 and D4 are taken in the fourth quarter of 2026.",
                 "bn": "পরিকল্পনার মাস ১ হলো প্রথম সেই মাস, যখন সমঝোতা স্মারক, আয়োজক-চুক্তি ও প্রথম বছরের অর্থায়ন তিনটিই নিশ্চিত। ২০২৬-এর চতুর্থ ত্রৈমাসিকে সিদ্ধান্ত D1, D2 ও D4 গৃহীত হলে জানুয়ারি ২০২৭ সবচেয়ে আগের সম্ভাব্য সূচনা।"},
    },
    # ------------------------------------------------------------------ 66
    {
        "id": "66",
        "widths": [1.5, 2.0, 2.0, 2.3, 1.4, 1.1, 1.8],
        "title": {"en": "Work packages: owners, preconditions, acceptance tests and gates",
                  "bn": "কাজের প্যাকেজ: দায়িত্বপ্রাপ্ত, পূর্বশর্ত, গ্রহণ-পরীক্ষা ও গেট"},
        "cols": {"en": ["Work package", "Objective and accountable owner", "Preconditions and dependencies", "Deliverables and acceptance test", "Budget line (Table 50)", "Main risks (Table 55)", "Gate and exit criterion"],
                 "bn": ["কাজের প্যাকেজ", "উদ্দেশ্য ও দায়িত্বপ্রাপ্ত", "পূর্বশর্ত ও নির্ভরতা", "ডেলিভারেবল ও গ্রহণ-পরীক্ষা", "বাজেট-খাত (সারণি ৫০)", "প্রধান ঝুঁকি (সারণি ৫৫)", "গেট ও প্রস্থানের মানদণ্ড"]},
        "rows": {
            "en": [
                ["1. Institution, charter and governance", "Constitute governance and adopt the charter; Director", "First six rows of Table 65", "Charter, terms of reference, register and policies; accepted when adopted by the Board and published", "Core staff; governance", "R1, R8, R16", "MS1; exit when all bodies meet as designed"],
                ["2. Data access and corpus", "Governed public corpus; data lead", "Decision D3; hosting", "Corpus releases with quality reports; accepted when Table 25 targets are met", "Data and annotation; compute", "R2, R3, R13", "MS2 and MS4; 5,000 documents with provenance by month 12"],
                ["3. P1 Policy Search", "Cited search pilot; P1 lead with an agency product owner", "Corpus from work package 2; benchmark v0; ERRC review (T2)", "Alpha and pilot report; accepted when Table 28 thresholds are met under Table 63 and 30 users are active", "Core staff; compute", "R4, R11, R12", "G2 at month 9, G3 at month 12, G4 at month 24"],
                ["4. P2 Budget dashboard", "Open budget dataset; P2 lead with a Finance Division product owner", "Published budget documents", "Dataset with DOI and dashboard; accepted at 99% accuracy on a 1,000-cell sample", "Core staff; data", "R2, R3", "G3 at month 12; G4 at month 24"],
                ["5. P3 Feedback analyser", "Aggregate analysis of one consultation; P3 lead with the consultation owner", "DPIA approved; consent wording approved by the ERRC", "Analysis report; accepted when topics are validated by people with no re-identification", "Core staff; governance", "R5, R6", "G2 and G3 at month 15; stop if the DPIA is not approved"],
                ["6. P4 Bangla foundation model", "Benchmark and evidence-based model decision; ML lead", "Corpus; annotators; compute for Stage 1", "Benchmark v0 and v1; Stage 1 decision memo; accepted under Table 30", "Data and annotation; compute", "R15, R17", "MS3, MS6 and MS8"],
                ["7. P5 Readiness observatory", "Indicator framework and annual report; policy lead", "Public indicators", "Framework and first report; accepted after peer review by the advisory panel and publication with data", "Core staff", "R9", "MS5 and MS7"],
                ["8. P6 Information integrity", "Methods review; research lead", "ERRC approval of the research protocol", "Methods paper; accepted when the approved protocol was followed", "Core staff; governance", "R6, R14", "Stop if the protocol is not approved"],
                ["9. Training and capacity", "500 officials trained; training lead", "Tools available; host facilities", "Programmes T1 to T6; accepted when pre- and post-tests show learning gains and 40% of trainees are women", "Training and outreach", "R7, R12", "MS4, MS7 and MS9"],
                ["10. Independent evaluation", "Credible evidence for decisions; commissioned by the Steering Board", "Funding; terms of reference", "Baseline, mid-term and final evaluations; accepted when published with a DOI", "Governance, audit and evaluation", "R1, R8", "MS6 and MS9"],
            ],
            "bn": [
                ["১. প্রতিষ্ঠান, সনদ ও শাসন", "শাসন-কাঠামো গঠন ও সনদ গ্রহণ; পরিচালক", "সারণি ৬৫-এর প্রথম ছয়টি সারি", "সনদ, কার্যপরিধি, নিবন্ধন ও নীতিমালা; বোর্ড কর্তৃক গৃহীত ও প্রকাশিত হলে গ্রহণযোগ্য", "মূল জনবল; শাসন", "R1, R8, R16", "MS1; সব সংস্থা নকশামতো সভা করলে প্রস্থান"],
                ["২. ডেটা প্রবেশাধিকার ও কর্পাস", "নিয়ন্ত্রিত উন্মুক্ত কর্পাস; ডেটা প্রধান", "সিদ্ধান্ত D3; হোস্টিং", "মান-প্রতিবেদনসহ কর্পাস রিলিজ; সারণি ২৫-এর লক্ষ্য অর্জিত হলে গ্রহণযোগ্য", "ডেটা ও টীকাকরণ; কম্পিউটিং", "R2, R3, R13", "MS2 ও MS4; মাস ১২-এর মধ্যে উৎস-তথ্যসহ ৫,০০০ নথি"],
                ["৩. P1 নীতি অনুসন্ধান", "উদ্ধৃতিযুক্ত অনুসন্ধানের পাইলট; সংস্থার প্রোডাক্ট ওনারের সঙ্গে P1 প্রধান", "কাজের প্যাকেজ ২-এর কর্পাস; বেঞ্চমার্ক v0; ERRC পর্যালোচনা (T2)", "আলফা ও পাইলট প্রতিবেদন; সারণি ৬৩ অনুযায়ী সারণি ২৮-এর সীমা অর্জিত এবং ৩০ জন সক্রিয় ব্যবহারকারী হলে গ্রহণযোগ্য", "মূল জনবল; কম্পিউটিং", "R4, R11, R12", "মাস ৯-এ G2, মাস ১২-এ G3, মাস ২৪-এ G4"],
                ["৪. P2 বাজেট ড্যাশবোর্ড", "উন্মুক্ত বাজেট ডেটাসেট; অর্থ বিভাগের প্রোডাক্ট ওনারের সঙ্গে P2 প্রধান", "প্রকাশিত বাজেট নথি", "DOI-সহ ডেটাসেট ও ড্যাশবোর্ড; ১,০০০ ঘরের নমুনায় ৯৯% নির্ভুলতায় গ্রহণযোগ্য", "মূল জনবল; ডেটা", "R2, R3", "মাস ১২-এ G3; মাস ২৪-এ G4"],
                ["৫. P3 মতামত বিশ্লেষক", "একটি পরামর্শ-প্রক্রিয়ার সমষ্টিগত বিশ্লেষণ; পরামর্শের মালিকের সঙ্গে P3 প্রধান", "DPIA অনুমোদিত; সম্মতির ভাষা ERRC কর্তৃক অনুমোদিত", "বিশ্লেষণ প্রতিবেদন; মানুষের দ্বারা বিষয় যাচাই এবং পুনঃশনাক্তকরণ না হলে গ্রহণযোগ্য", "মূল জনবল; শাসন", "R5, R6", "মাস ১৫-এ G2 ও G3; DPIA অনুমোদিত না হলে বন্ধ"],
                ["৬. P4 বাংলা ফাউন্ডেশন মডেল", "বেঞ্চমার্ক ও প্রমাণভিত্তিক মডেল-সিদ্ধান্ত; ML প্রধান", "কর্পাস; টীকাকার; পর্যায় ১-এর জন্য কম্পিউটিং", "বেঞ্চমার্ক v0 ও v1; পর্যায় ১-এর সিদ্ধান্ত-স্মারক; সারণি ৩০ অনুযায়ী গ্রহণযোগ্য", "ডেটা ও টীকাকরণ; কম্পিউটিং", "R15, R17", "MS3, MS6 ও MS8"],
                ["৭. P5 প্রস্তুতি পর্যবেক্ষণকেন্দ্র", "সূচক-কাঠামো ও বার্ষিক প্রতিবেদন; নীতি প্রধান", "উন্মুক্ত সূচক", "কাঠামো ও প্রথম প্রতিবেদন; উপদেষ্টা প্যানেলের পর্যালোচনা ও ডেটাসহ প্রকাশের পর গ্রহণযোগ্য", "মূল জনবল", "R9", "MS5 ও MS7"],
                ["৮. P6 তথ্য-অখণ্ডতা", "পদ্ধতি-পর্যালোচনা; গবেষণা প্রধান", "গবেষণা-প্রটোকলের ERRC অনুমোদন", "পদ্ধতি-প্রবন্ধ; অনুমোদিত প্রটোকল অনুসৃত হলে গ্রহণযোগ্য", "মূল জনবল; শাসন", "R6, R14", "প্রটোকল অনুমোদিত না হলে বন্ধ"],
                ["৯. প্রশিক্ষণ ও সক্ষমতা", "৫০০ কর্মকর্তা প্রশিক্ষিত; প্রশিক্ষণ প্রধান", "সরঞ্জাম প্রস্তুত; আয়োজকের সুবিধা", "কর্মসূচি T1 থেকে T6; পূর্ব ও পরবর্তী পরীক্ষায় শিখনের অগ্রগতি এবং ৪০% নারী প্রশিক্ষণার্থী হলে গ্রহণযোগ্য", "প্রশিক্ষণ ও সম্প্রসারণ", "R7, R12", "MS4, MS7 ও MS9"],
                ["১০. স্বাধীন মূল্যায়ন", "সিদ্ধান্তের জন্য বিশ্বাসযোগ্য প্রমাণ; স্টিয়ারিং বোর্ড কর্তৃক নিযুক্ত", "অর্থায়ন; কার্যপরিধি", "ভিত্তি, মধ্যমেয়াদি ও চূড়ান্ত মূল্যায়ন; DOI-সহ প্রকাশিত হলে গ্রহণযোগ্য", "শাসন, নিরীক্ষা ও মূল্যায়ন", "R1, R8", "MS6 ও MS9"],
            ],
        },
        "note": {"en": "Work packages correspond to the rows of Figure 12. Outputs, outcomes and impacts are separated in the logical framework (Table 53).",
                 "bn": "কাজের প্যাকেজগুলো চিত্র ১২-এর সারির সঙ্গে সংগতিপূর্ণ। লজিক্যাল ফ্রেমওয়ার্কে (সারণি ৫৩) উৎপাদ, ফলাফল ও প্রভাব আলাদা করা হয়েছে।"},
    },
    # ------------------------------------------------------------------ 67
    {
        "id": "67",
        "widths": [0.6, 3.0, 2.8, 1.2, 1.6],
        "title": {"en": "Risk monitoring: early-warning indicators, contingencies and residual ratings",
                  "bn": "ঝুঁকি পর্যবেক্ষণ: আগাম সতর্কসংকেত, বিকল্প ব্যবস্থা ও অবশিষ্ট মাত্রা"},
        "cols": {"en": ["ID", "Early-warning indicator", "Contingency if the risk occurs", "Residual (L/I)", "Review frequency"],
                 "bn": ["আইডি", "আগাম সতর্কসংকেত", "ঝুঁকি ঘটলে বিকল্প ব্যবস্থা", "অবশিষ্ট (স/প্র)", "পর্যালোচনার পুনরাবৃত্তি"]},
        "rows": {
            "en": [
                ["R1", "No government focal point named within 90 days of the request; change of senior sponsors", "Continue as a university research lab on public data; seek another sponsor", "M/M", "Quarterly"],
                ["R2", "No reply from a custodian within 60 days; bulk access refused", "Use documents already online; Right to Information requests; narrow the corpus", "M/M", "Monthly in Year 1"],
                ["R3", "OCR quality score below 0.9 on more than 20% of pages", "Increase manual correction; prioritise born-digital sources", "M/L", "Each corpus release"],
                ["R4", "Citation precision below 0.95; reports of wrong answers", "Fall back to search-only mode; retrain users", "L/H", "Each release; monthly in pilots"],
                ["R5", "Any P2 data found in logs; access anomalies", "Suspend P3; notify as the law requires; ERRC review", "L/H", "Monthly"],
                ["R6", "Requests to monitor individuals; scope changes touching tier T0", "ERRC refusal; publish the decision", "L/H", "At each gate"],
                ["R7", "Posts vacant for more than 3 months; more than 30% of offers refused", "Use fellows and contractors; remote staff", "M/M", "Quarterly"],
                ["R8", "No Phase 2 funding commitment by month 18", "Scale down to the core: corpus, benchmark and governance", "M/H", "Quarterly"],
                ["R9", "Overlapping activities in AI Hub project plans", "Joint work plan; divide work by function", "L/M", "Every six months"],
                ["R10", "A single vendor or model in more than one component without an exit plan", "Re-tender; switch model on the benchmark", "L/M", "At each ADR"],
                ["R11", "Critical penetration-test findings; intrusion alerts", "Isolate; restore from offline backup", "L/H", "Quarterly tests; continuous monitoring"],
                ["R12", "Monthly active users below half of target for two months", "Co-design sprint; reconsider the pilot", "M/M", "Monthly"],
                ["R13", "New rules issued; findings of the legal review", "Update procedures; pause affected processing", "L/M", "When rules are issued; quarterly"],
                ["R14", "Misuse reports; unusual aggregate query patterns", "Restrict access; ERRC review", "L/H", "Monthly"],
                ["R15", "Gap of more than 5 points between development and test results; signs of test leakage", "Refresh the test split", "L/M", "Each benchmark version"],
                ["R16", "Critical knowledge held by one person with no deputy", "Activate the succession plan", "M/M", "Quarterly"],
                ["R17", "Re-selection shows the chosen model more than 5 points behind an alternative", "Re-select through an ADR", "L/M", "Annually"],
                ["R18", "Flood or cyclone warnings; frequent power outages", "Switch to the recovery site; offline operation", "M/M", "Before each monsoon and after drills"],
            ],
            "bn": [
                ["R1", "অনুরোধের ৯০ দিনের মধ্যে কোনো সরকারি ফোকাল পয়েন্ট মনোনীত না হওয়া; জ্যেষ্ঠ পৃষ্ঠপোষকের পরিবর্তন", "উন্মুক্ত ডেটা নিয়ে বিশ্ববিদ্যালয়ের গবেষণা ল্যাব হিসেবে চালিয়ে যাওয়া; অন্য পৃষ্ঠপোষক খোঁজা", "মা/মা", "ত্রৈমাসিক"],
                ["R2", "৬০ দিনের মধ্যে ডেটা-রক্ষকের সাড়া না পাওয়া; একসঙ্গে প্রবেশাধিকার প্রত্যাখ্যাত", "ইতিমধ্যে অনলাইনে থাকা নথি ব্যবহার; তথ্য অধিকার আবেদন; কর্পাস সীমিত করা", "মা/মা", "প্রথম বছরে মাসিক"],
                ["R3", "২০%-এর বেশি পৃষ্ঠায় OCR মান-স্কোর ০.৯-এর নিচে", "হাতে সংশোধন বাড়ানো; ডিজিটালভাবে তৈরি উৎসকে অগ্রাধিকার", "মা/নি", "প্রতিটি কর্পাস রিলিজে"],
                ["R4", "উদ্ধৃতির নির্ভুলতা ০.৯৫-এর নিচে; ভুল উত্তরের প্রতিবেদন", "শুধু অনুসন্ধান-মোডে ফেরা; ব্যবহারকারীদের পুনঃপ্রশিক্ষণ", "নি/উ", "প্রতিটি রিলিজে; পাইলটে মাসিক"],
                ["R5", "লগে কোনো P2 ডেটা পাওয়া; প্রবেশাধিকারে অস্বাভাবিকতা", "P3 স্থগিত; আইন অনুযায়ী অবহিতকরণ; ERRC পর্যালোচনা", "নি/উ", "মাসিক"],
                ["R6", "ব্যক্তি-নজরদারির অনুরোধ; T0 স্তর-সংশ্লিষ্ট পরিধি-পরিবর্তন", "ERRC-এর প্রত্যাখ্যান; সিদ্ধান্ত প্রকাশ", "নি/উ", "প্রতিটি গেটে"],
                ["R7", "৩ মাসের বেশি পদ শূন্য; ৩০%-এর বেশি নিয়োগপ্রস্তাব প্রত্যাখ্যাত", "ফেলো ও চুক্তিভিত্তিক কর্মী; দূরবর্তী কর্মী", "মা/মা", "ত্রৈমাসিক"],
                ["R8", "মাস ১৮-এর মধ্যে দ্বিতীয় ধাপের অর্থায়ন-প্রতিশ্রুতি নেই", "মূল কাজে সংকুচিত করা: কর্পাস, বেঞ্চমার্ক ও শাসন", "মা/উ", "ত্রৈমাসিক"],
                ["R9", "এআই হাব প্রকল্পের পরিকল্পনায় সাংঘর্ষিক কার্যক্রম", "যৌথ কর্মপরিকল্পনা; কাজের ধরন অনুযায়ী বিভাজন", "নি/মা", "প্রতি ছয় মাসে"],
                ["R10", "বিকল্প-পরিকল্পনা ছাড়া একাধিক উপাদানে একক বিক্রেতা বা মডেল", "পুনঃদরপত্র; বেঞ্চমার্কের ভিত্তিতে মডেল বদল", "নি/মা", "প্রতিটি ADR-এ"],
                ["R11", "অনুপ্রবেশ পরীক্ষায় গুরুতর ত্রুটি; অনুপ্রবেশের সতর্কসংকেত", "বিচ্ছিন্ন করা; অফলাইন ব্যাকআপ থেকে পুনরুদ্ধার", "নি/উ", "ত্রৈমাসিক পরীক্ষা; নিরবচ্ছিন্ন পর্যবেক্ষণ"],
                ["R12", "টানা দুই মাস মাসিক সক্রিয় ব্যবহারকারী লক্ষ্যের অর্ধেকের নিচে", "সহ-নকশা স্প্রিন্ট; পাইলট পুনর্বিবেচনা", "মা/মা", "মাসিক"],
                ["R13", "নতুন বিধিমালা জারি; আইনি পর্যালোচনার ফলাফল", "প্রক্রিয়া হালনাগাদ; প্রভাবিত প্রক্রিয়াকরণ স্থগিত", "নি/মা", "বিধিমালা জারির সময়; ত্রৈমাসিক"],
                ["R14", "অপব্যবহারের প্রতিবেদন; সমষ্টিগত প্রশ্নধারায় অস্বাভাবিকতা", "প্রবেশাধিকার সীমিত; ERRC পর্যালোচনা", "নি/উ", "মাসিক"],
                ["R15", "উন্নয়ন ও পরীক্ষার ফলাফলে ৫ পয়েন্টের বেশি ব্যবধান; পরীক্ষা-প্রশ্ন ফাঁসের লক্ষণ", "পরীক্ষা-অংশ নবায়ন", "নি/মা", "প্রতিটি বেঞ্চমার্ক সংস্করণে"],
                ["R16", "গুরুত্বপূর্ণ জ্ঞান একজনের কাছে, কোনো সহকারী নেই", "উত্তরাধিকার-পরিকল্পনা চালু", "মা/মা", "ত্রৈমাসিক"],
                ["R17", "পুনর্নির্বাচনে দেখা যায় নির্বাচিত মডেল বিকল্পের চেয়ে ৫ পয়েন্টের বেশি পিছিয়ে", "ADR-এর মাধ্যমে পুনর্নির্বাচন", "নি/মা", "বার্ষিক"],
                ["R18", "বন্যা বা ঘূর্ণিঝড়ের সতর্কতা; ঘন ঘন বিদ্যুৎ-বিভ্রাট", "পুনরুদ্ধার-সাইটে স্থানান্তর; অফলাইন পরিচালনা", "মা/মা", "প্রতি বর্ষার আগে ও মহড়ার পরে"],
            ],
        },
        "note": {"en": "Residual ratings are likelihood and impact after the mitigations in Table 55: L = low, M = medium, H = high. Owners are those named in Table 55.",
                 "bn": "অবশিষ্ট মাত্রা হলো সারণি ৫৫-এর প্রশমনের পর সম্ভাবনা ও প্রভাব: নি = নিম্ন, মা = মাঝারি, উ = উচ্চ। দায়িত্বপ্রাপ্তরা সারণি ৫৫-এ উল্লিখিত।"},
    },
    # ------------------------------------------------------------------ 68
    {
        "id": "68",
        "widths": [1.6, 3.6, 2.6, 1.8],
        "title": {"en": "Revision history: changes made after the October 2026 audit",
                  "bn": "সংশোধনের ইতিহাস: অক্টোবর ২০২৬-এর নিরীক্ষার পর করা পরিবর্তন"},
        "cols": {"en": ["Where", "Change", "Reason", "Evidence or calculation"],
                 "bn": ["কোথায়", "পরিবর্তন", "কারণ", "প্রমাণ বা হিসাব"]},
        "rows": {
            "en": [
                ["Front matter", "Status table; disclaimer and Overview revised; budget added to the Overview; counts updated", "Separate what exists from what is proposed", "Repository check, 22 October 2026; Annex P"],
                ["Ch. 1", "Legal timing qualified; method step 6 (audit); implementation described as a research prototype", "Avoid overstating legal and software status", "[84, 85, 86, 113]"],
                ["Ch. 2; Table 4", "Primary sources for EGDI and GCI; corrected citation for the 2023 AI readiness rank; legal summary rewritten", "Accuracy and source quality", "[80, 119, 120]"],
                ["Ch. 3", "AI Hub described as a proposal with a signed grant agreement, not a project under implementation", "Source shows a proposal awaiting approval", "[35, 117]"],
                ["Ch. 5; Annexes E to G", "Legal status of bodies; independent selection of ERRC members; removal for cause; precedence of law (Article 13); charter confirmed after legal review", "Independence and legal accuracy", "Annex S"],
                ["Ch. 8, 10", "Chief data officers, NRDEX and the source-code repository attributed to the instruments that describe them; residency amendment; stricter-reading rule; GPU capacity matched to the budget", "Correct attribution; internal consistency", "[84, 113, 115]; Table 49"],
                ["Ch. 9; Tables 28, 30", "Benchmark composition, splits and statistical rationale; decision rule; refined metric definitions; five-step model ladder with feasibility estimates", "Make targets measurable; avoid assuming a new model is needed", "Wilson intervals; [121]"],
                ["Ch. 11; SECURITY.md", "Maturity terms defined; CI described as configured; security and dependency practice", "Distinguish prototype from production", "Repository"],
                ["Ch. 12, 13", "P1 exit tied to the protocol; complaints and appeals; labelling presented as BAPIL's rule", "Measurability; accountability; correct attribution", "[89]; Annex R"],
                ["Ch. 14; Tables 41 to 43", "Chronology of ordinances and Acts; enactment separated from commencement; legal review scope; new Section 14.7", "Legal statements rest on secondary sources", "[84 to 89, 106, 113 to 116]"],
                ["Ch. 15; Tables 44, 48", "Month 1 defined by MoU, host agreement and funding; MS1 and first 90 days aligned; calendar caveat", "Implementation realism", "Annex T"],
                ["Ch. 17; Tables 49, 50", "Budget revised from Tk 18.49 to 20.43 crore: escalation, recruitment ramp, separate contingency, evaluation items; scenarios and sensitivity; rounding explained", "Financial transparency", "budget_model.py; [118]; Table 61"],
                ["Ch. 18, 19; Tables 16, 18, 25, 54", "KPIs labelled as targets; time saved measured, not self-reported; training counts reconciled with the budget; OCR sampling; link to risk monitoring", "Consistency between plan, budget and measurement", "Annex R; Table 49"],
                ["Ch. 21; Table 57", "Conclusion reworded; Decision D4 revised; note that no decision creates a statutory body", "Overclaim; independence", "Annex S"],
                ["Annexes P to V", "Evidence status; budget reconciliation and scenarios; evaluation protocol; governance status; preconditions and work packages; risk monitoring; this revision history and unresolved items", "Review mandate", "As listed in each annex"],
                ["References", "References 113 to 121 added", "New evidence", "As listed"],
                ["Bangla edition", "All revisions translated; Bangla numerals for lists, citations, page numbers and chart labels", "Bilingual consistency; editorial quality", "Automated comparison of numbers by section"],
            ],
            "bn": [
                ["সূচনা-অংশ", "অবস্থা-সারণি; দায়স্বীকার ও এক নজরে অংশ সংশোধিত; এক নজরে অংশে বাজেট যুক্ত; সংখ্যা হালনাগাদ", "যা বিদ্যমান আর যা প্রস্তাবিত তা আলাদা করা", "রিপোজিটরি যাচাই, ২২ অক্টোবর ২০২৬; সংযুক্তি ত"],
                ["অধ্যায় ১", "আইনের সময়রেখা শর্তযুক্ত; পদ্ধতির ধাপ ৬ (নিরীক্ষা); বাস্তবায়নকে গবেষণা-প্রোটোটাইপ হিসেবে বর্ণনা", "আইনগত ও সফটওয়্যারের অবস্থা অতিরঞ্জন এড়ানো", "[84, 85, 86, 113]"],
                ["অধ্যায় ২; সারণি ৪", "EGDI ও GCI-এর প্রাথমিক উৎস; ২০২৩ সালের এআই প্রস্তুতি-র‍্যাংকের তথ্যসূত্র সংশোধন; আইনগত সারাংশ পুনর্লিখন", "নির্ভুলতা ও উৎসের মান", "[80, 119, 120]"],
                ["অধ্যায় ৩", "এআই হাবকে বাস্তবায়নাধীন প্রকল্প নয়, স্বাক্ষরিত অনুদান-চুক্তিসহ একটি প্রস্তাব হিসেবে বর্ণনা", "উৎসে অনুমোদনের অপেক্ষায় থাকা প্রস্তাবের কথা", "[35, 117]"],
                ["অধ্যায় ৫; সংযুক্তি ঙ থেকে ছ", "সংস্থাগুলোর আইনগত অবস্থান; ERRC সদস্যদের স্বাধীন বাছাই; কেবল যুক্তিসংগত কারণে অপসারণ; আইনের প্রাধান্য (ধারা ১৩); আইনি পর্যালোচনার পর সনদ নিশ্চিতকরণ", "স্বাধীনতা ও আইনগত নির্ভুলতা", "সংযুক্তি ধ"],
                ["অধ্যায় ৮, ১০", "প্রধান ডেটা কর্মকর্তা, NRDEX ও সোর্স কোড ভান্ডার যে দলিলে বর্ণিত তার নামে উল্লিখিত; ডেটা দেশে রাখার সংশোধনী; কঠোরতর ব্যাখ্যার নিয়ম; GPU-সক্ষমতা বাজেটের সঙ্গে সংগতিপূর্ণ", "সঠিক উৎস-নির্দেশ; অভ্যন্তরীণ সংগতি", "[84, 113, 115]; সারণি ৪৯"],
                ["অধ্যায় ৯; সারণি ২৮, ৩০", "বেঞ্চমার্কের গঠন, বিভাজন ও পরিসংখ্যানগত যুক্তি; সিদ্ধান্ত-নিয়ম; মাপকাঠির সংজ্ঞা পরিমার্জন; সম্ভাব্যতা-প্রাক্কলনসহ পাঁচ ধাপের মডেল-ধাপক্রম", "লক্ষ্য পরিমাপযোগ্য করা; নতুন মডেল প্রয়োজন বলে ধরে না নেওয়া", "উইলসন ব্যবধান; [121]"],
                ["অধ্যায় ১১; SECURITY.md", "পরিপক্বতার পরিভাষা সংজ্ঞায়িত; CI নির্ধারিত বলে বর্ণিত; নিরাপত্তা ও নির্ভরতা-চর্চা", "প্রোটোটাইপ ও উৎপাদন-ব্যবস্থা আলাদা করা", "রিপোজিটরি"],
                ["অধ্যায় ১২, ১৩", "P1-এর উত্তরণ প্রটোকলের সঙ্গে যুক্ত; অভিযোগ ও আপিল; লেবেলকে BAPIL-এর নিয়ম হিসেবে উপস্থাপন", "পরিমাপযোগ্যতা; জবাবদিহি; সঠিক উৎস-নির্দেশ", "[89]; সংযুক্তি দ"],
                ["অধ্যায় ১৪; সারণি ৪১ থেকে ৪৩", "অধ্যাদেশ ও আইনের সময়ক্রম; প্রণয়ন ও কার্যকারিতা আলাদা; আইনি পর্যালোচনার পরিধি; নতুন অনুচ্ছেদ ১৪.৭", "আইনগত বক্তব্য মাধ্যমিক উৎসনির্ভর", "[84 থেকে 89, 106, 113 থেকে 116]"],
                ["অধ্যায় ১৫; সারণি ৪৪, ৪৮", "সমঝোতা স্মারক, আয়োজক-চুক্তি ও অর্থায়ন দিয়ে মাস ১ সংজ্ঞায়িত; MS1 ও প্রথম ৯০ দিন সংগতিপূর্ণ; ক্যালেন্ডার-সতর্কতা", "বাস্তবায়নের বাস্তবতা", "সংযুক্তি ন"],
                ["অধ্যায় ১৭; সারণি ৪৯, ৫০", "বাজেট ১৮.৪৯ থেকে ২০.৪৩ কোটি টাকায় সংশোধিত: মূল্যবৃদ্ধি, ধাপে ধাপে নিয়োগ, পৃথক আপৎকালীন সংস্থান, মূল্যায়নের উপাদান; পরিস্থিতি ও সংবেদনশীলতা; আসন্নীকরণের ব্যাখ্যা", "আর্থিক স্বচ্ছতা", "budget_model.py; [118]; সারণি ৬১"],
                ["অধ্যায় ১৮, ১৯; সারণি ১৬, ১৮, ২৫, ৫৪", "KPI লক্ষ্য হিসেবে চিহ্নিত; সাশ্রয়কৃত সময় স্ব-প্রতিবেদন নয়, পরিমাপকৃত; প্রশিক্ষণের সংখ্যা বাজেটের সঙ্গে মেলানো; OCR নমুনা; ঝুঁকি পর্যবেক্ষণের সংযোগ", "পরিকল্পনা, বাজেট ও পরিমাপের সংগতি", "সংযুক্তি দ; সারণি ৪৯"],
                ["অধ্যায় ২১; সারণি ৫৭", "উপসংহার পুনর্লিখিত; সিদ্ধান্ত D4 সংশোধিত; কোনো সিদ্ধান্ত সংবিধিবদ্ধ সংস্থা সৃষ্টি করে না বলে টীকা", "অতিরঞ্জন; স্বাধীনতা", "সংযুক্তি ধ"],
                ["সংযুক্তি ত থেকে ফ", "প্রমাণগত অবস্থা; বাজেটের মিলকরণ ও পরিস্থিতি; মূল্যায়ন প্রটোকল; শাসন-অবস্থা; পূর্বশর্ত ও কাজের প্যাকেজ; ঝুঁকি পর্যবেক্ষণ; এই সংশোধনের ইতিহাস ও অমীমাংসিত বিষয়", "পর্যালোচনার নির্দেশনা", "প্রতিটি সংযুক্তিতে উল্লিখিত"],
                ["তথ্যসূত্র", "তথ্যসূত্র ১১৩ থেকে ১২১ যুক্ত", "নতুন প্রমাণ", "তালিকা অনুযায়ী"],
                ["বাংলা সংস্করণ", "সব সংশোধন অনূদিত; তালিকা, উদ্ধৃতি, পৃষ্ঠা-নম্বর ও চার্টের লেবেলে বাংলা সংখ্যা", "দ্বিভাষিক সংগতি; সম্পাদকীয় মান", "অংশভিত্তিক সংখ্যার স্বয়ংক্রিয় তুলনা"],
            ],
        },
        "note": {"en": "The full issue register, claim verification matrix and scores are in the separate Audit and Revision Report in the repository (blueprint/review/).",
                 "bn": "পূর্ণ সমস্যা-নিবন্ধন, দাবি-যাচাই ম্যাট্রিক্স ও স্কোর রিপোজিটরির পৃথক নিরীক্ষা ও সংশোধন প্রতিবেদনে (blueprint/review/) আছে।"},
    },
    # ------------------------------------------------------------------ 69
    {
        "id": "69",
        "widths": [0.6, 2.6, 2.2, 1.6, 2.0, 1.6],
        "title": {"en": "Unresolved items register", "bn": "অমীমাংসিত বিষয়ের নিবন্ধন"},
        "cols": {"en": ["ID", "Unresolved item", "Why it is unresolved", "Owner", "How and when it is resolved", "Affects"],
                 "bn": ["আইডি", "অমীমাংসিত বিষয়", "কেন অমীমাংসিত", "দায়িত্বপ্রাপ্ত", "কীভাবে ও কখন সমাধান", "যেখানে প্রভাব"]},
        "rows": {
            "en": [
                ["U1", "Commencement dates and provisions in force of the PDPA 2026, NDMA 2026 and Cyber Security Act 2026, and any rules issued", "Gazetted texts not reviewed; official database blocks automated retrieval", "Host institution with legal counsel", "Independent legal review before MS2 (Section 14.3)", "Ch. 2, 8, 14; Tables 42, 43"],
                ["U2", "Whether NRDEX, the national source-code repository and chief data officers are retained in the Acts", "Described only for the 2025 ordinances", "Legal counsel", "Same legal review", "Sect. 8.8, 8.11, 10.8"],
                ["U3", "Status of the 2026 data-residency amendment after the Act", "Not confirmed in available sources", "Legal counsel", "Same legal review", "Sect. 8.12; Table 43"],
                ["U4", "Public GitHub release v1.1.0 and the Blueprint DOI", "Not yet published at the time of writing", "Author", "Publish the release, then the DOI record (Annex D), before circulation", "Table 1; Ch. 11; Annex D"],
                ["U5", "Government approval of the AI hub technical assistance project", "Pending in June 2026; later status not found", "Author, with the ICT Division", "Check before Blueprint 1.1", "Sect. 3.6, 17.2; Table 42"],
                ["U6", "Budget inputs: host salary scale, overhead rate, equipment quotations, duty and VAT status", "No host selected; no quotations", "Feasibility and costing study", "Deliverable D1.3 by month 6", "Ch. 17; Tables 49, 50, 61, 62"],
                ["U7", "In-kind access to national compute for Stage 1", "Draft policy only", "ICT Division; National Data Center", "Confirm by MS2; otherwise use the high-scenario allocation", "Sect. 9.7, 10.3; Table 31"],
                ["U8", "BanglaPolicyQA does not exist; all quality targets are unmeasured", "Work not yet funded", "Work package 6", "Benchmark v0 at MS3; first results at G2", "Ch. 9, 12; Tables 28, 54, 63"],
                ["U9", "No host institution, governance body or government focal point", "Decisions not yet taken", "ICT Division; host", "Decisions D2 and D4; MS1", "Ch. 5; Annexes S, T"],
                ["U10", "No funding requested or approved", "Proposal stage", "ICT Division or partners", "Decisions D2 and D5; before month 1", "Ch. 15, 17; Table 65"],
                ["U11", "References 1 to 83 not re-verified item by item", "Inherited from the White Paper", "Author", "Check before Blueprint 1.1", "References"],
                ["U12", "Gazette status of the Ninth National Pay Scale", "Only Cabinet approval reported", "Feasibility study", "D1.3", "Sect. 17.5; Table 49"],
                ["U13", "2023 AI readiness rank taken from a secondary source", "Index report not checked", "Author", "Check before Blueprint 1.1", "Sect. 2.2; Table 4"],
                ["U14", "Full copy-edit of the Bangla edition by a native editor", "Not yet done", "Author", "Before Blueprint 1.1", "Bangla edition"],
            ],
            "bn": [
                ["U1", "ব্যক্তিগত উপাত্ত সুরক্ষা আইন ২০২৬, জাতীয় উপাত্ত ব্যবস্থাপনা আইন ২০২৬ ও সাইবার নিরাপত্তা আইন ২০২৬-এর কার্যকারিতার তারিখ ও বলবৎ বিধান, এবং জারিকৃত বিধিমালা", "গেজেটভুক্ত পাঠ পর্যালোচিত হয়নি; সরকারি ডেটাবেস স্বয়ংক্রিয় সংগ্রহ বন্ধ রাখে", "আইনজীবীসহ আয়োজক প্রতিষ্ঠান", "MS2-এর আগে স্বাধীন আইনি পর্যালোচনা (অনুচ্ছেদ ১৪.৩)", "অধ্যায় ২, ৮, ১৪; সারণি ৪২, ৪৩"],
                ["U2", "NRDEX, জাতীয় সোর্স কোড ভান্ডার ও প্রধান ডেটা কর্মকর্তা আইনে বহাল আছে কি না", "কেবল ২০২৫ সালের অধ্যাদেশে বর্ণিত", "আইনজীবী", "একই আইনি পর্যালোচনা", "অনুচ্ছেদ ৮.৮, ৮.১১, ১০.৮"],
                ["U3", "আইনের পর ২০২৬ সালের ডেটা দেশে রাখা-সংক্রান্ত সংশোধনীর অবস্থা", "প্রাপ্ত উৎসে নিশ্চিত নয়", "আইনজীবী", "একই আইনি পর্যালোচনা", "অনুচ্ছেদ ৮.১২; সারণি ৪৩"],
                ["U4", "গিটহাবে প্রকাশ্য রিলিজ v1.1.0 ও ব্লুপ্রিন্টের DOI", "রচনার সময় পর্যন্ত প্রকাশিত হয়নি", "লেখক", "বিতরণের আগে রিলিজ, তারপর DOI রেকর্ড প্রকাশ (সংযুক্তি ঘ)", "সারণি ১; অধ্যায় ১১; সংযুক্তি ঘ"],
                ["U5", "এআই হাব কারিগরি সহায়তা প্রকল্পের সরকারি অনুমোদন", "জুন ২০২৬-এ অপেক্ষমাণ; পরবর্তী অবস্থা পাওয়া যায়নি", "আইসিটি বিভাগের সঙ্গে লেখক", "ব্লুপ্রিন্ট ১.১-এর আগে যাচাই", "অনুচ্ছেদ ৩.৬, ১৭.২; সারণি ৪২"],
                ["U6", "বাজেটের উপাত্ত: আয়োজকের বেতন-কাঠামো, পরোক্ষ ব্যয়ের হার, যন্ত্রপাতির দরপত্র, শুল্ক ও ভ্যাটের অবস্থা", "আয়োজক নির্বাচিত হয়নি; দরপত্র নেই", "সম্ভাব্যতা ও ব্যয়-নিরূপণ সমীক্ষা", "মাস ৬-এর মধ্যে ডেলিভারেবল D1.3", "অধ্যায় ১৭; সারণি ৪৯, ৫০, ৬১, ৬২"],
                ["U7", "পর্যায় ১-এর জন্য জাতীয় কম্পিউটিংয়ে বস্তুগত প্রবেশাধিকার", "কেবল খসড়া নীতিতে", "আইসিটি বিভাগ; জাতীয় ডেটা সেন্টার", "MS2-এর মধ্যে নিশ্চিত করা; অন্যথায় উচ্চ পরিস্থিতির বরাদ্দ ব্যবহার", "অনুচ্ছেদ ৯.৭, ১০.৩; সারণি ৩১"],
                ["U8", "BanglaPolicyQA এখনো নেই; মানের সব লক্ষ্য অপরিমাপিত", "কাজটি এখনো অর্থায়িত হয়নি", "কাজের প্যাকেজ ৬", "MS3-এ বেঞ্চমার্ক v0; G2-তে প্রথম ফলাফল", "অধ্যায় ৯, ১২; সারণি ২৮, ৫৪, ৬৩"],
                ["U9", "কোনো আয়োজক প্রতিষ্ঠান, শাসন-সংস্থা বা সরকারি ফোকাল পয়েন্ট নেই", "সিদ্ধান্ত এখনো হয়নি", "আইসিটি বিভাগ; আয়োজক", "সিদ্ধান্ত D2 ও D4; MS1", "অধ্যায় ৫; সংযুক্তি ধ, ন"],
                ["U10", "কোনো অর্থ চাওয়া বা অনুমোদিত হয়নি", "প্রস্তাব-পর্যায়", "আইসিটি বিভাগ বা অংশীদার", "সিদ্ধান্ত D2 ও D5; মাস ১-এর আগে", "অধ্যায় ১৫, ১৭; সারণি ৬৫"],
                ["U11", "তথ্যসূত্র ১ থেকে ৮৩ প্রতিটি আলাদাভাবে পুনঃযাচাই হয়নি", "হোয়াইট পেপার থেকে নেওয়া", "লেখক", "ব্লুপ্রিন্ট ১.১-এর আগে যাচাই", "তথ্যসূত্র"],
                ["U12", "নবম জাতীয় বেতন স্কেলের গেজেট-অবস্থা", "কেবল মন্ত্রিসভার অনুমোদন প্রতিবেদিত", "সম্ভাব্যতা সমীক্ষা", "D1.3", "অনুচ্ছেদ ১৭.৫; সারণি ৪৯"],
                ["U13", "২০২৩ সালের এআই প্রস্তুতি-র‍্যাংক মাধ্যমিক উৎস থেকে নেওয়া", "সূচকের প্রতিবেদন যাচাই হয়নি", "লেখক", "ব্লুপ্রিন্ট ১.১-এর আগে যাচাই", "অনুচ্ছেদ ২.২; সারণি ৪"],
                ["U14", "বাংলাভাষী সম্পাদকের মাধ্যমে বাংলা সংস্করণের পূর্ণ সম্পাদনা", "এখনো হয়নি", "লেখক", "ব্লুপ্রিন্ট ১.১-এর আগে", "বাংলা সংস্করণ"],
            ],
        },
        "note": {"en": "Each item is marked in the text where it applies (\"to be confirmed\", \"proposed\" or \"planning estimate\"). The register is updated at every Blueprint version.",
                 "bn": "প্রতিটি বিষয় লেখার প্রাসঙ্গিক স্থানে চিহ্নিত (\"নিশ্চিত করতে হবে\", \"প্রস্তাবিত\" বা \"পরিকল্পনা-প্রাক্কলন\")। ব্লুপ্রিন্টের প্রতিটি সংস্করণে নিবন্ধনটি হালনাগাদ হয়।"},
    },
]
