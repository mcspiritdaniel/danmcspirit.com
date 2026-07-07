# Handoff: danmcspirit.com — Personal Site

## Overview
A personal site for Dan McSpirit — advisor, investor, and teacher — structured as a three-column editorial layout. The three columns are Identity (who he is), Work (career history), and Projects (built things). The aesthetic is warm paper-and-ink: cream backgrounds, serif editorial type, monospaced captions, and a navy accent.

## About the Design Files
The files in this bundle are **high-fidelity design references created in HTML** — not production code to copy directly. The task is to recreate these designs in a real deployment environment. The current prototype is a single self-contained `.dc.html` file; the production version should be a proper static site (plain HTML/CSS, Next.js, Astro, or similar) deployed to Vercel or equivalent. No framework requirement — choose whatever is cleanest for a mostly-static personal site.

## Fidelity
**High-fidelity.** Colors, typography, spacing, interactions, and copy are all final. Recreate pixel-perfectly.

---

## Layout

### Desktop (≥ 1200px)
Three fixed-width columns in a horizontal row, each independently scrollable, filling 100vh. The shell has `min-width: 1362px` and `overflow: hidden` so the page never reflows below that width on desktop.

| Column | Width | Background | Border |
|--------|-------|------------|--------|
| Identity (left) | 600px | `#EDE7D9` | `1px solid #DCD3C2` on right |
| Work (middle) | 362px | `#F4F0E7` | `1px solid #DCD3C2` on right |
| Projects (right) | `flex: 1`, min 440px | `#FBFAF6` | — |

Each column scrolls independently. Hide the scrollbar (`scrollbar-width: none`, `::-webkit-scrollbar { display: none }`). Each column has a sticky header and a bottom scroll-fade overlay.

### Mobile (< 1200px)
Columns stack vertically into one centered ~680px column. Each column becomes full-width with horizontal padding of `max(24px, (100% - 680px) / 2)`. Sticky headers become static. Scroll fades and "scroll ↓" cues are hidden. The `<h1>` drops to `32px`. The shell loses `height: 100vh` and `overflow: hidden` and becomes freely scrolling. A `<br class="mbreak">` in the headline is `display: none` on desktop and `display: inline` on mobile.

---

## Design Tokens

### Colors
```
Paper dark    #EDE7D9   Identity column bg
Paper mid     #F4F0E7   Work column bg
Paper light   #FBFAF6   Projects column bg
Rule          #DCD3C2   Borders, dividers
Rule light    #E8E1D2   Projects column borders
Ink           #1B2330   Primary text
Ink mid       #3B362B   Body copy
Ink light     #5C5648   Secondary body
Muted         #7A7468   Tertiary text
Faint         #A39A88   Labels, timestamps
Ghosted       #B3A88F   Scroll cues, copyright
Navy          #23426A   Accent, links, section labels
Tag text      #6E675B   Pill tag text
Tag bg        transparent
Warm tan      #8A8273   Location text
Gold          #9A7B3E   In-progress label text
Gold dot      #C79A45   Pulsing dot
```

### Typography
All three typefaces loaded from Google Fonts:
```
font-family: 'Newsreader', serif         — editorial, headings, body prose
font-family: 'IBM Plex Mono', monospace  — labels, tags, captions, metadata
font-family: 'IBM Plex Sans', sans-serif — shell default / utility text
```

Google Fonts import URL:
```
https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,300..500&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap
```

### Type Scale
| Use | Family | Size | Weight | Additional |
|-----|--------|------|--------|------------|
| Name / nav | Newsreader | 21px | 500 | `letter-spacing: -0.01em` |
| H1 headline | Newsreader | 40px (32px mobile) | 400 | `line-height: 1.04`, `letter-spacing: -0.02em` |
| Section label (navy) | IBM Plex Mono | 11px | 400 | `letter-spacing: 0.14em`, `text-transform: uppercase` |
| Column header label | IBM Plex Mono | 12px | 400 | `letter-spacing: 0.16em`, `text-transform: uppercase` |
| Body prose | Newsreader | 17px | 400 | `line-height: 1.6` |
| Body small | IBM Plex Sans | 13.5px | 400 | `line-height: 1.55` |
| Project card body | IBM Plex Sans | 14.5px | 400 | `line-height: 1.6` |
| Project title | Newsreader | 26px | 400 | `line-height: 1.12`, `letter-spacing: -0.01em` |
| Work entry title | Newsreader | 20–21px | 400 | `line-height: 1.15` |
| Blockquote | Newsreader | 24px | 400 | italic, `line-height: 1.28`, `letter-spacing: -0.01em` |
| Caption / placard | IBM Plex Mono | 10.5px | 400 | `letter-spacing: 0.14em`, uppercase |
| Tag pills | IBM Plex Mono | 10.5px | 400 | — |
| Link / email | Newsreader | 20px | 400 | `letter-spacing: -0.01em` |
| Metadata / location | IBM Plex Mono | 11px | 400 | `letter-spacing: 0.04em` |

### Spacing & Borders
- Column padding: `40px` horizontal, `40px` top (Identity); `24px 34px` (Work header), `30px 34px 48px` (Work body); `24px 48px 20px` (Projects header), `40px 48px 56px` (Projects body)
- Card border-radius: `4px` (portrait card, work highlight card); `5px` (browser mock frames); `3px` (teaching card)
- Tag pill padding: `5px 9px`
- Dividers: `1px solid #DCD3C2` (Identity/Work), `1px solid #E2DACA` (within Work entries)
- Scroll fade height: `52px` (Identity, Work), `56px` (Projects)
- Section bottom spacer before scroll fade: `46px`

---

## Screens / Views

### Column 1 — Identity

**Sticky-ish header area (scrolls with content):**
- Name "Dan McSpirit" — Newsreader 21px/500, left; "Denver, Colorado" — IBM Plex Mono 11px `#8A8273`, right. `margin-bottom: 30px`.
- Role line "Advisor | Builder | Teacher" — IBM Plex Mono 11px navy uppercase, `letter-spacing: 0.14em`, `margin-bottom: 18px`
- H1: "Closing the gap. Creating value." — Newsreader 40px/400, `margin-bottom: 26px`. On mobile a `<br>` between the two sentences breaks it to two lines.

**Portrait card:** `height: 260px`, `border: 1px solid #DCD3C2`, `border-radius: 4px`, `overflow: hidden`, `background: #EDE7D9`, `margin-bottom: 30px`. Two children side by side (flex row):
- Left pane (`flex: 1`): caption block pinned to bottom-left via `justify-content: flex-end`. Contains navy mono uppercase label "Principal" (10.5px, `letter-spacing: 0.14em`, `margin-bottom: 9px`) and Newsreader 19px "Otherwhere Capital".
- Right pane (`flex: 0 0 58%`): `background: url('assets/portrait-sketch.png') center top / cover no-repeat`. Two overlay gradients:
  - Left fade: `linear-gradient(90deg, #EDE7D9 0%, rgba(237,231,217,0) 27%)`
  - Bottom fade: `height: 72px`, `linear-gradient(to bottom, rgba(237,231,217,0) 0%, #EDE7D9 100%)`

**Body prose:** Two paragraphs, Newsreader 17px `#3B362B`, `line-height: 1.6`, `margin-bottom: 16px` / `28px`.

**Divider:** `1px solid #DCD3C2`, `margin: 4px 0 26px`.

**Hard-won truth block:**
- Section label: "Hard-won truth" — IBM Plex Mono 11px `#A39A88` uppercase, `margin-bottom: 14px`
- Blockquote: Newsreader 24px italic `#1B2330`, `line-height: 1.28`, `margin-bottom: 12px`. Text: *"Finance golden rule: You can't get somethin' for nothin'."*
- Sub-copy: 13.5px `#5C5648`, `line-height: 1.55`, `margin-bottom: 30px`

**Divider.**

**Contact block:**
- Label: "Contact" — IBM Plex Mono 11px `#A39A88` uppercase, `margin-bottom: 12px`
- Email link: `mcspiritdaniel@gmail.com` — Newsreader 20px navy, underline on hover, `display: block`, `margin-bottom: 14px`
- Row: LinkedIn ↗ link (IBM Plex Mono 11px navy, underline on hover) · "© 2026" (`#A39A88`)

**Bottom:** `46px` spacer + `52px` scroll-fade overlay (gradient to `#EDE7D9`).

---

### Column 2 — Work

**Sticky header:** `position: sticky; top: 0; z-index: 5`. Background `#F4F0E7`, `border-bottom: 1px solid #DCD3C2`. Padding `24px 34px 18px`.
- Row: "Work" label (IBM Plex Mono 12px uppercase `#1B2330`) + "scroll ↓" (IBM Plex Mono 10px uppercase `#B3A88F`, hidden on mobile)
- Italic sub-headline: Newsreader 16px `#5C5648` italic. Text: *"The thread through every role: a pull toward steep learning curves — and a habit of leading the climb."*

**Body:** padding `30px 34px 48px`.

**Section: Advisory & investing** (navy label, `margin-bottom: 16px`)

Entry — Otherwhere Capital:
- Date: "2019 — Present" — IBM Plex Mono 11px `#23426A`
- Title: "Otherwhere Capital" — Newsreader 21px
- Role: "Principal | Private Capital Advisory" — IBM Plex Mono 11px `#736E62`
- Body: 12.5px `#7A7468`, `line-height: 1.55`
- Bottom border: `1px solid #E2DACA`, `padding-bottom: 24px`, `margin-bottom: 24px`

**Section: Capital markets** (IBM Plex Mono 11px `#A39A88` uppercase)

Entry — BMO Capital Markets:
- Date: "2004 — 2019" — IBM Plex Mono 11px `#A39A88`
- Title: "BMO Capital Markets" — Newsreader 20px
- Role: "Director | Institutional Equity Research"
- Body: 12.5px `#7A7468`
- Bottom border, `margin-bottom: 22px`

Entry — First Albany Corporation:
- Date: "1996 — 2004"
- Title: "First Albany Corporation"
- Role: "Senior Associate | Investment Banking & Analyst | CFO Office"
- Body: 12.5px `#7A7468`
- Bottom border `1px solid #DCD3C2`, `margin-bottom: 30px`

**Section: In the classroom** (navy label)

Denver Public Schools card: `background: #EDE7D9`, `border: 1px solid #DCD3C2`, `border-radius: 3px`, `padding: 20px`, `margin-bottom: 34px`.
- Title: "Denver Public Schools" — Newsreader 20px
- Body: 13.5px `#5C5648`, `line-height: 1.6`

**Section: Education & credentials** (`#A39A88` label)

Four items in a flex column with `gap: 11px`, 13.5px `#3B362B`:
- The Wharton School (WMP21)
- CFA Charter
- CMA Certificate
- FSA Credential

Each prefixed with a navy `—` dash (IBM Plex Mono 11px, `padding-top: 2px`).

**Bottom:** `46px` spacer + `52px` scroll-fade to `#F4F0E7`.

---

### Column 3 — Projects

**Sticky header:** `position: sticky; top: 0; z-index: 5`. Background `#FBFAF6`, `border-bottom: 1px solid #E8E1D2`. Padding `24px 48px 20px`.
- Row: "Projects" label + "scroll ↓"
- Italic sub-headline: Newsreader 16px `#5C5648` italic. Text: *"Turning the conventional — the Excel model, the desk calculator — into modern, action-oriented apps."*

**Body:** `padding: 40px 48px 56px`.

Each project is a `.pcard` flex row (`flex-wrap: wrap`, `gap: 34px`, `margin-bottom: 52px`) with a left text pane and a right browser-mock pane.

**Left pane:** `flex: 1 1 270px`, `min-width: 240px`
**Right pane:** `flex: 2 1 420px`, `min-width: 330px`

On mobile the card stacks vertically (both panes become `width: 100%`).

**Browser mock frame structure:**
- Outer: `border: 1px solid #E8E1D2`, `border-radius: 5px`, `overflow: hidden`, `box-shadow: 0 1px 2px rgba(0,0,0,0.05)`
- Title bar: `height: 34px`, `background: #F2EFE8`, `border-bottom: 1px solid #E8E1D2`, `padding: 0 13px`. Three `9px` circles (`#DAD3C5`) + URL text (IBM Plex Mono 10.5px `#8A8273`)
- Content area: `height: 300px`, `overflow: hidden`. Live iframe scaled to 50% (`width: 200%; height: 600px; transform: scale(0.5); transform-origin: top left; pointer-events: none`). A full-size transparent `<a>` overlay links to the live URL.

**Project 1 — SpaceX (SPCX) Valuation Analysis**
- URL: `https://spcx-valuation-analysis.vercel.app/`
- "view ↗" link below title
- Description: *"SpaceX defies a single valuation line. This sum-of-the-parts framework breaks the business into its constituent segments and lets you stress-test the assumptions that drive the range — rebuilt from Excel into an interactive app you can actually argue with."*
- Tags: `ms excel` · `claude chat + design + code`

**Project 2 — LINEA Valuation Analysis**
- URL: `https://linea-valuation-analysis.vercel.app/`
- Description: *"A DCF and fee-multiple framework for the Linea blockchain protocol — the kind of model that usually lives buried in a spreadsheet, rebuilt as an interactive tool you can actually steer."*
- Tags: `ms excel` · `claude chat + cursor`

**Project 3 — RPN Financial Calculator**
- URL: `https://rpn-financial-calculator.vercel.app/`
- Description: *"A browser-based replica of the HP 12c RPN financial calculator — the desk classic a generation of analysts learned on, including yours truly, faithfully rebuilt for the web."*
- Tags: `hp 12c` · `claude chat + cursor`

---

## Interactions & Behavior

### Links
```css
.lnk {
  color: #23426A;
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: border-color 0.15s;
}
.lnk:hover { border-color: #23426A; }
```
All `<a>` elements should follow this style. External links open in `target="_blank"`.

### Scroll fades
Each column has a `position: sticky; bottom: 0` gradient overlay that creates a fade-to-background effect at the bottom of each scrollable column. It is `pointer-events: none` so it doesn't block interaction.

### Project card hover
`.pcard { transition: transform 0.2s ease; }` — subtle lift on hover is implied by this class; implement as `transform: translateY(-2px)` on hover if desired (the current prototype registers the transition but no explicit hover rule — add one).

### Mobile breakpoint (`max-width: 1200px`)
- Shell: `flex-direction: column`, `height: auto`, `overflow: visible`
- Each column: full width, `height: auto`, `overflow: visible`, no right border, bottom border instead
- Sticky headers → `position: static`
- Scroll fades + "scroll ↓" cues → `display: none`
- H1 → `font-size: 32px`
- Portrait card: stacks vertically (left caption above, portrait below — or revisit layout)
- Project cards: left and right panes stack vertically

---

## Assets

| File | Description |
|------|-------------|
| `assets/portrait-sketch.png` | Warm sepia pencil-sketch portrait. Used in the Identity column portrait card, `object-position: center top`. |

---

## Files in This Package

| File | Description |
|------|-------------|
| `Personal Site.dc.html` | Full high-fidelity design prototype. Open in a browser to see the live design. This is the reference — not production code. |
| `assets/portrait-sketch.png` | Portrait asset used in the design. |

---

## Deployment Notes

- Static site — no backend required.
- Deploy to Vercel, Netlify, or GitHub Pages.
- Domain: `danmcspirit.com`
- The three project iframes (SpaceX, LINEA, RPN) load live external URLs. They will load in production as long as those URLs remain live and don't set `X-Frame-Options: DENY`. If any do, replace the iframe with a static screenshot.
- Google Fonts requires an internet connection. For full offline capability, self-host the three typefaces.
