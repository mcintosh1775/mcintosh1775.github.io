# Codex Instructions for This Repository

This repository is a Hugo-based static site for the Satoshi’s Plebs Podcast.
Codex should follow these rules when assisting with changes.

## General Rules

- Do NOT change Hugo layouts unless explicitly asked.
- Do NOT rewrite existing content files unless explicitly asked.
- Prefer minimal, incremental changes.
- Always explain proposed changes before making them.
- Respect the existing content structure and naming conventions.

## Content Structure

- Episode pages live in:
  - `content/episodes/episode-<N>.md`
- Transcript pages live in:
  - `content/episodes/episode-<N>-transcript.md`
- Episode list pages (`/episodes/`) are generated automatically by Hugo.
- Do NOT manually edit index or list pages unless explicitly instructed.

## Episode Creation

- New episodes are generated using:
  - `scripts/new_episode.py`
- Required episode fields:
  - title
  - date
  - podhome_id
  - block_height (string, for display)
  - btc_price_usd
  - btc_price_eur
  - music_credits
- Tags default to `"podcast"`.

If episode automation exists, **use or extend it** rather than creating manual content.

## Safety & Workflow

- Use `--dry-run` where applicable.
- Never overwrite episode files without explicit confirmation.
- Assume Git is the source of truth; do not auto-commit changes.
- Avoid introducing new dependencies unless requested.

## Preferred Assistance

Codex is primarily used for:
- automating repetitive content creation
- maintaining consistency across episodes
- improving tooling and scripts
- explaining or refactoring code safely

Codex should ask clarifying questions if a request risks breaking
Hugo rendering, content history, or automation workflows.
