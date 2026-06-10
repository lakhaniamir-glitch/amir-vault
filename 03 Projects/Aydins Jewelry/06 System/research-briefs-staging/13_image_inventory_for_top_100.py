"""Cross-reference top 100 Etsy rings (24 keepers + 76 from sessions) with locally-generated
AI lifestyle hero images. Produce inventory: HAVE / NEED for each.

Inputs:
  - etsy-keep-list.csv (24 keepers)
  - top100-by-sessions-verified.csv (top 100 by sessions, includes the 24 + 76 net new)
  - gemini-full/ (51 generated hero images named by handle)
  - hero-images-existing/ (50 handle folders, each with hero.jpg + SHOPIFY-REFERENCE.jpg)
  - aydinsjewelry.myshopify.com (2).csv (to map codename -> handle)

Output:
  - image-inventory-top-100.md (full inventory report)
  - image-inventory-top-100.csv (codename | rank | source | image_status | image_path)
"""
import csv, sys
from pathlib import Path
from collections import defaultdict

csv.field_size_limit(min(sys.maxsize, 2**31 - 1))

ROOT = Path(r"C:\Users\amirl\Documents\Amirs Command Center\03 Projects\Aydins Jewelry\etsy\2026-06-04-revision")
GEMINI_DIR = ROOT / "gemini-full"
HERO_DIR   = ROOT / "hero-images-existing"

KEEP    = Path(r"C:\Users\amirl\Downloads\etsy-keep-list.csv")
TOP100  = Path(r"C:\Users\amirl\Downloads\top100-by-sessions-verified.csv")
SHOP    = Path(r"C:\Users\amirl\Downloads\aydinsjewelry.myshopify.com (2).csv")

OUT_MD  = Path(r"C:\Users\amirl\Downloads\image-inventory-top-100.md")
OUT_CSV = Path(r"C:\Users\amirl\Downloads\image-inventory-top-100.csv")

# Inventory existing image files
gemini_handles = set()
for p in GEMINI_DIR.glob("*.jpg"):
    gemini_handles.add(p.stem)
for p in GEMINI_DIR.glob("*.png"):
    gemini_handles.add(p.stem)
hero_existing_handles = set()
for d in HERO_DIR.iterdir():
    if d.is_dir() and (d / "hero.jpg").exists():
        hero_existing_handles.add(d.name)

print(f"gemini-full handles with AI hero image: {len(gemini_handles)}")
print(f"hero-images-existing handles with hero.jpg: {len(hero_existing_handles)}")
all_image_handles = gemini_handles | hero_existing_handles
print(f"Total unique handles with image: {len(all_image_handles)}")

# Map codename -> handle from Shopify
codename_to_handle = {}
handle_to_codename = {}
with open(SHOP, encoding="utf-8-sig", errors="replace") as f:
    for r in csv.DictReader(f):
        sku = (r.get("sku") or "").strip()
        cn = sku.split("-")[0].upper() if sku else ""
        h = (r.get("handle") or "").strip()
        if cn and h and cn not in codename_to_handle:
            codename_to_handle[cn] = h
        if h and cn and h not in handle_to_codename:
            handle_to_codename[h] = cn

# Load top 100 (from sessions ranking — includes everyone)
top100 = []
with open(TOP100, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        top100.append(r)
print(f"Top 100 from sessions: {len(top100)}")

# Load 24 keepers
keepers = []
with open(KEEP, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        keepers.append(r)
keep_codenames = {k["codename"] for k in keepers}
print(f"Keepers (on Etsy): {len(keepers)}")

# Build unified top 100 list — combine keepers + sessions-top-100, dedupe by codename
unified = []
seen_codenames = set()
# Start with keepers (these are already on Etsy)
for k in keepers:
    cn = k["codename"]
    if cn in seen_codenames: continue
    seen_codenames.add(cn)
    unified.append({
        "codename": cn,
        "source": "keeper_on_etsy",
        "rank": k.get("rank","?"),
        "title": k.get("shop_title", ""),
        "net_sales": k.get("net_sales", ""),
        "lid": k["lid"],
    })
# Add sessions top 100 entries not already covered
for t in top100:
    cn = t["codename"]
    if cn in seen_codenames: continue
    seen_codenames.add(cn)
    unified.append({
        "codename": cn,
        "source": "new_from_sessions",
        "rank": t.get("rank","?"),
        "title": t.get("title", ""),
        "sessions": t.get("sessions", ""),
        "url": t.get("url", ""),
        "handle": t.get("handle", ""),
    })

# Cap at 100 total
unified = unified[:100]
print(f"Unified top 100 (keepers + new): {len(unified)}")

# Match each unified entry to image inventory
out_rows = []
have_count = 0
need_count = 0
for u in unified:
    cn = u["codename"]
    handle = u.get("handle") or codename_to_handle.get(cn, "")
    image_status = "NEED"
    image_path = ""
    if handle in gemini_handles:
        image_status = "HAVE (gemini-full)"
        image_path = str(GEMINI_DIR / f"{handle}.jpg")
    elif handle in hero_existing_handles:
        image_status = "HAVE (hero-images-existing)"
        image_path = str(HERO_DIR / handle / "hero.jpg")
    elif handle == "":
        image_status = "NEED (no handle mapping)"

    out_rows.append({
        "codename": cn,
        "rank": u["rank"],
        "source": u["source"],
        "shop_title": u["title"],
        "shop_handle": handle,
        "image_status": image_status,
        "image_path": image_path,
        "etsy_lid": u.get("lid", ""),
        "sessions_or_sales": u.get("sessions") or u.get("net_sales", ""),
    })
    if "HAVE" in image_status: have_count += 1
    else: need_count += 1

print(f"\n=== INVENTORY ===")
print(f"HAVE images: {have_count}")
print(f"NEED images: {need_count}")

# Write CSV
with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["codename","rank","source","shop_title","shop_handle",
                                       "image_status","image_path","etsy_lid","sessions_or_sales"])
    w.writeheader()
    w.writerows(out_rows)

# Write MD report
have_rows = [r for r in out_rows if "HAVE" in r["image_status"]]
need_rows = [r for r in out_rows if "NEED" in r["image_status"]]

lines = [
    "# Top 100 Etsy Rings — Image Inventory",
    "",
    f"_Built from: 24 keepers (on Etsy) + top by sessions = 100 ring listings._",
    "",
    f"## Summary",
    f"- Have AI-generated lifestyle hero image: **{have_count}**",
    f"- Need image generation: **{need_count}**",
    "",
    f"## Have images ({have_count})",
    "",
    "| Codename | Rank | Source | Handle | Image |",
    "|---|---|---|---|---|",
]
for r in have_rows:
    lines.append(f"| {r['codename']} | {r['rank']} | {r['source']} | {r['shop_handle']} | {r['image_status']} |")
lines += [
    "",
    f"## Need image generation ({need_count})",
    "",
    "| Codename | Rank | Source | Shopify Title | Handle |",
    "|---|---|---|---|---|",
]
for r in need_rows:
    lines.append(f"| {r['codename']} | {r['rank']} | {r['source']} | {r['shop_title'][:60]} | {r['shop_handle']} |")

OUT_MD.write_text("\n".join(lines), encoding="utf-8")
print(f"\nFiles written:")
print(f"  {OUT_CSV}")
print(f"  {OUT_MD}")
print()
print("=== KEEPERS WITH IMAGES ===")
for r in have_rows:
    if r['source'] == 'keeper_on_etsy':
        print(f"  {r['codename']:<14}  rank={r['rank']:<4}  {r['shop_title'][:50]}")
print()
print("=== KEEPERS NEEDING IMAGES ===")
for r in need_rows:
    if r['source'] == 'keeper_on_etsy':
        print(f"  {r['codename']:<14}  rank={r['rank']:<4}  {r['shop_title'][:50]}")
