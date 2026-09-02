# Dr. Albert Poulose: Personal Website

Hugo-based academic portfolio site. Replaces [Google Sites](https://sites.google.com/view/albertpoulose/home) with a faster, cleaner layout.

## Current status

| Item | Status |
|------|--------|
| Local preview | Ready (`hugo server -D`) |
| Content & assets | Populated (publications, research pillars, gallery, PDFs) |
| CV | Public academic CV (print/save as PDF); optional hosted PDF at `static/files/cv/` |
| Google Analytics | GA4 configured (live site only; skipped on `hugo server`) |
| Site search | Client-side search at `/search/` (footer link; not in main nav) |
| GitHub Pages deploy | Workflow ready (`.github/workflows/deploy.yml`); repo not yet pushed |

**Production URL (after deploy):** `https://albert8943.github.io/dr-albert-poulose/`  
**Planned custom domain:** `albertpoulose.com` (buy and connect; see [Custom domain](#custom-domain))

## Features

- **Home:** research identity headline, featured PINN paper, selected publications, software, recent news
- **Research:** one-paragraph vision; three programs; visual pipelines; current / building-toward; long notes collapsed
- **Publications:** grouped by year; collapsible abstracts; Scholar/ORCID/Scopus; filter by research pillar
- **Teaching:** interests, short philosophy, and courses
- **Experience:** appointments and education (`/education/` redirects here)
- **Software:** PINN-TSA and related prototypes
- **CV:** public, one-click print/save; optional PDF download
- **Contact** and **Gallery:** linked from the footer (institutional email first; no home address or phone numbers)

## Local preview

This site is built with [Hugo](https://gohugo.io/). Run the dev server on your machine, then open the site at the same path used on GitHub Pages (with `/dr-albert-poulose/`).

### Prerequisites

**Hugo Extended is installed on this machine** via winget:

| | |
|---|---|
| Package | `Hugo.Hugo.Extended` |
| Version | 0.165.0 (extended) |
| Installed with | `winget install Hugo.Hugo.Extended` |

Check that it works:

```powershell
hugo version
```

Expected output:

```text
hugo v0.165.0+extended windows/amd64
```

If `hugo` is not recognized, Hugo is still installed. Your terminal may not have WinGet’s `Links` folder on `PATH` yet. Use the full path in step 1 below, or close and reopen your terminal (or restart Cursor) and try `hugo version` again.

### 1. Start the dev server

From the project root:

```powershell
cd D:\Albert_OneDrive\OneDrive\dr-albert-poulose
hugo server -D
```

If `hugo` is not on `PATH`, use the WinGet install location:

```powershell
cd D:\Albert_OneDrive\OneDrive\dr-albert-poulose
$hugo = "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\Hugo.Hugo.Extended_Microsoft.Winget.Source_8wekyb3d8bbwe\hugo.exe"
& $hugo server -D
```

- `-D` includes draft content.
- The server reloads automatically when you edit content or templates.
- Leave the terminal open while you browse; press **Ctrl+C** to stop.

Local preview uses `config/development/hugo.toml` with the same subpath as production:

| | Local | Production |
|---|---|---|
| Base URL | `http://localhost:1313/dr-albert-poulose/` | `https://albert8943.github.io/dr-albert-poulose/` |
| Config | `config/development/hugo.toml` | `config/_default/hugo.toml` |

You should see:

```text
Web Server is available at http://localhost:1313/dr-albert-poulose/
```

### 2. Open in your browser

Go to **http://localhost:1313/dr-albert-poulose/** (not `http://localhost:1313/` alone; that path has no site when mirroring GitHub Pages).

| Page | Path | Local URL | Production URL |
|------|------|-----------|----------------|
| Home | `/` | http://localhost:1313/dr-albert-poulose/ | https://albert8943.github.io/dr-albert-poulose/ |
| Research | `/research/` | http://localhost:1313/dr-albert-poulose/research/ | https://albert8943.github.io/dr-albert-poulose/research/ |
| Publications | `/publications/` | http://localhost:1313/dr-albert-poulose/publications/ | https://albert8943.github.io/dr-albert-poulose/publications/ |
| Teaching | `/teaching/` | http://localhost:1313/dr-albert-poulose/teaching/ | https://albert8943.github.io/dr-albert-poulose/teaching/ |
| Experience | `/experience/` | http://localhost:1313/dr-albert-poulose/experience/ | https://albert8943.github.io/dr-albert-poulose/experience/ |
| Software | `/software/` | http://localhost:1313/dr-albert-poulose/software/ | https://albert8943.github.io/dr-albert-poulose/software/ |
| Gallery | `/gallery/` | http://localhost:1313/dr-albert-poulose/gallery/ | https://albert8943.github.io/dr-albert-poulose/gallery/ |
| Contact | `/contact/` | http://localhost:1313/dr-albert-poulose/contact/ | https://albert8943.github.io/dr-albert-poulose/contact/ |
| CV | `/cv/` | http://localhost:1313/dr-albert-poulose/cv/ | https://albert8943.github.io/dr-albert-poulose/cv/ |
| Search | `/search/` | http://localhost:1313/dr-albert-poulose/search/ | https://albert8943.github.io/dr-albert-poulose/search/ |

### Install Hugo (other machines)

Only needed if Hugo is not installed yet. Requires [Hugo Extended](https://gohugo.io/installation/) **0.165+** (the extended build includes SCSS support).

**Windows (winget, recommended):**

```powershell
winget install Hugo.Hugo.Extended
```

**Windows (Chocolatey):**

```powershell
choco install hugo-extended
```

**Manual download:** [Hugo installation for Windows](https://gohugo.io/installation/windows/)

After installing, close and reopen your terminal, then run `hugo version`.

### Troubleshooting

**http://localhost:1313 does not load the site**

Use the full local base URL: **http://localhost:1313/dr-albert-poulose/**. Local preview mirrors the GitHub Pages subpath.

**The dev server is not running**

Start it (see step 1 above) and leave the terminal open. If port 1313 is busy, use another port and update the base URL to match:

```powershell
hugo server -D --port 1314 --baseURL "http://localhost:1314/dr-albert-poulose/"
```

Then open http://localhost:1314/dr-albert-poulose/ instead.

## Build

Requires Hugo Extended (already installed on this machine; see [Local preview](#local-preview)).

```powershell
hugo --minify
```

If `hugo` is not on `PATH`:

```powershell
$hugo = "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\Hugo.Hugo.Extended_Microsoft.Winget.Source_8wekyb3d8bbwe\hugo.exe"
& $hugo --minify
```

Output in `public/`. Open `public/index.html` in a browser, or serve the folder with any static file server, to preview a production build without the dev server.

## Project structure

```text
config/
  _default/hugo.toml      # Site params, menu, GA, research copy
  development/hugo.toml   # Local baseURL override
content/                  # Section front matter (title, description)
data/                     # Publications, teaching, timeline, news, pillars, gallery
layouts/                  # Page templates and partials
assets/css/main.css       # Site styles
assets/js/search.js         # Client-side search
static/                   # Images and PDFs (copied as-is to site root)
.github/workflows/deploy.yml
```

Page bodies are mostly driven by `data/*.yaml` and `config/_default/hugo.toml` params, not by Markdown body text.

## Content sources

| File | Purpose |
|------|---------|
| `config/_default/hugo.toml` | Contact links, bio, research narrative, menu, GA |
| `data/publications.yaml` | Papers and theses grouped by year; pillar tags for filters |
| `data/research_pillars.yaml` | Three pillars, project cards (`status`: `done`, `in_progress`, `planned`) |
| `data/teaching.yaml` | Courses |
| `data/timeline.yaml` | Appointments, education, earlier roles |
| `data/news.yaml` | Home page news (recent professional items only) |
| `data/software.yaml` | Research software cards |
| `data/gallery.yaml` | Gallery sections |
| `content/*/_index.md` | Section titles and descriptions (metadata) |

Canonical bio and publications also live in `Albert_Personal_Repository` (`shared/contact.tex`, `cv/bib/own-bib.bib`).

## Assets

Photos and publication PDFs live under `static/`. Hugo copies them to the site root, so gallery files at `static/images/gallery/lab-group.jpg` are served as `/images/gallery/lab-group.jpg`.

1. **Profile photo** → `static/images/profile.jpg`
2. **Gallery photos** → `static/images/gallery/` (`lab-supervisor.jpg`, `lab-group.jpg`, `graduation.jpg`). Add entries in `data/gallery.yaml` when you add more files.
3. **Research figures** → `static/images/research/`
4. **Thesis and slides PDFs** → `static/files/publications/`:
   - `phd-defense-slides.pdf` (Ph.D. thesis itself: KNU link, no local PDF needed)
   - `mtech-thesis.pdf`
   - `mtech-defense-slides.pdf`
   - `adintech-2025-slides.pdf`
   - `isap-2019-slides.pdf`
   - `iciccs-2019-paper.pdf`
   - `iciccs-2019-slides.pdf` (optional)
5. **Academic CV:** the `/cv/` page is public. Click **Download Academic CV** to print or save as PDF. To add a hosted PDF later, put `albert-poulose-cv.pdf` in `static/files/cv/`.
6. **Google Analytics:** GA4 ID in `[services.googleAnalytics]` in `hugo.toml`. Analytics runs on the live site only (not localhost).

Contact does **not** list a home address or phone numbers. Institutional email is shown first.

## Custom domain

The live GitHub Pages URL can stay as-is until DNS is ready. To attach `albertpoulose.com` later:

1. Buy the domain (Cloudflare Registrar is a common choice).
2. Point DNS to GitHub Pages (A/ALIAS/CNAME per GitHub’s custom-domain docs).
3. Add a `CNAME` file in `static/` containing `albertpoulose.com`.
4. Update `baseURL` in `config/_default/hugo.toml` and the `hugo --baseURL` flag in `.github/workflows/deploy.yml`.
5. In the GitHub repo: Settings → Pages → Custom domain.

That keeps the printed website URL stable if the host later moves from GitHub Pages to Vercel or elsewhere.

## Deploy to GitHub Pages

1. Create repo `albert8943/dr-albert-poulose` on GitHub (public)
2. Commit and push this folder to `main` (or `master`; the workflow supports both)
3. Settings → Pages → Source: **GitHub Actions**
4. Push triggers `.github/workflows/deploy.yml`
5. Site URL: `https://albert8943.github.io/dr-albert-poulose/`

After deploy, verify the CV page, search, contact details, and GA Realtime (Analytics may take a few minutes to appear).

## Maintenance

**New publication**

1. Add entry to `cv/bib/own-bib.bib` in CV repo
2. Mirror it in `data/publications.yaml` (include `pillars` tags: `01`, `02`, `03`, or omit for Other)
3. Add a news item in `data/news.yaml`
4. Link related project cards in `data/research_pillars.yaml` if applicable

**Research programme**

- Pillar copy and project cards: `data/research_pillars.yaml`
- Page framing (overview, current emphasis, assessment concepts): `config/_default/hugo.toml` under `[params]`
- Layout and figures: `layouts/research/`, `layouts/partials/research-*.html`

**New gallery photo**

1. Add image under `static/images/gallery/`
2. Add entry in `data/gallery.yaml`
