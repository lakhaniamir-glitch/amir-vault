"""Test image gen for NYMERIA and REVOLUTION with 4 distinct shot types."""
import base64, json, os, sys, time
from pathlib import Path
import urllib.request

ROOT = Path("/home/openclaw/.openclaw")
ENV_FILE = ROOT / "agents/beta/credentials/gemini.env"
MODEL = "gemini-3.1-flash-image"

# 2 products to test
PRODUCTS = [
    {
        "codename": "NYMERIA",
        "handle": "nymeria-tension-set-blue-sapphire-titanium-band-with-blue-stripe-4mm",
        "ref_url": "https://shopaydins.com/cdn/shop/products/nymeria-titanium-ring-blue-sapphire-nymeria-4-35-aydins-jewelry-258103.jpg?v=1691603881&width=2048",
        "product_desc": ("NYMERIA — Black Titanium Wedding Band with a tension-set round blue sapphire stone "
                         "set into the center, with a thin blue stripe running through the band. 4mm width. "
                         "Black titanium base with brushed finish."),
        "fidelity": ("Black titanium ring with a tension-mounted round blue sapphire gemstone in the center, "
                     "and a thin continuous blue inlay stripe encircling the band. Brushed black titanium finish. "
                     "Do NOT change the sapphire color, do NOT add extra stones, do NOT remove the blue stripe."),
        "material": "Black titanium",
        "core_feature": "tension-set blue sapphire",
    },
    {
        "codename": "REVOLUTION",
        "handle": "revolution-tungsten-carbide-spinner-ring-spinning-wedding-band-8mm",
        "ref_url": "https://shopaydins.com/cdn/shop/files/revolution-tungsten-ring-spinner-revolution-8-5-aydins-jewelry-677496.jpg?v=1724004539&width=2048",
        "product_desc": ("REVOLUTION — Silver Tungsten Carbide Spinner Ring, 8mm wide. The center band spins "
                         "freely on a polished tungsten base. Brushed center finish with polished beveled edges."),
        "fidelity": ("Silver tungsten carbide spinner ring with TWO LAYERS visible — a brushed-finish spinning "
                     "center band ON TOP of a polished tungsten base ring with beveled edges. The spinner is the "
                     "raised middle portion. Do NOT add stones, do NOT add inlay, do NOT add engravings. The ring "
                     "is solid silver-toned tungsten throughout."),
        "material": "Silver tungsten carbide",
        "core_feature": "spinning fidget center band",
    },
]

OUTPUT_ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-10-test-2more")
OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

# 4 shot specs (templated per product)
def make_shots(product):
    cn = product["codename"]
    return [
        {
            "name": "hero.jpg",
            "shot_type": "hero editorial product shot",
            "scene": (f"{cn} ring placed on dark walnut wood surface next to a tumbler of amber whiskey and "
                      f"worn leather wallet, warm side light from a window at golden hour, masculine editorial "
                      f"composition, 3/4 angle showing top face and inner band of ring, soft natural shadow"),
            "allow_humans": False,
        },
        {
            "name": "image-2.jpg",
            "shot_type": "lifestyle ring on hand",
            "scene": (f"the {cn} ring worn on the ring finger of a man's well-groomed left hand, hand resting "
                      f"naturally on a dark navy tailored suit jacket cuff with a glimpse of a leather watch "
                      f"strap, soft warm side light, sophisticated editorial wedding photography style, hand "
                      f"in soft focus around the ring, only the hand visible no face no upper body, masculine "
                      f"hand with neat clean nails"),
            "allow_humans": True,
        },
        {
            "name": "image-3.jpg",
            "shot_type": "extreme macro close-up",
            "scene": (f"extreme macro close-up of the {cn} ring filling the frame, showing the surface texture "
                      f"in razor-sharp detail, dramatic side lighting that highlights the materials and finish, "
                      f"deep black background, jewelry catalog macro photography style"),
            "allow_humans": False,
        },
        {
            "name": "image-4.jpg",
            "shot_type": "outdoor lifestyle scene",
            "scene": (f"{cn} ring resting on a weathered wooden picnic table at a mountain cabin retreat, autumn "
                      f"maple leaves scattered nearby, vintage brass compass and folded plaid wool blanket in "
                      f"soft focus background, late afternoon golden light, peaceful outdoor wedding venue mood"),
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

def build_prompt(product, shot):
    humans = ("" if shot["allow_humans"] else "No humans, no hands, no faces. ")
    return (f"Create a {shot['shot_type']} photograph for an Etsy ring listing.\n\n"
            f"FIDELITY (most important): The ring in the reference image is {product['product_desc']} "
            f"The generated image MUST preserve the EXACT ring: {product['fidelity']}\n\n"
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

for product in PRODUCTS:
    handle = product["handle"]
    out_dir = OUTPUT_ROOT / handle
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n=== {product['codename']} ===")

    # Download reference
    req = urllib.request.Request(product["ref_url"], headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            ref_bytes = r.read()
        ref_path = out_dir / "SHOPIFY-REFERENCE.jpg"
        ref_path.write_bytes(ref_bytes)
        print(f"  reference: {len(ref_bytes)} bytes")
    except Exception as e:
        print(f"  reference DOWNLOAD FAILED: {e}")
        continue
    ref_b64 = base64.b64encode(ref_bytes).decode("ascii")

    for shot in make_shots(product):
        prompt = build_prompt(product, shot)
        img = gemini_call(prompt, ref_b64)
        if img:
            (out_dir / shot["name"]).write_bytes(img)
            print(f"  {shot['name']}: {len(img)//1024}KB")
        else:
            print(f"  {shot['name']}: FAIL")
        time.sleep(2)

print(f"\n=== Done. Output: {OUTPUT_ROOT} ===")
for d in sorted(OUTPUT_ROOT.iterdir()):
    if d.is_dir():
        print(f"\n{d.name}:")
        for f in sorted(d.iterdir()):
            print(f"  {f.name}: {f.stat().st_size//1024}KB")
