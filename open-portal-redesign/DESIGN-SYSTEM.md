# FCG Developer Platform — design system

How to build a new page or app screen that matches the twelve pages in
[variant-b-impeccable/](variant-b-impeccable). Written to be followed cold, without reading the existing
CSS first.

The authority for this system is the FCG marketing site's own stylesheet, not a design tool's guess. When
this document and the live marketing site disagree, the live site wins and this document is wrong.

---

## 0. The fastest correct path

Do not hand-write a new page. The twelve pages are generated:

```bash
cd "open-portal-redesign/variant-b-impeccable"
python3 build-pages.py
```

`build-pages.py` lifts the `<head>`, the whole token/CSS block and the behaviour script **verbatim** out of
`index.html`, generates the nav and footer from one list, and writes them back into `index.html` too. So a
token cannot drift between pages. Page bodies live in `pages_content.py`.

**To add a page:** append one entry to `PAGES` in `pages_content.py` and add its label to `NAV` in
`build-pages.py` if it belongs in the primary nav. Then run the build. It refuses to build if you break one
of the copy rules in §5.

**To change a token, the nav or the footer:** change it in `index.html` (tokens, CSS) or in `build-pages.py`
(`NAV`, `FOOTER_COLS`) and rebuild. Never edit a generated page directly — the next build overwrites it.

Generated pages are: `app-management`, `api-docs-hotel`, `api-docs-hotel-process`, `api-docs-hotel-apis`,
`api-docs-flink`, `api-docs-errors`, `sdk`, `skills`, `ai-assistant`, `login`, `register`. `index.html` is
the shell donor and is only patched, not regenerated.

---

## 1. Tokens

Copy this block verbatim. Do not introduce a colour that is not here.

```css
:root{
  --ink:#0F1114;              /* all primary text */
  --ink-2:#111827;            /* chip and badge text, method pills */
  --muted:#6B7280;            /* body copy, captions, secondary links */
  --muted-card:#5A6069;       /* muted text ON #F3F4F6 — keeps AA */
  --card:#F3F4F6;             /* the only fill; this is what "depth" means here */
  --line:#D1D5DB;             /* visible hairline: card and table borders */
  --hair:rgba(15,17,20,.08);  /* quieter hairline: row dividers */
  --hair-soft:rgba(15,17,20,.06); /* quietest: list item dividers */
  --shell:rgba(15,17,20,.04); /* nav shell and tab rail ground */
  --accent:#F97316;           /* graphics only — see §2 */
  --accent-ink:#F97316;       /* small orange TEXT — see §2 */
  --footer:#f7f8fa;           /* footer and auth-form ground */
  --dark:#0F1114;             /* the terminal block, the only dark surface */
  --dark-line:#26282C;
  --dark-fg:#E7E8EA;
  --dark-muted:#9198A1;
  --sans:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,SFMono-Regular,"Cascadia Mono","Liberation Mono",Menlo,Consolas,monospace;
  --wrap:1200px;              /* content cap */
  --sec:128px;                /* section vertical padding */
  --ease:cubic-bezier(.16,1,.3,1);
  --ease-out:cubic-bezier(.23,1,.32,1);
  --ease-in-out:cubic-bezier(.77,0,.175,1);
  --press:160ms;
  --hover:160ms;
}
```

Ground is `#FFF`. Flat: **no drop shadows on light surfaces.** Depth is the `--card` fill plus a `--line`
hairline, nothing else.

---

## 2. The accent law

This is the single most important rule. Break it and the page stops looking like FCG.

**`--accent` may fill only:** a 6px status dot, a 12px eyebrow dash, a thin arc, the terminal cursor, the
focus-visible ring, and one 28px circular arrow on a tertiary link.

**`--accent` may never fill** a button, a panel, a card, a table cell, a nav item, or a gradient. The
primary button is a black pill. Always.

**Where orange text is correct** (all through `--accent-ink`):

| Place | Example |
| --- | --- |
| Section eyebrow label | `— SUPPORTS BOTH SDK AND API INTEGRATION` |
| The second clause of a headline, after a comma | `Twelve codes, <em>four families.</em>` |
| The lead-in phrase of a lede | `<b>Major global hotel inventory</b> over one standardised interface.` |
| The unit suffix of a statistic | `4.35` ink + `<u>M+</u>` orange |
| Mono micro-labels on cards and steps | `G-LINK HOTEL`, `STEP 01` |
| A tinted status chip | `● Sandbox ready` on `rgba(249,115,22,.07)` |

**One orange emphasis per block.** If a heading already carries an orange clause, its lede does **not** also
get an orange lead-in. The build enforces this.

**Contrast, stated plainly.** `#F97316` on white is **2.80:1** and fails WCAG AA below 18px. Every small
orange label in this system resolves through `--accent-ink`, so the fix is one value:

```css
--accent-ink:#C2410C;   /* 4.6:1 — every small orange label passes AA */
```

`--accent` stays `#F97316` for graphics and display-size text either way. Crystal chose to match the
marketing site, which has this failure; the swap is one line whenever that changes.

---

## 3. Type

Inter only, weights 300/400/500/600. **Never** SF Pro, Poppins, or Sora. Sora is loaded in the live
marketing site's `<head>` and never applied — do not reintroduce it.

| Role | Size | Notes |
| --- | --- | --- |
| Homepage `h1` | `clamp(42px,6.4vw,92px)` | `line-height:1`, `letter-spacing:-.035em` |
| Inner page `h1` | `clamp(34px,4.6vw,62px)` | `line-height:1.02`, `-.032em`, `max-width:22ch` |
| Section `h2` | `clamp(32px,5.1vw,72px)` | `line-height:1.02`, `-.03em`, `max-width:20ch` |
| Docs `h2` | `clamp(24px,2.4vw,32px)` | `line-height:1.12`, `-.02em` |
| `h3` | `clamp(24px,2.3vw,30px)` | `-.02em` |
| Lede | 16px / 26px | `--muted`, `max-width:62ch` |
| Docs body | 15px / 25px | `--muted`, `max-width:66ch` |
| Micro label | 11px | weight 500, `letter-spacing:.18em`, uppercase |
| Mono | 12.5px | `line-height:1.6`, `-.01em` |

Body default is 16px / 24px.

---

## 4. Shape and rhythm

- **Pill-first.** `999px` on nav, tab rails, chips, badges and CTAs.
- Cards `20px`. Large closing cards `24px`. Inputs `12px`. Method pills `4px`. The partner board `2px`.
- Section padding `--sec` (128px), dropping to 112px under 1180px and 80px under 640px.
- Content capped at `--wrap` (1200px), `padding: 0 32px`, 20px under 640px.
- **Section rhythm, in order:** orange dash + orange uppercase eyebrow → declarative `h2` ending in a full
  stop → grey lede at roughly 65% width → content.
- **Docs column rhythm is not uniform.** A flat gap between every sibling gives a heading the same weight as
  a paragraph break:

```css
.docs-main > * + *{margin-top:22px}
.docs-main > h2 + *,.docs-main > h3 + *{margin-top:16px}  /* tight under a heading */
.docs-main > * + h3{margin-top:54px}                       /* open above one */
.docs-main > * + h2{margin-top:64px}
.docs-main > * + .note{margin-top:34px}
.docs-main > * + .band-foot{margin-top:40px}
```

---

## 5. Copy rules — all three enforced by the build

`build-pages.py` refuses to build if any of these break. Each was proved by deliberately breaking it.

1. **An orange `<em>` clause must follow a comma.** A headline with no comma has no second clause and stays
   entirely ink. `Twenty endpoints, <em>five groups.</em>` is correct; `All F-Link <em>endpoints.</em>` is
   not.
2. **An `<h1>` is a page title and never ends in a full stop.** `G-Link Hotel API`, not
   `G-Link Hotel API.`. Section headings are declarative sentences and **keep** their full stop.
3. **One orange emphasis per block** — a heading with an orange clause does not also get an orange lede
   lead-in.

Plus, not machine-checked but non-negotiable:

- **British English.** standardised, cancellation, organisation, centre, initialisation.
- **Invent nothing.** No product, number, endpoint signature, version or rate limit that is not on the live
  portal. Everything currently in `pages_content.py` was read off
  `open.fusionconnectgroup.com` on 7 September 2026.
- **The orange clause is `display:block`**, so a comma can never orphan a word at the end of the ink line.
- **Inline the real wordmark** once as an SVG `<symbol id="fcg-logo">` and `<use>` it. Never set FCG as
  text, never redraw it. Source: `../brandkit/designlang/fcg-logo.svg` (88×24, `fill="currentColor"`).
- **Icons:** Iconify `solar:*-linear` only, thin outline, single weight. No 3D clay icons, no stock photos
  of people, no aeroplane or suitcase clichés.

---

## 6. Components

### Primary button

```css
.btn{
  display:inline-flex;align-items:center;gap:10px;
  height:52px;padding:0 12px 0 26px;border-radius:999px;
  background:var(--ink);color:#fff;border:1px solid var(--ink);
  font-size:15px;font-weight:500;letter-spacing:-.01em;cursor:pointer;
  transition:background var(--hover) ease,color var(--hover) ease,
             border-color var(--hover) ease,transform var(--press) var(--ease-out);
}
.btn iconify-icon{
  width:30px;height:30px;border-radius:999px;background:rgba(255,255,255,.12);
  padding:7px;font-size:16px;flex:none;transition:transform var(--hover) var(--ease-out);
}
.btn:active{transform:scale(.97)}
@media (hover:hover) and (pointer:fine){
  .btn:hover{background:#000}
  .btn:hover iconify-icon{transform:translateX(3px)}
}
```

`.btn--ghost` is the same pill, transparent, `--line` border, `--card` icon circle. `.btn--sm` is 40px.

### Nav shell

`background:var(--shell)`, `border:1px solid var(--hair)`, `border-radius:999px`, `padding:3px`, links as
34px pills inside that fill white on hover. The active link gets `.on` (white fill, weight 500).

### Tab rail

The nav shell grammar reused for in-page sections. **On mobile it wraps; it does not scroll** — a horizontal
scroller hides options behind an edge with no affordance:

```css
@media (max-width:640px){
  .rail{flex-wrap:wrap;overflow:visible;border-radius:18px;gap:4px;padding:5px}
  .rail a{height:32px;padding:0 13px;font-size:13px}
}
```

### Page band (replaces the hero on an inner page)

Breadcrumb → **eyebrow + status chip on one micro row** → `h1` → lede → CTA row. The chip rides the eyebrow
line; **the CTA row holds only CTAs.**

```html
<section class="band">
  <div class="band-grid" aria-hidden="true"></div>
  <div class="wrap band-in">
    <p class="crumb"><a href="…">Docs centre</a> <i>/</i> <span>This page</span></p>
    <div class="band-top">
      <p class="eyebrow micro">Eyebrow label</p>
      <span class="chip chip--live"><span class="dot" aria-hidden="true"></span>Status</span>
    </div>
    <h1>Page Title</h1>
    <p class="lede"><b>Lead-in phrase.</b> The rest of the lede.</p>
    <div class="band-foot">…CTAs only…</div>
  </div>
</section>
```

### Chips

`.chip` is a 28px pill on `--card` with a `--hair` border. `.chip--plain` is white on `--line`.
`.chip--live` is the tinted status pill: `rgba(249,115,22,.07)` ground, `rgba(249,115,22,.28)` border,
`--accent-ink` label, orange dot.

**A chip must add information the page does not already carry.** Seven were removed from these pages for
restating the heading or lede directly below them. If the `h2` says "Twelve codes, four families", a
`12 codes` chip above it is noise.

### Statistic

```html
<p class="n">4.35<u>M+</u></p>   <!-- numeral ink, unit suffix orange -->
<p class="c">Hotels</p>          <!-- 11px uppercase, .18em, --muted -->
```

Use `×`, not the letter `x`, in `7<u>×24</u>`. A count with no unit stays entirely ink — orange is the
suffix, never a whole word. `8 <u>SDKs</u>` is wrong; `8` with the caption "Published SDK releases" is right.

### Table

Cell classes **must** carry a `t-` prefix: `t-num`, `t-path`, `t-code`, `t-mid`, `t-dim`. A bare
`td class="path"` collides with the homepage's unscoped `.path` closing card and renders every cell as a
rounded panel with 40px padding. Wrap every table in `.tblwrap > .tblscroll` so wide tables scroll inside
their own container and the page body never scrolls sideways.

### The one dark surface

`.term` — an 18px-radius `--dark` block for code, with a bar, a mono body and one orange `.cursor`. This is
the only dark surface in the system. Do not add a second.

---

## 7. Motion

Built on Emil Kowalski's framework. `verify-motion.js` enforces the mechanical parts.

**Durations.** Press feedback 160ms. Hover 160ms — hover is seen dozens of times a day, so it stays quick.
Tooltips 125–200ms. Dropdowns 150–250ms. Drawers 200ms. **UI transitions stay under 300ms.** The scroll
reveal is explanatory rather than UI and is the one exception at 1s.

**Easing.** Entering or exiting → `--ease-out`. Moving or morphing on screen → `--ease-in-out`. Hover and
colour → `ease`. Constant motion → `linear`. **Never `ease-in` on UI** — it delays the exact moment the user
is watching, so it feels slower than an ease-out of the same duration.

**Rules that are checked:**

- **Every pressable thing has `:active {transform: scale(.94–.99)}`.** This is how the interface says it
  heard you. Buttons, nav pills, language buttons, the burger, rail tabs, sidebar links, copy buttons, the
  OAuth button, suggestion buttons.
- **Every hover animation is gated** behind `@media (hover:hover) and (pointer:fine)`. Ungated, it fires on
  tap and sticks.
- **Animate only `transform` and `opacity`.** Never `gap`, `top`, `width`, `height`, `margin`, `padding` or
  `font-size` — those trigger layout and paint. The tertiary link's arrow slides on `transform`; the row's
  `gap` stays fixed. The skip link moves on `translateY`, not `top`.
- **Never `transition: all`.** Name the properties.
- **Never enter from `scale(0)`.** Nothing in the real world appears from nothing. Start at `scale(.95)`
  with `opacity:0`.
- **Stagger 30–80ms** between items. This system uses 60ms, capped at the fourth item.

**Scroll reveal.** `.rv` goes `opacity 0→1` plus `translateY(30px)→0` over 1s `--ease`, driven by an
IntersectionObserver that unobserves after firing. Add `.rv` to a section's cards, not to every element.

**Mobile drawer.** `display:none` blocks a transition, so use `transition-behavior: allow-discrete` with
`@starting-style`:

```css
.mnav{
  display:none;opacity:0;transform:translateY(-6px);
  transition:opacity 200ms var(--ease-out),transform 200ms var(--ease-out),
             display 200ms allow-discrete;
}
.mnav.open{display:block;opacity:1;transform:none}
@starting-style{ .mnav.open{opacity:0;transform:translateY(-6px)} }
```

**Reduced motion means gentler, not off.** Keep opacity and colour, which carry meaning; drop movement.
Do not blanket-kill every transition with `*{transition-duration:.01ms!important}` — that also kills the
colour changes that help comprehension.

```css
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  html.js .rv{opacity:1!important;transform:none!important;transition:none}
  .cursor{animation:none}
  .btn:active,.shell a:active,.lang button:active{transform:none}
  .btn iconify-icon,.tlink iconify-icon{transition:none;transform:none!important}
}
```

---

## 8. Layout traps found the hard way

Each of these shipped as a real bug in this build. Check for them in any new page.

**A nowrap flex row inside a column flex container will be clipped, not scrolled.** A flex item's
`min-width` defaults to `auto`, so it keeps its min-content width and `max-width:100%` never bites. Because
`body` has `overflow-x:hidden`, no scrollbar appears — the content is silently cut off. Every child of a
column flex container needs clamping:

```css
.band-in > *{max-width:100%;min-width:0}
.band-foot{width:100%;min-width:0}
```

**A horizontal-scroll check proves nothing** while `body{overflow-x:hidden}` is set. Compare each child's
width against its `.wrap` content box instead. `verify-pages.js` does this.

**Class collisions across two stylesheets are real.** Both CSS blocks are in scope on every page. Before
naming a class, check it is not already styled unscoped elsewhere. `.path` was the only genuine collision;
prefer a prefix (`t-path`) over a bare noun.

**Scope every descendant rule to the component that owns it.** `.mnav a` also hit the drawer's CTA pills and
flattened them with `display:block` plus vertical padding — it needed to be `.mnav ul a`. `code.inl` scoped
to `.docs-main` meant every instance outside that column fell back to the browser's default monospace.

**`min-height` for row alignment lands on the wrong element easily.** `.card-k` is also a `<p>`, so
`.card-h p{min-height}` inflated the eyebrow and never touched the description. Use
`.card-h > p:not(.card-k)`.

**Buttons on mobile size to content with the label flush left.** A full-bleed pill reads as a banner on a
phone and centres its label away from the text column. Form submits are the exception and stay full width.

**A tall column beside a short one pushes the short one below the fold** when the container centres its
items. The auth aside is `align-items:flex-start` with a sticky inner column so it clears the fold from
720px viewport height upward.

---

## 9. Accessibility floor

- Real heading order: exactly one `h1` per page, no skipped levels. **Navigation labels are not headings** —
  the docs sidebar groups, the footer columns and the suggestion panel use `<p>` with `aria-labelledby` on a
  `<nav>` or `role="group"`, which keeps them out of the heading outline.
- `:focus-visible{outline:2px solid var(--accent);outline-offset:3px}` on everything focusable.
- A skip link to `#main` as the first element in `<body>`.
- No `alert()`. No dead `href="#"` that jumps the page — use `href="#section-id"` or
  `<button type="button">`.
- Required-field markers stay ink, not orange: at 11px, orange is the one place the contrast failure would
  hide real information.
- Wide content (tables, code blocks, diagrams) scrolls inside its own `overflow-x:auto` container. The page
  body never scrolls sideways.

---

## 10. Verify by observation

Reading the code does not count. Both scripts attach to the always-on Chrome for Testing on `:9222` — they
never launch a browser.

```bash
curl -s localhost:9222/json/version    # must return JSON; if not:
# launchctl load ~/Library/LaunchAgents/com.crystal.chrome-debug.plist

cd open-portal-redesign
NODE_PATH=$(npm root -g) node verify-pages.js     # layout, brand, a11y — 12 pages x 1280 and 375
NODE_PATH=$(npm root -g) node verify-motion.js    # the motion rules in §7
```

`verify-pages.js` asserts: no console or page errors, no horizontal scroll, nothing clipped by its `.wrap`,
the accent never filling anything at button scale, Inter throughout, one `h1` with no heading skips, no dead
`href="#"`, no table cell inheriting panel styling, card meta rows aligned within a visual row, and
`--accent-ink` holding an approved value. It also counts small orange labels, so a jump in that count is
visible in review.

**Force the reveal animations to their end state before capturing**, or a full-page screenshot comes out
blank:

```js
document.querySelectorAll(".rv").forEach(e => {
  e.classList.add("in"); e.style.transition = "none";
  e.style.opacity = 1; e.style.transform = "none";
});
```

Run about 12 pages per invocation and do not run two puppeteer processes at once — they contend for the
single shared browser and one will time out.

---

## 11. Applying this to app UI rather than marketing pages

The tokens, accent law, type scale, shape language, motion rules and accessibility floor all carry over
unchanged. What changes:

- **Density goes up.** Drop `--sec` from 128px to about 48–64px between panels. Keep the 22/16/54px docs
  rhythm from §4 for anything text-heavy.
- **The nav shell becomes the app's primary navigation**, either a top rail or a left sidebar reusing
  `.docs-side` (252px, sticky, `--accent-ink` group labels, pill links with an `.on` state).
- **Tables and forms are the workhorses.** `.tblwrap`, `table.tbl` with `t-` prefixed cells, `.fld` inputs
  and `.plist` parameter rows already cover most of a console. Keep the `t-` prefix discipline.
- **Motion matters more, not less.** An app screen is seen hundreds of times a day, so §7's frequency rule
  bites harder: **never animate a keyboard-initiated action**, and cut or drastically reduce anything a user
  triggers tens of times a day. Press feedback stays — it is the one animation that earns its place at any
  frequency.
- **Skip the scroll reveal.** `.rv` is a marketing device. On a screen someone opens forty times a day it
  reads as lag.
- **Empty, loading and error states need the same care as the happy path.** Use `.note` for inline guidance,
  `.chip--live` for status, and the `--card` fill plus a `--line` hairline for an empty-state panel. Never
  reach for orange to signal an error — orange is the brand accent here, not a semantic colour. If the app
  needs true semantic status colours, that is a decision to take to Crystal, not to invent.
