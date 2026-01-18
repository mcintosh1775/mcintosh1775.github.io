# satoshis-plebs-hugo
The Satoshis Plebs Website using hugo templating..

## Weekly episode creation
Create a new episode and transcript from RSS. Output files are written to `content/episodes/`.

Directory structure:
- `content/episodes/episode-<NNN>.md` (episode page, zero-padded)
- `content/episodes/episode-<N>-transcript.md` (transcript page, when available)
- `scripts/new_episode.py` (generator)

Options overview:
- RSS mode: `--from-rss --feed-url [--episode N] [--episodes 1-25]` (auto-fetches transcript when available)
- Shared: `--episode N` (override number), `--dry-run`, `--force`

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

## Preferred show notes format
Use this structure for consistent parsing and rendering:
```
<EPISODE NUMBER> - <Episode Title>

<Short summary paragraph. You can include links inline.>

Recorded: YYYY-MM-DD

Bitcoin Price at Time of Recording
Jan 6th, 2026: $91,180 USD | 78,000 Euro

Block Height at Time of Recording
928,310

Music Credits
Song Title by Artist
Another Song by Artist
```
