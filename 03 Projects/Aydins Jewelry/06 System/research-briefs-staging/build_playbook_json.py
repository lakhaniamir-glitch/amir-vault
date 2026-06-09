"""Build a Listing-ID -> {title, tags, description, price, var_sku} JSON from listings-corrected-FINAL.csv.
Also strips SKU/codename pollution from titles (configurable).

Output: C:\\Users\\amirl\\Downloads\\playbook-by-listingid.json
"""
import csv, json, re
from pathlib import Path

SRC = Path(r"C:\Users\amirl\Downloads\listings-corrected-FINAL.csv")
OUT = Path(r"C:\Users\amirl\Downloads\playbook-by-listingid.json")

STRIP_SKU_POLLUTION = True  # Set False to push raw

# Codename patterns to strip from titles when they appear as standalone tokens.
# Format: " Ring CODENAME, " -> " Ring, "  (matches codename right after "Ring " word)
# Also handles capitalized versions like "Maui", "Jdtr709", "Aytr022", "Tr210"
SKU_REGEX = re.compile(r"\s+(?:Ring|Band)\s+([A-Z][a-z]+\d*|[A-Z]+\d+|[A-Z]{2,}-?\d+|[A-Z]{4,})(\s*[,.]?\s*)", re.IGNORECASE)

def strip_pollution(title: str) -> str:
    """Removes ' Ring Maui,' -> ' Ring,' and ' Ring Jdtr709,' -> ' Ring,'."""
    # Specific known patterns first
    # Match: "<word like 'Ring' or 'Band'> <Capitalized codename token>" followed by punctuation/space
    out = title
    # Pattern: codename appears AFTER "Tungsten Ring" or "Titanium Ring" etc., before next comma
    # e.g. "8mm Silver Mens Tungsten Ring Maui, Personalized" -> "8mm Silver Mens Tungsten Ring, Personalized"
    out = re.sub(
        r"(Tungsten Ring|Titanium Ring|Damascus Ring|Damascus Steel Ring|Tungsten Band|Titanium Band|Wedding Ring|Wedding Band)\s+([A-Z][a-zA-Z]*\d*)(\s*,)",
        r"\1\3",
        out,
    )
    # Collapse double spaces
    out = re.sub(r"\s{2,}", " ", out).strip()
    return out

with open(SRC, encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

playbook = {}
sku_strip_count = 0
sample_strips = []

for r in rows:
    lid = (r.get("Listing ID") or "").strip()
    if not lid:
        continue
    title_raw = (r.get("Title") or "").strip()
    title_clean = strip_pollution(title_raw) if STRIP_SKU_POLLUTION else title_raw
    if title_raw != title_clean:
        sku_strip_count += 1
        if len(sample_strips) < 6:
            sample_strips.append((title_raw[:80], title_clean[:80]))

    tags = (r.get("Tags") or "").strip().rstrip(",")  # drop trailing comma
    desc = (r.get("Description") or "").strip()
    price = (r.get("Price") or "").strip()
    var_sku = (r.get("Var SKU") or "").strip()

    playbook[lid] = {
        "title": title_clean,
        "title_orig": title_raw,
        "tags": tags,
        "description": desc,
        "price": price,
        "var_sku": var_sku,
    }

OUT.write_text(json.dumps(playbook, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Listings written: {len(playbook)}")
print(f"Titles with SKU pollution stripped: {sku_strip_count}")
print(f"Output: {OUT}")
print()
print("=== Sample strips ===")
for orig, clean in sample_strips:
    print(f"  BEFORE: {orig!r}")
    print(f"  AFTER:  {clean!r}")
    print()
