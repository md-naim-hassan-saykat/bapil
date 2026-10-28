**সারণি ৫৮।** প্রয়োজনীয়তা অনুসরণযোগ্যতা ম্যাট্রিক্স

| প্রয়োজনীয়তা | সারাংশ | উপাদান | কোড মডিউল | যাচাই |
|----------|------------------------------|----------|-------------------|----------------|
| FR-01 | দ্বিভাষিক অনুসন্ধান | C2, C4 | bapil.text, bapil.search | test_text, test_search |
| FR-02 | উদ্ধৃতিসহ উত্তর ও বিরত থাকা | C5 | bapil.answer | test_answer |
| FR-03 | গ্রহণের সময় উৎস-তথ্য | C2, C3 | bapil.corpus | test_corpus |
| FR-04 | ড্যাশবোর্ড | C6, C7 | শুধু বিনির্দেশিত | পাইলট P2 গ্রহণ |
| FR-05 | সামষ্টিক মতামত বিশ্লেষণ | C6 | শুধু বিনির্দেশিত | পাইলট P3-এর DPIA ও গ্রহণ |
| FR-06 | এআই ব্যবস্থা নিবন্ধন | C12 | bapil.registry | test_registry |
| FR-07 | ঝুঁকি-স্তর মূল্যায়ন | C12 | bapil.risk | test_risk |
| FR-08 | মূল্যায়ন কাঠামো | C11 | bapil.evaluate | test_evaluate |
| FR-09 | স্বচ্ছতা নিবন্ধন | C12 | bapil.registry (রপ্তানি) | test_registry |
| FR-10 | সংস্করণকৃত API | C8 | bapil.api | test_api |
| NFR-01 | ভাষাগত সমতা | C2, C4 | bapil.text শব্দকোষ ও প্রমিতকারী | test_text; বেঞ্চমার্ক |
| NFR-07 | পুনরুৎপাদনযোগ্যতা | সব | CI ওয়ার্কফ্লো; বাহ্যিক নির্ভরতা নেই | GitHub Actions |
| NFR-08 | ব্যাখ্যাযোগ্যতা | C5 | bapil.answer (উৎস ও স্কোর) | test_answer |
| GR-02 | নির্মাণের আগে গেট | C12 | bapil.risk | test_risk |
| GR-04 | হস্তক্ষেপ-শনাক্তযোগ্য লগ | C10 | bapil.audit | test_audit |
| GR-06 | নিষিদ্ধ ব্যবহার | C12 | bapil.risk (T0 যাচাই) | test_risk |
