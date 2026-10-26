# Ruang Uji — independent, expandable practice-test website

**Baseline release: `1.0.0` · 26 October 2026**  
**Platform:** plain HTML, CSS, native ES modules, JSON · **Hosting:** Cloudflare Pages · **Accounts/database:** none.

Ruang Uji is a separate project with its own identity, repository, JSON catalogue, assessment engine, and versioned browser storage. Langkah English was inspected only as an example of an approachable quiz/explanation experience. **Its files are neither included, imported nor modified.**

## Start here

1. Unzip this archive to its own folder, for example `ruang-uji`.
2. Open a terminal in that folder (Linux Mint).
3. Run `python3 -m http.server 8000`.
4. Open `http://localhost:8000/` in your browser. **Do not double-click `index.html` directly**, because ES modules and `fetch()` need HTTP.
5. Open the test card in either **Mode Latihan** or **Mode Tes**. Answer questions and submit to see the result and full review.
6. Before public deployment, **verify your permission to republish the questions and reading texts** extracted from the supplied PDF. Uploading a PDF to a private chat alone does not establish redistribution rights.

To run automated checks from the same directory:

```bash
python3 tools/validate.py
node --test tests/*.test.mjs
```

The site itself does not require Node or Python; these are developer/validation helpers only. The special source-extraction utility `tools/extract_source.py` uses optional **PyMuPDF** (`fitz`) and is **not** needed to add ordinary JSON tests or host the site.

## Files and folders

| File / directory | Purpose |
|---|---|
| `index.html` | Searchable test catalogue, local history indicators, backups |
| `test.html` | Reusable practice/test interface, questions and passages |
| `results.html` | Saved results, option-by-option feedback and evidence |
| `css/style.css` | Responsive, standalone presentation; system fonts |
| `js/home.js` | Catalogue filtering and backup controls |
| `js/test.js` | Answer interactions, navigation, optional stopwatch, local draft and submission |
| `js/results.js` | Saved review interface, including Indonesian translations |
| `js/scoring.js` | Pure grading code (unit tested) |
| `js/storage.js` | Browser-local versioned persistence and JSON backup/import |
| `js/common.js` | Safe text output and JSON loading |
| `data/catalog.json` | List of published test IDs, file paths, metadata |
| `data/tests/*.json` | One content JSON per independent practice test |
| `data/source_extracted.json` | Source-extracted baseline for PDF-fidelity regression checks |
| `assets/` | Brand icon and future per-test assets |
| `docs/question-inventory.json` | Every PDF question’s stable ID, number, format, source page and passage |
| `docs/CONTENT-VERIFICATION.md` | Extraction, independently reasoned keys, unresolved issues |
| `docs/DEPLOYMENT.md` | Step-by-step GitHub Desktop (Linux Mint) and Cloudflare Pages |
| `docs/ADDING-TESTS.md` | Stable-ID and version-safe future PDF expansion workflow |
| `docs/DATA-SCHEMA.md` | JSON schema, scoring policy, backups and examples |
| `tools/validate.py` | Offline JSON, reference, fidelity and scoring-key checks |
| `tests/*.test.mjs` | Scoring regression tests with Node’s built-in test runner |
| `.github/workflows/validate.yml` | GitHub Actions validation after push/PR |

## User experience

**Mode Latihan:** No time limit. Reading passage remains available beside the question on large screens; on smaller screens students can open a focused reading dialog without losing their place. Question translations and individual option translations are hidden initially; they can be revealed as needed. After responding, learners can check the answer, read Indonesian reasoning, literal English evidence and per-option justifications. Students can revise previously checked responses.

**Mode Tes:** Does not show keys, translations, explanations or hints until submission. Includes question navigation and a visible answered-count indicator. There is **no official time limit** in the provided PDF. The stopwatch is explicitly **optional**, starts only on student request, and has no automatic submission.

**Hasil:** Displays the saved attempt’s total, separates incorrect/unanswered from ungradable problems, and provides expandable review for every question. Reading passages, translations, evidence, vocabulary and the reasoning for each answer option are available after submission. Students can retake the test.

**Storage:** `localStorage` key `ruang-uji-progress-v1`, with JSON `{schemaVersion: 1, drafts: {...}, history: {...}}`. Attempts are appended to `history[testId]` and drafts keyed by `testId:practice`/`testId:test`. No accounts, cookies for tracking, analytics, third-party fonts, API keys, database or network calls beyond static file requests. Browsing in private mode or clearing browser data may erase progress. Backups allow export/import and merge histories by attempt ID; **there is no cross-device synchronization**.

## Scoring and source caution

Single-answer questions are scored by an exact selection. Multi-select answers receive **one point for the exact set**, with no partial credit. Three-row Yes/No questions receive **one point only when every row is correct**, with no partial credit. Blank answers on gradeable questions receive zero. The provided PDF contains **no official key**, so all proposed keys are **independently derived and nonofficial**. Questions **4, 5 and 19** have genuinely problematic wording and are **excluded from both the numerator and denominator**, even if a student enters an answer. The first test is scored out of **17** verified-for-use questions, not 20. See the [content verification report](docs/CONTENT-VERIFICATION.md) before relying on these results for high-stakes decisions.

## Adding a test

Copy the shape of `data/tests/tka-eng-to03.json` (but use a **new ID and separate file**), include every question and passage, add the entry to `data/catalog.json`, run validation, and commit to GitHub. The HTML and JS should **not** be edited for ordinary new test additions. Detailed instructions, backward-compatibility advice, and patch-ZIP guidance appear in [ADDING-TESTS.md](docs/ADDING-TESTS.md).

## Accuracy and verification limitations

The supplied PDF is **eight digitally selectable, text-only pages** and contains **20 questions, five texts, no embedded images, no supplied key and no explanations**. The original options/reading passages are extracted from that file and compared verbatim (after PDF line wrap normalization) to `data/source_extracted.json` during validation. English evidence snippets are required to occur **literally** in their source passage. The author has not provided copyright ownership, licensing, or redistribution permission.

Automatic validation and pure scoring regression checks were executed. See `docs/CONTENT-VERIFICATION.md` for their results and additional limitations. An admin-managed browser on the authoring environment blocked navigation, so the UI could not be fully browser-smoke-tested there; desktop/mobile visual checks and real-device assistive-technology checks should be performed locally before public release. There is no claim of official test endorsement.
