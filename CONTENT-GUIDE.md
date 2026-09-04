# Content editing guide

Use this file when you want to **edit, update, or add** content on [albertpoulose.com](https://albertpoulose.com/).  
For Hugo install, **daily local preview**, and deploy, see [README.md → Local preview](README.md#local-preview) (especially [Any day you open this repo](README.md#any-day-you-open-this-repo)).

**Rule of thumb:** most page copy lives in `config/_default/hugo.toml` and `data/*.yaml`.  
`content/*/_index.md` files usually hold only the page **title** and **meta description**.

### Preview before you edit (every session)

Localhost does **not** start when you open the repo. Error **-102** means Hugo is not running.

```powershell
cd D:\Albert_OneDrive\OneDrive\dr-albert-poulose
hugo server -D
```

Then open **http://localhost:1313/**. Leave the terminal open. Full steps: [README — Any day you open this repo](README.md#any-day-you-open-this-repo).

After edits, confirm the pages in that preview, then push `main` to deploy.

---

## Quick map: page → files

| Website page | Primary files to edit |
|--------------|------------------------|
| Home | `config/_default/hugo.toml`, `data/publications.yaml` (`selected`), `data/software.yaml`, `data/news.yaml`, `data/metrics.yaml` |
| Research | `config/_default/hugo.toml`, `data/research_pillars.yaml` |
| Research Notes | `config/_default/hugo.toml` (assessment params), `layouts/research/single.html`, `layouts/partials/research-*.html` |
| Publications | `data/publications.yaml`, `data/metrics.yaml` |
| Teaching | `config/_default/hugo.toml`, `data/teaching.yaml`, `static/files/teaching/`, `static/images/teaching/` |
| Experience | `data/timeline.yaml` |
| Software | `data/software.yaml` |
| CV | `config/_default/hugo.toml` (`cvUpdated`, `cvPdf`), `static/files/cv/`, `layouts/cv/list.html` (structure) |
| Contact | `config/_default/hugo.toml` (email, address, links) |
| Gallery (footer) | `data/gallery.yaml`, `static/images/gallery/` |
| Search | usually no content edits; index is built from site data |
| Navigation / menu | `config/_default/hugo.toml` → `[menu]` |
| Styles | `assets/css/main.css` |

---

## 1. Home (`/`)

**Layout:** `layouts/index.html`

### Identity and bio

File: [`config/_default/hugo.toml`](config/_default/hugo.toml) under `[params]`

| Param | What it controls |
|-------|------------------|
| `name`, `role`, `affiliation`, `university` | Hero name and position line |
| `researchIdentity` | Headline under your name (programme label) |
| `bioIntro` | First bio paragraph |
| `bioCurrent` | Second bio paragraph |
| `researchInterests` | Bullet list under **Research interests** |
| `currentResearch` | **Current focus** line on Home (also **Current research** on Research) |

### Featured research

Same file:

| Param | What it controls |
|-------|------------------|
| `featuredTitle`, `featuredSummary`, `featuredVenue` | Featured card copy |
| `featuredPaper`, `featuredCode`, `featuredProject` | Buttons |

### Selected publications

File: [`data/publications.yaml`](data/publications.yaml)

- Set `selected: true` on items you want on Home.
- Home shows the full `title` (not `homepageTitle`).
- Keep `homepageTitle` optional/legacy; it is unused on Home now.

### Research software teaser

File: [`data/software.yaml`](data/software.yaml)

- Home shows the first three entries.
- Uses `title`, `short`, `stack`, `status`.

### Recent news

File: [`data/news.yaml`](data/news.yaml)

```yaml
- date: YYYY-MM-DD
  text: "Plain text or HTML (links with <a href=...>)"
```

Newest dates appear first if you keep the list ordered by date descending.

### Profile photo

- Replace: `static/images/profile.jpg`
- Fallback: `static/images/profile-placeholder.svg`

---

## 2. Research (`/research/`)

**Layout:** `layouts/research/list.html`  
**Pillars partial:** `layouts/partials/research-pillars-inner.html`

### Vision and horizons

File: [`config/_default/hugo.toml`](config/_default/hugo.toml)

| Param | What it controls |
|-------|------------------|
| `researchVisionTitle` | Section heading |
| `researchVision` | First vision paragraph |
| `researchVisionContinued` | Second vision paragraph |
| `researchProgramsTitle` | “Three research programs” heading |
| `researchCurrentTitle` / `currentResearch` | **Current research** list |
| `researchBuildingTitle` / `futureResearch` | **Building toward** list |

### Three research programmes (pillars)

File: [`data/research_pillars.yaml`](data/research_pillars.yaml)

Each pillar has:

| Field | Role |
|-------|------|
| `number`, `id`, `title` | Heading and anchor (`#scientific-ai`, etc.) |
| `description`, `tags` | Tagline and keyword line |
| `problem`, `approach`, `currentDirection` | Main prose blocks (order on page: Problem → Approach → Selected work → Current direction) |
| `pipeline` | Short step labels in the pipeline figure |
| `overlaps` | Cross-links to other pillars |
| `projects[]` | Selected work cards: `title`, `status` (`done` / `in_progress` / `planned`), `description` |
| `note` | Optional HTML note under a pillar (e.g. GitHub link) |
| `figure` | Partial name for notes page figures (e.g. `research-fig-01.html`) |

**Do not** put long tutorial text back into pillars; keep that on Research Notes.

### Overlap / flow figures

- `layouts/partials/research-overlap.html`
- `layouts/partials/research-pipeline.html`

### Link to Research Notes

Footer line on Research is in `layouts/research/list.html` (text + URL).  
Notes page itself: see [§3](#3-research-notes-researchnotes).

---

## 3. Research Notes (`/research/notes/`)

**Content stub:** [`content/research/notes.md`](content/research/notes.md) (title / description)  
**Layout:** `layouts/research/single.html`

### Assessment / TSA / CCT copy

File: [`config/_default/hugo.toml`](config/_default/hugo.toml)

| Param | Section |
|-------|---------|
| `researchAssessmentTitle`, `researchAssessmentIntro` | Intro |
| `researchDefinitionTitle`, `researchDefinition` | Dynamic security definition |
| `researchStabilityTitle`, `researchStabilityIntro` | IEEE/CIGRE placement |
| `researchTsaTitle`, `researchTsaNote` | Transient stability note |
| `researchMarginTitle`, `researchMarginIntro` | CCT margin |

### Partials and images

| Partial / asset | Purpose |
|-----------------|--------|
| `layouts/partials/research-assessment-concepts.html` | Assembles assessment block |
| `layouts/partials/research-stability-context.html` | Classification + TSA cases |
| `layouts/partials/research-fig-dsa.html` | CCT margin figure |
| `layouts/partials/research-fig-01.html` … `03` | Programme figures |
| `static/images/research/` | Raster figures if used |

---

## 4. Publications (`/publications/`)

**Layout:** `layouts/publications/list.html`  
**Data:** [`data/publications.yaml`](data/publications.yaml)

### Add a paper

1. Add under the correct `year:` block (or create a new year).
2. Fill fields as needed:

| Field | Notes |
|-------|--------|
| `type` | `journal`, `conference`, `thesis`, etc. |
| `pillars` | `["01"]`, `["02"]`, `["01","02"]`, … Be conservative: tag **03 Digital Twins** only when the paper truly supports it |
| `selected` | `true` → also on Home |
| `authors`, `title`, `venue` | Required display fields |
| `doi`, `url`, `code` | Links (DOI preferred for IEEE) |
| `abstract`, `keywords` | Collapsible abstract on Publications |
| `pdf` / slide paths | If linked from YAML and files exist under `static/files/publications/` |

3. Optionally add a news item in `data/news.yaml`.
4. Optionally update a related project in `data/research_pillars.yaml` or `data/software.yaml`.

### Local PDFs / slides

Folder: `static/files/publications/`  
See `static/files/publications/README.txt` for expected filenames.

---

## Citation metrics (Home & Publications)

Shown as Citations · h-index · i10-index from **OpenAlex** (not Google Scholar scraping).

| File | Role |
|------|------|
| [`data/metrics.yaml`](data/metrics.yaml) | Numbers + `updated` date |
| [`layouts/partials/metrics-strip.html`](layouts/partials/metrics-strip.html) | Shared UI |
| [`scripts/fetch-openalex-metrics.py`](scripts/fetch-openalex-metrics.py) | Fetches by ORCID |
| [`.github/workflows/update-metrics.yml`](.github/workflows/update-metrics.yml) | Weekly Monday refresh + manual run |

**Force refresh:** GitHub → Actions → **Update OpenAlex metrics** → Run workflow.

OpenAlex counts are often lower than Google Scholar. The strip links to Scholar for the familiar profile. Do not edit metrics by hand unless the Action is unavailable—prefer re-running the workflow.

---

## 5. Teaching (`/teaching/`)

**Layout:** `layouts/teaching/list.html`

### Interests and philosophy

File: [`config/_default/hugo.toml`](config/_default/hugo.toml)

| Param | What it controls |
|-------|------------------|
| `teachingInterests` | Interest chips |
| `teachingPhilosophy` | Array of paragraphs (one string per paragraph) |

### Courses

File: [`data/teaching.yaml`](data/teaching.yaml)

Grouped by `year`, each course:

| Field | Required? | Notes |
|-------|-----------|--------|
| `code`, `title`, `period`, `institution`, `students` | Yes | Header line |
| `focus` | Recommended | Bullets under **Course focus** |
| `syllabus` | Optional | Path under `static/`, e.g. `files/teaching/numerical-analysis-2025.pdf` |
| `photo`, `photoCaption`, `photoAlt` | Optional | Path under `static/`, e.g. `images/teaching/….jpg` |

**Syllabus button** and **photo** appear only if the file exists on disk (`os.FileExists`).

### Add a new course

1. Add an entry in `data/teaching.yaml`.
2. Put syllabus PDF in `static/files/teaching/` and set `syllabus:`.
3. Put group photo in `static/images/teaching/` and set `photo:` + captions.
4. Use clear filenames: `<course-slug>-<year>.pdf` / `.jpg`.

---

## 6. Experience (`/experience/`)

**Layout:** `layouts/experience/list.html`  
**Data:** [`data/timeline.yaml`](data/timeline.yaml)

| YAML key | Page section |
|----------|----------------|
| `appointments` | Appointments |
| `education` | Education |
| `early_career` | Earlier appointments |
| `school` | Earlier education (collapsed) |

Each item typically has:

```yaml
- period: "YYYY.MM – YYYY.MM"
  role: "Title"
  institution: "…"
  highlights:   # optional list
    - "…"
```

**Do not** attach appointment letters or degree certificates here. Formal docs belong in applications / the Academic CV PDF.

`/education/` redirects to Experience (keep that unless you intentionally change redirects).

---

## 7. Software (`/software/`)

**Layout:** `layouts/software/list.html`  
**Data:** [`data/software.yaml`](data/software.yaml)

| Field | Notes |
|-------|--------|
| `id`, `title`, `short`, `description`, `stack` | Core card |
| `status` | `available` / `in_progress` / `planned` |
| `paper`, `code`, `project` | Optional links |
| `inputs`, `outputs`, `validatedAgainst`, `statusLabel` | Optional evidence block (use for mature tools like PINN-TSA) |

Home teaser uses the first three entries and prefers `short` + `stack`.

---

## 8. CV (`/cv/`)

**Layout:** `layouts/cv/list.html`

| What to change | Where |
|----------------|--------|
| Last-updated label | `cvUpdated` in `hugo.toml` |
| PDF path | `cvPdf` (default `files/cv/albert-poulose-cv.pdf`) |
| Replace PDF | Overwrite `static/files/cv/albert-poulose-cv.pdf` |
| Bio / identity on web CV | Same `bioIntro`, `bioCurrent`, `researchIdentity` as Home |
| Appointments / education / teaching / software blocks | Pulled from `timeline.yaml`, `publications.yaml` (`selected`), `teaching.yaml`, `software.yaml` |

Button label: **Academic CV — PDF · Updated …** (appears when the PDF file exists).

---

## 9. Contact (`/contact/`)

**Layout:** `layouts/contact/list.html`  
**Params in** `hugo.toml`:

- `email`, `emailPersonal`
- `currentAddress`
- `scholar`, `orcid`, `scopus`, `linkedin`, `github`

Keep residential address and phone off the site.

---

## 10. Gallery (`/gallery/` — footer only)

**Data:** [`data/gallery.yaml`](data/gallery.yaml)  
**Images:** `static/images/gallery/`

```yaml
- title: "Section name"
  items:
    - caption: "…"
      image: "/images/gallery/filename.jpg"
      alt: "…"
```

Prefer putting **teaching** photos on the Teaching page, not Gallery.

---

## 11. Site-wide settings

### Main navigation

`config/_default/hugo.toml` → `[[menu.main]]` entries (`name`, `url`, `weight`).

### Footer links

`layouts/partials/footer.html` (Contact, Gallery, Search, CV).

### Meta / analytics

- Page descriptions: each `content/.../_index.md` → `description`
- GA4: `[services.googleAnalytics]` in `hugo.toml`

### Acronym style (keep consistent)

On **each page**, first use: full name (ACRONYM); later uses: ACRONYM only.  
Examples: critical clearing time (CCT), transient stability assessment (TSA), grid-forming (GFM), physics-informed neural network (PINN), phasor measurement unit (PMU).

### Digital Twins labelling

Keep Soft claims: use **building toward** / **in progress** / **planned** until you have direct published outputs for pillar **03**.

---

## Common workflows

### New journal / conference paper

1. `data/publications.yaml` — full entry + `pillars`
2. Optionally `selected: true` for Home
3. `data/news.yaml` — short announcement
4. Update Software / Research projects if relevant
5. Preview → commit → push `main`

### New teaching course

1. `data/teaching.yaml`
2. Syllabus → `static/files/teaching/`
3. Photo → `static/images/teaching/`
4. Preview Teaching page

### Update Academic CV PDF

1. Replace `static/files/cv/albert-poulose-cv.pdf`
2. Set `cvUpdated` in `hugo.toml` (e.g. `Sep 03, 2026`)

### Soften or expand a research pillar

1. Edit the pillar in `data/research_pillars.yaml`
2. Align Home `researchInterests` / `currentResearch` and Research vision in `hugo.toml` if the public story changed
3. Keep tutorial depth on `/research/notes/`, not on `/research/`

---

## What usually should not be edited for content tweaks

| Path | Why |
|------|-----|
| `layouts/` (except known partials above) | Structure/behaviour; prefer YAML/TOML for text |
| `public/` | Build output; overwritten by Hugo |
| `.github/workflows/deploy.yml` | Only when changing deploy/baseURL |
| `static/CNAME` | Only if the domain changes |

---

## Checklist before publishing

1. Start Hugo if it is not already running (`hugo server -D`), then open the changed pages at http://localhost:1313/ (see [README — Local preview](README.md#local-preview)).
2. Check acronym first-use on that page.
3. Confirm new images/PDFs appear (file name must match YAML).
4. Confirm pillar tags on new papers are conservative.
5. Push to `main` and verify https://albertpoulose.com/ after deploy.
