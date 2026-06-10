"""Corrected top 100 strategy:
  Tier A: 50 codenames that ALREADY have AI-generated images (locked-in)
  Tier B: 50 more from sessions-by-product (top sessions, excluding Tier A) → need images
  Final: 100 listings, only 50 new images needed (down from 88).

Inputs:
  - gemini-full/ image handles
  - sessions-by-product-90d.csv
  - aydinsjewelry.myshopify.com (2).csv (handle ↔ codename + product details)
  - etsy-keep-list.csv (which are already on Etsy)

Outputs:
  - top100-final-tiered.csv (Tier A + Tier B)
  - top100-tier-report.md (readable summary)
  - tier-b-image-generation-list.txt (50 handles needing images)
"""
import csv, re, sys, os
from collections import defaultdict
from pathlib import Path

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

GEMINI_DIR = Path(r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\etsy\2026-06-04-revision\gemini-full")
HERO_DIR   = Path(r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\etsy\2026-06-04-revision\hero-images-existing")
SESS = Path(r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\01 Ideas & Validation\sessions-by-product-90d.csv")
SHOP = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")
KEEP = Path(r"C:\Users\amirl\Downloads\etsy-keep-list.csv")

OUT_CSV = Path(r"C:\Users\amirl\Downloads\top100-final-tiered.csv")
OUT_MD  = Path(r"C:\Users\amirl\Downloads\top100-tier-report.md")
OUT_TIER_B = Path(r"C:\Users\amirl\Downloads\tier-b-image-generation-list.txt")

# 1. Inventory existing image handles
generated_handles = set()
for f in os.listdir(GEMINI_DIR):
    if f.lower().endswith(('.jpg','.png','.jpeg')):
        generated_handles.add(os.path.splitext(f)[0])
print(f"Generated image handles in gemini-full: {len(generated_handles)}")

# 2. Read Shopify, build handle -> product info
shop_by_handle = {}
for r in csv.DictReader(open(SHOP, encoding="utf-8-sig", errors="replace")):
    h = (r.get("handle") or "").strip()
    if not h or h in shop_by_handle: continue
    sku = (r.get("sku") or "").strip()
    cn = sku.split("-")[0].upper() if sku else ""
    shop_by_handle[h] = {
        "codename": cn,
        "title": (r.get("title") or "").strip(),
        "product_type": (r.get("product_type") or "").strip(),
        "first_sku": sku,
        "first_price": (r.get("price") or "").strip(),
        "url": (r.get("absolute_product_url") or "").strip(),
        "featured_image": (r.get("featured_image_url") or "").strip(),
    }
print(f"Shopify handles: {len(shop_by_handle)}")

# 3. Read sessions, aggregate by handle
def num(x):
    try: return int((x or '0').replace(',',''))
    except: return 0

handle_sessions = {}
for r in csv.DictReader(open(SESS, encoding="utf-8-sig", errors="replace")):
    if (r.get("Landing page type") or "").lower() != "product": continue
    path = r.get("Landing page path","")
    m = re.match(r"^/products/([^/?#]+)", path)
    if not m: continue
    h = m.group(1)
    s = num(r.get("Sessions"))
    if s > handle_sessions.get(h, 0):
        handle_sessions[h] = s

# 4. Tier A: 50 handles with generated images. Match each to Shopify data.
keepers_codenames = set()
keepers_by_codename = {}
for r in csv.DictReader(open(KEEP, encoding="utf-8-sig")):
    keepers_codenames.add(r["codename"])
    keepers_by_codename[r["codename"]] = r

tier_a = []
for h in sorted(generated_handles):
    info = shop_by_handle.get(h)
    if not info:
        tier_a.append({"handle": h, "codename": "?", "title": "?", "product_type": "?",
                        "first_sku": "?", "first_price": "?", "url": "?",
                        "sessions": handle_sessions.get(h, 0),
                        "in_keepers": False, "image_path": str(GEMINI_DIR / f"{h}.jpg")})
        continue
    cn = info["codename"]
    tier_a.append({
        "handle": h, "codename": cn,
        "title": info["title"], "product_type": info["product_type"],
        "first_sku": info["first_sku"], "first_price": info["first_price"],
        "url": info["url"],
        "sessions": handle_sessions.get(h, 0),
        "in_keepers": cn in keepers_codenames,
        "etsy_lid": keepers_by_codename.get(cn, {}).get("lid", ""),
        "image_path": str(GEMINI_DIR / f"{h}.jpg"),
    })

# Sort tier_a by sessions desc
tier_a.sort(key=lambda x: -x["sessions"])

# 5. Tier B: 50 more from sessions ranking, excluding handles already in Tier A AND non-ring product types
tier_a_handles = {t["handle"] for t in tier_a}
sessions_sorted = sorted(handle_sessions.items(), key=lambda x: -x[1])

tier_b = []
non_ring_skipped = 0
for h, sess in sessions_sorted:
    if h in tier_a_handles: continue
    if h not in shop_by_handle: continue
    info = shop_by_handle[h]
    if info["product_type"].lower() not in {"rings", "ring"}:
        non_ring_skipped += 1; continue
    cn = info["codename"]
    tier_b.append({
        "handle": h, "codename": cn,
        "title": info["title"], "product_type": info["product_type"],
        "first_sku": info["first_sku"], "first_price": info["first_price"],
        "url": info["url"],
        "sessions": sess,
        "in_keepers": cn in keepers_codenames,
        "etsy_lid": keepers_by_codename.get(cn, {}).get("lid", ""),
        "image_path": "NEEDS_GENERATION",
    })
    if len(tier_b) == 50: break

print(f"\nTier A (with images): {len(tier_a)}")
print(f"Tier B (need images): {len(tier_b)}")
print(f"Non-ring handles skipped during Tier B build: {non_ring_skipped}")
print(f"Final total: {len(tier_a) + len(tier_b)}")

# Write unified CSV
all_rows = []
for i, t in enumerate(tier_a, 1):
    all_rows.append({"tier": "A", "rank": i, **t})
for i, t in enumerate(tier_b, 1):
    all_rows.append({"tier": "B", "rank": len(tier_a) + i, **t})

with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["tier","rank","handle","codename","title","product_type",
                                      "first_sku","first_price","url","sessions","in_keepers",
                                      "etsy_lid","image_path"])
    w.writeheader()
    w.writerows(all_rows)

# Write Tier B image generation list
with open(OUT_TIER_B, "w", encoding="utf-8") as f:
    f.write("# Tier B — 50 handles needing AI lifestyle hero image generation\n")
    f.write("# Each: pull Shopify featured_image_url as reference, run gpt-image-2 (per existing pattern), output 2048x2048 JPEG\n\n")
    for t in tier_b:
        f.write(f"{t['handle']}\t{t['codename']}\t{t['featured_image'] if 'featured_image' in t else shop_by_handle[t['handle']]['featured_image']}\n")

# Stats: how many keepers cover by Tier A
keepers_in_a = [t for t in tier_a if t["in_keepers"]]
keepers_in_b = [t for t in tier_b if t["in_keepers"]]
keepers_in_neither = keepers_codenames - {t["codename"] for t in tier_a} - {t["codename"] for t in tier_b}

# MD report
lines = [
    "# Top 100 Etsy Rings — Tier A + Tier B",
    "",
    f"_Strategy: 50 already-generated images (Tier A) + 50 more from session ranking (Tier B). 50 new images to generate, not 88._",
    "",
    "## Summary",
    f"- **Tier A (50, have AI image)**: 12 keepers already on Etsy, 38 new",
    f"- **Tier B (50, need AI image)**: top sessions-ranked products NOT in Tier A",
    f"- **24 keepers total**: {len(keepers_in_a)} are in Tier A, {len(keepers_in_b)} in Tier B, {len(keepers_in_neither)} in neither (need to be added to Tier B manually)",
    "",
    "## Tier A — 50 products with generated images (ready to use)",
    "",
    "| Rank | Codename | Sessions | $Price | Title | Keeper? |",
    "|---|---|---|---|---|---|",
]
for i, t in enumerate(tier_a, 1):
    lines.append(f"| {i} | {t['codename']} | {t['sessions']} | ${t['first_price']} | {t['title'][:55]} | {'✓' if t['in_keepers'] else ''} |")
lines += [
    "",
    "## Tier B — 50 products needing image generation",
    "",
    "| Rank | Codename | Sessions | $Price | Title | Keeper? |",
    "|---|---|---|---|---|---|",
]
for i, t in enumerate(tier_b, 1):
    lines.append(f"| {len(tier_a)+i} | {t['codename']} | {t['sessions']} | ${t['first_price']} | {t['title'][:55]} | {'✓' if t['in_keepers'] else ''} |")

if keepers_in_neither:
    lines += ["", "## Keepers NOT covered by either tier (need decision)",
              ""]
    for cn in sorted(keepers_in_neither):
        lines.append(f"- {cn}  (currently on Etsy as keeper LID {keepers_by_codename.get(cn,{}).get('lid')})")

OUT_MD.write_text("\n".join(lines), encoding="utf-8")
print(f"\nWrote: {OUT_CSV}")
print(f"Wrote: {OUT_MD}")
print(f"Wrote: {OUT_TIER_B}")
print()
print(f"Keepers in Tier A: {len(keepers_in_a)}  ({[t['codename'] for t in keepers_in_a]})")
print(f"Keepers in Tier B: {len(keepers_in_b)}  ({[t['codename'] for t in keepers_in_b]})")
print(f"Keepers in NEITHER: {len(keepers_in_neither)}  ({sorted(keepers_in_neither)})")
