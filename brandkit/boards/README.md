# Raster brand boards — not generated

The two prompts here were written per the `brandkit` skill's PROMPT TEMPLATE and are ready to run.
Blocked on image-model quota, 7 Sep 2026:

- Google AI Studio keys (both, in 1Password `LLM Automations`): `429 … free_tier_requests, limit: 0`
  for gemini-3-pro-image / gemini-3.1-flash-image / gemini-2.5-flash-image. No billing on the project.
- Higgsfield CLI: `Not authenticated` — needs an interactive `hf auth login`.

To run once a billed key exists:

    export GK=$(op read "op://LLM Automations/igeiixpop4ayfxl5bnbzdrpilu/credential")
    MODEL=gemini-3-pro-image python3 prompts/generate.py prompts/board-1-identity-3x3.txt fcg-identity.png 16:9
    MODEL=gemini-3-pro-image python3 prompts/generate.py prompts/board-2-deck-2x3.txt fcg-deck.png 4:3

Valid aspect ratios: 1:1 1:4 1:8 2:3 3:2 3:4 4:1 4:3 4:5 5:4 8:1 9:16 16:9 21:9 (no 16:10).
