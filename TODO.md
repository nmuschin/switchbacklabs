# Switchback Labs — combined to-do list

*This file is public on the studio site, like everything in this repo.*

Built on 2026-11-05 (last updated 2026-11-08: Waymark email was already set up; CloudKit schemas deployed for FuelTrack, DateGlow and CellarStories) from every connected repo's TODO.md, PLAN*.md, ROADMAP.md, README "next steps", docs and code comments. When it was built, none of the repos had open GitHub issues or PRs, so everything here comes from those files. Covers 14 repos; netmap and diabetes-project were added on 2026-11-05.

**How it's ordered:** first fixes for problems people can hit today, then apps that are built and only need launch steps, then feature work. Within each tier, the item that finishes an app comes before the one that starts something new.

**Who does it:**
- 🧑 You: Apple Developer portal, App Store Connect, Xcode on a Mac, real devices, dashboards.
- 🤖 Me: code, docs and pages I can do from a session.
- 🤝 Both: I prepare it and you finish it.

---

## Tier 0 — Fix now (people can hit these today)

- [x] **CellarStories: the "Continue with Apple" button.** Already hidden since 2026-10-20 behind `APPLE_SIGN_IN_ENABLED = false`; its `TODO.md` was out of date (fixed in nmuschin/CellarStories#1). To bring it back: configure the Apple provider (`docs/deployment-guide.md` C3), then flip the flag. 🧑
- [x] **Waymark Study: password-reset emails.** The sending domain `updates.waymarkstudy.com` is verified in Resend, and `MAIL_FROM` and `APP_URL` were already set on the host (confirmed 2026-11-08). Worth one test: request a reset for a second address you own and check it arrives. 🧑
- [x] **QuoteBloom: `TODO.md` was copied into the app bundle.** Fixed in nmuschin/QuoteBloom#1, merged 2026-11-05. The same PR fixed the macOS build: the iOS-only widget is now embedded only in the iOS build. Confirmed in Xcode on iOS and macOS. 🤝

## Decide this week (these have lead time and block several launches)

- [ ] **Publish as yourself or as a company?** The App Store shows the developer's legal name. An individual Apple Developer account shows your personal name; showing a studio name needs an organization account, which requires a legal entity (such as an LLC) and a free D-U-N-S number, and that can take a week or two. Decide before the first submission, because changing the seller later means transferring every app. 🧑
- [ ] **Studio name and domain** (Saturday's reminder). It feeds the developer name, the contact email for the privacy and support pages, and the website address. 🧑
- [ ] **Start the Apple paperwork in one sitting:** the Developer ID certificate and `notarytool` profile (MarkdownDoctor), and App Store Connect records for High Low Buffalo, QuoteBloom, CellarStories and FuelTrack. 🧑

## Tier 1 — Ship what's built (closest to the finish line)

### 1. High Low Buffalo (HLB) for iPhone
Web is live. iOS milestones I0–I6 and Phase 2 (Friends, History, Settings, Widget) are built, and the listing text was committed on Oct 29.
- [ ] App Store Connect app record + a demo account for App Review 🧑
- [ ] First TestFlight upload (`ios/README.md`) 🧑
- [ ] App Review notes: delete account, report and block paths (draft in `PLAN-ios.md` §8) 🤝
- [ ] Screenshots + the privacy "nutrition label" (email, name, user content, no tracking) 🧑
- [ ] Check `APNS_KEY_ID` / `APNS_PRIVATE_KEY` are in Vercel, or no push is sent 🧑
- [x] Icon: the same bison on a terracotta gradient tile (option 1, kept simple while the studio name may still change). Merged in nmuschin/HighLowBuffalo#20 on 2026-11-06 🤝
- [ ] Check the new icon on your Mac: the in-app logo on the Welcome screen shows the gradient (not a flat or black tile), the Home Screen app icon, and the favicon on the live site in a private window 🧑

### 2. QuoteBloom
Everything for 1.0 is done except the listing.
- [ ] Screenshots (iPhone, iPad, Mac) 🧑
- [ ] Description, using the draft in `docs/app-store-listing.md` 🤝
- [ ] CloudKit schema to Production. Not done yet: as of 2026-11-08 Development only has the built-in `Users` type, because no development build has synced yet. QuoteBloom calls CloudKit directly, so its types are `UserQuote` and `Favorite` (no `CD_` prefix). Steps: run a debug build signed into iCloud, add a quote and favorite a built-in one; then in Development add a **QUERYABLE** index on `recordName` for both types (the app's fetch-all queries fail without it); then Deploy Schema Changes 🧑
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
- [x] Deploy the CloudKit schema from Development to Production (done 2026-11-08) 🧑
- [ ] Submit iOS: App Store Connect record, screenshots, privacy policy URL, 17+ age rating (alcohol) 🧑
- [ ] Decide on an app icon (it was on the "revise later" list) 🤝

### 5. MarkdownDoctor (Mac)
All engineering for 1.0 is done. `Scripts/release.sh` archives, signs, notarizes and builds the DMG.
- [ ] Create a "Developer ID Application" certificate 🧑 *(has lead time)*
- [ ] Create a `notarytool` keychain profile (needs an app-specific password) 🧑
- [ ] App Store Connect record + name reservation, if you want the Mac App Store too 🧑
- [ ] Metadata: screenshots, description, keywords, support URL 🤝
- [ ] Pick where the notarized DMG is downloaded from (a GitHub Release, or a download link on the studio site) and add it to the app grid 🤝

### 6. FuelTrack
The 1.0 build settings, privacy manifest and validation are done.
- [x] Deploy the CloudKit schema from Development to Production (done 2026-11-08; `CD_Car` and `CD_FuelEntry`) 🧑
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
- [ ] Deploy the CloudKit schema to Production before shipping beyond your own Mac 🧑
- [ ] Per-job "why this score" view built on the `FitScorer` details 🤖
- [ ] 0.7 automation round-trip (skill, scheduled search, a discoverable sync folder) → 0.8 charts → 0.9 generalize for other users (remove the MSL-specific language) 🤝

### 8. DateGlow
- [ ] 0.6: App Group + shared store, a widget target, iOS and Mac widgets, widget deep links, tappable menu bar rows 🤖
- [ ] Fill in 0.7–1.0 (currently empty) and an App Store checklist like FuelTrack's 🤝
- [x] Deploy the CloudKit schema to Production (done 2026-11-08) 🧑

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
- [ ] Branding round, as planned: icons for Bellwether and CellarStories (HLB's is done) 🤝
- [x] **Shared working preferences in every repo.** A short "Working preferences" section in each of the 14 repos' `CLAUDE.md`, pointing at the full version in nmuschin/CodeAI. Merged 2026-11-05. 🤖
- [ ] Delete the leftover branches (the "Delete branch" button on each merged PR; I can't delete branches from a session): `claude/studio-site`, `claude/brand-resources` (switchbacklabs), `claude/waymark-brand-icons` (waymarkstudy), `claude/todo-update-nov5` and `claude/todo-hlb-icon` (switchbacklabs), `claude/working-preferences` in the 13 other repos, `claude/hlb-gradient-tile` (HLB), `claude/hlb-nickname` (CodeAI) and `claude/eloquent-curie-sw2h86` (ClassroomDesigner). 🧑
- [ ] Netmap's default branch is `claude/confident-bohr-i73ycp`: rename it to `main` (Settings → Branches) 🧑

---

## Plan to finish (week by week)

Rough times, assuming evenings and weekends. Each week ends with something shipped or submitted. If a week slips, push the whole plan back a week rather than starting the next app early.

### Week 1 · Nov 5–8 · decisions and paperwork (~3 h)
1. ~~Waymark Study: set `MAIL_FROM` and `APP_URL` on the host~~ (already set).
2. Decide: individual or company developer account, and the studio name and domain. Start a D-U-N-S request if going the company route.
3. Apple paperwork in one sitting: Developer ID certificate, `notarytool` profile, and App Store Connect records for HLB, QuoteBloom, CellarStories and FuelTrack (1–2 h).
4. Deploy CloudKit schemas to Production: FuelTrack, DateGlow and CellarStories done 2026-11-08. QuoteBloom still needs a development build to sync first (see its section).

### Week 2 · Nov 9–15 · High Low Buffalo and QuoteBloom (~6 h)
1. HLB: TestFlight upload, demo account, review notes, screenshots, submit.
2. QuoteBloom: screenshots for iPhone, iPad and Mac, description from the draft, submit.
3. Studio: once the contact email is chosen, merge the privacy and support pages so both apps have their URLs.

### Week 3 · Nov 16–22 · Cite It Right and MarkdownDoctor (~6 h)
1. Cite It Right: first phase-6 build in Xcode, camera test on a real iPhone, TestFlight.
2. MarkdownDoctor: run `Scripts/release.sh`, publish the DMG, add it to the site.

### Week 4 · Nov 23–29 · CellarStories (lighter week: Thanksgiving)
1. Import your real journal, run the live acceptance test with a friend, test iCloud sync across devices.
2. Screenshots, 17+ age rating, submit.

### Week 5 · Nov 30–Dec 6 · FuelTrack
1. Check receipt scanning and CSV import, fix the slow first switch to Map or Stats, more parser test fixtures.
2. Check the icon at every size, screenshots, submit.

### December · feature work
JobTrack's distribution decision and 0.6 polish, DateGlow widgets, the Bellwether icon and schedule import, and Netmap's first build.

## App Store submission checklist (use for every app)

- [ ] Bundle ID registered, and the App Store Connect record created
- [ ] Version and build number bumped; export-compliance answer set (`ITSAppUsesNonExemptEncryption`)
- [ ] Privacy manifest (`PrivacyInfo.xcprivacy`) present in the app and each extension
- [ ] iCloud apps: CloudKit schema deployed to Production
- [ ] Privacy policy URL and support URL (the studio site's `/privacy/<app>.html` and `/support.html`)
- [ ] App Privacy "nutrition label" filled in, matching the privacy policy
- [ ] Age rating questionnaire
- [ ] Screenshots: the largest iPhone (6.9", 1320 × 2868), 13" iPad (2064 × 2752) if it runs on iPad, and a Mac size (such as 2880 × 1800) for Mac apps. Check App Store Connect for the current list.
- [ ] Name, subtitle, description, keywords, promotional text
- [ ] Apps with sign-in: a demo account and review notes explaining account deletion, reporting and blocking
- [ ] Archive, upload, test it yourself in TestFlight, then submit

## Tips for finishing on time

- **One app in flight at a time.** Finish its submission before starting the next; a half-submitted app costs more to pick back up than it saves.
- **Batch the same kind of work.** All App Store Connect records in one sitting, all screenshots in another. In the Simulator, `xcrun simctl io booted screenshot shot.png` saves a full-resolution screenshot.
- **Ask Claude for the text.** Listings, review notes and release notes can be drafted from each repo's README and docs; you edit and paste.
- **Keep this file current.** Tick items off as they land and print a fresh copy each week; it's the one list.
- **Expect one App Review round-trip.** First submissions are often rejected once for something small, like a missing demo account or a privacy-label mismatch. Leave a few days of slack before any date that matters.

## Quick reference

- Studio site: https://nmuschin.github.io/switchbacklabs/ (brand page at `/brand.html`)
- Live web apps: High Low Buffalo at https://www.highlowbuffaloapp.com, CellarStories at https://cellarstories.app, Cite It Right at https://citeitright.org
- Email (Resend, sending only): `updates.cellarstories.app`, `updates.waymarkstudy.com`, `highlowbuffaloapp.com`. `hello@highlowbuffaloapp.com` forwards to Gmail.
- iCloud apps that need a CloudKit schema in Production: QuoteBloom, JobTrack, Netmap. Done: FuelTrack, DateGlow, CellarStories. To check one: CloudKit Console → container → switch the P/D badge at the top → Schema → Record Types; Production should list the app's types, not just the built-in `Users`.
