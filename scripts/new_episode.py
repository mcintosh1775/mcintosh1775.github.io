#!/usr/bin/env python3
import argparse
import email.utils
import html
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET


EPISODE_RE = re.compile(r"^episode-(\d+)\.md$")
RECORDING_DATE_RE = re.compile(r"Recorded:\s*(\d{4}-\d{2}-\d{2})")
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


def strip_html(text):
    text = re.sub(r"<\s*br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<\s*/p\s*>", "\n\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<\s*p\s*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<\s*/div\s*>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<\s*div[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text


def html_to_text(text):
    stripped = strip_html(text)
    lines = [line.rstrip() for line in stripped.split("\n")]
    return "\n".join(lines).strip()


def fetch_url(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; CodexBot/1.0)"},
    )
    with urllib.request.urlopen(request) as response:
        return response.read().decode("utf-8", errors="replace")


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


def parse_episode_number(value):
    if not value:
        return None
    match = re.search(r"\d+", str(value))
    return int(match.group(0)) if match else None


def clean_title(title):
    if not title:
        return ""
    cleaned = re.sub(
        r"^\s*(?:episode\s*)?\d+\s*[-:]\s*",
        "",
        title,
        flags=re.IGNORECASE,
    )
    return cleaned.strip() or title.strip()


def parse_pubdate(item):
    pub_date = item.findtext("pubDate")
    if not pub_date:
        return None
    try:
        return email.utils.parsedate_to_datetime(pub_date)
    except (TypeError, ValueError):
        return None


def choose_item(root, ns, episode_number):
    items = root.findall("./channel/item")
    if not items:
        raise ValueError("RSS feed contains no items")

    if episode_number is not None:
        for item in items:
            itunes_episode = parse_episode_number(item.findtext("itunes:episode", namespaces=ns))
            podcast_episode = parse_episode_number(item.findtext("podcast:episode", namespaces=ns))
            if itunes_episode == episode_number or podcast_episode == episode_number:
                return item
        raise ValueError(f"RSS item with episode {episode_number} not found")

    dated_items = []
    for item in items:
        parsed = parse_pubdate(item)
        if parsed:
            dated_items.append((parsed, item))
    if dated_items:
        dated_items.sort(key=lambda pair: pair[0])
        return dated_items[-1][1]
    return items[0]


def extract_music_credits(description_html):
    lower = description_html.lower()
    start_index = lower.find(HEADER_MUSIC)
    if start_index == -1:
        return []
    start_index += len(HEADER_MUSIC)
    end_index = None
    for header in (HEADER_BITCOIN, HEADER_BLOCK):
        index = lower.find(header, start_index)
        if index != -1:
            end_index = index if end_index is None else min(end_index, index)
    section_html = description_html[start_index:end_index]
    section_html = section_html.replace("\r\n", "\n").replace("\r", "\n")
    lines = re.split(r"\n+", re.sub(r"<\s*br\s*/?>", "\n", section_html, flags=re.IGNORECASE))

    credits = []
    seen = set()
    link_re = re.compile(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.IGNORECASE)
    for line in lines:
        candidate = line.strip()
        if not candidate:
            continue
        match = link_re.search(candidate)
        link = ""
        if match:
            link = match.group(1).strip()
        title = strip_html(candidate).strip()
        if not title:
            continue
        key = (title, link)
        if key in seen:
            continue
        seen.add(key)
        credits.append({"title": title, "link": link})
    return credits


def extract_summary(description_text):
    lower = description_text.lower()
    index = lower.find(HEADER_BITCOIN)
    if index == -1:
        return description_text.strip()
    return description_text[:index].strip()


def parse_rss_item(item, ns):
    itunes_episode = item.findtext("itunes:episode", namespaces=ns)
    podcast_episode = item.findtext("podcast:episode", namespaces=ns)
    episode_number = parse_episode_number(itunes_episode) or parse_episode_number(podcast_episode)

    raw_title = (
        item.findtext("itunes:title", namespaces=ns)
        or item.findtext("title")
        or ""
    ).strip()
    cleaned_title = clean_title(raw_title)

    if episode_number is None:
        episode_number = parse_episode_number(raw_title)
    if episode_number is None:
        raise ValueError("Could not determine episode number from RSS item")

    guid = (item.findtext("guid") or "").strip()
    if not guid:
        raise ValueError("RSS item guid is missing")

    description_html = item.findtext("description") or ""
    description_text = html_to_text(description_html)

    recorded_match = RECORDING_DATE_RE.search(description_text)
    recorded_date = recorded_match.group(1) if recorded_match else None

    price_match = DATE_LINE_RE.search(description_text)
    date_from_price = None
    btc_usd = None
    btc_eur = None
    if price_match:
        month_name = price_match.group(1).lower()
        day = int(price_match.group(2))
        year = int(price_match.group(4))
        month = MONTHS.get(month_name)
        if not month:
            raise ValueError(f"unknown month name: {price_match.group(1)}")
        date_from_price = f"{year:04d}-{month:02d}-{day:02d}"
        btc_usd = price_match.group(5)
        btc_eur = price_match.group(6)

    pubdate_dt = parse_pubdate(item)
    pubdate = pubdate_dt.date().isoformat() if pubdate_dt else None

    if recorded_date:
        date = recorded_date
    elif date_from_price:
        date = date_from_price
    elif pubdate:
        date = pubdate
    else:
        raise ValueError("Unable to determine episode date")

    if not btc_usd or not btc_eur:
        raise ValueError("Bitcoin price line not found in description")

    block_height = None
    block_header_found = False
    for line in description_text.splitlines():
        if normalize_header(line) == HEADER_BLOCK:
            block_header_found = True
            continue
        if block_header_found:
            candidate = line.strip()
            if candidate and re.fullmatch(r"[\d,]+", candidate):
                block_height = candidate
                break
    if not block_height:
        raise ValueError("Block height not found in description")

    music_credits = extract_music_credits(description_html)
    if not music_credits:
        raise ValueError("Music credits not found in description")

    summary = extract_summary(description_text)
    if not summary:
        raise ValueError("Summary content not found in description")

    transcript_elements = item.findall("podcast:transcript", namespaces=ns)
    transcript_url = ""
    for element in transcript_elements:
        rel = element.get("rel")
        content_type = element.get("type")
        url = element.get("url")
        if rel == "transcript" and content_type == "text/html" and url:
            transcript_url = url
            break
    if not transcript_url:
        raise ValueError("Transcript URL not found in RSS item")

    return {
        "episode_number": episode_number,
        "title": cleaned_title,
        "guid": guid,
        "date": date,
        "btc_usd": btc_usd,
        "btc_eur": btc_eur,
        "block_height": block_height,
        "music_credits": music_credits,
        "summary": summary,
        "transcript_url": transcript_url,
        "pubdate": pubdate,
    }


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
    parser.add_argument("--from-rss", action="store_true")
    parser.add_argument("--feed-url")
    parser.add_argument("--title")
    parser.add_argument("--date", help="YYYY-MM-DD")
    parser.add_argument("--podhome-id")
    parser.add_argument("--block-height")
    parser.add_argument("--btc-usd")
    parser.add_argument("--btc-eur")
    parser.add_argument("--summary-file")
    parser.add_argument("--summary-blob-file")
    parser.add_argument("--transcript-file")
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

    if args.from_rss:
        if not args.feed_url:
            raise ValueError("--feed-url is required when using --from-rss")
        try:
            feed_xml = fetch_url(args.feed_url)
        except Exception as exc:
            raise ValueError(f"Failed to fetch RSS feed: {exc}") from exc
        root = ET.fromstring(feed_xml)
        namespaces = {
            "itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
            "podcast": "https://podcastindex.org/namespace/1.0",
        }
        item = choose_item(root, namespaces, args.episode)
        rss_data = parse_rss_item(item, namespaces)
        if args.episode and rss_data["episode_number"] != args.episode:
            raise ValueError("RSS item episode number does not match --episode")

        if rss_data["pubdate"] and rss_data["date"]:
            if rss_data["pubdate"][:4] != rss_data["date"][:4]:
                print(
                    "warning: recording date year differs from pubDate year",
                    file=sys.stderr,
                )

        try:
            transcript_html = fetch_url(rss_data["transcript_url"])
        except Exception as exc:
            raise ValueError(f"Failed to fetch transcript: {exc}") from exc
        transcript_text = html_to_text(transcript_html)
        if not transcript_text:
            raise ValueError("Transcript content is empty")

        episode_number = rss_data["episode_number"]
        args.title = rss_data["title"]
        args.date = rss_data["date"]
        args.btc_usd = rss_data["btc_usd"]
        args.btc_eur = rss_data["btc_eur"]
        args.block_height = rss_data["block_height"]
        args.podhome_id = rss_data["guid"]
        summary = rss_data["summary"]
        music_credits = rss_data["music_credits"]
        transcript = f"```text\n{transcript_text}\n```"

        if args.dry_run:
            item_title = (
                item.findtext("itunes:title", namespaces=namespaces)
                or item.findtext("title")
                or ""
            ).strip()
            itunes_episode = item.findtext("itunes:episode", namespaces=namespaces)
            podcast_episode = item.findtext("podcast:episode", namespaces=namespaces)
            print("[dry-run] selected RSS item:")
            print(f"  title: {item_title}")
            print(f"  itunes:episode: {itunes_episode}")
            print(f"  podcast:episode: {podcast_episode}")
            print(f"  guid: {rss_data['guid']}")
            print("[dry-run] extracted values:")
            print(f"  episode: {episode_number}")
            print(f"  title: {args.title}")
            print(f"  date: {args.date}")
            print(f"  btc_usd: {args.btc_usd}")
            print(f"  btc_eur: {args.btc_eur}")
            print(f"  block_height: {args.block_height}")
            print(f"  music_credits: {len(music_credits)}")
            print(f"  transcript_url: {rss_data['transcript_url']}")
    else:
        if not args.podhome_id:
            raise ValueError("missing required argument: --podhome-id")
        if not args.transcript_file:
            raise ValueError("missing required argument: --transcript-file")
        auto_episode = next_episode_number(episodes_dir)
        episode_number = args.episode or auto_episode
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

    episode_path = os.path.join(
        episodes_dir, f"episode-{episode_number}.md"
    )
    transcript_path = os.path.join(
        episodes_dir, f"episode-{episode_number}-transcript.md"
    )

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
