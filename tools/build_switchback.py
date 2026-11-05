"""Build the Switchback Labs SVG set (mark A, Indigo) with the wordmark converted to outlines."""
import os
import sys

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONT_DIR, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

INDIGO_TOP, INDIGO_BOTTOM = "#6E7BFF", "#2F38C8"
INK, GRAY, PAPER = "#16171B", "#55575E", "#F5F5F7"
DARK_BG, DARK_GRAY = "#16171B", "#A4A7AE"

fonts = {w: TTFont(os.path.join(FONT_DIR, f"PlusJakartaSans-{w}.ttf")) for w in (500, 800)}

TRAIL = "M28 82 L70 70 L30 55 L70 40 L44 24"
STOPS = [(70, 70, 7), (30, 55, 7), (70, 40, 7), (44, 24, 9.5)]


def mark_a(color, trail_opacity=0.55, start=True):
    """Mark A: faint zigzag trail with a bright stop at each turn (one per project)."""
    out = [f'<path d="{TRAIL}" fill="none" stroke="{color}" stroke-opacity="{trail_opacity}" stroke-width="7" '
           f'stroke-linecap="round" stroke-linejoin="round"/>']
    if start:
        out.append(f'<circle cx="28" cy="82" r="4.5" fill="{color}"/>')
    out += [f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>' for x, y, r in STOPS]
    return "".join(out)


def mark_c(color):
    """Mark C: bold zigzag, used where mark A gets too busy (16-32 px)."""
    return (f'<path d="M26 80 L68 67 L32 51 L64 38" fill="none" stroke="{color}" stroke-width="14" '
            f'stroke-linecap="round" stroke-linejoin="round"/><circle cx="68" cy="21" r="11" fill="{color}"/>')


def gradient(gid, x1=0, y1=0, x2=0, y2=1, units="objectBoundingBox"):
    return (f'<defs><linearGradient id="{gid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" gradientUnits="{units}">'
            f'<stop offset="0" stop-color="{INDIGO_TOP}"/><stop offset="1" stop-color="{INDIGO_BOTTOM}"/>'
            f'</linearGradient></defs>')


def tile(size=100, rx=None, inner=None, full_bleed=False, gid="sbg"):
    """Indigo gradient tile with the white mark centred at ~76% of the tile."""
    inner = inner or mark_a("#FFFFFF")
    rx = 0 if full_bleed else (rx if rx is not None else size * 0.225)
    s = size * 0.76 / 100
    off = (size - 100 * s) / 2
    return (f'{gradient(gid)}<rect width="{size:g}" height="{size:g}" rx="{rx:g}" fill="url(#{gid})"/>'
            f'<g transform="translate({off:g} {off:g}) scale({s:g})">{inner}</g>')


def text_path(text, weight, size, x, baseline):
    font = fonts[weight]
    gs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
    scale = size / font["head"].unitsPerEm
    pen, bounds = SVGPathPen(gs), BoundsPen(gs)
    cx = 0
    for ch in text:
        name = cmap[ord(ch)]
        tr = (scale, 0, 0, -scale, x + cx * scale, baseline)
        gs[name].draw(TransformPen(pen, tr))
        gs[name].draw(TransformPen(bounds, tr))
        cx += hmtx[name][0]
    b = bounds.bounds or (0, baseline, 0, baseline)
    return pen.getCommands(), cx * scale, (b[1], b[3])


def svg(w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:g}" height="{h:g}" viewBox="0 0 {w:g} {h:g}" '
            f'role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n')


def write(name, content):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)


NAME = "Switchback Labs"

# Standalone marks (no tile)
write("switchback-mark.svg", svg(100, 100, mark_a(INDIGO_BOTTOM), NAME))
write("switchback-mark-white.svg", svg(100, 100, mark_a("#FFFFFF", 0.5), NAME))
write("switchback-mark-ink.svg", svg(100, 100, mark_a(INK, 0.45), NAME))
write("switchback-mark-small.svg", svg(100, 100, mark_c(INDIGO_BOTTOM), NAME))

# Tiles
write("switchback-tile.svg", svg(100, 100, tile(), NAME))
write("app-icon.svg", svg(1024, 1024, tile(1024, full_bleed=True), f"{NAME} app icon"))
write("favicon.svg", svg(100, 100, tile(inner=mark_c("#FFFFFF")), NAME))


# Horizontal lockup: tile (100) + "Switchback Labs", text centred on the tile
def lockup_h(word_color, labs_color, suffix):
    size, x0 = 56, 124
    _, _, (y0, y1) = text_path("Switchback", 800, size, 0, 0)
    baseline = 50 - (y0 + y1) / 2
    d1, w1, _ = text_path("Switchback", 800, size, x0, baseline)
    d2, w2, _ = text_path(" Labs", 500, size, x0 + w1, baseline)
    width = x0 + w1 + w2 + 4
    body = f'{tile(gid="h" + suffix)}<path d="{d1}" fill="{word_color}"/><path d="{d2}" fill="{labs_color}"/>'
    return svg(round(width, 1), 100, body, NAME)


write("switchback-lockup-horizontal.svg", lockup_h(INK, GRAY, "l"))
write("switchback-lockup-horizontal-dark.svg", lockup_h(PAPER, DARK_GRAY, "d"))


# Stacked lockup: tile centred above the wordmark
def lockup_s(word_color, labs_color, suffix):
    size = 40
    _, w1, _ = text_path("Switchback", 800, size, 0, 0)
    _, w2, _ = text_path(" Labs", 500, size, 0, 0)
    width = w1 + w2 + 8
    tx = (width - (w1 + w2)) / 2
    baseline = 100 + 22 + size * 0.74
    d1, _, _ = text_path("Switchback", 800, size, tx, baseline)
    d2, _, (_, ymax) = text_path(" Labs", 500, size, tx + w1, baseline)
    height = max(ymax, baseline) + 6
    body = (f'<g transform="translate({(width - 100) / 2:g} 0)">{tile(gid="s" + suffix)}</g>'
            f'<path d="{d1}" fill="{word_color}"/><path d="{d2}" fill="{labs_color}"/>')
    return svg(round(width, 1), round(height, 1), body, NAME)


write("switchback-lockup-stacked.svg", lockup_s(INK, GRAY, "l"))
write("switchback-lockup-stacked-dark.svg", lockup_s(PAPER, DARK_GRAY, "d"))

# Social / Open Graph card (1200x630): stacked lockup on paper
d1, w1, _ = text_path("Switchback", 800, 88, 0, 0)
_, w2, _ = text_path(" Labs", 500, 88, 0, 0)
tx = (1200 - (w1 + w2)) / 2
d1, _, _ = text_path("Switchback", 800, 88, tx, 470)
d2, _, _ = text_path(" Labs", 500, 88, tx + w1, 470)
og = (f'<rect width="1200" height="630" fill="{PAPER}"/>'
      f'<g transform="translate(480 100) scale(2.4)">{tile(gid="og")}</g>'
      f'<path d="{d1}" fill="{INK}"/><path d="{d2}" fill="{GRAY}"/>')
write("social-card.svg", svg(1200, 630, og, NAME))
print("ok")
