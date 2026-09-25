# Session Viewer (web app)

A static, no-build web app that browses all 75 sessions of the
UCAM11I Python Programming course — code, description, and the
documented sample output for each program.

## Structure

```
web-app/
├── index.html          # app shell
├── css/style.css        # all styling (no framework)
├── js/app.js             # renders sidebar + session view from data/sessions.json
├── data/sessions.json    # generated — do not hand-edit, see below
└── README.md
```

## Run it locally

No build step. From this folder:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Regenerating the data

`data/sessions.json` is generated from `Session_Programs/` by
`../build_data.py`. Whenever session content changes (new sessions
added, programs edited), re-run it from the repo root:

```bash
python3 build_data.py
```

This re-parses every `.py` file's docstring (title, description,
sample output, "try also" hint) and every no-code session's
`README.md`, and rewrites `data/sessions.json`. Commit the
regenerated file along with your content changes.

## Deploying

This repo has a `netlify.toml` at the root (`publish = "web-app"`,
no build command), so connecting the repo in Netlify's dashboard
deploys this folder with no manual configuration.
