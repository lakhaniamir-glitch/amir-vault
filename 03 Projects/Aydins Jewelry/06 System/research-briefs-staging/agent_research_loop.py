#!/usr/bin/env python3
"""Daily research loop for agents. Reads YAML briefs, fetches sources,
synthesizes via OpenRouter (DeepSeek), writes findings + cumulative learnings,
alerts on critical.

Freshness filter (added 2026-06-08):
- RSS items: dropped if pubdate is older than RESEARCH_MAX_AGE_DAYS (default 14)
- RSS items with unparseable or missing pubdate: dropped (was leaking 2020-era content)
- Google News RSS: query now appends `when:7d` to bias toward fresh items
- HN already filters by created_at_i > 2 days ago
- Reddit already uses top.json?t=day
- LLM prompt now includes today's date + explicit "ignore items older than 30 days" rule
"""
import os
import sys
import json
import yaml
import time
import re
import hashlib
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path

BRIEFS_DIR = Path("/home/openclaw/.openclaw/agents/research-briefs")
LOG_FILE = Path("/home/openclaw/.openclaw/command-center/logs/agent_research.log")
TELEGRAM_ENV = Path("/home/openclaw/.openclaw/agents/beta/credentials/telegram.env")

UA = "AydinsResearchBot/1.0 (https://shopaydins.com; contact: ops@aydinsjewelry.com)"

MAX_AGE_DAYS = int(os.environ.get("RESEARCH_MAX_AGE_DAYS", "14"))


def log(msg):
    ts = datetime.now(timezone.utc).isoformat()
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a") as f:
        f.write(f"[{ts}] {msg}\n")
    print(f"[{ts}] {msg}")


def http_get(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def parse_pubdate(s):
    """Parse RFC 2822 / ISO 8601 / common RSS date formats. Returns aware datetime or None."""
    if not s:
        return None
    s = s.strip()
    # Try RFC 2822 (RSS): "Wed, 04 Jun 2026 14:30:00 +0000"
    try:
        dt = parsedate_to_datetime(s)
        if dt is not None:
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
    except Exception:
        pass
    # Try ISO 8601 (Atom): "2026-06-04T14:30:00Z" or "2026-06-04T14:30:00+00:00"
    try:
        s2 = s.replace("Z", "+00:00")
        dt = datetime.fromisoformat(s2)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        pass
    # Try just YYYY-MM-DD
    try:
        dt = datetime.strptime(s[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        pass
    return None


def is_fresh(item, max_days=None):
    """Return True if item is within max_days. RSS items with no/unparseable pubdate are dropped.
    Reddit/HN items are always considered fresh (their fetchers already filter by date)."""
    src = (item.get("source") or "")
    if src.startswith("Reddit:") or src.startswith("HackerNews"):
        return True
    max_days = max_days if max_days is not None else MAX_AGE_DAYS
    pub_str = item.get("pubdate", "")
    dt = parse_pubdate(pub_str)
    if dt is None:
        return False  # no/unparseable date -> drop (was the bug)
    age = datetime.now(timezone.utc) - dt
    return timedelta(seconds=0) <= age <= timedelta(days=max_days)


def fetch_rss(url):
    """Parse RSS/Atom feed via stdlib xml.etree. Drops items older than MAX_AGE_DAYS."""
    items = []
    dropped_old = 0
    try:
        body = http_get(url, timeout=15)
        root = ET.fromstring(body)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        # RSS 2.0
        for it in root.findall(".//item"):
            title = (it.findtext("title") or "").strip()
            link = (it.findtext("link") or "").strip()
            desc = (it.findtext("description") or "").strip()
            pub = (it.findtext("pubDate") or "").strip()
            if not (title and link):
                continue
            item = {"title": title[:200], "url": link, "summary": desc[:600], "source": "RSS:" + url, "pubdate": pub}
            if is_fresh(item):
                items.append(item)
            else:
                dropped_old += 1
        # Atom
        for it in root.findall(".//atom:entry", ns):
            title = (it.findtext("atom:title", namespaces=ns) or "").strip()
            link_el = it.find("atom:link", ns)
            link = link_el.get("href") if link_el is not None else ""
            summary = (it.findtext("atom:summary", namespaces=ns) or "").strip()
            pub = (it.findtext("atom:updated", namespaces=ns) or "").strip()
            if not (title and link):
                continue
            item = {"title": title[:200], "url": link, "summary": summary[:600], "source": "RSS:" + url, "pubdate": pub}
            if is_fresh(item):
                items.append(item)
            else:
                dropped_old += 1
        if dropped_old:
            log(f"  RSS {url} -> kept {len(items)} fresh, dropped {dropped_old} stale (>{MAX_AGE_DAYS}d)")
    except Exception as e:
        log(f"  RSS fetch failed {url}: {e}")
    return items


def fetch_reddit(subreddit, limit=15):
    """Reddit JSON API - no key needed. Already filtered to top-of-day."""
    items = []
    try:
        url = f"https://www.reddit.com/r/{subreddit}/top.json?t=day&limit={limit}"
        body = http_get(url, timeout=15)
        data = json.loads(body)
        for child in data.get("data", {}).get("children", []):
            d = child.get("data", {})
            if d.get("score", 0) < 20:
                continue
            items.append({
                "title": d.get("title", "")[:200],
                "url": "https://reddit.com" + d.get("permalink", ""),
                "summary": (d.get("selftext", "") or "")[:600],
                "source": f"Reddit:r/{subreddit}",
                "score": d.get("score", 0),
                "pubdate": datetime.fromtimestamp(d.get("created_utc", time.time()), tz=timezone.utc).isoformat(),
            })
    except Exception as e:
        log(f"  Reddit fetch failed {subreddit}: {e}")
    return items


def fetch_hn(query, limit=10):
    """Hacker News Algolia search. Already filtered to last 2 days."""
    items = []
    try:
        url = f"https://hn.algolia.com/api/v1/search?query={urllib.parse.quote(query)}&tags=story&numericFilters=created_at_i>{int(time.time()) - 86400 * 2}&hitsPerPage={limit}"
        body = http_get(url, timeout=15)
        data = json.loads(body)
        for hit in data.get("hits", []):
            if (hit.get("points") or 0) < 30:
                continue
            items.append({
                "title": hit.get("title", "")[:200],
                "url": hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID')}",
                "summary": "",
                "source": "HackerNews",
                "score": hit.get("points", 0),
                "pubdate": hit.get("created_at", ""),
            })
    except Exception as e:
        log(f"  HN fetch failed '{query}': {e}")
    return items


def fetch_news(query, limit=8):
    """Google News RSS via custom search. Appends `when:7d` to query to bias toward fresh."""
    items = []
    try:
        # Google News supports `when:Nd` operator for date filtering
        bounded_query = query + " when:7d"
        url = f"https://news.google.com/rss/search?q={urllib.parse.quote(bounded_query)}&hl=en-US&gl=US&ceid=US:en"
        items.extend(fetch_rss(url)[:limit])
    except Exception as e:
        log(f"  News fetch failed '{query}': {e}")
    return items


def dedupe_items(items):
    """Dedupe by URL hash."""
    seen = set()
    out = []
    for it in items:
        key = hashlib.sha1((it.get("url") or it.get("title", "")).encode()).hexdigest()
        if key in seen:
            continue
        seen.add(key)
        out.append(it)
    return out


def synthesize_via_llm(agent_name, focus, business_context, topics, items):
    """Call OpenRouter (DeepSeek) for structured synthesis."""
    if not items:
        return "## Daily Research — No fresh items in last %d days\n" % MAX_AGE_DAYS
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        log("OPENROUTER_API_KEY missing - skipping synthesis")
        return "## SYNTHESIS SKIPPED — OpenRouter key missing\n\n" + items_to_markdown(items)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    items_md = items_to_markdown(items)
    prompt = (
        "You are advising " + agent_name + ".\n\n"
        "TODAY'S DATE: " + today + "\n"
        "FRESHNESS WINDOW: items fetched from the last " + str(MAX_AGE_DAYS) + " days. "
        "If a title or summary clearly refers to an event MORE than 30 days before " + today + ", "
        "classify it IRRELEVANT regardless of topic match. We only want news that is actually new.\n\n"
        "FOCUS:\n" + focus + "\n\n"
        "BUSINESS CONTEXT (Aydins Jewelry):\n" + business_context + "\n\n"
        "TRACKED TOPICS:\n" + ", ".join(topics) + "\n\n"
        "Below are " + str(len(items)) + " items. Classify each into ONE of:\n"
        "- CRITICAL: something is actively breaking or changing strategy NOW. Action this week. MUST be new (last 14 days). Cite the date evidence in your reasoning.\n"
        "- ACTIONABLE: should be tested or adopted in next 2-4 weeks. Recent (last 30 days).\n"
        "- INFORMATIONAL: useful context, no action required. Recent context only.\n"
        "- IRRELEVANT: skip. Use this for items that are off-topic OR clearly old news (rehash of a 2020/2021/2022/2023/2024/2025 event).\n\n"
        "STALENESS HEURISTICS — classify as IRRELEVANT if any of these match:\n"
        "- Title mentions a year before " + today[:4] + " as the news event year\n"
        "- Summary describes a launch/policy/feature that already happened years ago\n"
        "- Article URL contains a year path before " + today[:4] + " (e.g., /2020/, /2021/, /2022/, /2023/, /2024/, /2025/)\n"
        "- Headline reads like an evergreen rehash (e.g., 'X Announces Y' for an announcement that is old hat)\n\n"
        "For each non-IRRELEVANT item, output:\n"
        "- [title](url) - 1-sentence why it matters for Aydins + 1-sentence recommended action.\n\n"
        "Structure the output:\n\n"
        "## CRITICAL\n(none if empty)\n\n"
        "## ACTIONABLE\n(none if empty)\n\n"
        "## INFORMATIONAL\n(none if empty)\n\n"
        "End with a 2-3 sentence executive summary that notes if any items were rejected as stale.\n\n"
        "ITEMS:\n" + items_md + "\n"
    )

    body = {
        "model": "deepseek/deepseek-v3.2",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": 4096,
    }
    url = "https://openrouter.ai/api/v1/chat/completions"
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(body).encode(),
            method="POST",
            headers={
                "Authorization": "Bearer " + api_key,
                "Content-Type": "application/json",
                "HTTP-Referer": "https://shopaydins.com",
                "X-Title": "Aydins Agent Research Loop",
            },
        )
        with urllib.request.urlopen(req, timeout=180) as r:
            data = json.loads(r.read())
        text = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        return text or "(empty response)"
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()[:400]
        log("  OpenRouter HTTPError " + str(e.code) + ": " + err_body)
        return "## SYNTHESIS FAILED — HTTP " + str(e.code) + ": " + err_body + "\n\n" + items_md
    except Exception as e:
        log("  OpenRouter error: " + str(e))
        return "## SYNTHESIS FAILED — " + str(e) + "\n\n" + items_md


def items_to_markdown(items):
    lines = []
    for it in items[:80]:  # cap at 80 to keep prompt manageable
        # Include pubdate in the line so LLM can use it for freshness check
        pub = it.get("pubdate", "?")
        lines.append(f"- [{it.get('title','?')}]({it.get('url','#')}) — {it.get('source','?')} | pubdate: {pub} | {it.get('summary','')[:200]}")
    return "\n".join(lines)


def extract_critical_section(synthesis):
    """Extract the CRITICAL section content for Telegram alert."""
    m = re.search(r"##\s*CRITICAL\s*\n(.*?)(?:##|$)", synthesis, re.DOTALL | re.IGNORECASE)
    if not m:
        return ""
    body = m.group(1).strip()
    if body.lower().startswith("(none") or not body or body == "none":
        return ""
    return body


def send_telegram(text):
    try:
        env_text = TELEGRAM_ENV.read_text()
        token = None
        for line in env_text.splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k, _, v = line.partition("=")
                if k.strip() in ("TELEGRAM_BOT_TOKEN", "BOT_TOKEN", "TOKEN"):
                    token = v.strip().strip(chr(34)).strip(chr(39))
                    break
        if not token:
            log("Telegram token missing")
            return
        chat_id = "8101774399"
        data = urllib.parse.urlencode({
            "chat_id": chat_id,
            "text": text[:3800],
            "disable_web_page_preview": "true",
        }).encode()
        req = urllib.request.Request("https://api.telegram.org/bot" + token + "/sendMessage", data=data)
        urllib.request.urlopen(req, timeout=15).read()
    except Exception as e:
        log("Telegram send failed: " + str(e))


def run_for_brief(brief_path):
    brief = yaml.safe_load(brief_path.read_text())
    agent = brief["agent"]
    log(f"=== RESEARCH RUN: {agent} (freshness window: {MAX_AGE_DAYS}d) ===")

    items = []
    sources = brief.get("sources", {})
    for rss_url in sources.get("rss", []):
        items.extend(fetch_rss(rss_url))
    for sub in sources.get("reddit", []):
        items.extend(fetch_reddit(sub))
    for q in sources.get("news_queries", []):
        items.extend(fetch_news(q))
    for q in sources.get("hackernews_queries", []):
        items.extend(fetch_hn(q))

    items = dedupe_items(items)
    log(f"  fetched {len(items)} unique FRESH items (window {MAX_AGE_DAYS}d)")

    synthesis = synthesize_via_llm(
        agent,
        brief.get("focus", ""),
        brief.get("business_context", ""),
        brief.get("topics", []),
        items,
    )

    output_dir = Path(brief.get("output_dir", f"/home/openclaw/.openclaw/vault/brands/aydins/research/{agent}/"))
    output_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    daily = output_dir / f"{today}.md"
    daily.write_text(f"# {agent} Research — {today}\n\nFresh items fetched: {len(items)} (window: last {MAX_AGE_DAYS} days)\n\n{synthesis}\n")

    # Append to cumulative learnings (newest first)
    learnings = output_dir / "learnings.md"
    existing = learnings.read_text() if learnings.exists() else f"# {agent} Cumulative Learnings\n\n"
    actionable_match = re.search(r"##\s*ACTIONABLE\s*\n(.*?)(?:##|$)", synthesis, re.DOTALL | re.IGNORECASE)
    actionable_body = actionable_match.group(1).strip() if actionable_match else ""
    critical_match = re.search(r"##\s*CRITICAL\s*\n(.*?)(?:##|$)", synthesis, re.DOTALL | re.IGNORECASE)
    critical_body = critical_match.group(1).strip() if critical_match else ""

    new_section = f"\n## {today}\n"
    if critical_body and not critical_body.lower().startswith("(none"):
        new_section += f"### Critical\n{critical_body}\n"
    if actionable_body and not actionable_body.lower().startswith("(none"):
        new_section += f"### Actionable\n{actionable_body}\n"
    if new_section.strip() != f"## {today}":
        header_end = existing.find("\n\n") + 2
        learnings.write_text(existing[:header_end] + new_section + existing[header_end:])

    # Alert on critical
    critical = extract_critical_section(synthesis)
    if critical:
        send_telegram(f"🚨 {agent} CRITICAL\n\n{critical[:3000]}\n\nFull: {daily}")
        log(f"  CRITICAL alert sent for {agent}")
    else:
        log(f"  no critical items, no Telegram sent")

    log(f"  wrote {daily}")


def main():
    # Load creds
    or_env = Path("/home/openclaw/.openclaw/agents/beta/credentials/openrouter.env")
    if or_env.exists():
        for line in or_env.read_text().splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

    if not BRIEFS_DIR.exists():
        log(f"No briefs dir at {BRIEFS_DIR} - nothing to do")
        return

    # Allow single-agent runs: python3 agent_research_loop.py beta-etsy
    only = sys.argv[1] if len(sys.argv) > 1 else None
    briefs = sorted(BRIEFS_DIR.glob("*.yaml"))
    if only:
        briefs = [b for b in briefs if b.stem == only]
        log(f"Single-agent mode: {only} ({len(briefs)} brief)")
    else:
        log(f"Found {len(briefs)} briefs")
    for b in briefs:
        try:
            run_for_brief(b)
        except Exception as e:
            log(f"FATAL on {b.name}: {e}")
            import traceback
            log(traceback.format_exc())


if __name__ == "__main__":
    main()
