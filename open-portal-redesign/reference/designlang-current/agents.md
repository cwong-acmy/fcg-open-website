# Agent instructions — design system

This project follows the design system extracted from https://open.fusionconnectgroup.com/home.
Any coding agent working here must use the tokens below and avoid inventing new ones.
Source: https://open.fusionconnectgroup.com/home
Extracted by designlang v7.0.0 on 2026-09-07T09:38:29.093Z

## Semantic tokens (use these)
- color.action.primary: #f97316
- color.surface.default: #f5f7fa
- color.text.body: #1f1f1f
- radius.control: 4px
- typography.body.fontFamily: SF Pro Display

## Regions
- nav
- nav
- pricing
- content
- hero
- content
- content
- pricing
- footer

## How to use
- Prefer `semantic.*` tokens over `primitive.*`.
- Never invent new tokens or hex values; reuse the ones above.
- When a value is missing, pick the closest existing semantic token and flag the gap.
- Reference tokens by their dotted path (e.g. `semantic.color.action.primary`).
