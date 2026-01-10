# satoshis-plebs-hugo
The Satoshis Plebs Website using hugo templating..

## Weekly episode creation
Create a new episode and transcript from a summary blob and transcript file.

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

Example command:
```bash
python3 scripts/new_episode.py \
  --podhome-id "uuid-here" \
  --summary-blob-file /path/to/summary.txt \
  --transcript-file /path/to/transcript.md
```
