"""Test correct image generation for ONE product (HALSTEN) with verified reference."""
import base64, json, os, sys, time
from pathlib import Path
import urllib.request

ROOT = Path("/home/openclaw/.openclaw")
ENV_FILE = ROOT / "agents/beta/credentials/gemini.env"
OUTPUT_DIR = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-10-test-halsten")
MODEL = "gemini-3.1-flash-image"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# HALSTEN data
HANDLE = "halsten-platinum-inlaid-beveled-tungsten-carbide-wedding-ring-6mm-or-8mm"
CODENAME = "HALSTEN"
REF_URL = "https://shopaydins.com/cdn/shop/files/halsten-tungsten-ring-inlay-beveled-halsten-6-4-aydins-jewelry-907891.jpg?v=1776798520&width=2048"
PRODUCT_DESC = ("HALSTEN — Tungsten Carbide Wedding Ring with a 2mm wide band of solid white "
                "Platinum inlaid into the center. Polished Tungsten Carbide base with platinum inlay. "
                "Available in 6mm and 8mm widths.")

# 4 scenes for HALSTEN
SCENES = [
    "tailored navy suit cuff with leather watch strap on dark walnut desk, vintage compass and brass-trimmed leather notebook visible, warm late-afternoon side light through window blinds, masculine editorial mood, no humans",
    "high-end watchmaker's workbench with precision tools loupe and brass parts holder, focused warm task light on the worn leather surface, no humans",
    "executive office desk with leather blotter and brass paperweight on dark mahogany, warm desk lamp glow, single white French-cuff shirt sleeve at edge of frame, no humans no faces",
    "minimalist concrete loft kitchen with matte black espresso machine and white ceramic cup, soft north-facing daylight, dark henley sleeve at edge of frame, no humans no faces",
]

def load_env():
    env = {}
    for raw in ENV_FILE.read_text().splitlines():
        line = raw.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env

ENV = load_env()
API_KEY = ENV.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

# Step 1: Download reference image and VERIFY it succeeded
print(f"\n=== Step 1: Download reference from {REF_URL[:80]}... ===")
ref_path = OUTPUT_DIR / "SHOPIFY-REFERENCE.jpg"
req = urllib.request.Request(REF_URL, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        ref_bytes = r.read()
    if len(ref_bytes) < 5000:
        print(f"FAIL: reference too small ({len(ref_bytes)} bytes)")
        sys.exit(1)
    ref_path.write_bytes(ref_bytes)
    print(f"OK: reference downloaded {len(ref_bytes)} bytes -> {ref_path}")
except Exception as e:
    print(f"FAIL: {e}")
    sys.exit(1)

ref_b64 = base64.b64encode(ref_bytes).decode("ascii")

# Step 2: For each scene, call Gemini with reference + scene + product description
def gemini_call(prompt_text, ref_b64):
    parts = [
        {"inline_data": {"mime_type": "image/jpeg", "data": ref_b64}},
        {"text": prompt_text},
    ]
    body = {"contents": [{"parts": parts}],
            "generationConfig": {"responseModalities": ["IMAGE"]}}
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode()[:200]}")
        return None
    candidates = data.get("candidates") or []
    if not candidates: return None
    for p in candidates[0].get("content", {}).get("parts", []):
        inline = p.get("inline_data") or p.get("inlineData")
        if inline and inline.get("data"):
            return base64.b64decode(inline["data"])
    return None

PROMPT_TEMPLATE = """The ring in the reference image is the {product_desc}

Create an editorial product lifestyle photograph that PRESERVES THE RING EXACTLY as shown in the reference image. Same material (Tungsten Carbide), same platinum inlay band in center, same polished finish, same proportions, same beveled edges. Do NOT add stones, engravings, or decorations not in the reference. Do NOT change the ring.

Scene context: {scene}

Composition: place the ring naturally in the scene at 3/4 angle showing the top face and inner band of the ring. The ring is the focal point. Warm editorial lighting with soft natural shadow. No humans, no faces, no hands. No text overlays. 2048x2048 square format. Photorealistic editorial style."""

for i, scene in enumerate(SCENES):
    name = "hero.jpg" if i == 0 else f"image-{i+1}.jpg"
    print(f"\n=== Generating {name} (scene: {scene[:60]}...) ===")
    prompt = PROMPT_TEMPLATE.format(product_desc=PRODUCT_DESC, scene=scene)
    img_bytes = gemini_call(prompt, ref_b64)
    if img_bytes:
        out = OUTPUT_DIR / name
        out.write_bytes(img_bytes)
        print(f"  OK: {len(img_bytes)//1024}KB -> {out}")
    else:
        print(f"  FAIL")
    time.sleep(2)

print(f"\n=== Done. Output in {OUTPUT_DIR} ===")
print(f"Files:")
for f in sorted(OUTPUT_DIR.iterdir()):
    print(f"  {f.name}: {f.stat().st_size//1024}KB")
