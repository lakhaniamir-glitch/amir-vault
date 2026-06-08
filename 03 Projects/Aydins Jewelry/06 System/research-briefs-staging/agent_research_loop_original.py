#!/usr/bin/env python3
"""Daily research loop for agents. Reads YAML briefs, fetches sources,
synthesizes via Gemini, writes findings + cumulative learnings, alerts on critical."""
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
from pathlib import Path

BRIEFS_DIR = Path("/home/openclaw/.openclaw/agents/research-briefs")
LOG_FILE = Path("/home/openclaw/.openclaw/command-center/logs/agent_research.log")
TELEGRAM_ENV = Path("/home/openclaw/.openclaw/agents/beta/credentials/telegram.env")

UA = "AydinsResearchBot/1.0 (https://shopaydins.com; contact: ops@aydinsjewelry.com)"


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


def fetch_rss(url):
    """Parse RSS/Atom feed via stdlib xml.etree."""
    items = []
    try:
        body = http_get(url, timeout=15)
        root = ET.fromstring(body)
        # Handle RSS 2.0 (rss/channel/item) and Atom (feed/entry)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        # Try RSS
        for it in root.findall(".//item"):
            title = (it.findtext("title") or "").strip()
            link = (it.findtext("link") or "").strip()
            desc = (it.findtext("description") or "").strip()
            pub = (it.findtext("pubDate") or "").strip()
            if title and link:
                items.append({"title": title[:200], "url": link, "summary": desc[:600], "source": "RSS:" + url, "pubdate": pub})
        # Try Atom
        for it in root.findall(".//atom:entry", ns):
            title = (it.findtext("atom:title", namespaces=ns) or "").strip()
            link_el = it.find("atom:link", ns)
            link = link_el.get("href") if link_el is not None else ""
            summary = (it.findtext("atom:summary", namespaces=ns) or "").strip()
            pub = (it.findtext("atom:updated", namespaces=ns) or "").strip()
            if title and link:
                items.append({"title": title[:200], "url": link, "summary": summary[:600], "source": "RSS:" + url, "pubdate": pub})
    except Exception as e:
        log(f"  RSS fetch failed {url}: {e}")
    return items


def fetch_reddit(subreddit, limit=15):
    """Reddit JSON API - no key needed."""
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
            })
    except Exception as e:
        log(f"  Reddit fetch failed {subreddit}: {e}")
    return items


def fetch_hn(query, limit=10):
    """Hacker News Algolia search."""
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
            })
    except Exception as e:
        log(f"  HN fetch failed '{query}': {e}")
    return items


def fetch_news(query, limit=8):
    """Google News RSS via custom search."""
    items = []
    try:
        url = f"https://news.google.com/rss/search?q={urllib.parse.quote(query)}&hl=en-US&gl=US&ceid=US:en"
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
        return "## Daily Research \u2014 No new items in last 24 hours\n"
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        log("OPENROUTER_API_KEY missing - skipping synthesis")
        return "## SYNTHESIS SKIPPED \u2014 OpenRouter key missing\n\n" + items_to_markdown(items)

    items_md = items_to_markdown(items)
    prompt = (
        "You are advising " + agent_name + ".\n\n"
        "FOCUS:\n" + focus + "\n\n"
        "BUSINESS CONTEXT (Aydins Jewelry):\n" + business_context + "\n\n"
        "TRACKED TOPICS:\n" + ", ".join(topics) + "\n\n"
        "Below are " + str(len(items)) + " items collected in the last 24 hours. Classify each into ONE of:\n"
        "- CRITICAL: something is actively breaking or changing strategy NOW. Action this week.\n"
        "- ACTIONABLE: should be tested or adopted in next 2-4 weeks.\n"
        "- INFORMATIONAL: useful context, no action required.\n"
        "- IRRELEVANT: skip (not related to focus + business).\n\n"
        "For each non-IRRELEVANT item, output:\n"
        "- [title](url) - 1-sentence why it matters for Aydins + 1-sentence recommended action.\n\n"
        "Structure the output:\n\n"
        "## CRITICAL\n(none if empty)\n\n"
        "## ACTIONABLE\n(none if empty)\n\n"
        "## INFORMATIONAL\n(none if empty)\n\n"
        "End with a 2-3 sentence executive summary.\n\n"
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
        return "## SYNTHESIS FAILED \u2014 HTTP " + str(e.code) + ": " + err_body + "\n\n" + items_md
    except Exception as e:
        log("  OpenRouter error: " + str(e))
        return "## SYNTHESIS FAILED \u2014 " + str(e) + "\n\n" + items_md


def items_to_markdown(items):
    lines = []
    for it in items[:80]:  # cap at 80 to keep prompt manageable
        lines.append(f"- [{it.get('title','?')}]({it.get('url','#')}) — {it.get('source','?')}: {it.get('summary','')[:200]}")
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
    log(f"=== RESEARCH RUN: {agent} ===")

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
    log(f"  fetched {len(items)} unique items")

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
    daily.write_text(f"# {agent} Research — {today}\n\nItems fetched: {len(items)}\n\n{synthesis}\n")

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
        # only append if there's actual content
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

    briefs = sorted(BRIEFS_DIR.glob("*.yaml"))
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
