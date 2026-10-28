# -*- coding: utf-8 -*-
"""Blueprint tables 1-11 (English and Bangla).

Each table: id, widths (relative), title{en,bn}, cols{en,bn}, rows{en,bn}, note{en,bn} (optional).
Cell markup: **bold** only. Do not use the pipe character inside cells.
{{DOI}} and {{SUMMARY_DOI}} are replaced by the Blueprint and Summary DOIs at build time.
"""

TABLES_A = [
    # ------------------------------------------------------------------ 1
    {
        "id": "01",
        "widths": [1.5, 1.1, 2.6, 1.9, 2.1],
        "title": {
            "en": "The BAPIL document family and persistent identifiers",
            "bn": "BAPIL নথি-পরিবার ও স্থায়ী শনাক্তকারী (Persistent Identifier)",
        },
        "cols": {
            "en": ["Output", "Version", "Purpose", "Primary audience", "Identifier"],
            "bn": ["নথি/উপকরণ", "সংস্করণ", "উদ্দেশ্য", "প্রধান পাঠক", "শনাক্তকারী"],
        },
        "rows": {
            "en": [
                ["**White Paper**", "1.0 (repository release v1.0.1)", "Conceptual framework, international lessons, vision to 2041", "All stakeholders", "10.5281/zenodo.21363967"],
                ["**Executive Summary**", "1.0", "Concise summary of the White Paper", "Senior policymakers", "10.5281/zenodo.21441172"],
                ["**Technical Blueprint** (this document)", "1.0", "Buildable design: institution, architecture, data, governance, delivery plan", "Ministries, agencies, technical teams, partners", "{{DOI}}"],
                ["**Blueprint Summary**", "1.0", "Short summary of the Blueprint", "Decision-makers", "{{SUMMARY_DOI}}"],
                ["**Reference implementation**", "0.1.0 (to be issued in repository release v1.1.0 with this Blueprint)", "Research prototype of core Blueprint components with unit tests; not a production system", "Engineers, researchers, auditors", "GitHub repository; archived with the record"],
            ],
            "bn": [
                ["**হোয়াইট পেপার**", "১.০ (রিপোজিটরি রিলিজ v1.0.1)", "ধারণাগত কাঠামো, আন্তর্জাতিক শিক্ষা, ২০৪১ পর্যন্ত রূপকল্প", "সকল অংশীজন", "10.5281/zenodo.21363967"],
                ["**নির্বাহী সারসংক্ষেপ**", "১.০", "হোয়াইট পেপারের সংক্ষিপ্ত সার", "জ্যেষ্ঠ নীতিনির্ধারক", "10.5281/zenodo.21441172"],
                ["**টেকনিক্যাল ব্লুপ্রিন্ট** (এই নথি)", "১.০", "বাস্তবায়নযোগ্য নকশা: প্রতিষ্ঠান, স্থাপত্য, ডেটা, শাসন, বাস্তবায়ন পরিকল্পনা", "মন্ত্রণালয়, সংস্থা, কারিগরি দল, অংশীদার", "{{DOI}}"],
                ["**ব্লুপ্রিন্ট সারসংক্ষেপ**", "১.০", "ব্লুপ্রিন্টের সংক্ষিপ্ত সার", "সিদ্ধান্তগ্রহণকারী", "{{SUMMARY_DOI}}"],
                ["**রেফারেন্স বাস্তবায়ন**", "০.১.০ (এই ব্লুপ্রিন্টের সঙ্গে রিপোজিটরি রিলিজ v1.1.0-এ প্রকাশের জন্য নির্ধারিত)", "ইউনিট পরীক্ষাসহ ব্লুপ্রিন্টের মূল উপাদানের গবেষণা-প্রোটোটাইপ; উৎপাদন-ব্যবস্থা নয়", "প্রকৌশলী, গবেষক, নিরীক্ষক", "গিটহাব রিপোজিটরি; রেকর্ডের সঙ্গে সংরক্ষিত"],
            ],
        },
    },
    # ------------------------------------------------------------------ 2
    {
        "id": "02",
        "widths": [1.3, 2.6, 1.7, 1.7, 1.9, 1.8],
        "title": {
            "en": "System maturity classes used throughout this Blueprint",
            "bn": "এই ব্লুপ্রিন্টে ব্যবহৃত ব্যবস্থার পরিপক্বতা শ্রেণি",
        },
        "cols": {
            "en": ["Class", "Definition", "Users", "Permitted data", "Example", "Approval"],
            "bn": ["শ্রেণি", "সংজ্ঞা", "ব্যবহারকারী", "অনুমোদিত ডেটা", "উদাহরণ", "অনুমোদন"],
        },
        "rows": {
            "en": [
                ["**R** Research prototype", "Experimental system used to test methods; outputs never used for official decisions", "BAPIL researchers and research partners", "DC0; DC1 under a data-sharing agreement", "Benchmark experiments with open models", "Gates G0 and G1"],
                ["**A** Advisory tool", "Used by officials as one input among several; a person reviews every output before use", "Officials in pilot agencies", "DC0 and DC1; de-identified DC2 only", "Policy Search pilot in two to three agencies", "Gates G2 and G3; ERRC approval for tier T2"],
                ["**O** Operational system", "Integrated into agency workflows and owned and operated by the agency, not by BAPIL", "Host agency staff and, where intended, the public", "As authorised by law and the agency", "Agency-operated search service", "Gate G4 with host-agency legal review"],
            ],
            "bn": [
                ["**R** গবেষণা-প্রোটোটাইপ", "পদ্ধতি পরীক্ষার জন্য পরীক্ষামূলক ব্যবস্থা; এর ফলাফল কখনো সরকারি সিদ্ধান্তে ব্যবহৃত হয় না", "BAPIL গবেষক ও গবেষণা অংশীদার", "DC0; ডেটা-বিনিময় চুক্তির অধীনে DC1", "উন্মুক্ত মডেল দিয়ে বেঞ্চমার্ক পরীক্ষা", "গেট G0 ও G1"],
                ["**A** পরামর্শমূলক সরঞ্জাম", "কর্মকর্তারা একাধিক উৎসের একটি হিসেবে ব্যবহার করেন; প্রতিটি ফলাফল ব্যবহারের আগে একজন মানুষ পর্যালোচনা করেন", "পাইলট সংস্থার কর্মকর্তা", "DC0 ও DC1; শুধু পরিচয়-অপসারিত DC2", "দুই থেকে তিনটি সংস্থায় নীতি অনুসন্ধান পাইলট", "গেট G2 ও G3; T2 স্তরের জন্য ERRC অনুমোদন"],
                ["**O** পরিচালনাগত ব্যবস্থা", "সংস্থার কর্মপ্রবাহে সংযুক্ত; মালিকানা ও পরিচালনা সংস্থার, BAPIL-এর নয়", "স্বাগতিক সংস্থার কর্মী এবং প্রযোজ্য ক্ষেত্রে জনসাধারণ", "আইন ও সংস্থার অনুমোদন অনুযায়ী", "সংস্থা-পরিচালিত অনুসন্ধান সেবা", "স্বাগতিক সংস্থার আইনি পর্যালোচনাসহ গেট G4"],
            ],
        },
    },
    # ------------------------------------------------------------------ 3
    {
        "id": "03",
        "widths": [0.9, 4.6, 0.9],
        "title": {
            "en": "Core requirements (functional, non-functional and governance)",
            "bn": "মূল প্রয়োজনীয়তা (কার্যগত, অ-কার্যগত ও শাসনগত)",
        },
        "cols": {
            "en": ["ID", "Requirement", "Priority"],
            "bn": ["আইডি", "প্রয়োজনীয়তা", "অগ্রাধিকার"],
        },
        "rows": {
            "en": [
                ["FR-01", "Bilingual (Bangla and English) search over policy documents, robust to spelling variants and to Bangla or ASCII digits", "Must"],
                ["FR-02", "Answers grounded only in retrieved sources, with passage-level citations; the system abstains when evidence is insufficient", "Must"],
                ["FR-03", "Ingestion records provenance for every document: source URL, publisher, date, checksum and reuse terms", "Must"],
                ["FR-04", "Indicator and budget dashboards with downloadable data and methods notes", "Should"],
                ["FR-05", "Aggregate analysis of consultation feedback (topics, sentiment) with no profiling of individuals", "Should"],
                ["FR-06", "Register of all AI systems with owner, purpose, risk tier, model card and status", "Must"],
                ["FR-07", "Risk-tier assessment applied before any build and at every lifecycle gate", "Must"],
                ["FR-08", "Evaluation harness with versioned benchmarks and reproducible reports", "Must"],
                ["FR-09", "Public transparency register generated from the AI system register", "Should"],
                ["FR-10", "Documented, versioned API for programmatic access", "Should"],
                ["NFR-01", "Language parity: Bangla quality within 5 points of English on core metrics", "Must"],
                ["NFR-02", "Data residency: DC1 to DC3 data hosted in Bangladesh in accredited facilities", "Must"],
                ["NFR-03", "Security by design aligned with NIST CSF 2.0 and zero-trust access", "Must"],
                ["NFR-04", "Availability of 99% for pilots (working hours) once the recovery site is in place in Year 2; best effort with offline backups in Year 1; 99.5% at scale", "Should"],
                ["NFR-05", "Accessibility to WCAG 2.2 level AA; usable on mobile and low-bandwidth connections", "Must"],
                ["NFR-06", "Open standards and open source by default; no single-vendor lock-in", "Must"],
                ["NFR-07", "Reproducibility: versioned code, data snapshots and evaluation reports archived with DOIs", "Must"],
                ["NFR-08", "Explainability: every output shows its sources, confidence and known limitations", "Must"],
                ["NFR-09", "Performance: search p95 at most 3 s; answers p95 at most 10 s", "Should"],
                ["NFR-10", "Cost transparency: cost per 1,000 queries reported each quarter", "Could"],
                ["GR-01", "Human review of consequential outputs; AI is never the final decision-maker", "Must"],
                ["GR-02", "No build without tier screening (G0) and no pilot without gate approval (G2)", "Must"],
                ["GR-03", "Data minimisation: public data first; DPIA before any DC2 or DC3 processing", "Must"],
                ["GR-04", "Tamper-evident audit logs of queries, sources consulted and outputs", "Must"],
                ["GR-05", "Incident reporting and response within defined time limits", "Must"],
                ["GR-06", "Prohibited uses (tier T0) excluded by the BAPIL charter", "Must"],
            ],
            "bn": [
                ["FR-01", "নীতি-নথিতে দ্বিভাষিক (বাংলা ও ইংরেজি) অনুসন্ধান, যা বানানভেদ এবং বাংলা বা ইংরেজি অঙ্কের পার্থক্যে স্থিতিশীল", "আবশ্যিক"],
                ["FR-02", "উত্তর শুধু উদ্ধারকৃত উৎসের ভিত্তিতে, অনুচ্ছেদ-পর্যায়ের উদ্ধৃতিসহ; প্রমাণ অপর্যাপ্ত হলে ব্যবস্থা উত্তর দেওয়া থেকে বিরত থাকে", "আবশ্যিক"],
                ["FR-03", "প্রতিটি নথির উৎস-তথ্য (Provenance) সংরক্ষণ: উৎস URL, প্রকাশক, তারিখ, চেকসাম ও পুনর্ব্যবহারের শর্ত", "আবশ্যিক"],
                ["FR-04", "ডাউনলোডযোগ্য ডেটা ও পদ্ধতিগত টীকাসহ সূচক ও বাজেট ড্যাশবোর্ড", "প্রয়োজনীয়"],
                ["FR-05", "পরামর্শ-মতামতের সামষ্টিক বিশ্লেষণ (বিষয়, মনোভাব), কোনো ব্যক্তির প্রোফাইলিং ছাড়া", "প্রয়োজনীয়"],
                ["FR-06", "সকল এআই ব্যবস্থার নিবন্ধন: মালিক, উদ্দেশ্য, ঝুঁকি-স্তর, মডেল কার্ড ও অবস্থা", "আবশ্যিক"],
                ["FR-07", "যেকোনো নির্মাণের আগে এবং প্রতিটি জীবনচক্র-গেটে ঝুঁকি-স্তর মূল্যায়ন", "আবশ্যিক"],
                ["FR-08", "সংস্করণকৃত বেঞ্চমার্ক ও পুনরুৎপাদনযোগ্য প্রতিবেদনসহ মূল্যায়ন কাঠামো", "আবশ্যিক"],
                ["FR-09", "এআই ব্যবস্থা নিবন্ধন থেকে প্রস্তুত জনসমক্ষে স্বচ্ছতা নিবন্ধন", "প্রয়োজনীয়"],
                ["FR-10", "প্রোগ্রাম্যাটিক প্রবেশাধিকারের জন্য নথিভুক্ত ও সংস্করণকৃত API", "প্রয়োজনীয়"],
                ["NFR-01", "ভাষাগত সমতা: মূল মাপকাঠিতে বাংলার মান ইংরেজির তুলনায় ৫ পয়েন্টের মধ্যে", "আবশ্যিক"],
                ["NFR-02", "ডেটা-অবস্থান: DC1 থেকে DC3 ডেটা বাংলাদেশে স্বীকৃত স্থাপনায় সংরক্ষিত", "আবশ্যিক"],
                ["NFR-03", "NIST CSF 2.0 ও জিরো-ট্রাস্ট প্রবেশাধিকারের সঙ্গে সামঞ্জস্যপূর্ণ নকশাগত নিরাপত্তা", "আবশ্যিক"],
                ["NFR-04", "দ্বিতীয় বছরে পুনরুদ্ধার-স্থাপনা চালু হলে পাইলটে ৯৯% (কর্মঘণ্টায়); প্রথম বছরে অফলাইন ব্যাকআপসহ সর্বোচ্চ প্রচেষ্টা; সম্প্রসারিত পর্যায়ে ৯৯.৫% প্রাপ্যতা", "প্রয়োজনীয়"],
                ["NFR-05", "WCAG 2.2 AA মানের প্রবেশযোগ্যতা; মোবাইল ও স্বল্প-ব্যান্ডউইথে ব্যবহারযোগ্য", "আবশ্যিক"],
                ["NFR-06", "ডিফল্টভাবে উন্মুক্ত মানদণ্ড ও উন্মুক্ত সোর্স; একক বিক্রেতার উপর নির্ভরশীলতা নয়", "আবশ্যিক"],
                ["NFR-07", "পুনরুৎপাদনযোগ্যতা: সংস্করণকৃত কোড, ডেটা স্ন্যাপশট ও মূল্যায়ন প্রতিবেদন DOI-সহ সংরক্ষিত", "আবশ্যিক"],
                ["NFR-08", "ব্যাখ্যাযোগ্যতা: প্রতিটি ফলাফলে উৎস, আস্থার মাত্রা ও জানা সীমাবদ্ধতা প্রদর্শিত", "আবশ্যিক"],
                ["NFR-09", "কর্মক্ষমতা: অনুসন্ধানের p95 সর্বোচ্চ ৩ সেকেন্ড; উত্তরের p95 সর্বোচ্চ ১০ সেকেন্ড", "প্রয়োজনীয়"],
                ["NFR-10", "ব্যয়-স্বচ্ছতা: প্রতি ১,০০০ অনুসন্ধানের ব্যয় প্রতি ত্রৈমাসিকে প্রকাশ", "ঐচ্ছিক"],
                ["GR-01", "গুরুত্বপূর্ণ ফলাফলের মানব-পর্যালোচনা; এআই কখনো চূড়ান্ত সিদ্ধান্তগ্রহণকারী নয়", "আবশ্যিক"],
                ["GR-02", "স্তর-যাচাই (G0) ছাড়া কোনো নির্মাণ নয় এবং গেট-অনুমোদন (G2) ছাড়া কোনো পাইলট নয়", "আবশ্যিক"],
                ["GR-03", "ডেটা ন্যূনতমকরণ: প্রথমে জনসমক্ষে প্রকাশিত ডেটা; DC2 বা DC3 প্রক্রিয়াকরণের আগে DPIA", "আবশ্যিক"],
                ["GR-04", "অনুসন্ধান, ব্যবহৃত উৎস ও ফলাফলের হস্তক্ষেপ-শনাক্তযোগ্য নিরীক্ষা লগ", "আবশ্যিক"],
                ["GR-05", "নির্ধারিত সময়সীমার মধ্যে ঘটনা প্রতিবেদন ও প্রতিক্রিয়া", "আবশ্যিক"],
                ["GR-06", "নিষিদ্ধ ব্যবহার (স্তর T0) BAPIL সনদে বাদ দেওয়া", "আবশ্যিক"],
            ],
        },
        "note": {
            "en": "Priority follows the MoSCoW convention (Must, Should, Could). Annex A traces 16 requirements to components, code modules and tests or pilot acceptance; the others are verified through pilot acceptance criteria, security testing or governance review.",
            "bn": "অগ্রাধিকার MoSCoW রীতি অনুসরণ করে (আবশ্যিক, প্রয়োজনীয়, ঐচ্ছিক)। সংযুক্তি ক ১৬টি প্রয়োজনীয়তাকে উপাদান, কোড মডিউল ও পরীক্ষা বা পাইলট গ্রহণের সঙ্গে সংযুক্ত করে; বাকিগুলো পাইলট গ্রহণের মানদণ্ড, নিরাপত্তা পরীক্ষা বা শাসনগত পর্যালোচনার মাধ্যমে যাচাই করা হয়।",
        },
    },
    # ------------------------------------------------------------------ 4
    {
        "id": "04",
        "widths": [2.6, 1.3, 1.1, 1.1, 1.1, 1.35, 1.6],
        "title": {
            "en": "Assessment of institutional operating-model options",
            "bn": "প্রাতিষ্ঠানিক পরিচালন-মডেলের বিকল্পসমূহের মূল্যায়ন",
        },
        "cols": {
            "en": ["Option", "Independence", "Data access", "Policy uptake", "Speed to start", "Sustainability", "Verdict"],
            "bn": ["বিকল্প", "স্বাধীনতা", "ডেটা প্রবেশাধিকার", "নীতিতে প্রয়োগ", "শুরুর গতি", "টেকসইতা", "সিদ্ধান্ত"],
        },
        "rows": {
            "en": [
                ["**A.** Unit embedded in a government agency", "Low", "High", "High", "Medium", "Medium", "Not recommended for Phase 1"],
                ["**B.** University research centre", "High", "Low", "Low", "High", "Medium", "Partial fit"],
                ["**C.** Hybrid: university-anchored lab with a government MoU and a multi-stakeholder board", "High", "Medium to high", "Medium to high", "High", "Medium to high", "**Recommended**"],
                ["**D.** Independent non-profit foundation", "High", "Low to medium", "Medium", "Low", "Medium", "Option for a later stage"],
            ],
            "bn": [
                ["**ক.** সরকারি সংস্থার অভ্যন্তরীণ ইউনিট", "নিম্ন", "উচ্চ", "উচ্চ", "মাঝারি", "মাঝারি", "প্রথম ধাপের জন্য সুপারিশকৃত নয়"],
                ["**খ.** বিশ্ববিদ্যালয়-ভিত্তিক গবেষণা কেন্দ্র", "উচ্চ", "নিম্ন", "নিম্ন", "উচ্চ", "মাঝারি", "আংশিক উপযুক্ত"],
                ["**গ.** মিশ্র মডেল: সরকারি সমঝোতা স্মারক (MoU) ও বহু-অংশীজন বোর্ডসহ বিশ্ববিদ্যালয়-ভিত্তিক ল্যাব", "উচ্চ", "মাঝারি থেকে উচ্চ", "মাঝারি থেকে উচ্চ", "উচ্চ", "মাঝারি থেকে উচ্চ", "**সুপারিশকৃত**"],
                ["**ঘ.** স্বাধীন অলাভজনক ফাউন্ডেশন", "উচ্চ", "নিম্ন থেকে মাঝারি", "মাঝারি", "নিম্ন", "মাঝারি", "পরবর্তী ধাপের বিকল্প"],
            ],
        },
        "note": {
            "en": "Qualitative assessment by the author against five criteria; to be validated in the Phase 1 feasibility study (Deliverable D1.3).",
            "bn": "পাঁচটি মানদণ্ডে লেখকের গুণগত মূল্যায়ন; প্রথম ধাপের সম্ভাব্যতা সমীক্ষায় (ডেলিভারেবল D1.3) যাচাই করা হবে।",
        },
    },
    # ------------------------------------------------------------------ 5
    {
        "id": "05",
        "widths": [1.7, 2.6, 2.8, 1.6],
        "title": {
            "en": "Governance bodies, composition and decision rights",
            "bn": "শাসন-কাঠামোর সংস্থাসমূহ, গঠন ও সিদ্ধান্তের অধিকার",
        },
        "cols": {
            "en": ["Body", "Composition", "Key responsibilities", "Decision rights"],
            "bn": ["সংস্থা", "গঠন", "প্রধান দায়িত্ব", "সিদ্ধান্তের অধিকার"],
        },
        "rows": {
            "en": [
                ["**Steering Board**", "7 to 9 members: ICT Division (co-chair), host institution (co-chair), Planning Commission, a data custodian agency, academia, civil society, industry; BAPIL Director as secretary", "Strategy, annual plan and budget; partnership approvals; joint G4 adoption decisions with host agencies", "Approves plans and budgets"],
                ["**Ethics and Risk Review Committee (ERRC)**", "5 to 7 members, majority external: law and human rights, data protection, ethics, domain experts, civil society, technical reviewer", "Reviews tier T2 and T3 systems at G1, G2 and G4; reviews incidents; publishes decision summaries", "Veto on pilots and deployment, binding on BAPIL and on the host within its statutes (Section 5.3)"],
                ["**Technical Architecture Board (TAB)**", "Lead engineers, security lead, two external technical reviewers", "Architecture and security standards; design reviews; model and dependency approvals", "Approves designs at G1"],
                ["**International Advisory Panel**", "Invited experts serving in a personal capacity", "Peer review of methods, benchmarks and governance; international linkages", "Advisory only"],
                ["**Director and units**", "Director, six thematic units from the White Paper, and a cross-cutting platform engineering team", "Delivery of research, pilots, training and publications", "Operational decisions within approved plans"],
                ["**Host-agency product owners**", "Named officials in each agency piloting a tool", "Define needs, recruit pilot users, accept or reject at G3 and G4", "Acceptance of pilots in their agency"],
            ],
            "bn": [
                ["**স্টিয়ারিং বোর্ড**", "৭ থেকে ৯ জন সদস্য: আইসিটি বিভাগ (সহ-সভাপতি), স্বাগতিক প্রতিষ্ঠান (সহ-সভাপতি), পরিকল্পনা কমিশন, একটি ডেটা-রক্ষক সংস্থা, একাডেমিয়া, নাগরিক সমাজ, শিল্পখাত; BAPIL পরিচালক সদস্য-সচিব", "কৌশল, বার্ষিক পরিকল্পনা ও বাজেট; অংশীদারিত্ব অনুমোদন; স্বাগতিক সংস্থার সঙ্গে যৌথভাবে G4 গ্রহণ-সিদ্ধান্ত", "পরিকল্পনা ও বাজেট অনুমোদন"],
                ["**নৈতিকতা ও ঝুঁকি পর্যালোচনা কমিটি (ERRC)**", "৫ থেকে ৭ জন, সংখ্যাগরিষ্ঠ বহিঃস্থ: আইন ও মানবাধিকার, ডেটা সুরক্ষা, নৈতিকতা, বিষয়-বিশেষজ্ঞ, নাগরিক সমাজ, কারিগরি পর্যালোচক", "G1, G2 ও G4-এ T2 ও T3 স্তরের ব্যবস্থা পর্যালোচনা; ঘটনা পর্যালোচনা; সিদ্ধান্তের সারাংশ প্রকাশ", "পাইলট ও প্রয়োগে ভেটো, যা BAPIL-এর জন্য এবং স্বাগতিকের সংবিধির মধ্যে স্বাগতিকের জন্য বাধ্যতামূলক (অনুচ্ছেদ ৫.৩)"],
                ["**কারিগরি স্থাপত্য বোর্ড (TAB)**", "প্রধান প্রকৌশলী, নিরাপত্তা প্রধান, দুইজন বহিঃস্থ কারিগরি পর্যালোচক", "স্থাপত্য ও নিরাপত্তা মানদণ্ড; নকশা পর্যালোচনা; মডেল ও নির্ভরতা অনুমোদন", "G1-এ নকশা অনুমোদন"],
                ["**আন্তর্জাতিক উপদেষ্টা প্যানেল**", "ব্যক্তিগত সক্ষমতায় আমন্ত্রিত বিশেষজ্ঞ", "পদ্ধতি, বেঞ্চমার্ক ও শাসনব্যবস্থার সমকক্ষ পর্যালোচনা; আন্তর্জাতিক সংযোগ", "শুধু পরামর্শমূলক"],
                ["**পরিচালক ও ইউনিটসমূহ**", "পরিচালক, হোয়াইট পেপারের ছয়টি বিষয়ভিত্তিক ইউনিট এবং একটি আন্তঃবিভাগীয় প্ল্যাটফর্ম প্রকৌশল দল", "গবেষণা, পাইলট, প্রশিক্ষণ ও প্রকাশনা বাস্তবায়ন", "অনুমোদিত পরিকল্পনার মধ্যে পরিচালনাগত সিদ্ধান্ত"],
                ["**স্বাগতিক সংস্থার প্রোডাক্ট ওনার**", "পাইলট পরিচালনাকারী প্রতিটি সংস্থার মনোনীত কর্মকর্তা", "চাহিদা নির্ধারণ, পাইলট ব্যবহারকারী সংগ্রহ, G3 ও G4-এ গ্রহণ বা প্রত্যাখ্যান", "নিজ সংস্থায় পাইলট গ্রহণ"],
            ],
        },
    },
    # ------------------------------------------------------------------ 6
    {
        "id": "06",
        "widths": [0.6, 1.9, 3.0, 2.6, 1.6],
        "title": {
            "en": "Reference architecture components and candidate technologies",
            "bn": "রেফারেন্স স্থাপত্যের উপাদান ও সম্ভাব্য প্রযুক্তি",
        },
        "cols": {
            "en": ["ID", "Component", "Function", "Candidate open technologies", "Reference implementation"],
            "bn": ["আইডি", "উপাদান", "কাজ", "সম্ভাব্য উন্মুক্ত প্রযুক্তি", "রেফারেন্স বাস্তবায়ন"],
        },
        "rows": {
            "en": [
                ["C1", "Source connectors", "Harvest public documents on a schedule, respecting site terms; record provenance", "Python workers, Scrapy, cron or Airflow", "Planned"],
                ["C2", "Ingestion and normalisation", "Extract text from PDF and HTML, Bangla OCR, Unicode normalisation, chunking", "Apache Tika [136], Tesseract (ben, eng) [135], custom normaliser", "bapil.text, bapil.corpus"],
                ["C3", "Document store and catalogue", "Originals, extracted text and DCAT-aligned metadata with versioning", "PostgreSQL [137], MinIO (S3-compatible), CKAN [138]", "JSONL corpus with checksums"],
                ["C4", "Search index", "Lexical BM25 plus dense vectors with hybrid ranking", "OpenSearch [139], or PostgreSQL with pgvector [140]", "bapil.search (BM25, bilingual)"],
                ["C5", "Answer service", "Retrieve, cite, abstain; optional LLM generation with citation verification", "Open-weight LLMs served with vLLM or llama.cpp", "bapil.answer (extractive, cited)"],
                ["C6", "Analytics engine", "Budget extraction, indicators, topic models", "Python, pandas, DuckDB", "Planned"],
                ["C7", "Portal and dashboards", "Bilingual, accessible user interface", "Web framework; Apache Superset", "Planned"],
                ["C8", "API gateway", "Versioned REST API, quotas, rate limits", "FastAPI, Kong", "bapil.api (standard library)"],
                ["C9", "Identity and access", "Single sign-on, role-based access, MFA", "Keycloak", "Planned"],
                ["C10", "Audit and observability", "Tamper-evident logs, metrics, tracing", "OpenTelemetry, Prometheus, Grafana", "bapil.audit (hash-chained JSONL)"],
                ["C11", "Model registry and evaluation", "Model cards, versioned evaluations, benchmarks", "MLflow", "bapil.evaluate"],
                ["C12", "Governance workbench", "AI system register, risk assessments, incidents, transparency register", "Lightweight web application", "bapil.risk, bapil.registry"],
            ],
            "bn": [
                ["C1", "উৎস সংযোগকারী", "সাইটের শর্ত মেনে নির্ধারিত সময়ে জনসমক্ষে প্রকাশিত নথি সংগ্রহ; উৎস-তথ্য সংরক্ষণ", "Python worker, Scrapy, cron বা Airflow", "পরিকল্পিত"],
                ["C2", "গ্রহণ ও প্রমিতকরণ", "PDF ও HTML থেকে টেক্সট নিষ্কাশন, বাংলা OCR, ইউনিকোড প্রমিতকরণ, খণ্ডকরণ", "Apache Tika [136], Tesseract (ben, eng) [135], নিজস্ব প্রমিতকারী", "bapil.text, bapil.corpus"],
                ["C3", "নথি সংরক্ষণাগার ও ক্যাটালগ", "মূল নথি, নিষ্কাশিত টেক্সট ও DCAT-সামঞ্জস্যপূর্ণ মেটাডেটা, সংস্করণসহ", "PostgreSQL [137], MinIO (S3-সামঞ্জস্যপূর্ণ), CKAN [138]", "চেকসামসহ JSONL কর্পাস"],
                ["C4", "অনুসন্ধান সূচি", "শব্দভিত্তিক BM25 ও ঘন ভেক্টরের মিশ্র র‍্যাংকিং", "OpenSearch [139], বা pgvector-সহ [140] PostgreSQL", "bapil.search (BM25, দ্বিভাষিক)"],
                ["C5", "উত্তর সেবা", "উদ্ধার, উদ্ধৃতি, বিরত থাকা; উদ্ধৃতি যাচাইসহ ঐচ্ছিক LLM উৎপাদন", "vLLM বা llama.cpp-এ চালিত উন্মুক্ত-ওজন LLM", "bapil.answer (উদ্ধৃতিসহ নিষ্কাশনমূলক)"],
                ["C6", "বিশ্লেষণ ইঞ্জিন", "বাজেট নিষ্কাশন, সূচক, বিষয়-মডেল", "Python, pandas, DuckDB", "পরিকল্পিত"],
                ["C7", "পোর্টাল ও ড্যাশবোর্ড", "দ্বিভাষিক ও প্রবেশযোগ্য ব্যবহারকারী ইন্টারফেস", "ওয়েব ফ্রেমওয়ার্ক; Apache Superset", "পরিকল্পিত"],
                ["C8", "API গেটওয়ে", "সংস্করণকৃত REST API, কোটা, হার-সীমা", "FastAPI, Kong", "bapil.api (স্ট্যান্ডার্ড লাইব্রেরি)"],
                ["C9", "পরিচয় ও প্রবেশাধিকার", "একক সাইন-অন, ভূমিকাভিত্তিক প্রবেশাধিকার, বহু-উপাদান প্রমাণীকরণ", "Keycloak", "পরিকল্পিত"],
                ["C10", "নিরীক্ষা ও পর্যবেক্ষণযোগ্যতা", "হস্তক্ষেপ-শনাক্তযোগ্য লগ, মেট্রিক, ট্রেসিং", "OpenTelemetry, Prometheus, Grafana", "bapil.audit (হ্যাশ-শৃঙ্খলিত JSONL)"],
                ["C11", "মডেল রেজিস্ট্রি ও মূল্যায়ন", "মডেল কার্ড, সংস্করণকৃত মূল্যায়ন, বেঞ্চমার্ক", "MLflow", "bapil.evaluate"],
                ["C12", "শাসন কর্মক্ষেত্র", "এআই ব্যবস্থা নিবন্ধন, ঝুঁকি মূল্যায়ন, ঘটনা, স্বচ্ছতা নিবন্ধন", "হালকা ওয়েব অ্যাপ্লিকেশন", "bapil.risk, bapil.registry"],
            ],
        },
        "note": {
            "en": "Technologies are candidates, not mandates; final choices are made by the Technical Architecture Board against requirements NFR-02, NFR-03 and NFR-06.",
            "bn": "প্রযুক্তিগুলো সম্ভাব্য বিকল্প, বাধ্যতামূলক নয়; চূড়ান্ত পছন্দ কারিগরি স্থাপত্য বোর্ড NFR-02, NFR-03 ও NFR-06 অনুযায়ী নির্ধারণ করবে।",
        },
    },
    # ------------------------------------------------------------------ 7
    {
        "id": "07",
        "widths": [1.4, 2.0, 2.4, 2.8, 1.5],
        "title": {
            "en": "Data classification and handling rules",
            "bn": "ডেটা শ্রেণিবিন্যাস ও ব্যবস্থাপনার নিয়ম",
        },
        "cols": {
            "en": ["Class", "Description", "Examples", "Handling rules", "Use in pilots"],
            "bn": ["শ্রেণি", "বিবরণ", "উদাহরণ", "ব্যবস্থাপনার নিয়ম", "পাইলটে ব্যবহার"],
        },
        "rows": {
            "en": [
                ["**DC0** Public", "Officially published and intended for the public", "Laws, gazettes, budget documents, plans, statistical releases", "Provenance and integrity checks; reuse subject to source terms", "Yes"],
                ["**DC1** Internal", "Non-personal information not yet published", "Draft reports shared under agreement, administrative metadata", "Data-sharing agreement; role-based access; hosted in Bangladesh", "Limited, under agreement"],
                ["**DC2** Personal", "Information identifying a person", "Named consultation submissions, survey microdata", "Lawful basis under the PDPA 2026; DPIA; de-identification before analysis; ERRC approval", "Only consented and de-identified"],
                ["**DC3** Sensitive or restricted", "Sensitive personal data or security-classified information", "Health, biometric, financial or children’s data; security data", "Excluded from BAPIL work", "No"],
            ],
            "bn": [
                ["**DC0** উন্মুক্ত", "সরকারিভাবে প্রকাশিত ও জনসাধারণের জন্য উদ্দিষ্ট", "আইন, গেজেট, বাজেট নথি, পরিকল্পনা, পরিসংখ্যান প্রকাশনা", "উৎস-তথ্য ও অখণ্ডতা যাচাই; উৎসের শর্ত সাপেক্ষে পুনর্ব্যবহার", "হ্যাঁ"],
                ["**DC1** অভ্যন্তরীণ", "অপ্রকাশিত, ব্যক্তিগত নয় এমন তথ্য", "চুক্তির অধীনে বিনিময়কৃত খসড়া প্রতিবেদন, প্রশাসনিক মেটাডেটা", "ডেটা-বিনিময় চুক্তি; ভূমিকাভিত্তিক প্রবেশাধিকার; বাংলাদেশে সংরক্ষণ", "সীমিত, চুক্তির অধীনে"],
                ["**DC2** ব্যক্তিগত", "ব্যক্তিকে শনাক্তযোগ্য তথ্য", "নামসহ পরামর্শ-মতামত, জরিপের মাইক্রোডেটা", "ব্যক্তিগত উপাত্ত সুরক্ষা আইন ২০২৬ অনুযায়ী আইনগত ভিত্তি; DPIA; বিশ্লেষণের আগে পরিচয়-অপসারণ; ERRC অনুমোদন", "শুধু সম্মতিপ্রাপ্ত ও পরিচয়-অপসারিত"],
                ["**DC3** সংবেদনশীল বা সংরক্ষিত", "সংবেদনশীল ব্যক্তিগত বা নিরাপত্তা-শ্রেণিভুক্ত তথ্য", "স্বাস্থ্য, বায়োমেট্রিক, আর্থিক বা শিশুদের ডেটা; নিরাপত্তা-সংক্রান্ত ডেটা", "BAPIL-এর কাজে বর্জিত", "না"],
            ],
        },
    },
    # ------------------------------------------------------------------ 8
    {
        "id": "08",
        "widths": [2.1, 2.1, 2.2, 1.1, 0.8, 2.3],
        "title": {
            "en": "Initial inventory of public data sources for the pilot corpus",
            "bn": "পাইলট কর্পাসের জন্য জনসমক্ষে প্রকাশিত ডেটা-উৎসের প্রাথমিক তালিকা",
        },
        "cols": {
            "en": ["Source", "Custodian", "Content", "Format", "Class", "Access note"],
            "bn": ["উৎস", "রক্ষক", "বিষয়বস্তু", "ফরম্যাট", "শ্রেণি", "প্রবেশাধিকার-সংক্রান্ত টীকা"],
        },
        "rows": {
            "en": [
                ["Laws of Bangladesh (bdlaws.minlaw.gov.bd)", "Legislative and Parliamentary Affairs Division", "Acts and ordinances in Bangla and English", "HTML", "DC0", "Confirm reuse terms; request bulk export (Decision D3)"],
                ["Bangladesh Gazette (dpp.gov.bd)", "Department of Printing and Publications", "Gazette notifications", "PDF, often scanned", "DC0", "OCR quality is a key risk (R3)"],
                ["National budget documents (mof.gov.bd)", "Finance Division", "Budget speeches, MTBF, allocations", "PDF, spreadsheets", "DC0", "Basis of Pilot P2"],
                ["Development plans (plancomm.gov.bd)", "Planning Commission", "Five-year plans, perspective plan, ADP", "PDF, spreadsheets", "DC0", "Versioning across plan revisions"],
                ["Official statistics (bbs.gov.bd)", "Bangladesh Bureau of Statistics", "Yearbooks and survey reports", "PDF, spreadsheets", "DC0", "Aggregates only; microdata excluded"],
                ["Open Government Data (data.gov.bd)", "ICT Division and a2i", "Machine-readable datasets", "CSV, spreadsheets, API", "DC0", "Check dataset-level licences"],
                ["National Portal (bangladesh.gov.bd)", "ICT Division and a2i", "Office information, services, notices", "HTML", "DC0", "High volume; prioritise by ministry"],
                ["Parliament (parliament.gov.bd)", "Bangladesh Parliament Secretariat", "Bills, debates, committee reports", "PDF", "DC0", "Mixed scanned and digital"],
                ["e-Nothi records", "a2i and ministries", "Administrative files", "Internal system", "DC1 to DC3", "Out of scope for pilots"],
                ["BAPIL publications (this repository)", "BAPIL", "White Paper, Executive Summary, Blueprint, studies", "Markdown, PDF", "DC0", "Demonstration corpus of the reference implementation"],
            ],
            "bn": [
                ["বাংলাদেশের আইন (bdlaws.minlaw.gov.bd)", "লেজিসলেটিভ ও সংসদ বিষয়ক বিভাগ", "বাংলা ও ইংরেজিতে আইন ও অধ্যাদেশ", "HTML", "DC0", "পুনর্ব্যবহারের শর্ত নিশ্চিত করা; একসঙ্গে রপ্তানির অনুরোধ (সিদ্ধান্ত D3)"],
                ["বাংলাদেশ গেজেট (dpp.gov.bd)", "মুদ্রণ ও প্রকাশনা অধিদপ্তর", "গেজেট প্রজ্ঞাপন", "PDF, প্রায়ই স্ক্যানকৃত", "DC0", "OCR-এর মান একটি বড় ঝুঁকি (R3)"],
                ["জাতীয় বাজেট নথি (mof.gov.bd)", "অর্থ বিভাগ", "বাজেট বক্তৃতা, মধ্যমেয়াদি বাজেট কাঠামো, বরাদ্দ", "PDF, স্প্রেডশিট", "DC0", "পাইলট P2-এর ভিত্তি"],
                ["উন্নয়ন পরিকল্পনা (plancomm.gov.bd)", "পরিকল্পনা কমিশন", "পঞ্চবার্ষিক পরিকল্পনা, প্রেক্ষিত পরিকল্পনা, এডিপি", "PDF, স্প্রেডশিট", "DC0", "পরিকল্পনা সংশোধনের মধ্যে সংস্করণ ব্যবস্থাপনা"],
                ["সরকারি পরিসংখ্যান (bbs.gov.bd)", "বাংলাদেশ পরিসংখ্যান ব্যুরো", "বর্ষগ্রন্থ ও জরিপ প্রতিবেদন", "PDF, স্প্রেডশিট", "DC0", "শুধু সামষ্টিক তথ্য; মাইক্রোডেটা বর্জিত"],
                ["উন্মুক্ত সরকারি ডেটা (data.gov.bd)", "আইসিটি বিভাগ ও এটুআই", "যন্ত্র-পাঠযোগ্য ডেটাসেট", "CSV, স্প্রেডশিট, API", "DC0", "ডেটাসেটভিত্তিক লাইসেন্স যাচাই"],
                ["জাতীয় তথ্য বাতায়ন (bangladesh.gov.bd)", "আইসিটি বিভাগ ও এটুআই", "দপ্তরের তথ্য, সেবা, বিজ্ঞপ্তি", "HTML", "DC0", "বিপুল পরিমাণ; মন্ত্রণালয়ভিত্তিক অগ্রাধিকার"],
                ["জাতীয় সংসদ (parliament.gov.bd)", "বাংলাদেশ জাতীয় সংসদ সচিবালয়", "বিল, বিতর্ক, কমিটির প্রতিবেদন", "PDF", "DC0", "স্ক্যানকৃত ও ডিজিটালের মিশ্রণ"],
                ["ই-নথি রেকর্ড", "এটুআই ও মন্ত্রণালয়সমূহ", "প্রশাসনিক নথি", "অভ্যন্তরীণ ব্যবস্থা", "DC1 থেকে DC3", "পাইলটের আওতাবহির্ভূত"],
                ["BAPIL প্রকাশনা (এই রিপোজিটরি)", "BAPIL", "হোয়াইট পেপার, নির্বাহী সারসংক্ষেপ, ব্লুপ্রিন্ট, গবেষণা", "Markdown, PDF", "DC0", "রেফারেন্স বাস্তবায়নের প্রদর্শনী কর্পাস"],
            ],
        },
        "note": {
            "en": "Custodians and access terms must be confirmed with each agency before ingestion. Listing a source does not imply any agreement with its custodian.",
            "bn": "গ্রহণের আগে প্রতিটি সংস্থার সঙ্গে রক্ষক ও প্রবেশাধিকারের শর্ত নিশ্চিত করতে হবে। কোনো উৎস তালিকাভুক্ত করা মানে তার রক্ষকের সঙ্গে কোনো চুক্তি বোঝায় না।",
        },
    },
    # ------------------------------------------------------------------ 9
    {
        "id": "09",
        "widths": [1.5, 2.3, 3.2, 1.6],
        "title": {
            "en": "Evaluation metrics and proposed pilot exit thresholds",
            "bn": "মূল্যায়নের মাপকাঠি ও প্রস্তাবিত পাইলট উত্তরণ-সীমা",
        },
        "cols": {
            "en": ["Dimension", "Metric", "Definition", "Proposed threshold"],
            "bn": ["মাত্রা", "মাপকাঠি", "সংজ্ঞা", "প্রস্তাবিত সীমা"],
        },
        "rows": {
            "en": [
                ["Retrieval", "Recall@10", "Share of answerable test questions with at least one gold passage in the top 10 results [128]", "at least 0.85"],
                ["Retrieval", "MRR@10", "Mean reciprocal rank of the first relevant passage [129]", "at least 0.70"],
                ["Retrieval", "nDCG@10", "Rank-weighted relevance against graded judgements [130]", "at least 0.75"],
                ["Grounding", "Citation precision", "Share of answer sentences whose cited passage fully supports the sentence, judged by two trained annotators", "at least 0.95"],
                ["Grounding", "Unsupported-claim rate", "Share of answer sentences not supported by any retrieved passage, judged on the same sample", "at most 2%"],
                ["Abstention", "Correct abstention", "Share of out-of-scope questions on which the system declines to answer", "at least 0.90"],
                ["Abstention", "Answer coverage", "Share of answerable questions that are answered rather than abstained", "at least 0.80"],
                ["Language parity", "Bangla and English gap", "Difference in Recall@10 between Bangla and English question sets, reported with its confidence interval", "at most 5 points"],
                ["Robustness", "Variant spelling recall", "Recall@10 on variant-spelling Bangla queries in Bangla script (romanised queries reported in v0 and gated from v1)", "at least 0.75"],
                ["Safety", "Prompt-injection success", "Share of red-team injection attempts that change system behaviour", "at most 5%"],
                ["Human evaluation", "Usefulness and fluency", "Mean rating by pilot users and Bangla editors on a 5-point scale", "at least 4.0"],
                ["Efficiency", "Latency p95", "95th-percentile response time for search and for answers under pilot load", "3 s and 10 s"],
                ["Reliability", "Availability", "Share of working hours in which search is available during the pilot", "at least 99%"],
            ],
            "bn": [
                ["উদ্ধার", "Recall@10", "যেসব উত্তরযোগ্য পরীক্ষা-প্রশ্নের অন্তত একটি সঠিক অনুচ্ছেদ প্রথম ১০টি ফলাফলে আসে তার অনুপাত [128]", "কমপক্ষে ০.৮৫"],
                ["উদ্ধার", "MRR@10", "প্রথম প্রাসঙ্গিক অনুচ্ছেদের র‍্যাংকের গড় বিপরীত মান [129]", "কমপক্ষে ০.৭০"],
                ["উদ্ধার", "nDCG@10", "স্তরভিত্তিক বিচারের বিপরীতে র‍্যাংক-ভারিত প্রাসঙ্গিকতা [130]", "কমপক্ষে ০.৭৫"],
                ["ভিত্তিস্থাপন", "উদ্ধৃতির নির্ভুলতা", "যেসব উত্তর-বাক্যের উদ্ধৃত অনুচ্ছেদ বাক্যটিকে পুরোপুরি সমর্থন করে তার অনুপাত, দুজন প্রশিক্ষিত টীকাকারের বিচারে", "কমপক্ষে ০.৯৫"],
                ["ভিত্তিস্থাপন", "অসমর্থিত দাবির হার", "যেসব উত্তর-বাক্য কোনো উদ্ধারকৃত অনুচ্ছেদ দ্বারা সমর্থিত নয় তার অনুপাত, একই নমুনায় বিচারকৃত", "সর্বোচ্চ ২%"],
                ["বিরত থাকা", "সঠিক বিরতি", "আওতাবহির্ভূত প্রশ্নে ব্যবস্থার উত্তর না দেওয়ার অনুপাত", "কমপক্ষে ০.৯০"],
                ["বিরত থাকা", "উত্তর-আওতা", "উত্তরযোগ্য প্রশ্নের মধ্যে যেগুলোর উত্তর দেওয়া হয়, বিরত থাকা হয় না, তার অনুপাত", "কমপক্ষে ০.৮০"],
                ["ভাষাগত সমতা", "বাংলা ও ইংরেজির ব্যবধান", "বাংলা ও ইংরেজি প্রশ্নসেটে Recall@10-এর পার্থক্য, আস্থা-ব্যবধানসহ প্রতিবেদিত", "সর্বোচ্চ ৫ পয়েন্ট"],
                ["স্থিতিশীলতা", "বানানভেদে উদ্ধার", "বাংলা হরফে ভিন্ন বানানের প্রশ্নে Recall@10 (রোমান হরফের প্রশ্ন v0-তে প্রতিবেদিত, v1 থেকে গেটের অধীনে)", "কমপক্ষে ০.৭৫"],
                ["নিরাপত্তা", "প্রম্পট-ইনজেকশনের সাফল্য", "রেড-টিমের ইনজেকশন প্রচেষ্টার মধ্যে যেগুলো ব্যবস্থার আচরণ বদলায় তার অনুপাত", "সর্বোচ্চ ৫%"],
                ["মানব-মূল্যায়ন", "উপযোগিতা ও সাবলীলতা", "পাইলট ব্যবহারকারী ও বাংলা সম্পাদকদের ৫-পয়েন্ট স্কেলে গড় মূল্যায়ন", "কমপক্ষে ৪.০"],
                ["দক্ষতা", "লেটেন্সি p95", "পাইলট-চাপে অনুসন্ধান ও উত্তরের ৯৫তম পার্সেন্টাইল প্রতিক্রিয়া-সময়", "৩ সেকেন্ড ও ১০ সেকেন্ড"],
                ["নির্ভরযোগ্যতা", "প্রাপ্যতা", "পাইলট চলাকালে কর্মঘণ্টার যে অংশে অনুসন্ধান সেবা চালু থাকে", "কমপক্ষে ৯৯%"],
            ],
        },
        "note": {
            "en": "All values are proposed targets, not measured results. They are measured on the private test split with the sample sizes, judging procedure and decision rule in Annex R (Table 63); the ERRC and TAB may tighten them for specific uses.",
            "bn": "সব মান প্রস্তাবিত লক্ষ্য, পরিমাপকৃত ফলাফল নয়। সংযুক্তি দ-এর (সারণি ৬৩) নমুনার আকার, বিচার-পদ্ধতি ও সিদ্ধান্ত-নিয়ম অনুযায়ী এগুলো ব্যক্তিগত পরীক্ষা-অংশে পরিমাপ করা হয়; নির্দিষ্ট ব্যবহারের জন্য ERRC ও TAB এগুলো আরও কঠোর করতে পারে।",
        },
    },
    # ------------------------------------------------------------------ 10
    {
        "id": "10",
        "widths": [1.7, 1.6, 1.4, 0.9, 2.6, 2.2],
        "title": {
            "en": "Pilot portfolio: users, data, risk tier, scope and exit criteria",
            "bn": "পাইলট পোর্টফোলিও: ব্যবহারকারী, ডেটা, ঝুঁকি-স্তর, পরিসর ও উত্তরণ-মানদণ্ড",
        },
        "cols": {
            "en": ["Pilot", "Primary users", "Data", "Tier", "Minimum viable scope (first 12 months of each pilot)", "Exit criterion"],
            "bn": ["পাইলট", "প্রধান ব্যবহারকারী", "ডেটা", "স্তর", "ন্যূনতম কার্যকর পরিসর (প্রতিটি পাইলটের প্রথম ১২ মাস)", "উত্তরণ-মানদণ্ড"],
        },
        "rows": {
            "en": [
                ["**P1** Bangladesh Policy Search Engine", "Policy analysts, researchers, officials", "Laws, gazettes, plans, budget documents (DC0)", "T1; T2 when used by officials", "Bilingual search with citations over a core corpus of national laws, plans and budget documents", "Recall@10 at least 0.85; answer correctness at least 0.80; citation precision at least 0.95; mean usefulness rating of at least 4.0 of 5 from 30 or more active users"],
                ["**P2** Budget Intelligence Dashboard", "Finance and planning analysts, journalists, researchers", "Published budget documents and ADP (DC0)", "T2 (public dashboard)", "Five fiscal years of ministry-level allocations extracted reproducibly, published as open data by month 12; public dashboard from month 15", "Extraction accuracy at least 99% on a hand-checked sample"],
                ["**P3** Citizen Feedback Analyser", "Owners of public consultations", "Consented, de-identified submissions (DC1, DC2)", "T2", "Topic and sentiment summaries for one public consultation, reported only in aggregate", "DPIA approved; topics validated by people; zero re-identification incidents"],
                ["**P4** Bangla Policy Foundation Model, Stages 0 and 1", "Researchers", "Governed public corpus (DC0)", "T1", "Evaluate existing open models with retrieval; release benchmark BanglaPolicyQA v0", "Benchmark published; Stage 1 go or no-go decision documented"],
                ["**P5** National AI Readiness Observatory", "Policymakers, development partners", "Public indicators and surveys (DC0)", "T2 (public report)", "Indicator framework and first annual report", "First report published with open data"],
                ["**P6** Information-integrity research", "Researchers, fact-checkers", "Public research datasets (DC0)", "T2", "Review and benchmark of Bangla misinformation and synthetic-media detection methods; no monitoring of individuals", "Methods paper published; ERRC approval of research protocol"],
            ],
            "bn": [
                ["**P1** বাংলাদেশ নীতি অনুসন্ধান ইঞ্জিন", "নীতি-বিশ্লেষক, গবেষক, কর্মকর্তা", "আইন, গেজেট, পরিকল্পনা, বাজেট নথি (DC0)", "T1; কর্মকর্তারা ব্যবহার করলে T2", "জাতীয় আইন, পরিকল্পনা ও বাজেট নথির মূল কর্পাসে উদ্ধৃতিসহ দ্বিভাষিক অনুসন্ধান", "Recall@10 কমপক্ষে ০.৮৫; উত্তরের সঠিকতা কমপক্ষে ০.৮০; উদ্ধৃতির নির্ভুলতা কমপক্ষে ০.৯৫; ৩০ বা ততোধিক সক্রিয় ব্যবহারকারীর গড় উপযোগিতা-মূল্যায়ন ৫-এ কমপক্ষে ৪.০"],
                ["**P2** বাজেট ইন্টেলিজেন্স ড্যাশবোর্ড", "অর্থ ও পরিকল্পনা বিশ্লেষক, সাংবাদিক, গবেষক", "প্রকাশিত বাজেট নথি ও এডিপি (DC0)", "T2 (প্রকাশ্য ড্যাশবোর্ড)", "পাঁচ অর্থবছরের মন্ত্রণালয়ভিত্তিক বরাদ্দ পুনরুৎপাদনযোগ্যভাবে নিষ্কাশন ও মাস ১২-এর মধ্যে উন্মুক্ত ডেটা হিসেবে প্রকাশ; মাস ১৫ থেকে প্রকাশ্য ড্যাশবোর্ড", "হাতে-যাচাইকৃত নমুনায় নিষ্কাশনের নির্ভুলতা কমপক্ষে ৯৯%"],
                ["**P3** নাগরিক মতামত বিশ্লেষক", "জন-পরামর্শ পরিচালনাকারী কর্তৃপক্ষ", "সম্মতিপ্রাপ্ত ও পরিচয়-অপসারিত মতামত (DC1, DC2)", "T2", "একটি জন-পরামর্শের বিষয় ও মনোভাবের সারাংশ, শুধু সামষ্টিক আকারে", "DPIA অনুমোদিত; মানুষের দ্বারা যাচাইকৃত বিষয়; পুনঃশনাক্তকরণের কোনো ঘটনা নেই"],
                ["**P4** বাংলা নীতি ফাউন্ডেশন মডেল, পর্যায় ০ ও ১", "গবেষক", "নিয়ন্ত্রিত উন্মুক্ত কর্পাস (DC0)", "T1", "উদ্ধারসহ বিদ্যমান উন্মুক্ত মডেলের মূল্যায়ন; BanglaPolicyQA v0 বেঞ্চমার্ক প্রকাশ", "বেঞ্চমার্ক প্রকাশিত; পর্যায় ১-এর এগোনো বা না-এগোনোর সিদ্ধান্ত নথিভুক্ত"],
                ["**P5** জাতীয় এআই প্রস্তুতি পর্যবেক্ষণকেন্দ্র", "নীতিনির্ধারক, উন্নয়ন সহযোগী", "উন্মুক্ত সূচক ও জরিপ (DC0)", "T2 (প্রকাশ্য প্রতিবেদন)", "সূচক-কাঠামো ও প্রথম বার্ষিক প্রতিবেদন", "উন্মুক্ত ডেটাসহ প্রথম প্রতিবেদন প্রকাশিত"],
                ["**P6** তথ্য-অখণ্ডতা গবেষণা", "গবেষক, তথ্য-যাচাইকারী", "উন্মুক্ত গবেষণা ডেটাসেট (DC0)", "T2", "বাংলা ভুল তথ্য ও কৃত্রিম মিডিয়া শনাক্তকরণ পদ্ধতির পর্যালোচনা ও বেঞ্চমার্ক; কোনো ব্যক্তির ওপর নজরদারি নয়", "পদ্ধতিগত গবেষণাপত্র প্রকাশিত; গবেষণা প্রটোকলে ERRC অনুমোদন"],
            ],
        },
    },
    # ------------------------------------------------------------------ 11
    {
        "id": "11",
        "widths": [2.0, 2.2, 4.0],
        "title": {
            "en": "Security threats specific to AI systems and planned controls",
            "bn": "এআই ব্যবস্থার নির্দিষ্ট নিরাপত্তা হুমকি ও পরিকল্পিত নিয়ন্ত্রণ",
        },
        "cols": {
            "en": ["Threat (OWASP LLM Top 10, 2025)", "Example in BAPIL context", "Planned controls"],
            "bn": ["হুমকি (OWASP LLM Top 10, ২০২৫)", "BAPIL প্রেক্ষাপটে উদাহরণ", "পরিকল্পিত নিয়ন্ত্রণ"],
        },
        "rows": {
            "en": [
                ["LLM01 Prompt injection", "Instructions hidden inside an ingested PDF", "Treat retrieved text as data only; no tool execution; citation-only answering; red-team tests at every G2"],
                ["LLM02 Sensitive information disclosure", "Personal data surfacing in answers", "DC0-first corpus; PII scanning at ingestion; access control per collection; log redaction"],
                ["LLM03 Supply chain", "Compromised model weights or packages", "Pinned dependencies; software bill of materials; model checksums and provenance; signed releases"],
                ["LLM04 Data and model poisoning", "Manipulated documents entering the corpus", "Source allow-list; provenance hashes; change detection; human curation of any fine-tuning data"],
                ["LLM05 Improper output handling", "Model output rendered as active content", "Escape all output; structured-output validation; no direct execution"],
                ["LLM06 Excessive agency", "Tool given authority to act on systems", "Read-only design; no autonomous actions; human approval for any change"],
                ["LLM07 System prompt leakage", "Secrets placed in prompts", "No secrets in prompts; prompts versioned and published where possible"],
                ["LLM08 Vector and embedding weaknesses", "Cross-collection leakage in the index", "Per-collection access control enforced at query time; tenant isolation"],
                ["LLM09 Misinformation", "Confident but wrong answer", "Mandatory citations; abstention; confidence display; user training"],
                ["LLM10 Unbounded consumption", "Query floods driving up compute cost", "Quotas, rate limits, timeouts, cost monitoring"],
            ],
            "bn": [
                ["LLM01 প্রম্পট-ইনজেকশন", "গৃহীত PDF-এর ভেতরে লুকানো নির্দেশনা", "উদ্ধারকৃত টেক্সটকে শুধু ডেটা হিসেবে গণ্য করা; কোনো টুল চালানো নয়; শুধু উদ্ধৃতিভিত্তিক উত্তর; প্রতিটি G2-তে রেড-টিম পরীক্ষা"],
                ["LLM02 সংবেদনশীল তথ্য প্রকাশ", "উত্তরে ব্যক্তিগত তথ্য চলে আসা", "প্রথমে DC0 কর্পাস; গ্রহণের সময় ব্যক্তিগত তথ্য স্ক্যান; সংগ্রহভিত্তিক প্রবেশ নিয়ন্ত্রণ; লগ থেকে তথ্য অপসারণ"],
                ["LLM03 সরবরাহ শৃঙ্খল", "ক্ষতিগ্রস্ত মডেল-ওজন বা প্যাকেজ", "নির্দিষ্ট সংস্করণের নির্ভরতা; সফটওয়্যার উপাদান তালিকা (SBOM); মডেলের চেকসাম ও উৎস-তথ্য; স্বাক্ষরিত রিলিজ"],
                ["LLM04 ডেটা ও মডেল বিষক্রিয়া", "কর্পাসে কারসাজিকৃত নথি প্রবেশ", "অনুমোদিত উৎসের তালিকা; উৎস-হ্যাশ; পরিবর্তন শনাক্তকরণ; ফাইন-টিউনিং ডেটার মানব-বাছাই"],
                ["LLM05 অনুপযুক্ত আউটপুট ব্যবস্থাপনা", "মডেলের আউটপুট সক্রিয় কনটেন্ট হিসেবে প্রদর্শিত", "সকল আউটপুট এস্কেপ করা; কাঠামোবদ্ধ আউটপুট যাচাই; সরাসরি চালনা নয়"],
                ["LLM06 অতিরিক্ত কর্তৃত্ব", "সরঞ্জামকে ব্যবস্থায় পদক্ষেপ নেওয়ার ক্ষমতা দেওয়া", "শুধু-পঠন নকশা; কোনো স্বয়ংক্রিয় পদক্ষেপ নয়; যেকোনো পরিবর্তনে মানব-অনুমোদন"],
                ["LLM07 সিস্টেম প্রম্পট ফাঁস", "প্রম্পটে গোপন তথ্য রাখা", "প্রম্পটে কোনো গোপন তথ্য নয়; প্রম্পট সংস্করণকৃত ও সম্ভব হলে প্রকাশিত"],
                ["LLM08 ভেক্টর ও এমবেডিং দুর্বলতা", "সূচিতে এক সংগ্রহ থেকে অন্য সংগ্রহে তথ্য ফাঁস", "অনুসন্ধানের সময় সংগ্রহভিত্তিক প্রবেশ নিয়ন্ত্রণ; ব্যবহারকারী-গোষ্ঠী পৃথকীকরণ"],
                ["LLM09 ভুল তথ্য", "আত্মবিশ্বাসী কিন্তু ভুল উত্তর", "বাধ্যতামূলক উদ্ধৃতি; বিরত থাকা; আস্থার মাত্রা প্রদর্শন; ব্যবহারকারী প্রশিক্ষণ"],
                ["LLM10 সীমাহীন সম্পদ ব্যবহার", "অনুসন্ধানের বন্যায় কম্পিউটিং ব্যয় বৃদ্ধি", "কোটা, হার-সীমা, সময়সীমা, ব্যয় পর্যবেক্ষণ"],
            ],
        },
    },
]
