"""Strip SKU codes from listing titles.
Keep named brand codenames (MAUI, HAYDEN, FERRARI, etc.) - those are intentional product names.
Strip internal SKU codes (AYTR140, JDTR709, TR729, LST*, AYSSS*, FPR*).
"""
import csv, re
from pathlib import Path

ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04")

# Patterns that ARE internal SKU codes (must strip from titles)
SKU_PATTERN = re.compile(
    r"\s*\b("
    r"Aytr\d+"           # Aytr140
    r"|Jdtr\d+"          # Jdtr709
    r"|Tr\d+"            # Tr729
    r"|Aysss[a-z]*"      # Aysss / Ayssscl / Ayssstag
    r"|Aysstag[a-z]*"    # Aysstagp etc
    r"|Lst\d+"           # Lst4512054275 (my fallback codename)
    r"|Fpr[A-Za-z]*\d*"  # Fpr-anything
    r")\b",
    re.IGNORECASE,
)

# Clean up tail patterns that get awkward after stripping
def clean_title(title):
    if not title: return title
    new = SKU_PATTERN.sub("", title)
    # Collapse double commas and orphan spaces from stripped tokens
    new = re.sub(r"\s*,\s*,", ",", new)
    new = re.sub(r"\s+", " ", new)
    # Collapse pattern like "Ring , " -> "Ring,"
    new = re.sub(r"\s+,", ",", new)
    # Fix accidental "Ring  Personalized" -> "Ring, Personalized" if comma was eaten
    new = re.sub(r"Ring\s+Personalized", "Ring, Personalized", new)
    # Trim
    new = new.strip(", ").strip()
    return new

for fname in ["listings-corrected.csv", "new-shopify-listings.csv"]:
    path = ROOT / fname
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    fixed = 0
    samples = []
    for r in rows:
        title = r.get("Title", "")
        if not title: continue
        if SKU_PATTERN.search(title):
            new = clean_title(title)
            if new != title:
                r["Title"] = new
                fixed += 1
                if len(samples) < 5:
                    samples.append((title, new))

    tmp = path.with_suffix(".csv.tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(path)

    print(f"\n=== {fname} ===")
    print(f"  titles cleaned: {fixed}")
    if samples:
        print(f"\n  samples:")
        for old, new in samples:
            print(f"    OLD: {old}")
            print(f"    NEW: {new}")
            print()

# Verify no SKU codes remain
print("\n=== POST-CHECK ===")
for fname in ["listings-corrected.csv", "new-shopify-listings.csv"]:
    path = ROOT / fname
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    remaining = sum(1 for r in rows if r.get("Title") and SKU_PATTERN.search(r["Title"]))
    print(f"  {fname}: {remaining} titles still have SKU patterns")
