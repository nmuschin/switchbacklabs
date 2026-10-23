#!/usr/bin/env bash
# Rebuild both brand kits, the site's favicons and the zip downloads from source.
#
#   pip install fonttools
#   npm install --no-save playwright && npx playwright install chromium
#   brew install imagemagick        # or: apt install imagemagick zip
#   tools/build.sh
#
# The colours, marks and wordmark sizes live in tools/build_*.py; change them there,
# never in the generated SVGs. Plus Jakarta Sans is fetched from Google Fonts into
# tools/.fonts (git-ignored) the first time this runs.
set -euo pipefail
cd "$(dirname "$0")/.."

FONTS=tools/.fonts
mkdir -p "$FONTS"
for w in 500 800; do
  f="$FONTS/PlusJakartaSans-$w.ttf"
  if [ ! -s "$f" ]; then
    # A non-browser User-Agent makes the css2 API answer with TrueType URLs.
    url=$(curl -fsS -A "curl" "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@$w" | grep -o 'https://[^)]*\.ttf' | head -1)
    curl -fsS -o "$f" "$url"
  fi
done

build_kit() { # name prefix
  local dir="brand/$1"
  rm -rf "$dir/svg" "$dir/png"
  python3 "tools/build_$2.py" "$FONTS" "$dir/svg"
  node "tools/rasterize_$2.js" "$dir/svg" "$dir/png"
  (cd "$dir/png" && convert favicon-16.png favicon-32.png favicon-48.png favicon.ico)
}

build_kit switchback-labs switchback
build_kit waymark-study waymark

# Waymark Study ships as a Next.js app; these names follow the App Router's metadata files.
next=brand/waymark-study/nextjs-src-app
mkdir -p "$next"
cp brand/waymark-study/svg/favicon.svg "$next/icon.svg"
cp brand/waymark-study/png/favicon.ico "$next/favicon.ico"
cp brand/waymark-study/png/apple-touch-icon-180.png "$next/apple-icon.png"
cp brand/waymark-study/png/social-card-1200x630.png "$next/opengraph-image.png"

# The site's own icons and link-preview image.
cp brand/switchback-labs/svg/favicon.svg favicon.svg
cp brand/switchback-labs/png/favicon.ico favicon.ico
cp brand/switchback-labs/png/apple-touch-icon-180.png apple-touch-icon.png
cp brand/switchback-labs/png/social-card-1200x630.png assets/social-card.png

# One zip per kit for the brand page. -X leaves out extra file attributes.
mkdir -p brand/downloads
for kit in switchback-labs waymark-study; do
  rm -f "brand/downloads/$kit-brand.zip"
  (cd brand && zip -qrX "downloads/$kit-brand.zip" "$kit")
done

echo "Rebuilt brand/switchback-labs, brand/waymark-study, the site icons and brand/downloads."
