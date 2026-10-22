# Bangla editorial pass: 22 October 2026

This is an internal record and is not part of the publication. It covers the Bangla Technical Blueprint (`blueprint/src/bn/*.md`), the Bangla Summary and Decision Memo sources, and the Bangla strings in the table and figure scripts (`tables_*.py`, `figures_new.py`).

This pass was systematic, but it was done by the author's assistant and not by a professional Bangla editor. Item U14 in Annex V (independent professional language review) stays open.

## 1. Method

1. **Mechanical scan** (`bnscan.py`). It looked for:
   - doubled words and spaces;
   - Latin punctuation inside Bangla sentences;
   - ASCII digits in Bangla prose;
   - stray zero-width characters;
   - a mismatched danda or full stop;
   - unbalanced brackets and quotation marks.

   Result: essentially clean. The remaining hits are false positives:
   - the zero-width joiner in র‍্য is required for correct rendering;
   - repeated words are Bangla reduplication (for example ধাপে ধাপে);
   - English words appear on purpose (API field names, relation names, examples of queries);
   - full stops before raw LaTeX or HTML comments are not prose.
2. **Context scan** (`bnscan2.py`): English words left in running text, and terms whose use differs from the bilingual register in `docs/source-of-truth.md`.
3. **Consistency scan**: every compound term that appears both hyphenated and spaced, counted across all Bangla sources. Where a form clearly dominated, the dominant form became canonical. Where usage was close to even, the choice followed the closest standard pattern: hyphenated for noun-noun compounds used as one technical term, spaced where the second word is a common verbal noun.
4. **Reading review** of the Bangla text added in October 2026:
   - Section 6.3, Terms of employment;
   - Section 17.2: tranches, capital and revenue;
   - Section 17.3;
   - Annex W (W.1 to W.4);
   - the scale-up paragraphs of the Summary and the Memo.

## 2. Spelling standardised

76 occurrences were changed. Every change is a spelling-only change of the same word.

| Variant replaced | Canonical form | Changes |
|---|---|---:|
| ডেটা বিনিময় | ডেটা-বিনিময় | 16 |
| উন্নয়ন-সহযোগী | উন্নয়ন সহযোগী | 6 |
| শাসন-ব্যবস্থা | শাসনব্যবস্থা | 5 |
| স্বাগতিক চুক্তি | স্বাগতিক-চুক্তি | 5 |
| উন্মুক্ত প্রবেশাধিকার | উন্মুক্ত-প্রবেশাধিকার | 5 |
| প্রবেশ-নিয়ন্ত্রণ | প্রবেশ নিয়ন্ত্রণ | 4 |
| শাসন বিশ্লেষক | শাসন-বিশ্লেষক | 4 |
| ডেটা-সেন্টার | ডেটা সেন্টার | 3 |
| ব্যয়-নিরূপিত | ব্যয়-নির্ধারিত (“costed”, the majority form) | 3 |
| বিশ্ববিদ্যালয়ভিত্তিক | বিশ্ববিদ্যালয়-ভিত্তিক | 2 |
| নিষিদ্ধ-ব্যবহার | নিষিদ্ধ ব্যবহার | 2 |
| জনবল-পরিকল্পনা | জনবল পরিকল্পনা | 2 |
| সূচক কাঠামো | সূচক-কাঠামো | 2 |
| দক্ষতা কাঠামো | দক্ষতা-কাঠামো | 2 |
| জিপিইউ | GPU (as in the other 35 uses) | 2 |
| বাদ পড়া (adjective: “known omitted costs”) | বাদ-পড়া | 1 |
| ব্যয় নিরূপণ | ব্যয়-নিরূপণ | 1 |
| উন্মুক্ত-সোর্স | উন্মুক্ত সোর্স | 1 |
| মান যাচাই | মান-যাচাই | 1 |
| স্বাগতিক-সংস্থা | স্বাগতিক সংস্থা | 1 |
| গবেষণা প্রোটোটাইপ | গবেষণা-প্রোটোটাইপ | 1 |
| প্রম্পট ইনজেকশন | প্রম্পট-ইনজেকশন | 1 |
| শাসন কাঠামো | শাসন-কাঠামো | 1 |
| ডেটা চুক্তি | ডেটা-চুক্তি | 1 |
| পরিস্থিতি-বিশ্লেষণ | পরিস্থিতি বিশ্লেষণ | 1 |
| অনুসন্ধান-সরঞ্জাম | অনুসন্ধান সরঞ্জাম | 1 |
| জনআস্থা | জন-আস্থা | 1 |
| সিদ্ধান্তগ্রহীতারা | সিদ্ধান্তগ্রহণকারীরা (as in the other 8 uses) | 1 |

“বাদ পড়ার ঝুঁকি” (the risk of being left out) is a verbal phrase, so it stays spaced. The mechanical replacement was reverted for that one occurrence.

## 3. Word choice

* **উপাত্ত → ডেটা**, in two general uses:
  - the source note “উল্লিখিত ডেটা থেকে লেখকের হিসাব”;
  - “বাজেটের ডেটা:”.

  The register uses ডেটা for “data”. উপাত্ত stays wherever it is part of a legal title, such as the personal data protection ordinance, and in the Charter clause on data protection, which follows that legal usage.
* **Summary, scale-up paragraph.** The sentence “একটি নতুন ল্যাব এর চেয়ে অনেক বড় অঙ্ক ভালোভাবে নিয়োগ বা ব্যয় করতে পারত না” said that an *amount* is hired. It now says the lab could not hire many more staff, or spend a much larger amount, well.
* **Annex W.3.** The closing sentence on planning estimates was reordered so that it reads naturally. The meaning is the same as the English text.

## 4. Checked and left unchanged

| Item | Reason |
|---|---|
| বিরতি for “abstention” (24 uses), with বিরত থাকা as the verb (16 uses) | This follows the register entry “বিরতি (উত্তর থেকে বিরত থাকা)”. The noun and the verb have different roles, so they are not variants |
| পথনকশা (4 uses) beside রোডম্যাপ (26 uses) | পথনকশা translates “pathway” (the integrated pathway in Figure 16 and Table 71). রোডম্যাপ translates “roadmap”. These are different terms |
| অংশীজন (stakeholder) and অংশীদার (partner) | Different terms, each used consistently |
| সমঝোতা স্মারক (44 uses) | Already consistent |
| Section 6.3, 17.2, 17.3 and Annex W text | Read in full. Apart from the changes above, the text is natural and matches the English on every number, condition and citation |

## 5. Verification

* The citation keys, table and figure markers, LaTeX commands and code were not touched; the replacements matched Bangla word boundaries only.
* The number parity check between the English and Bangla editions was run again after the rebuild (`QA_REPORT.md`, section 12).
* A professional Bangla editor should still review the whole text before any printed or official use (U14).
