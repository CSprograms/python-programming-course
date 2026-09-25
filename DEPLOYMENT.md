# Deploying the Session Viewer to Netlify

The site uses **Netlify's Git integration**. Netlify reads `netlify.toml`:

| Setting | Value | Why |
|---|---|---|
| Build command | `python3 build_data.py` | Regenerates `web-app/data/sessions.json` (from `Session_Programs/`) and `question_bank.json` (from `Question_Bank/question_bank.csv`) |
| Publish directory | `web-app` | The static site |
| Functions | none | Everything runs in the browser |

GitHub Actions (`.github/workflows/validate.yml`) **does not deploy**. It checks
that every program compiles and that the generated data has all 75 sessions.
It also warns you if the committed `sessions.json` is out of date.

## One-time setup

1. Push the repository to GitHub (`CSprograms/python-programming-course`).
2. Sign in at <https://app.netlify.com> → **Add new site** → **Import an existing project** → **GitHub**.
3. Pick the `python-programming-course` repository and the `main` branch.
4. Leave the build fields as Netlify pre-fills them from `netlify.toml`:
   Base directory *(empty)*, Build command `python3 build_data.py`,
   Publish directory `web-app`.
5. Click **Deploy**. The site goes live at `https://<random-name>.netlify.app`.
6. Optional: rename it under **Site configuration → Change site name**
   (for example `ucam11-python.netlify.app`), or add a custom domain under
   **Domain management**.

No tokens, secrets or environment variables are needed.

> If an older setup added `NETLIFY_AUTH_TOKEN` / `NETLIFY_SITE_ID` secrets for a
> GitHub Actions deploy, you can delete them. They are no longer used.

## Everyday updates

```bash
python build_data.py          # optional locally; Netlify also runs it
git add Session_Programs Question_Bank web-app/data
git commit -m "Update Session NN programs"
git push origin main          # Netlify builds and publishes in about a minute
```

## Caching

`app.js`, `style.css` and `sessions.json` keep fixed file names, so they are
served with `Cache-Control: max-age=0, must-revalidate`. Browsers check for a
new version on each visit and get a quick 304 reply when nothing has changed,
so students see updates right away without a hard refresh.

## Routing

The viewer uses hash links (`/#session-12`), so it needs no redirect rules.
Unknown paths show `web-app/404.html`.

## Pre-launch checklist

- [ ] `python build_data.py` prints `Sessions: 75, Programs: 230, No-code sessions: 15`
      (the numbers change if you add programs)
- [ ] The local server shows the home page, and a few sessions open correctly
      (for example 1, 12, 14, 40, 75)
- [ ] Search finds programs (try "dictionary" and "40")
- [ ] **Question Bank** (top bar) shows five unit cards. Each unit page opens, and its
      Part A / Part B / Part C tabs work (try `/#qb/unit-II/part-B`)
- [ ] The **Validate course data** workflow is green on GitHub
- [ ] The Netlify deploy log shows `Wrote …/web-app/data/sessions.json` and **Published**
- [ ] The live site works on a phone (the menu button opens the session list)

## Troubleshooting

| Symptom | Fix |
|---|---|
| Deploy fails at `python3 build_data.py` with "syntax error in Session_Programs/…" | Fix that program (the message gives the file and line), then push again |
| "Could not load session data" on the page | Open the Netlify deploy log and confirm the build step ran and `web-app/data/sessions.json` was written |
| Blank page when `index.html` is opened directly | Use a local server (see README); `file://` pages cannot fetch the data |
| Site not updating | Netlify → **Deploys**: check the latest deploy for errors; **Trigger deploy → Clear cache and deploy site** |

## Rollback

Netlify → **Deploys** → choose an earlier successful deploy → **Publish deploy**.

## Manual deploy (optional)

```bash
npm install -g netlify-cli
netlify login
python build_data.py
netlify deploy --prod --dir=web-app
```
