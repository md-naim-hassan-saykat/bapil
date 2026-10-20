**সারণি ২০।** API বিনির্দেশ (সংস্করণ ১)

| এন্ডপয়েন্ট | পদ্ধতি | প্যারামিটার | প্রতিক্রিয়া | ত্রুটি |
|-------------------|-------|--------------------|--------------------------|--------------|
| /v1/health | GET | নেই | status, version, corpus_version, documents, passages | নেই |
| /v1/search | GET | q (১ থেকে ৫০০ অক্ষর); k (১ থেকে ৫০, ডিফল্ট ১০) | query, corpus_version, results: pid, doc_id, heading, lang, score, matched_terms, text, provenance | ৪০০ অনুপস্থিত বা অবৈধ প্যারামিটার |
| /v1/answer | GET | q (১ থেকে ৫০০ অক্ষর) | abstained; confidence; evidence (top_score, coverage); উদ্ধৃতিসহ উত্তর-বাক্য; sources; corpus_version | ৪০০ অনুপস্থিত প্যারামিটার |
| /v1/risk/assess | POST | JSON প্রশ্নমালা (সংযুক্তি খ-এর স্কিমা) | system_id, tier, tier_name, total, reasons, controls, approver | ৪০০ অবৈধ প্রশ্নমালা; ৪০০ বডি ৬৪ কিলোবাইটের বেশি |
| সকল এন্ডপয়েন্ট |  |  | UTF-8 JSON; প্রতিটি অনুরোধ নিরীক্ষা-শৃঙ্খলে লগকৃত | ৪০৪ অজানা পথ |
