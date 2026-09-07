# FCG Open Website — developer portal redesign

Realigns FCG's developer portal, `open.fusionconnectgroup.com`, to the FCG marketing brand at
`fusionconnectgroup.com`, so a visitor crossing between the two feels no seam.

Separate from `cwong-acmy/fcg-website`, which holds the marketing site.

## What is here

| Path | What |
| --- | --- |
| [open-portal-redesign/variant-b-impeccable/](open-portal-redesign/variant-b-impeccable) | The build. 12 pages × 3 languages: English at the root, Simplified in `zh-CN/`, Traditional in `zh-TW/`. |
| [open-portal-redesign/DESIGN-SYSTEM.md](open-portal-redesign/DESIGN-SYSTEM.md) | How to build a new page or app screen in this language. Written to be followed cold. |
| [open-portal-redesign/BRIEF.md](open-portal-redesign/BRIEF.md) | The original brief. |
| [open-portal-redesign/variant-a-huashu/](open-portal-redesign/variant-a-huashu) | The direction that was not chosen, kept for the record. |
| [brandkit/](brandkit) | The extracted FCG brand kit. The portal build's authority for tokens and the wordmark. |
| [STATE-LOG.md](STATE-LOG.md) | Project memory: what changed, decisions, blockers, next actions. Read this first. |

Pages: `index`, `app-management`, `api-docs-hotel`, `api-docs-hotel-process`, `api-docs-hotel-apis`,
`api-docs-flink`, `api-docs-errors`, `sdk`, `skills`, `ai-assistant`, `login`, `register`.

## Build

No build step to view — every page is a self-contained HTML file that opens from `file://`. To
regenerate after editing content or tokens:

```bash
cd open-portal-redesign/variant-b-impeccable
python3 build-pages.py
```

`build-pages.py` lifts the `<head>`, the token/CSS block and the behaviour script **verbatim** out of
`index.html` and generates the nav and footer from one list, writing them back into `index.html` too — so
a token cannot drift between pages. Page content is in `pages_content.py`. The Chinese editions are the
same document with its text nodes swapped (`i18n.py` plus `i18n_zh_cn.py` / `i18n_zh_tw.py`), so markup
and CSS are byte-identical across locales by construction.

The build refuses to run if a copy rule breaks or if any string has no translation entry.

## Verify

Both scripts attach to an already-running Chrome for Testing on `:9222`. They never launch a browser.

```bash
curl -s localhost:9222/json/version    # must return JSON

cd open-portal-redesign
NODE_PATH=$(npm root -g) node verify-pages.js            # English
NODE_PATH=$(npm root -g) node verify-pages.js zh-CN      # Simplified
NODE_PATH=$(npm root -g) node verify-pages.js zh-TW      # Traditional
NODE_PATH=$(npm root -g) node verify-motion.js
```

`verify-pages.js` loads every page at 1280, 768 and 375 and asserts: no console or page errors, no
horizontal scroll, nothing clipped by its `.wrap`, the accent never filling anything at button scale,
Inter throughout, one `h1` per page with no heading skips, no dead `href="#"`, no table cell inheriting
panel styling, and card meta rows aligned within a visual row. It also writes screenshots to
`open-portal-redesign/shots/b-pages/`, which is gitignored because it regenerates.

`verify-motion.js` asserts the motion rules: no `transition: all`, no `scale(0)` entry, no `ease-in` on
UI, no UI transition over 300ms, no layout property animated, `:active` on every pressable, and every
hover gated behind `(hover:hover) and (pointer:fine)`.

## Status

Not deployed, and no deployment target agreed. The live marketing site is served from the OneDrive
"07 Website" folder on nginx — not from a repository and not from Vercel — so nothing here changes
anything live.

One open decision is recorded in `STATE-LOG.md`: `#F97316` on white is 2.80:1 and fails WCAG AA below
18px. The marketing site does this and the build matches it, but every small orange label resolves
through the `--accent-ink` token, so switching that one value to `#C2410C` (4.6:1) makes all of them pass.

## Content provenance

Every endpoint path, method, SDK version, error code, rate limit and install command was read off the
live portal on 7 September 2026. Nothing is invented. Copy is rewritten into FCG's declarative voice in
British English; the substance is unchanged.
