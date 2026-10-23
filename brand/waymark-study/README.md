# Waymark Study — brand kit

A Switchback Labs app.

**Mark:** the Switchback Labs trail-with-stops, adapted for spaced repetition. Each climb between stops is longer than the last, like review intervals growing as you learn a card, and the trail ends at a **waymark** flag. **Color:** the app's own terracotta accent (`--accent` in `globals.css`) as a gradient. **Wordmark:** Plus Jakarta Sans (ExtraBold "Waymark", Medium "Study"), the same as Switchback Labs, converted to outlines.

## Drop-in for the Next.js app

`nextjs-src-app/` uses the App Router's file conventions. Copy these four files into `src/app/` and Next.js wires up the `<link>` and `og:image` tags itself:

| File | What Next.js does with it |
|---|---|
| `icon.svg` | Browser favicon (SVG) |
| `favicon.ico` | Fallback favicon |
| `apple-icon.png` | iOS home-screen icon (180 px) |
| `opengraph-image.png` | Link-preview image (1200×630) |

Check the Metadata Files docs for the Next.js version in `node_modules/next/dist/docs/` first, as the repo's `AGENTS.md` asks.

## Files

| File | Use |
|---|---|
| `svg/waymark-tile.svg`, `png/waymark-tile-512.png` | The primary mark: app header, login screen, docs |
| `png/waymark-avatar-400.png` | Social profile picture |
| `svg/app-icon.svg`, `png/app-icon-1024.png` | Full-bleed 1024 square for PWA or native icon slots that apply their own mask |
| `svg/waymark-lockup-horizontal(-dark).svg` + `@2x.png` | App header, landing page, README |
| `svg/waymark-lockup-stacked(-dark).svg` + `@2x.png` | Login and register screens, splash |
| `svg/social-card.svg`, `png/social-card-1200x630.png` | Link previews |
| `svg/waymark-mark.svg` / `-white.svg` / `-ink.svg` | The mark without a tile, on light / dark / one-color backgrounds |
| `svg/favicon.svg`, `svg/waymark-mark-small.svg`, `png/favicon*` | Small sizes: one bold switchback and the flag. The stops blur below 32 px. |

## Colors

The colors match the tokens already in `src/app/globals.css`.

| Role | Hex | Token |
|---|---|---|
| Terracotta, gradient bottom (solid fallback) | `#B0552F` | `--accent` (light) |
| Terracotta, gradient top | `#E07A4F` | — |
| Terracotta, dark mode | `#D97A4E` | `--accent` (dark) |
| Ink | `#1C1B19` | `--text` |
| Muted ("Study") | `#6B6A65` | `--muted` |
| Background | `#F7F7F5` | `--bg` |

**Secondary palette (recall ratings 1–5):** `#B4413C`, `#C1703A`, `#B09030`, `#5D8A4A`, `#3F7D6E` (`--rating-1` to `--rating-5`). Use these for UI, not for the logo. The logo stays one terracotta.

## Relationship to Switchback Labs
- Same construction: a faint trail, bright stops, and a white mark on a gradient tile with the same corner radius.
- Different color: Switchback is indigo, Waymark is terracotta. Each app keeps its own color.
- Where both appear (the website, an About screen), you can add "by Switchback Labs" in the muted color under the Waymark lockup.

Plus Jakarta Sans is licensed under the SIL Open Font License, so commercial use is fine.
