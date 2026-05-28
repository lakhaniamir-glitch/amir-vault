"""Pull full structure + email content for 7 Klaviyo flows via REST API."""
import json
import time
import urllib.request
import urllib.error
import re
from html.parser import HTMLParser
from datetime import datetime

API_KEY = "pk_Wwq8mG_5d4a3f4d7071070312f7e7a4e4c667c057"
BASE_URL = "https://a.klaviyo.com/api"
HEADERS = {
    "Authorization": f"Klaviyo-API-Key {API_KEY}",
    "revision": "2024-10-15",
    "accept": "application/vnd.api+json",
}

FLOWS = [
    ("XQZ9kX", "Welcome Series", "LIVE"),
    ("TrNjjf", "Abandoned Cart", "LIVE"),
    ("QVt7Vu", "Customer Winback", "LIVE"),
    ("S3ZsM6", "Customer Thank You", "LIVE"),
    ("UiUnac", "Browse Abandonment", "LIVE"),
    ("W5AfdY", "Order Confirmation", "DRAFT"),
    ("WcmfHm", "Shipping Confirmation", "DRAFT"),
]

OUTPUT_PATH = r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\(C) Klaviyo Current Flow Audit.md"

failed_flows = []
total_emails = 0
start_time = time.time()


def api_get(path_or_url):
    """GET with retry on 429."""
    url = path_or_url if path_or_url.startswith("http") else f"{BASE_URL}{path_or_url}"
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(2)
                continue
            body = e.read().decode("utf-8", errors="replace")[:500]
            raise RuntimeError(f"HTTP {e.code} on {url}: {body}") from e
        except Exception as e:
            if attempt < 2:
                time.sleep(1)
                continue
            raise
    raise RuntimeError(f"Failed after retries: {url}")


def get_paginated(path):
    """Follow links.next pagination, return combined data list and combined included list."""
    all_data = []
    all_included = []
    url = f"{BASE_URL}{path}"
    while url:
        resp = api_get(url)
        data = resp.get("data")
        if isinstance(data, list):
            all_data.extend(data)
        elif data is not None:
            all_data.append(data)
        all_included.extend(resp.get("included", []) or [])
        nxt = (resp.get("links") or {}).get("next")
        url = nxt
    return all_data, all_included


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.in_skip = 0
        self.current_href = None
        self.in_a = False
        self.a_text = []
        # track style/script
        self.skip_tags = {"script", "style", "head", "meta", "title"}

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        attrs_d = dict(attrs)
        if tag in self.skip_tags:
            self.in_skip += 1
            return
        if tag == "a":
            self.in_a = True
            self.current_href = attrs_d.get("href", "")
            self.a_text = []
        elif tag == "img":
            alt = attrs_d.get("alt", "").strip()
            if alt:
                self.parts.append(f"[IMG: {alt}]")
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.parts.append("\n## ")
        elif tag in ("p", "div", "br", "tr", "li"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in self.skip_tags:
            if self.in_skip > 0:
                self.in_skip -= 1
            return
        if tag == "a":
            text = "".join(self.a_text).strip()
            href = self.current_href or ""
            if text or href:
                # Heuristic: if it looks like a button (short text + href) treat as button
                if href and text:
                    if len(text) < 50 and not text.startswith("http"):
                        self.parts.append(f"[BUTTON: \"{text}\" -> {href}]")
                    else:
                        self.parts.append(f"{text} ({href})")
                elif text:
                    self.parts.append(text)
            self.in_a = False
            self.a_text = []
            self.current_href = None
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6", "p", "div", "li"):
            self.parts.append("\n")

    def handle_data(self, data):
        if self.in_skip:
            return
        if self.in_a:
            self.a_text.append(data)
            return
        self.parts.append(data)

    def get_text(self):
        raw = "".join(self.parts)
        # normalize whitespace
        raw = re.sub(r"[ \t]+", " ", raw)
        raw = re.sub(r"\n{2,}", "\n", raw)
        lines = [ln.strip() for ln in raw.split("\n")]
        lines = [ln for ln in lines if ln]
        return "\n".join(lines)


def extract_text_and_codes(html):
    if not html:
        return "", []
    parser = TextExtractor()
    try:
        parser.feed(html)
    except Exception:
        pass
    text = parser.get_text()
    # Find ALL-CAPS words 4+ chars that look like discount codes
    codes = set()
    for match in re.findall(r"\b[A-Z][A-Z0-9]{3,}\b", text):
        if match in {"FREE", "SHOP", "OFF", "USA", "USD", "FAQ", "FAQS", "VIP", "NEW",
                     "SALE", "ONLY", "BOGO", "EARTH", "GOLD", "SILVER", "AYDINS",
                     "CLICK", "SHIPPING", "RETURN", "RETURNS"}:
            continue
        codes.add(match)
    # cap to 200 words
    words = text.split()
    if len(words) > 200:
        text = " ".join(words[:200]) + " ..."
    return text, sorted(codes)


def truncate_words(text, n=200):
    if not text:
        return ""
    words = text.split()
    if len(words) <= n:
        return text
    return " ".join(words[:n]) + " ..."


def fetch_flow(flow_id):
    """Return flow JSON, list of (action_obj, [message_objs]), and template lookup dict."""
    # Step 1: flow with actions
    flow_resp = api_get(f"/flows/{flow_id}/?include=flow-actions")
    flow_data = flow_resp.get("data", {})
    included_actions = {item["id"]: item for item in flow_resp.get("included", []) or []
                        if item.get("type") == "flow-action"}

    # Step 2: get all flow-actions (no include — not supported at collection)
    actions_data, _ = get_paginated(f"/flows/{flow_id}/flow-actions/")

    action_message_pairs = []
    def sort_key(a):
        attrs = a.get("attributes", {}) or {}
        return (attrs.get("position", 0) or 0, a.get("id", ""))
    sorted_actions = sorted(actions_data, key=sort_key)

    for action in sorted_actions:
        action_id = action.get("id")
        action_type_raw = ((action.get("attributes") or {}).get("type")
                           or (action.get("attributes") or {}).get("action_type") or "").lower()
        msgs = []
        # Only email/sms send actions have messages
        if "send" in action_type_raw or "email" in action_type_raw or "sms" in action_type_raw or "push" in action_type_raw:
            try:
                msg_resp, _ = get_paginated(f"/flow-actions/{action_id}/flow-messages/")
                msgs = msg_resp
            except Exception as e:
                print(f"   warn: couldn't fetch messages for action {action_id}: {e}")
        action_message_pairs.append((action, msgs))

    return flow_data, action_message_pairs


def fetch_message_with_template(message_id):
    """Get full message and template HTML."""
    resp = api_get(f"/flow-messages/{message_id}/?include=template")
    msg = resp.get("data", {})
    template = None
    for item in resp.get("included", []) or []:
        if item.get("type") == "template":
            template = item
            break
    template_id = None
    if template:
        template_id = template.get("id")
    elif (msg.get("relationships", {}).get("template", {}).get("data") or {}).get("id"):
        template_id = msg["relationships"]["template"]["data"]["id"]
    # Fetch full template if we have id (the included one may already include html)
    template_full = None
    if template_id:
        try:
            tresp = api_get(f"/templates/{template_id}/")
            template_full = tresp.get("data", {})
        except Exception as e:
            template_full = template  # fallback
    elif template:
        template_full = template
    return msg, template_full


def format_action(idx, action, messages):
    """Return markdown for an action. Updates global total_emails."""
    global total_emails
    out = []
    attrs = action.get("attributes", {}) or {}
    action_type = attrs.get("type") or attrs.get("action_type") or "Unknown"
    action_id = action.get("id", "")
    settings = attrs.get("settings", {}) or {}

    type_lower = (action_type or "").lower()

    if "send" in type_lower and "email" in type_lower or type_lower == "send-email" or type_lower == "send_email":
        kind = "Email"
    elif "time-delay" in type_lower or "time_delay" in type_lower or "delay" in type_lower:
        kind = "Time Delay"
    elif "conditional-split" in type_lower or "conditional_split" in type_lower:
        kind = "Conditional Split"
    elif "trigger-split" in type_lower or "trigger_split" in type_lower:
        kind = "Trigger Split"
    elif "update-profile" in type_lower or "update_profile" in type_lower:
        kind = "Update Profile"
    elif "send-sms" in type_lower or "send_sms" in type_lower:
        kind = "SMS"
    elif "send-push" in type_lower or "send_push" in type_lower:
        kind = "Push"
    elif "webhook" in type_lower:
        kind = "Webhook"
    else:
        kind = action_type

    if kind == "Email":
        # We expect 1 message per email action typically
        for msg in messages:
            mid = msg.get("id", "")
            try:
                full_msg, template = fetch_message_with_template(mid)
            except Exception as e:
                out.append(f"### Action {idx}: Email — ERROR fetching message {mid}: {e}")
                continue
            mattrs = full_msg.get("attributes", {}) or {}
            content = mattrs.get("content", {}) or {}
            subject = content.get("subject") or mattrs.get("name") or ""
            preview = content.get("preview_text", "") or ""
            from_email = content.get("from_email", "")
            from_label = content.get("from_label", "")
            reply_to = content.get("reply_to_email", "") or ""
            smart_sending = mattrs.get("smart_sending_enabled", None)
            if smart_sending is None:
                smart_sending = mattrs.get("send_options", {}).get("use_smart_sending", None) if isinstance(mattrs.get("send_options"), dict) else None

            template_id = ""
            template_name = ""
            html_body = ""
            if template:
                template_id = template.get("id", "")
                tattrs = template.get("attributes", {}) or {}
                template_name = tattrs.get("name", "")
                html_body = tattrs.get("html", "") or ""

            text_body, codes = extract_text_and_codes(html_body)

            out.append(f"### Action {idx}: Email — Subject: \"{subject}\"")
            out.append(f"- Message ID: {mid}")
            out.append(f"- Template ID: {template_id}")
            out.append(f"- Template Name: {template_name}")
            out.append(f"- Preview: \"{preview}\"")
            from_str = f"{from_email}" + (f" ({from_label})" if from_label else "")
            out.append(f"- From: {from_str}")
            if reply_to:
                out.append(f"- Reply-To: {reply_to}")
            out.append(f"- Smart Sending: {smart_sending}")
            if codes:
                out.append(f"- Discount/Codes detected: {', '.join(codes)}")
            out.append("- **Body extracted:**")
            out.append("")
            out.append("```")
            out.append(text_body if text_body else "(no body content extracted)")
            out.append("```")
            out.append("")
            total_emails += 1

    elif kind == "Time Delay":
        # delay format
        units = settings.get("units") or attrs.get("delay_units") or ""
        value = settings.get("value") or attrs.get("delay_value") or attrs.get("delay_seconds") or ""
        delay_str = ""
        if value and units:
            delay_str = f"{value} {units}"
        elif "delay_seconds" in attrs:
            secs = attrs.get("delay_seconds", 0) or 0
            if secs >= 86400:
                delay_str = f"{secs // 86400} days"
            elif secs >= 3600:
                delay_str = f"{secs // 3600} hours"
            elif secs >= 60:
                delay_str = f"{secs // 60} minutes"
            else:
                delay_str = f"{secs} seconds"
        else:
            # dump settings as fallback
            delay_str = json.dumps(settings) if settings else "(no delay info)"
        out.append(f"### Action {idx}: Time Delay — {delay_str}")
        out.append(f"- Action ID: {action_id}")
        out.append(f"- Raw settings: `{json.dumps(settings)}`")
        out.append("")

    elif kind in ("Conditional Split", "Trigger Split"):
        out.append(f"### Action {idx}: {kind}")
        out.append(f"- Action ID: {action_id}")
        # Try to surface logic
        condition = attrs.get("condition") or settings.get("condition") or settings
        out.append(f"- Logic: `{json.dumps(condition)[:1000]}`")
        out.append("")

    elif kind == "Update Profile":
        out.append(f"### Action {idx}: Update Profile")
        out.append(f"- Action ID: {action_id}")
        out.append(f"- Settings: `{json.dumps(settings)[:500]}`")
        out.append("")

    else:
        out.append(f"### Action {idx}: {kind}")
        out.append(f"- Action ID: {action_id}")
        out.append(f"- Raw attrs: `{json.dumps(attrs)[:500]}`")
        out.append("")

    return "\n".join(out)


def get_trigger_info(flow_data):
    """Extract trigger metric/list/filter info from flow data."""
    attrs = flow_data.get("attributes", {}) or {}
    trigger_type = attrs.get("trigger_type", "")
    # Klaviyo flow definition often in 'definition'
    definition = attrs.get("definition", {}) or {}
    triggers = definition.get("triggers", []) or []
    customer_filter = definition.get("customer_filter") or definition.get("profile_filter")

    pieces = []
    if trigger_type:
        pieces.append(f"Trigger Type: {trigger_type}")
    for t in triggers:
        ttype = t.get("type", "") or t.get("trigger_type", "")
        if ttype:
            pieces.append(f"- {ttype}")
        # metric
        metric_id = (t.get("metric_id") or
                     ((t.get("metric") or {}).get("id") if isinstance(t.get("metric"), dict) else None))
        if metric_id:
            pieces.append(f"  - metric_id: {metric_id}")
        list_id = t.get("list_id") or ((t.get("list") or {}).get("id") if isinstance(t.get("list"), dict) else None)
        if list_id:
            pieces.append(f"  - list_id: {list_id}")
        tf = t.get("trigger_filter") or t.get("filters")
        if tf:
            pieces.append(f"  - trigger filter: `{json.dumps(tf)[:400]}`")
    if customer_filter:
        pieces.append(f"- Profile/Customer Filter: `{json.dumps(customer_filter)[:600]}`")

    if not pieces:
        # dump raw
        return f"`{json.dumps(definition)[:800] or json.dumps(attrs)[:800]}`"
    return "\n".join(pieces)


def main():
    global failed_flows
    md = []
    md.append("# Klaviyo Current Flow Audit")
    md.append(f"Pulled: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    md.append("")

    for i, (flow_id, name, status) in enumerate(FLOWS, 1):
        print(f"Fetching flow {i}: {name} ({flow_id})...")
        md.append(f"## Flow {i}: {name} — {status}")
        md.append(f"- ID: {flow_id}")
        try:
            flow_data, action_pairs = fetch_flow(flow_id)
        except Exception as e:
            md.append(f"- ERROR fetching flow: {e}")
            md.append("")
            failed_flows.append((flow_id, name, str(e)))
            print(f"  FAILED: {e}")
            continue

        attrs = flow_data.get("attributes", {}) or {}
        flow_name = attrs.get("name", name)
        flow_status = attrs.get("status", status)
        archived = attrs.get("archived", False)
        created = attrs.get("created", "")
        updated = attrs.get("updated", "")
        md.append(f"- Klaviyo Name: {flow_name}")
        md.append(f"- Status: {flow_status} (archived: {archived})")
        md.append(f"- Created: {created} / Updated: {updated}")
        md.append("- Trigger:")
        md.append(get_trigger_info(flow_data))
        md.append("")

        if not action_pairs:
            md.append("(No actions found)")
            md.append("")
            continue

        for idx, (action, messages) in enumerate(action_pairs, 1):
            try:
                md.append(format_action(idx, action, messages))
            except Exception as e:
                md.append(f"### Action {idx}: ERROR — {e}")
                md.append("")
        md.append("")
        md.append("---")
        md.append("")

    # summary
    runtime = time.time() - start_time
    md.append("## Run Summary")
    md.append(f"- Total flows requested: {len(FLOWS)}")
    md.append(f"- Failed flows: {len(failed_flows)}")
    if failed_flows:
        for fid, name, err in failed_flows:
            md.append(f"  - {name} ({fid}): {err}")
    md.append(f"- Total emails pulled: {total_emails}")
    md.append(f"- Runtime: {runtime:.1f}s")

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print(f"\nDone. File: {OUTPUT_PATH}")
    print(f"Total emails: {total_emails}")
    print(f"Failed flows: {len(failed_flows)}")
    print(f"Runtime: {runtime:.1f}s")


if __name__ == "__main__":
    main()
