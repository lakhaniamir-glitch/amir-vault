"""Generate 4 lifestyle images per product for the 88 new Etsy listings.

Strategy:
  1. Download Shopify product photo as SHOPIFY-REFERENCE.jpg
  2. Use Gemini 3.1 Flash Image with reference + scene prompt
  3. Generate 4 images per product: hero, image-2, image-3, image-4

Scene prompts are template-generated based on product attributes (material, color, feature).
"""
import base64, json, os, re, sys, time
from pathlib import Path
import urllib.request
import urllib.error

ROOT = Path("/home/openclaw/.openclaw")
ENV_FILE = ROOT / "agents/beta/credentials/gemini.env"
TARGETS_JSON = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-10/images-to-generate.json")
OUTPUT_ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-10/images")
MANIFEST = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-10/image-gen-manifest.json")
MODEL = "gemini-3.1-flash-image"

OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

def load_env():
    env = {}
    if not ENV_FILE.exists(): return env
    for raw in ENV_FILE.read_text().splitlines():
        line = raw.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env

ENV = load_env()
API_KEY = ENV.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

# Scene templates by category - one entry rotated by image position for variety
SCENE_LIBRARY = {
    "carbon_fiber_black": [
        "carbon fiber dashboard with brushed aluminum trim, racing-inspired cabin, warm tungsten interior light, charcoal driving glove resting nearby",
        "matte black race helmet on workshop bench, technical drawings in background, warm cool-blue mixed light, no people",
        "high-performance car interior at twilight, leather and carbon fiber accents, side mirror catching warm sunset light",
        "luxury garage with carbon fiber panel display, polished concrete floor, warm spotlights, masculine workshop mood",
    ],
    "diamond_luxury": [
        "rich black leather armchair and brass side table with crystal decanter, warm low light, charcoal suit cuff",
        "black tie formal event with marble bar top and crystal glassware out of focus, sharp tuxedo cuff",
        "executive office desk with leather blotter and gold pen, warm desk lamp, white French-cuff shirt sleeve",
        "private champagne tasting room with crystal flute and dark wood, soft chandelier light, formal mood",
    ],
    "wood_inlay_warm": [
        "warm woodworking workshop with leather tool roll and walnut shavings, late afternoon side light, denim sleeve cuff",
        "rustic cabin hearth with stacked firewood and hand-forged iron tools, warm fireplace glow, wool flannel cuff",
        "wooden writing desk with vintage typewriter and leather journal, sunlit window light, brown sweater sleeve",
        "old-growth forest floor with moss and tree bark texture, dappled sun light through canopy, calm natural mood",
    ],
    "wood_inlay_exotic": [
        "tropical hardwood workshop with exotic Koa boards and brass calipers, warm Hawaiian afternoon light, linen shirt cuff",
        "luxury safari camp tent corner with leather case and brass lantern on rustic wood crate, warm golden hour light",
        "high-end woodworking studio with exotic veneers laid out, focused task lighting, denim apron texture",
        "ethnographic museum collection wood display, soft museum lighting, deep brown wool jacket cuff",
    ],
    "rose_gold_elegant": [
        "rose gold accents on white marble countertop in modern apartment, soft morning daylight, white linen shirt sleeve",
        "champagne brunch table with rose gold cutlery and pink peonies, soft window light, beige cashmere sleeve",
        "boutique hotel lounge with blush velvet armchair and brass side table, warm low light, sophisticated mood",
        "art deco bar with rose gold trim and marble surface, evening glow, soft amber pendant light",
    ],
    "antler_outdoors": [
        "rustic hunting lodge mantel with antlers and lever-action rifle on display, warm fireplace light, wool sweater cuff",
        "outdoor camp scene with cast iron pan and weathered leather gloves on stump, late autumn afternoon light",
        "deer hunter's cabin with hand-tied flies and tackle box on wooden table, warm interior light, plaid flannel cuff",
        "mountain ridge view with worn binoculars and topographic map on rock, golden hour light, no people",
    ],
    "sapphire_blue": [
        "sapphire blue silk pocket square next to fountain pen on dark wood desk, warm tungsten desk lamp",
        "deep blue velvet jewelry display tray with magnifying loupe, jeweler's workbench, focused task lighting",
        "blue tile spa pool edge with rolled white towel and stone bowl, soft morning daylight, calm minimal mood",
        "navy suit jacket on wooden hanger with brass detail, gentleman's dressing room, warm side light",
    ],
    "spinner_workshop": [
        "industrial workshop with vintage spinning lathe and brass calipers on workbench, warm task lighting, leather apron",
        "high-end watchmaker's bench with precision tools and magnifier, focused desk light, white shirt sleeve",
        "fidget toy collection display on minimal desk, warm natural light, dark grey crewneck sleeve",
        "skateboard bearings and tools on concrete surface, urban garage vibe, warm overhead light",
    ],
    "ceramic_minimal_white": [
        "minimalist concrete loft kitchen with matte black espresso machine and white ceramic cup, soft north-facing daylight, dark henley sleeve",
        "modern bathroom counter with white ceramic vase and dried wildflowers, soft morning daylight, white linen towel",
        "Japanese tea ceremony setting with white ceramic bowl on dark wood, soft daylight, neutral aesthetic",
        "minimalist art gallery white wall with single sculpture, museum lighting, deep grey cashmere sleeve",
    ],
    "ceramic_lava_dark": [
        "rocky volcanic shore with weathered grey stones and crashing waves, overcast moody light, dark olive canvas jacket cuff",
        "geological museum display with raw obsidian and basalt samples, focused track lighting, deep charcoal sweater sleeve",
        "modern fireplace with stone surround and matte black accessories, warm fire glow, dark wool sleeve",
        "volcanic black sand beach at dusk, lone driftwood and stone, dramatic blue hour light",
    ],
    "damascus_blacksmith": [
        "active blacksmith forge with glowing embers and leather apron, warm orange firelight, denim sleeve cuff",
        "knife maker's workshop with damascus blades on dark cloth and bone-handled tools, focused warm lighting",
        "vintage forge bench with hammer and tongs on iron surface, dramatic side light, leather glove nearby",
        "metallurgy workshop with damascus pattern samples on slate, focused desk light, dark canvas apron texture",
    ],
    "fingerprint_couples": [
        "vintage wedding photo album open on white linen, soft morning daylight, warm sentimental mood",
        "anniversary love letter on parchment with vintage fountain pen, warm desk lamp, intimate quiet light",
        "couples ring box on velvet jewelry tray, soft pink lighting, soft focus rose petals nearby",
        "honeymoon scene with two coffee cups on hotel balcony at sunrise, warm golden light, no people",
    ],
    "default_masculine": [
        "tailored navy suit cuff and a tumbler of amber whiskey on dark walnut desk, warm late-afternoon side light, leather chair edge",
        "rich black leather armchair and brass side table with art deco lamp, warm low light, charcoal suit cuff",
        "dim speakeasy whiskey bar with crystal tumbler of bourbon on dark wood, warm low light, charcoal blazer cuff",
        "executive desk with leather blotter and brass paperweight, warm desk lamp, white French-cuff shirt sleeve",
    ],
}

def pick_scene_category(material: str, color: str, feature: str, title: str, tags: str) -> str:
    """Map product attributes to scene library category."""
    f = (feature or "").lower()
    t = (title or "").lower()
    tg = (tags or "").lower()
    blob = f"{f} {t} {tg}"

    if "carbon fiber" in blob: return "carbon_fiber_black"
    if "diamond" in blob and color.lower() == "black": return "diamond_luxury"
    if "diamond" in blob: return "diamond_luxury"
    if "sapphire" in blob: return "sapphire_blue"
    if "antler" in blob or "deer" in blob: return "antler_outdoors"
    if "lava rock" in blob or "lava" in blob: return "ceramic_lava_dark"
    if material.lower() == "ceramic" and color.lower() in {"white", "silver"}: return "ceramic_minimal_white"
    if material.lower() == "damascus steel": return "damascus_blacksmith"
    if "spinner" in blob or "fidget" in blob: return "spinner_workshop"
    if "koa" in blob or "olive wood" in blob or "snake wood" in blob: return "wood_inlay_exotic"
    if "wood" in blob: return "wood_inlay_warm"
    if color.lower() == "rose gold": return "rose_gold_elegant"
    if "fingerprint" in blob: return "fingerprint_couples"
    return "default_masculine"

def gemini_generate(prompt_text: str, reference_b64: str | None) -> bytes | None:
    """Call Gemini 3.1 Flash Image with optional reference."""
    parts = []
    if reference_b64:
        parts.append({
            "inline_data": {
                "mime_type": "image/jpeg",
                "data": reference_b64,
            }
        })
    parts.append({"text": prompt_text})
    body = {
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
        }
    }
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"    HTTP {e.code}: {e.read().decode()[:200]}")
        return None
    except Exception as e:
        print(f"    Error: {e}")
        return None

    candidates = data.get("candidates") or []
    if not candidates: return None
    parts = candidates[0].get("content", {}).get("parts", [])
    for p in parts:
        inline = p.get("inline_data") or p.get("inlineData")
        if inline and inline.get("data"):
            return base64.b64decode(inline["data"])
    return None

def download_reference(url: str) -> bytes | None:
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return r.read()
    except Exception as e:
        print(f"    Failed to download {url[:60]}: {e}")
        return None

PROMPT_TEMPLATE = """Create a hyperrealistic editorial product lifestyle photograph for an Etsy listing. The ring shown in the reference image must be preserved EXACTLY — same material color inlay shape proportions and details. Do not add stones, engravings, decoration, text, or features not present in the reference.

Scene: {scene}

Composition: ring placed naturally in the scene as a focal point but not centered like a product shot. 3/4 angle showing top face and inner band. Warm editorial lighting. Soft natural shadow underneath. No humans, no faces, no hands holding the ring. No text overlays, no logos. 2048×2048 square format. High quality photographic realism."""

def main():
    targets = json.loads(TARGETS_JSON.read_text())
    print(f"Loaded {len(targets)} products needing images")

    manifest = {"started": time.time(), "results": []}
    success_count = 0
    fail_count = 0

    for i, t in enumerate(targets, 1):
        codename = t["codename"]
        handle = t.get("handle") or codename.lower()
        data = t.get("data", {})
        title = data.get("title", "")
        tags = data.get("tags", "")
        ref_url = data.get("featured_image", "")

        # Extract material/color/feature from earlier processing (stored in data or derive)
        material = "Tungsten"
        for m in ["Ceramic", "Damascus", "Titanium", "14k Gold"]:
            if m.lower() in title.lower(): material = m; break
        color = "Black"
        for c in ["Rose Gold", "Yellow Gold", "Black", "Silver", "Gold", "Blue", "Green", "Red", "Purple", "Orange", "White"]:
            if c.lower() in (title.lower() + " " + tags.lower()): color = c; break
        feature = ""
        for f_key in ["diamond", "sapphire", "opal", "wood", "carbon fiber", "antler", "spinner",
                      "hammered", "brushed", "beveled", "domed", "groove", "lava rock", "meteorite"]:
            if f_key in (title.lower() + " " + tags.lower()):
                feature = f_key; break

        category = pick_scene_category(material, color, feature, title, tags)
        scenes = SCENE_LIBRARY[category]

        out_dir = OUTPUT_ROOT / handle
        out_dir.mkdir(parents=True, exist_ok=True)

        print(f"[{i}/{len(targets)}] {codename} → {handle[:50]}... ({category})")

        # Download Shopify reference once
        ref_bytes = None
        ref_b64 = None
        if ref_url:
            ref_path = out_dir / "SHOPIFY-REFERENCE.jpg"
            if not ref_path.exists():
                ref_bytes = download_reference(ref_url)
                if ref_bytes:
                    ref_path.write_bytes(ref_bytes)
            else:
                ref_bytes = ref_path.read_bytes()
            if ref_bytes:
                ref_b64 = base64.b64encode(ref_bytes).decode("ascii")

        per_product = {"codename": codename, "handle": handle, "category": category, "images": []}
        # Generate 4 images: hero, image-2, image-3, image-4
        for j, scene in enumerate(scenes):
            img_name = "hero.jpg" if j == 0 else f"image-{j+1}.jpg"
            img_path = out_dir / img_name
            if img_path.exists() and img_path.stat().st_size > 50000:
                per_product["images"].append({"name": img_name, "status": "exists_skipped"})
                continue
            prompt = PROMPT_TEMPLATE.format(scene=scene)
            img_bytes = gemini_generate(prompt, ref_b64)
            if img_bytes:
                img_path.write_bytes(img_bytes)
                per_product["images"].append({"name": img_name, "status": "ok", "bytes": len(img_bytes)})
                success_count += 1
                print(f"   ✓ {img_name} ({len(img_bytes)//1024}KB)")
            else:
                per_product["images"].append({"name": img_name, "status": "failed"})
                fail_count += 1
                print(f"   ✗ {img_name} failed")
            # Rate limit
            time.sleep(2)

        manifest["results"].append(per_product)
        # Update manifest periodically
        if i % 10 == 0:
            MANIFEST.write_text(json.dumps(manifest, indent=2))

    manifest["ended"] = time.time()
    manifest["success"] = success_count
    manifest["failed"] = fail_count
    MANIFEST.write_text(json.dumps(manifest, indent=2))
    print(f"\n=== DONE ===")
    print(f"Total products: {len(targets)}")
    print(f"Images generated successfully: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"Manifest: {MANIFEST}")

if __name__ == "__main__":
    main()
