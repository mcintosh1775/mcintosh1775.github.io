# satoshis-plebs-hugo
The Satoshis Plebs Website using hugo templating..

## Weekly episode creation
Create a new episode and transcript using one of the modes below.

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
