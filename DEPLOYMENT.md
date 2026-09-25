# UCAM11 Deployment Guide

Complete instructions for deploying the UCAM11 Python Course Web App to Netlify.

## Prerequisites

- GitHub account with the UCAM11 repository
- Netlify account (free tier is sufficient)
- Git installed on your local machine
- Python 3.9+ (optional, only if regenerating session data)

## Automated Deployment (Recommended)

### Step 1: Connect Repository to Netlify

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Initial UCAM11 project setup"
   git push origin main
   ```

2. **Go to [netlify.com](https://netlify.com)** and sign in with your GitHub account

3. **Click "Add new site"** → **"Import an existing project"**

4. **Select GitHub** as your provider and authorize Netlify

5. **Choose your UCAM11 repository** from the list

6. **Build settings** should auto-detect:
   - **Base directory**: (leave empty)
   - **Build command**: (leave empty — no build needed)
   - **Publish directory**: `web-app`

7. **Click "Deploy site"**

   Your site is now live! Netlify will assign a random subdomain like `random-name-12345.netlify.app`.

### Step 2: Configure Custom Domain (Optional)

1. In the Netlify dashboard, go to **Site settings** → **Domain management**
2. Under **Custom domains**, click **Add custom domain**
3. Enter your domain (e.g., `ucam11.example.com`)
4. Follow Netlify's DNS configuration instructions
5. Once DNS is set up, your site is accessible at your custom domain

## Automatic Deploys

Every time you push to `main`:

1. Netlify detects the push
2. The `web-app/` directory is deployed
3. Your site updates instantly (~30 seconds)

### Monitoring Deployments

1. Netlify dashboard → **Deploys**
2. Each deployment shows status, logs, timestamp, and commit message

## Manual Deployment

Using Netlify CLI:

```bash
npm install -g netlify-cli
netlify login
netlify deploy --prod --dir=web-app
```

## Regenerating Session Data

If you've added or edited session programs:

```bash
python3 build_data.py
git add web-app/data/sessions.json
git commit -m "Update session data"
git push origin main
```

Netlify auto-deploys; no manual action needed.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Site not updating after push | Check Netlify's **Deploys** tab for errors |
| "Publish directory not found" | Ensure `web-app/` folder exists and contains `index.html` |
| Build command failing | Leave build command empty (static site) |
| Old content showing | Hard refresh: Ctrl+Shift+R or clear browser cache |
| Data not updating | Run `python3 build_data.py` and re-push |

## Rollback

To revert to a previous deployment:

1. Netlify dashboard → **Deploys**
2. Find the good version
3. Click **...** → **Publish deploy**

The previous version is immediately live.

## Security & Performance

- ✓ Free automatic HTTPS
- ✓ Security headers configured
- ✓ Aggressive caching for static assets
- ✓ Fresh content on updates

---

For detailed setup instructions, see [SETUP.md](./SETUP.md).
