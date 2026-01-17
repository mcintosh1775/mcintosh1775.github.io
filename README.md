# satoshis-plebs-hugo
The Satoshis Plebs Website using hugo templating..

## Weekly episode creation
Create a new episode and transcript using one of the modes below. Output files are written to `content/episodes/`.

Directory structure:
- `content/episodes/episode-<NNN>.md` (episode page, zero-padded)
- `content/episodes/episode-<N>-transcript.md` (transcript page, when available)
- `scripts/new_episode.py` (generator)

Options overview:
- Manual mode: `--title --date --podhome-id --block-height --btc-usd --btc-eur --summary-file --transcript-file --music-credits-file`
- Summary blob mode: `--podhome-id --summary-blob-file --transcript-file`
- RSS mode: `--from-rss --feed-url [--episode N] [--episodes 1-25]` (auto-fetches transcript when available)
- Shared: `--episode N` (override number), `--dry-run`, `--force`

Required flags by mode:
- Manual mode: `--title --date --podhome-id --block-height --btc-usd --btc-eur --summary-file --transcript-file --music-credits-file`
- Summary blob mode: `--podhome-id --summary-blob-file --transcript-file`
- RSS mode: `--from-rss --feed-url` (optionally add `--episode N` or `--episodes 1-25`)

Summary blob format example:
```
237 - From El Salvador to Africa: Fighting Monetary Control

In this episode, McIntosh and Kenshin discuss the IMF's influence over El Salvador's Bitcoin adoption.
The conversation expands into monetary colonialism in Africa and governance systems.

Bitcoin Price at Time of Recording
Dec 23rd, 2025: $87,770 USD | 74,450 Euro

Block Height at Time of Recording
928,310

Music Credits
The Top Hat Orchestra - Let It Snow
The Top Hat Orchestra - Hot Chocolate
```

The script dedupes repeated music lines and ignores duplicated sections.

Summary blob mode example:
```bash
python3 scripts/new_episode.py \
  --podhome-id "uuid-here" \
  --summary-blob-file /path/to/summary.txt \
  --transcript-file /path/to/transcript.md
```

Manual mode example:
```bash
python3 scripts/new_episode.py \
  --title "Episode Title" \
  --date 2025-01-01 \
  --podhome-id "uuid-here" \
  --block-height "928,310" \
  --btc-usd "85,700" \
  --btc-eur "72,991" \
  --summary-file /path/to/summary.md \
  --transcript-file /path/to/transcript.md \
  --music-credits-file /path/to/music-credits.txt
```

RSS mode example (latest episode):
```bash
python3 scripts/new_episode.py --from-rss --feed-url 'https://serve.podhome.fm/rss/3d1d205b-b9f7-5253-b09d-df1c8ec4fc25'
```

Optional flags:
- `--episode N` to select a specific episode from the feed.

Recommended show notes line for recording date:
- `Recorded: YYYY-MM-DD`

Output behavior:
- Always creates the episode page.
- Creates a transcript page only when a transcript is available.

Missing data handling (RSS mode):
- Prints warnings like `[WARN] No block height found for episode 182`.
- Missing transcript results in a note added to the episode body:
  `Transcript not available for this episode.`
- Optional fields are omitted when missing: block height, BTC prices, music credits.
