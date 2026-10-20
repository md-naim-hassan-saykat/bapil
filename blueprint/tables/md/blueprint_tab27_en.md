**Table 27.** Bangla text challenges and normalisation rules

| Challenge | Example | Rule or method |
|-------------------|------------------------|---------------------------------|
| Alternative encodings of nukta letters | য় as one code point or as য + nukta | Unicode NFC (decomposes U+09DC, U+09DD, U+09DF consistently) |
| Legacy khanda ta | ত + virama + ZWJ instead of ৎ | Map the sequence to U+09CE before removing zero-width characters |
| Zero-width characters | ZWJ, ZWNJ, soft hyphen inside words | Remove for matching; keep the original for display |
| Bangla and ASCII digits | ২০২৬ and 2026 | Fold Bangla digits to ASCII for matching |
| Inflection | নীতি, নীতির, নীতিসমূহের | Light suffix stripping; index both surface form and stem |
| Spelling variants and reforms | সরকারী and সরকারি; জাতীয় written with different encodings | Variant list maintained by language editors; NFC first |
| Code-mixing and romanised Bangla | budget বরাদ্দ; romanised queries such as bajet | Bilingual glossary; transliteration candidates in later versions |
| OCR errors in conjuncts | ক্ষ, ষ্ণ, ন্ত্র misread | OCR quality score per page; human correction queue |
| Bangla calendar dates | Dates given in the Bangla calendar | Store both Gregorian and Bangla dates where given |
| Name transliteration | Ministry and place names in several spellings | Authority list of names with variants |
