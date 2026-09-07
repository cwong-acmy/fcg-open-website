# FCG Brand Kit

**Source:** https://fusionconnectgroup.com/ (live, nginx, uploaded 20 July 2026)
**Extracted:** 7 September 2026
**Method:** `designlang` v12.15.0 full extraction, then every token cross-checked against the live page's own inline `<style>` block. Where the two disagree, the live source wins — designlang's heuristics rank CSS frequency, not brand intent.

---

## 1. The one-line brand idea

> **One connection.**

FCG is the supply layer underneath other people's travel products. The brand has to read as *infrastructure*, not as travel. Nothing about the visual system says holiday; everything about it says routing, inventory, uptime.

Live headline, verbatim: *"Connect to the supply infrastructure behind travel."*

---

## 2. Colour

The whole system is white, one ink, one accent. Thirteen unique colours on the entire homepage.

| Role | Light (shipped default) | Dark | Notes |
|---|---|---|---|
| Background | `#FFFFFF` | `#080805` | dark is warm near-black, not `#000` |
| Ink / foreground | `#0F1114` | `#FFFFFF` | never pure black on light |
| Accent | `#F97316` | `#F97316` | identical in both themes |
| Card / raised | `#F3F4F6` | `#121212` | |
| Border hairline | `#D1D5DB` | `#2A2A2A` | |
| Muted text | `#6B7280` | `#888888` | all lede and caption copy |
| Secondary ink | `#111827` | — | dark chips, pill CTAs |
| Footer ground | `#f7f8fa` | — | hairline `rgba(15,17,20,.1)` |

**Accent discipline — this is the whole trick.** `#F97316` appears 49 times against ink's 188. It is never a fill for anything large. It only ever shows up as:

- a 6px status dot before a micro-label
- a short 12px dash before a section eyebrow
- the suffix of a statistic (`4.35` in ink, **`M+`** in orange)
- thin great-circle arcs over the black globe
- the focus ring / active state
- a soft `0 0 8px rgba(249,115,22,.4)` glow on live indicators

Never an orange button. Never an orange panel. Never an orange gradient.

---

## 3. Type

**Inter alone.** Weights 300 / 400 / 500 / 600. Sora is loaded in the live `<head>` and then never applied — do not reintroduce it.

| Level | Size | Weight | Line height | Tracking |
|---|---|---|---|---|
| h1 | 96px | 500 | 96px (1.0) | ~ -0.03em |
| h2 | 76px | 500 | 76px (1.0) | ~ -0.03em |
| h3 | 48px | 500 | 48px | ~ -0.02em |
| h4 | 30px | 500 | 36px | normal |
| Body / lede | 16px | 400 | 24px | normal, `--color-muted` |
| Micro-label | 11–12px | 500 | — | **uppercase, 0.18em** |

Display headlines are set at line-height 1.0 with tight negative tracking, so they lock into a dense typographic block. That density against the surrounding white is the signature.

Voice: neutral, third-person, Title Case, tight. Headlines are declarative sentences ending in a full stop: *"Deep, not just wide."* · *"The supply advantage behind every connection."* · *"One inventory underneath. Three product families."*

---

## 4. Shape and surface

- **Radii:** pill-first. `2 · 6 · 15 · 24 · 999`. Nav, chips, badges and CTAs are all `999px`. Cards are 15–24px.
- **Material:** flat. No drop shadows on light. Depth comes from the `#F3F4F6` card fill and the `#D1D5DB` hairline, nothing else.
- **Nav shell:** `background rgba(15,17,20,.04)` · `border 1px rgba(15,17,20,.08)` · `border-radius 999px` · `padding 3px`. The links sit inside as pills that fill on hover.
- **Glass** (dark contexts only): `rgba(255,255,255,.05)` + `backdrop-filter: blur(12px)` + `1px rgba(255,255,255,.1)`.
- **Grids as texture:** 40px line grid at 5% opacity, masked to transparent by 100% height; or a 12px dot grid. Both drift on a 20s linear loop.

---

## 5. Layout rhythm

Sections are enormous. Vertical padding runs 128–170px and the section scale is `40 · 48 · 64 · 80 · 96 · 128 · 160`. Content is centred and capped near 1100–1200px, with lede copy at roughly two-thirds of the headline width.

The repeating section pattern:

```
  — SECTION EYEBROW            (orange dash + orange uppercase 0.18em)
  A declarative headline.      (h2, 76px/500, centred, ends in a full stop)
  One or two lines of grey lede at ~65% width.
  [ content ]
```

**Logo wall:** a bordered checkerboard grid, alternating `#FFFFFF` and `#F3F4F6` cells, with small `+` crosshair marks drawn at the interior grid intersections. Partner logos sit in greyscale.

**Statistics:** oversized ink numeral, orange unit suffix, tiny grey caption underneath.

**CTA:** a black `999px` pill, white label, right-arrow glyph. The only button style that matters.

---

## 6. Motion

| Behaviour | Spec |
|---|---|
| Section reveal | `opacity 0→1`, `translateY(30px)→0`, `1s cubic-bezier(.16,1,.3,1)`, GSAP ScrollTrigger |
| Marquee | `20s linear infinite` |
| Grid drift | `20s linear infinite` |
| Hover | `240ms ease` on colour + background |
| Live pulse | slow `ping` on the orange status dot |

Restrained and slow. Nothing bounces.

---

## 7. Iconography and illustration

- **Icons:** Iconify, `solar:*-linear` set only — thin outline, 19px in nav, single-weight. No filled icons, no duotone.
- **Illustration:** flat vector. The homepage hero is one large solid-black organic blob standing in for the globe, crossed by thin orange arcs, with small dark rounded city chips (`SINGAPORE`, `HKG → CDG`) pinned at the arc endpoints.
- **Never:** 3D clay/plasticine icons, isometric scenes, stock photography of people, aeroplane and suitcase clichés, purple or blue accents, neon, gradient glow.

---

## 8. Logo

The wordmark is a custom geometric construction of the letters F, C, G with cut corners and a shared stroke weight — an 88×24 SVG that inherits `currentColor`, so it flips between themes for free. Extracted verbatim to [fcg-logo.svg](brandkit/designlang/fcg-logo.svg). Rendered at 28px height in the header.

Use the real SVG. Do not set "FCG" as live text in a font, and do not redraw it.

---

## 9. Known defects on the source

Carried over from the live site, worth not inheriting:

- 3 colour pairs fail WCAG AA contrast
- 216 `!important` rules
- ~90% of the CSS ships unused (Tailwind CDN, unpurged)
- 487 duplicate declarations
- React 18 + Babel `standalone` compiling JSX **in the browser** at runtime

---

## 10. Files in this kit

| Path | What it is |
|---|---|
| [FCG-BRAND-KIT.md](brandkit/FCG-BRAND-KIT.md) | this document |
| [fcg-brandkit-board.html](brandkit/fcg-brandkit-board.html) | the 3×3 identity board, built in code from the real tokens |
| [tokens/fcg-tokens.css](brandkit/tokens/fcg-tokens.css) | copy-paste custom properties + measured scales |
| [tokens/fcg-live-extracted.css](brandkit/tokens/fcg-live-extracted.css) | the live site's four `<style>` blocks, verbatim |
| [designlang/](brandkit/designlang) | full `designlang` extraction — 47 files |
| [designlang/fcg-DESIGN.md](brandkit/designlang/fcg-DESIGN.md) | agent-native design brief |
| [designlang/fcg-logo.svg](brandkit/designlang/fcg-logo.svg) | the real FCG wordmark |
| [designlang/screenshots/](brandkit/designlang/screenshots) | hero, nav, cards, buttons, 4 responsive breakpoints × light/dark |
| [designlang/fcg-prompts/](brandkit/designlang/fcg-prompts) | v0 / Cursor / Lovable / Claude prompt packs |
| [boards/](brandkit/boards) | reserved for raster brand boards — **empty, see below** |

### Raster boards: BLOCKED

The `brandkit` skill at `/Users/crystalwong/Desktop/Claude/.claude/skills/brandkit` is an image-generation skill. Its two board prompts were written and are ready, but every available image model refused on quota:

- Both Google AI Studio keys in 1Password return `429 … free_tier_requests, limit: 0` for `gemini-3-pro-image`, `gemini-3.1-flash-image` and `gemini-2.5-flash-image` — billing is not enabled on either project.
- Higgsfield returns `Not authenticated` and needs an interactive `hf auth login`.

`fcg-brandkit-board.html` is the substitute, and is arguably the better artifact: it uses the real wordmark and the real hex values rather than a model's approximation of them, and it is editable. Say the word once a billed key or a Higgsfield login is available and the raster boards can be generated from the stored prompts.
