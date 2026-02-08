#!/usr/bin/env python3
import argparse
import email.utils
import html
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date as date_today


EPISODE_RE = re.compile(r"^episode-(\d+)\.md$")
RECORDING_DATE_RE = re.compile(r"Recorded:\s*(\d{4}-\d{2}-\d{2})")
DATE_LINE_RE = re.compile(
    r"([A-Za-z]+)\s+(\d{1,2})(st|nd|rd|th)?,\s*(\d{4})\s*:",
    re.IGNORECASE,
)
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


def normalize_header(line):
    return re.sub(r":\s*$", "", line.strip()).lower()


def strip_html(text):
    text = re.sub(r"<\s*br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<\s*/p\s*>", "\n\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<\s*p\s*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<\s*/div\s*>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<\s*div[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(
        r'<\s*a[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
        lambda match: f"[{strip_html(match.group(2))}]({match.group(1)})",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text


def html_to_text(text):
    stripped = strip_html(text)
    lines = [line.rstrip() for line in stripped.split("\n")]
    return "\n".join(lines).strip()


def normalize_transcript_text(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    return "\n".join(lines).strip()


def normalize_html_transcript(text):
    cleaned = html_to_text(text)
    cleaned = re.sub(r"([A-Za-z])([0-9]{2}:[0-9]{2}:[0-9]{2})", r"\1 \2", cleaned)
    cleaned = re.sub(r"([0-9]{2}:[0-9]{2}:[0-9]{2})([A-Za-z])", r"\1 \2", cleaned)
    return normalize_transcript_text(cleaned)

def convert_caption_transcript(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")
    out = []
    in_note = False
    current_time = None
    current_text = []

    def flush():
        nonlocal current_time, current_text
        if current_time is None:
            current_text = []
            return
        combined = " ".join(chunk.strip() for chunk in current_text if chunk.strip())
        if combined:
            out.append(f"[{current_time}] {combined}")
            out.append("")
        current_time = None
        current_text = []

    time_re = re.compile(
        r"(\d{2}:\d{2}:\d{2})[.,]\d+\s+-->\s+\d{2}:\d{2}:\d{2}[.,]\d+"
    )

    for line in lines:
        raw = line.strip()
        if in_note:
            if raw == "":
                in_note = False
            continue
        if raw == "WEBVTT":
            continue
        if raw.startswith("NOTE"):
            in_note = True
            continue
        if raw.isdigit() and current_time is None:
            continue
        match = time_re.match(raw)
        if match:
            if current_time is not None:
                flush()
            current_time = match.group(1)
            continue
        if raw == "":
            flush()
            continue
        if current_time is not None:
            current_text.append(raw)
    flush()
    return "\n".join(out).rstrip()


def format_transcript_body(transcript_text, transcript_type):
    if transcript_type == "text/html":
        return transcript_text.strip()
    if transcript_type in ("vtt", "srt"):
        return convert_caption_transcript(transcript_text)
    return transcript_text.strip()


def strip_footer_block(text):
    marker = "podcasting 2.0 apps available at"
    lower = text.lower()
    index = lower.find(marker)
    if index == -1:
        return text.strip()
    return text[:index].rstrip()


def fetch_url(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; CodexBot/1.0)"},
    )
    with urllib.request.urlopen(request) as response:
        return response.read().decode("utf-8", errors="replace")


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


def format_episode_number(number):
    return f"{number:03d}"


def parse_episode_list(value):
    if not value:
        return []
    episodes = []
    seen = set()
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_text, end_text = [chunk.strip() for chunk in part.split("-", 1)]
            if not start_text.isdigit() or not end_text.isdigit():
                continue
            start = int(start_text)
            end = int(end_text)
            if start > end:
                start, end = end, start
            for number in range(start, end + 1):
                if number in seen:
                    continue
                seen.add(number)
                episodes.append(number)
        else:
            if not part.isdigit():
                continue
            number = int(part)
            if number in seen:
                continue
            seen.add(number)
            episodes.append(number)
    return episodes


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


def filter_music_credits(credits):
    filtered = []
    footer_markers = [
        "podcasting 2.0 apps available",
        "value4value",
        "i can be reached by email",
        "mastodon handle",
        "nostr npub",
        "twitter",
        "contact",
        "satoshis-plebs.com",
    ]
    for credit in credits:
        title = credit.get("title", "")
        link = credit.get("link", "")
        lower = title.lower()
        if any(marker in lower for marker in footer_markers):
            continue
        if link and link.lower().startswith("mailto:"):
            continue
        filtered.append(credit)
    return filtered


def normalize_music_credits(credits):
    normalized = []
    for credit in credits:
        title = credit.get("title", "")
        link = credit.get("link", "")
        def first_url(text):
            match = re.search(r"\[(https?://[^\]]+)\]\(about:blank\)", text)
            if match:
                return match.group(1)
            match = re.search(r"\[Link:\s*(https?://[^\]]+)\]\(about:blank\)", text, re.IGNORECASE)
            if match:
                return match.group(1)
            match = re.search(r"\]\((https?://[^)]+)\)", text)
            if match:
                return match.group(1)
            match = re.search(r"https?://[^\s)]+", text)
            if match:
                url = match.group(0)
                if "](about:blank" in url:
                    url = url.split("](", 1)[0]
                return url
            return ""

        if "Music:" in title or "music:" in title:
            url_match = first_url(title)
            preamble = title.split("Music:", 1)[0]
            preamble_lines = [line.strip() for line in preamble.splitlines() if line.strip()]
            if preamble_lines:
                pre_title = preamble_lines[0]
                if not pre_title.lower().startswith("link:"):
                    normalized.append(
                        {"title": pre_title, "link": url_match}
                    )
            for match in re.finditer(r"Music:\s*([^\n]+)(.*?)(?=\nMusic:|$)", title, re.IGNORECASE | re.DOTALL):
                song_title = match.group(1).strip()
                chunk = match.group(2)
                song_link = first_url(chunk)
                normalized.append({"title": song_title, "link": song_link})
            if normalized:
                continue
        lower = title.lower()
        if "link:" in lower or "license" in lower:
            lines = [line.strip() for line in title.splitlines() if line.strip()]
            current = None
            for line in lines:
                line_lower = line.lower().lstrip("[")
                if line_lower.startswith("link:"):
                    url = first_url(line)
                    if current and url:
                        current["link"] = url
                    continue
                if line_lower.startswith("license:") or line_lower.startswith("license ("):
                    continue
                if line_lower.startswith("the following music was used"):
                    continue
                if line_lower in ("website", "artist website"):
                    continue
                if line_lower.startswith("http://") or line_lower.startswith("https://"):
                    if current and not current.get("link"):
                        current["link"] = line
                    continue
                if current:
                    normalized.append(current)
                current = {"title": line, "link": ""}
            if current:
                normalized.append(current)
            if normalized:
                continue
        if "Link:" in title or "link:" in title:
            if title.count("Link:") + title.count("link:") > 1:
                parts = re.split(r"\bLink:\b", title, flags=re.IGNORECASE)
                base = parts[0].strip()
                if base:
                    first_link = first_url(title)
                    normalized.append({"title": base, "link": first_link})
                for chunk in parts[1:]:
                    chunk = chunk.strip()
                    if not chunk:
                        continue
                    chunk_title = chunk.split("License:", 1)[0].strip()
                    if not chunk_title:
                        continue
                    chunk_link = first_url(chunk)
                    normalized.append({"title": chunk_title, "link": chunk_link})
                if normalized:
                    continue
        if "Link:" in title or "link:" in title:
            lead = re.split(r"\bLink:\b", title, maxsplit=1, flags=re.IGNORECASE)[0]
            lead = lead.strip()
            if lead:
                lead_link = first_url(title)
                normalized.append({"title": lead, "link": lead_link})
                continue
        normalized.append({"title": title, "link": link})
    return normalized


def extract_summary(description_text):
    lower = description_text.lower()
    index = lower.find(HEADER_BITCOIN)
    if index == -1:
        return description_text.strip()
    return description_text[:index].strip()


def parse_rss_item(item, ns):
    itunes_episode = item.findtext("itunes:episode", namespaces=ns)
    podcast_episode = item.findtext("podcast:episode", namespaces=ns)
    warnings = []
    episode_number = parse_episode_number(itunes_episode) or parse_episode_number(
        podcast_episode
    )

    raw_title = (
        item.findtext("itunes:title", namespaces=ns)
        or item.findtext("title")
        or ""
    ).strip()
    cleaned_title = clean_title(raw_title)

    if episode_number is None:
        episode_number = parse_episode_number(raw_title)
    if episode_number is None:
        warnings.append("No episode number found in RSS item")

    guid = (item.findtext("guid") or "").strip()
    if not guid:
        warnings.append("No guid found in RSS item")

    description_html = item.findtext("description") or ""
    description_text = html_to_text(description_html)

    recorded_match = RECORDING_DATE_RE.search(description_text)
    recorded_date = recorded_match.group(1) if recorded_match else None

    price_match = None
    price_line = None
    for line in description_text.splitlines():
        match = DATE_LINE_RE.search(line)
        if match:
            price_match = match
            price_line = line
            break
    date_from_price = None
    btc_usd = None
    btc_eur = None
    if price_match:
        month_name = price_match.group(1).lower()
        day = int(price_match.group(2))
        year = int(price_match.group(4))
        month = MONTHS.get(month_name)
        if not month:
            warnings.append(f"Unknown month name: {price_match.group(1)}")
        else:
            date_from_price = f"{year:04d}-{month:02d}-{day:02d}"
            if price_line:
                usd_match = re.search(r"\$?([\d,]+)\s*USD", price_line, re.IGNORECASE)
                eur_match = re.search(r"([\d,]+)\s*(?:Euro|EUR)", price_line, re.IGNORECASE)
                if usd_match:
                    btc_usd = usd_match.group(1)
                if eur_match:
                    btc_eur = eur_match.group(1)
    else:
        warnings.append("No bitcoin price found")

    pubdate_dt = parse_pubdate(item)
    pubdate = pubdate_dt.date().isoformat() if pubdate_dt else None

    if recorded_date:
        date = recorded_date
    elif date_from_price:
        date = date_from_price
    elif pubdate:
        date = pubdate
    else:
        date = None

    block_height = None
    block_header_found = False
    for line in description_text.splitlines():
        lowered = line.lower()
        if normalize_header(line) == HEADER_BLOCK or (
            "block height" in lowered and "recording" in lowered
        ):
            block_header_found = True
            inline_match = re.search(r"([\d,]+)", line)
            if inline_match:
                block_height = inline_match.group(1)
                break
            continue
        if block_header_found:
            candidate = line.strip()
            if candidate and re.fullmatch(r"[\d,]+", candidate):
                block_height = candidate
                break
    if not block_height:
        warnings.append("No block height found")

    music_credits = extract_music_credits(description_html)
    if not music_credits:
        warnings.append("No music credits found")

    summary = extract_summary(description_text)
    if not summary:
        warnings.append("No summary content found")

    transcript_elements = item.findall("podcast:transcript", namespaces=ns)
    transcript_url = ""
    transcript_type = ""
    for element in transcript_elements:
        rel = element.get("rel")
        content_type = element.get("type")
        url = element.get("url")
        if rel == "transcript" and content_type == "text/html" and url:
            transcript_url = url
            transcript_type = "text/html"
            break
    if not transcript_url:
        for element in transcript_elements:
            content_type = element.get("type")
            url = element.get("url")
            if content_type in ("application/srt", "text/srt") and url:
                transcript_url = url
                transcript_type = "srt"
                break
    if not transcript_url:
        for element in transcript_elements:
            content_type = element.get("type")
            url = element.get("url")
            if content_type in ("text/vtt", "application/vtt") and url:
                transcript_url = url
                transcript_type = "vtt"
                break
    if not transcript_url:
        pass

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
        "transcript_type": transcript_type,
        "pubdate": pubdate,
        "warnings": warnings,
    }


def process_rss_episode(root, namespaces, episodes_dir, args, warn, requested_episode, bulk_mode):
    try:
        item = choose_item(root, namespaces, requested_episode)
    except ValueError as exc:
        warn(f"[WARN] {exc}")
        return "failed"
    rss_data = parse_rss_item(item, namespaces)
    for warning in rss_data["warnings"]:
        if rss_data["episode_number"]:
            warn(f"[WARN] {warning} for episode {rss_data['episode_number']}")
        elif requested_episode:
            warn(f"[WARN] {warning} for episode {requested_episode}")
        else:
            warn(f"[WARN] {warning}")

    episode_number = rss_data["episode_number"] or requested_episode
    if episode_number is None:
        episode_number = next_episode_number(episodes_dir)
        warn("[WARN] No episode number found; using next available number")

    if requested_episode and rss_data["episode_number"] and rss_data["episode_number"] != requested_episode:
        warn("[WARN] RSS item episode number does not match --episode")

    if rss_data["pubdate"] and rss_data["date"]:
        if rss_data["pubdate"][:4] != rss_data["date"][:4]:
            warn("[WARN] Recording date year differs from pubDate year")

    transcript = None
    transcript_url = rss_data["transcript_url"]
    transcript_warned = False
    if transcript_url:
        try:
            transcript_raw = fetch_url(transcript_url)
            if rss_data["transcript_type"] == "text/html":
                transcript_text = normalize_html_transcript(transcript_raw)
            else:
                transcript_text = normalize_transcript_text(transcript_raw)
            if transcript_text:
                transcript = format_transcript_body(
                    transcript_text, rss_data["transcript_type"]
                )
            else:
                warn(f"[WARN] Transcript content is empty for episode {episode_number}")
                transcript_warned = True
        except Exception as exc:
            warn(f"[WARN] Failed to fetch transcript for episode {episode_number}: {exc}")
            transcript_warned = True
    else:
        warn(f"[WARN] No transcript available for episode {episode_number}")
        transcript_warned = True

    if not transcript and not transcript_warned:
        warn(f"[WARN] No transcript available for episode {episode_number}")

    if not rss_data["date"] and rss_data["pubdate"]:
        warn(f"[WARN] No recording date found for episode {episode_number}, using pubDate")

    args.title = rss_data["title"] or ""
    args.date = rss_data["date"] or rss_data["pubdate"] or ""
    if not args.date:
        args.date = date_today.today().isoformat()
        warn(
            f"[WARN] No recording date or pubDate found for episode {episode_number}, using today's date"
        )
    args.btc_usd = rss_data["btc_usd"]
    args.btc_eur = rss_data["btc_eur"]
    args.block_height = rss_data["block_height"]
    music_credits = rss_data["music_credits"] or []
    args.podhome_id = rss_data["guid"] or ""
    summary = rss_data["summary"] or ""
    summary = strip_footer_block(summary)
    summary = summary.replace(
        "mcintosh@gen-btc.com", "mcintosh@satoshis-plebs.com"
    )
    summary = summary.replace(
        "mcintosh@genwealthcrypto.com", "mcintosh@satoshis-plebs.com"
    )
    if music_credits:
        for credit in music_credits:
            credit["title"] = credit["title"].replace(
                "mcintosh@gen-btc.com", "mcintosh@satoshis-plebs.com"
            ).replace(
                "mcintosh@genwealthcrypto.com", "mcintosh@satoshis-plebs.com"
            )
            if credit.get("link"):
                credit["link"] = credit["link"].replace(
                    "mcintosh@gen-btc.com", "mcintosh@satoshis-plebs.com"
                ).replace(
                    "mcintosh@genwealthcrypto.com", "mcintosh@satoshis-plebs.com"
                )
        music_credits = normalize_music_credits(music_credits)
        music_credits = filter_music_credits(music_credits)
    if not summary:
        summary = "Summary not available for this episode."
    if not transcript:
        summary = (summary + "\n\nTranscript not available for this episode.").strip()

    episode_frontmatter = build_episode_frontmatter(args, episode_number, music_credits)
    transcript_frontmatter = build_transcript_frontmatter(episode_number)
    episode_content = f"{episode_frontmatter}\n{summary}\n"
    transcript_content = None
    if transcript:
        transcript_content = f"{transcript_frontmatter}\n{transcript}\n"

    episode_path = os.path.join(
        episodes_dir, f"episode-{format_episode_number(episode_number)}.md"
    )
    transcript_path = os.path.join(
        episodes_dir, f"episode-{episode_number}-transcript.md"
    )

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
        if not transcript:
            print("  transcript: none")
        print(f"[dry-run] would write: {episode_path}")
        if transcript_content:
            print(f"[dry-run] would write: {transcript_path}")
        else:
            print(f"[dry-run] would skip: {transcript_path}")
        return "dry-run"

    if os.path.exists(episode_path) and not args.force:
        warn(f"[WARN] Episode file already exists: {episode_path}")
        return "skipped"
    if transcript_content and os.path.exists(transcript_path) and not args.force:
        warn(f"[WARN] Transcript file already exists: {transcript_path}")
        return "skipped"

    write_file(episode_path, episode_content, args.force)
    if transcript_content:
        write_file(transcript_path, transcript_content, args.force)
    print(f"wrote {episode_path}")
    if transcript_content:
        print(f"wrote {transcript_path}")
    return "written"


def build_episode_frontmatter(args, episode_number, music_credits):
    lines = [
        "---",
        f'title: "{escape_yaml(args.title)}"',
        f"date: {args.date}",
        f"episode: {episode_number}",
        f'podhome_id: "{escape_yaml(args.podhome_id)}"',
    ]
    if args.btc_usd:
        lines.append(f'btc_price_usd: "{escape_yaml(args.btc_usd)}"')
    if args.btc_eur:
        lines.append(f'btc_price_eur: "{escape_yaml(args.btc_eur)}"')
    if args.block_height:
        lines.append(f'block_height: "{escape_yaml(args.block_height)}"')
    if music_credits:
        lines.append("music_credits:")
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
    parser.add_argument("--episodes", help="Episode list/range (RSS mode only)")
    parser.add_argument("--episode", type=int, help="Override auto-numbering")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    warn_messages = set()

    def warn(message):
        if message in warn_messages:
            return
        warn_messages.add(message)
        print(message, file=sys.stderr)

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    episodes_dir = os.path.join(repo_root, "content", "episodes")
    if not os.path.isdir(episodes_dir):
        print("content/episodes directory not found", file=sys.stderr)
        return 1

    if not args.from_rss:
        raise ValueError("RSS mode only: use --from-rss with --feed-url")
    if not args.feed_url:
        raise ValueError("--feed-url is required when using --from-rss")
    feed_xml = ""
    try:
        feed_xml = fetch_url(args.feed_url)
    except Exception as exc:
        warn(f"[WARN] Failed to fetch RSS feed: {exc}")
        return 0
    try:
        root = ET.fromstring(feed_xml)
    except ET.ParseError as exc:
        warn(f"[WARN] Failed to parse RSS feed XML: {exc}")
        return 0
    namespaces = {
        "itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
        "podcast": "https://podcastindex.org/namespace/1.0",
    }
    if args.episodes and args.episode:
        warn("[WARN] --episode ignored when --episodes is provided")

    if args.episodes:
        episode_list = parse_episode_list(args.episodes)
        if not episode_list:
            warn("[WARN] No valid episodes provided to --episodes")
            return 0
        summary_counts = {"written": 0, "skipped": 0, "failed": 0, "dry-run": 0}
        for episode_number in episode_list:
            result = process_rss_episode(
                root,
                namespaces,
                episodes_dir,
                args,
                warn,
                episode_number,
                bulk_mode=True,
            )
            summary_counts[result] = summary_counts.get(result, 0) + 1
        print(
            "bulk summary: "
            + ", ".join(
                f"{key}={value}"
                for key, value in summary_counts.items()
                if value
            )
        )
        return 0

    process_rss_episode(
        root,
        namespaces,
        episodes_dir,
        args,
        warn,
        args.episode,
        bulk_mode=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
