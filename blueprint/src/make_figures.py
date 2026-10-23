#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Blueprint figures (TikZ) in English and Bangla, then compile to PDF and PNG.

Outputs: blueprint/figures/blueprint_figNN[_bn].{tex,pdf,png}
Each figure is a single TikZ layout with «label» placeholders filled per language,
so both language versions share identical geometry.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "figures")

PRE_EN = r"""\documentclass[border=8pt]{standalone}
\usepackage{fontspec}
\setmainfont{TeX Gyre Heros}[Ligatures=TeXOff]
\XeTeXgenerateactualtext=1
\setsansfont{TeX Gyre Heros}
"""
PRE_BN = r"""\documentclass[border=8pt]{standalone}
\usepackage{fontspec}
\setmainfont{Noto Sans}[Ligatures=TeXOff]
\XeTeXgenerateactualtext=1
\setsansfont{Noto Sans}
\newfontfamily\bengalifont{Noto Sans Bengali}[Script=Bengali, NFSSFamily=bnfam]
\usepackage[Latin,Bengali]{ucharclasses}
% group-free font switching (as in header-common.tex): robust inside braces, cells and quotes
\makeatletter
\def\BN@saved{\rmdefault}
\def\BN@bn{bnfam}
\newcommand\BNin{\edef\BN@tmp{\f@family}\ifx\BN@tmp\BN@bn\else\let\BN@saved\BN@tmp\fi\fontfamily{bnfam}\selectfont}
\newcommand\BNout{\fontfamily{\BN@saved}\selectfont}
\makeatother
\setTransitionsFor{Bengali}{\BNin}{\BNout}
% Typographic quotes and dashes are not in a ucharclasses class (class 0), so a Bangla word right
% after “ or ‘ would not trigger the Bangla font. Treat them as Latin so that every switch fires.
\XeTeXcharclass"2018=\XeTeXcharclass`A
\XeTeXcharclass"2019=\XeTeXcharclass`A
\XeTeXcharclass"201C=\XeTeXcharclass`A
\XeTeXcharclass"201D=\XeTeXcharclass`A
\XeTeXcharclass"2013=\XeTeXcharclass`A
\XeTeXcharclass"2014=\XeTeXcharclass`A
\XeTeXcharclass"2026=\XeTeXcharclass`A
\usepackage{newunicodechar}
\newunicodechar{।}{{\bengalifont\char"0964}}
"""
COMMON = r"""\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,shapes.geometric,shapes.misc,shapes.symbols,fit,backgrounds,calc,chains}
\definecolor{ink}{HTML}{111827}
\definecolor{band}{HTML}{F3F4F6}
\definecolor{band2}{HTML}{E5E7EB}
\definecolor{accent}{HTML}{1D4ED8}
\definecolor{accentlight}{HTML}{DBEAFE}
\definecolor{warn}{HTML}{B91C1C}
\definecolor{warnlight}{HTML}{FEE2E2}
\definecolor{ok}{HTML}{047857}
\definecolor{oklight}{HTML}{D1FAE5}
\tikzset{
  >={Stealth[length=2.6mm]},
  box/.style={draw=ink, line width=0.6pt, rounded corners=9pt, fill=white, align=center,
              inner sep=4pt, font=\small},
  pill/.style={box, rounded corners=13pt},
  key/.style={box, fill=accentlight, draw=accent, line width=0.9pt},
  soft/.style={box, fill=band},
  dec/.style={draw=ink, line width=0.6pt, diamond, aspect=2.2, align=center, inner sep=1.5pt,
              font=\footnotesize, fill=white},
  arr/.style={->, draw=ink, line width=0.6pt},
  darr/.style={->, draw=ink, line width=0.6pt, dashed},
  lbl/.style={font=\footnotesize, fill=white, inner sep=1.5pt},
  layer/.style={draw=band2, fill=band, rounded corners=6pt},
  title/.style={font=\bfseries\small, align=left, anchor=west},
}
"""

FIGS = {}

# ---------------------------------------------------------------- Figure 1
FIGS["01"] = {
    "tikz": r"""
\begin{tikzpicture}[node distance=7mm and 9mm]
\node[pill, minimum width=46mm, minimum height=15mm] (wp) {\textbf{«wp»}\\«v10»\\{\footnotesize DOI 10.5281/zenodo.21363967}};
\node[pill, minimum width=46mm, minimum height=15mm, right=12mm of wp] (es) {\textbf{«es»}\\«v10»\\{\footnotesize DOI 10.5281/zenodo.21441172}};
\node[key, rounded corners=13pt, minimum width=46mm, minimum height=15mm, right=12mm of es] (bp) {\textbf{«bp»}\\«v10»\\{\footnotesize «newdoi»}};
\draw[arr] (wp) -- (es);
\draw[arr] (es) -- (bp);
\node[box, minimum width=40mm, minimum height=11mm, below=14mm of bp.south, xshift=-32mm] (sum) {«sum»};
\node[key, minimum width=40mm, minimum height=11mm, below=14mm of bp.south, xshift=32mm] (code) {«code»};
\foreach \n in {sum,code} \draw[arr] (bp.south) -- (\n.north);
\node[soft, minimum width=150mm, minimum height=11mm, below=12mm of sum, xshift=32mm] (pilots) {«pilots»};
\foreach \n in {sum,code} \draw[arr] (\n.south) -- (\n.south |- pilots.north);
\node[box, minimum width=88mm, minimum height=11mm, below=9mm of pilots] (eval) {«eval»};
\draw[arr] (pilots) -- (eval);
\node[box, dashed, minimum width=40mm, minimum height=10mm, left=10mm of eval] (zen) {«zenodo»};
\node[box, dashed, minimum width=40mm, minimum height=10mm, right=10mm of eval] (gh) {«github»};
\draw[darr] (eval) -- (zen);
\draw[darr] (eval) -- (gh);
\end{tikzpicture}""",
    "en": {"wp": "White Paper", "es": "Executive Summary", "bp": "Technical Blueprint", "v10": "Version 1.0",
           "newdoi": "DOI: new Zenodo record", "sum": "Blueprint Summary",
           "code": "Reference implementation\\\\(GitHub repository)",
           "pilots": "Controlled pilots P1 to P6 under the gates G0 to G4",
           "eval": "Independent evaluation and adoption decisions",
           "zenodo": "Archived on Zenodo", "github": "Versioned on GitHub"},
    "bn": {"wp": "হোয়াইট পেপার", "es": "নির্বাহী সারসংক্ষেপ", "bp": "টেকনিক্যাল ব্লুপ্রিন্ট", "v10": "সংস্করণ ১.০",
           "newdoi": "DOI: নতুন Zenodo রেকর্ড", "sum": "ব্লুপ্রিন্ট সারসংক্ষেপ",
           "code": "রেফারেন্স বাস্তবায়ন\\\\(গিটহাব রিপোজিটরি)",
           "pilots": "গেট G0 থেকে G4-এর অধীনে নিয়ন্ত্রিত পাইলট P1 থেকে P6",
           "eval": "স্বাধীন মূল্যায়ন ও গ্রহণের সিদ্ধান্ত",
           "zenodo": "Zenodo-তে সংরক্ষিত", "github": "গিটহাবে সংস্করণকৃত"},
}

# ---------------------------------------------------------------- Figure 2
FIGS["02"] = {
    "tikz": r"""
\begin{tikzpicture}[node distance=8mm and 8mm]
\node[soft, minimum width=40mm, minimum height=11mm] (gov) at (-35mm,0) {«gov»};
\node[soft, minimum width=40mm, minimum height=11mm] (host) at (35mm,0) {«host»};
\node[key, minimum width=62mm, minimum height=13mm] (sb) at (0,-22mm) {\textbf{«sb»}\\{\footnotesize «sbsub»}};
\draw[arr] (gov.south) |- node[lbl, pos=0.3]{«mou»} (sb.west);
\draw[arr] (host.south) |- (sb.east);
\node[pill, minimum width=46mm, minimum height=12mm] (dir) at (0,-48mm) {\textbf{«dir»}};
\draw[arr] (sb) -- (dir);
\node[box, draw=warn, fill=warnlight, minimum width=44mm, minimum height=14mm, font=\small\bfseries] (errc) at (-66mm,-48mm) {«errc»\\{\footnotesize\mdseries «errcsub»}};
\node[box, dashed, minimum width=44mm, minimum height=14mm, font=\small\bfseries] (iap) at (66mm,-48mm) {«iap»\\{\footnotesize\mdseries «iapsub»}};
\draw[arr, draw=warn] (errc) -- node[lbl, below=1mm, text=warn, font=\scriptsize]{«veto»} (dir);
\draw[darr] (iap) -- (dir);
\node[box, minimum width=44mm, minimum height=10mm] (tab) at (66mm,-66mm) {«tab»};
\draw[arr] (dir.south east) ++(-4mm,0) |- (tab.west);
\tikzset{unit/.style={box, minimum width=24mm, minimum height=13mm, font=\footnotesize}}
\foreach \i/\x in {1/-67.5,2/-40.5,3/-13.5,4/13.5,5/40.5,6/67.5} \node[unit] (u\i) at (\x mm,-90mm) {};
\node[unit] at (u1) {«u1»}; \node[unit] at (u2) {«u2»}; \node[unit] at (u3) {«u3»};
\node[unit] at (u4) {«u4»}; \node[unit] at (u5) {«u5»}; \node[unit] at (u6) {«u6»};
\draw[ink, line width=0.6pt] (dir.south) -- (0,-76mm) coordinate (bus);
\draw[ink, line width=0.6pt] (-67.5mm,-76mm) -- (67.5mm,-76mm);
\foreach \i in {1,...,6} \draw[arr] (u\i.north |- bus) -- (u\i.north);
\node[key, minimum width=159mm, minimum height=9mm] (plat) at (0,-107mm) {«plat»};
\node[soft, minimum width=159mm, minimum height=10mm] (agency) at (0,-127mm) {«agency»};
\draw[arr, <->] (plat) -- node[lbl, right=1mm]{«codesign»} (agency);
\end{tikzpicture}""",
    "en": {"gov": "Government (ICT Division)", "host": "Host institution", "mou": "MoU",
           "sb": "Steering Board", "sbsub": "strategy, plan, budget, joint G4 decisions",
           "errc": "Ethics and Risk\\\\Review Committee", "errcsub": "independent; binding veto",
           "iap": "International\\\\Advisory Panel", "iapsub": "peer review; advisory only",
           "dir": "BAPIL Director", "veto": "review and veto", "tab": "Technical Architecture Board",
           "u1": "Policy and\\\\Research", "u2": "Data Analytics\\\\and Sentiment", "u3": "Digital Security\\\\and Integrity",
           "u4": "Governance\\\\and Ethics", "u5": "Education\\\\and Talent", "u6": "Innovation and\\\\Startups",
           "plat": "Platform engineering team (shared data, search, security and evaluation services)",
           "agency": "Host-agency product owners and pilot users in ministries and agencies",
           "codesign": "co-design"},
    "bn": {"gov": "সরকার (আইসিটি বিভাগ)", "host": "স্বাগতিক প্রতিষ্ঠান", "mou": "সমঝোতা স্মারক",
           "sb": "স্টিয়ারিং বোর্ড", "sbsub": "কৌশল, পরিকল্পনা, বাজেট, যৌথ G4 সিদ্ধান্ত",
           "errc": "নৈতিকতা ও ঝুঁকি\\\\পর্যালোচনা কমিটি", "errcsub": "স্বাধীন; বাধ্যতামূলক ভেটো",
           "iap": "আন্তর্জাতিক\\\\উপদেষ্টা প্যানেল", "iapsub": "সমকক্ষ পর্যালোচনা; শুধু পরামর্শ",
           "dir": "BAPIL পরিচালক", "veto": "পর্যালোচনা ও ভেটো", "tab": "কারিগরি স্থাপত্য বোর্ড",
           "u1": "নীতি ও\\\\গবেষণা", "u2": "ডেটা বিশ্লেষণ\\\\ও মতামত", "u3": "ডিজিটাল নিরাপত্তা\\\\ও অখণ্ডতা",
           "u4": "শাসন ও\\\\নৈতিকতা", "u5": "শিক্ষা ও\\\\মেধা", "u6": "উদ্ভাবন ও\\\\স্টার্টআপ",
           "plat": "প্ল্যাটফর্ম প্রকৌশল দল (যৌথ ডেটা, অনুসন্ধান, নিরাপত্তা ও মূল্যায়ন সেবা)",
           "agency": "মন্ত্রণালয় ও সংস্থার প্রোডাক্ট ওনার এবং পাইলট ব্যবহারকারী",
           "codesign": "সহ-নকশা"},
}

# ---------------------------------------------------------------- Figure 3
FIGS["03"] = {
    "tikz": r"""
\begin{tikzpicture}
\def\W{128mm}
% layer bands
\foreach \y/\t in {0/«l5»,-21/«l4»,-42/«l3»,-63/«l2»,-84/«l1»} {
  \fill[band, rounded corners=6pt] (0,\y mm) rectangle (\W,\y mm-17mm);
  \node[title, font=\bfseries\footnotesize] at (2mm,\y mm-2.8mm) {\t};
}
\tikzset{cell/.style={box, minimum height=9mm, font=\footnotesize, inner sep=2pt}}
% users
\node[cell, minimum width=29mm] at (17mm,-10mm) {«u1»};
\node[cell, minimum width=29mm] at (48mm,-10mm) {«u2»};
\node[cell, minimum width=29mm] at (79mm,-10mm) {«u3»};
\node[cell, minimum width=29mm] at (110mm,-10mm) {«u4»};
% experience
\node[cell, minimum width=60mm] (c7) at (33mm,-31mm) {«c7»};
\node[cell, minimum width=60mm] (c8) at (95mm,-31mm) {«c8»};
% intelligence
\node[key, cell, minimum width=29mm] (c4) at (17mm,-52mm) {«c4»};
\node[key, cell, minimum width=29mm] (c5) at (48mm,-52mm) {«c5»};
\node[cell, minimum width=29mm] (c6) at (79mm,-52mm) {«c6»};
\node[cell, minimum width=29mm] (c11) at (110mm,-52mm) {«c11»};
% data
\node[cell, minimum width=39mm] (c1) at (22mm,-73mm) {«c1»};
\node[cell, minimum width=39mm] (c2) at (64mm,-73mm) {«c2»};
\node[cell, minimum width=39mm] (c3) at (106mm,-73mm) {«c3»};
% sources
\node[cell, minimum width=29mm] (s1) at (17mm,-94mm) {«s1»};
\node[cell, minimum width=29mm] (s2) at (48mm,-94mm) {«s2»};
\node[cell, minimum width=29mm] (s3) at (79mm,-94mm) {«s3»};
\node[cell, minimum width=29mm] (s4) at (110mm,-94mm) {«s4»};
% flow arrows
\draw[arr] (64mm,-84mm) -- (64mm,-80mm);
\draw[arr] (c1) -- (c2); \draw[arr] (c2) -- (c3);
\draw[arr] (64mm,-63mm) -- (64mm,-59mm);
\draw[arr] (64mm,-42mm) -- (64mm,-38mm);
\draw[arr] (64mm,-21mm) -- (64mm,-17mm);
% governance column
\fill[accentlight, rounded corners=6pt] (\W+5mm,0) rectangle (\W+42mm,-101mm);
\node[title, font=\bfseries\footnotesize, align=center, anchor=north, text width=35mm] at (\W+23.5mm,-2mm) {«gtitle»};
\tikzset{gcell/.style={box, draw=accent, minimum width=33mm, minimum height=14mm, font=\footnotesize, text width=30mm}}
\node[gcell] at (\W+23.5mm,-24mm) {«c9»};
\node[gcell] at (\W+23.5mm,-44mm) {«c10»};
\node[gcell] at (\W+23.5mm,-64mm) {«c12»};
\node[gcell] at (\W+23.5mm,-86mm) {«gates»};
\draw[darr, <->, draw=accent] (\W+1mm,-50mm) -- (\W+6.5mm,-50mm);
\end{tikzpicture}""",
    "en": {"l5": "Users", "l4": "Experience", "l3": "Intelligence", "l2": "Data", "l1": "Sources (public first)",
           "u1": "Policymakers", "u2": "Analysts, researchers", "u3": "Agencies", "u4": "Public",
           "c7": "C7 Portal and dashboards (Bangla, English)", "c8": "C8 API gateway (versioned)",
           "c4": "C4 Search index\\\\BM25 + dense", "c5": "C5 Answer service\\\\cite or abstain",
           "c6": "C6 Analytics engine", "c11": "C11 Model registry\\\\and evaluation",
           "c1": "C1 Source connectors", "c2": "C2 Ingestion and\\\\normalisation, OCR", "c3": "C3 Document store\\\\and catalogue",
           "s1": "Laws, gazettes", "s2": "Budgets, plans", "s3": "Statistics, open data", "s4": "Consented feedback",
           "gtitle": "Governance and security (cross-cutting)",
           "c9": "C9 Identity and access (SSO, roles, MFA)", "c10": "C10 Audit and observability (hash-chained logs)",
           "c12": "C12 Governance workbench (register, risk tiers)", "gates": "Gates G0 to G5\\\\ERRC and TAB reviews"},
    "bn": {"l5": "ব্যবহারকারী", "l4": "অভিজ্ঞতা স্তর", "l3": "বুদ্ধিমত্তা স্তর", "l2": "ডেটা স্তর", "l1": "উৎস (প্রথমে উন্মুক্ত)",
           "u1": "নীতিনির্ধারক", "u2": "বিশ্লেষক, গবেষক", "u3": "সরকারি সংস্থা", "u4": "জনসাধারণ",
           "c7": "C7 পোর্টাল ও ড্যাশবোর্ড (বাংলা, ইংরেজি)", "c8": "C8 API গেটওয়ে (সংস্করণকৃত)",
           "c4": "C4 অনুসন্ধান সূচি\\\\BM25 + ঘন ভেক্টর", "c5": "C5 উত্তর সেবা\\\\উদ্ধৃতি বা বিরতি",
           "c6": "C6 বিশ্লেষণ ইঞ্জিন", "c11": "C11 মডেল রেজিস্ট্রি\\\\ও মূল্যায়ন",
           "c1": "C1 উৎস সংযোগকারী", "c2": "C2 গ্রহণ ও প্রমিতকরণ,\\\\OCR", "c3": "C3 নথি সংরক্ষণাগার\\\\ও ক্যাটালগ",
           "s1": "আইন, গেজেট", "s2": "বাজেট, পরিকল্পনা", "s3": "পরিসংখ্যান, উন্মুক্ত ডেটা", "s4": "সম্মতিপ্রাপ্ত মতামত",
           "gtitle": "শাসন ও নিরাপত্তা (সর্বস্তরীয়)",
           "c9": "C9 পরিচয় ও প্রবেশাধিকার (SSO, ভূমিকা, MFA)", "c10": "C10 নিরীক্ষা ও পর্যবেক্ষণ (হ্যাশ-শৃঙ্খলিত লগ)",
           "c12": "C12 শাসন কর্মক্ষেত্র (নিবন্ধন, ঝুঁকি-স্তর)", "gates": "গেট G0 থেকে G5\\\\ERRC ও TAB পর্যালোচনা"},
}

# ---------------------------------------------------------------- Figure 4
FIGS["04"] = {
    "tikz": r"""
\begin{tikzpicture}[node distance=6mm and 6mm]
\tikzset{st/.style={box, minimum width=31mm, minimum height=15mm, font=\footnotesize, text width=28mm}}
\node[pill, minimum width=31mm, minimum height=15mm, font=\footnotesize, text width=28mm] (q) {\textbf{«q»}};
\node[st, right=of q] (n) {\textbf{«n»}\\«nsub»};
\node[st, right=of n] (e) {\textbf{«e»}\\«esub»};
\node[st, right=of e] (r) {\textbf{«r»}\\«rsub»};
\node[st, below=12mm of r] (k) {\textbf{«k»}\\«ksub»};
\node[dec, left=10mm of k, text width=24mm] (d) {«d»};
\node[key, minimum width=31mm, minimum height=15mm, font=\footnotesize, text width=28mm, below=12mm of d] (a) {\textbf{«a»}\\«asub»};
\node[box, draw=warn, fill=warnlight, minimum width=31mm, minimum height=15mm, font=\footnotesize, text width=28mm, left=12mm of d] (x) {\textbf{«x»}\\«xsub»};
\node[st, right=of a] (h) {\textbf{«h»}\\«hsub»};
\node[soft, minimum width=31mm, minimum height=15mm, font=\footnotesize, text width=28mm, right=of h] (l) {\textbf{«l»}\\«lsub»};
\draw[arr] (q) -- (n); \draw[arr] (n) -- (e); \draw[arr] (e) -- (r); \draw[arr] (r) -- (k);
\draw[arr] (k) -- (d);
\draw[arr] (d) -- node[lbl, right]{«yes»} (a);
\draw[arr] (d) -- node[lbl, above]{«no»} (x);
\draw[arr] (a) -- (h); \draw[arr] (h) -- (l);
\draw[arr] (x.south) |- ($(l.south)+(0,-6mm)$) -- (l.south);
\end{tikzpicture}""",
    "en": {"q": "Question in Bangla or English", "n": "Normalise", "nsub": "Unicode NFC, digits, light suffix stripping",
           "e": "Expand", "esub": "bilingual glossary, spelling variants",
           "r": "Retrieve", "rsub": "BM25 and dense vectors, top-k passages",
           "k": "Check evidence", "ksub": "score threshold, passage coverage",
           "d": "Enough evidence?", "yes": "yes", "no": "no",
           "a": "Answer with citations", "asub": "every sentence linked to a passage",
           "x": "Abstain", "xsub": "show closest sources, say why",
           "h": "Human review", "hsub": "required in class A use",
           "l": "Audit log", "lsub": "query, sources, output, hash chain"},
    "bn": {"q": "বাংলা বা ইংরেজিতে প্রশ্ন", "n": "প্রমিতকরণ", "nsub": "ইউনিকোড NFC, অঙ্ক, হালকা প্রত্যয় অপসারণ",
           "e": "সম্প্রসারণ", "esub": "দ্বিভাষিক শব্দকোষ, বানানভেদ",
           "r": "উদ্ধার", "rsub": "BM25 ও ঘন ভেক্টর, শীর্ষ অনুচ্ছেদ",
           "k": "প্রমাণ যাচাই", "ksub": "স্কোর-সীমা, অনুচ্ছেদের ব্যাপ্তি",
           "d": "যথেষ্ট প্রমাণ?", "yes": "হ্যাঁ", "no": "না",
           "a": "উদ্ধৃতিসহ উত্তর", "asub": "প্রতিটি বাক্য একটি অনুচ্ছেদের সঙ্গে যুক্ত",
           "x": "বিরত থাকা", "xsub": "নিকটতম উৎস দেখানো, কারণ জানানো",
           "h": "মানব-পর্যালোচনা", "hsub": "A শ্রেণির ব্যবহারে আবশ্যিক",
           "l": "নিরীক্ষা লগ", "lsub": "প্রশ্ন, উৎস, ফলাফল, হ্যাশ শৃঙ্খল"},
}

# ---------------------------------------------------------------- Figure 5
FIGS["05"] = {
    "tikz": r"""
\begin{tikzpicture}
\tikzset{stage/.style={box, minimum width=96mm, minimum height=17mm, text width=92mm, font=\footnotesize},
         gate/.style={dec, aspect=3.2, text width=44mm, font=\footnotesize}}
\node[key, stage] (s0) at (0,0) {\textbf{«s0»} \quad «s0t»\\[1mm]«s0b»};
\node[gate] (g1) at (0,-25mm) {«g1»};
\node[stage] (s1) at (0,-50mm) {\textbf{«s1»} \quad «s1t»\\[1mm]«s1b»};
\node[gate] (g2) at (0,-75mm) {«g2»};
\node[stage] (s2) at (0,-100mm) {\textbf{«s2»} \quad «s2t»\\[1mm]«s2b»};
\draw[arr] (s0) -- (g1);
\draw[arr] (g1) -- node[lbl, right]{«yes»} (s1);
\draw[arr] (s1) -- (g2);
\draw[arr] (g2) -- node[lbl, right]{«yes»} (s2);
\node[box, dashed, font=\footnotesize, text width=34mm] (st1) at (74mm,-25mm) {«stay»};
\node[box, dashed, font=\footnotesize, text width=34mm] (st2) at (74mm,-75mm) {«stay»};
\draw[darr] (g1) -- (st1); \draw[darr] (g2) -- (st2);
\node[soft, minimum width=150mm, text width=146mm, minimum height=9mm, font=\footnotesize] at (14mm,-120mm) {«base»};
\end{tikzpicture}""",
    "en": {"s0": "Stage 0", "s0t": "months 1 to 12",
           "s0b": "Retrieval over existing open models; no training; BanglaPolicyQA v0",
           "g1": "Gap above threshold, data and compute ready?",
           "s1": "Stage 1", "s1t": "months 13 to 30",
           "s1b": "Domain adaptation (LoRA) on governed public corpus; instruction tuning; model card",
           "g2": "Material gain and safety tests passed?",
           "s2": "Stage 2", "s2t": "after month 30, only if justified",
           "s2b": "Continued pre-training on shared national compute; independent audit",
           "yes": "yes", "stay": "no: remain at current stage",
           "base": "Every stage: open benchmark, evaluation report, ERRC review, release archived with a DOI"},
    "bn": {"s0": "পর্যায় ০", "s0t": "মাস ১ থেকে ১২",
           "s0b": "বিদ্যমান উন্মুক্ত মডেলে উদ্ধারভিত্তিক ব্যবস্থা; কোনো প্রশিক্ষণ নয়; BanglaPolicyQA v0",
           "g1": "ঘাটতি সীমার ওপরে, ডেটা ও কম্পিউটিং প্রস্তুত?",
           "s1": "পর্যায় ১", "s1t": "মাস ১৩ থেকে ৩০",
           "s1b": "নিয়ন্ত্রিত উন্মুক্ত কর্পাসে ডোমেইন অভিযোজন (LoRA); নির্দেশনা-টিউনিং; মডেল কার্ড",
           "g2": "উল্লেখযোগ্য উন্নতি ও নিরাপত্তা পরীক্ষা উত্তীর্ণ?",
           "s2": "পর্যায় ২", "s2t": "মাস ৩০-এর পর, শুধু যৌক্তিক হলে",
           "s2b": "যৌথ জাতীয় কম্পিউটিংয়ে অব্যাহত প্রাক-প্রশিক্ষণ; স্বাধীন নিরীক্ষা",
           "yes": "হ্যাঁ", "stay": "না: বর্তমান পর্যায়ে থাকা",
           "base": "প্রতিটি পর্যায়: উন্মুক্ত বেঞ্চমার্ক, মূল্যায়ন প্রতিবেদন, ERRC পর্যালোচনা, DOI-সহ সংরক্ষিত রিলিজ"},
}

# ---------------------------------------------------------------- Figure 6
FIGS["06"] = {
    "tikz": r"""
\begin{tikzpicture}
\tikzset{zone/.style={draw=ink, line width=0.6pt, rounded corners=8pt, fill=band},
         zc/.style={box, minimum height=10mm, font=\footnotesize, text width=26mm},
         zt/.style={font=\bfseries\footnotesize, anchor=north east}}
\draw[draw=accent, line width=1pt, dashed, rounded corners=10pt] (-3mm,8mm) rectangle (150mm,-117mm);
\node[font=\bfseries\footnotesize, text=accent, anchor=north east] at (148mm,6mm) {«host»};
\node[pill, minimum width=40mm, minimum height=10mm, font=\footnotesize] (users) at (18mm,22mm) {«users»};
\draw[zone] (0,-2mm) rectangle (110mm,-26mm); \node[zt] at (108mm,-3mm) {«dmz»};
\node[zc] (waf) at (18mm,-16mm) {«waf»};
\node[zc] (portal) at (52mm,-16mm) {«portal»};
\node[zc] (api) at (88mm,-16mm) {«api»};
\draw[zone] (0,-31mm) rectangle (110mm,-55mm); \node[zt] at (108mm,-32mm) {«app»};
\node[zc] (search) at (18mm,-45mm) {«search»};
\node[zc] (answer) at (52mm,-45mm) {«answer»};
\node[zc] (analytics) at (88mm,-45mm) {«analytics»};
\draw[zone] (0,-60mm) rectangle (110mm,-84mm); \node[zt] at (108mm,-61mm) {«model»};
\node[key, zc, text width=30mm] (gpu) at (52mm,-74mm) {«gpu»};
\draw[zone] (0,-89mm) rectangle (110mm,-113mm); \node[zt] at (108mm,-90mm) {«data»};
\node[zc] (idx) at (18mm,-103mm) {«idx»};
\node[zc] (bak) at (52mm,-103mm) {«bak»};
\node[zc] (docs) at (88mm,-103mm) {«docs»};
\draw[zone, fill=accentlight] (116mm,-2mm) rectangle (147mm,-113mm);
\node[font=\bfseries\footnotesize, align=center, anchor=north, text width=29mm] at (131.5mm,-4mm) {«mgmt»};
\foreach \y/\k in {-30/{«idp»},-52/{«siem»},-74/{«cicd»},-96/{«keys»}} \node[zc, text width=24mm, draw=accent] at (131.5mm,\y mm) {\k};
\draw[arr] (users) -- (waf);
\draw[arr] (waf) -- (portal); \draw[arr] (portal) -- (api);
\draw[arr] (api) -- (analytics);
\draw[arr] (api.south west) -- (answer.north east);
\draw[arr] (answer) -- (search);
\draw[arr] (answer) -- (gpu);
\draw[arr] (search) -- (idx);
\draw[arr] (analytics) -- (docs);
\draw[arr] (docs.west) -- (bak.east);
\draw[darr, <->] (113mm,-20mm) -- node[lbl, rotate=90, fill=white]{«mtls»} (113mm,-95mm);
\end{tikzpicture}""",
    "en": {"host": "Hosted in Bangladesh: National Data Center or accredited facility",
           "users": "Users (internet, VPN)", "dmz": "Public zone (DMZ)", "waf": "WAF and rate limits",
           "portal": "Portal", "api": "API gateway", "app": "Application zone",
           "search": "Search service", "answer": "Answer service", "analytics": "Analytics",
           "model": "Model zone (no internet egress)", "gpu": "Open-weight model inference on local GPUs",
           "data": "Data zone (encrypted at rest)", "docs": "Document store", "idx": "Search index", "bak": "Offline backups",
           "mgmt": "Management zone", "idp": "Identity provider", "siem": "Logging and SIEM",
           "cicd": "CI/CD and SBOM", "keys": "Key management", "mtls": "mutual TLS"},
    "bn": {"host": "বাংলাদেশে হোস্টকৃত: জাতীয় ডেটা সেন্টার বা স্বীকৃত স্থাপনা",
           "users": "ব্যবহারকারী (ইন্টারনেট, VPN)", "dmz": "জনমুখী অঞ্চল (DMZ)", "waf": "WAF ও হার-সীমা",
           "portal": "পোর্টাল", "api": "API গেটওয়ে", "app": "অ্যাপ্লিকেশন অঞ্চল",
           "search": "অনুসন্ধান সেবা", "answer": "উত্তর সেবা", "analytics": "বিশ্লেষণ",
           "model": "মডেল অঞ্চল (ইন্টারনেট সংযোগহীন)", "gpu": "স্থানীয় GPU-তে উন্মুক্ত-ওজন মডেল চালনা",
           "data": "ডেটা অঞ্চল (সংরক্ষিত অবস্থায় এনক্রিপ্টেড)", "docs": "নথি সংরক্ষণাগার", "idx": "অনুসন্ধান সূচি", "bak": "অফলাইন ব্যাকআপ",
           "mgmt": "ব্যবস্থাপনা অঞ্চল", "idp": "পরিচয় প্রদানকারী", "siem": "লগ ও SIEM",
           "cicd": "CI/CD ও SBOM", "keys": "চাবি ব্যবস্থাপনা", "mtls": "পারস্পরিক TLS"},
}

# ---------------------------------------------------------------- Figure 7
FIGS["07"] = {
    "tikz": r"""
\begin{tikzpicture}[node distance=9mm and 12mm]
\node[pill, minimum width=50mm, minimum height=10mm] (start) {\textbf{«start»}};
\node[dec, below=8mm of start, text width=30mm] (p) {«p»};
\node[box, draw=warn, fill=warnlight, minimum width=44mm, minimum height=13mm, right=16mm of p] (t0) {\textbf{«t0»}\\{\footnotesize «t0s»}};
\node[box, minimum width=50mm, minimum height=10mm, below=8mm of p] (score) {«score»};
\node[dec, below=8mm of score, text width=36mm] (h) {«h»};
\node[box, draw=warn, minimum width=44mm, minimum height=13mm, right=16mm of h] (t3) {\textbf{«t3»}\\{\footnotesize «t3s»}};
\node[dec, below=9mm of h, text width=32mm] (l) {«l»};
\node[box, draw=accent, fill=accentlight, minimum width=44mm, minimum height=13mm, right=16mm of l] (t2) {\textbf{«t2»}\\{\footnotesize «t2s»}};
\node[box, draw=ok, fill=oklight, minimum width=50mm, minimum height=13mm, below=9mm of l] (t1) {\textbf{«t1»}\\{\footnotesize «t1s»}};
\draw[arr] (start) -- (p);
\draw[arr] (p) -- node[lbl, above]{«yes»} (t0);
\draw[arr] (p) -- node[lbl, right]{«no»} (score);
\draw[arr] (score) -- (h);
\draw[arr] (h) -- node[lbl, above]{«yes»} (t3);
\draw[arr] (h) -- node[lbl, right]{«no»} (l);
\draw[arr] (l) -- node[lbl, above]{«yes»} (t2);
\draw[arr] (l) -- node[lbl, right]{«no»} (t1);
\node[box, dashed, text width=40mm, font=\footnotesize, left=14mm of h] (note) {«note»};
\end{tikzpicture}""",
    "en": {"start": "New AI system proposal (G0)", "p": "Any prohibited use?",
           "t0": "T0 Prohibited", "t0s": "stop; excluded by charter",
           "score": "Score dimensions D1 to D7 (Annex B)",
           "h": "Total at least 13, or D1\\,=\\,3, or D2\\,=\\,3, or D2 and D3 at least 2?",
           "t3": "T3 High", "t3s": "research only; DPIA; binding ERRC review",
           "l": "Total at least 6, or D1\\,=\\,2, or D7 at least 2?",
           "t2": "T2 Limited", "t2s": "ERRC review; human review in use",
           "t1": "T1 Low", "t1s": "unit lead and TAB approve",
           "yes": "yes", "no": "no",
           "note": "Reassessed at every gate and after any change in purpose, data or users."},
    "bn": {"start": "নতুন এআই ব্যবস্থার প্রস্তাব (G0)", "p": "কোনো নিষিদ্ধ ব্যবহার?",
           "t0": "T0 নিষিদ্ধ", "t0s": "বন্ধ; সনদ দ্বারা বর্জিত",
           "score": "মাত্রা D1 থেকে D7 স্কোর করা (সংযুক্তি খ)",
           "h": "মোট কমপক্ষে ১৩, বা D1\\,=\\,৩, বা D2\\,=\\,৩, বা D2 ও D3 কমপক্ষে ২?",
           "t3": "T3 উচ্চ", "t3s": "শুধু গবেষণা; DPIA; বাধ্যতামূলক ERRC পর্যালোচনা",
           "l": "মোট কমপক্ষে ৬, বা D1\\,=\\,২, বা D7 কমপক্ষে ২?",
           "t2": "T2 সীমিত", "t2s": "ERRC পর্যালোচনা; ব্যবহারে মানব-পর্যালোচনা",
           "t1": "T1 নিম্ন", "t1s": "ইউনিট প্রধান ও TAB অনুমোদন করেন",
           "yes": "হ্যাঁ", "no": "না",
           "note": "প্রতিটি গেটে এবং উদ্দেশ্য, ডেটা বা ব্যবহারকারী বদলালে পুনর্মূল্যায়ন।"},
}

# ---------------------------------------------------------------- Figure 8
FIGS["08"] = {
    "tikz": r"""
\begin{tikzpicture}
\tikzset{g/.style={draw=ink, line width=0.6pt, fill=white, signal, signal to=east, signal from=west,
                   minimum height=14mm, minimum width=28mm, align=center, font=\footnotesize, text width=22mm, inner sep=2pt},
         ev/.style={box, font=\scriptsize, text width=25mm, minimum height=24mm, anchor=north, fill=band, rounded corners=5pt}}
\node[g, signal from=nowhere] (g0) at (0,0) {\textbf{G0}\\«g0»};
\node[g] (g1) at (29mm,0) {\textbf{G1}\\«g1»};
\node[g, fill=accentlight] (g2) at (58mm,0) {\textbf{G2}\\«g2»};
\node[g, fill=accentlight] (g3) at (87mm,0) {\textbf{G3}\\«g3»};
\node[g, fill=accentlight] (g4) at (116mm,0) {\textbf{G4}\\«g4»};
\node[g] (g5) at (145mm,0) {\textbf{G5}\\«g5»};
\node[ev] at (0,-10mm) {«e0»};
\node[ev] at (29mm,-10mm) {«e1»};
\node[ev] at (58mm,-10mm) {«e2»};
\node[ev] at (87mm,-10mm) {«e3»};
\node[ev] at (116mm,-10mm) {«e4»};
\node[ev] at (145mm,-10mm) {«e5»};
\draw[darr] (g4.north) to[bend right=22] node[lbl, above]{«rework»} (g1.north);
\node[font=\footnotesize, anchor=west, text=accent] at (49mm,-38mm) {«shade»};
\end{tikzpicture}""",
    "en": {"g0": "Register and screen", "g1": "Design review", "g2": "Pre-pilot readiness",
           "g3": "Pilot", "g4": "Adoption decision", "g5": "Update or retire",
           "e0": "AI system record; tier screening; prohibited-use check",
           "e1": "Data plan; DPIA if DC2; TAB design approval",
           "e2": "Benchmark thresholds met; red-team and security tests; ERRC approval for T2",
           "e3": "Limited users; monitoring; incident procedure; user feedback",
           "e4": "Independent evaluation; host-agency acceptance; legal review",
           "e5": "Re-evaluation after changes; responsible decommissioning; archive",
           "rework": "rework when evidence is insufficient",
           "shade": "Shaded gates require an ERRC decision for tier T2 and above"},
    "bn": {"g0": "নিবন্ধন ও যাচাই", "g1": "নকশা পর্যালোচনা", "g2": "পাইলট-পূর্ব প্রস্তুতি",
           "g3": "পাইলট", "g4": "গ্রহণের সিদ্ধান্ত", "g5": "হালনাগাদ বা অবসান",
           "e0": "এআই ব্যবস্থার রেকর্ড; স্তর যাচাই; নিষিদ্ধ ব্যবহার যাচাই",
           "e1": "ডেটা পরিকল্পনা; DC2 হলে DPIA; TAB-এর নকশা অনুমোদন",
           "e2": "বেঞ্চমার্ক-সীমা অর্জিত; রেড-টিম ও নিরাপত্তা পরীক্ষা; T2-এর জন্য ERRC অনুমোদন",
           "e3": "সীমিত ব্যবহারকারী; পর্যবেক্ষণ; ঘটনা-প্রক্রিয়া; ব্যবহারকারীর মতামত",
           "e4": "স্বাধীন মূল্যায়ন; স্বাগতিক সংস্থার গ্রহণ; আইনি পর্যালোচনা",
           "e5": "পরিবর্তনের পর পুনর্মূল্যায়ন; দায়িত্বশীল অবসান; সংরক্ষণ",
           "rework": "প্রমাণ অপর্যাপ্ত হলে পুনরায় কাজ",
           "shade": "রঙিন গেটগুলোতে T2 ও তদূর্ধ্ব স্তরের জন্য ERRC সিদ্ধান্ত আবশ্যিক"},
}

# ---------------------------------------------------------------- Figure 9 (Gantt)
FIGS["09"] = {
    "tikz": r"""
\begin{tikzpicture}
\def\x{4.2mm}  % per month
\def\h{7mm}    % per row
\def\L{48mm}   % label width
% header
\foreach \yr/\s in {«y1»/0,«y2»/12,«y3»/24} {
  \fill[band2] (\L+\s*\x,0) rectangle (\L+\s*\x+12*\x,6mm);
  \node[font=\bfseries\footnotesize] at (\L+\s*\x+6*\x,3mm) {\yr};
}
\foreach \q in {0,...,11} {
  \pgfmathtruncatemacro{\qq}{mod(\q,4)+1}
  \node[font=\scriptsize] at (\L+\q*3*\x+1.5*\x,-2.5mm) {«qlab»};
}
\foreach \m in {0,3,...,36} \draw[band2, line width=0.4pt] (\L+\m*\x,-5mm) -- (\L+\m*\x,-5mm-10*\h-2mm);
% rows: label, start month (0-based), end month, style
\newcommand{\gbar}[5]{%
  \node[font=\footnotesize, anchor=west, text width=\L-2mm] at (0,-5mm-#1*\h-0.5*\h) {#2};
  \fill[#5, rounded corners=2pt] (\L+#3*\x,-5mm-#1*\h-0.2*\h) rectangle (\L+#4*\x,-5mm-#1*\h-0.8*\h);}
\gbar{0}{«w1»}{0}{6}{ink}
\gbar{1}{«w2»}{1}{36}{ink!55}
\gbar{2}{«w3»}{3}{24}{accent}
\gbar{3}{«w4»}{4}{24}{accent!70}
\gbar{4}{«w5»}{10}{30}{accent!50}
\gbar{5}{«w6»}{0}{36}{accent!35}
\gbar{6}{«w7»}{9}{36}{ink!35}
\gbar{7}{«w8»}{6}{30}{ink!25}
\gbar{8}{«w9»}{6}{36}{ok!70}
\gbar{9}{«w10»}{15}{36}{warn!60}
% milestones
\foreach \m/\n in {3/1,6/2,9/3,12/4,15/5,18/6,24/7,30/8,36/9} {
  \node[draw=ink, fill=white, diamond, inner sep=1.6pt] at (\L+\m*\x,-5mm-10*\h-5mm) {};
  \node[font=\scriptsize, anchor=north] at (\L+\m*\x,-5mm-10*\h-7mm) {MS\n};
}
\node[font=\scriptsize, anchor=west] at (0,-5mm-10*\h-5mm) {«ms»};
\end{tikzpicture}""",
    "en": {"y1": "Year 1 (2027-28)", "y2": "Year 2 (2028-29)", "y3": "Year 3 (2029-30)",
           "w1": "Institution, charter, governance", "w2": "Data access and corpus", "w3": "P1 Policy Search",
           "w4": "P2 Budget dashboard", "w5": "P3 Feedback analyser", "w6": "P4 Bangla foundation model",
           "w7": "P5 Readiness observatory", "w8": "P6 Information integrity", "w9": "Training and capacity",
           "w10": "Independent evaluation", "ms": "Milestones", "qlab": "Q\\qq"},
    "bn": {"y1": "বছর ১ (২০২৭-২৮)", "y2": "বছর ২ (২০২৮-২৯)", "y3": "বছর ৩ (২০২৯-৩০)",
           "w1": "প্রতিষ্ঠান, সনদ, শাসন", "w2": "ডেটা প্রবেশাধিকার ও কর্পাস", "w3": "P1 নীতি অনুসন্ধান",
           "w4": "P2 বাজেট ড্যাশবোর্ড", "w5": "P3 মতামত বিশ্লেষক", "w6": "P4 বাংলা ফাউন্ডেশন মডেল",
           "w7": "P5 প্রস্তুতি পর্যবেক্ষণকেন্দ্র", "w8": "P6 তথ্য-অখণ্ডতা", "w9": "প্রশিক্ষণ ও সক্ষমতা",
           "w10": "স্বাধীন মূল্যায়ন", "ms": "মাইলফলক",
           # quarter ticks as Bangla ordinals (1st to 4th quarter)
           "qlab": "\\ifcase\\qq\\or ১ম\\or ২য়\\or ৩য়\\or ৪র্থ\\fi"},
}


# First-edition figure numbers mapped to the expanded edition, plus the new figures.
FIG_RENUMBER = {"01": "01", "02": "03", "03": "04", "04": "07", "05": "08", "06": "09",
                "07": "10", "08": "11", "09": "12"}
sys.path.insert(0, HERE)
from figures_new import NEW_FIGS  # noqa: E402

FIGS = dict({FIG_RENUMBER[k]: v for k, v in FIGS.items()}, **NEW_FIGS)


def render(fid, lang):
    spec = FIGS[fid]
    body = spec["tikz"]
    for k, v in spec[lang].items():
        body = body.replace("«%s»" % k, v)
    if "«" in body:
        raise SystemExit("unfilled placeholder in figure %s %s: %s" % (fid, lang, body[body.index("«"):][:30]))
    pre = PRE_EN if lang == "en" else PRE_BN
    return pre + COMMON + "\\begin{document}\n\\sffamily\\hyphenpenalty=10000\\exhyphenpenalty=10000\n" + body + "\n\\end{document}\n"


def compile_fig(tex_path):
    stem = tex_path[:-4]
    with tempfile.TemporaryDirectory() as tmp:
        base = os.path.basename(tex_path)
        shutil.copy(tex_path, os.path.join(tmp, base))
        r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", base],
                           cwd=tmp, capture_output=True, text=True)
        if r.returncode != 0:
            sys.stderr.write(r.stdout[-2500:])
            raise SystemExit("xelatex failed: %s" % base)
        with open(os.path.join(tmp, base[:-4] + ".log"), encoding="utf-8", errors="replace") as fh:
            miss = [l.strip() for l in fh if "Missing character" in l]
        if miss:
            sys.stderr.write("WARNING %s: %s\n" % (base, miss[:3]))
        shutil.copy(os.path.join(tmp, base[:-4] + ".pdf"), stem + ".pdf")
    subprocess.run(["pdftoppm", "-r", "300", "-png", "-singlefile", stem + ".pdf", stem], check=True)


def main():
    only = sys.argv[1].split(",") if len(sys.argv) > 1 else sorted(FIGS)
    os.makedirs(OUT, exist_ok=True)
    for fid in only:
        for lang in ("en", "bn"):
            stem = "blueprint_fig%s%s" % (fid, "" if lang == "en" else "_bn")
            p = os.path.join(OUT, stem + ".tex")
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(render(fid, lang))
            compile_fig(p)
        print("figure", fid, "done")


if __name__ == "__main__":
    main()
