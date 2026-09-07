# Brief — realign the FCG Developer Platform homepage to the FCG marketing brand

## The job

`https://open.fusionconnectgroup.com/home` is FCG's developer portal. It works, but it looks like a
different company from `https://fusionconnectgroup.com/`. Redesign **the homepage only**, so that a
visitor moving from the marketing site to the portal feels no seam.

Deliverable: **one self-contained `index.html`** — inline CSS, no build step, no local asset files.
It must open correctly from `file://`. Google Fonts and CDN scripts are fine.

## Target design language — FCG marketing site

Read [../brandkit/FCG-BRAND-KIT.md](../brandkit/FCG-BRAND-KIT.md) in full before writing anything.
It is the spec. The short version:

- **Palette.** White `#FFFFFF` ground, ink `#0F1114`, muted `#6B7280`, card `#F3F4F6`, hairline
  `#D1D5DB`, secondary ink `#111827`, footer ground `#f7f8fa`. One accent: `#F97316`.
- **Accent discipline is the single most important rule.** Orange only as: a 6px status dot, a 12px
  dash before a section eyebrow, the *unit suffix* of a statistic (`4.35` ink + `M+` orange), thin
  arcs, focus rings. **Never an orange button, panel, or gradient.** The current portal breaks this
  constantly — orange buttons and orange-tinted cards everywhere. Fix it.
- **Type: Inter only**, weights 300/400/500/600. h1 96px/500 at line-height 1.0 with about -0.03em
  tracking; h2 76px; h3 48px. Micro-labels 11–12px uppercase at 0.18em tracking. Body 16px/24px in
  muted grey. Do **not** use SF Pro, Poppins or Sora.
- **Shape.** Pill-first: `999px` on nav, chips, badges and CTAs. Cards 15–24px. Flat — no drop
  shadows on light; depth is the `#F3F4F6` fill plus the `#D1D5DB` hairline.
- **Nav shell.** `background rgba(15,17,20,.04)`, `border 1px rgba(15,17,20,.08)`,
  `border-radius 999px`, `padding 3px`, links as pills inside it that fill on hover.
- **CTA.** Black `999px` pill, white label, right-arrow glyph. That is the button.
- **Section rhythm.** 128–170px vertical padding. Content capped ~1100–1200px, centred. Each section:
  orange dash + orange uppercase eyebrow → declarative h2 ending in a full stop → grey lede at ~65%
  width → content.
- **Icons.** Iconify `solar:*-linear` only, thin outline, single weight.
  `<script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>`
- **Motion.** Reveal on scroll: `opacity 0→1` + `translateY(30px)→0`, `1s cubic-bezier(.16,1,.3,1)`.
  Hover 240ms ease. Slow and restrained; nothing bounces.
- **Never:** 3D clay/plasticine icons (the current portal is full of them), purple or blue accents,
  neon, gradient glow, stock photos of people, aeroplane/suitcase clichés.

The real wordmark is at [../brandkit/designlang/fcg-logo.svg](../brandkit/designlang/fcg-logo.svg) —
88×24, `fill="currentColor"`. **Inline that SVG verbatim.** Do not redraw it or set FCG as text.
Render at 28px height. The portal is a sub-brand: put the wordmark next to a lighter-weight
"Developer Platform" or "Open Platform" lockup.

Reference screenshots of the marketing site: [../brandkit/designlang/screenshots/](../brandkit/designlang/screenshots)
(`hero.png` and `nav.png` are the two to study). Current portal, for reference only —
do not preserve its look: [reference/designlang-current/](reference/designlang-current)

## Content to carry over

Keep the substance. Rewrite headlines into FCG's declarative voice (Title Case, tight, ending in a
full stop, third person). British English. Do not invent products, numbers or claims.

**Nav:** Home · App Management · API Docs · SDK · Skills · AI Assistant · language switcher · Login · Register

**Hero.** Eyebrow "Supports both SDK and API integration". Title "FCG Developer Platform". Lede: a
travel-focused open platform for distributors such as OTAs and travel management companies;
standardised APIs and flexible SDKs aggregate and distribute hotel, flight and other core travel
resources, plus TMC API capabilities so partners can launch branded travel platforms faster.
CTAs "Start Integration" (primary) and "Book a Demo" (secondary).

**Core Products** — three: built around three core products covering the key travel workflows end to end.
- *G-Link Hotel API* — major global hotel inventory, full workflow from real-time search and test booking to reservation and cancellation, industry-grade data accuracy. Chips: Search APIs · Booking management · Rate calendar · Room details.
- *F-Link Flight API* — direct airline seat inventory, domestic and international carriers, BSP support, covering search, pricing, ticketing, refunds and changes. Chips: Flight search · Live fares · Order management · Refund rules.
- *TMC API* — mature API-based travel management, branded enterprise travel service quickly, deep customisation, no need to build from scratch. Chips: Enterprise control · Expense rules · Billing reports · Approval flow.

**Skills Packages** (badge: NEW) — integration skill packages for AI coding assistants; import into
Claude, ChatGPT or Copilot for more accurate auth code, API debugging and issue diagnosis. Points:
full G-Link & F-Link coverage · Auth / Query / Booking / Payment · prompt templates included ·
continuously updated. CTA "Browse Skills".

**Product Use Cases** — three groups of three:
- G-Link / Hotel API Distribution: OTA aggregation · Enterprise travel procurement · Destination management
- F-Link / Flight API Distribution: Agency distribution · Travel policy control · Fare aggregation and comparison
- TMC API / Travel Management API: Branded deployment · Enterprise policy controls · Unified billing and reporting

**Flexible Integration Options** — MCP Smart Integration (Model Context Protocol, so AI models can
call travel capabilities directly; for LLM apps and assistants) · Fast SDK Integration (Go, Java,
Python today; Node.js in progress; auth, retry and serialisation built in) · API (standard APIs
callable from any language or framework).

**Customer Types** — Distributors / OTAs (recommended: API / SDK) · Travel Management Companies
(most popular; recommended: full product suite + API integration) · Large Enterprises (recommended:
fast TMC API deployment).

**Statistics** — 50+ enterprise clients · 10M+ daily requests · 99.9% service uptime · 7x24 technical
support. Set these in the marketing site's pattern: ink numeral, **orange unit suffix**, tiny grey caption.

**Partner network** — "The supply and partner network behind FCG." Trusted by 50+ enterprise clients,
central SOEs and Fortune Global 500, including State Grid, China Mobile and Ping An. Logos, greyscale,
in the marketing site's bordered checkerboard grid with `+` crosshairs at the interior intersections:
PST · Connexus Travel · Sabre · Hilton · Amadeus · 华住 · IHG · Marriott. Render each as a greyscale
text lockup — do not hotlink logo images.

**Closing** — two paths. *Free Access*: register for a sandbox and test the full API set at no upfront
cost, production billed by volume; full sandbox experience · complete API docs and SDKs · community
support and docs centre · usage-based billing with no minimum spend; CTA "Register for free".
*Business Consultation / Demo*: talk to the business team about custom solutions, dedicated pricing
and TMC API deployment; dedicated business manager · custom integration plan · TMC API deployment
demo · dedicated SLA coverage; CTA "Book a 30-minute demo".

**Footer** — `#f7f8fa` ground, `rgba(15,17,20,.1)` hairline, muted `#6B7280` links.

## Constraints

- Desktop-first at 1280px, but responsive down to 375px. No horizontal scroll at any width.
- Light theme only for this round. Do not build a theme toggle.
- Accessible: real heading order, focus-visible rings in `#F97316`, AA contrast. Do not put ink
  text on orange or orange text on white below 18px.
- No `alert()`, no dead `href="#"` that jumps the page — use `href="#section-id"` or `type="button"`.
- One file. Under about 120KB.
