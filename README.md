# UCAM11 — Python Programming Course Web App

A modern, responsive web application to browse and explore all 75 sessions of the **UCAM11I Python Programming** course, organized into 5 units by topic.

## Features

- **75 Sessions organized by unit** — Introduction to Python, Flow Control, Functions and Exception Handling, Strings and Lists, Tuples and Dictionaries
- **Full code with syntax highlighting** — View source code with color-coded Python syntax
- **Docstring metadata** — Title, description, sample output, and "try also" references for each program
- **Fast search** — Find sessions and programs by name, keyword, or session number
- **Responsive design** — Works on desktop, tablet, and mobile
- **No dependencies** — Static HTML/CSS/JavaScript; zero build required
- **Offline capable** — Data is bundled; works without internet after first load

## Quick Start

### Run Locally

```bash
# From the repo root
python3 -m http.server 8000 --directory web-app

# Open http://localhost:8000
```

Or use npm scripts:

```bash
npm install    # Optional; no dependencies to install, but creates a reference
npm run dev
```

### Regenerate Session Data

Session data is stored in `web-app/data/sessions.json`. Whenever you add, edit, or remove session programs:

```bash
python3 build_data.py
```

This script:
1. Scans `Session_Programs/` for all `.py` files
2. Extracts each file's docstring (title, description, sample output, hints)
3. Rewrites `web-app/data/sessions.json`

**Always commit the regenerated JSON along with your content changes.**

## Project Structure

```
UCAM11/
├── web-app/                      # Static web app (published to Netlify)
│   ├── index.html                # App shell
│   ├── css/style.css             # All styling (no framework)
│   ├── js/app.js                 # App logic and rendering
│   ├── data/sessions.json        # Auto-generated session data
│   └── README.md                 # Web app documentation
├── build_data.py                 # Builds sessions.json from Session_Programs/
├── netlify.toml                  # Netlify deployment config
├── package.json                  # NPM metadata
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## Deployment

This project is hosted on **Netlify** and deploys automatically on every push to `main`.

### Manual Deployment

```bash
npm run build                      # Regenerate session data if needed
npm run deploy                     # Deploy to Netlify (requires Netlify CLI)
```

### Environment Setup

1. **Fork/clone the repository** on GitHub
2. **Connect to Netlify**:
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Select your GitHub repo
   - Build settings should auto-detect (`netlify.toml`)
   - Deploy

3. **Custom domain** (optional):
   - In Netlify dashboard → Site settings → Domain management
   - Add your custom domain

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed deployment steps.

## Development

### Technology Stack

- **HTML5** — Semantic, accessible markup
- **CSS3** — No frameworks; vanilla CSS with CSS variables for theming
- **JavaScript (ES6+)** — Vanilla JS; no build, no dependencies
- **Highlight.js** — Code syntax highlighting (CDN)
- **Google Fonts** — Public Sans, JetBrains Mono (CDN)

### Adding Sessions

1. Add your `.py` files to `Session_Programs/`
2. Write clear docstrings following the course format:
   ```python
   """
   Session N: Description
   
   Full description of what the program teaches.
   
   Sample Output:
   Output goes here
   
   Try also:
   Session X, Session Y
   """
   ```
3. Run `python3 build_data.py`
4. Commit both the new `.py` files and the regenerated `web-app/data/sessions.json`

### Customizing the UI

- **Colors/fonts**: Edit `web-app/css/style.css` (CSS variables at the top)
- **Layout**: Modify `web-app/index.html` and `web-app/js/app.js`
- **Search/filtering**: Update logic in `web-app/js/app.js`

## Performance

- **Load time**: < 1 second (static HTML/CSS/JS)
- **Bundle size**: ~200 KB gzipped (including all session data)
- **Caching**: Aggressive caching for static assets, fresh content on updates

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Android)

## Security

- No server-side code or database
- No user input processed; all data is read-only
- Security headers configured in `netlify.toml`
- CSP and CORS handled by Netlify

## Contributing

1. Fork the repo
2. Create a branch (`git checkout -b feature/your-feature`)
3. Make changes and test locally
4. Run `python3 build_data.py` if you added/edited sessions
5. Commit with clear messages
6. Push and open a Pull Request

## License

MIT — See LICENSE file for details

## Author

**Aravindhan Mohan**  
Assistant Professor, Department of Computer Science  
Sri Sankara Arts and Science College (Autonomous)  
Kancheepuram, Tamil Nadu, India

---

**Questions or feedback?** Open an issue or contact the course instructor.
