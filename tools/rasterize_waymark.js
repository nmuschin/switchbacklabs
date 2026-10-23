// Render the Waymark Study SVGs to PNG with headless Chromium. Usage: node rasterize_waymark.js <svgDir> <pngDir>
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const [svgDir, pngDir] = process.argv.slice(2);
fs.mkdirSync(pngDir, { recursive: true });

// [svg file, output name, width] (height follows the SVG's aspect ratio)
const jobs = [
  ['app-icon.svg', 'app-icon-1024.png', 1024],
  ['app-icon.svg', 'apple-touch-icon-180.png', 180],
  ['waymark-tile.svg', 'waymark-tile-512.png', 512],
  ['waymark-tile.svg', 'waymark-avatar-400.png', 400],
  ['waymark-mark.svg', 'waymark-mark-1024.png', 1024],
  ['waymark-mark-white.svg', 'waymark-mark-white-1024.png', 1024],
  ['waymark-lockup-horizontal.svg', 'waymark-lockup-horizontal@2x.png', 1200],
  ['waymark-lockup-horizontal-dark.svg', 'waymark-lockup-horizontal-dark@2x.png', 1200],
  ['waymark-lockup-stacked.svg', 'waymark-lockup-stacked@2x.png', 640],
  ['waymark-lockup-stacked-dark.svg', 'waymark-lockup-stacked-dark@2x.png', 640],
  ['social-card.svg', 'social-card-1200x630.png', 1200],
  ['favicon.svg', 'favicon-16.png', 16],
  ['favicon.svg', 'favicon-32.png', 32],
  ['favicon.svg', 'favicon-48.png', 48],
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const [src, out, width] of jobs) {
    const svg = fs.readFileSync(path.join(svgDir, src), 'utf8');
    const [, vw, vh] = svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);
    const height = Math.round((width * Number(vh)) / Number(vw));
    await page.setViewportSize({ width, height });
    const sized = svg.replace(/width="[^"]*" height="[^"]*"/, `width="${width}" height="${height}"`);
    await page.setContent(`<html><body style="margin:0;background:transparent">${sized}</body></html>`);
    await page.screenshot({ path: path.join(pngDir, out), omitBackground: true, clip: { x: 0, y: 0, width, height } });
  }
  await browser.close();
  console.log(`rendered ${jobs.length} PNGs`);
})();
