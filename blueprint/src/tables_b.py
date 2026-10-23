# -*- coding: utf-8 -*-
"""Blueprint tables 12-22 (English and Bangla)."""

TABLES_B = [
    # ------------------------------------------------------------------ 12
    {
        "id": "12",
        "widths": [1.5, 2.4, 3.6, 1.5],
        "title": {
            "en": "Risk tiers and the minimum controls each tier requires",
            "bn": "ঝুঁকি-স্তর এবং প্রতিটি স্তরের ন্যূনতম আবশ্যিক নিয়ন্ত্রণ",
        },
        "cols": {
            "en": ["Tier", "Typical systems", "Minimum required controls", "Who approves"],
            "bn": ["স্তর", "সাধারণ ব্যবস্থা", "ন্যূনতম আবশ্যিক নিয়ন্ত্রণ", "অনুমোদনকারী"],
        },
        "rows": {
            "en": [
                ["**T0** Prohibited", "Social scoring; mass or indiscriminate biometric surveillance; profiling people’s political or religious opinions; deceptive synthetic media of real people; manipulation exploiting vulnerabilities", "Not built, not piloted, not supported by BAPIL under any arrangement", "Excluded by charter"],
                ["**T1** Low", "Research tools and search over public documents; internal dashboards of published data", "AI system record; model or data card; evaluation report; audit logging; public listing in the transparency register", "Unit lead and TAB"],
                ["**T2** Limited", "Advisory tools used by officials; public dashboards, reports and other public-facing information tools; aggregate analysis of de-identified feedback", "All T1 controls plus: ERRC review; red-team test; human review of every output in use (for public dashboards and reports, review of every release); user training; incident procedure; quarterly monitoring report", "ERRC (Steering Board consulted)"],
                ["**T3** High", "Any system that informs decisions about specific people or entities, processes personal data at scale, or is used in enforcement", "BAPIL does not build T3 operational systems. Research only, with: DPIA, legal review, independent audit, ERRC approval, and a published impact assessment", "ERRC (binding) and host-agency legal review"],
            ],
            "bn": [
                ["**T0** নিষিদ্ধ", "সামাজিক স্কোরিং; গণ বা নির্বিচার বায়োমেট্রিক নজরদারি; মানুষের রাজনৈতিক বা ধর্মীয় মতের প্রোফাইলিং; বাস্তব ব্যক্তির প্রতারণামূলক কৃত্রিম মিডিয়া; দুর্বলতাকে কাজে লাগিয়ে প্রভাবিত করা", "কোনো ব্যবস্থাতেই BAPIL এগুলো নির্মাণ, পাইলট বা সমর্থন করে না", "সনদ দ্বারা বর্জিত"],
                ["**T1** নিম্ন", "উন্মুক্ত নথিতে গবেষণা ও অনুসন্ধান সরঞ্জাম; প্রকাশিত ডেটার অভ্যন্তরীণ ড্যাশবোর্ড", "এআই ব্যবস্থার রেকর্ড; মডেল বা ডেটা কার্ড; মূল্যায়ন প্রতিবেদন; নিরীক্ষা লগ; স্বচ্ছতা নিবন্ধনে প্রকাশ্য তালিকাভুক্তি", "ইউনিট প্রধান ও TAB"],
                ["**T2** সীমিত", "কর্মকর্তাদের ব্যবহৃত পরামর্শমূলক সরঞ্জাম; প্রকাশ্য ড্যাশবোর্ড, প্রতিবেদন ও অন্যান্য জনমুখী তথ্য সরঞ্জাম; পরিচয়-অপসারিত মতামতের সামষ্টিক বিশ্লেষণ", "T1-এর সব নিয়ন্ত্রণ এবং: ERRC পর্যালোচনা; রেড-টিম পরীক্ষা; ব্যবহারে প্রতিটি ফলাফলের মানব-পর্যালোচনা (প্রকাশ্য ড্যাশবোর্ড ও প্রতিবেদনের ক্ষেত্রে প্রতিটি সংস্করণের পর্যালোচনা); ব্যবহারকারী প্রশিক্ষণ; ঘটনা-প্রক্রিয়া; ত্রৈমাসিক পর্যবেক্ষণ প্রতিবেদন", "ERRC (স্টিয়ারিং বোর্ডের পরামর্শসহ)"],
                ["**T3** উচ্চ", "নির্দিষ্ট ব্যক্তি বা প্রতিষ্ঠান-সংক্রান্ত সিদ্ধান্তে ভূমিকা রাখে, বৃহৎ পরিসরে ব্যক্তিগত ডেটা প্রক্রিয়া করে বা প্রয়োগকারী কাজে ব্যবহৃত যেকোনো ব্যবস্থা", "BAPIL T3 পরিচালনাগত ব্যবস্থা নির্মাণ করে না। শুধু গবেষণা, এই শর্তে: DPIA, আইনি পর্যালোচনা, স্বাধীন নিরীক্ষা, ERRC অনুমোদন এবং প্রকাশিত প্রভাব মূল্যায়ন", "ERRC (বাধ্যতামূলক) ও স্বাগতিক সংস্থার আইনি পর্যালোচনা"],
            ],
        },
    },
    # ------------------------------------------------------------------ 13
    {
        "id": "13",
        "widths": [1.7, 1.4, 1.6, 1.2, 1.6, 1.5, 1.8],
        "title": {
            "en": "Indicative crosswalk of BAPIL control areas to international and national frameworks",
            "bn": "আন্তর্জাতিক ও জাতীয় কাঠামোর সঙ্গে BAPIL নিয়ন্ত্রণ-ক্ষেত্রের নির্দেশক সংযোগ-সারণি",
        },
        "cols": {
            "en": ["BAPIL control area", "OECD AI Principles", "UNESCO Recommendation", "NIST AI RMF 1.0", "ISO/IEC 42001:2023", "EU AI Act", "Bangladesh (draft policy and Acts)"],
            "bn": ["BAPIL নিয়ন্ত্রণ-ক্ষেত্র", "OECD এআই নীতিমালা", "UNESCO সুপারিশ", "NIST AI RMF 1.0", "ISO/IEC 42001:2023", "ইইউ এআই আইন", "বাংলাদেশ (খসড়া নীতি ও আইন)"],
        },
        "rows": {
            "en": [
                ["Governance and accountability", "1.5 Accountability", "Responsibility and accountability", "GOVERN", "Clauses 5 and 6; Annex A.2, A.3", "Art. 17, Art. 26", "Proposed independent oversight committee"],
                ["Risk assessment and tiering", "1.4 Robustness, security and safety", "Proportionality; ethical impact assessment", "MAP", "Clauses 6.1, 8.2 to 8.4; A.5", "Art. 5, Art. 9, Art. 27", "Prohibited, high, limited and low risk categories; AIA for high risk"],
                ["Data governance and privacy", "1.2 Human rights, incl. privacy", "Privacy and data protection", "MAP, MEASURE", "A.7 Data for AI systems", "Art. 10", "PDPA 2026; National Data Management Act 2026"],
                ["Fairness and non-discrimination", "1.2 Fairness", "Fairness and non-discrimination", "MEASURE", "A.5, A.7", "Art. 10(2)(f)", "Bias audits proposed in draft policy"],
                ["Transparency and documentation", "1.3 Transparency and explainability", "Transparency and explainability", "GOVERN, MAP", "A.6, A.8", "Art. 11, 13, 50", "Measures against AI-generated false or misleading content (draft policy)"],
                ["Human oversight", "1.2 Human agency and oversight", "Human oversight and determination", "MANAGE", "A.9 Use of AI systems", "Art. 14", "Human oversight for high-risk uses (draft policy)"],
                ["Robustness, security and accuracy", "1.4 Robustness, security and safety", "Safety and security", "MEASURE", "A.6 Verification and validation", "Art. 15", "Cyber Security Act 2026 as amended"],
                ["Monitoring and incidents", "1.4, 1.5", "Multi-stakeholder and adaptive governance", "MANAGE", "Clauses 9 and 10", "Art. 72, 73", "Audits by oversight committee (draft policy)"],
                ["Stakeholder engagement and redress", "1.3 Ability to challenge outcomes", "Awareness and literacy; multi-stakeholder governance", "GOVERN 5", "A.8 Information for interested parties", "Art. 85, 86", "Public consultation on the national AI policy"],
            ],
            "bn": [
                ["শাসন ও জবাবদিহি", "১.৫ জবাবদিহি", "দায়িত্ব ও জবাবদিহি", "GOVERN", "অনুচ্ছেদ ৫ ও ৬; পরিশিষ্ট A.2, A.3", "অনু. ১৭, অনু. ২৬", "প্রস্তাবিত স্বাধীন তত্ত্বাবধান কমিটি"],
                ["ঝুঁকি মূল্যায়ন ও স্তরবিন্যাস", "১.৪ দৃঢ়তা, নিরাপত্তা ও সুরক্ষা", "আনুপাতিকতা; নৈতিক প্রভাব মূল্যায়ন", "MAP", "অনুচ্ছেদ ৬.১, ৮.২ থেকে ৮.৪; A.5", "অনু. ৫, ৯, ২৭", "নিষিদ্ধ, উচ্চ, সীমিত ও নিম্ন ঝুঁকির শ্রেণি; উচ্চ ঝুঁকিতে AIA"],
                ["ডেটা শাসন ও গোপনীয়তা", "১.২ মানবাধিকার, গোপনীয়তাসহ", "গোপনীয়তা ও উপাত্ত সুরক্ষা", "MAP, MEASURE", "A.7 এআই ব্যবস্থার ডেটা", "অনু. ১০", "ব্যক্তিগত উপাত্ত সুরক্ষা আইন ২০২৬; জাতীয় উপাত্ত ব্যবস্থাপনা আইন ২০২৬"],
                ["ন্যায্যতা ও বৈষম্যহীনতা", "১.২ ন্যায্যতা", "ন্যায্যতা ও বৈষম্যহীনতা", "MEASURE", "A.5, A.7", "অনু. ১০(২)(চ)", "খসড়া নীতিতে প্রস্তাবিত পক্ষপাত-নিরীক্ষা"],
                ["স্বচ্ছতা ও নথিভুক্তি", "১.৩ স্বচ্ছতা ও ব্যাখ্যাযোগ্যতা", "স্বচ্ছতা ও ব্যাখ্যাযোগ্যতা", "GOVERN, MAP", "A.6, A.8", "অনু. ১১, ১৩, ৫০", "এআই-সৃষ্ট মিথ্যা বা বিভ্রান্তিকর কনটেন্ট প্রতিরোধের ব্যবস্থা (খসড়া নীতি)"],
                ["মানব-তত্ত্বাবধান", "১.২ মানব-কর্তৃত্ব ও তত্ত্বাবধান", "মানব-তত্ত্বাবধান ও নির্ধারণ", "MANAGE", "A.9 এআই ব্যবস্থার ব্যবহার", "অনু. ১৪", "উচ্চ-ঝুঁকিপূর্ণ ব্যবহারে মানব-তত্ত্বাবধান (খসড়া নীতি)"],
                ["দৃঢ়তা, নিরাপত্তা ও নির্ভুলতা", "১.৪ দৃঢ়তা, নিরাপত্তা ও সুরক্ষা", "নিরাপত্তা ও সুরক্ষা", "MEASURE", "A.6 যাচাই ও বৈধকরণ", "অনু. ১৫", "সংশোধিত সাইবার সুরক্ষা আইন ২০২৬"],
                ["পর্যবেক্ষণ ও ঘটনা", "১.৪, ১.৫", "বহু-অংশীজন ও অভিযোজনক্ষম শাসন", "MANAGE", "অনুচ্ছেদ ৯ ও ১০", "অনু. ৭২, ৭৩", "তত্ত্বাবধান কমিটির নিরীক্ষা (খসড়া নীতি)"],
                ["অংশীজন সম্পৃক্ততা ও প্রতিকার", "১.৩ ফলাফল চ্যালেঞ্জের সুযোগ", "সচেতনতা ও সাক্ষরতা; বহু-অংশীজন শাসন", "GOVERN 5", "A.8 আগ্রহী পক্ষের জন্য তথ্য", "অনু. ৮৫, ৮৬", "জাতীয় এআই নীতিতে জন-পরামর্শ"],
            ],
        },
        "note": {
            "en": "Indicative mapping for orientation only; it is not a legal compliance assessment. Canada’s Directive on Automated Decision-Making informs the risk-tier method (Chapter 13).",
            "bn": "শুধু দিকনির্দেশনার জন্য নির্দেশক সংযোগ; এটি আইনি সম্মতি-মূল্যায়ন নয়। কানাডার স্বয়ংক্রিয় সিদ্ধান্তগ্রহণ নির্দেশনা ঝুঁকি-স্তর পদ্ধতিকে প্রভাবিত করেছে (অধ্যায় ১৩)।",
        },
    },
    # ------------------------------------------------------------------ 14
    {
        "id": "14",
        "widths": [1.8, 3.3, 2.5, 2.2],
        "title": {
            "en": "Bangladesh legal and policy instruments relevant to BAPIL (status, October 2026)",
            "bn": "BAPIL-এর সঙ্গে প্রাসঙ্গিক বাংলাদেশের আইন ও নীতি-দলিল (অবস্থা, অক্টোবর ২০২৬)",
        },
        "cols": {
            "en": ["Instrument", "Status", "Relevance", "Blueprint design response"],
            "bn": ["দলিল", "অবস্থা", "প্রাসঙ্গিকতা", "ব্লুপ্রিন্টের নকশাগত সাড়া"],
        },
        "rows": {
            "en": [
                ["Personal Data Protection Act, 2026", "Act No. 63 of 2026, gazetted on 10 April 2026, replacing the Personal Data Protection Ordinance, 2025 [162, 163]. Deemed in force from 6 November 2025, except section 23 (chief data officers) and sections 31 to 35, which come into force by Gazette notification after 18 months [167]. Rules: to be confirmed", "Consent as a clear affirmative indication, with other specified grounds (s. 5); data-subject rights including withdrawal from automated decisions (s. 13); enhanced protection of sensitive and children’s data (s. 7); chief data officers (s. 23); data-residency provisions changed by the 2026 amendment ordinance [115], reportedly limited to critical sectors [122] (whether carried into the Act: to be confirmed)", "DC0-first; DPIA before any DC2 work; DC3 excluded; no automated decisions about individuals; hosting in Bangladesh"],
                ["National Data Management Act, 2026", "Act No. 80 of 2026, gazetted on 10 April 2026, succeeding the National Data Management Ordinance, 2025 (called the National Data Governance Ordinance in some English reports) [84, 162, 164]. Deemed in force from 6 November 2025 [167]. Rules: to be confirmed", "National Data Management Authority (s. 8); National Responsible Data Exchange (NRDEX); a chief data officer in every institution (s. 33); national code repository for government software (s. 23) [167]", "Use NRDEX agreements where available; publish code openly; coordinate with the Authority and agency data officers"],
                ["Cyber Security Act, 2026 and amendment", "Act No. 81 of 2026, gazetted on 10 April 2026, deemed in force from 21 May 2025 [162, 165, 167]. Cyber Security (Amendment) Act, 2026 (Act No. 99), gazetted on 1 July 2026 with immediate effect, omits only section 20, the online gambling provision [123, 166]; it does not concern AI-generated content, contrary to an earlier report [87]. A further amendment under cabinet committee review from July 2026 was still proposed in September 2026 [124, 168]", "National Cyber Security Agency (s. 5); critical information infrastructure; removal and blocking of content, subject to Tribunal approval within three days (s. 8); AI and AI-generated data named in the definitions (s. 2)", "NIST CSF 2.0 controls; incident reporting; information-integrity research kept within law and rights"],
                ["Right to Information Act, 2009", "In force [105]", "Proactive disclosure of public information", "Supports the DC0 corpus and the public transparency register"],
                ["National AI policy", "Draft 2026-2030 released for public consultation in late January 2026 [88, 89]; revised draft (version 2.0, 9 February 2026) posted on the official portal [125]; formulation by a joint team announced to begin in Q4 2026 [91]. Not adopted", "Risk categories; algorithmic impact assessment; an independent oversight committee to be created by an Act of Parliament; Bangla LLM; national compute; AI innovation fund of Tk 200 to 250 crore to 2030 (proposed) [88]", "Tiers aligned to draft categories; Blueprint offered as technical input; BPFM coordinated with national LLM plans"],
                ["Long-term national plans", "Perspective Plan 2021 to 2041 (2020) and the draft ICT Master Plan 2041 [29, 30]", "Long-term digital transformation goals", "Roadmap aligned to the 2041 horizon and adaptable to plan revisions"],
                ["AI Hub and AI skills project (KOICA, ICT Division, Bangladesh Hi-Tech Park Authority)", "Technical assistance project proposal of Tk 192.66 crore awaiting government approval in June 2026 [35]; USD 13 million grant agreement (Record of Discussion) reported signed in August 2026 for 2026 to 2029 [117]. Not reported as operational", "Skills, startups, AI adoption", "Complementary division of labour; shared benchmarks and open data"],
            ],
            "bn": [
                ["ব্যক্তিগত উপাত্ত সুরক্ষা আইন, ২০২৬ (Personal Data Protection Act, 2026)", "২০২৬ সালের ৬৩ নং আইন, ১০ এপ্রিল ২০২৬-এ গেজেটে প্রকাশিত, ব্যক্তিগত উপাত্ত সুরক্ষা অধ্যাদেশ, ২০২৫-এর স্থলাভিষিক্ত [162, 163]। ৬ নভেম্বর ২০২৫ থেকে কার্যকর বলে গণ্য, তবে ধারা ২৩ (প্রধান উপাত্ত কর্মকর্তা) এবং ধারা ৩১ থেকে ৩৫ ১৮ মাস পর গেজেট প্রজ্ঞাপনের মাধ্যমে কার্যকর হবে [167]। বিধিমালা: নিশ্চিত করতে হবে", "সুস্পষ্ট ইতিবাচক নির্দেশনা হিসেবে সম্মতি, সঙ্গে অন্যান্য নির্দিষ্ট ভিত্তি (ধারা ৫); স্বয়ংক্রিয় সিদ্ধান্ত থেকে সরে আসার অধিকারসহ ডেটা-বিষয়ীর অধিকার (ধারা ১৩); সংবেদনশীল ও শিশুদের ডেটার বাড়তি সুরক্ষা (ধারা ৭); প্রধান উপাত্ত কর্মকর্তা (ধারা ২৩); ২০২৬ সালের সংশোধনী অধ্যাদেশে পরিবর্তিত ডেটা দেশে রাখা-সংক্রান্ত বিধান [115], প্রতিবেদন অনুযায়ী গুরুত্বপূর্ণ খাতে সীমিত [122] (আইনে বহাল আছে কি না: নিশ্চিত করতে হবে)", "প্রথমে DC0; যেকোনো DC2 কাজের আগে DPIA; DC3 বর্জিত; ব্যক্তিসংক্রান্ত কোনো স্বয়ংক্রিয় সিদ্ধান্ত নয়; বাংলাদেশে হোস্টিং"],
                ["জাতীয় উপাত্ত ব্যবস্থাপনা আইন, ২০২৬ (National Data Management Act, 2026)", "২০২৬ সালের ৮০ নং আইন, ১০ এপ্রিল ২০২৬-এ গেজেটে প্রকাশিত, জাতীয় উপাত্ত ব্যবস্থাপনা অধ্যাদেশ, ২০২৫-এর (কিছু ইংরেজি প্রতিবেদনে National Data Governance Ordinance নামে উল্লিখিত) স্থলাভিষিক্ত [84, 162, 164]। ৬ নভেম্বর ২০২৫ থেকে কার্যকর বলে গণ্য [167]। বিধিমালা: নিশ্চিত করতে হবে", "জাতীয় উপাত্ত ব্যবস্থাপনা কর্তৃপক্ষ (ধারা ৮); জাতীয় দায়িত্বশীল ডেটা-বিনিময় (NRDEX); প্রত্যেক প্রতিষ্ঠানে একজন প্রধান উপাত্ত কর্মকর্তা (ধারা ৩৩); সরকারি সফটওয়্যারের জাতীয় কোড রিপোজিটরি (ধারা ২৩) [167]", "সম্ভব হলে ডেটা প্রবেশাধিকারে NRDEX চুক্তি ব্যবহার; উন্মুক্তভাবে কোড প্রকাশ; কর্তৃপক্ষ ও সংস্থার ডেটা কর্মকর্তাদের সঙ্গে সমন্বয়"],
                ["সাইবার সুরক্ষা আইন, ২০২৬ ও সংশোধনী", "২০২৬ সালের ৮১ নং আইন, ১০ এপ্রিল ২০২৬-এ গেজেটে প্রকাশিত, ২১ মে ২০২৫ থেকে কার্যকর বলে গণ্য [162, 165, 167]। সাইবার সুরক্ষা (সংশোধন) আইন, ২০২৬ (৯৯ নং আইন), ১ জুলাই ২০২৬-এ গেজেটে প্রকাশিত ও অবিলম্বে কার্যকর, কেবল অনলাইন জুয়া-সংক্রান্ত ধারা ২০ বিলুপ্ত করেছে [123, 166]; এটি এআই-সৃষ্ট কনটেন্ট-সংক্রান্ত নয়, যদিও একটি আগের প্রতিবেদনে তা বলা হয়েছিল [87]। জুলাই ২০২৬ থেকে মন্ত্রিসভা কমিটির পর্যালোচনাধীন আরেকটি সংশোধনী সেপ্টেম্বর ২০২৬-এও প্রস্তাব পর্যায়ে ছিল [124, 168]", "জাতীয় সাইবার সুরক্ষা এজেন্সি (ধারা ৫); গুরুত্বপূর্ণ তথ্য অবকাঠামো; কনটেন্ট অপসারণ ও ব্লক করা, তিন দিনের মধ্যে ট্রাইব্যুনালের অনুমোদন সাপেক্ষে (ধারা ৮); সংজ্ঞায় এআই ও এআই-সৃষ্ট ডেটার উল্লেখ (ধারা ২)", "NIST CSF 2.0 নিয়ন্ত্রণ; ঘটনা প্রতিবেদন; তথ্য-অখণ্ডতা গবেষণা আইন ও অধিকারের সীমার মধ্যে"],
                ["তথ্য অধিকার আইন, ২০০৯", "বলবৎ [105]", "জনগুরুত্বপূর্ণ তথ্যের স্বতঃপ্রণোদিত প্রকাশ", "DC0 কর্পাস ও জনসমক্ষে স্বচ্ছতা নিবন্ধনকে সহায়তা করে"],
                ["জাতীয় এআই নীতি", "খসড়া ২০২৬-২০৩০ জানুয়ারি ২০২৬-এর শেষে জন-পরামর্শের জন্য প্রকাশিত [88, 89]; সংশোধিত খসড়া (সংস্করণ ২.০, ৯ ফেব্রুয়ারি ২০২৬) সরকারি পোর্টালে প্রকাশিত [125]; একটি যৌথ দলের মাধ্যমে ২০২৬-এর চতুর্থ ত্রৈমাসিকে প্রণয়ন শুরুর ঘোষণা [91]। গৃহীত হয়নি", "ঝুঁকির শ্রেণি; অ্যালগরিদমিক প্রভাব মূল্যায়ন; সংসদের আইনের মাধ্যমে গঠিতব্য একটি স্বাধীন তত্ত্বাবধান কমিটি; বাংলা LLM; জাতীয় কম্পিউটিং; ২০৩০ পর্যন্ত ২০০ থেকে ২৫০ কোটি টাকার এআই উদ্ভাবন তহবিল (প্রস্তাবিত) [88]", "খসড়ার শ্রেণির সঙ্গে স্তর সামঞ্জস্যপূর্ণ; ব্লুপ্রিন্ট কারিগরি উপকরণ হিসেবে প্রস্তাবিত; জাতীয় LLM পরিকল্পনার সঙ্গে BPFM সমন্বিত"],
                ["দীর্ঘমেয়াদি জাতীয় পরিকল্পনা", "প্রেক্ষিত পরিকল্পনা ২০২১ থেকে ২০৪১ (২০২০) ও খসড়া আইসিটি মাস্টারপ্ল্যান ২০৪১ [29, 30]", "দীর্ঘমেয়াদি ডিজিটাল রূপান্তরের লক্ষ্য", "২০৪১ দিগন্তের সঙ্গে সামঞ্জস্যপূর্ণ ও পরিকল্পনা সংশোধনের সঙ্গে খাপ খাওয়ানো যায় এমন রোডম্যাপ"],
                ["এআই হাব ও এআই দক্ষতা প্রকল্প (কোইকা, আইসিটি বিভাগ, বাংলাদেশ হাই-টেক পার্ক কর্তৃপক্ষ)", "১৯২.৬৬ কোটি টাকার কারিগরি সহায়তা প্রকল্প প্রস্তাব জুন ২০২৬-এ সরকারি অনুমোদনের অপেক্ষায় ছিল [35]; ২০২৬ থেকে ২০২৯ মেয়াদের জন্য ১৩ মিলিয়ন মার্কিন ডলারের অনুদান-চুক্তি (রেকর্ড অব ডিসকাশন) আগস্ট ২০২৬-এ স্বাক্ষরিত বলে প্রতিবেদিত [117]। চালু হওয়ার কোনো প্রতিবেদন নেই", "দক্ষতা, স্টার্টআপ, এআই গ্রহণ", "পরিপূরক কর্মবিভাজন; যৌথ বেঞ্চমার্ক ও উন্মুক্ত ডেটা"],
            ],
        },
        "note": {
            "en": "Act numbers and Gazette dates are taken from the Legislative Division’s list and from Gazette copies published by the ICT Division; provisions are summarised from the texts in the official laws database and from commentary, checked in October 2026. The Gazette copies could not be read in full by automated means (Annex P), so qualified Bangladesh counsel must confirm the provisions. This table is not legal advice.",
            "bn": "আইনের নম্বর ও গেজেটের তারিখ লেজিসলেটিভ ও সংসদ বিষয়ক বিভাগের তালিকা এবং আইসিটি বিভাগের প্রকাশিত গেজেট-কপি থেকে নেওয়া; বিধানগুলো সরকারি আইন-ডেটাবেসের পাঠ ও ভাষ্য থেকে সংক্ষেপিত, অক্টোবর ২০২৬-এ যাচাইকৃত। গেজেট-কপিগুলো স্বয়ংক্রিয়ভাবে পূর্ণ পড়া যায়নি (সংযুক্তি ত), তাই বিধানগুলো যোগ্য বাংলাদেশি আইনজীবীকে নিশ্চিত করতে হবে। এই সারণি আইনি পরামর্শ নয়।"
        },
    },
    # ------------------------------------------------------------------ 15
    {
        "id": "15",
        "widths": [1.7, 3.6, 1.6, 1.4],
        "title": {
            "en": "Reference implementation modules",
            "bn": "রেফারেন্স বাস্তবায়নের মডিউলসমূহ",
        },
        "cols": {
            "en": ["Module", "What it does", "Requirements", "Tests"],
            "bn": ["মডিউল", "কী করে", "প্রয়োজনীয়তা", "পরীক্ষা"],
        },
        "rows": {
            "en": [
                ["bapil.text", "Unicode normalisation for Bangla, digit folding, light Bangla suffix stripping, bilingual glossary expansion", "FR-01, NFR-01", "test_text"],
                ["bapil.corpus", "Loads Markdown documents, splits them into cited passages, records provenance and SHA-256 checksums", "FR-03", "test_corpus"],
                ["bapil.search", "BM25 index over passages with language-aware tokenisation and cross-lingual query expansion", "FR-01", "test_search"],
                ["bapil.answer", "Extractive answers in which every sentence carries a citation; abstains below an evidence threshold", "FR-02, NFR-08", "test_answer"],
                ["bapil.risk", "Risk-tier questionnaire and scoring rules of Annex B, returning tier, reasons and required controls", "FR-07, GR-02, GR-06", "test_risk"],
                ["bapil.registry", "AI system register validated against a JSON schema; exports the public transparency register", "FR-06, FR-09", "test_registry"],
                ["bapil.evaluate", "Recall@k, MRR and nDCG over a versioned question set; JSON report", "FR-08", "test_evaluate"],
                ["bapil.audit", "Hash-chained, tamper-evident JSONL audit log with verification", "GR-04", "test_audit"],
                ["bapil.api", "Minimal JSON HTTP API (search, answer, risk) on the Python standard library", "FR-10", "test_api"],
                ["bapil.cli", "Command line: index, search, ask, assess, evaluate, register, verify-log", "All", "test_cli"],
            ],
            "bn": [
                ["bapil.text", "বাংলার ইউনিকোড প্রমিতকরণ, অঙ্ক একীকরণ, হালকা বাংলা প্রত্যয় অপসারণ, দ্বিভাষিক শব্দকোষ সম্প্রসারণ", "FR-01, NFR-01", "test_text"],
                ["bapil.corpus", "Markdown নথি লোড, উদ্ধৃতিযোগ্য অনুচ্ছেদে বিভাজন, উৎস-তথ্য ও SHA-256 চেকসাম সংরক্ষণ", "FR-03", "test_corpus"],
                ["bapil.search", "ভাষা-সচেতন টোকেনাইজেশন ও আন্তঃভাষিক প্রশ্ন-সম্প্রসারণসহ অনুচ্ছেদভিত্তিক BM25 সূচি", "FR-01", "test_search"],
                ["bapil.answer", "নিষ্কাশনমূলক উত্তর, যার প্রতিটি বাক্যে উদ্ধৃতি থাকে; প্রমাণ-সীমার নিচে বিরত থাকে", "FR-02, NFR-08", "test_answer"],
                ["bapil.risk", "সংযুক্তি খ-এর ঝুঁকি-স্তর প্রশ্নমালা ও স্কোরিং নিয়ম; স্তর, কারণ ও আবশ্যিক নিয়ন্ত্রণ প্রদান", "FR-07, GR-02, GR-06", "test_risk"],
                ["bapil.registry", "JSON স্কিমায় যাচাইকৃত এআই ব্যবস্থা নিবন্ধন; জনসমক্ষে স্বচ্ছতা নিবন্ধন রপ্তানি", "FR-06, FR-09", "test_registry"],
                ["bapil.evaluate", "সংস্করণকৃত প্রশ্নসেটে Recall@k, MRR ও nDCG; JSON প্রতিবেদন", "FR-08", "test_evaluate"],
                ["bapil.audit", "যাচাই-সুবিধাসহ হ্যাশ-শৃঙ্খলিত, হস্তক্ষেপ-শনাক্তযোগ্য JSONL নিরীক্ষা লগ", "GR-04", "test_audit"],
                ["bapil.api", "Python স্ট্যান্ডার্ড লাইব্রেরিভিত্তিক ন্যূনতম JSON HTTP API (অনুসন্ধান, উত্তর, ঝুঁকি)", "FR-10", "test_api"],
                ["bapil.cli", "কমান্ড লাইন: index, search, ask, assess, evaluate, register, verify-log", "সব", "test_cli"],
            ],
        },
    },
    # ------------------------------------------------------------------ 16
    {
        "id": "16",
        "widths": [0.9, 0.8, 4.0, 2.2, 0.8],
        "title": {
            "en": "Milestones and deliverables over 36 months",
            "bn": "৩৬ মাসের মাইলফলক ও ডেলিভারেবল",
        },
        "cols": {
            "en": ["Milestone", "Month", "Achievement", "Key deliverables", "Gate"],
            "bn": ["মাইলফলক", "মাস", "অর্জন", "প্রধান ডেলিভারেবল", "গেট"],
        },
        "rows": {
            "en": [
                ["MS1", "3", "Director appointed; Steering Board, ERRC and TAB constituted; charter adopted (the MoU and host agreement are in place from month 1)", "D1.1 Charter; D1.2 Risk and ethics procedures", "G0"],
                ["MS2", "6", "Phase 2 work plan and budget updated from the Phase 0 study; DC0 data access confirmed; benchmark protocol agreed", "D1.3 Phase 2 work plan and budget; D1.4 Data access plan", "G1"],
                ["MS3", "9", "P1 Policy Search alpha in internal use; BanglaPolicyQA v0 (500 questions)", "D2.1 P1 alpha; D2.2 Benchmark v0", "G2"],
                ["MS4", "12", "P1 pilot with 30 or more users in two to three agencies; P2 dashboard v1 public; Year 1 report", "D2.3 Pilot report; D2.4 Open budget dataset", "G3"],
                ["MS5", "15", "P3 consultation-analysis pilot after DPIA; P5 observatory framework; P6 research protocol approved by the ERRC", "D3.1 DPIA; D3.2 Observatory framework", "G2 (P3)"],
                ["MS6", "18", "Independent mid-term evaluation; decision on BPFM Stage 1; P3 pilot results", "D3.3 Mid-term evaluation; D3.4 Stage 1 decision", "G3 (P3); review"],
                ["MS7", "24", "Adoption decisions on P1 and P2 with host agencies; first observatory report; P6 methods paper; 300 officials trained", "D3.5 Adoption memos; D3.6 Observatory report 1", "G4"],
                ["MS8", "30", "BPFM Stage 1 model with model card if approved; benchmark v1 (2,000 questions)", "D4.1 Model and model card; D4.2 Benchmark v1", "G2"],
                ["MS9", "36", "Final evaluation; sustainability plan; Blueprint version 2.0", "D4.3 Final evaluation; D4.4 Blueprint 2.0", "Review"],
            ],
            "bn": [
                ["MS1", "৩", "পরিচালক নিয়োগ; স্টিয়ারিং বোর্ড, ERRC ও TAB গঠন; সনদ গ্রহণ (সমঝোতা স্মারক ও স্বাগতিক-চুক্তি মাস ১ থেকে বলবৎ)", "D1.1 সনদ; D1.2 ঝুঁকি ও নৈতিকতা কার্যপ্রণালী", "G0"],
                ["MS2", "৬", "ধাপ ০-এর সমীক্ষার ভিত্তিতে দ্বিতীয় ধাপের কর্মপরিকল্পনা ও বাজেট হালনাগাদ; DC0 ডেটা প্রবেশাধিকার নিশ্চিত; বেঞ্চমার্ক প্রটোকল সম্মত", "D1.3 দ্বিতীয় ধাপের কর্মপরিকল্পনা ও বাজেট; D1.4 ডেটা প্রবেশাধিকার পরিকল্পনা", "G1"],
                ["MS3", "৯", "P1 নীতি অনুসন্ধানের আলফা সংস্করণ অভ্যন্তরীণ ব্যবহারে; BanglaPolicyQA v0 (৫০০ প্রশ্ন)", "D2.1 P1 আলফা; D2.2 বেঞ্চমার্ক v0", "G2"],
                ["MS4", "১২", "দুই থেকে তিনটি সংস্থায় ৩০ বা ততোধিক ব্যবহারকারী নিয়ে P1 পাইলট; P2 ড্যাশবোর্ড v1 প্রকাশ্য; প্রথম বছরের প্রতিবেদন", "D2.3 পাইলট প্রতিবেদন; D2.4 উন্মুক্ত বাজেট ডেটাসেট", "G3"],
                ["MS5", "১৫", "DPIA-র পর P3 পরামর্শ-বিশ্লেষণ পাইলট; P5 পর্যবেক্ষণকেন্দ্রের কাঠামো; ERRC কর্তৃক P6 গবেষণা-প্রটোকল অনুমোদন", "D3.1 DPIA; D3.2 পর্যবেক্ষণকেন্দ্রের কাঠামো", "G2 (P3)"],
                ["MS6", "১৮", "স্বাধীন মধ্যবর্তী মূল্যায়ন; BPFM পর্যায় ১-এর সিদ্ধান্ত; P3 পাইলটের ফলাফল", "D3.3 মধ্যবর্তী মূল্যায়ন; D3.4 পর্যায় ১-এর সিদ্ধান্ত", "G3 (P3); পর্যালোচনা"],
                ["MS7", "২৪", "স্বাগতিক সংস্থার সঙ্গে P1 ও P2 গ্রহণের সিদ্ধান্ত; পর্যবেক্ষণকেন্দ্রের প্রথম প্রতিবেদন; P6-এর পদ্ধতি-প্রবন্ধ; ৩০০ কর্মকর্তা প্রশিক্ষিত", "D3.5 গ্রহণ-স্মারক; D3.6 পর্যবেক্ষণকেন্দ্রের প্রতিবেদন ১", "G4"],
                ["MS8", "৩০", "অনুমোদিত হলে মডেল কার্ডসহ BPFM পর্যায় ১ মডেল; বেঞ্চমার্ক v1 (২,০০০ প্রশ্ন)", "D4.1 মডেল ও মডেল কার্ড; D4.2 বেঞ্চমার্ক v1", "G2"],
                ["MS9", "৩৬", "চূড়ান্ত মূল্যায়ন; টেকসইতা পরিকল্পনা; ব্লুপ্রিন্ট সংস্করণ ২.০", "D4.3 চূড়ান্ত মূল্যায়ন; D4.4 ব্লুপ্রিন্ট ২.০", "পর্যালোচনা"],
            ],
        },
        "note": {
            "en": "Month 1 is the first month in which the MoU, the host agreement and Year 1 funding are all in place (Annex T), after a preparatory Phase 0 of about six months; July 2027, the start of FY2027-28, is the earliest plausible calendar start.",
            "bn": "মাস ১ হলো প্রথম সেই মাস, যখন সমঝোতা স্মারক, স্বাগতিক-চুক্তি ও প্রথম বছরের অর্থায়ন তিনটিই নিশ্চিত (সংযুক্তি ন), প্রায় ছয় মাসের প্রস্তুতিমূলক ধাপ ০-এর পরে; ২০২৭-২৮ অর্থবছরের শুরু, জুলাই ২০২৭, সবচেয়ে আগের সম্ভাব্য সূচনা।",
        },
    },
    # ------------------------------------------------------------------ 17
    {
        "id": "17",
        "widths": [3.6, 1.2, 1.2, 1.2],
        "title": {
            "en": "Indicative core staffing plan (full-time equivalents)",
            "bn": "নির্দেশক মূল জনবল পরিকল্পনা (পূর্ণকালীন সমতুল্য)",
        },
        "cols": {
            "en": ["Role", "Months 1-12", "Months 13-24", "Months 25-36"],
            "bn": ["ভূমিকা", "মাস ১-১২", "মাস ১৩-২৪", "মাস ২৫-৩৬"],
        },
        "rows": {
            "en": [
                ["Director and principal investigator", "1", "1", "1"],
                ["Policy research lead and analysts", "1", "2", "3"],
                ["Machine learning and Bangla NLP engineers", "2", "3", "4"],
                ["Data engineers", "1", "2", "2"],
                ["Software and platform (DevSecOps) engineers", "1", "2", "2"],
                ["Security engineer", "0.5", "1", "1"],
                ["Governance, legal and ethics analysts", "1", "1", "2"],
                ["User experience and accessibility designer", "0.5", "1", "1"],
                ["Programme and partnership coordinator", "1", "1", "1"],
                ["Training and outreach officers", "0", "1", "2"],
                ["**Total core staff**", "**9**", "**15**", "**19**"],
            ],
            "bn": [
                ["পরিচালক ও প্রধান গবেষক", "১", "১", "১"],
                ["নীতি-গবেষণা প্রধান ও বিশ্লেষক", "১", "২", "৩"],
                ["মেশিন লার্নিং ও বাংলা NLP প্রকৌশলী", "২", "৩", "৪"],
                ["ডেটা প্রকৌশলী", "১", "২", "২"],
                ["সফটওয়্যার ও প্ল্যাটফর্ম (DevSecOps) প্রকৌশলী", "১", "২", "২"],
                ["নিরাপত্তা প্রকৌশলী", "০.৫", "১", "১"],
                ["শাসন, আইন ও নৈতিকতা বিশ্লেষক", "১", "১", "২"],
                ["ব্যবহারকারী অভিজ্ঞতা ও প্রবেশযোগ্যতা নকশাকার", "০.৫", "১", "১"],
                ["কর্মসূচি ও অংশীদারিত্ব সমন্বয়ক", "১", "১", "১"],
                ["প্রশিক্ষণ ও প্রচার কর্মকর্তা", "০", "১", "২"],
                ["**মোট মূল জনবল**", "**৯**", "**১৫**", "**১৯**"],
            ],
        },
        "note": {
            "en": "Excludes part-time ERRC members, advisers, visiting fellows and graduate students. Indicative costs are in Table 49; final costs are set by the feasibility study (D1.3).",
            "bn": "খণ্ডকালীন ERRC সদস্য, উপদেষ্টা, অতিথি ফেলো ও স্নাতকোত্তর শিক্ষার্থী অন্তর্ভুক্ত নয়। নির্দেশক ব্যয় সারণি ৪৯-এ; চূড়ান্ত ব্যয় সম্ভাব্যতা সমীক্ষায় (D1.3) নির্ধারিত হবে।",
        },
    },
    # ------------------------------------------------------------------ 18
    {
        "id": "18",
        "widths": [1.2, 3.7, 1.1, 1.2, 1.2],
        "title": {
            "en": "Monitoring and evaluation framework: key performance indicators",
            "bn": "পরিবীক্ষণ ও মূল্যায়ন কাঠামো: মূল কর্মদক্ষতা সূচক",
        },
        "cols": {
            "en": ["Level", "Indicator", "Baseline", "Month 12", "Month 36"],
            "bn": ["স্তর", "সূচক", "ভিত্তিমান", "মাস ১২", "মাস ৩৬"],
        },
        "rows": {
            "en": [
                ["Input", "Core staff in post (FTE)", "0", "9", "19"],
                ["Input", "Public documents indexed with full provenance", "0", "5,000", "25,000"],
                ["Output", "BanglaPolicyQA benchmark questions released", "0", "500", "2,000"],
                ["Output", "User-facing pilots (P1 to P3) that passed Gate G3", "0", "2", "3"],
                ["Output", "Open releases archived with a DOI (including this Blueprint)", "3", "5", "10"],
                ["Output", "Officials trained in responsible AI and the tools", "0", "100", "500"],
                ["Outcome", "Monthly active pilot users", "0", "30", "300"],
                ["Outcome", "Median time saved on evidence search, measured in time-to-evidence studies (Annex R)", "Baseline study", "First measurement", "30%"],
                ["Outcome", "Agencies with signed data or collaboration agreements", "0", "3", "10"],
                ["Quality", "Recall@10 on Bangla and English questions", "Not yet measured", "0.85", "0.90"],
                ["Governance", "Pilots listed in the transparency register with model cards", "Not applicable", "100%", "100%"],
                ["Governance", "Serious incidents (all handled within agreed time limits)", "Not applicable", "0", "0"],
                ["Impact", "Official documents or policy briefs citing BAPIL evidence", "0", "1", "20"],
            ],
            "bn": [
                ["উপকরণ", "কর্মরত মূল জনবল (পূর্ণকালীন সমতুল্য)", "০", "৯", "১৯"],
                ["উপকরণ", "পূর্ণ উৎস-তথ্যসহ সূচিবদ্ধ উন্মুক্ত নথি", "০", "৫,০০০", "২৫,০০০"],
                ["উৎপাদ", "প্রকাশিত BanglaPolicyQA বেঞ্চমার্ক প্রশ্ন", "০", "৫০০", "২,০০০"],
                ["উৎপাদ", "গেট G3 উত্তীর্ণ ব্যবহারকারীমুখী পাইলট (P1 থেকে P3)", "০", "২", "৩"],
                ["উৎপাদ", "DOI-সহ সংরক্ষিত উন্মুক্ত রিলিজ (এই ব্লুপ্রিন্টসহ)", "৩", "৫", "১০"],
                ["উৎপাদ", "দায়িত্বশীল এআই ও সরঞ্জাম বিষয়ে প্রশিক্ষিত কর্মকর্তা", "০", "১০০", "৫০০"],
                ["ফলাফল", "মাসিক সক্রিয় পাইলট ব্যবহারকারী", "০", "৩০", "৩০০"],
                ["ফলাফল", "প্রমাণ অনুসন্ধানে সাশ্রয়কৃত সময়ের মধ্যমা, প্রমাণ-প্রাপ্তির সময় সমীক্ষায় পরিমাপকৃত (সংযুক্তি দ)", "ভিত্তি সমীক্ষা", "প্রথম পরিমাপ", "৩০%"],
                ["ফলাফল", "ডেটা বা সহযোগিতা চুক্তি স্বাক্ষরকারী সংস্থা", "০", "৩", "১০"],
                ["মান", "বাংলা ও ইংরেজি প্রশ্নে Recall@10", "এখনো পরিমাপ হয়নি", "০.৮৫", "০.৯০"],
                ["শাসন", "মডেল কার্ডসহ স্বচ্ছতা নিবন্ধনে তালিকাভুক্ত পাইলট", "প্রযোজ্য নয়", "১০০%", "১০০%"],
                ["শাসন", "গুরুতর ঘটনা (সবগুলো সম্মত সময়সীমায় নিষ্পন্ন)", "প্রযোজ্য নয়", "০", "০"],
                ["প্রভাব", "BAPIL-এর প্রমাণ উদ্ধৃতকারী সরকারি নথি বা নীতি-সংক্ষেপ", "০", "১", "২০"],
            ],
        },
    },
    # ------------------------------------------------------------------ 19
    {
        "id": "19",
        "widths": [0.55, 2.5, 1.0, 0.75, 3.3, 1.4],
        "title": {
            "en": "Risk register",
            "bn": "ঝুঁকি নিবন্ধন",
        },
        "cols": {
            "en": ["ID", "Risk", "Likelihood", "Impact", "Mitigation", "Owner"],
            "bn": ["আইডি", "ঝুঁকি", "সম্ভাবনা", "প্রভাব", "প্রশমন", "দায়িত্বপ্রাপ্ত"],
        },
        "rows": {
            "en": [
                ["R1", "Political or institutional change shifts priorities", "M", "H", "Institution-neutral design; university host; alignment with the national AI policy process; cross-party briefings", "Director, Steering Board"],
                ["R2", "Delays in data access, including bulk document export", "H", "H", "Confirm access in Phase 0; start with documents already public, by assisted manual download where automated retrieval is not permitted and through university law libraries; NRDEX agreements; RTI requests as fallback", "Data lead"],
                ["R3", "Poor text quality from scanned Bangla PDFs", "H", "M", "OCR evaluation; human correction loops; prioritise born-digital sources", "ML lead"],
                ["R4", "Incorrect answers mislead officials", "M", "H", "Extractive-first answers; mandatory citations; abstention; training; classes R and A only", "ML lead, ERRC"],
                ["R5", "Privacy breach or misuse of personal data", "L", "H", "DC0-first; DPIA; access control; independent audits", "Security lead, governance analyst"],
                ["R6", "Mission creep toward surveillance", "L", "H", "T0 list in charter; ERRC veto; public transparency register", "ERRC"],
                ["R7", "Talent shortage or loss of staff", "H", "M", "Fellowships; diaspora partnerships; competitive terms; remote collaboration", "Director"],
                ["R8", "Funding gaps between phases", "M", "H", "Diversified funding (White Paper Appendix C); phased commitments", "Steering Board"],
                ["R9", "Duplication with the AI Hub or other initiatives", "M", "M", "MoU on division of labour; shared benchmarks and data", "Director"],
                ["R10", "Vendor or model lock-in", "M", "M", "Open standards; open-weight models; portable containers; code in national repository", "Platform lead"],
                ["R11", "Cyber attack on the platform", "M", "H", "NIST CSF 2.0 controls; penetration tests; offline backups and restore drills", "Security lead"],
                ["R12", "Low adoption by officials", "M", "H", "Co-design with users; training; measure time saved; product owners in agencies", "Policy lead"],
                ["R13", "Legal uncertainty while implementing rules are issued", "M", "M", "Legal review; conservative data scope; update procedures as rules are published", "Governance analyst"],
            ],
            "bn": [
                ["R1", "রাজনৈতিক বা প্রাতিষ্ঠানিক পরিবর্তনে অগ্রাধিকার বদল", "মা", "উ", "প্রতিষ্ঠান-নিরপেক্ষ নকশা; বিশ্ববিদ্যালয় স্বাগতিক; জাতীয় এআই নীতি প্রক্রিয়ার সঙ্গে সামঞ্জস্য; সর্বদলীয় অবহিতকরণ", "পরিচালক, স্টিয়ারিং বোর্ড"],
                ["R2", "একসঙ্গে নথি রপ্তানিসহ ডেটা প্রবেশাধিকারে বিলম্ব", "উ", "উ", "ধাপ ০-এ প্রবেশাধিকার নিশ্চিত করা; ইতিমধ্যে প্রকাশিত নথি দিয়ে শুরু, স্বয়ংক্রিয় সংগ্রহের অনুমতি না থাকলে সহায়তাপ্রাপ্ত হাতে-করা ডাউনলোড ও বিশ্ববিদ্যালয়ের আইন-গ্রন্থাগারের মাধ্যমে; NRDEX চুক্তি; বিকল্প হিসেবে তথ্য অধিকার আবেদন", "ডেটা প্রধান"],
                ["R3", "স্ক্যানকৃত বাংলা PDF থেকে নিম্নমানের টেক্সট", "উ", "মা", "OCR মূল্যায়ন; মানব-সংশোধন চক্র; জন্মগতভাবে ডিজিটাল উৎসকে অগ্রাধিকার", "ML প্রধান"],
                ["R4", "ভুল উত্তরে কর্মকর্তারা বিভ্রান্ত", "মা", "উ", "নিষ্কাশনমূলক উত্তর আগে; বাধ্যতামূলক উদ্ধৃতি; বিরত থাকা; প্রশিক্ষণ; শুধু R ও A শ্রেণি", "ML প্রধান, ERRC"],
                ["R5", "গোপনীয়তা লঙ্ঘন বা ব্যক্তিগত ডেটার অপব্যবহার", "নি", "উ", "প্রথমে DC0; DPIA; প্রবেশ নিয়ন্ত্রণ; স্বাধীন নিরীক্ষা", "নিরাপত্তা প্রধান, শাসন-বিশ্লেষক"],
                ["R6", "লক্ষ্যচ্যুত হয়ে নজরদারির দিকে যাওয়া", "নি", "উ", "সনদে T0 তালিকা; ERRC-এর ভেটো; জনসমক্ষে স্বচ্ছতা নিবন্ধন", "ERRC"],
                ["R7", "দক্ষ জনবলের ঘাটতি বা কর্মী হারানো", "উ", "মা", "ফেলোশিপ; প্রবাসী অংশীদারিত্ব; প্রতিযোগিতামূলক শর্ত; দূরবর্তী সহযোগিতা", "পরিচালক"],
                ["R8", "ধাপগুলোর মধ্যে অর্থায়নের ঘাটতি", "মা", "উ", "বহুমুখী অর্থায়ন (হোয়াইট পেপার পরিশিষ্ট গ); ধাপভিত্তিক প্রতিশ্রুতি", "স্টিয়ারিং বোর্ড"],
                ["R9", "এআই হাব বা অন্য উদ্যোগের সঙ্গে দ্বৈততা", "মা", "মা", "কর্মবিভাজন বিষয়ে সমঝোতা স্মারক; যৌথ বেঞ্চমার্ক ও ডেটা", "পরিচালক"],
                ["R10", "বিক্রেতা বা মডেলের উপর আটকে পড়া", "মা", "মা", "উন্মুক্ত মানদণ্ড; উন্মুক্ত-ওজন মডেল; বহনযোগ্য কন্টেইনার; জাতীয় ভান্ডারে কোড", "প্ল্যাটফর্ম প্রধান"],
                ["R11", "প্ল্যাটফর্মে সাইবার আক্রমণ", "মা", "উ", "NIST CSF 2.0 নিয়ন্ত্রণ; অনুপ্রবেশ পরীক্ষা; অফলাইন ব্যাকআপ ও পুনরুদ্ধার মহড়া", "নিরাপত্তা প্রধান"],
                ["R12", "কর্মকর্তাদের মধ্যে কম গ্রহণযোগ্যতা", "মা", "উ", "ব্যবহারকারীর সঙ্গে সহ-নকশা; প্রশিক্ষণ; সাশ্রয়কৃত সময় পরিমাপ; সংস্থায় প্রোডাক্ট ওনার", "নীতি প্রধান"],
                ["R13", "বাস্তবায়ন বিধিমালা জারির সময় আইনি অনিশ্চয়তা", "মা", "মা", "আইনি পর্যালোচনা; রক্ষণশীল ডেটা পরিসর; বিধিমালা প্রকাশের সঙ্গে কার্যপ্রণালী হালনাগাদ", "শাসন-বিশ্লেষক"],
            ],
        },
        "note": {
            "en": "L = low, M = medium, H = high. The register is reviewed quarterly by the Steering Board. Early-warning indicators, contingencies, residual ratings and review frequencies are given in Annex U (Table 67).",
            "bn": "নি = নিম্ন, মা = মাঝারি, উ = উচ্চ। স্টিয়ারিং বোর্ড প্রতি ত্রৈমাসিকে নিবন্ধনটি পর্যালোচনা করে। আগাম সতর্কসংকেত, বিকল্প ব্যবস্থা, অবশিষ্ট মাত্রা ও পর্যালোচনার পুনরাবৃত্তি সংযুক্তি প-তে (সারণি ৬৭) দেওয়া আছে।",
        },
    },
    # ------------------------------------------------------------------ 20
    {
        "id": "20",
        "widths": [0.6, 4.4, 2.4, 1.3],
        "title": {
            "en": "Decisions requested from the relevant authorities",
            "bn": "সংশ্লিষ্ট কর্তৃপক্ষের কাছে প্রত্যাশিত সিদ্ধান্ত",
        },
        "cols": {
            "en": ["No.", "Decision", "Responsible authority", "Timing"],
            "bn": ["নং", "সিদ্ধান্ত", "দায়িত্বপ্রাপ্ত কর্তৃপক্ষ", "সময়"],
        },
        "rows": {
            "en": [
                ["D1", "Accept this Blueprint as a technical input to the national AI policy drafting process", "Ministry of Posts, Telecommunications and Information Technology (ICT Division)", "Q4 2026"],
                ["D2", "After Phase 0: approve the 12-month Phase 1 pilot, agree an MoU with the selected host institution, and commit Year 1 funding (about Tk 4.7 crore, Table 50, as confirmed by the Phase 0 costing study)", "ICT Division and host institution", "End of Phase 0"],
                ["D3", "Authorise structured bulk access to already-public document collections and nominate data custodians", "Legislative and Parliamentary Affairs Division, Finance Division, Planning Commission, BBS, a2i", "During Phase 0"],
                ["D4", "Nominate Steering Board members, and agree that ERRC members are selected through an open call by an independent nominations panel", "ICT Division and host institution (Steering Board); independent panel (ERRC)", "During Phase 0"],
                ["D5", "Fund and commission Phase 0 (about Tk 0.44 crore, about six months): an open host call, an independent legal review, an independent feasibility and costing study, and confirmation of data access; name a government focal point", "ICT Division or a development partner", "Within 90 days"],
                ["D6", "Confirm guardrails: no deployment beyond class A without a G4 decision, and no use in prohibited categories", "Steering Board", "At charter adoption"],
            ],
            "bn": [
                ["D1", "জাতীয় এআই নীতি প্রণয়ন-প্রক্রিয়ায় এই ব্লুপ্রিন্টকে কারিগরি উপকরণ হিসেবে গ্রহণ", "ডাক, টেলিযোগাযোগ ও তথ্যপ্রযুক্তি মন্ত্রণালয় (আইসিটি বিভাগ)", "২০২৬-এর চতুর্থ ত্রৈমাসিক"],
                ["D2", "ধাপ ০-এর পর: ১২ মাসের প্রথম ধাপের পাইলট অনুমোদন, নির্বাচিত স্বাগতিক প্রতিষ্ঠানের সঙ্গে সমঝোতা স্মারক এবং প্রথম বছরের অর্থের (প্রায় ৪.৭ কোটি টাকা, সারণি ৫০, ধাপ ০-এর ব্যয়-নিরূপণ সমীক্ষায় নিশ্চিত) প্রতিশ্রুতি", "আইসিটি বিভাগ ও স্বাগতিক প্রতিষ্ঠান", "ধাপ ০-এর শেষে"],
                ["D3", "ইতিমধ্যে প্রকাশিত নথিসংগ্রহে কাঠামোবদ্ধভাবে একসঙ্গে প্রবেশাধিকার অনুমোদন ও ডেটা-রক্ষক মনোনয়ন", "লেজিসলেটিভ ও সংসদ বিষয়ক বিভাগ, অর্থ বিভাগ, পরিকল্পনা কমিশন, বিবিএস, এটুআই", "ধাপ ০ চলাকালে"],
                ["D4", "স্টিয়ারিং বোর্ডে সদস্য মনোনয়ন, এবং একটি স্বাধীন মনোনয়ন প্যানেলের উন্মুক্ত আহ্বানের মাধ্যমে ERRC সদস্য বাছাইয়ে সম্মতি", "আইসিটি বিভাগ ও স্বাগতিক প্রতিষ্ঠান (স্টিয়ারিং বোর্ড); স্বাধীন প্যানেল (ERRC)", "ধাপ ০ চলাকালে"],
                ["D5", "ধাপ ০-এর অর্থায়ন ও নির্দেশ (প্রায় ০.৪৪ কোটি টাকা, প্রায় ছয় মাস): স্বাগতিকের উন্মুক্ত আহ্বান, স্বাধীন আইনি পর্যালোচনা, স্বাধীন সম্ভাব্যতা ও ব্যয়-নিরূপণ সমীক্ষা এবং ডেটা প্রবেশাধিকার নিশ্চিতকরণ; সরকারি ফোকাল পয়েন্ট মনোনয়ন", "আইসিটি বিভাগ বা কোনো উন্নয়ন সহযোগী", "৯০ দিনের মধ্যে"],
                ["D6", "সুরক্ষাসীমা নিশ্চিত করা: G4 সিদ্ধান্ত ছাড়া A শ্রেণির বাইরে কোনো প্রয়োগ নয় এবং নিষিদ্ধ শ্রেণিতে কোনো ব্যবহার নয়", "স্টিয়ারিং বোর্ড", "সনদ গ্রহণের সময়"],
            ],
        },
        "note": {
            "en": "In time, D1 and D5 come first; D3 and D4 are prepared during Phase 0; D2 follows Phase 0 and D6 the adoption of the charter. None of these decisions creates a statutory body or gives BAPIL legal powers. The approvals and agreements needed before month 1 are listed in Annex T (Table 65).",
            "bn": "সময়ের ক্রমে প্রথমে D1 ও D5; ধাপ ০ চলাকালে D3 ও D4 প্রস্তুত হয়; ধাপ ০-এর পরে D2 এবং সনদ গ্রহণের সময় D6। এসব সিদ্ধান্তের কোনোটিই কোনো সংবিধিবদ্ধ সংস্থা সৃষ্টি করে না বা BAPIL-কে আইনি ক্ষমতা দেয় না। মাস ১-এর আগে প্রয়োজনীয় অনুমোদন ও চুক্তির তালিকা সংযুক্তি ন-তে (সারণি ৬৫) দেওয়া আছে।",
        },
    },
    # ------------------------------------------------------------------ 21
    {
        "id": "21",
        "widths": [1.0, 3.0, 1.0, 1.9, 1.6],
        "title": {
            "en": "Requirements traceability matrix",
            "bn": "প্রয়োজনীয়তা অনুসরণযোগ্যতা ম্যাট্রিক্স",
        },
        "cols": {
            "en": ["Requirement", "Summary", "Component", "Code module", "Verification"],
            "bn": ["প্রয়োজনীয়তা", "সারাংশ", "উপাদান", "কোড মডিউল", "যাচাই"],
        },
        "rows": {
            "en": [
                ["FR-01", "Bilingual search", "C2, C4", "bapil.text, bapil.search", "test_text, test_search"],
                ["FR-02", "Cited answers and abstention", "C5", "bapil.answer", "test_answer"],
                ["FR-03", "Provenance at ingestion", "C2, C3", "bapil.corpus", "test_corpus"],
                ["FR-04", "Dashboards", "C6, C7", "Specified only", "Pilot P2 acceptance"],
                ["FR-05", "Aggregate feedback analysis", "C6", "Specified only", "Pilot P3 DPIA and acceptance"],
                ["FR-06", "AI system register", "C12", "bapil.registry", "test_registry"],
                ["FR-07", "Risk-tier assessment", "C12", "bapil.risk", "test_risk"],
                ["FR-08", "Evaluation harness", "C11", "bapil.evaluate", "test_evaluate"],
                ["FR-09", "Transparency register", "C12", "bapil.registry (export)", "test_registry"],
                ["FR-10", "Versioned API", "C8", "bapil.api", "test_api"],
                ["NFR-01", "Language parity", "C2, C4", "bapil.text glossary and normaliser", "test_text; benchmark"],
                ["NFR-07", "Reproducibility", "All", "CI workflow; no external dependencies", "GitHub Actions"],
                ["NFR-08", "Explainability", "C5", "bapil.answer (sources and scores)", "test_answer"],
                ["GR-02", "Gate before build", "C12", "bapil.risk", "test_risk"],
                ["GR-04", "Tamper-evident logs", "C10", "bapil.audit", "test_audit"],
                ["GR-06", "Prohibited uses", "C12", "bapil.risk (T0 screen)", "test_risk"],
            ],
            "bn": [
                ["FR-01", "দ্বিভাষিক অনুসন্ধান", "C2, C4", "bapil.text, bapil.search", "test_text, test_search"],
                ["FR-02", "উদ্ধৃতিসহ উত্তর ও বিরত থাকা", "C5", "bapil.answer", "test_answer"],
                ["FR-03", "গ্রহণের সময় উৎস-তথ্য", "C2, C3", "bapil.corpus", "test_corpus"],
                ["FR-04", "ড্যাশবোর্ড", "C6, C7", "শুধু বিনির্দেশিত", "পাইলট P2 গ্রহণ"],
                ["FR-05", "সামষ্টিক মতামত বিশ্লেষণ", "C6", "শুধু বিনির্দেশিত", "পাইলট P3-এর DPIA ও গ্রহণ"],
                ["FR-06", "এআই ব্যবস্থা নিবন্ধন", "C12", "bapil.registry", "test_registry"],
                ["FR-07", "ঝুঁকি-স্তর মূল্যায়ন", "C12", "bapil.risk", "test_risk"],
                ["FR-08", "মূল্যায়ন কাঠামো", "C11", "bapil.evaluate", "test_evaluate"],
                ["FR-09", "স্বচ্ছতা নিবন্ধন", "C12", "bapil.registry (রপ্তানি)", "test_registry"],
                ["FR-10", "সংস্করণকৃত API", "C8", "bapil.api", "test_api"],
                ["NFR-01", "ভাষাগত সমতা", "C2, C4", "bapil.text শব্দকোষ ও প্রমিতকারী", "test_text; বেঞ্চমার্ক"],
                ["NFR-07", "পুনরুৎপাদনযোগ্যতা", "সব", "CI ওয়ার্কফ্লো; বাহ্যিক নির্ভরতা নেই", "GitHub Actions"],
                ["NFR-08", "ব্যাখ্যাযোগ্যতা", "C5", "bapil.answer (উৎস ও স্কোর)", "test_answer"],
                ["GR-02", "নির্মাণের আগে গেট", "C12", "bapil.risk", "test_risk"],
                ["GR-04", "হস্তক্ষেপ-শনাক্তযোগ্য লগ", "C10", "bapil.audit", "test_audit"],
                ["GR-06", "নিষিদ্ধ ব্যবহার", "C12", "bapil.risk (T0 যাচাই)", "test_risk"],
            ],
        },
    },
    # ------------------------------------------------------------------ 22
    {
        "id": "22",
        "widths": [0.6, 1.9, 1.5, 1.5, 1.5, 1.5],
        "title": {
            "en": "Risk-tier questionnaire: scored dimensions (Annex B)",
            "bn": "ঝুঁকি-স্তর প্রশ্নমালা: স্কোরযুক্ত মাত্রা (সংযুক্তি খ)",
        },
        "cols": {
            "en": ["Code", "Dimension", "Score 0", "Score 1", "Score 2", "Score 3"],
            "bn": ["কোড", "মাত্রা", "স্কোর ০", "স্কোর ১", "স্কোর ২", "স্কোর ৩"],
        },
        "rows": {
            "en": [
                ["D1", "Influence on decisions", "Research only", "Informs analysts", "Informs official decisions on policies or programmes", "Informs or automates decisions about specific people or entities"],
                ["D2", "Data sensitivity", "DC0 public", "DC1 internal, non-personal", "DC2 personal", "DC3 sensitive personal or restricted"],
                ["D3", "People potentially affected", "None or internal", "Fewer than 10,000", "10,000 to 1 million", "More than 1 million"],
                ["D4", "Reversibility of harm", "Trivially reversible", "Reversible with effort", "Hard to reverse", "Irreversible"],
                ["D5", "Degree of automation", "Suggestions on request", "Person reviews every output", "Person reviews samples", "Fully automated"],
                ["D6", "Vulnerability of affected groups", "No affected individuals", "General public", "Includes vulnerable groups", "Targets vulnerable groups"],
                ["D7", "Exposure", "Internal researchers", "Officials", "Public information", "Public guidance with consequences"],
            ],
            "bn": [
                ["D1", "সিদ্ধান্তে প্রভাব", "শুধু গবেষণা", "বিশ্লেষককে তথ্য দেয়", "নীতি বা কর্মসূচি-সংক্রান্ত সরকারি সিদ্ধান্তে তথ্য দেয়", "নির্দিষ্ট ব্যক্তি বা প্রতিষ্ঠান-সংক্রান্ত সিদ্ধান্তে তথ্য দেয় বা স্বয়ংক্রিয় করে"],
                ["D2", "ডেটার সংবেদনশীলতা", "DC0 উন্মুক্ত", "DC1 অভ্যন্তরীণ, ব্যক্তিগত নয়", "DC2 ব্যক্তিগত", "DC3 সংবেদনশীল ব্যক্তিগত বা সংরক্ষিত"],
                ["D3", "সম্ভাব্য প্রভাবিত মানুষ", "কেউ নয় বা অভ্যন্তরীণ", "১০,০০০-এর কম", "১০,০০০ থেকে ১০ লক্ষ", "১০ লক্ষের বেশি"],
                ["D4", "ক্ষতির প্রত্যাবর্তনযোগ্যতা", "সহজেই প্রত্যাবর্তনযোগ্য", "চেষ্টায় প্রত্যাবর্তনযোগ্য", "প্রত্যাবর্তন কঠিন", "অপ্রত্যাবর্তনযোগ্য"],
                ["D5", "স্বয়ংক্রিয়তার মাত্রা", "অনুরোধে পরামর্শ", "প্রতিটি ফলাফল মানুষ পর্যালোচনা করেন", "নমুনা মানুষ পর্যালোচনা করেন", "সম্পূর্ণ স্বয়ংক্রিয়"],
                ["D6", "প্রভাবিত গোষ্ঠীর ঝুঁকিপ্রবণতা", "কোনো প্রভাবিত ব্যক্তি নেই", "সাধারণ জনগণ", "ঝুঁকিপূর্ণ গোষ্ঠী অন্তর্ভুক্ত", "ঝুঁকিপূর্ণ গোষ্ঠীকে লক্ষ্য করে"],
                ["D7", "উন্মুক্ততা", "অভ্যন্তরীণ গবেষক", "কর্মকর্তা", "জনসাধারণের জন্য তথ্য", "পরিণামসহ জনসাধারণের জন্য নির্দেশনা"],
            ],
        },
        "note": {
            "en": "Tier rules: any prohibited-use flag gives T0. Otherwise T3 if total at least 13, or D1 = 3, or D2 = 3, or both D2 and D3 at least 2; T2 if total at least 6, or D1 = 2, or D7 at least 2; else T1. Implemented in bapil.risk.",
            "bn": "স্তর-নিয়ম: কোনো নিষিদ্ধ ব্যবহার চিহ্ন থাকলে T0। অন্যথায় মোট স্কোর কমপক্ষে ১৩, বা D1 = ৩, বা D2 = ৩, বা D2 ও D3 উভয়ই কমপক্ষে ২ হলে T3; মোট কমপক্ষে ৬, বা D1 = ২, বা D7 কমপক্ষে ২ হলে T2; অন্যথায় T1। bapil.risk-এ বাস্তবায়িত।",
        },
    },
]
