# Dr. Albert Poulose: Personal Website

Hugo-based academic site for **albertpoulose.com**. Research-programme focused: power-system stability, scientific AI, and grid digital twins.

## Current status

| Item | Status |
|------|--------|
| Local preview | Ready (`hugo server -D`) |
| Content & assets | Populated (publications, research pillars, teaching syllabi/photos, software, CV PDF) |
| Citation metrics | Built (OpenAlex); **hidden** via `showCitationMetrics = false` until re-enabled |
| CV | Hosted PDF at `static/files/cv/albert-poulose-cv.pdf`; web summary at `/cv/` |
| Teaching | Interests, philosophy, courses with optional syllabus PDF and group photo per course |
| Research Notes | Technical background at `/research/notes/` (not in main nav) |
| Google Analytics | GA4 configured (live site only; skipped on `hugo server`) |
| Site search | Client-side search at `/search/` (footer link; not in main nav) |
| GitHub Pages deploy | Live via GitHub Actions |
| Custom domain | `albertpoulose.com` connected (Cloudflare DNS → GitHub Pages) |

**Production URL:** `https://albertpoulose.com/`  
**Also:** `https://albert8943.github.io/dr-albert-poulose/` (GitHub usually redirects after custom domain is set)

## Features

- **Home:** research identity, two-paragraph bio, research interests, current focus, featured PINN paper, selected publications (full titles), software, recent news
- **Research:** two-paragraph vision; three programmes; overlap figure; current / building-toward; pillar sections (Problem → Approach → Selected work → Current direction); link to Research Notes
- **Research Notes:** IEEE/CIGRE / TSA / CCT background and programme figures (footer of Research only; not main nav)
- **Publications:** grouped by year; collapsible abstracts; Scholar/ORCID/Scopus; filter by research pillar (`01` Stability · `02` Scientific AI · `03` Digital Twins)
- **Teaching:** interests, multi-paragraph philosophy, courses with **Syllabus (PDF)** and optional class photo
- **Experience:** appointments and education (`/education/` redirects here); no certificate PDFs on this page
- **Software:** PINN-TSA (evidence block) plus in-progress / planned prototypes
- **CV:** web summary plus clear **Academic CV — PDF** download
- **Contact** and **Gallery:** footer only (institutional email first; no home address or phone). Gallery is optional secondary content

## Local preview

Local preview is **not** automatic. Opening this repo in Cursor (or a browser bookmark to `http://localhost:1313/`) does **not** start the site. You must run Hugo in a terminal first. If you skip that step, the browser shows **Error Code: -102** (connection refused): nothing is listening on port 1313.

### Any day you open this repo

1. Open a terminal in the project root (Cursor: **Terminal → New Terminal**).
2. Start Hugo:

```powershell
cd D:\Albert_OneDrive\OneDrive\dr-albert-poulose
hugo server -D
```

3. Wait until the terminal prints:

```text
Web Server is available at http://localhost:1313/
```

4. Open **http://localhost:1313/** in your browser (site root — not `/dr-albert-poulose/`).
5. Leave that terminal open while you browse. Edits to content/templates reload automatically.
6. When finished, press **Ctrl+C** in the terminal to stop the server.

If `hugo` is not recognized, use the full path:

```powershell
cd D:\Albert_OneDrive\OneDrive\dr-albert-poulose
$hugo = "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\Hugo.Hugo.Extended_Microsoft.Winget.Source_8wekyb3d8bbwe\hugo.exe"
& $hugo server -D
```

| | Local | Production |
|---|---|---|
| Base URL | `http://localhost:1313/` | `https://albertpoulose.com/` |
| Config | `config/development/hugo.toml` | `config/_default/hugo.toml` |

**Important:** production and local preview both use the site root (no `/dr-albert-poulose/` path). That subpath was only used before the custom domain. Bookmarks like `http://localhost:1313/dr-albert-poulose/` are obsolete and return 404.

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

If `hugo` is not recognized, Hugo is still installed. Your terminal may not have WinGet’s `Links` folder on `PATH` yet. Use the full path in [Any day you open this repo](#any-day-you-open-this-repo), or close and reopen your terminal (or restart Cursor) and try `hugo version` again.

### Page URL map

| Page | Path | Local URL | Production URL |
|------|------|-----------|----------------|
| Home | `/` | http://localhost:1313/ | https://albertpoulose.com/ |
| Research | `/research/` | http://localhost:1313/research/ | https://albertpoulose.com/research/ |
| Research Notes | `/research/notes/` | http://localhost:1313/research/notes/ | https://albertpoulose.com/research/notes/ |
| Publications | `/publications/` | http://localhost:1313/publications/ | https://albertpoulose.com/publications/ |
| Teaching | `/teaching/` | http://localhost:1313/teaching/ | https://albertpoulose.com/teaching/ |
| Experience | `/experience/` | http://localhost:1313/experience/ | https://albertpoulose.com/experience/ |
| Software | `/software/` | http://localhost:1313/software/ | https://albertpoulose.com/software/ |
| CV | `/cv/` | http://localhost:1313/cv/ | https://albertpoulose.com/cv/ |
| Contact | `/contact/` | http://localhost:1313/contact/ | https://albertpoulose.com/contact/ |
| Gallery | `/gallery/` | http://localhost:1313/gallery/ | https://albertpoulose.com/gallery/ |
| Search | `/search/` | http://localhost:1313/search/ | https://albertpoulose.com/search/ |

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

**Error Code: -102 / connection refused / “This site can’t be reached”**

Hugo is not running. The browser bookmark alone is not enough. Follow [Any day you open this repo](#any-day-you-open-this-repo): start `hugo server -D`, wait for `Web Server is available at http://localhost:1313/`, then open the URL.

**Wrong page, blank page, or 404 at http://localhost:1313/**

Usually an old Hugo process is still serving the pre-domain subpath, or the browser is still on `/dr-albert-poulose/`.

1. Open **http://localhost:1313/** (not `/dr-albert-poulose/`).
2. Stop every Hugo server (**Ctrl+C** in its terminal, or end `hugo` in Task Manager).
3. Start again from the project root: `hugo server -D`.
4. Confirm the terminal prints `Web Server is available at http://localhost:1313/`.

After changing `baseURL` in `config/development/hugo.toml`, restart the server. A long-running process may keep the old path until you restart it.

**Port 1313 is already in use**

Stop the other Hugo process, or use another port:

```powershell
hugo server -D --port 1314 --baseURL "http://localhost:1314/"
```

Then open http://localhost:1314/ instead.

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
  _default/hugo.toml      # Production baseURL (albertpoulose.com), params, menu, GA
  development/hugo.toml   # Local baseURL (http://localhost:1313/)
content/                  # Section front matter (title, description)
  research/notes.md       # Research Notes page
data/                     # Publications, teaching, timeline, news, pillars, software, gallery
layouts/                  # Page templates and partials
assets/css/main.css       # Site styles
assets/js/search.js       # Client-side search
static/                   # Images, PDFs, CNAME (copied as-is to site root)
  images/teaching/        # One group photo per course
  files/teaching/         # One syllabus PDF per course
  files/cv/               # Hosted academic CV PDF
static/CNAME              # albertpoulose.com (GitHub Pages custom domain)
.github/workflows/deploy.yml  # Builds with --baseURL https://albertpoulose.com/
```

Page bodies are mostly driven by `data/*.yaml` and `config/_default/hugo.toml` params, not by Markdown body text.

## Content sources

| File | Purpose |
|------|---------|
| `config/_default/hugo.toml` | Bio, research interests/focus/vision, teaching interests/philosophy, contact, menu, GA; production `baseURL` |
| `config/development/hugo.toml` | Local preview `baseURL` (`http://localhost:1313/`) |
| `static/CNAME` | Custom domain hostname for GitHub Pages (`albertpoulose.com`) |
| `data/publications.yaml` | Papers and theses by year; pillar tags (`01`/`02`/`03`) for filters |
| `data/research_pillars.yaml` | Three pillars and project cards (`done` / `in_progress` / `planned`) |
| `data/teaching.yaml` | Courses, focus bullets, optional `photo` / `syllabus` paths |
| `data/timeline.yaml` | Appointments, education, earlier roles |
| `data/news.yaml` | Home page news (recent professional items only) |
| `data/software.yaml` | Research software cards (optional evidence fields for mature tools) |
| `data/metrics.yaml` | OpenAlex citation metrics (citations, h-index, i10-index); refreshed weekly |
| `data/gallery.yaml` | Optional gallery sections (footer link) |
| `content/*/_index.md` | Section titles and descriptions (metadata) |
| `content/research/notes.md` | Research Notes title/description |

Canonical bio and publications also live in `Albert_Personal_Repository` (`shared/contact.tex`, `cv/bib/own-bib.bib`).

## Assets

Files under `static/` are copied to the site root (e.g. `static/images/teaching/…` → `/images/teaching/…`).

1. **Profile photo** → `static/images/profile.jpg`
2. **Teaching photos** → `static/images/teaching/` (one per course; see that folder’s README)
3. **Teaching syllabi** → `static/files/teaching/` (one PDF per course; see that folder’s README)
4. **Academic CV PDF** → `static/files/cv/albert-poulose-cv.pdf` (button on `/cv/` shows when present)
5. **Gallery photos** (optional) → `static/images/gallery/` + entries in `data/gallery.yaml`
6. **Research figures** → `static/images/research/` (also SVG partials under `layouts/partials/research-fig-*.html`)
7. **Thesis and slides PDFs** → `static/files/publications/` as needed for publication links
8. **Google Analytics:** GA4 ID in `[services.googleAnalytics]` in `hugo.toml` (live site only)

Contact does **not** list a home address or phone numbers. Institutional email is shown first. Experience does **not** host appointment letters or degree certificates.

## Custom domain

Canonical public URL: **https://albertpoulose.com/**  
Registrar: Cloudflare Registrar. Hosting: GitHub Pages (not Cloudflare Workers/Pages).

### DNS (Cloudflare)

Use **DNS only** (grey cloud), not Proxied (orange cloud), so GitHub can verify the domain and issue HTTPS.

| Type | Name | Content | Proxy |
|------|------|---------|-------|
| A | `@` | `185.199.108.153` | DNS only |
| A | `@` | `185.199.109.153` | DNS only |
| A | `@` | `185.199.110.153` | DNS only |
| A | `@` | `185.199.111.153` | DNS only |
| CNAME | `www` | `albert8943.github.io` | DNS only |

Those four A-record IPs are GitHub Pages’ published addresses for apex domains. Ignore Cloudflare’s empty-DNS email (MX) recommendations unless you later add custom email for this domain.

### GitHub Pages

1. Repo **Settings → Pages → Custom domain:** `albertpoulose.com`
2. Wait for **DNS check successful**
3. Enable **Enforce HTTPS** after the certificate is issued (may take minutes to hours; the checkbox stays grey until then)

### Repo files that must stay in sync

| File | Value |
|------|--------|
| `config/_default/hugo.toml` → `baseURL` | `https://albertpoulose.com/` |
| `config/development/hugo.toml` → `baseURL` | `http://localhost:1313/` |
| `.github/workflows/deploy.yml` → `hugo --baseURL` | `https://albertpoulose.com/` |
| `static/CNAME` | `albertpoulose.com` |

If the public hostname ever changes, update all four together, then push `main` and restart any local `hugo server`.

## Deploy to GitHub Pages

Push to `main` triggers `.github/workflows/deploy.yml` (builds with production `baseURL`).

Live site: **https://albertpoulose.com/**  
Fallback GitHub URL: `https://albert8943.github.io/dr-albert-poulose/` (often redirects once the custom domain is set).

After deploy, check Home, Research, Teaching, Publications, Software, CV, Search, and images. When HTTPS is ready, confirm the lock icon on `https://albertpoulose.com/`.

## Maintenance

For a **detailed page-by-page editing guide** (which files and fields to change), see **[CONTENT-GUIDE.md](CONTENT-GUIDE.md)**.

**New publication**

1. Add entry to `cv/bib/own-bib.bib` in CV repo
2. Mirror it in `data/publications.yaml` (include `pillars`: `01`, `02`, `03`; use only pillars the paper genuinely supports)
3. Add a news item in `data/news.yaml` if appropriate
4. Link related project cards in `data/research_pillars.yaml` if applicable

**Research programme**

- Pillar copy and project cards: `data/research_pillars.yaml`
- Bio, interests, current focus, vision, teaching copy: `config/_default/hugo.toml` under `[params]`
- Assessment / tutorial material: Research Notes (`layouts/research/single.html`, related partials)
- Layout and figures: `layouts/research/`, `layouts/partials/research-*.html`

**Teaching course assets**

1. Syllabus PDF → `static/files/teaching/<slug>.pdf` and `syllabus:` in `data/teaching.yaml`
2. Group photo → `static/images/teaching/<slug>.jpg` and `photo:` / captions in `data/teaching.yaml`

**Gallery (optional)**

1. Add image under `static/images/gallery/`
2. Add entry in `data/gallery.yaml`
