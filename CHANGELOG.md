# Changelog

## v2.1 (2026-01-10)
- Simplified the episode generator to RSS-only mode.
- Removed legacy/manual parsing paths in favor of structured RSS sections.

## v2.0 (2026-01-10)
- Added RSS mode to `scripts/new_episode.py` with `--from-rss` and `--feed-url`.
- RSS workflow auto-selects the latest (or specified) episode, extracts episode metadata, and fetches transcripts.
- RSS extraction includes recording date (with `Recorded: YYYY-MM-DD` support), BTC prices, block height, music credits, and summary parsing.
- Transcript HTML is converted to text and wrapped in a fenced `text` block.
- Dry-run output expanded to show selected RSS item and extracted values.
- `README.md` updated with RSS mode usage and the recommended recording-date line.

## v1.0 (2026-01-10)
- Added `scripts/new_episode.py` to generate new episode and transcript pages.
- Supported manual mode with explicit flags and summary-blob mode.
- Episodes created in `content/episodes/episode-<N>.md`.
- Transcripts created in `content/episodes/episode-<N>-transcript.md`.
- Tags default to `["podcast"]`.
- `README.md` updated with weekly creation examples.
