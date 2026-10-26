# Publish Ruang Uji — beginner guide (Linux Mint / GitHub Desktop / Cloudflare Pages)

This guide applies to **Ruang Uji baseline `1.0.0` (26 October 2026)**, **not** to the separate Langkah English website.

> **Before publishing:** the PDF's redistribution rights were not supplied. The test JSON includes its English passages and questions verbatim, so **confirm your right to publish the material** and any needed attribution/licence first. Hosting a public site, including a public Cloudflare Pages site linked to a private GitHub repository, makes the text accessible to visitors. There is no claim of official exam endorsement.

## 1. Prepare the website folder

1. Download and unzip `ruang-uji-v1.0.0-complete-site.zip` (the archive accompanying this guide).
2. Place the extracted files in their **own** folder, for example `~/Projects/ruang-uji/`. The folder must contain `index.html`, `test.html`, `results.html`, `css/`, `js/`, `data/`, etc **directly at the top level**. Do not have an extra nested `ruang-uji/ruang-uji/` level if you plan to use the root as a Cloudflare build output directory.
3. If you have Python 3 installed (usual on Linux Mint), open a terminal in that folder and run:

   ```bash
   python3 -m http.server 8000
   ```

4. In Firefox or another ordinary browser, visit `http://localhost:8000/`, open the first test, and click through the questions. To stop the preview server, press Ctrl+C in the terminal.
5. Optional: run `python3 tools/validate.py`, and, if Node.js is installed, `node --test tests/*.test.mjs`. These are **checks**, not deployment dependencies.

## 2. Install/sign in to GitHub Desktop on Linux Mint

**Important:** Official GitHub Desktop does **not** support Linux; Linux packages come from the **community-maintained Shiftkey fork**. See GitHub's official project (`https://github.com/desktop/desktop`) and the Linux fork (`https://github.com/shiftkey/desktop`) for current details. Use a community release suitable for your Linux Mint/Ubuntu version. A `.deb` package may be installed using Mint's package installer. Do not download unverified installers from unrelated websites. Alternative: use Git on the command line or another Mint Git client.

Open the Linux build of GitHub Desktop. Sign in to your GitHub account through the app. Keep the Ruang Uji folder **separate** from the Langkah English folder/repository.

## 3. Create a new Ruang Uji repository

**Option A — from the existing folder in Desktop:**

1. In GitHub Desktop use **File → Add Local Repository…**.
2. Choose your `ruang-uji` folder.
3. If Desktop says that it is not a Git repository, use its **Create a Repository Here** option (UI wording may vary). Set a name such as `ruang-uji-practice` and description such as “Independent interactive English practice tests”.
4. Ensure your branch is `main` (if necessary: **Branch → Rename**).
5. In the changes panel, review the initial files. Enter a summary such as `Initial Ruang Uji 1.0.0 site` and click **Commit to main**.
6. Click **Publish repository**. **Keep it private while copyright/permission remains unresolved.** GitHub repository privacy is independent of whether a deployed Pages site is public.

**Option B — if Desktop cannot initialize the existing folder:** use a terminal **inside** `ruang-uji`:

```bash
git init -b main
git add .
git commit -m "Initial Ruang Uji 1.0.0 site"
```

Then in GitHub Desktop choose **File → Add Local Repository** and **Publish repository**. If Git asks for a name/email, configure your Git author identity as the prompts direct (do not put passwords in commands). Do not add the entire ZIP itself to the folder alongside the extracted files.

At GitHub, verify the repo's root contains `index.html` and `data/catalog.json`. The first GitHub Actions run should execute validation and scoring tests. Do not treat an Actions pass as a substitute for checking the site in a browser.

## 4. Connect the repo to Cloudflare Pages

Only after confirming redistribution permission:

1. Sign in at `https://dash.cloudflare.com/`.
2. Open **Workers & Pages → Create application → Pages** and choose **Import an existing Git repository** or **Connect to Git** (the exact labels may change).
3. Authorize the Cloudflare Pages GitHub integration to read the new **Ruang Uji** repository. Select that repo, not Langkah English.
4. Enter a project name, for example `ruang-uji-practice` (availability depends on Cloudflare).
5. Select **Production branch: `main`**.
6. In build configuration choose **Framework preset: None** or no framework. Set **Build command: `exit 0`** (Cloudflare's static HTML guide permits this; leaving it blank is another no-build choice). Set **Build output directory: `.`** (a single dot — site files live in repository root). Leave root/project directory at the repository root, or blank when applicable.
7. You do **not** need API tokens, a build tool, installation commands, a database, environment variables, or a paid service for this site.
8. Start deployment. Cloudflare will assign a `*.pages.dev` URL. Open it and verify the homepage and other pages load. If the homepage is a 404, check that `index.html` exists at the **build output root** rather than in a nested directory.

Official Cloudflare docs: `https://developers.cloudflare.com/pages/framework-guides/deploy-anything/` and `https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/`.

Cloudflare Pages typically redeploys automatically when you push new commits to the linked production branch. A change pushed to a feature branch may create a preview instead of production.

## 5. Verify the live site manually

Use an ordinary desktop browser **and** a phone or narrow responsive viewport. Check these actions before sharing the URL:

- Home: catalogue card appears; search for `Labuan` finds the test; status filters change after an attempt.
- Mode Latihan: passages can be read, questions 1–20 appear once, option translations start hidden, clicking an option and **Periksa jawaban** shows an evidence-based explanation. In Q1, selecting **B** should be correct. Q4 and Q5 should be **unresolved / not graded**, not silently assigned keys.
- Passage navigation: the passage switches at Q6, Q11, Q14 and Q18; on a phone, use **Buka teks bacaan** and close it to return to the current question.
- Multiple-answer: in Q11 select **A, B, E** and check; selecting only **A, B** must **not** receive a point.
- Category: in Q18 choose **A Yes, B Yes, C No**; all rows must be answered before the question is marked complete. Q19 must be shown as unresolved.
- Mode Tes: does **not** reveal translations, answers or explanations before submission. Stopwatch is optional and no official time is implied.
- Result page: shows **17** graded questions in the denominator and three unresolved ones. Every review entry includes question text, your answer, translations and option-level explanations; can filter problem questions. Retake leads to a new draft.
- Local persistence: answer a few questions, refresh, and verify they remain selected. Submit, return to home, and open latest result. Export JSON backup, then import a backup in another browser/profile and verify history is present. Import never deletes existing results by design.
- Keyboard/screen-reader checks: tab through cards, answer controls and buttons, check focus indication and label announcements, verify that the reading dialog opens/closes. On a phone, make sure the document does not scroll horizontally and reading controls remain usable.
- If direct URL navigation works on homepage but `/test.html` or `/results.html` fails, verify those files were deployed, and ensure relative `data/` fetch URLs return actual JSON rather than HTML error pages.

## 6. Publish future updates

1. Put your new/changed files into the local **Ruang Uji** folder, preserving its current structure and stable IDs.
2. Run `python3 tools/validate.py` and `node --test tests/*.test.mjs`.
3. In GitHub Desktop inspect the changed-file list, **Commit to main**, then **Push origin**.
4. Open Cloudflare **Workers & Pages → your Pages project → Deployments**; confirm the latest `main` build finishes, then check the public site.
5. Keep the same repository/project. Never start over or replace old test IDs to publish a new test. Student backups remain compatible across **additive** v1 changes.

For each future PDF use `docs/ADDING-TESTS.md`. If you use a patch ZIP from a subsequent update, it must state precisely which **baseline version** it applies to; always make a backup of the repo before overlaying a patch.
