# Content schema & scoring — Ruang Uji v1

Ruang Uji uses simple **JSON data**, not question-specific HTML or application rewrites. `schemaVersion: 1` applies to the catalogue and test files. Student backup files use their own `schemaVersion: 1`. A future incompatible format requires an intentional migration, not silent overwriting.

## Catalogue

`data/catalog.json`:

```json
{
  "schemaVersion": 1,
  "tests": [{
    "id": "unique-stable-id",
    "path": "data/tests/unique-stable-id.json",
    "title": "My practice test",
    "subtitle": "Descriptive topic name",
    "subject": "Bahasa Inggris",
    "exam": "TKA",
    "topics": ["Narrative"],
    "questionCount": 5,
    "gradedCount": 5,
    "year": null,
    "officialDurationMinutes": null,
    "verification": "Independent key; not official",
    "badge": "BARU",
    "available": true
  }]
}
```

`id` is stable: lowercase letters/numbers/hyphens. The referenced test JSON's `id` must match. `year` and official duration **must stay `null` if unknown**. An estimated time may be added as honest user-facing metadata later, but do not label it an official time limit.

## Test object

Main example: `data/tests/tka-eng-to03.json`. Fields include:

```json
{
  "schemaVersion": 1,
  "id": "unique-stable-id",
  "title": "Example",
  "subtitle": "Overview",
  "exam": "TKA",
  "subject": "Bahasa Inggris Wajib",
  "questionCount": 2,
  "contentRevision": 1,
  "source": {"file": "source.pdf", "pages": 5, "answerKeyIncluded": false, "publicationRights": "not verified"},
  "passages": [{
    "id": "text-1", "title": "Reading passage",
    "original": "Full English text...", "translationId": "Terjemahan Indonesia...",
    "page": 1, "originalNumberRange": "1–2"
  }],
  "questions": [
    {"id":"q01", "number":1, "type":"single", "passageId":"text-1", "page":1,
     "prompt":"Question?", "options":[{"id":"A","text":"Choice 1"},{"id":"B","text":"Choice 2"},{"id":"C","text":"Choice 3"}],
     "translationId":{"prompt":"Terjemahan soal?","options":{"A":"Pilihan 1","B":"Pilihan 2","C":"Pilihan 3"}},
     "graded":true,"answer":["B"], "answerProvenance":"independently-derived", "scoring":"single-exact",
     "explanationId":"Penjelasan khusus untuk soal ini...", "optionReasonId":{"A":"Mengapa salah","B":"Mengapa benar","C":"Mengapa salah"},
     "evidence":[{"quote":"Full English text", "kind":"direct"}], "vocabulary":[]
    }
  ]
}
```

Source keys and passage texts are plain text, *not HTML*. Browser code escapes their content before display to limit injection from newly added JSON. Passage paragraphs are split at blank lines. The study-session original text includes numbered step headings embedded in paragraphs and the missing Step 6 body is **not** reconstructed.

### Supported question types

| `type` | UI control | Student response | Key format | Grade |
|---|---|---|---|---|
| `single` | radio | `"B"` | `["B"]` | one point only if same choice |
| `multiple` | checkbox | `["A","C"]` | `["A","C"]` | one point only if **exact set**, never partial |
| `category` | per-row independent radio | `{"A":"Yes","B":"No"}` | `{"A":"Yes","B":"No"}` | one point only if **all rows** match |

`category` questions also need a `categories` array, for instance `[{"id":"Yes","label":"Yes","translation":"Ya"},{"id":"No","label":"No","translation":"Tidak"}]`, and `scoring: "all-rows-correct"`.

An item that **cannot be keyed responsibly** must have `graded: false`, `answer: null`, `answerProvenance: "unresolved"`, and a human-readable `sourceIssue`. Students may enter answers, but they are never awarded or denied points for these questions. An unresolved question still appears in navigation, results and option-by-option educational review.

**Completed result formula:** `Math.round(100 * correct / gradeableQuestionCount)`. Every gradeable question contributes exactly one point to the denominator, including **unanswered** questions (which receive zero). Questions with `graded: false` contribute zero to both numerator and denominator. The saved attempt stores its result snapshot and contentRevision to avoid unnoticed shifts in historical scores.

### Evidence and explanations

Each question contains Indonesian `explanationId` and `optionReasonId` for every choice or category statement. English evidence is in `evidence[].quote` and **must match a verbatim substring** of the linked `passageId`'s `original` field. Interpretation and inference belong in the Indonesian explanation, **not inside quotation marks as fabricated source text**. `translationId.prompt`, `translationId.options`, and `passages[].translationId` must be complete. `vocabulary` is an optional array of `[English expression, Indonesian explanation]` pairs. Assets, when used, should live under `assets/tests/`; add valid relative paths to a passage's `assets` array and ensure `tools/validate.py` checks those paths.

### Source integrity

Maintain original numbering, exact English wording and original answer choices. Do not turn a multiple-answer question into a single choice. A source with 12 questions must have 12 question objects and a matching `questionCount` in **both** files. Source pages are `page` (question and passage). If an official key is supplied, record that key's provenance and check it; do not silently overwrite a supplied key. If a source is ambiguous or incomplete, flag and exclude it from grading.

## Local progress schema

Browser key `ruang-uji-progress-v1`:

```json
{
  "schemaVersion": 1,
  "drafts": {
    "unique-stable-id:practice": {
      "responses": {"q01": "A", "q02": ["B", "D"]},
      "checked": ["q01"], "index": 1, "timerSeconds": 52,
      "updatedAt": "2026-10-26T00:00:00.000Z", "contentRevision": 1
    }
  },
  "history": {
    "unique-stable-id": [
      {"id": "unique-attempt-id", "mode": "practice", "contentRevision": 1,
       "submittedAt": "2026-10-26T00:00:00.000Z",
       "responses": {"q01": "A"}, "metrics": {"correct": 0, "incorrect": 1, "unanswered": 1, "unresolved": 0, "gradable": 2, "percentage": 0}}
    ]
  }
}
```

No progress is written to the server. The **Export backup** action downloads a JSON file; **Import backup** validates basic shape and merges drafts by latest update time and result histories by unique attempt ID, retaining existing attempts. File extensions are not trusted as guarantees; import errors are explained. Back up before changing devices, clearing browser data or changing content IDs.

## Compatibility policy

- New tests: add new IDs, no code changes; previous local histories remain keyed to their test IDs.
- Fix explanations/translation without changing keys: advance `contentRevision` and note it in release notes. Past saved result remains historically scored; review loads the latest explanations and shows a revision warning.
- Correct a key: advance `contentRevision` **and document score changes**. Past scores remain saved as originally awarded; readers see a version warning. Consider an explicit migration if retroactive regrading is legally/educationally required.
- Renaming question IDs or test IDs breaks progress linkage. Never do this without a documented mapping and migration utility.
- Incompatible schema changes need a new schemaVersion and an old-backup migration, not a silent change to v1.

For details on adding tests and packaging future updates, see `ADDING-TESTS.md`.
