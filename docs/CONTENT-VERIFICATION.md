# Content verification report — TKA Bahasa Inggris TO 03

**Source:** `103 TO 03 TKA ENG (Elephant, Study Session, Labuan Bajo).pdf`  
**Extracted:** 26 October 2026  
**Status:** Source transcription checked programmatically; editorial keys are independently derived **and not official**.

## Complete extraction inventory

The file contains **eight PDF pages**, 20 numbered questions and five related reading passages. The PDF has selectable English text and **zero embedded images**. It does not include an answer key, suggested answers, scoring rubric, explanations, or a time limit. Its cover heading says `Mapel : Bahasa Inggris Wajib` and `Soal : 20 butir`. No material was added to missing parts of the original English text.

| Question range | Passage title | Source pages | Type |
|---|---|---|---|
| 1–5 | The Elephant and the Little Bird | 1–3 | 5 single-choice |
| 6–10 | How to Prepare for an Effective Study Session | 3–4 | 5 single-choice |
| 11–13 | Labuan Bajo, East Nusa Tenggara | 4–6 | 3 multiple-choice / choose-all |
| 14–17 | My First Coldplay Concert Experience | 6–7 | 4 multiple-choice / choose-all |
| 18–20 | A Memorable Trip to Yogyakarta | 7–8 | 3 Yes/No category questions (three statements each) |

Total: **10 single-answer**, **7 multiple-answer** and **3 category/Yes–No** questions. Every original number 1–20 appears exactly once. Single-answer and multi-answer questions each preserve five A–E options; category questions each preserve three A–C statements with their original `(Yes / No)` wording. All passages, prompts, and options match `data/source_extracted.json`; the same file was generated from the uploaded source PDF and serves as the regression baseline. No images, charts, tables or diagrams need assets for this particular test.

Detailed per-item page references and unique IDs are in `question-inventory.json`.

## Independently determined working answer key

No supplied/official answer key exists in the uploaded PDF. The following answers are reasoned from the readings. **Do not describe them as official.**

| Q | Working answer | Status / reasoning note |
|---|---|---|
| 1 | B | Covers beginning, conflict, rescue and moral |
| 2 | E | Bird later helps endangered elephant |
| 3 | A | Being small does not prevent an important contribution |
| **4** | **Unresolved** | Question presumes an event not described; none of five reasons is supported |
| **5** | **Unresolved** | Several sentences reveal the elephant's character, without a disambiguating instruction |
| 6 | C | Short sessions and brief breaks explicitly improve concentration |
| 7 | A | Matches numbered steps 1, 2, 3, 4 and 7 in that order |
| 8 | D | Main purpose is improved organization and learning outcomes |
| 9 | C | Short sessions plus regular review address both problems |
| 10 | A | Self-testing inferred from the unelaborated step 6 heading; see caveat below |
| 11 | A, B, E | Tropical forests, coral reefs and Padar Island |
| 12 | A, B, C | Manggarai traditions, dances/music and traditional houses |
| 13 | C, D | Tourism economic role; government improved infrastructure |
| 14 | B, D, E | Gratitude for tickets, sustained excitement and interactions with fans |
| 15 | A, D | Chris Martin sought connection with audience; warm interaction |
| 16 | A, B | Enthusiasm and band shirts/light sticks described explicitly |
| 17 | B, C | Wristband display and personal interaction; E is thematically debatable |
| 18 | A Yes; B Yes; C No | History and batik vs beach volleyball |
| **19** | **Unresolved** | Statement C contradicts the passage on teacher vs tour guide |
| 20 | A Yes; B No; C Yes | Learning and memories; travel was not only sightseeing; tiring but worthwhile |

**Graded / denominator: 17 questions.** The three unresolved questions (4, 5, 19) are included in the interface and results, but not scored. Graded multi-answer questions are exact-set (all correct options, no extras); category questions require all statements correct. No partial credit. Missing answers on gradeable questions earn zero. Possible total **17/17 = 100%**. Students should not confuse this percentage with a 20-question official score.

## Source problems and editorial decisions

1. **Q4: false premise.** The story does not say the elephant decided to let the bird go or refrained from chasing her. The bird feels sad but simply does not argue. A–E speculate about incidents that were never narrated. The question is excluded from grading rather than assigning a fabricated key.
2. **Q5: multiple valid character clues.** Option D demonstrates dismissive/arrogant behavior; E shows recognition of error and personality growth. B also provides characterization context. The singular-selection frame gives no unique rule for selecting one. Excluded.
3. **Q8: duplicated options C and E.** The source repeats the same complete sentence. This duplicate is retained; D remains clearly stronger as the general-purpose answer. Gradeable with documented defect.
4. **Study-session passage: missing paragraph at step 6.** “6. Practice What You Learn” has no accompanying body text in the PDF. Q10's proposed A follows a reasonable understanding of *practice* and diagnostic self-testing, but the phrase “without referring to her notes” is not present in the passage. This is a labeled inference, not fabricated evidence. Editorial review recommended before high-stakes use.
5. **Q15, B:** The source says Chris Martin's effort made the performance feel personal, but does not claim **he himself** felt it was more personal. A and D are better supported.
6. **Q16, D:** The reading mentions **cheering** and illuminated wristbands. It does **not** state that thousands of audience members joined **singing**. D is not selected.
7. **Q17, E:** A conclusion that music unites people is conceivable, but no line specifically states that realization. B and C have clearer direct evidence; answer is marked as independently reasoned with a caveat, not a guaranteed official key. If intended key includes E, revise using documented editorial review and advance `contentRevision`.
8. **Q19, C:** The option reads “**The tour guide** asked everyone to move away…” but the text says “**Our teacher** quickly asked everyone to move away…”. If the examiner intended to test the activity change only, they might expect Yes, but the stated agent is wrong. Rather than grading a contested interpretation, exclude the question pending correction/confirmation.
9. **Source ownership:** This PDF may be copyrighted. The file's origin and licensing are unknown. Verify publication rights before making verbatim English passages/questions and answer options publicly accessible. The repository is **not affiliated with an official examination board**.

## Review evidence and translations

Every question JSON contains:
- Faithful English question and answer options, with original PDF question number and page.
- Translations of question and every answer option into natural Indonesian.
- A full Indonesian translation of its associated English passage.
- A question-specific explanatory paragraph and **one reason per original option**, including incorrect options.
- One or more literal English evidence excerpts matched to its referenced passage.
- Optional vocabulary notes, suitable for students learning English.
- `answerProvenance`, `graded`, and any relevant `sourceIssue`.

**Evidence** entries are exact source substrings. An inference may be based on those quotations without being asserted as the quotation itself. Short literary interpretations remain editor opinions, explicitly independent of any official key.

## Automated validation actually executed

From the repository root:

```bash
python3 tools/validate.py
node --test tests/*.test.mjs
```

**Observed:** static validator reports **1 test, 20 questions, 0 errors and 0 warnings**; Node scoring suite reports **13 passing / 0 failing**. The tests cover full source numbering, correct/incorrect/unanswered/unresolved statuses, exact-set scoring, all-rows-correct categories, exclusion of unresolved items from denominator, perfect answer scores, wrong multi-select penalties, duplicate Q8 options, issue flags, display of correct answer labels, draft persistence by mode, backup merging without duplicate history, and rejection of broken backup files. JS module syntax checks also passed using `node --check`.

**Not fully verified:** browser navigation and visual layout. Attempted UI automation in headless Chromium/Playwright, but the execution environment's managed Chromium policy blocked **all page navigation** (`net::ERR_BLOCKED_BY_ADMINISTRATOR`), including local HTTP and data pages. Therefore **no browser UI smoke test was completed**, and no real-device mobile/keyboard/screen-reader test was completed. Inspect mobile and desktop rendering and run the manual acceptance checks listed in `DEPLOYMENT.md` before publishing. There is no claim that these unexecuted tests passed.
