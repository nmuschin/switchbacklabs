"""Build the Waymark Study SVG set (Switchback trail variant, terracotta) with the wordmark converted to outlines."""
import os
import sys

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONT_DIR, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

INDIGO_TOP, INDIGO_BOTTOM = "#E07A4F", "#B0552F"
INK, GRAY, PAPER = "#1C1B19", "#6B6A65", "#F7F7F5"
DARK_BG, DARK_GRAY = "#16161A", "#9B9A95"

fonts = {w: TTFont(os.path.join(FONT_DIR, f"PlusJakartaSans-{w}.ttf")) for w in (500, 800)}

TRAIL = "M28 88 L66 82 L30 70 L70 52 L40 26"
STOPS = [(66, 82, 5.5), (30, 70, 6.5), (70, 52, 7.5)]
FLAG = "M40 7 H63 L56.5 14.5 L63 22 H40 Z"


def mark_a(color, trail_opacity=0.55, start=True):
    """Waymark mark: Switchback trail whose stops spread out as it climbs (growing review
    intervals), ending at a waymark flag."""
    out = [f'<path d="{TRAIL}" fill="none" stroke="{color}" stroke-opacity="{trail_opacity}" stroke-width="7" '
           f'stroke-linecap="round" stroke-linejoin="round"/>']
    if start:
        out.append(f'<circle cx="28" cy="88" r="4" fill="{color}"/>')
    out += [f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>' for x, y, r in STOPS]
    out.append(f'<path d="M40 28 V6" fill="none" stroke="{color}" stroke-width="6" stroke-linecap="round"/>')
    out.append(f'<path d="{FLAG}" fill="{color}" stroke="{color}" stroke-width="3" stroke-linejoin="round"/>')
    return "".join(out)


def mark_c(color):
    """Small mark: one bold switchback and the flag, for 16-32 px."""
    return (f'<path d="M26 84 L66 72 L34 56" fill="none" stroke="{color}" stroke-width="12" '
            f'stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M34 58 V18" fill="none" stroke="{color}" stroke-width="10" stroke-linecap="round"/>'
            f'<path d="M34 19 H64 L56 29 L64 39 H34 Z" fill="{color}" stroke="{color}" stroke-width="4" '
            f'stroke-linejoin="round"/>')


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


NAME = "Waymark Study"

# Standalone marks (no tile)
write("waymark-mark.svg", svg(100, 100, mark_a(INDIGO_BOTTOM), NAME))
write("waymark-mark-white.svg", svg(100, 100, mark_a("#FFFFFF", 0.5), NAME))
write("waymark-mark-ink.svg", svg(100, 100, mark_a(INK, 0.45), NAME))
write("waymark-mark-small.svg", svg(100, 100, mark_c(INDIGO_BOTTOM), NAME))

# Tiles
write("waymark-tile.svg", svg(100, 100, tile(), NAME))
write("app-icon.svg", svg(1024, 1024, tile(1024, full_bleed=True), f"{NAME} app icon"))
write("favicon.svg", svg(100, 100, tile(inner=mark_c("#FFFFFF")), NAME))


# Horizontal lockup: tile (100) + "Waymark Study", text centred on the tile
def lockup_h(word_color, labs_color, suffix):
    size, x0 = 56, 124
    _, _, (y0, y1) = text_path("Waymark", 800, size, 0, 0)
    baseline = 50 - (y0 + y1) / 2
    d1, w1, _ = text_path("Waymark", 800, size, x0, baseline)
    d2, w2, _ = text_path(" Study", 500, size, x0 + w1, baseline)
    width = x0 + w1 + w2 + 4
    body = f'{tile(gid="h" + suffix)}<path d="{d1}" fill="{word_color}"/><path d="{d2}" fill="{labs_color}"/>'
    return svg(round(width, 1), 100, body, NAME)


write("waymark-lockup-horizontal.svg", lockup_h(INK, GRAY, "l"))
write("waymark-lockup-horizontal-dark.svg", lockup_h(PAPER, DARK_GRAY, "d"))


# Stacked lockup: tile centred above the wordmark
def lockup_s(word_color, labs_color, suffix):
    size = 40
    _, w1, _ = text_path("Waymark", 800, size, 0, 0)
    _, w2, _ = text_path(" Study", 500, size, 0, 0)
    width = w1 + w2 + 8
    tx = (width - (w1 + w2)) / 2
    baseline = 100 + 22 + size * 0.74
    d1, _, _ = text_path("Waymark", 800, size, tx, baseline)
    d2, _, (_, ymax) = text_path(" Study", 500, size, tx + w1, baseline)
    height = max(ymax, baseline) + 6
    body = (f'<g transform="translate({(width - 100) / 2:g} 0)">{tile(gid="s" + suffix)}</g>'
            f'<path d="{d1}" fill="{word_color}"/><path d="{d2}" fill="{labs_color}"/>')
    return svg(round(width, 1), round(height, 1), body, NAME)


write("waymark-lockup-stacked.svg", lockup_s(INK, GRAY, "l"))
write("waymark-lockup-stacked-dark.svg", lockup_s(PAPER, DARK_GRAY, "d"))

# Social / Open Graph card (1200x630): stacked lockup on paper
d1, w1, _ = text_path("Waymark", 800, 88, 0, 0)
_, w2, _ = text_path(" Study", 500, 88, 0, 0)
tx = (1200 - (w1 + w2)) / 2
d1, _, _ = text_path("Waymark", 800, 88, tx, 470)
d2, _, _ = text_path(" Study", 500, 88, tx + w1, 470)
og = (f'<rect width="1200" height="630" fill="{PAPER}"/>'
      f'<g transform="translate(480 100) scale(2.4)">{tile(gid="og")}</g>'
      f'<path d="{d1}" fill="{INK}"/><path d="{d2}" fill="{GRAY}"/>')
write("social-card.svg", svg(1200, 630, og, NAME))
print("ok")
