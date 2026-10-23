# Switchback Labs — brand kit

Lots of projects, constant switching, always climbing.

**Mark:** "Trail with stops". It's a zigzag trail with a bright stop at each turn, one per project, and the faint path between them is the switching back and forth. **Color:** Indigo gradient. **Wordmark:** Plus Jakarta Sans (ExtraBold "Switchback", Medium "Labs"), converted to outlines, so no font is needed.

## Files

| File | Use |
|---|---|
| `svg/switchback-tile.svg`, `png/switchback-tile-512.png` | The primary mark: website header, About pages, docs |
| `png/switchback-avatar-400.png` | GitHub, App Store Connect, social profile pictures |
| `svg/app-icon.svg`, `png/app-icon-1024.png` | Full-bleed 1024 square for anything that applies its own corner mask (iOS/macOS icon slots) |
| `svg/switchback-lockup-horizontal(-dark).svg` + `@2x.png` | Website header, README banners, email signature |
| `svg/switchback-lockup-stacked(-dark).svg` + `@2x.png` | Splash and About screens, square spots |
| `svg/social-card.svg`, `png/social-card-1200x630.png` | `og:image` / Twitter card for the website |
| `svg/switchback-mark.svg` / `-white.svg` / `-ink.svg` | The mark without a tile, on light / dark / one-color backgrounds |
| `svg/favicon.svg`, `png/favicon.ico`, `favicon-16/32/48.png` | Web favicons. These use the bold zigzag (mark C) because the stops blur below 32 px. |
| `svg/switchback-mark-small.svg` | The bold zigzag on its own, for other tiny placements |
| `png/apple-touch-icon-180.png` | `<link rel="apple-touch-icon">` |

## Colors

| Role | Hex |
|---|---|
| Indigo, gradient top | `#6E7BFF` |
| Indigo, gradient bottom (and the solid fallback) | `#2F38C8` |
| Ink (wordmark) | `#16171B` |
| Gray ("Labs", secondary text) | `#55575E` |
| Paper (light background) | `#F5F5F7` |
| Dark-mode gray ("Labs" on dark) | `#A4A7AE` |

The gradient runs straight down, top to bottom.

## Quick rules
- Keep clear space around the tile of at least a quarter of its width.
- Use the tile wherever you can. Use the bare mark only where a tile won't fit.
- At 32 px and below, use the favicon / small mark (the bold zigzag).
- Don't recolor the stops individually. The mark is one color: white on the tile, or indigo/ink on its own.

## Website snippet

```html
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon-180.png">
<meta property="og:image" content="https://YOUR-DOMAIN/social-card-1200x630.png">
```

## SwiftUI

```swift
extension Color {
    static let switchbackIndigoTop    = Color(red: 0x6E/255, green: 0x7B/255, blue: 0xFF/255)
    static let switchbackIndigo       = Color(red: 0x2F/255, green: 0x38/255, blue: 0xC8/255)
    static let switchbackInk          = Color(red: 0x16/255, green: 0x17/255, blue: 0x1B/255)
    static let switchbackGray         = Color(red: 0x55/255, green: 0x57/255, blue: 0x5E/255)
}

extension LinearGradient {
    static let switchback = LinearGradient(colors: [.switchbackIndigoTop, .switchbackIndigo],
                                           startPoint: .top, endPoint: .bottom)
}
```

Plus Jakarta Sans is licensed under the SIL Open Font License, so commercial use is fine.
