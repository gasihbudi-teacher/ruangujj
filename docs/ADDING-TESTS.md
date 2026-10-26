# Safely add a new PDF as another independent test

**Required baseline for initial future patches: Ruang Uji complete-site `1.0.0` (26 October 2026).** If your repo has changed since that release, ask that patch authors compare your actual latest archive or commit. Do not blindly overlay a patch intended for a different baseline.

The library is designed to add a new test without touching existing application code or rewriting existing tests.

## 1. Inspect and inventory the next PDF

- Count every question; record original numbers, pages, passages, formats, answer options, any diagrams/figures/tables, references and instructions.
- Check whether a source answer key is supplied and **record its provenance**. Independently cross-check it. A missing key can be reasoned from the source, but label it *independent*, never *official*. Mark truly unresolved or ambiguous problems **ungradable** (`graded: false; answer: null`).
- Preserve English original questions, options and passage wording, including unusual or duplicated choices. Document OCR or source defects outside those fields.
- Translate the passage, every question and every option to accurate Indonesian. Write an educational Indonesian explanation **specific to that question** plus individual reasons for the right and wrong choices. Include literal source evidence and optional vocabulary.
- Confirm source rights, attribution and permission before public release. Scanning/uploading a PDF is not itself public redistribution permission.

## 2. Create a new test file

Use a **new** slug, e.g. `tka-eng-to04-community-reading`, that has never been used for another test. Create `data/tests/tka-eng-to04-community-reading.json`. Follow `docs/DATA-SCHEMA.md` or copy the *structure* of the existing JSON without copying its content or identifiers. Fill:

- `schemaVersion: 1`, stable `id`, `title`, subject, exam/topic/year metadata only when known, number of questions, `contentRevision: 1`.
- `passages` with unique IDs, complete English text, complete Indonesian translation, source page and question range.
- `questions` with stable IDs, original numbering, source page, supported type, linked passage ID, exact options, translated options, independently reviewed key or an unresolved designation, explanation, per-option reasons, literal quotations and notes on source problems.
- `questionCount` equal to the actual array length; count every format and every original question exactly once.

If the new PDF has diagrams, store optimized, legible images in `assets/tests/<new-test-id>/`. Set references with paths in `assets/tests/...` and verify them. Images must not be replaced with guesses from OCR. For a truly **new interaction format** beyond single/multiple/category, extend the scoring engine and UI **with additional automated tests**; never silently change the source format to fit existing controls.

## 3. Register it in the catalogue

Append exactly **one** object to the `tests` array in `data/catalog.json`, with the same stable ID and correct `path`, count and **gradable** count. Do not edit or remove older catalogue entries. Use `null` for unknown years/durations; do not invent official time limits.

If the PDF is a completely different examination or subject, use the existing generic metadata fields; do not rename the application to accommodate a single test.

## 4. Validate before pushing

Run:

```bash
python3 tools/validate.py
node --test tests/*.test.mjs
```

The static validator checks malformed JSON, missing/duplicate IDs, counts, invalid answer references, missing translations and explanations, missing passage references, unsupported formats, absent evidence, quotes that do not appear in the passage, missing asset files and exact original text integrity for the initial test. **It does not judge whether a newly invented answer is semantically correct.** Review answers and translations manually with the PDF and, ideally, a second human reviewer. Also manually test each format in a browser before publishing.

For each new PDF, add a source-specific inventory and regression baseline if you want original-vs-extracted checks as strict as the first test. Do not overwrite `data/source_extracted.json`, which is specifically the **first PDF's** verified extraction baseline. Name additional baselines for their test IDs and extend the validator where needed.

## 5. Preserve progress and older functionality

- Keep existing `data/tests/*.json` intact unless an existing key/translation genuinely needs correction. Preserve every existing `test.id` and `question.id` and meaning.
- Never delete a prior question and reuse its identifier for a different item. Old attempt records refer to these IDs.
- If a previously published test needs a correction, update its `contentRevision`, explain the change in release notes, and be explicit that previously saved scores remain as originally recorded. Follow a migration plan before any breaking schema or ID change.
- Keep `schemaVersion: 1` in additive releases. If a later release changes the shape of progress backups, provide an import migration for older backups first.
- Re-run the old scoring tests and manual smoke checklist after every update. A new test must not break earlier ones.

## 6. Updating GitHub / Cloudflare

Commit the new JSON, catalogue change, accompanying assets, editorial issue report and any new regression tests. Push through GitHub Desktop to the **same** repo's `main` branch. Cloudflare Pages will usually deploy that commit automatically.

## 7. Patch ZIPs versus full-site ZIPs

For an additive future test, deliver **both** if useful:

**Patch ZIP:** contains only changed/new relative files, for example:

```
PATCH-MANIFEST.md
 data/catalog.json
 data/tests/tka-eng-to04-community-reading.json
 assets/tests/tka-eng-to04-community-reading/example-diagram.svg
 docs/reviews/tka-eng-to04.md
```

Patch manifest must state: `Requires exactly Ruang Uji baseline 1.0.0` (or the specific later tag/commit), files to replace/add, checksum of critical files if available, any changed answer keys/ID migrations, validation commands and expected counts. A replacement `data/catalog.json` must contain all previously published test entries. Do not send a patch which replaces the whole `data/tests/` folder.

**Updated complete-site ZIP:** contains the entire independent repository at the new version, including every earlier test and all docs. This is preferable when there are application changes or when a patch's baseline is uncertain. Keep the previous complete-site ZIP as a rollback checkpoint.

### Future request to reuse

> Please convert this PDF into a **new** practice test for my existing Ruang Uji website. Base the update on my attached **latest complete-site ZIP** (currently 1.0.0 unless updated). Inventory all source questions, preserve original English wording, verify keys, write Indonesian passage/question/option translations with evidence and per-option explanations, flag unresolved items, add the test JSON and catalogue entry without changing old IDs, run the regression checks, and provide both a patch ZIP naming its exact required baseline and a full updated ZIP.
