# -*- coding: utf-8 -*-
"""Figures added in the expanded edition (new numbering): 02, 05, 06, 13, 14, 15, 16."""

NEW_FIGS = {}

# ---------------------------------------------------------------- Figure 2: stakeholder map
NEW_FIGS["02"] = {
    "tikz": r"""
\begin{tikzpicture}
\def\W{150mm}\def\H{104mm}
\fill[band] (0,0) rectangle (0.5*\W,0.5*\H);
\fill[accentlight!60] (0.5*\W,0) rectangle (\W,0.5*\H);
\fill[band2] (0,0.5*\H) rectangle (0.5*\W,\H);
\fill[accentlight] (0.5*\W,0.5*\H) rectangle (\W,\H);
\draw[ink, line width=0.6pt] (0,0) rectangle (\W,\H);
\draw[ink!50, dashed] (0.5*\W,0) -- (0.5*\W,\H);
\draw[ink!50, dashed] (0,0.5*\H) -- (\W,0.5*\H);
\draw[arr] (0,-6mm) -- node[below=1mm, font=\small]{«interest»} (\W,-6mm);
\draw[arr] (-6mm,0) -- node[above=1mm, font=\small, rotate=90]{«influence»} (-6mm,\H);
\node[font=\small\bfseries, anchor=north west, text=ink!70] at (2mm,\H-2mm) {«q1»};
\node[font=\small\bfseries, anchor=north east, text=accent] at (\W-2mm,\H-2mm) {«q2»};
\node[font=\small\bfseries, anchor=south west, text=ink!70] at (2mm,2mm) {«q3»};
\node[font=\small\bfseries, anchor=south east, text=accent] at (\W-2mm,2mm) {«q4»};
\tikzset{sh/.style={box, rounded corners=7pt, font=\footnotesize, inner sep=2.5pt}, shk/.style={sh, key}}
\node[shk] at (120mm,90mm) {«ict»};
\node[shk] at (104mm,78mm) {«plan»};
\node[shk] at (132mm,73mm) {«fin»};
\node[sh] at (36mm,86mm) {«cab»};
\node[sh] at (44mm,70mm) {«ndma»};
\node[shk] at (98mm,62mm) {«lpad»};
\node[sh] at (128mm,58mm) {«bbs»};
\node[sh] at (90mm,40mm) {«a2i»};
\node[sh] at (36mm,58mm) {«dp»};
\node[sh] at (130mm,42mm) {«uni»};
\node[sh] at (110mm,26mm) {«cso»};
\node[sh] at (60mm,36mm) {«hub»};
\node[sh] at (38mm,22mm) {«ind»};
\node[sh] at (124mm,12mm) {«cit»};
\node[sh] at (70mm,14mm) {«media»};
\end{tikzpicture}""",
    "en": {"interest": "Interest in BAPIL’s work", "influence": "Influence over BAPIL’s success",
           "q1": "Keep satisfied", "q2": "Manage closely", "q3": "Monitor", "q4": "Keep informed and involved",
           "ict": "ICT Division", "plan": "Planning Commission", "fin": "Finance Division", "cab": "Cabinet Division",
           "ndma": "Data Management Authority", "lpad": "Legislative Division", "bbs": "BBS",
           "a2i": "a2i and BCC", "dp": "Development partners", "uni": "Universities", "cso": "Civil society",
           "hub": "AI Hub", "ind": "Industry and startups", "cit": "Citizens", "media": "Media"},
    "bn": {"interest": "BAPIL-এর কাজে আগ্রহ", "influence": "BAPIL-এর সাফল্যে প্রভাব",
           "q1": "সন্তুষ্ট রাখা", "q2": "ঘনিষ্ঠভাবে সম্পৃক্ত রাখা", "q3": "পর্যবেক্ষণ", "q4": "অবহিত ও সম্পৃক্ত রাখা",
           "ict": "আইসিটি বিভাগ", "plan": "পরিকল্পনা কমিশন", "fin": "অর্থ বিভাগ", "cab": "মন্ত্রিপরিষদ বিভাগ",
           "ndma": "উপাত্ত ব্যবস্থাপনা কর্তৃপক্ষ", "lpad": "লেজিসলেটিভ বিভাগ", "bbs": "বিবিএস",
           "a2i": "এটুআই ও বিসিসি", "dp": "উন্নয়ন সহযোগী", "uni": "বিশ্ববিদ্যালয়", "cso": "নাগরিক সমাজ",
           "hub": "এআই হাব", "ind": "শিল্প ও স্টার্টআপ", "cit": "নাগরিক", "media": "সংবাদমাধ্যম"},
}

# ---------------------------------------------------------------- Figure 5: request sequence
NEW_FIGS["05"] = {
    "tikz": r"""
\begin{tikzpicture}
\tikzset{life/.style={box, minimum width=30mm, minimum height=11mm, font=\footnotesize\bfseries},
         msg/.style={->, draw=ink, line width=0.6pt}, ret/.style={->, draw=ink, line width=0.6pt, dashed},
         ml/.style={font=\footnotesize, fill=white, inner sep=1pt}}
\foreach \i/\x/\k in {1/0/u,2/36/g,3/72/s,4/108/a,5/144/l} {
  \node[life] (h\i) at (\x mm,0) {};
  \draw[ink!50, line width=0.5pt, dashed] (\x mm,-6mm) -- (\x mm,-104mm);
}
\node[life] at (h1) {«u»}; \node[life] at (h2) {«g»}; \node[life] at (h3) {«s»};
\node[life] at (h4) {«a»}; \node[life] at (h5) {«l»};
\draw[msg] (0,-14mm) -- node[ml, above]{«m1»} (36mm,-14mm);
\draw[msg] (36mm,-24mm) -- node[ml, above]{«m2»} (144mm,-24mm);
\draw[msg] (36mm,-34mm) -- node[ml, above]{«m3»} (108mm,-34mm);
\draw[msg] (108mm,-44mm) -- node[ml, above]{«m4»} (72mm,-44mm);
\draw[ret] (72mm,-54mm) -- node[ml, above]{«m5»} (108mm,-54mm);
\node[dec, minimum width=30mm] (ev) at (108mm,-66mm) {«m6»};
\node[box, fill=oklight, draw=ok, font=\footnotesize, text width=27mm] at (128mm,-81mm) {«m7»};
\node[box, fill=warnlight, draw=warn, font=\footnotesize, text width=27mm] at (86mm,-81mm) {«m8»};
\draw[msg] (108mm,-93mm) -- node[ml, above]{«m9»} (144mm,-93mm);
\draw[ret] (108mm,-100mm) -- node[ml, above, pos=0.5]{«m10»} (0,-100mm);
\end{tikzpicture}""",
    "en": {"u": "User or portal", "g": "API gateway (C8)", "s": "Search index (C4)", "a": "Answer service (C5)",
           "l": "Audit log (C10)", "m1": "1. Query in Bangla or English", "m2": "2. Authenticate, check role, record request",
           "m3": "3. Forward query", "m4": "4. Normalise, expand, retrieve top passages",
           "m5": "5. Ranked passages with scores", "m6": "6. Evidence\\\\sufficient?",
           "m7": "Yes: extractive answer, one citation per sentence", "m8": "No: abstain, show closest sources and reason",
           "m9": "7. Write hash-chained record", "m10": "8. Answer or abstention, sources, corpus version"},
    "bn": {"u": "ব্যবহারকারী বা পোর্টাল", "g": "API গেটওয়ে (C8)", "s": "অনুসন্ধান সূচি (C4)", "a": "উত্তর সেবা (C5)",
           "l": "নিরীক্ষা লগ (C10)", "m1": "১. বাংলা বা ইংরেজিতে প্রশ্ন", "m2": "২. প্রমাণীকরণ, ভূমিকা যাচাই, অনুরোধ লিপিবদ্ধ",
           "m3": "৩. প্রশ্ন প্রেরণ", "m4": "৪. প্রমিতকরণ, সম্প্রসারণ, শীর্ষ অনুচ্ছেদ উদ্ধার",
           "m5": "৫. স্কোরসহ ক্রমবিন্যস্ত অনুচ্ছেদ", "m6": "৬. প্রমাণ\\\\যথেষ্ট?",
           "m7": "হ্যাঁ: নিষ্কাশনমূলক উত্তর, প্রতি বাক্যে উদ্ধৃতি", "m8": "না: বিরতি, নিকটতম উৎস ও কারণ প্রদর্শন",
           "m9": "৭. হ্যাশ-শৃঙ্খলিত রেকর্ড লিখন", "m10": "৮. উত্তর বা বিরতি, উৎস, কর্পাস সংস্করণ"},
}

# ---------------------------------------------------------------- Figure 6: data lifecycle
NEW_FIGS["06"] = {
    "tikz": r"""
\begin{tikzpicture}
\node[key, circle, minimum size=44mm, text width=38mm, font=\footnotesize] (c) at (0,0) {\textbf{«gov»}\\[1mm]«govsub»};
\tikzset{st/.style={box, minimum width=36mm, minimum height=13mm, text width=33mm, font=\footnotesize}}
\foreach \i/\a in {1/90,2/45,3/0,4/-45,5/-90,6/-135,7/180,8/135} {
  \node[st] (s\i) at (\a:56mm) {};
}
\node[st] at (s1) {\textbf{«s1»}\\«d1»}; \node[st] at (s2) {\textbf{«s2»}\\«d2»};
\node[st] at (s3) {\textbf{«s3»}\\«d3»}; \node[st] at (s4) {\textbf{«s4»}\\«d4»};
\node[st] at (s5) {\textbf{«s5»}\\«d5»}; \node[st] at (s6) {\textbf{«s6»}\\«d6»};
\node[st] at (s7) {\textbf{«s7»}\\«d7»}; \node[st] at (s8) {\textbf{«s8»}\\«d8»};
\foreach \i/\j in {1/2,2/3,3/4,4/5,5/6,6/7,7/8,8/1} \draw[arr] (s\i) -- (s\j);
\foreach \i in {1,...,8} \draw[darr, draw=accent] (c) -- (s\i);
\end{tikzpicture}""",
    "en": {"gov": "Data governance", "govsub": "Steward and custodian roles; classes P0 to P3; quality metrics; audit",
           "s1": "1. Acquire", "d1": "Allow-listed sources; reuse terms",
           "s2": "2. Ingest", "d2": "Extract, OCR, normalise",
           "s3": "3. Classify", "d3": "Data class; DCAT metadata",
           "s4": "4. Store", "d4": "Originals, checksums, versions",
           "s5": "5. Index", "d5": "Passages; lexical and dense",
           "s6": "6. Use", "d6": "Search, answers, analytics",
           "s7": "7. Publish", "d7": "Open data and benchmarks",
           "s8": "8. Retain or dispose", "d8": "Retention schedule; archive"},
    "bn": {"gov": "ডেটা শাসন", "govsub": "স্টুয়ার্ড ও রক্ষকের ভূমিকা; P0 থেকে P3 শ্রেণি; মানের মাপকাঠি; নিরীক্ষা",
           "s1": "১. সংগ্রহ", "d1": "অনুমোদিত উৎস; পুনর্ব্যবহারের শর্ত",
           "s2": "২. গ্রহণ", "d2": "নিষ্কাশন, OCR, প্রমিতকরণ",
           "s3": "৩. শ্রেণিবিন্যাস", "d3": "ডেটা-শ্রেণি; DCAT মেটাডেটা",
           "s4": "৪. সংরক্ষণ", "d4": "মূল নথি, চেকসাম, সংস্করণ",
           "s5": "৫. সূচিকরণ", "d5": "অনুচ্ছেদ; শব্দভিত্তিক ও ঘন",
           "s6": "৬. ব্যবহার", "d6": "অনুসন্ধান, উত্তর, বিশ্লেষণ",
           "s7": "৭. প্রকাশ", "d7": "উন্মুক্ত ডেটা ও বেঞ্চমার্ক",
           "s8": "৮. সংরক্ষণ বা নিষ্পত্তি", "d8": "সংরক্ষণ-সূচি; আর্কাইভ"},
}

# ---------------------------------------------------------------- Figure 13: horizon roadmap
NEW_FIGS["13"] = {
    "tikz": r"""
\begin{tikzpicture}
\def\L{27mm}\def\C{30.5mm}\def\R{17mm}
\tikzset{hd/.style={box, rounded corners=5pt, minimum width=\C-1.5mm, minimum height=13mm, text width=\C-3mm, font=\footnotesize, inner sep=2pt},
         cell/.style={box, rounded corners=4pt, minimum width=\C-1.5mm, minimum height=\R-2mm, text width=\C-4mm, font=\scriptsize, inner sep=1.5pt},
         ln/.style={font=\footnotesize\bfseries, text width=\L-3mm, align=left, anchor=west}}
\foreach \c/\col in {0/ink!10,1/accentlight,2/accent!30,3/accent!45,4/accent!60,5/ink!20} {
  \node[hd, fill=\col] (h\c) at (\L+\c*\C+0.5*\C, 0) {};
}
\node[hd, fill=ink!10] at (h0) {\textbf{«h0»}\\«p0»}; \node[hd, fill=accentlight] at (h1) {\textbf{«h1»}\\«p1»};
\node[hd, fill=accent!30] at (h2) {\textbf{«h2»}\\«p2»}; \node[hd, fill=accent!45] at (h3) {\textbf{«h3»}\\«p3»};
\node[hd, fill=accent!60] at (h4) {\textbf{«h4»}\\«p4»}; \node[hd, fill=ink!20] at (h5) {\textbf{«h5»}\\«p5»};
\draw[arr, line width=1.2pt] (\L,-9.5mm) -- (\L+6*\C+3mm,-9.5mm);
\newcommand{\lane}[8]{%
  \fill[band, rounded corners=4pt] (0,-12mm-#1*\R) rectangle (\L+6*\C,-12mm-#1*\R-\R+0.8mm);
  \node[ln] at (0.5mm,-12mm-#1*\R-0.5*\R) {#2};
  \node[cell] at (\L+0.5*\C,-12mm-#1*\R-0.5*\R) {#3};
  \node[cell] at (\L+1.5*\C,-12mm-#1*\R-0.5*\R) {#4};
  \node[cell] at (\L+2.5*\C,-12mm-#1*\R-0.5*\R) {#5};
  \node[cell] at (\L+3.5*\C,-12mm-#1*\R-0.5*\R) {#6};
  \node[cell] at (\L+4.5*\C,-12mm-#1*\R-0.5*\R) {#7};
  \node[cell] at (\L+5.5*\C,-12mm-#1*\R-0.5*\R) {#8};}
\lane{0}{«l1»}{«a0»}{«a1»}{«a2»}{«a3»}{«a4»}{«a5»}
\lane{1}{«l2»}{«b0»}{«b1»}{«b2»}{«b3»}{«b4»}{«b5»}
\lane{2}{«l3»}{«c0»}{«c1»}{«c2»}{«c3»}{«c4»}{«c5»}
\lane{3}{«l4»}{«d0»}{«d1»}{«d2»}{«d3»}{«d4»}{«d5»}
\lane{4}{«l5»}{«e0»}{«e1»}{«e2»}{«e3»}{«e4»}{«e5»}
\foreach \c/\t in {1/{«r1»},2/{«r2»},3/{«r3»},4/{«r4»}} {
  \node[draw=ink, fill=white, diamond, inner sep=1.6pt] at (\L+\c*\C+0.5*\C-12mm,-12mm-5*\R-4mm) {};
  \node[font=\scriptsize, anchor=west] at (\L+\c*\C+0.5*\C-10mm,-12mm-5*\R-4mm) {\t};
}
\node[font=\scriptsize\bfseries, anchor=west] at (0.5mm,-12mm-5*\R-4mm) {«rev»};
\end{tikzpicture}""",
    "en": {"h0": "H0 Foundation", "p0": "Q4 2026", "h1": "H1 Short term", "p1": "2027 to 2028",
           "h2": "H2 Medium term", "p2": "2029 to 2030", "h3": "H3 Long term", "p3": "2031 to 2035",
           "h4": "H4 Vision", "p4": "2036 to 2041", "h5": "Beyond 2041", "p5": "After 2041",
           "l1": "Institution", "l2": "Platform and data", "l3": "Bangla AI", "l4": "Governance", "l5": "People",
           "a0": "Blueprint published; host selection", "a1": "Lab under MoU; charter; ERRC and TAB",
           "a2": "Multi-year funding; agency service agreements", "a3": "Foundation or statutory centre considered",
           "a4": "Mature national institution", "a5": "Charter renewed or function absorbed",
           "b0": "Reference implementation (v1.1.0)", "b1": "P0 corpus; P1 search; P2 budget data",
           "b2": "G4 adoption by agencies; hybrid search", "b3": "Federated search across ministries",
           "b4": "Evidence services in every policy cycle", "b5": "Adaptive, open services",
           "c0": "Bilingual normalisation and glossary", "c1": "BanglaPolicyQA v0; Stage 0 baselines",
           "c2": "Benchmark v1; Stage 1 if justified", "c3": "Bangla policy model kept as a public good",
           "c4": "Open Bangla resources across domains", "c5": "Continuous renewal",
           "d0": "Tiers, gates and charter designed", "d1": "Register and gates in use",
           "d2": "Blueprint 2.0; national policy alignment", "d3": "Common assurance across government",
           "d4": "Regional and South-South cooperation", "d5": "Periodic independent review",
           "e0": "Briefings for decision-makers", "e1": "300 officials trained; fellows",
           "e2": "1,000 officials trained", "e3": "5,000 trained; regional hubs",
           "e4": "Part of public-service training", "e5": "Lifelong learning",
           "rev": "Reviews", "r1": "2027, 2028", "r2": "2029, 2030", "r3": "2035", "r4": "2041"},
    "bn": {"h0": "H0 ভিত্তি", "p0": "চতুর্থ ত্রৈমাসিক ২০২৬", "h1": "H1 স্বল্পমেয়াদি", "p1": "২০২৭ থেকে ২০২৮",
           "h2": "H2 মধ্যমেয়াদি", "p2": "২০২৯ থেকে ২০৩০", "h3": "H3 দীর্ঘমেয়াদি", "p3": "২০৩১ থেকে ২০৩৫",
           "h4": "H4 রূপকল্প", "p4": "২০৩৬ থেকে ২০৪১", "h5": "২০৪১-এর পরে", "p5": "২০৪১-এর পর",
           "l1": "প্রতিষ্ঠান", "l2": "প্ল্যাটফর্ম ও ডেটা", "l3": "বাংলা এআই", "l4": "শাসন", "l5": "জনবল",
           "a0": "ব্লুপ্রিন্ট প্রকাশ; স্বাগতিক নির্বাচন", "a1": "সমঝোতা স্মারকের অধীনে ল্যাব; সনদ; ERRC ও TAB",
           "a2": "বহুবর্ষী অর্থায়ন; সংস্থার সঙ্গে সেবা-চুক্তি", "a3": "ফাউন্ডেশন বা সংবিধিবদ্ধ কেন্দ্র বিবেচনা",
           "a4": "পরিণত জাতীয় প্রতিষ্ঠান", "a5": "সনদ নবায়ন বা কাজটি সরকারে আত্তীকৃত",
           "b0": "রেফারেন্স বাস্তবায়ন (v1.1.0)", "b1": "P0 কর্পাস; P1 অনুসন্ধান; P2 বাজেট-ডেটা",
           "b2": "সংস্থার G4 গ্রহণ; মিশ্র অনুসন্ধান", "b3": "মন্ত্রণালয়জুড়ে সমন্বিত অনুসন্ধান",
           "b4": "প্রতিটি নীতিচক্রে প্রমাণ-সেবা", "b5": "অভিযোজনক্ষম, উন্মুক্ত সেবা",
           "c0": "দ্বিভাষিক প্রমিতকরণ ও শব্দকোষ", "c1": "BanglaPolicyQA v0; পর্যায় ০ ভিত্তিমান",
           "c2": "বেঞ্চমার্ক v1; যৌক্তিক হলে পর্যায় ১", "c3": "জনসম্পদ হিসেবে বাংলা নীতি মডেল",
           "c4": "বিভিন্ন ক্ষেত্রে উন্মুক্ত বাংলা সম্পদ", "c5": "নিরবচ্ছিন্ন নবায়ন",
           "d0": "স্তর, গেট ও সনদের নকশা", "d1": "নিবন্ধন ও গেট চালু",
           "d2": "ব্লুপ্রিন্ট ২.০; জাতীয় নীতির সঙ্গে সামঞ্জস্য", "d3": "সরকারজুড়ে অভিন্ন আশ্বাস-পদ্ধতি",
           "d4": "আঞ্চলিক ও দক্ষিণ-দক্ষিণ সহযোগিতা", "d5": "পর্যায়ক্রমিক স্বাধীন পর্যালোচনা",
           "e0": "সিদ্ধান্তগ্রহণকারীদের অবহিতকরণ", "e1": "৩০০ কর্মকর্তা প্রশিক্ষিত; ফেলো",
           "e2": "১,০০০ কর্মকর্তা প্রশিক্ষিত", "e3": "৫,০০০ প্রশিক্ষিত; আঞ্চলিক কেন্দ্র",
           "e4": "জনপ্রশাসন প্রশিক্ষণের অংশ", "e5": "আজীবন শিক্ষা",
           "rev": "পর্যালোচনা", "r1": "২০২৭, ২০২৮", "r2": "২০২৯, ২০৩০", "r3": "২০৩৫", "r4": "২০৪১"},
}

# ---------------------------------------------------------------- Figure 14: theory of change
NEW_FIGS["14"] = {
    "tikz": r"""
\begin{tikzpicture}
\tikzset{tc/.style={box, minimum width=31mm, minimum height=50mm, text width=28mm, font=\footnotesize, align=left, anchor=north}}
\foreach \i/\x in {1/0,2/36,3/72,4/108,5/144} \node[tc] (t\i) at (\x mm,0) {};
\node[tc, fill=band] at (t1.north) {\textbf{«t1»}\\[1mm]«x1»};
\node[tc] at (t2.north) {\textbf{«t2»}\\[1mm]«x2»};
\node[tc] at (t3.north) {\textbf{«t3»}\\[1mm]«x3»};
\node[tc, fill=accentlight, draw=accent, line width=0.9pt] at (t4.north) {\textbf{«t4»}\\[1mm]«x4»};
\node[tc, fill=oklight, draw=ok] at (t5.north) {\textbf{«t5»}\\[1mm]«x5»};
\foreach \i/\j in {1/2,2/3,3/4,4/5} \draw[arr, line width=1pt] (t\i.east |- 0,-25mm) -- (t\j.west |- 0,-25mm);
\node[soft, minimum width=175mm, text width=170mm, font=\footnotesize, align=left] (as) at (72mm,-72mm) {\textbf{«as»} «asx»};
\draw[darr] (t5.south) -- ++(0,-8mm) -| node[lbl, pos=0.25]{«loop»} (t1.south);
\end{tikzpicture}""",
    "en": {"t1": "Inputs", "x1": "Core team and fellows\\\\Public documents and data\\\\Shared compute\\\\Funding and MoU",
           "t2": "Activities", "x2": "Build corpus and search\\\\Create benchmark\\\\Run pilots under gates\\\\Train officials",
           "t3": "Outputs", "x3": "P1 search and P2 data\\\\BanglaPolicyQA\\\\Charter, ERRC, register\\\\Trained officials",
           "t4": "Outcomes", "x4": "Faster, cited evidence\\\\Governed, trusted AI\\\\National Bangla AI capacity",
           "t5": "Impact", "x5": "Better grounded public policy\\\\Public trust in public-sector AI",
           "as": "Key assumptions:", "asx": "agencies release staff time; data access is granted; the ERRC stays independent; trained staff remain in post; funding is released on time.",
           "loop": "Evaluation, learning and Blueprint revisions"},
    "bn": {"t1": "উপকরণ", "x1": "মূল দল ও ফেলো\\\\উন্মুক্ত নথি ও ডেটা\\\\যৌথ কম্পিউটিং\\\\অর্থায়ন ও সমঝোতা স্মারক",
           "t2": "কার্যক্রম", "x2": "কর্পাস ও অনুসন্ধান নির্মাণ\\\\বেঞ্চমার্ক তৈরি\\\\গেটের অধীনে পাইলট\\\\কর্মকর্তা প্রশিক্ষণ",
           "t3": "উৎপাদ", "x3": "P1 অনুসন্ধান ও P2 ডেটা\\\\BanglaPolicyQA\\\\সনদ, ERRC, নিবন্ধন\\\\প্রশিক্ষিত কর্মকর্তা",
           "t4": "ফলাফল", "x4": "দ্রুত, উদ্ধৃতিযুক্ত প্রমাণ\\\\নিয়ন্ত্রিত, আস্থাভাজন এআই\\\\জাতীয় বাংলা এআই সক্ষমতা",
           "t5": "প্রভাব", "x5": "প্রমাণে দৃঢ় জননীতি\\\\সরকারি খাতের এআই-তে জন-আস্থা",
           "as": "মূল অনুমান:", "asx": "সংস্থাগুলো কর্মীদের সময় দেয়; ডেটা প্রবেশাধিকার মেলে; ERRC স্বাধীন থাকে; প্রশিক্ষিত কর্মীরা পদে থাকেন; সময়মতো অর্থছাড় হয়।",
           "loop": "মূল্যায়ন, শিক্ষা ও ব্লুপ্রিন্ট সংশোধন"},
}

# ---------------------------------------------------------------- Figure 15: risk heat map
NEW_FIGS["15"] = {
    "tikz": r"""
\begin{tikzpicture}
\def\S{38mm}
\foreach \r/\c/\col in {0/0/oklight,0/1/oklight,0/2/accentlight,1/0/oklight,1/1/accentlight,1/2/warnlight,2/0/accentlight,2/1/warnlight,2/2/warn!45} {
  \fill[\col] (\c*\S,\r*\S) rectangle (\c*\S+\S,\r*\S+\S);
}
\draw[ink, line width=0.6pt, step=\S] (0,0) grid (3*\S,3*\S);
\foreach \c/\t in {0/«lo»,1/«me»,2/«hi»} {
  \node[font=\small] at (\c*\S+0.5*\S,-5mm) {\t};
  \node[font=\small, anchor=east] at (-3mm,\c*\S+0.5*\S) {\t};
}
\node[font=\small\bfseries] at (1.5*\S,-13mm) {«impact»};
\node[font=\small\bfseries, rotate=90] at (-25mm,1.5*\S) {«like»};
\tikzset{rk/.style={draw=ink, fill=white, rounded corners=3pt, font=\footnotesize\bfseries, inner sep=2pt, minimum width=9mm}}
% High likelihood, high impact
\node[rk] at (2*\S+0.3*\S,2*\S+0.65*\S) {R2}; \node[rk] at (2*\S+0.7*\S,2*\S+0.65*\S) {R16};
% High likelihood, medium impact
\node[rk] at (1*\S+0.3*\S,2*\S+0.5*\S) {R3}; \node[rk] at (1*\S+0.7*\S,2*\S+0.5*\S) {R7};
% Medium likelihood, high impact
\node[rk] at (2*\S+0.3*\S,1*\S+0.78*\S) {R1}; \node[rk] at (2*\S+0.7*\S,1*\S+0.78*\S) {R4};
\node[rk] at (2*\S+0.3*\S,1*\S+0.5*\S) {R8}; \node[rk] at (2*\S+0.7*\S,1*\S+0.5*\S) {R11};
\node[rk] at (2*\S+0.3*\S,1*\S+0.22*\S) {R12}; \node[rk] at (2*\S+0.7*\S,1*\S+0.22*\S) {R18};
% Medium likelihood, medium impact
\node[rk] at (1*\S+0.3*\S,1*\S+0.78*\S) {R9}; \node[rk] at (1*\S+0.7*\S,1*\S+0.78*\S) {R10};
\node[rk] at (1*\S+0.3*\S,1*\S+0.5*\S) {R13}; \node[rk] at (1*\S+0.7*\S,1*\S+0.5*\S) {R15};
\node[rk] at (1*\S+0.5*\S,1*\S+0.22*\S) {R17};
% Low likelihood, high impact
\node[rk] at (2*\S+0.3*\S,0.65*\S) {R5}; \node[rk] at (2*\S+0.7*\S,0.65*\S) {R6};
\node[rk] at (2*\S+0.5*\S,0.3*\S) {R14};
\node[font=\footnotesize, text width=42mm, align=left, anchor=north west] at (3*\S+6mm,3*\S) {«legend»};
\end{tikzpicture}""",
    "en": {"lo": "Low", "me": "Medium", "hi": "High", "impact": "Impact", "like": "Likelihood",
           "legend": "\\textbf{Reading the map}\\\\[1mm]Each label is a risk in the register (Table 55).\\\\[1mm]Red cells need active mitigation and quarterly Steering Board attention.\\\\[1mm]Blue cells need named owners and monitoring.\\\\[1mm]Green cells are accepted and reviewed annually."},
    "bn": {"lo": "নিম্ন", "me": "মাঝারি", "hi": "উচ্চ", "impact": "প্রভাব", "like": "সম্ভাবনা",
           "legend": "\\textbf{মানচিত্র পড়ার নিয়ম}\\\\[1mm]প্রতিটি লেবেল নিবন্ধনের (সারণি ৫৫) একটি ঝুঁকি।\\\\[1mm]লাল ঘরে সক্রিয় প্রশমন ও স্টিয়ারিং বোর্ডের ত্রৈমাসিক মনোযোগ প্রয়োজন।\\\\[1mm]নীল ঘরে মনোনীত দায়িত্বপ্রাপ্ত ও পর্যবেক্ষণ প্রয়োজন।\\\\[1mm]সবুজ ঘর গৃহীত এবং বার্ষিক পর্যালোচিত।"},
}

# ---------------------------------------------------------------- Figure 16: integrated pathway (Annex W)
def _fig16_values():
    import budget_model as bm
    fb = bm.funding_by_source()
    posts = bm.stage_posts()
    keys = [k for k, _, _ in bm.STAGES]
    tot = {k: sum(fb[k]) for k in keys}
    colours = ["accent", "accent!45", "ok!55", "warn!45", "ink!30"]
    bars = []
    for c, k in enumerate(keys):
        x0 = 0.0
        for i, v in enumerate(fb[k]):
            w = v / tot[k]
            if w <= 0:
                continue
            bars.append(r"\fill[%s] ($(\L+%d*\C+3mm+%.4f*\C-%.4f*6mm, -12mm-4*\R-0.5*\R-2.6mm)$) rectangle ($(\L+%d*\C+3mm+%.4f*\C-%.4f*6mm, -12mm-4*\R-0.5*\R+2.6mm)$);"
                        % (colours[i], c, x0, x0, c, x0 + w, x0 + w))
            x0 += w
        bars.append(r"\draw[ink, line width=0.4pt] (\L+%d*\C+3mm, -12mm-4*\R-0.5*\R-2.6mm) rectangle (\L+%d*\C+\C-3mm, -12mm-4*\R-0.5*\R+2.6mm);" % (c, c))
    gov = [100 * fb[k][0] / tot[k] for k in keys]
    num = {k: ("%d" % posts[k]) for k in keys}
    money = {k: "%.2f" % bm.crore(tot[k]) for k in keys}
    return "\n".join(bars), gov, num, money


_F16_BARS, _F16_GOV, _F16_POSTS, _F16_MONEY = _fig16_values()
_BN_D = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")

NEW_FIGS["16"] = {
    "tikz": r"""
\begin{tikzpicture}
\def\L{26mm}\def\C{40mm}\def\R{15mm}
\tikzset{hd/.style={box, rounded corners=5pt, minimum width=\C-1.5mm, minimum height=13mm, text width=\C-3mm, font=\footnotesize, inner sep=2pt},
         cell/.style={box, rounded corners=4pt, minimum width=\C-1.5mm, minimum height=\R-2mm, text width=\C-4mm, font=\scriptsize, inner sep=1.5pt},
         ln/.style={font=\footnotesize\bfseries, text width=\L-3mm, align=left, anchor=west}}
\foreach \c/\col in {0/accentlight,1/accent!30,2/accent!45,3/accent!60} {
  \node[hd, fill=\col] (h\c) at (\L+\c*\C+0.5*\C, 0) {};
}
\node[hd, fill=accentlight] at (h0) {\textbf{«h0»}\\«p0»}; \node[hd, fill=accent!30] at (h1) {\textbf{«h1»}\\«p1»};
\node[hd, fill=accent!45] at (h2) {\textbf{«h2»}\\«p2»}; \node[hd, fill=accent!60] at (h3) {\textbf{«h3»}\\«p3»};
\draw[arr, line width=1.2pt] (\L,-9.5mm) -- (\L+4*\C+3mm,-9.5mm);
\newcommand{\lane}[6]{%
  \fill[band, rounded corners=4pt] (0,-12mm-#1*\R) rectangle (\L+4*\C,-12mm-#1*\R-\R+0.8mm);
  \node[ln] at (0.5mm,-12mm-#1*\R-0.5*\R) {#2};
  \node[cell] at (\L+0.5*\C,-12mm-#1*\R-0.5*\R) {#3};
  \node[cell] at (\L+1.5*\C,-12mm-#1*\R-0.5*\R) {#4};
  \node[cell] at (\L+2.5*\C,-12mm-#1*\R-0.5*\R) {#5};
  \node[cell] at (\L+3.5*\C,-12mm-#1*\R-0.5*\R) {#6};}
\lane{0}{«l1»}{«a0»}{«a1»}{«a2»}{«a3»}
\lane{1}{«l2»}{«b0»}{«b1»}{«b2»}{«b3»}
\lane{2}{«l3»}{«c0»}{«c1»}{«c2»}{«c3»}
\lane{3}{«l4»}{«d0»}{«d1»}{«d2»}{«d3»}
\fill[band, rounded corners=4pt] (0,-12mm-4*\R) rectangle (\L+4*\C,-12mm-4*\R-\R+0.8mm);
\node[ln] at (0.5mm,-12mm-4*\R-0.5*\R) {«l5»};
«bars»
\node[cell, draw=none, fill=none] at (\L+3.5*\C,-12mm-4*\R-0.5*\R) {«e3»};
\foreach \c/\t in {1/{«g1»},2/{«g2»},3/{«g3»}} {
  \node[draw=ink, fill=white, diamond, inner sep=1.8pt] at (\L+\c*\C,-12mm-5*\R-3mm) {};
  \node[font=\scriptsize, anchor=north, text width=\C-6mm, align=center] at (\L+\c*\C,-12mm-5*\R-5mm) {\t};
}
\node[font=\scriptsize\bfseries, anchor=west] at (0.5mm,-12mm-5*\R-3mm) {«gates»};
\foreach \i/\col/\t in {0/accent/{«s1»},1/accent!45/{«s2»},2/ok!55/{«s3»},3/warn!45/{«s4»},4/ink!30/{«s5»}} {
  \fill[\col] (\L+\i*0.8*\C,-12mm-5*\R-21mm) rectangle ++(3.2mm,3.2mm);
  \node[font=\scriptsize, anchor=west, text width=0.8*\C-5mm] at (\L+\i*0.8*\C+3.6mm,-12mm-5*\R-19.4mm) {\t};
}
\end{tikzpicture}""",
    "en": {"h0": "Phase 1 pilot", "p0": "Year 1 (2027)", "h1": "Phase 2", "p1": "Years 2 and 3 (2028 to 2029)",
           "h2": "Conditional scale-up", "p2": "Years 4 to 8 (2030 to 2034)", "h3": "Institutionalisation", "p3": "From 2035",
           "l1": "Institutional form", "l2": "Government role", "l3": "Direct posts", "l4": "Budget (Tk crore)", "l5": "Funding mix",
           "a0": "University-anchored lab under MoU; host employs staff", "a1": "Same; ERRC, TAB and register in use",
           "a2": "Multi-year core funding; four divisional nodes", "a3": "Foundation, statutory centre or smaller lab",
           "b0": "ICT Division MoU and Board co-chair; custodians open data", "b1": "Agencies host pilots; G4 adoption decisions",
           "b2": "Agencies own tools, host analysts, sign service agreements", "b3": "Legislation or government decision if statutory",
           "c0": _F16_POSTS["phase1"], "c1": _F16_POSTS["phase2"], "c2": _F16_POSTS["scaleup"] + " by Year 8", "c3": "Set at the 2035 review",
           "d0": _F16_MONEY["phase1"], "d1": _F16_MONEY["phase2"], "d2": _F16_MONEY["scaleup"] + " (not requested now)", "d3": "Set at the 2035 review",
           "bars": _F16_BARS, "e3": "Government share expected to rise further (Table 51)",
           "gates": "Gates", "g1": "Month-12 review and costing study", "g2": "Final evaluation; P1 and P2 pass G4", "g3": "2035 strategic review",
           "s1": "Government", "s2": "Research grants", "s3": "Development partners", "s4": "Agency service agreements", "s5": "Industry and philanthropy"},
    "bn": {"h0": "পর্যায় ১-এর পাইলট", "p0": "বছর ১ (২০২৭)", "h1": "পর্যায় ২", "p1": "বছর ২ ও ৩ (২০২৮ থেকে ২০২৯)",
           "h2": "শর্তসাপেক্ষ সম্প্রসারণ", "p2": "বছর ৪ থেকে ৮ (২০৩০ থেকে ২০৩৪)", "h3": "প্রাতিষ্ঠানিকীকরণ", "p3": "২০৩৫ থেকে",
           "l1": "প্রাতিষ্ঠানিক রূপ", "l2": "সরকারের ভূমিকা", "l3": "প্রত্যক্ষ পদ", "l4": "বাজেট (কোটি টাকা)", "l5": "অর্থায়নের মিশ্রণ",
           "a0": "সমঝোতা স্মারকের অধীনে বিশ্ববিদ্যালয়-ভিত্তিক ল্যাব; স্বাগতিক কর্মী নিয়োগ দেয়", "a1": "একই; ERRC, TAB ও নিবন্ধন চালু",
           "a2": "বহুবর্ষী মূল অর্থায়ন; চারটি বিভাগীয় কেন্দ্র", "a3": "ফাউন্ডেশন, সংবিধিবদ্ধ কেন্দ্র বা ছোট ল্যাব",
           "b0": "আইসিটি বিভাগের সমঝোতা স্মারক ও বোর্ডের সহ-সভাপতি; রক্ষকেরা ডেটা উন্মুক্ত করে", "b1": "সংস্থাগুলো পাইলট ধারণ করে; G4 গ্রহণ-সিদ্ধান্ত",
           "b2": "সংস্থাগুলো সরঞ্জামের মালিক, বিশ্লেষক ধারণ ও সেবা-চুক্তি করে", "b3": "সংবিধিবদ্ধ হলে আইন বা সরকারি সিদ্ধান্ত",
           "c0": _F16_POSTS["phase1"].translate(_BN_D), "c1": _F16_POSTS["phase2"].translate(_BN_D), "c2": "বছর ৮-এর মধ্যে " + _F16_POSTS["scaleup"].translate(_BN_D), "c3": "২০৩৫-এর পর্যালোচনায় নির্ধারিত",
           "d0": _F16_MONEY["phase1"].translate(_BN_D), "d1": _F16_MONEY["phase2"].translate(_BN_D), "d2": _F16_MONEY["scaleup"].translate(_BN_D) + " (এখন অনুরোধকৃত নয়)", "d3": "২০৩৫-এর পর্যালোচনায় নির্ধারিত",
           "bars": _F16_BARS, "e3": "সরকারের অংশ আরও বাড়ার প্রত্যাশা (সারণি ৫১)",
           "gates": "গেট", "g1": "মাস ১২-এর পর্যালোচনা ও ব্যয়-নিরূপণ সমীক্ষা", "g2": "চূড়ান্ত মূল্যায়ন; P1 ও P2 গেট G4 উত্তীর্ণ", "g3": "২০৩৫-এর কৌশলগত পর্যালোচনা",
           "s1": "সরকার", "s2": "গবেষণা অনুদান", "s3": "উন্নয়ন সহযোগী", "s4": "সংস্থার সেবা-চুক্তি", "s5": "শিল্প ও জনহিতৈষী উৎস"},
}
