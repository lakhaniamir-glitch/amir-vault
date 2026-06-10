"""Test for 2 products from the actual needs-gen list: BAXTER and EZRA."""
import base64, json, os, sys, time
from pathlib import Path
import urllib.request

ROOT = Path("/home/openclaw/.openclaw")
ENV_FILE = ROOT / "agents/beta/credentials/gemini.env"
MODEL = "gemini-3.1-flash-image"

PRODUCTS = [
    {
        "codename": "JDTR217",
        "handle": "baxter-mens-domed-tungsten-wedding-band-with-sterling-silver-braided-insert-center-8mm",
        "ref_url": "https://shopaydins.com/cdn/shop/files/baxter-silver-tungsten-sterling-silver-braided-wedding-ring-8mm-rings-aydins-jewelry-2915750.png?v=1777056797&width=2048",
        "product_desc": ("BAXTER — Polished Silver Tungsten Carbide Wedding Band with a Sterling Silver "
                         "Braided Insert in the center. Domed profile. 8mm width."),
        "fidelity": ("Polished silver-toned tungsten carbide ring with a domed profile, with a distinct "
                     "horizontal woven/braided sterling silver insert running through the center band. "
                     "The braided insert has visible interweaving strands. Do NOT add stones, gems, "
                     "engravings, or color. Both the ring and the braided insert are silver-toned. "
                     "Do NOT change the braided pattern in the center."),
        "core_feature": "sterling silver braided insert center",
    },
    {
        "codename": "MELO",
        "handle": "ezra-black-ceramic-ring-with-purple-gold-stone-inlay",
        "ref_url": "https://shopaydins.com/cdn/shop/products/ezra-ceramic-ring-purple-gold-stone-inlay-melo-8-5-aydins-jewelry-203622.jpg?v=1691602313&width=2048",
        "product_desc": ("EZRA — Black Ceramic Wedding Ring with Purple Goldstone Inlay in the center "
                         "channel, polished finish, beveled edges, 8mm width. High-tech advanced ceramic."),
        "fidelity": ("Black ceramic ring with polished finish and beveled edges. The center channel is "
                     "inlaid with PURPLE GOLDSTONE — a deep violet-purple stone with sparkly metallic "
                     "copper-gold flecks (like a galaxy/cosmic look) filling the center groove. The ring "
                     "base is solid matte/polished BLACK CERAMIC. Do NOT add additional stones, do NOT "
                     "change the purple goldstone color, do NOT add engravings, do NOT make the ring "
                     "any other color than black."),
        "core_feature": "purple goldstone inlay",
    },
]

OUTPUT_ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-10-test-baxter-ezra")
OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

def make_shots(product):
    cn = product["codename"]
    return [
        {
            "name": "hero.jpg",
            "shot_type": "hero editorial product shot",
            "scene": (f"ring placed on dark walnut wood surface next to a tumbler of amber whiskey and "
                      f"worn leather wallet, warm side light from a window at golden hour, masculine "
                      f"editorial composition, 3/4 angle showing top face and inner band of ring, "
                      f"soft natural shadow"),
            "allow_humans": False,
        },
        {
            "name": "image-2.jpg",
            "shot_type": "lifestyle ring on hand",
            "scene": (f"the ring worn on the ring finger of a man's well-groomed left hand, hand resting "
                      f"naturally on a dark navy tailored suit jacket cuff with a glimpse of a leather "
                      f"watch strap, soft warm side light, sophisticated editorial wedding photography "
                      f"style, hand in soft focus around the ring, only the hand visible no face no "
                      f"upper body, masculine hand with neat clean nails"),
            "allow_humans": True,
        },
        {
            "name": "image-3.jpg",
            "shot_type": "extreme macro close-up",
            "scene": (f"extreme macro close-up of the ring filling the frame, showing the surface "
                      f"texture and inlay in razor-sharp detail, dramatic side lighting that highlights "
                      f"the materials and finish, deep black background, jewelry catalog macro "
                      f"photography style"),
            "allow_humans": False,
        },
        {
            "name": "image-4.jpg",
            "shot_type": "outdoor lifestyle scene",
            "scene": (f"ring resting on a weathered wooden picnic table at a mountain cabin retreat, "
                      f"autumn maple leaves scattered nearby, vintage brass compass and folded plaid "
                      f"wool blanket in soft focus background, late afternoon golden light, peaceful "
                      f"outdoor wedding venue mood"),
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
    print(f"\n=== {product['codename']} ({product['core_feature']}) ===")

    # Download reference
    req = urllib.request.Request(product["ref_url"], headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            ref_bytes = r.read()
        ref_path = out_dir / "SHOPIFY-REFERENCE.jpg"
        ref_path.write_bytes(ref_bytes)
        print(f"  reference: {len(ref_bytes)} bytes")
    except Exception as e:
        print(f"  REFERENCE FAILED: {e}")
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
