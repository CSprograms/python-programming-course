# UCAM11 Setup & Configuration Guide

Complete setup instructions for the UCAM11 Python Course Web App.

## Local Development Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/UCAM11.git
cd UCAM11
```

### Step 2: Regenerate Session Data

```bash
python3 build_data.py
```

This creates `web-app/data/sessions.json` from `Session_Programs/`.

### Step 3: Start Local Server

**Using Python (Recommended)**:
```bash
python3 -m http.server 8000 --directory web-app
# Open http://localhost:8000
```

**Using npm**:
```bash
npm run dev
# Open http://localhost:8000
```

## Project Configuration

### Customizing Build Process

Edit `build_data.py` to modify unit definitions:

```python
UNITS = [
    {"number": "I", "title": "Introduction to Python", "start": 1, "end": 15},
    {"number": "II", "title": "Flow Control", "start": 16, "end": 30},
    # ... modify as needed
]
```

### Customizing Web App

**Edit `web-app/index.html`**:
- Page title
- Course metadata
- External library imports

**Edit `web-app/css/style.css`**:
- Color scheme (CSS variables at the top)
- Fonts, spacing, layout

**Edit `web-app/js/app.js`**:
- Search behavior
- Sidebar layout
- Code highlighting options

### Netlify Configuration

File: `netlify.toml`

Key settings:
```toml
[build]
  publish = "web-app"          # Directory to deploy
  command = ""                 # No build needed

[dev]
  command = "python3 -m http.server 8000"
  port = 8000
```

## Adding Session Programs

### Format

Each `.py` file in `Session_Programs/` should have this docstring format:

```python
"""
Session N: Program Title

Description of what the program teaches.

Sample Output:
Enter a number: 5
Output: 25

Try also:
Session 4, Session 6
"""

# Your Python code here
```

### Steps

1. **Create the file**:
   ```bash
   cat > Session_Programs/Session_42.py << 'EOF'
   """
   Session 42: Dictionary Operations
   
   Learn how to create, access, and modify dictionaries.
   
   Sample Output:
   {'name': 'Alice', 'age': 30}
   
   Try also:
   Session 41, Session 43
   """
   
   student = {"name": "Alice", "age": 30}
   print(student)
   EOF
   ```

2. **Regenerate data**:
   ```bash
   python3 build_data.py
   ```

3. **Test locally**:
   ```bash
   python3 -m http.server 8000 --directory web-app
   # Search for "Session 42" in the web app
   ```

4. **Commit and push**:
   ```bash
   git add Session_Programs/Session_42.py web-app/data/sessions.json
   git commit -m "Add Session 42: Dictionary Operations"
   git push origin main
   ```

## GitHub Actions Setup (Optional)

To enable automatic session data regeneration on GitHub:

1. **Add GitHub Secrets**:
   - Go to GitHub repo → Settings → Secrets and variables → Actions
   - Add `NETLIFY_AUTH_TOKEN` and `NETLIFY_SITE_ID`

2. **Workflow file is already included**:
   - Located at `.github/workflows/deploy.yml`
   - Automatically regenerates session data on push
   - Deploys to Netlify

## Environment Variables

For Netlify deployments, set variables in the dashboard:

1. Netlify Dashboard → Site settings → Build & deploy → Environment
2. Add variables as needed (optional for this static site)

## Troubleshooting

### Session data not generating

**Check**:
1. `Session_Programs/` directory exists
2. Files are named `Session_1.py`, `Session_2.py`, etc.
3. Python 3.9+ is installed: `python3 --version`

**Fix**:
```bash
python3 build_data.py
cat web-app/data/sessions.json | head
```

### Local server shows 404 errors

**Check**:
1. You're in the UCAM11 directory
2. `web-app/` folder exists with `index.html`
3. Server is running correctly

**Fix**:
```bash
ls -la web-app/index.html
python3 -m http.server 8000 --directory web-app
```

### Changes not showing on deployed site

**Check**:
1. Files committed: `git status`
2. Push successful: `git log --oneline -5`
3. Netlify build successful: Check dashboard → Deploys

**Fix**:
```bash
git add .
git commit -m "Update session data"
git push origin main
# Wait 30 seconds for Netlify
# Hard refresh: Ctrl+Shift+R
```

## Next Steps

1. Customize branding (colors, fonts, layout)
2. Set up custom domain (optional)
3. Configure analytics (optional)
4. Add CI/CD workflow (already included)
5. Invite collaborators

---

For deployment instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md).
