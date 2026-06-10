"""4 distinct shot types for HALSTEN test.
Hero (editorial), Hand (on man's ring finger), Macro close-up, Lifestyle scene.
"""
import base64, json, os, sys, time
from pathlib import Path
import urllib.request

ROOT = Path("/home/openclaw/.openclaw")
ENV_FILE = ROOT / "agents/beta/credentials/gemini.env"
OUTPUT_DIR = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-10-test-halsten")
MODEL = "gemini-3.1-flash-image"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PRODUCT_DESC = ("HALSTEN — Tungsten Carbide Wedding Ring with a 2mm wide band of solid white "
                "Platinum inlaid into the center. Polished Tungsten Carbide base with platinum inlay "
                "and beveled edges. Available in 6mm and 8mm widths.")

REF_URL = "https://shopaydins.com/cdn/shop/files/halsten-tungsten-ring-inlay-beveled-halsten-6-4-aydins-jewelry-907891.jpg?v=1776798520&width=2048"

# 4 distinct shot specifications
SHOTS = [
    {
        "name": "hero.jpg",
        "shot_type": "hero editorial product shot",
        "scene": "ring placed on dark walnut wood surface next to a tumbler of amber whiskey and worn leather wallet, warm side light from a window at golden hour, masculine editorial composition, 3/4 angle showing top face and inner band of ring, soft natural shadow",
        "allow_humans": False,
    },
    {
        "name": "image-2.jpg",
        "shot_type": "lifestyle ring on hand",
        "scene": "the HALSTEN ring is worn on the ring finger of a man's well-groomed left hand, hand resting naturally on a dark navy tailored suit jacket cuff with a glimpse of a leather watch strap, soft warm side light, sophisticated editorial wedding photography style, hand in soft focus around the ring, only the hand visible no face no upper body, masculine hand with neat clean nails",
        "allow_humans": True,
    },
    {
        "name": "image-3.jpg",
        "shot_type": "extreme macro close-up",
        "scene": "extreme macro close-up of the HALSTEN ring filling the frame, showing the polished tungsten carbide surface texture and the platinum inlay in razor-sharp detail, dramatic side lighting that highlights the beveled edges and the metallic reflection of the platinum band, deep black background, jewelry catalog macro photography style",
        "allow_humans": False,
    },
    {
        "name": "image-4.jpg",
        "shot_type": "outdoor lifestyle scene",
        "scene": "ring resting on a weathered wooden picnic table at a mountain cabin retreat, autumn maple leaves scattered nearby, vintage brass compass and folded plaid wool blanket in soft focus background, late afternoon golden light, peaceful outdoor wedding venue mood",
        "allow_humans": False,
    },
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

# Download reference
print(f"=== Downloading reference from live Shopify page ===")
req = urllib.request.Request(REF_URL, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=30) as r:
    ref_bytes = r.read()
ref_path = OUTPUT_DIR / "SHOPIFY-REFERENCE.jpg"
ref_path.write_bytes(ref_bytes)
print(f"OK {len(ref_bytes)} bytes")
ref_b64 = base64.b64encode(ref_bytes).decode("ascii")

def build_prompt(shot):
    fidelity = (f"The ring shown in the reference image is the {PRODUCT_DESC} The ring in the generated image "
                f"MUST PRESERVE the EXACT same material (polished Tungsten Carbide base), the SAME 2mm white platinum band "
                f"inlaid straight down the center, the SAME beveled edges, the SAME proportions. Do NOT add stones, gems, "
                f"engravings, decorations, additional bands, or any feature not in the reference image.")
    humans = ("" if shot["allow_humans"] else "No humans, no hands, no faces. ")
    return (f"Create a {shot['shot_type']} photograph for an Etsy ring listing.\n\n"
            f"FIDELITY (most important): {fidelity}\n\n"
            f"Scene: {shot['scene']}\n\n"
            f"Composition: photorealistic editorial style, 2048x2048 square format. {humans}"
            f"No text overlays, no logos, no watermarks.")

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
        print(f"HTTP {e.code}: {e.read().decode()[:300]}")
        return None
    candidates = data.get("candidates") or []
    if not candidates: return None
    for p in candidates[0].get("content", {}).get("parts", []):
        inline = p.get("inline_data") or p.get("inlineData")
        if inline and inline.get("data"):
            return base64.b64decode(inline["data"])
    return None

for shot in SHOTS:
    print(f"\n=== {shot['name']} ({shot['shot_type']}) ===")
    prompt = build_prompt(shot)
    img_bytes = gemini_call(prompt, ref_b64)
    if img_bytes:
        out = OUTPUT_DIR / shot["name"]
        out.write_bytes(img_bytes)
        print(f"OK {len(img_bytes)//1024}KB")
    else:
        print("FAIL")
    time.sleep(2)

print(f"\n=== Done. Files in {OUTPUT_DIR}: ===")
for f in sorted(OUTPUT_DIR.iterdir()):
    print(f"  {f.name}: {f.stat().st_size//1024}KB")
