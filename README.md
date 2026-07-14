# FORMA RE — Landing Page

Static "launching soon" landing page for **forma.re**. No build step, no dependencies — just plain HTML/CSS.

## Running locally

The page uses `@font-face` and absolute (`/…`) asset paths, so open it through a local web server rather than double-clicking the file (a `file://` open will fail to load the fonts and favicons).

### Live reload (recommended)

Auto-refreshes the browser every time you save a file. One-time setup:

```bash
pip install livereload
```

Then, from the project root:

```bash
python serve.py
```

Open <http://127.0.0.1:8000>. Edit any file and the browser reloads on its own. Stop with `Ctrl+C`.

### Plain server (no reload)

If you just want to preview without installing anything:

```bash
python -m http.server 8000
```

Then open <http://localhost:8000> and refresh manually. Stop with `Ctrl+C`.

## Project structure

```
.
├── index.html            # the page (all CSS is inline in <head>)
├── favicon.ico           # root fallback icon (browsers/crawlers request /favicon.ico)
├── site.webmanifest      # PWA manifest referencing the app icons
├── fonts/                # PP Telegraf + Helvetica Neue (@font-face sources)
└── assets/
    ├── brand/            # source logos
    │   ├── logo.png      #   full FORMA RE wordmark (shown centered on the page)
    │   └── icon.png      #   geometric mark (top-left + source for all favicons)
    └── favicons/         # generated icon set
        ├── favicon-16x16.png
        ├── favicon-32x32.png
        ├── apple-touch-icon.png
        ├── android-chrome-192x192.png
        └── android-chrome-512x512.png
```

## Editing

- **Contact address** — the CONTACT button in `index.html` points to `mailto:hello@forma.re`. Change it to your real address (look for the `TODO` comment).
- **Social links** — the four `<a href="">` entries (Instagram, LinkedIn, X, Behance) are empty. Fill in each `href`, or delete any platform you don't use.
- **Background** — currently a brand-toned CSS gradient. To use a photo, follow the `BACKGROUND` comment in the `<style>` block: drop an image in the project and swap the one `background:` line.
- **Regenerating favicons** — all icons are derived from `assets/brand/icon.png`. If you change that source, re-run the Pillow script that produced them (sizes: 16, 32, 180 apple-touch, 192, 512, plus the multi-res `favicon.ico`).

## Deployment

Hosted on GitHub Pages with a custom domain (`forma.re`). The absolute asset paths assume the site is served from the domain root, which is how GitHub Pages serves it.
