# UCAM11 Netlify Deployment — Pre-Launch Checklist

## ✅ Configuration Setup Complete

### Core Configuration Files
- [x] `netlify.toml` — Netlify deployment configuration
  - Static site publishing (web-app directory)
  - Security headers configured
  - Cache control policies set
  - SPA routing enabled
  
- [x] `package.json` — NPM project metadata
  - Development scripts configured
  - Project metadata defined
  - Dependencies listed
  
- [x] `.gitignore` — Git ignore rules
  - Node modules, Python cache, environment files excluded
  - IDE settings, OS files excluded
  
- [x] `.env.example` — Environment variable template
  - Analytics, Netlify tokens documented

### Documentation
- [x] `README.md` — Main project documentation
- [x] `DEPLOYMENT.md` — Deployment guide
- [x] `SETUP.md` — Setup and configuration
- [x] `SETUP_SUMMARY.md` — Quick reference
- [x] `DEPLOYMENT_CHECKLIST.md` — This file

### Web App
- [x] `web-app/_redirects` — SPA routing configuration
- [x] `web-app/index.html` — App shell (existing)
- [x] `web-app/css/style.css` — Styling (existing)
- [x] `web-app/js/app.js` — App logic (existing)
- [x] `web-app/data/sessions.json` — Session data (existing)

### CI/CD
- [x] `.github/workflows/deploy.yml` — GitHub Actions workflow
  - Auto-regenerates session data on push
  - Validates JSON data
  - Deploys to Netlify
  - Comments on PRs

---

## 🚀 Before Deploying

### Local Testing
- [ ] Verify session data regenerates: `python3 build_data.py`
- [ ] Test local server: `python3 -m http.server 8000 --directory web-app`
- [ ] Open http://localhost:8000 and test functionality
- [ ] Test search feature with various keywords
- [ ] Check syntax highlighting works
- [ ] Test responsive design (resize browser or use mobile view)

### Git Setup
- [ ] Commit all new files: `git add .`
- [ ] Review commits: `git log --oneline -10`
- [ ] Verify `.gitignore` working: `git status` (should not show node_modules, etc.)

### GitHub Setup
- [ ] Push to GitHub: `git push origin main`
- [ ] Verify all files appear on GitHub.com
- [ ] Repository is public (or collaborators have access)

---

## 📋 Deployment Steps

### Step 1: Connect to Netlify
1. [ ] Go to https://netlify.com and sign in with GitHub account
2. [ ] Click "Add new site" → "Import an existing project"
3. [ ] Select GitHub repository
4. [ ] Verify build settings:
   - Base directory: (empty)
   - Build command: (empty)
   - Publish directory: `web-app`
5. [ ] Click "Deploy site"

### Step 2: Verify Deployment
- [ ] Check deployment status in Netlify dashboard
- [ ] Open assigned subdomain (e.g., random-name-12345.netlify.app)
- [ ] Verify site loads correctly
- [ ] Test search functionality
- [ ] Verify session data loads

### Step 3: Configure GitHub Actions (Optional)
1. [ ] Go to GitHub repo → Settings → Secrets and variables → Actions
2. [ ] Add `NETLIFY_AUTH_TOKEN` (from Netlify → User settings → Applications)
3. [ ] Add `NETLIFY_SITE_ID` (from Netlify → Site settings → API ID)
4. [ ] Workflow is now active and will auto-deploy on push

### Step 4: Custom Domain (Optional)
1. [ ] In Netlify dashboard → Site settings → Domain management
2. [ ] Click "Add custom domain"
3. [ ] Enter your domain (e.g., ucam11.example.com)
4. [ ] Follow DNS configuration instructions for your registrar
5. [ ] Verify DNS propagation (can take up to 24 hours)

---

## 🔍 Post-Deployment Verification

### Functionality
- [ ] Homepage loads without errors
- [ ] Search works (try "Session 1", "dictionary", "loop")
- [ ] All 75 sessions are accessible
- [ ] Code syntax highlighting works
- [ ] Mobile responsive (check with F12 → Responsive Design Mode)
- [ ] Navigation works smoothly
- [ ] No JavaScript errors (F12 → Console)

### Performance
- [ ] Page loads in < 2 seconds
- [ ] Syntax highlighting loads properly
- [ ] No broken images or resources (F12 → Network)

### Security
- [ ] Site uses HTTPS (lock icon in browser)
- [ ] No mixed content warnings (F12 → Console)
- [ ] Security headers are set (check via: https://securityheaders.com)

### Analytics
- [ ] (Optional) Google Analytics configured if added
- [ ] (Optional) Sentry error tracking working if configured

---

## 📝 Ongoing Maintenance

### Adding Sessions
- [ ] Create Session_N.py in Session_Programs/
- [ ] Include proper docstring format
- [ ] Run `python3 build_data.py`
- [ ] Verify sessions.json updated
- [ ] Commit and push
- [ ] Auto-deployed by GitHub Actions

### Updating Code
- [ ] Edit files locally
- [ ] Test changes: `npm run dev`
- [ ] Commit changes
- [ ] Push to GitHub
- [ ] Auto-deployed by GitHub Actions

### Monitoring
- [ ] Check Netlify dashboard occasionally for deploy status
- [ ] Monitor GitHub Actions workflow runs
- [ ] Monitor error tracking if configured

### Updates
- [ ] Keep dependencies updated (Highlight.js, etc.)
- [ ] Monitor Netlify and GitHub security alerts
- [ ] Keep documentation current

---

## ❓ FAQ

**Q: Do I need to manually deploy after pushing?**  
A: No! GitHub Actions automatically regenerates session data and Netlify auto-deploys when code is pushed to main.

**Q: How do I test locally before deploying?**  
A: Run `python3 -m http.server 8000 --directory web-app` and open http://localhost:8000

**Q: Can I rollback a bad deployment?**  
A: Yes! In Netlify dashboard → Deploys → Find good version → Click "..." → "Publish deploy"

**Q: How do I add analytics?**  
A: See SETUP.md → Environment Variables for Google Analytics setup

**Q: How do I use a custom domain?**  
A: See DEPLOYMENT.md → Step 2 or GitHub → Domain Management

---

## 🎉 Ready to Launch!

Once all items in this checklist are complete, your UCAM11 course web app is ready for production use.

**Next Step**: Start with "Local Testing" section above.

---

**Status**: ✅ Configuration complete — ready to follow this checklist!
