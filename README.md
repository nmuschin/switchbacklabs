# Switchback Labs

The studio website and brand files for Switchback Labs.

Lots of projects, constant switching, always climbing.

## The site

Plain HTML and CSS with no build step: `index.html`, `styles.css`, the favicons at the root, and the images in `assets/`. It's served by GitHub Pages from the root of `main` (`.nojekyll` turns off Jekyll processing).

To preview it locally:

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

All paths are relative, so the site works both at `https://nmuschin.github.io/switchbacklabs/` and on a custom domain. The `og:url` and `og:image` tags in `index.html` are absolute and need updating if the domain changes.

## Brand files

| Folder | What's in it |
|---|---|
| `brand/switchback-labs/` | The studio mark (a trail with a stop per project) on an indigo tile: lockups, app icon, favicons, social card and a README with colours and SwiftUI snippets |
| `brand/waymark-study/` | Waymark Study's mark (the same trail, with stops spreading out like review intervals, ending at a waymark flag) on its terracotta, plus Next.js-ready icon files |

`assets/apps/` holds each app's current icon at 256 px, for the app grid.

## Adding an app

Copy one `<li class="app">` block in `index.html`, then add a 256×256 PNG icon in `assets/apps/`. Apps without an icon yet can use the `icon-placeholder` block, as Bellwether does.
