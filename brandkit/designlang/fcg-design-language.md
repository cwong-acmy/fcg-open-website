# Design Language: FCG Group - Travel Infrastructure

> Extracted from `https://fusionconnectgroup.com/` on September 7, 2026
> 1196 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#f97316` | rgb(249, 115, 22) | hsl(25, 95%, 53%) | 49 |
| Secondary | `#111827` | rgb(17, 24, 39) | hsl(221, 39%, 11%) | 188 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 759 |
| `#0f1114` | hsl(216, 14%, 7%) | 753 |
| `#6b7280` | hsl(220, 9%, 46%) | 257 |
| `#4b5563` | hsl(215, 14%, 34%) | 210 |
| `#000000` | hsl(0, 0%, 0%) | 128 |
| `#d1d5db` | hsl(216, 12%, 84%) | 121 |
| `#ffffff` | hsl(0, 0%, 100%) | 83 |
| `#f3f4f6` | hsl(220, 14%, 96%) | 26 |
| `#9ca3af` | hsl(218, 11%, 65%) | 14 |
| `#374151` | hsl(217, 19%, 27%) | 1 |
| `#27272a` | hsl(240, 4%, 16%) | 1 |

### Background Colors

Used on large-area elements: `#ffffff`, `#f3f4f6`, `#000000`, `#f7f8fa`

### Text Colors

Text color palette: `#000000`, `#0f1114`, `#111827`, `#f97316`, `#6b7280`, `#ffffff`, `#374151`, `#18181b`, `#e4e4e7`, `#4b5563`

### Gradients

```css
background-image: linear-gradient(to top, rgb(255, 255, 255) 30%, rgba(0, 0, 0, 0) 70%);
```

```css
background-image: linear-gradient(to right, rgb(249, 250, 251), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(to left, rgb(249, 250, 251), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(to right, rgba(0, 0, 0, 0.08) 1px, rgba(0, 0, 0, 0) 1px), linear-gradient(rgba(0, 0, 0, 0.08) 1px, rgba(0, 0, 0, 0) 1px);
```

```css
background-image: radial-gradient(circle at 100% 0%, rgba(0, 0, 0, 0.03), rgba(0, 0, 0, 0) 50%);
```

```css
background-image: linear-gradient(to right, rgba(0, 0, 0, 0.05) 1px, rgba(0, 0, 0, 0) 1px), linear-gradient(rgba(0, 0, 0, 0.05) 1px, rgba(0, 0, 0, 0) 1px);
```

```css
background-image: linear-gradient(to left, rgba(0, 0, 0, 0.02), rgba(0, 0, 0, 0));
```

```css
background-image: radial-gradient(circle, rgba(0, 0, 0, 0.03), rgba(0, 0, 0, 0) 42%);
```

```css
background-image: linear-gradient(rgba(255, 255, 255, 0.03), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(to right top, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.05));
```

```css
background-image: linear-gradient(rgba(82, 82, 82, 0.6), rgba(38, 38, 38, 0.3), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(rgb(64, 64, 64), rgb(38, 38, 38));
```

```css
background-image: linear-gradient(to right bottom, rgba(64, 64, 64, 0.5), rgba(38, 38, 38, 0.2), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(to left bottom, rgba(64, 64, 64, 0.5), rgba(38, 38, 38, 0.2), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(rgb(38, 38, 38), rgba(38, 38, 38, 0.5));
```

```css
background-image: linear-gradient(rgba(64, 64, 64, 0.3), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(to top, rgba(255, 255, 255, 0.8), rgba(0, 0, 0, 0));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border, background, text | 759 |
| `#0f1114` | text, border, background | 753 |
| `#6b7280` | text, border, background | 257 |
| `#4b5563` | text, border | 210 |
| `#111827` | text, background, border | 188 |
| `#000000` | text, border, background | 128 |
| `#d1d5db` | border, background, text | 121 |
| `#ffffff` | background, text, border | 83 |
| `#f97316` | text, border, background | 49 |
| `#f3f4f6` | background | 26 |
| `#9ca3af` | background, text | 14 |
| `#374151` | text | 1 |
| `#27272a` | background | 1 |

## Typography

### Font Families

- **Inter** — used for all (1196 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 96px | 6rem | 500 | 96px | -4.8px | h1 |
| 76px | 4.75rem | 500 | 76px | -1.9px | h1, span |
| 60px | 3.75rem | 300 | 60px | -3px | span |
| 48px | 3rem | 500 | 48px | -1.2px | h2, span |
| 30px | 1.875rem | 500 | 36px | -0.75px | h2, strong, h3, div |
| 24px | 1.5rem | 400 | 32px | normal | iconify-icon, style, svg, g |
| 20px | 1.25rem | 500 | 28px | -0.5px | h3, iconify-icon, style, svg |
| 18px | 1.125rem | 300 | 28px | normal | p, span, div, h3 |
| 16px | 1rem | 400 | 24px | normal | html, head, script, meta |
| 14px | 0.875rem | 500 | 20px | -0.35px | button, iconify-icon, style, svg |
| 12px | 0.75rem | 400 | 16px | -0.6px | div, span, iconify-icon, style |
| 10.4px | 0.65rem | 400 | 15.6px | normal | footer, style, div, svg |
| 10px | 0.625rem | 400 | 14px | 1.8px | h3, span, div |
| 9px | 0.5625rem | 400 | 13.5px | normal | div, span |
| 8px | 0.5rem | 400 | 12px | 0.8px | div |

### Heading Scale

```css
h1 { font-size: 96px; font-weight: 500; line-height: 96px; }
h1 { font-size: 76px; font-weight: 500; line-height: 76px; }
h2 { font-size: 48px; font-weight: 500; line-height: 48px; }
h2 { font-size: 30px; font-weight: 500; line-height: 36px; }
h3 { font-size: 20px; font-weight: 500; line-height: 28px; }
h3 { font-size: 18px; font-weight: 300; line-height: 28px; }
h3 { font-size: 16px; font-weight: 400; line-height: 24px; }
h3 { font-size: 14px; font-weight: 500; line-height: 20px; }
h2 { font-size: 12px; font-weight: 400; line-height: 16px; }
h3 { font-size: 10px; font-weight: 400; line-height: 14px; }
```

### Body Text

```css
body { font-size: 12px; font-weight: 400; line-height: 16px; }
```

### Font Weights in Use

`400` (954x), `300` (159x), `500` (69x), `600` (13x), `700` (1x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-64 | 64px | 4rem |
| spacing-80 | 80px | 5rem |
| spacing-96 | 96px | 6rem |
| spacing-128 | 128px | 8rem |
| spacing-141 | 141px | 8.8125rem |
| spacing-160 | 160px | 10rem |
| spacing-170 | 170px | 10.625rem |
| spacing-213 | 213px | 13.3125rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 9 |
| md | 6px | 8 |
| lg | 11px | 3 |
| lg | 15px | 3 |
| xl | 24px | 10 |
| full | 32px | 14 |
| full | 50px | 2 |
| full | 999px | 5 |
| full | 9999px | 50 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(249, 115, 22, 0.4) 0px 0px 8px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(249, 115, 22, 0.5) 0px 0px 8px 0px;
```

**sm (inset)** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.9) 0px 0px 60px 0px, rgba(0, 0, 0, 0.2) 0px 0px 20px 0px inset;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.8) 0px 0px 10px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(249, 115, 22, 0.5) 0px 0px 10px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.4) 0px 0px 8px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.6) 0px 0px 8px 0px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.8) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.12) 0px 20px 40px -15px;
```

**sm (inset)** — blur: 4px
```css
box-shadow: rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset;
```

**md** — blur: 10px
```css
box-shadow: rgba(0, 0, 0, 0.15) 0px 0px 10px 0px;
```

**lg** — blur: 20px
```css
box-shadow: rgba(0, 0, 0, 0.15) 0px 0px 20px 0px;
```

**lg** — blur: 32px
```css
box-shadow: rgba(0, 0, 0, 0.12) 0px 0px 32px 0px;
```

**xl** — blur: 30px
```css
box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 30px 0px;
```

**xl** — blur: 25px
```css
box-shadow: rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.08) 0px 8px 10px -6px;
```

**xl (inset)** — blur: 47.5009px
```css
box-shadow: rgba(255, 255, 255, 0.25) 0px 0px 47.5009px 0px, rgba(255, 255, 255, 0.14) 0px 0px 23.7505px 0px inset;
```

**xl** — blur: 45px
```css
box-shadow: rgba(15, 17, 20, 0.08) 0px 18px 45px 0px;
```

**xl** — blur: 50px
```css
box-shadow: rgba(0, 0, 0, 0.15) 0px 25px 50px -12px;
```

**xl** — blur: 70px
```css
box-shadow: rgba(15, 17, 20, 0.18) 0px 28px 70px 0px;
```

## CSS Custom Properties

### Colors

```css
--color-bg: #080805;
--color-fg: #ffffff;
--color-accent: #F97316;
--color-card: #121212;
--color-border: #2A2A2A;
--color-muted: #888888;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--tw-ring-inset: ;
--tw-ring-offset-width: 0px;
--tw-border-spacing-x: 0;
--tw-shadow-colored: 0 0 #0000;
--tw-border-spacing-y: 0;
--tw-ring-color: rgb(59 130 246 / 0.5);
--tw-ring-offset-color: #fff;
```

### Spacing

```css
--tw-contain-size: ;
--tw-numeric-spacing: ;
```

### Shadows

```css
--tw-shadow: 0 0 #0000;
--tw-drop-shadow: ;
```

### Other

```css
--tw-contrast: ;
--tw-backdrop-sepia: ;
--tw-sepia: ;
--tw-skew-x: 0;
--tw-ordinal: ;
--tw-backdrop-saturate: ;
--tw-backdrop-blur: ;
--tw-contain-style: ;
--tw-translate-x: 0;
--tw-gradient-via-position: ;
--tw-backdrop-invert: ;
--tw-saturate: ;
--tw-scroll-snap-strictness: proximity;
--tw-grayscale: ;
--tw-scale-x: 1;
--tw-backdrop-hue-rotate: ;
--tw-gradient-to-position: ;
--tw-brightness: ;
--tw-numeric-fraction: ;
--tw-backdrop-grayscale: ;
--tw-hue-rotate: ;
--tw-scale-y: 1;
--tw-pan-y: ;
--tw-backdrop-contrast: ;
--tw-skew-y: 0;
--tw-backdrop-brightness: ;
--tw-slashed-zero: ;
--tw-blur: ;
--tw-invert: ;
--tw-pan-x: ;
--tw-translate-y: 0;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--tw-numeric-figure: ;
--tw-rotate: 0;
--tw-pinch-zoom: ;
--tw-contain-paint: ;
--tw-contain-layout: ;
```

### Semantic

```css
success: [object Object];
warning: [object Object];
error: [object Object];
info: [object Object];
```

## Breakpoints

| Name | Value | Type |
|------|-------|------|
| sm | 639px | max-width |
| sm | 640px | min-width |
| md | 768px | min-width |
| 900px | 900px | max-width |
| lg | 1023px | max-width |
| lg | 1024px | min-width |
| xl | 1280px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.3s`, `0.15s`, `1.2s`, `0.5s`, `0.7s`, `0.24s`, `0.18s`, `0.22s`, `1s`, `0.1s`, `0.075s`, `0.2s`

### Common Transitions

```css
transition: all;
transition: background-color 0.3s, color 0.3s;
transition: 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 1.2s;
transition: opacity 0.5s, filter 0.5s;
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: transform 0.7s cubic-bezier(0, 0, 0.2, 1);
transition: opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: color 0.24s, background-color 0.24s;
```

### Keyframe Animations

**gridMove**
```css
@keyframes gridMove {
  0% { transform: translateY(0px); }
  100% { transform: translateY(40px); }
}
```

**float**
```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}
```

**marquee**
```css
@keyframes marquee {
  0% { transform: translateX(0px); }
  100% { transform: translateX(-33.333%); }
}
```

**shimmer**
```css
@keyframes shimmer {
  100% { background-position: 200% center; }
}
```

**barPulse1**
```css
@keyframes barPulse1 {
  0% { height: 30%; }
  100% { height: 70%; }
}
```

**barPulse2**
```css
@keyframes barPulse2 {
  0% { height: 60%; }
  100% { height: 95%; }
}
```

**barPulse3**
```css
@keyframes barPulse3 {
  0% { height: 40%; }
  100% { height: 80%; }
}
```

**barPulse4**
```css
@keyframes barPulse4 {
  0% { height: 75%; }
  100% { height: 45%; }
}
```

**barPulse5**
```css
@keyframes barPulse5 {
  0% { height: 50%; }
  100% { height: 85%; }
}
```

**floatLayer**
```css
@keyframes floatLayer {
  0%, 100% { transform: translateY(0px) rotateX(45deg) rotateZ(-45deg); }
  50% { transform: translateY(-10px) rotateX(45deg) rotateZ(-45deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (3 instances)

```css
.button {
  background-color: rgb(17, 24, 39);
  color: rgb(107, 114, 128);
  font-size: 14px;
  font-weight: 400;
  padding-top: 8px;
  padding-right: 16px;
  border-radius: 999px;
}
```

### Cards (50 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 12px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 30px 0px;
  padding-top: 0px;
  padding-right: 12px;
}
```

### Inputs (1 instances)

```css
.input {
  color: rgb(15, 17, 20);
  border-color: rgb(15, 17, 20);
  border-radius: 0px;
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (26 instances)

```css
.link {
  color: rgb(107, 114, 128);
  font-size: 10.4px;
  font-weight: 400;
}
```

### Navigation (8 instances)

```css
.navigatio {
  background-color: rgba(255, 255, 255, 0.86);
  color: rgb(107, 114, 128);
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 16px;
  padding-right: 16px;
  position: relative;
  box-shadow: rgba(15, 17, 20, 0.08) 0px 18px 45px 0px;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: rgb(247, 248, 250);
  color: rgb(107, 114, 128);
  padding-top: 96px;
  padding-bottom: 96px;
  font-size: 10.4px;
}
```

### Dropdowns (17 instances)

```css
.dropdown {
  background-color: rgb(255, 255, 255);
  border-radius: 6px;
  box-shadow: rgba(15, 17, 20, 0.18) 0px 28px 70px 0px;
  border-color: rgb(209, 213, 219);
  padding-top: 0px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(17, 24, 39);
  color: rgb(255, 255, 255);
  padding: 16px 32px 16px 32px;
  border-radius: 9999px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 14px;
  font-weight: 500;
```

### Card — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(243, 244, 246);
  color: rgb(15, 17, 20);
  padding: 32px 32px 32px 32px;
  border-radius: 0px;
  border: 0px 1px 1px 0px solid rgb(209, 213, 219);
  font-size: 16px;
  font-weight: 400;
```

### Card — 5 instances, 2 variants

**Variant 1** (4 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(15, 17, 20);
  padding: 32px 32px 32px 32px;
  border-radius: 0px;
  border: 0px 1px 1px 0px solid rgb(209, 213, 219);
  font-size: 16px;
  font-weight: 400;
```

**Variant 2** (1 instance)

```css
  background: rgb(243, 244, 246);
  color: rgb(15, 17, 20);
  padding: 32px 32px 32px 32px;
  border-radius: 0px;
  border: 0px 1px 0px 0px solid rgb(209, 213, 219);
  font-size: 16px;
  font-weight: 400;
```

### Card — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(243, 244, 246);
  color: rgb(15, 17, 20);
  padding: 32px 32px 32px 32px;
  border-radius: 0px;
  border: 0px 1px 1px 0px solid rgb(209, 213, 219);
  font-size: 16px;
  font-weight: 400;
```

### Card — 6 instances, 1 variant

**Variant 1** (6 instances)

```css
  background: rgba(0, 0, 0, 0.05);
  color: rgb(15, 17, 20);
  padding: 16px 16px 16px 16px;
  border-radius: 16px;
  border: 1px solid rgba(0, 0, 0, 0.12);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgb(243, 244, 246);
  color: rgb(15, 17, 20);
  padding: 40px 40px 40px 40px;
  border-radius: 32px;
  border: 1px solid rgb(209, 213, 219);
  font-size: 16px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(107, 114, 128);
  padding: 8px 16px 8px 16px;
  border-radius: 999px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 14px;
  font-weight: 400;
```

## Layout System

**12 grid containers** and **211 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1600px | 0px |
| 600px | 0px |
| 940px | 0px |
| 1440px | 48px |
| 1232px | 28px |
| 1280px | 0px |
| 1203.2px | 0px |
| 1152px | 0px |
| 960px | 0px |
| 1024px | 0px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 4x |
| 1-column | 3x |
| 12-column | 2x |
| 4-column | 2x |
| 2-column | 1x |

### Grid Templates

```css
grid-template-columns: 296px 296px 296px 296px;
gap: 16px;
grid-template-columns: 76.6562px 76.6562px 76.6562px 76.6562px 76.6562px 76.6562px 76.6562px 76.6562px 76.6562px 76.6562px 76.6562px 76.6562px;
gap: 24px;
grid-template-columns: 394.656px 394.672px 394.656px;
gap: 24px;
grid-template-columns: 378.656px 378.672px 378.656px;
gap: 24px;
grid-template-columns: 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px;
gap: 32px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 54x |
| row/nowrap | 157x |

**Gap values:** `128px`, `12px`, `16px`, `24px`, `28px`, `32px`, `40px`, `48px`, `48px 32px`, `4px`, `6px`, `8px`, `96px`

## Responsive Design

### Viewport Snapshots

| Viewport | Body Font | Nav Visible | Max Columns | Hamburger | Page Height |
|----------|-----------|-------------|-------------|-----------|-------------|
| mobile (375px) | 16px | Yes | 2 | No | 14082px |
| tablet (768px) | 16px | Yes | 12 | No | 10852px |
| desktop (1280px) | 16px | Yes | 12 | No | 9628px |
| wide (1920px) | 16px | Yes | 12 | No | 9867px |

### Breakpoint Changes

**375px → 768px** (mobile → tablet):
- H1 size: `48px` → `72px`
- Max grid columns: `2` → `12`
- Page height: `14082px` → `10852px`

**768px → 1280px** (tablet → desktop):
- H1 size: `72px` → `96px`
- Page height: `10852px` → `9628px`

**1280px → 1920px** (desktop → wide):
- Page height: `9628px` → `9867px`

## Interaction States

### Button States

**"Get connected"**
```css
/* Focus */
background-color: rgb(17, 24, 39) → rgb(55, 65, 81);
outline: rgb(255, 255, 255) none 3px → rgb(255, 255, 255) auto 3px;
```

**"Products"**
```css
/* Focus */
color: rgb(107, 114, 128) → rgb(18, 20, 24);
background-color: rgba(0, 0, 0, 0) → rgba(249, 115, 22, 0.098);
outline: rgb(107, 114, 128) none 3px → rgb(0, 95, 204) auto 1px;
```

**"Network"**
```css
/* Focus */
outline: rgb(107, 114, 128) none 3px → rgb(0, 95, 204) auto 1px;
```

## Accessibility (WCAG 2.1)

**Overall Score: 25%** — 1 passing, 3 failing color pairs

### Failing Color Pairs

| Foreground | Background | Ratio | Level | Used On |
|------------|------------|-------|-------|---------|
| `#6b7280` | `#f3f4f6` | 4.39:1 | FAIL | span (3x) |

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#111827` | 17.74:1 | AAA |

## Dark Mode

The site has a distinct dark mode color scheme:

- **Primary:** `#f97316`
- **Secondary:** `#111827`
- **Backgrounds:** `#ffffff`, `#f3f4f6`, `#000000`, `#f7f8fa`
- **Text:** `#000000`, `#0f1114`, `#111827`, `#f97316`, `#6b7280`

### Dark Mode CSS Variables

```css
--color-bg: #080805;
--color-fg: #ffffff;
--color-accent: #F97316;
--color-card: #121212;
--color-border: #2A2A2A;
--color-muted: #888888;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--tw-ring-inset: ;
--tw-ring-offset-width: 0px;
--tw-border-spacing-x: 0;
--tw-shadow-colored: 0 0 #0000;
--tw-border-spacing-y: 0;
--tw-ring-color: rgb(59 130 246 / 0.5);
--tw-ring-offset-color: #fff;
--tw-contain-size: ;
--tw-numeric-spacing: ;
--tw-shadow: 0 0 #0000;
--tw-drop-shadow: ;
--tw-contrast: ;
--tw-backdrop-sepia: ;
--tw-sepia: ;
--tw-skew-x: 0;
--tw-ordinal: ;
--tw-backdrop-saturate: ;
--tw-contain-style: ;
--tw-backdrop-blur: ;
--tw-translate-x: 0;
--tw-gradient-via-position: ;
--tw-backdrop-invert: ;
--tw-saturate: ;
--tw-scroll-snap-strictness: proximity;
--tw-grayscale: ;
--tw-scale-x: 1;
--tw-backdrop-hue-rotate: ;
--tw-gradient-to-position: ;
--tw-brightness: ;
--tw-numeric-fraction: ;
--tw-backdrop-grayscale: ;
--tw-hue-rotate: ;
--tw-scale-y: 1;
--tw-pan-y: ;
--tw-backdrop-contrast: ;
--tw-skew-y: 0;
--tw-backdrop-brightness: ;
--tw-slashed-zero: ;
--tw-blur: ;
--tw-invert: ;
--tw-pan-x: ;
--tw-translate-y: 0;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--tw-numeric-figure: ;
--tw-rotate: 0;
--tw-pinch-zoom: ;
--tw-contain-paint: ;
--tw-contain-layout: ;
success: [object Object];
warning: [object Object];
error: [object Object];
info: [object Object];
```

## Design System Score

**Overall: 72/100 (Grade: C)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 82/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 78/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 25/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Good CSS variable tokenization

**Issues:**
- 3 WCAG contrast failures
- 216 !important rules — prefer specificity over overrides
- 90% of CSS is unused — consider purging
- 487 duplicate CSS declarations

## Gradients

**19 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | to top | 2 | brand |
| linear | to right | 2 | brand |
| linear | to left | 2 | brand |
| linear | to right | 2 | brand |
| linear | — | 2 | brand |
| radial | circle at 100% 0% | 2 | brand |
| linear | to right | 2 | brand |
| linear | — | 2 | brand |
| linear | to left | 2 | brand |
| radial | circle | 2 | brand |
| linear | — | 2 | brand |
| linear | to right top | 2 | brand |
| linear | — | 3 | bold |
| linear | — | 2 | brand |
| linear | to right bottom | 3 | bold |

```css
background: linear-gradient(to top, rgb(255, 255, 255) 30%, rgba(0, 0, 0, 0) 70%);
background: linear-gradient(to right, rgb(249, 250, 251), rgba(0, 0, 0, 0));
background: linear-gradient(to left, rgb(249, 250, 251), rgba(0, 0, 0, 0));
background: linear-gradient(to right, rgba(0, 0, 0, 0.08) 1px, rgba(0, 0, 0, 0) 1px);
background: linear-gradient(rgba(0, 0, 0, 0.08) 1px, rgba(0, 0, 0, 0) 1px);
```

## Z-Index Map

**12 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 10,50 | section.r.e.l.a.t.i.v.e. .z.-.1.0. .m.i.n.-.h.-.[.1.0.0.s.v.h.]. .p.t.-.2.4. .p.b.-.1.2. .p.x.-.6. .m.d.:.p.x.-.1.2. .f.l.e.x. .f.l.e.x.-.c.o.l. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .w.-.f.u.l.l, div.a.b.s.o.l.u.t.e. .b.o.t.t.o.m.-.1.0. .-.l.e.f.t.-.1.0. .f.l.e.x. .f.l.e.x.-.c.o.l. .g.a.p.-.1. .s.u.r.f.a.c.e.-.g.l.a.s.s. .p.-.4. .r.o.u.n.d.e.d.-.x.l. .b.o.r.d.e.r. .t.e.x.t.-.x.s. .f.o.n.t.-.m.o.n.o. .t.e.x.t.-.z.i.n.c.-.5.0.0. .z.-.1.0. .s.h.a.d.o.w.-.2.x.l. .b.o.r.d.e.r.-.w.h.i.t.e./.1.0, div |
| base | -10,7 | div.a.b.s.o.l.u.t.e. .t.o.p.-.1./.2. .l.e.f.t.-.1./.2. .-.t.r.a.n.s.l.a.t.e.-.x.-.1./.2. .-.t.r.a.n.s.l.a.t.e.-.y.-.1./.2. .w.-.[.6.0.0.p.x.]. .h.-.[.6.0.0.p.x.]. .b.g.-.a.c.c.e.n.t./.5. .r.o.u.n.d.e.d.-.f.u.l.l. .b.l.u.r.-.[.1.0.0.p.x.]. .-.z.-.1.0, div, div |

## SVG Icons

**10 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| xs | 1 |
| sm | 1 |
| md | 4 |
| lg | 1 |
| xl | 3 |

**Icon colors:** `currentColor`, `black`, `rgba(255,255,255,0.6)`, `rgb(0, 0, 0)`, `white`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Inter | google-fonts | 300, 400, 500, 600 | normal |
| Sora | google-fonts | 300, 400, 500, 600 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 8 | objectFit: contain, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (1x), 2.64:1 (1x), 3.94:1 (1x), 2.7:1 (1x), 2.97:1 (1x), 21:9 (1x), 6.08:1 (1x), 3.15:1 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `75ms` | 75 |
| `xs` | `100ms` | 100 |
| `sm` | `180ms` | 180 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `1s` | 1000 |

### Easing Families

- **custom** (39 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`
- **ease-out** (24 uses) — `cubic-bezier(0, 0, 0.2, 1)`, `cubic-bezier(0.16, 1, 0.3, 1)`, `cubic-bezier(0.23, 1, 0.32, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `gridMove` | slide-y | transform | 5 |
| `marquee` | slide-x | transform | 1 |
| `barPulse1` | custom | height | 3 |
| `barPulse2` | custom | height | 3 |
| `barPulse3` | custom | height | 2 |
| `barPulse4` | custom | height | 2 |
| `barPulse5` | custom | height | 2 |
| `floatLayer` | slide-y | transform | 3 |
| `pulse` | fade | opacity | 8 |
| `core-pulse-anim` | slide | transform, box-shadow | 1 |
| `radar-pull-anim` | slide | transform, opacity, border-width | 3 |
| `gravity-well-anim` | slide | transform, opacity, filter | 12 |

## Component Anatomy

### card — 17 instances

**Slots:** media
**Sizes:** md

### button — 3 instances

**Slots:** label
**Sizes:** sm

## Brand Voice

**Tone:** neutral · **Pronoun:** third-person · **Headings:** Title Case (tight)

### Top CTA Verbs

- **get** (1)
- **products** (1)
- **network** (1)

### Button Copy Patterns

- "get connected" (1×)
- "products" (1×)
- "network" (1×)

### Sample Headings

> Connect to the supply infrastructure behind travel.
> The supply and partner network behind FCG.
> The supply advantage behind every connection.
> One inventory underneath. Three product families.
> G-Link
> F-Link
> AgreeEase
> Atlas
> The supply advantage behind every connection.
> Deep, not just wide.

## Page Intent

**Type:** `landing` (confidence 0.29)

Alternates: legal (0.4), blog-post (0.35)

## Section Roles

Reading order (top→bottom): hero → logo-wall → pricing-table → content → feature-grid → content → pricing-table → comparison → content → content → nav → nav → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | hero | Connect to the supply infrastructure behind travel. | 0.85 |
| 1 | logo-wall | The supply and partner network behind FCG. | 0.85 |
| 2 | pricing-table | The supply advantage behind every connection. | 0.9 |
| 3 | content | One inventory underneath. Three product families. | 0.3 |
| 4 | feature-grid | The supply advantage behind every connection. | 0.8 |
| 5 | nav | — | 0.9 |
| 6 | content | THE CORE | 0.3 |
| 7 | pricing-table | The Connection at a Glance | 0.9 |
| 8 | comparison | Open connections vs. closed platforms. | 0.7 |
| 9 | content | The inventory that everything connects to. | 0.3 |
| 10 | content | The inventory that everything connects to. | 0.3 |
| 11 | nav | The inventory that everything connects to. | 0.4 |
| 12 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.209 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 19 |

## Imagery Style

**Label:** `flat-illustration` (confidence 0.417)
**Counts:** total 8, svg 5, icon 1, screenshot-like 0, photo-like 0
**Dominant aspect:** ultra-wide
**Radius profile on images:** square

## Component Library

**Detected:** `shadcn/ui` (confidence 0.65)

Evidence:
- shadcn css tokens

Also considered: tailwindcss (0.3)

## Component Screenshots

9 retina crops written to `screenshots/`. Index: `*-screenshots.json`.

| Cluster | Variant | Size (px) | File |
|---------|---------|-----------|------|
| button--default--sm | 0 | 184 × 52 | `screenshots/button-default-sm-0.png` |
| card--default--md | 0 | 235 × 104 | `screenshots/card-default-md-0.png` |
| card--default--md | 1 | 235 × 104 | `screenshots/card-default-md-1.png` |
| card--default--md | 2 | 235 × 104 | `screenshots/card-default-md-2.png` |
| card--default | 0 | 334 × 98 | `screenshots/card-default-0.png` |
| card--default | 1 | 334 × 113 | `screenshots/card-default-1.png` |
| card--default | 2 | 334 × 113 | `screenshots/card-default-2.png` |
| button--default | 0 | 111 × 36 | `screenshots/button-default-0.png` |
| button--default | 1 | 108 × 36 | `screenshots/button-default-1.png` |

Full-page: `screenshots/full-page.png`

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
