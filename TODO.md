# Switchback Labs — combined to-do list

*This file is public on the studio site, like everything in this repo.*

Built on 2026-11-05 (last updated 2026-11-05, after QuoteBloom#1 merged) from every connected repo's TODO.md, PLAN*.md, ROADMAP.md, README "next steps", docs and code comments. When it was built, none of the repos had open GitHub issues or PRs, so everything here comes from those files. Covers 14 repos; netmap and diabetes-project were added on 2026-11-05.

**How it's ordered:** first fixes for problems people can hit today, then apps that are built and only need launch steps, then feature work. Within each tier, the item that finishes an app comes before the one that starts something new.

**Who does it:**
- 🧑 You: Apple Developer portal, App Store Connect, Xcode on a Mac, real devices, dashboards.
- 🤖 Me: code, docs and pages I can do from a session.
- 🤝 Both: I prepare it and you finish it.

---

## Tier 0 — Fix now (people can hit these today)

- [x] **CellarStories: the "Continue with Apple" button.** Already hidden since 2026-10-20 behind `APPLE_SIGN_IN_ENABLED = false`; its `TODO.md` was out of date (fixed in nmuschin/CellarStories#1). To bring it back: configure the Apple provider (`docs/deployment-guide.md` C3), then flip the flag. 🧑
- [ ] **Waymark Study: password-reset emails only reach your own address.** The sending domain `updates.waymarkstudy.com` is already verified in Resend (checked 2026-11-05), so what's left is setting `MAIL_FROM="Waymark Study <no-reply@updates.waymarkstudy.com>"` on the host, plus `APP_URL` as the production URL (link previews need it), then redeploying. 🧑
- [x] **QuoteBloom: `TODO.md` was copied into the app bundle.** Fixed in nmuschin/QuoteBloom#1, merged 2026-11-05. The same PR fixed the macOS build: the iOS-only widget is now embedded only in the iOS build. Confirmed in Xcode on iOS and macOS. 🤝

## Tier 1 — Ship what's built (closest to the finish line)

### 1. High Low Buffalo for iPhone
Web is live. iOS milestones I0–I6 and Phase 2 (Friends, History, Settings, Widget) are built, and the listing text was committed on Oct 29.
- [ ] App Store Connect app record + a demo account for App Review 🧑
- [ ] First TestFlight upload (`ios/README.md`) 🧑
- [ ] App Review notes: delete account, report and block paths (draft in `PLAN-ios.md` §8) 🤝
- [ ] Screenshots + the privacy "nutrition label" (email, name, user content, no tracking) 🧑
- [ ] Check `APNS_KEY_ID` / `APNS_PRIVATE_KEY` are in Vercel, or no push is sent 🧑
- [ ] Choose the icon direction from the three options on the canvas (branding round) 🧑

### 2. QuoteBloom
Everything for 1.0 is done except the listing.
- [ ] Screenshots (iPhone, iPad, Mac) 🧑
- [ ] Description, using the draft in `docs/app-store-listing.md` 🤝
- [ ] Privacy policy page declaring CloudKit and local notifications: `/privacy/quotebloom.html` in switchbacklabs#3 🤝
- [ ] Optional, after launch: a Mac widget. The widget code already handles macOS; the target needs macOS added, the App Sandbox entitlement and the Mac runpath. 🤖

### 3. Cite It Right (Apple app)
Phases 1–5 are merged. Phase 6 (Spanish, accessibility, icon, TestFlight prep) is written and waiting for its first Xcode build.
- [ ] First build of phase 6 in Xcode; fix whatever it turns up 🤝
- [ ] Test the live camera features (barcode, photo) on a real iPhone 🧑
- [ ] TestFlight: identifiers, App Store Connect record, App Privacy, uploads for iOS and Mac (`docs/testflight.md`) 🧑

### 4. CellarStories
Web went live on Oct 20. The iOS app is feature-complete for 1.0.
- [ ] Import your real journal (`.winenote` → `/import`) and check scores and photos survive, and that re-imports don't duplicate 🧑
- [ ] Re-run the acceptance test live with a friend on a real phone 🧑
- [ ] Test CloudKit sync across iPhone ⇄ iPhone and iPhone ⇄ Mac 🧑
- [ ] Submit iOS: App Store Connect record, screenshots, privacy policy URL, 17+ age rating (alcohol) 🧑
- [ ] Decide on an app icon (it was on the "revise later" list) 🤝

### 5. MarkdownDoctor (Mac)
All engineering for 1.0 is done. `Scripts/release.sh` archives, signs, notarizes and builds the DMG.
- [ ] Create a "Developer ID Application" certificate 🧑 *(has lead time)*
- [ ] Create a `notarytool` keychain profile (needs an app-specific password) 🧑
- [ ] App Store Connect record + name reservation, if you want the Mac App Store too 🧑
- [ ] Metadata: screenshots, description, keywords, support URL 🤝

### 6. FuelTrack
The 1.0 build settings, privacy manifest and validation are done.
- [ ] Deploy the CloudKit schema from Development to Production 🧑 *(blocks release: sync breaks without it)*
- [ ] Check the receipt-scanning extraction and the CSV import (0.5 items) 🤝
- [ ] Add more receipt-parser test fixtures beyond the 3 "oncue_regular" cases 🤖
- [ ] Fix the first-launch slowness when moving from Log to Map or Stats on iOS 🤖
- [ ] Check `FuelTrack.icon` at every size and appearance 🧑
- [ ] Screenshots + listing metadata 🧑

## Tier 2 — Feature work on apps you're using

### 7. JobTrack (Mac, version 0.6 in progress)
- [ ] **Decide the distribution channel first.** The bundled `JobTrackDigestMCP` helper isn't sandboxed and is launched by a fixed path, which the Mac App Store doesn't allow. The choice is a direct download with notarization (keeps the MCP helper) or the Mac App Store (needs a redesign). It shapes the whole 0.9 milestone. 🧑 decision, 🤖 write-up
- [ ] 0.6 polish: searchable text, help documentation, the toolbar margin TODO in `JobDetailView.swift`, two-pane layout for the views that show "No Job Selected", accessibility, Spanish to 100% 🤖
- [ ] Fix the broken `defaultsAreOpeningAndFourBeats` test (TODO in `JobTrackTests.swift`) 🤖
- [ ] Local notifications for follow-ups and interview dates 🤖
- [ ] Per-job "why this score" view built on the `FitScorer` details 🤖
- [ ] 0.7 automation round-trip (skill, scheduled search, a discoverable sync folder) → 0.8 charts → 0.9 generalize for other users (remove the MSL-specific language) 🤝

### 8. DateGlow
- [ ] 0.6: App Group + shared store, a widget target, iOS and Mac widgets, widget deep links, tappable menu bar rows 🤖
- [ ] Fill in 0.7–1.0 (currently empty) and an App Store checklist like FuelTrack's 🤝

### 9. Bellwether (iPhone + Watch)
- [ ] An app icon (it has none yet) 🤝
- [ ] "Paste your bell schedule" import instead of adding periods one at a time 🤖
- [ ] Half-day and exam schedules that shift bell times 🤖
- [ ] Localize the bare "Weekdays" string 🤖
- [ ] Write a 1.0 / TestFlight checklist; there's no plan doc yet 🤖

### 10. Waymark Study (after the Tier 0 email fix)
- [ ] FSRS parameter optimization per user, once there are enough reviews 🤖
- [ ] Tier 4 nice-to-haves: cloze cards (which also unblocks cloze import from Anki), reverse cards, reminders, text-to-speech 🤖
- [ ] An iOS client (roadmap section "Toward an iOS client") 🤝

### 11. ClassroomDesigner
Every module in `PLAN.md`'s build order is built, and there's no open backlog.
- [ ] Try it with a real class or a teacher, and collect what's missing 🧑
- [ ] Link-preview image, once you share the production URL 🤖

### 12. Netmap (Mac + iPhone network scanner)
Phases 1–3 are written (presence monitoring for the Home Assistant Pi, history, notifications, both apps, iCloud sync with push alerts, and the general scanner) but **have never been compiled**: it was written without a Swift toolchain, and the logic was checked by mirroring it in Python (~160 checks).
- [ ] Confirm the assumptions on your network first: `arp -an`, `dns-sd -B _home-assistant._tcp .`, `nc -vz <pi-ip> 8123`, and note the Pi's MAC on both wired and Wi-Fi (README, "Before building") 🧑
- [ ] First build: `xcodegen generate`, then `swift build` / `swift test`, and fix the compile errors. Most likely in `ICMPProbe`, `TCPConnectProbe`, the `#Predicate` macros and the SwiftUI views 🤝
- [ ] iCloud setup per `docs/CLOUDKIT.md`: container ID, the queryable index, deploy the schema to Production, APNs environment 🧑
- [ ] Wire the scan screens (`ScanView`, `ScanResultsView`, `ScanDiffView`) into both apps' navigation 🤖
- [ ] App icons and asset catalogs 🤝
- [ ] Phase 4: the nmap engine and privileged helper (`ScanProfile` already builds the commands) 🤖
- [ ] Phase 5: a headless watcher executable (`NetmapWatch` is already UI-free) 🤖
- [ ] Later: the full IEEE vendor list instead of the seed `OUIDatabase`, and two-way device-settings sync 🤖

## Other repos

### diabetes-project
Only a README so far: "Project looking at the cost of diabetes and the shift to GLP-1 usage." Not an app, so it's kept off the studio site.
- [ ] Decide the question, the data sources and the output (report, notebook or dashboard), then add a plan to the repo 🤝

## Studio (Switchback Labs)

- [ ] **Privacy policy and support pages.** Written in nmuschin/switchbacklabs#3 (draft) for QuoteBloom, FuelTrack, DateGlow, Bellwether, MarkdownDoctor and CellarStories, plus `/support.html`. Waiting on a contact email to replace the `CONTACT_EMAIL` placeholder. 🧑
- [ ] Add App Store and website links to the app grid as each app ships 🤖
- [ ] Branding round, as planned: the HighLowBuffalo icon choice, plus icons for Bellwether and CellarStories 🤝
- [ ] Delete the leftover branches `claude/studio-site`, `claude/brand-resources` (switchbacklabs) and `claude/waymark-brand-icons` (waymarkstudy). I can't delete branches from a session. 🧑

---

## Suggested order for the next two weeks

1. Tier 0: fix Waymark's reset email (set `MAIL_FROM` and `APP_URL`, then redeploy). The QuoteBloom fix is merged.
2. Start the Apple paperwork that has lead time, all at once: the Developer ID certificate, the notarytool profile, and App Store Connect records for HLB, QuoteBloom, CellarStories and FuelTrack. Deploy FuelTrack's CloudKit schema.
3. Pick a contact email so the privacy and support pages (switchbacklabs#3) can go live; every submission then has its URLs.
4. Ship in this order: **High Low Buffalo → QuoteBloom → Cite It Right → CellarStories → MarkdownDoctor → FuelTrack**. Each one needs mostly screenshots and a listing, and they share the same App Store Connect steps, so doing them back to back is quickest.
5. Then feature work: the JobTrack channel decision and 0.6 polish, DateGlow widgets, the Bellwether icon and schedule import, and Netmap's first build.
