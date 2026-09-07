# Design Language: Open Platform

> Extracted from `https://open.fusionconnectgroup.com/home` on September 7, 2026
> 580 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#f97316` | rgb(249, 115, 22) | hsl(25, 95%, 53%) | 79 |
| Secondary | `#020617` | rgb(2, 6, 23) | hsl(229, 84%, 5%) | 17 |
| Accent | `#10b981` | rgb(16, 185, 129) | hsl(160, 84%, 39%) | 1 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e2e4e9` | hsl(223, 14%, 90%) | 551 |
| `#ffffff` | hsl(0, 0%, 100%) | 166 |
| `#0f1114` | hsl(216, 14%, 7%) | 75 |
| `#6b7280` | hsl(220, 9%, 46%) | 40 |
| `#64748b` | hsl(215, 16%, 47%) | 37 |
| `#52525b` | hsl(240, 5%, 34%) | 29 |
| `#3f3f46` | hsl(240, 5%, 26%) | 19 |
| `#1f1f1f` | hsl(0, 0%, 12%) | 13 |
| `#fff7ed` | hsl(33, 100%, 96%) | 13 |
| `#334155` | hsl(215, 25%, 27%) | 3 |
| `#000000` | hsl(0, 0%, 0%) | 1 |

### Background Colors

Used on large-area elements: `#f5f7fa`, `#f9fafb`, `#ffffff`, `#020617`, `#0f1114`, `#fbfcfd`

### Text Colors

Text color palette: `#1f1f1f`, `#0f172a`, `#182231`, `#ffffff`, `#0f1114`, `#686f7d`, `#334155`, `#020617`, `#64748b`, `#6b7280`

### Gradients

```css
background-image: linear-gradient(135deg, rgb(38, 53, 72) 0%, rgb(24, 34, 49) 42%, rgb(16, 23, 34) 100%);
```

```css
background-image: linear-gradient(to right, rgba(15, 17, 20, 0.043) 1px, rgba(0, 0, 0, 0) 1px), linear-gradient(rgba(15, 17, 20, 0.043) 1px, rgba(0, 0, 0, 0) 1px);
```

```css
background-image: linear-gradient(rgb(248, 250, 252), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(to right, rgba(255, 255, 255, 0.08) 1px, rgba(0, 0, 0, 0) 1px), linear-gradient(rgba(255, 255, 255, 0.08) 1px, rgba(0, 0, 0, 0) 1px);
```

```css
background-image: radial-gradient(circle at 50% 57%, rgba(221, 228, 234, 0.32) 0px, rgba(238, 242, 245, 0.16) 30%, rgba(255, 255, 255, 0) 62%), linear-gradient(to right, rgba(15, 17, 20, 0.027) 1px, rgba(0, 0, 0, 0) 1px), linear-gradient(rgba(15, 17, 20, 0.027) 1px, rgba(0, 0, 0, 0) 1px), none;
```

```css
background-image: radial-gradient(circle, rgb(255, 255, 255) 0px, rgb(255, 255, 255) 32%, rgb(247, 248, 249) 60%, rgb(233, 236, 239) 100%);
```

```css
background-image: linear-gradient(135deg, rgba(255, 255, 255, 0.78), rgba(247, 249, 251, 0.48));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e2e4e9` | border | 551 |
| `#ffffff` | background, text, border | 166 |
| `#0f172a` | text | 161 |
| `#f97316` | background, border, text | 79 |
| `#0f1114` | text, background | 75 |
| `#6b7280` | text | 40 |
| `#64748b` | text | 37 |
| `#52525b` | text | 29 |
| `#3f3f46` | text | 19 |
| `#020617` | text, background, border | 17 |
| `#22c55e` | text | 16 |
| `#1f1f1f` | text | 13 |
| `#fff7ed` | background | 13 |
| `#c2410c` | text | 7 |
| `#334155` | text | 3 |
| `#fed7aa` | border | 3 |
| `#182231` | text, border | 2 |
| `#000000` | border | 1 |
| `#10b981` | background | 1 |

## Typography

### Font Families

- **SF Pro Display** — used for all (580 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 96px | 6rem | 500 | 92.16px | normal | h1 |
| 44px | 2.75rem | 600 | 47.52px | normal | h2 |
| 36px | 2.25rem | 700 | 43.2px | normal | div |
| 32px | 2rem | 400 | 0px | normal | span, svg, path, div |
| 28px | 1.75rem | 400 | 42px | normal | div, span, svg, path |
| 24px | 1.5rem | 400 | 36px | normal | div, span, svg, path |
| 20px | 1.25rem | 400 | 28px | normal | p, h3 |
| 18px | 1.125rem | 600 | 28px | normal | a, div, svg, path |
| 16px | 1rem | 400 | 24px | normal | html, head, style, meta |
| 15px | 0.9375rem | 650 | 18px | normal | span |
| 14px | 0.875rem | 500 | 16px | normal | a, button, span, svg |
| 12px | 0.75rem | 500 | 16px | normal | a, div, span, svg |
| 9px | 0.5625rem | 700 | 9px | normal | span |

### Heading Scale

```css
h1 { font-size: 96px; font-weight: 500; line-height: 92.16px; }
h2 { font-size: 44px; font-weight: 600; line-height: 47.52px; }
h3 { font-size: 20px; font-weight: 400; line-height: 28px; }
h3 { font-size: 18px; font-weight: 600; line-height: 28px; }
h3 { font-size: 14px; font-weight: 500; line-height: 16px; }
```

### Body Text

```css
body { font-size: 14px; font-weight: 500; line-height: 16px; }
```

### Font Weights in Use

`400` (451x), `500` (63x), `600` (45x), `700` (13x), `650` (8x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-2 | 2px | 0.125rem |
| spacing-24 | 24px | 1.5rem |
| spacing-28 | 28px | 1.75rem |
| spacing-40 | 40px | 2.5rem |
| spacing-48 | 48px | 3rem |
| spacing-64 | 64px | 4rem |
| spacing-78 | 78px | 4.875rem |
| spacing-88 | 88px | 5.5rem |
| spacing-112 | 112px | 7rem |
| spacing-192 | 192px | 12rem |
| spacing-272 | 272px | 17rem |
| spacing-288 | 288px | 18rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| sm | 4px | 2 |
| md | 8px | 37 |
| lg | 16px | 3 |
| full | 50px | 1 |
| full | 999px | 19 |
| full | 9999px | 21 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 17, 20, 0.06) 0px 18px 50px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 17, 20, 0.06) 0px 10px 30px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 17, 20, 0.16) 0px 18px 48px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 17, 20, 0.06) 0px 12px 34px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 17, 20, 0.38) 0px 24px 54px -34px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 17, 20, 0.06) 0px 1px 3px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 23, 42, 0.14) 0px 18px 50px 0px;
```

**xl (inset)** — blur: 42px
```css
box-shadow: rgba(36, 50, 68, 0.26) 0px 16px 42px -24px, rgba(255, 255, 255, 0.18) 0px 1px 0px 0px inset;
```

**xl (inset)** — blur: 46px
```css
box-shadow: rgba(100, 116, 139, 0.1) 0px 22px 46px 0px, rgba(100, 116, 139, 0.043) 0px 2px 5px 0px, rgba(255, 255, 255, 0.86) 0px 1px 0px 0px inset;
```

**xl** — blur: 54px
```css
box-shadow: rgba(15, 17, 20, 0.38) 0px 24px 54px -34px;
```

**xl (inset)** — blur: 80px
```css
box-shadow: rgba(148, 163, 184, 0.2) 0px 24px 80px 0px, rgba(255, 255, 255, 0.92) 0px 1px 0px 0px inset;
```

## CSS Custom Properties

### Colors

```css
--opaque-button-border-intensity: -8;
--foreground: 220 14% 7%;
--border: 220 14% 90%;
--card: 0 0% 100%;
--card-foreground: 220 14% 7%;
--card-border: 220 14% 91%;
--sidebar-foreground: 220 12% 86%;
--sidebar-border: 220 12% 18%;
--sidebar-primary: 24 95% 53%;
--sidebar-primary-foreground: 0 0% 100%;
--sidebar-accent: 220 12% 18%;
--sidebar-accent-foreground: 220 12% 92%;
--sidebar-ring: 24 95% 53%;
--popover: 0 0% 100%;
--popover-foreground: 220 14% 7%;
--popover-border: 220 14% 90%;
--primary: 24 95% 53%;
--primary-foreground: 0 0% 100%;
--secondary: 220 14% 95%;
--secondary-foreground: 220 14% 12%;
--muted: 220 14% 96%;
--muted-foreground: 220 9% 45%;
--accent: 24 95% 96%;
--accent-foreground: 220 14% 7%;
--premium-ink-border: #344458;
--destructive: 0 84% 60%;
--destructive-foreground: 0 0% 100%;
--ring: 24 95% 53%;
--chart-1: 24 95% 53%;
--chart-2: 142 76% 36%;
--chart-3: 47 96% 53%;
--chart-4: 25 95% 53%;
--chart-5: 16 85% 58%;
--tag-hotel-bg: 40 100% 96%;
--tag-hotel-foreground: 32 78% 32%;
--tag-hotel-border: 42 82% 82%;
--tag-flight-bg: 197 100% 96%;
--tag-flight-foreground: 200 88% 34%;
--tag-flight-border: 200 88% 84%;
--tag-tmc-bg: 268 100% 97%;
--tag-tmc-foreground: 270 61% 42%;
--tag-tmc-border: 268 83% 86%;
--sidebar-primary-border: hsl(var(--sidebar-primary));
--sidebar-accent-border: hsl(var(--sidebar-accent));
--primary-border: hsl(var(--primary));
--secondary-border: hsl(var(--secondary));
--muted-border: hsl(var(--muted));
--accent-border: hsl(var(--accent));
--destructive-border: hsl(var(--destructive));
--op-select-border: #e5e7eb;
--op-select-hover-border: #cbd5e1;
--op-select-focus-border: #0f172a;
--op-select-focus-ring: rgba(15, 23, 42, 0.1);
--op-select-option-hover-bg: #f8fafc;
--op-select-option-selected-bg: #f1f5f9;
--op-select-option-selected-hover-bg: #e2e8f0;
--op-json-bg: #f8fafc;
--op-json-bg-hover: #f1f5f9;
--op-json-border: #e5e7eb;
--op-json-border-focus: #0f172a;
--op-json-ring: rgba(15, 23, 42, 0.1);
--op-json-muted: #64748b;
--tw-ring-shadow: 0 0 #0000;
--tw-border-spacing-x: 0;
--tw-ring-color: rgb(59 130 246 / .5);
--tw-ring-offset-color: #fff;
--tw-ring-offset-width: 0px;
--tw-shadow-colored: 0 0 #0000;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-inset: ;
--tw-border-spacing-y: 0;
--tw-border-opacity: 1;
```

### Spacing

```css
--spacing: .25rem;
--tw-numeric-spacing: ;
--tw-contain-size: ;
```

### Typography

```css
--app-font-sans: "SF Pro Display", "SF Pro Text", "Poppins", "PingFang SC", "Microsoft YaHei", sans-serif;
--app-font-serif: Georgia, serif;
--app-font-mono: "JetBrains Mono", Menlo, monospace;
--tracking-normal: 0em;
--op-select-option-hover-text: #0f172a;
--op-select-option-selected-text: #0f172a;
--op-select-option-selected-hover-text: #0f172a;
--op-json-text: #334155;
```

### Shadows

```css
--shadow-2xs: 0px 1px 2px 0px rgba(0, 0, 0, .05);
--shadow-xs: 0px 1px 3px 0px rgba(15, 17, 20, .06);
--shadow-sm: 0px 10px 28px -24px rgba(15, 17, 20, .28);
--shadow: 0px 18px 42px -30px rgba(15, 17, 20, .34);
--shadow-md: 0px 24px 54px -34px rgba(15, 17, 20, .38);
--shadow-lg: 0px 32px 68px -42px rgba(15, 17, 20, .42);
--shadow-xl: 0px 40px 90px -52px rgba(15, 17, 20, .5);
--shadow-2xl: 0px 56px 120px -64px rgba(15, 17, 20, .55);
--tw-drop-shadow: ;
--tw-shadow: 0 0 #0000;
```

### Radii

```css
--radius: .375rem;
```

### Other

```css
--button-outline: rgba(0, 0, 0, .1);
--badge-outline: rgba(0, 0, 0, .05);
--elevate-1: rgba(0, 0, 0, .03);
--elevate-2: rgba(0, 0, 0, .08);
--background: 210 20% 98%;
--sidebar: 220 16% 10%;
--premium-ink: #182231;
--premium-ink-soft: #243244;
--premium-ink-deep: #101722;
--premium-ink-glow: rgba(36, 50, 68, .26);
--input: 30 18% 85%;
--tw-backdrop-sepia: ;
--tw-sepia: ;
--tw-ordinal: ;
--tw-contain-style: ;
--tw-backdrop-invert: ;
--tw-backdrop-grayscale: ;
--tw-hue-rotate: ;
--tw-pan-y: ;
--tw-rotate: 0;
--tw-gradient-via-position: ;
--tw-saturate: ;
--tw-scroll-snap-strictness: proximity;
--tw-grayscale: ;
--tw-backdrop-hue-rotate: ;
--tw-gradient-to-position: ;
--tw-numeric-fraction: ;
--tw-skew-y: 0;
--tw-slashed-zero: ;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--tw-pinch-zoom: ;
--tw-contain-paint: ;
--tw-backdrop-saturate: ;
--tw-brightness: ;
--tw-scale-y: 1;
--tw-backdrop-contrast: ;
--tw-backdrop-brightness: ;
--tw-pan-x: ;
--tw-translate-y: 0;
--tw-contrast: ;
--tw-skew-x: 0;
--tw-backdrop-blur: ;
--tw-translate-x: 0;
--tw-scale-x: 1;
--tw-blur: ;
--tw-invert: ;
--tw-numeric-figure: ;
--tw-contain-layout: ;
```

### Dependencies

```css
--sidebar-primary-border: --sidebar-primary;
--sidebar-accent-border: --sidebar-accent;
--primary-border: --primary;
--secondary-border: --secondary;
--muted-border: --muted;
--accent-border: --accent;
--destructive-border: --destructive;
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
| sm | 520px | max-width |
| sm | 640px | min-width |
| md | 768px | min-width |
| md | 812px | max-width |
| 850px | 850px | max-width |
| 851px | 851px | min-width |
| 900px | 900px | min-width |
| lg | 1024px | min-width |
| lg | 1060px | max-width |
| 1100px | 1100px | min-width |
| 1200px | 1200px | min-width |
| xl | 1280px | min-width |
| 2xl | 1536px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`

**Durations:** `0.18s`, `0.26s`, `0.15s`, `0.3s`, `0.82s`, `0.25s`, `0.2s`, `0.09s`, `0.08s`, `0.07s`, `0.14s`, `0.21s`

### Common Transitions

```css
transition: all;
transition: transform 0.18s, border-color 0.18s, box-shadow 0.18s, background-position 0.26s;
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 0.82s cubic-bezier(0.18, 0.86, 0.32, 1), transform 0.82s cubic-bezier(0.18, 0.86, 0.32, 1), filter 0.82s cubic-bezier(0.18, 0.86, 0.32, 1);
transition: transform 0.25s, border-color 0.25s, box-shadow 0.25s;
transition: gap 0.2s, transform 0.2s;
transition: opacity 0.82s cubic-bezier(0.18, 0.86, 0.32, 1) 0.09s, transform 0.82s cubic-bezier(0.18, 0.86, 0.32, 1) 0.09s, filter 0.82s cubic-bezier(0.18, 0.86, 0.32, 1) 0.09s;
transition: opacity 0.82s cubic-bezier(0.18, 0.86, 0.32, 1) 0.18s, transform 0.82s cubic-bezier(0.18, 0.86, 0.32, 1) 0.18s, filter 0.82s cubic-bezier(0.18, 0.86, 0.32, 1) 0.18s;
transition: opacity 0.82s cubic-bezier(0.18, 0.86, 0.32, 1) 0.08s, transform 0.82s cubic-bezier(0.18, 0.86, 0.32, 1) 0.08s, filter 0.82s cubic-bezier(0.18, 0.86, 0.32, 1) 0.08s;
```

### Keyframe Animations

**loadingCircle**
```css
@keyframes loadingCircle {
  100% { transform: rotate(360deg); }
}
```

**loadingCircle**
```css
@keyframes loadingCircle {
  100% { transform: rotate(360deg); }
}
```

**mapboxgl-spin**
```css
@keyframes mapboxgl-spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(1turn); }
}
```

**mapboxgl-user-location-dot-pulse**
```css
@keyframes mapboxgl-user-location-dot-pulse {
  0% { transform: scale(1); opacity: 1; }
  70% { transform: scale(3); opacity: 0; }
  100% { transform: scale(1); opacity: 0; }
}
```

**pulse**
```css
@keyframes pulse {
  50% { opacity: 0.5; }
}
```

**spin**
```css
@keyframes spin {
  100% { transform: rotate(360deg); }
}
```

**globe-label-float**
```css
@keyframes globe-label-float {
  0%, 100% { transform: translateZ(0px); }
  50% { transform: translate3d(0px, -6px, 0px); }
}
```

**hero-decor-float**
```css
@keyframes hero-decor-float {
  0%, 100% { transform: translateZ(0px) scale(1); }
  50% { transform: translate3d(0px, -30px, 0px) scale(1.018); }
}
```

**home-hero-rise**
```css
@keyframes home-hero-rise {
  0% { opacity: 0; transform: translate3d(0px, 42px, 0px); }
  100% { opacity: 1; transform: translateZ(0px); }
}
```

**home-hero-visual-in**
```css
@keyframes home-hero-visual-in {
  0% { opacity: 0; transform: translate3d(42px, 34px, 0px) scale(0.96); }
  100% { opacity: 1; transform: translateZ(0px) scale(1); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (5 instances)

```css
.button {
  background-color: rgb(255, 255, 255);
  color: rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 400;
  padding-top: 8px;
  padding-right: 8px;
  border-radius: 9999px;
}
```

### Cards (2 instances)

```css
.card {
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 9999px;
  box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 17, 20, 0.06) 0px 10px 30px 0px;
  padding-top: 6px;
  padding-right: 12px;
}
```

### Links (25 instances)

```css
.link {
  color: rgb(100, 116, 139);
  font-size: 14px;
  font-weight: 500;
}
```

### Navigation (3 instances)

```css
.navigatio {
  background-color: rgba(249, 115, 22, 0.1);
  color: rgb(15, 23, 42);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
  padding-right: 0px;
  position: static;
}
```

### Footer (1 instances)

```css
.foote {
  background-color: rgb(255, 255, 255);
  color: rgb(15, 23, 42);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

### Dropdowns (1 instances)

```css
.dropdown {
  border-radius: 0px;
  border-color: rgb(226, 228, 233);
  padding-top: 0px;
}
```

### Badges (2 instances)

```css
.badge {
  color: rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 500;
  padding-top: 8px;
  padding-right: 14px;
  border-radius: 9999px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(0, 0, 0, 0);
  color: rgb(104, 111, 125);
  padding: 6px 10px 6px 10px;
  border-radius: 9999px;
  border: 0px solid rgb(226, 228, 233);
  font-size: 14px;
  font-weight: 400;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(255, 255, 255);
  color: rgb(2, 6, 23);
  padding: 12px 28px 12px 28px;
  border-radius: 9999px;
  border: 0px solid rgb(226, 228, 233);
  font-size: 14px;
  font-weight: 600;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgba(255, 255, 255, 0.05);
  color: rgb(255, 255, 255);
  padding: 8px 16px 8px 16px;
  border-radius: 9999px;
  border: 1px solid rgba(0, 0, 0, 0.1);
  font-size: 14px;
  font-weight: 500;
```

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(249, 112, 21);
  color: rgb(255, 255, 255);
  padding: 0px 0px 0px 0px;
  border-radius: 8px;
  border: 1px solid rgb(249, 112, 21);
  font-size: 16px;
  font-weight: 400;
```

## Layout System

**8 grid containers** and **180 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1500px | 32px |
| 672px | 0px |
| 760px | 0px |
| 576px | 0px |
| 840px | 0px |
| 1280px | 32px |
| 896px | 32px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 4x |
| 2-column | 2x |
| 4-column | 2x |

### Grid Templates

```css
grid-template-columns: 525.594px 642.406px;
gap: 48px;
grid-template-columns: 393.328px 393.328px 393.344px;
gap: 18px;
grid-template-columns: 393.328px 393.328px 393.344px;
gap: 18px;
grid-template-columns: 393.328px 393.328px 393.344px;
gap: 18px;
grid-template-columns: 407px 407px;
gap: 18px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| row/nowrap | 155x |
| row/wrap | 6x |
| column/nowrap | 19x |

**Gap values:** `10px`, `12px`, `16px`, `18px`, `32px`, `48px`, `4px`, `6px`, `8px`

## Responsive Design

### Viewport Snapshots

| Viewport | Body Font | Nav Visible | Max Columns | Hamburger | Page Height |
|----------|-----------|-------------|-------------|-----------|-------------|
| mobile (375px) | 16px | Yes | 2 | Yes | 10903px |
| tablet (768px) | 16px | Yes | 4 | Yes | 7446px |
| desktop (1280px) | 16px | Yes | 4 | Yes | 6440px |
| wide (1920px) | 16px | Yes | 4 | Yes | 6720px |

### Breakpoint Changes

**375px → 768px** (mobile → tablet):
- H1 size: `60px` → `88px`
- Max grid columns: `2` → `4`
- Page height: `10903px` → `7446px`

**768px → 1280px** (tablet → desktop):
- H1 size: `88px` → `96px`
- Page height: `7446px` → `6440px`

**1280px → 1920px** (desktop → wide):
- Page height: `6440px` → `6720px`

## Interaction States

### Button States

**"English"**
```css
/* Hover */
color: rgb(104, 111, 125) → rgb(18, 20, 24);
background-color: rgba(0, 0, 0, 0) → rgba(241, 245, 249, 0.97);
outline: rgb(104, 111, 125) none 3px → rgb(18, 20, 24) none 3px;
```
```css
/* Focus */
color: rgb(104, 111, 125) → rgb(15, 17, 20);
background-color: rgba(0, 0, 0, 0) → rgb(241, 245, 249);
outline: rgb(104, 111, 125) none 3px → rgb(0, 95, 204) auto 1px;
```

**"Browse Skills"**
```css
/* Hover */
background-color: rgb(255, 255, 255) → rgba(255, 255, 255, 0.925);
```
```css
/* Focus */
background-color: rgb(255, 255, 255) → rgba(255, 255, 255, 0.9);
outline: rgb(2, 6, 23) none 3px → rgb(1, 59, 130) auto 1px;
```

**"AI"**
```css
/* Hover */
transform: none → matrix(1.03266, 0, 0, 1.03266, 0, -1.30658);
```
```css
/* Focus */
transform: none → matrix(1.05, 0, 0, 1.05, 0, -2);
outline: rgb(255, 255, 255) none 3px → rgb(10, 101, 206) auto 1px;
```

### Link Hover

```css
border-color: color(srgb 0.203922 0.266667 0.345098 / 0.74) → rgba(71, 85, 105, 0.82);
box-shadow: rgba(36, 50, 68, 0.26) 0px 16px 42px -24px, rgba(255, 255, 255, 0.18) 0px 1px 0px 0px inset → rgba(24, 34, 49, 0.38) 0px 20px 52px -24px, rgba(255, 255, 255, 0.22) 0px 1px 0px 0px inset;
transform: none → matrix(1, 0, 0, 1, 0, -1);
```

## Accessibility (WCAG 2.1)

**Overall Score: 95%** — 20 passing, 1 failing color pairs

### Failing Color Pairs

| Foreground | Background | Ratio | Level | Used On |
|------------|------------|-------|-------|---------|
| `#ffffff` | `#10b981` | 2.54:1 | FAIL | span (1x) |

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#c2410c` | `#fff7ed` | 4.88:1 | AA |
| `#3f3f46` | `#f4f4f5` | 9.5:1 | AAA |
| `#52525b` | `#f4f4f5` | 7.03:1 | AAA |
| `#0f1114` | `#f1f5f9` | 17.26:1 | AAA |
| `#020617` | `#ffffff` | 20.17:1 | AAA |
| `#0f1114` | `#f3f4f6` | 17.18:1 | AAA |

## Design System Score

**Overall: 88/100 (Grade: B)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 90/100 |
| Spacing System | 100/100 |
| Shadow Consistency | 78/100 |
| Border Radius Consistency | 90/100 |
| Accessibility | 95/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Consistent typography system, Well-defined spacing scale, Consistent border radii, Strong accessibility compliance, Good CSS variable tokenization

**Issues:**
- 1 WCAG contrast failures
- 327 !important rules — prefer specificity over overrides
- 90% of CSS is unused — consider purging
- 1820 duplicate CSS declarations

## Gradients

**11 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | 135deg | 3 | bold |
| linear | to right | 2 | brand |
| linear | — | 2 | brand |
| linear | — | 2 | brand |
| linear | to right | 2 | brand |
| linear | — | 2 | brand |
| radial | circle at 50% 57% | 3 | bold |
| linear | to right | 2 | brand |
| linear | — | 2 | brand |
| radial | circle | 4 | bold |
| linear | 135deg | 2 | brand |

```css
background: linear-gradient(135deg, rgb(38, 53, 72) 0%, rgb(24, 34, 49) 42%, rgb(16, 23, 34) 100%);
background: linear-gradient(to right, rgba(15, 17, 20, 0.043) 1px, rgba(0, 0, 0, 0) 1px);
background: linear-gradient(rgba(15, 17, 20, 0.043) 1px, rgba(0, 0, 0, 0) 1px);
background: linear-gradient(rgb(248, 250, 252), rgba(0, 0, 0, 0));
background: linear-gradient(to right, rgba(255, 255, 255, 0.08) 1px, rgba(0, 0, 0, 0) 1px);
```

## Z-Index Map

**6 unique z-index values** across 3 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| modal | 9998,9998 | button.f.i.x.e.d. .z.-.[.9.9.9.8.]. .f.l.e.x. .h.-.[.5.2.p.x.]. .w.-.[.5.2.p.x.]. .i.t.e.m.s.-.c.e.n.t.e.r. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .r.o.u.n.d.e.d.-.[.8.p.x.]. .b.o.r.d.e.r. .b.o.r.d.e.r.-.p.r.i.m.a.r.y.-.b.o.r.d.e.r. .b.g.-.p.r.i.m.a.r.y. .t.e.x.t.-.w.h.i.t.e. .s.h.a.d.o.w.-.s.o.f.t. .c.u.r.s.o.r.-.g.r.a.b. .t.r.a.n.s.i.t.i.o.n.-.a.l.l. .d.u.r.a.t.i.o.n.-.2.0.0. .h.o.v.e.r.:.-.t.r.a.n.s.l.a.t.e.-.y.-.0...5. .h.o.v.e.r.:.s.c.a.l.e.-.1.0.5. .a.c.t.i.v.e.:.c.u.r.s.o.r.-.g.r.a.b.b.i.n.g. .a.c.t.i.v.e.:.s.c.a.l.e.-.9.5 |
| sticky | 10,20 | div.r.e.l.a.t.i.v.e. .z.-.1.0. .m.x.-.a.u.t.o. .m.a.x.-.w.-.[.1.5.0.0.p.x.]. .p.x.-.4. .s.m.:.p.x.-.6. .l.g.:.p.x.-.8, div.r.e.l.a.t.i.v.e. .z.-.1.0. .f.l.e.x. .f.l.e.x.-.c.o.l. .m.d.:.f.l.e.x.-.r.o.w. .i.t.e.m.s.-.c.e.n.t.e.r. .g.a.p.-.8. .p.x.-.1.0. .p.y.-.1.0, div.r.e.l.a.t.i.v.e. .z.-.1.0. .f.l.e.x. .w.-.f.u.l.l. .f.l.e.x.-.c.o.l. .i.t.e.m.s.-.c.e.n.t.e.r |
| base | 0,3 | a.i.n.l.i.n.e.-.f.l.e.x. .m.i.n.-.h.-.8. .i.t.e.m.s.-.c.e.n.t.e.r. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .g.a.p.-.2. .w.h.i.t.e.s.p.a.c.e.-.n.o.w.r.a.p. .r.o.u.n.d.e.d.-.m.d. .b.o.r.d.e.r. .b.o.r.d.e.r.-.t.r.a.n.s.p.a.r.e.n.t. .p.x.-.3. .t.e.x.t.-.x.s. .f.o.n.t.-.m.e.d.i.u.m. .t.e.x.t.-.f.o.r.e.g.r.o.u.n.d. .t.r.a.n.s.i.t.i.o.n.-.c.o.l.o.r.s. .f.o.c.u.s.-.v.i.s.i.b.l.e.:.o.u.t.l.i.n.e.-.n.o.n.e. .f.o.c.u.s.-.v.i.s.i.b.l.e.:.r.i.n.g.-.1. .f.o.c.u.s.-.v.i.s.i.b.l.e.:.r.i.n.g.-.r.i.n.g. .d.i.s.a.b.l.e.d.:.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .d.i.s.a.b.l.e.d.:.o.p.a.c.i.t.y.-.5.0. .[.&._.s.v.g.].:.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .[.&._.s.v.g.].:.s.i.z.e.-.4. .[.&._.s.v.g.].:.s.h.r.i.n.k.-.0. .h.o.v.e.r.-.e.l.e.v.a.t.e. .a.c.t.i.v.e.-.e.l.e.v.a.t.e.-.2, a.i.n.l.i.n.e.-.f.l.e.x. .i.t.e.m.s.-.c.e.n.t.e.r. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .w.h.i.t.e.s.p.a.c.e.-.n.o.w.r.a.p. .t.e.x.t.-.s.m. .f.o.n.t.-.m.e.d.i.u.m. .f.o.c.u.s.-.v.i.s.i.b.l.e.:.o.u.t.l.i.n.e.-.n.o.n.e. .f.o.c.u.s.-.v.i.s.i.b.l.e.:.r.i.n.g.-.1. .f.o.c.u.s.-.v.i.s.i.b.l.e.:.r.i.n.g.-.r.i.n.g. .d.i.s.a.b.l.e.d.:.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .d.i.s.a.b.l.e.d.:.o.p.a.c.i.t.y.-.5.0. .[.&._.s.v.g.].:.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .[.&._.s.v.g.].:.s.i.z.e.-.4. .[.&._.s.v.g.].:.s.h.r.i.n.k.-.0. .h.o.v.e.r.-.e.l.e.v.a.t.e. .a.c.t.i.v.e.-.e.l.e.v.a.t.e.-.2. .b.g.-.p.r.i.m.a.r.y. .t.e.x.t.-.p.r.i.m.a.r.y.-.f.o.r.e.g.r.o.u.n.d. .b.o.r.d.e.r. .b.o.r.d.e.r.-.p.r.i.m.a.r.y.-.b.o.r.d.e.r. .m.i.n.-.h.-.9. .p.x.-.4. .p.y.-.2. .w.-.f.u.l.l. .r.o.u.n.d.e.d.-.f.u.l.l. .g.a.p.-.2. .a.c.t.i.v.e.:.s.c.a.l.e.-.9.5. .t.r.a.n.s.i.t.i.o.n.-.a.l.l. .d.u.r.a.t.i.o.n.-.3.0.0. .n.o.-.u.n.d.e.r.l.i.n.e, a.i.n.l.i.n.e.-.f.l.e.x. .i.t.e.m.s.-.c.e.n.t.e.r. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .w.h.i.t.e.s.p.a.c.e.-.n.o.w.r.a.p. .t.e.x.t.-.s.m. .f.o.n.t.-.m.e.d.i.u.m. .f.o.c.u.s.-.v.i.s.i.b.l.e.:.o.u.t.l.i.n.e.-.n.o.n.e. .f.o.c.u.s.-.v.i.s.i.b.l.e.:.r.i.n.g.-.1. .f.o.c.u.s.-.v.i.s.i.b.l.e.:.r.i.n.g.-.r.i.n.g. .d.i.s.a.b.l.e.d.:.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .d.i.s.a.b.l.e.d.:.o.p.a.c.i.t.y.-.5.0. .[.&._.s.v.g.].:.p.o.i.n.t.e.r.-.e.v.e.n.t.s.-.n.o.n.e. .[.&._.s.v.g.].:.s.i.z.e.-.4. .[.&._.s.v.g.].:.s.h.r.i.n.k.-.0. .h.o.v.e.r.-.e.l.e.v.a.t.e. .a.c.t.i.v.e.-.e.l.e.v.a.t.e.-.2. .b.o.r.d.e.r. .[.b.o.r.d.e.r.-.c.o.l.o.r.:.v.a.r.(.-.-.b.u.t.t.o.n.-.o.u.t.l.i.n.e.).]. .s.h.a.d.o.w.-.x.s. .a.c.t.i.v.e.:.s.h.a.d.o.w.-.n.o.n.e. .m.i.n.-.h.-.9. .p.x.-.4. .p.y.-.2. .w.-.f.u.l.l. .r.o.u.n.d.e.d.-.f.u.l.l. .g.a.p.-.2. .b.o.r.d.e.r.-.w.h.i.t.e./.3.0. .t.e.x.t.-.w.h.i.t.e. .h.o.v.e.r.:.b.g.-.w.h.i.t.e./.1.0. .a.c.t.i.v.e.:.s.c.a.l.e.-.9.5. .t.r.a.n.s.i.t.i.o.n.-.a.l.l. .d.u.r.a.t.i.o.n.-.3.0.0. .b.g.-.w.h.i.t.e./.5. .n.o.-.u.n.d.e.r.l.i.n.e |

## SVG Icons

**19 unique SVG icons** detected. Dominant style: **filled**.

| Size Class | Count |
|------------|-------|
| xs | 8 |
| sm | 3 |
| md | 6 |
| lg | 2 |

**Icon colors:** `white`, `currentColor`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| thumbnail | 50 | objectFit: fill, borderRadius: 0px, shape: square |
| gallery | 1 | objectFit: contain, borderRadius: 0px, shape: square |

**Aspect ratios:** 1:1 (50x), 3:2 (1x)

## Motion Language

**Feel:** responsive · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `70ms` | 70 |
| `xs` | `90ms` | 90 |
| `sm` | `180ms` | 180 |
| `md` | `260ms` | 260 |
| `xl` | `820ms` | 820 |

### Easing Families

- **custom** (21 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`
- **ease-out** (24 uses) — `cubic-bezier(0.18, 0.86, 0.32, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `hero-decor-float` | slide | transform | 1 |
| `home-hero-rise` | slide | opacity, transform | 4 |
| `home-hero-visual-in` | slide | opacity, transform | 1 |
| `partner-core-drift` | slide | transform | 1 |
| `partner-core-icon` | rotate | transform | 1 |
| `partner-collect-in` | slide | transform, opacity, filter | 8 |
| `partner-collect-in` | slide | transform, opacity, filter | 8 |
| `partner-collect-in` | slide | transform, opacity, filter | 8 |
| `partner-collect-in` | slide | transform, opacity, filter | 8 |
| `partner-collect-in` | slide | transform, opacity, filter | 8 |
| `partner-collect-in` | slide | transform, opacity, filter | 8 |
| `partner-collect-in` | slide | transform, opacity, filter | 8 |
| `partner-collect-in` | slide | transform, opacity, filter | 8 |

## Component Anatomy

### button — 4 instances

**Slots:** label, icon
**Variants:** outline · primary
**Sizes:** sm

| variant | count | sample label |
|---|---|---|
| default | 2 | English |
| outline | 1 | Book a 30-minute demo |
| primary | 1 | AI |

## Brand Voice

**Tone:** neutral · **Pronoun:** you-only · **Headings:** Title Case (tight)

### Top CTA Verbs

- **english** (1)
- **browse** (1)
- **book** (1)
- **ai** (1)

### Button Copy Patterns

- "english" (1×)
- "browse skills" (1×)
- "book a 30-minute demo" (1×)
- "ai" (1×)

### Sample Headings

> FCG Developer Platform
> Core Products
> G-Link Hotel API
> F-Link Flight API
> TMC API
> FCG Developer Platform
> Skills Packages
> The supply and partner network behind FCG.
> Ready to get started?
> Free Access

## Page Intent

**Type:** `unknown` (confidence 0)

## Section Roles

Reading order (top→bottom): nav → nav → pricing → content → hero → content → testimonial → pricing-table → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | nav | — | 0.4 |
| 1 | nav | — | 0.9 |
| 2 | pricing | FCG Developer Platform | 0.4 |
| 3 | content | FCG Developer Platform | 0.3 |
| 4 | hero | Skills Packages | 0.4 |
| 5 | content | — | 0.3 |
| 6 | testimonial | The supply and partner network behind FCG. | 0.8 |
| 7 | pricing-table | Ready to get started? | 0.9 |
| 8 | footer | Product Docs | 0.95 |

## Material Language

**Label:** `material-you` (confidence 0.45)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.389 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 11 |

## Imagery Style

**Label:** `mixed` (confidence 0.039)
**Counts:** total 51, svg 0, icon 50, screenshot-like 0, photo-like 0
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `shadcn/ui` (confidence 0.65)

Evidence:
- shadcn css tokens

Also considered: tailwindcss (0.3)

## Component Screenshots

4 retina crops written to `screenshots/`. Index: `*-screenshots.json`.

| Cluster | Variant | Size (px) | File |
|---------|---------|-----------|------|
| button--default--sm | 0 | 90 × 32 | `screenshots/button-default-sm-0.png` |
| button--default--sm | 1 | 168 × 43 | `screenshots/button-default-sm-1.png` |
| button--outline--sm | 0 | 336 × 37 | `screenshots/button-outline-sm-0.png` |
| button--primary | 0 | 52 × 52 | `screenshots/button-primary-0.png` |

Full-page: `screenshots/full-page.png`

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `SF Pro Display` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
