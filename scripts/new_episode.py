#!/usr/bin/env python3
import argparse
import os
import re
import sys


EPISODE_RE = re.compile(r"^episode-(\d+)\.md$")
DATE_LINE_RE = re.compile(
    r"([A-Za-z]+)\s+(\d{1,2})(st|nd|rd|th)?,\s*(\d{4})\s*:\s*\$?([\d,]+)\s*USD\s*\|\s*([\d,]+)\s*(?:Euro|EUR)",
    re.IGNORECASE,
)
SUMMARY_TITLE_RE = re.compile(r"^(\d+)\s*-\s*(.+)$")
HEADER_BITCOIN = "bitcoin price at time of recording"
HEADER_BLOCK = "block height at time of recording"
HEADER_MUSIC = "music credits"
KNOWN_HEADERS = {HEADER_BITCOIN, HEADER_BLOCK, HEADER_MUSIC}
MONTHS = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}


def read_file(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def escape_yaml(value):
    return value.replace("\\", "\\\\").replace('"', '\\"')


def parse_music_credits(path):
    credits = []
    raw = read_file(path)
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "|" in line:
            title, link = [part.strip() for part in line.split("|", 1)]
        else:
            title, link = line, ""
        if not title:
            continue
        credits.append({"title": title, "link": link})
    if not credits:
        raise ValueError("music credits file must include at least one entry")
    return credits


def normalize_header(line):
    return re.sub(r":\s*$", "", line.strip()).lower()


def parse_summary_blob(path):
    raw = read_file(path)
    lines = raw.splitlines()
    if not lines:
        raise ValueError("summary blob file is empty")
    title_line = lines[0].strip()
    match = SUMMARY_TITLE_RE.match(title_line)
    if not match:
        raise ValueError('first line must be "<episode> - <title>"')

    blob_episode = int(match.group(1))
    title = match.group(2).strip()
    if not title:
        raise ValueError("title is missing from summary blob first line")

    summary_lines = []
    for line in lines[1:]:
        if normalize_header(line) == HEADER_BITCOIN:
            break
        summary_lines.append(line)
    summary = "\n".join(summary_lines).strip()
    if not summary:
        raise ValueError("summary content not found before Bitcoin Price header")

    date = None
    btc_usd = None
    btc_eur = None
    for line in lines:
        match = DATE_LINE_RE.search(line)
        if match:
            month_name = match.group(1).lower()
            day = int(match.group(2))
            year = int(match.group(4))
            month = MONTHS.get(month_name)
            if not month:
                raise ValueError(f"unknown month name: {match.group(1)}")
            date = f"{year:04d}-{month:02d}-{day:02d}"
            btc_usd = match.group(5)
            btc_eur = match.group(6)
            break
    if not date:
        raise ValueError("Bitcoin price line not found in summary blob")

    block_height = None
    block_header_found = False
    for line in lines:
        if normalize_header(line) == HEADER_BLOCK:
            block_header_found = True
            continue
        if block_header_found:
            candidate = line.strip()
            if candidate and re.fullmatch(r"[\d,]+", candidate):
                block_height = candidate
                break
    if not block_height:
        raise ValueError("block height value not found after header")

    music_credits = []
    seen_music = set()
    music_header_found = False
    for line in lines:
        normalized = normalize_header(line)
        if normalized == HEADER_MUSIC and not music_header_found:
            music_header_found = True
            continue
        if music_header_found and normalized in KNOWN_HEADERS:
            break
        if music_header_found:
            candidate = line.strip()
            if not candidate:
                continue
            if candidate in seen_music:
                continue
            seen_music.add(candidate)
            music_credits.append({"title": candidate, "link": ""})
    if not music_credits:
        raise ValueError("music credits section is missing or empty")

    return {
        "blob_episode": blob_episode,
        "title": title,
        "summary": summary,
        "date": date,
        "btc_usd": btc_usd,
        "btc_eur": btc_eur,
        "block_height": block_height,
        "music_credits": music_credits,
    }


def next_episode_number(episodes_dir):
    max_episode = 0
    for name in os.listdir(episodes_dir):
        match = EPISODE_RE.match(name)
        if not match:
            continue
        number = int(match.group(1))
        max_episode = max(max_episode, number)
    return max_episode + 1


def build_episode_frontmatter(args, episode_number, music_credits):
    lines = [
        "---",
        f'title: "{escape_yaml(args.title)}"',
        f"date: {args.date}",
        f"episode: {episode_number}",
        f'podhome_id: "{escape_yaml(args.podhome_id)}"',
        f'btc_price_usd: "{escape_yaml(args.btc_usd)}"',
        f'btc_price_eur: "{escape_yaml(args.btc_eur)}"',
        f'block_height: "{escape_yaml(args.block_height)}"',
        "music_credits:",
    ]
    for credit in music_credits:
        lines.append(f'  - title: "{escape_yaml(credit["title"])}"')
        if credit["link"]:
            lines.append(f'    link: "{escape_yaml(credit["link"])}"')
    lines.append('tags: ["podcast"]')
    lines.append("---")
    return "\n".join(lines)


def build_transcript_frontmatter(episode_number):
    lines = [
        "---",
        f'title: "Episode {episode_number} Transcript"',
        "draft: false",
        "_build:",
        "  list: never",
        "  render: always",
        "---",
    ]
    return "\n".join(lines)


def write_file(path, content, force):
    if os.path.exists(path) and not force:
        raise FileExistsError(f"{path} already exists (use --force to overwrite)")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def main():
    parser = argparse.ArgumentParser(
        description="Create a new episode and transcript in content/episodes/."
    )
    parser.add_argument("--title")
    parser.add_argument("--date", help="YYYY-MM-DD")
    parser.add_argument("--podhome-id", required=True)
    parser.add_argument("--block-height")
    parser.add_argument("--btc-usd")
    parser.add_argument("--btc-eur")
    parser.add_argument("--summary-file")
    parser.add_argument("--summary-blob-file")
    parser.add_argument("--transcript-file", required=True)
    parser.add_argument("--music-credits-file")
    parser.add_argument("--episode", type=int, help="Override auto-numbering")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    episodes_dir = os.path.join(repo_root, "content", "episodes")
    if not os.path.isdir(episodes_dir):
        print("content/episodes directory not found", file=sys.stderr)
        return 1

    auto_episode = next_episode_number(episodes_dir)
    episode_number = args.episode or auto_episode
    episode_path = os.path.join(episodes_dir, f"episode-{episode_number}.md")
    transcript_path = os.path.join(
        episodes_dir, f"episode-{episode_number}-transcript.md"
    )

    if args.summary_blob_file:
        blob = parse_summary_blob(args.summary_blob_file)
        if args.episode is None and blob["blob_episode"] != auto_episode:
            raise ValueError(
                "summary blob episode number does not match auto-number; use --episode to override"
            )
        args.title = blob["title"]
        args.date = blob["date"]
        args.btc_usd = blob["btc_usd"]
        args.btc_eur = blob["btc_eur"]
        args.block_height = blob["block_height"]
        summary = blob["summary"]
        music_credits = blob["music_credits"]
    else:
        missing = [
            name
            for name, value in {
                "--title": args.title,
                "--date": args.date,
                "--block-height": args.block_height,
                "--btc-usd": args.btc_usd,
                "--btc-eur": args.btc_eur,
                "--summary-file": args.summary_file,
                "--music-credits-file": args.music_credits_file,
            }.items()
            if not value
        ]
        if missing:
            raise ValueError(
                "missing required arguments: " + ", ".join(missing)
            )
        summary = read_file(args.summary_file).rstrip()
        music_credits = parse_music_credits(args.music_credits_file)

    transcript = read_file(args.transcript_file).rstrip()

    episode_frontmatter = build_episode_frontmatter(args, episode_number, music_credits)
    transcript_frontmatter = build_transcript_frontmatter(episode_number)

    episode_content = f"{episode_frontmatter}\n{summary}\n"
    transcript_content = f"{transcript_frontmatter}\n{transcript}\n"

    if args.dry_run:
        print(f"[dry-run] would write: {episode_path}")
        print(f"[dry-run] would write: {transcript_path}")
        return 0

    write_file(episode_path, episode_content, args.force)
    write_file(transcript_path, transcript_content, args.force)
    print(f"wrote {episode_path}")
    print(f"wrote {transcript_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
