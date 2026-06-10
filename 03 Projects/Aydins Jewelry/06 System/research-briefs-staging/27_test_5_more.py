"""5 more products from the needs-gen list for final variety check."""
import base64, json, os, sys, time
from pathlib import Path
import urllib.request

ROOT = Path("/home/openclaw/.openclaw")
ENV_FILE = ROOT / "agents/beta/credentials/gemini.env"
MODEL = "gemini-3.1-flash-image"

PRODUCTS = [
    {
        "codename": "AYTR032",
        "handle": "nightshade-purple-groove-mens-tungsten-wedding-band",
        "ref_url": "https://shopaydins.com/cdn/shop/products/nightshade-black-ring-black-tungsten-ring-purple-groove-stepped-edge-aytr032-8-7-aydins-jewelry-920266.jpg?v=1691604327&width=2048",
        "product_desc": ("NIGHTSHADE - Black Tungsten Carbide Wedding Band with a polished finish, "
                         "stepped edge profile, and a thin PURPLE groove running through the center "
                         "of the band. 8mm width."),
        "fidelity": ("Solid BLACK tungsten carbide ring with a stepped-edge profile (the band has a "
                     "raised center section with a step down to the polished edges), polished finish. "
                     "A single thin PURPLE inlaid groove runs horizontally around the center band. "
                     "Do NOT add stones, additional grooves, decoration, or change colors. Single "
                     "purple groove on a black tungsten background."),
        "core_feature": "purple groove stepped edge",
    },
    {
        "codename": "AYTR128",
        "handle": "gunmetal-damascus-ring-with-green-inside-aluminum",
        "ref_url": "https://shopaydins.com/cdn/shop/products/kiwi-green-ring-gunmetal-damascus-steel-ring-domed-aytr128-6-5-aydins-jewelry-989410.jpg?v=1691602426&width=2048",
        "product_desc": ("KIWI - Gunmetal Damascus Steel Wedding Band with a distinctive layered "
                         "damascus pattern. Domed profile. The interior of the ring is anodized "
                         "GREEN aluminum (only visible from inside or at the edges)."),
        "fidelity": ("Domed Damascus Steel ring showing the distinctive WAVY MARBLED FLOWING PATTERN "
                     "of damascus steel layers - dark gunmetal grey and lighter steel forming swirling "
                     "fluid lines across the surface. Color: gunmetal grey / dark steel. The INTERIOR "
                     "(visible through the ring opening or at the bottom edge) is bright GREEN. "
                     "Do NOT add stones, do NOT add inlay, do NOT change the damascus pattern. The "
                     "pattern is the central feature."),
        "core_feature": "damascus steel pattern with green interior",
    },
    {
        "codename": "STEGASAURUS",
        "handle": "dinosaur-stegasaurus-ring-laser-engraved-tungsten-wedding-ring",
        "ref_url": "https://shopaydins.com/cdn/shop/products/laser-engraved-dinosaur-stegasaurus-print-flat-tungsten-outdoorsmen-ring-4mm-12mm-stegasaurus-aydins-jewelry-514905.jpg?v=1691604326&width=2048",
        "product_desc": ("STEGASAURUS - Flat Polished Tungsten Carbide Wedding Ring with a LASER "
                         "ENGRAVED dinosaur (stegosaurus) silhouette design running around the band. "
                         "Available 4-12mm widths."),
        "fidelity": ("Polished silver-toned tungsten carbide ring with a flat profile. Around the "
                     "outside of the band is a continuous LASER ENGRAVED black silhouette pattern "
                     "of stegosaurus dinosaurs (the distinctive plated-back dinosaur shape) and "
                     "possibly trees/landscape elements forming a continuous scene. The engraving "
                     "is black/etched into the silver polished tungsten. Do NOT add stones, do NOT "
                     "add inlay, do NOT change the dinosaur design. The engraved scene is the feature."),
        "core_feature": "laser engraved dinosaur design",
    },
    {
        "codename": "AYTR183",
        "handle": "grain-tungsten-black-domed-with-a-comfort-fit-bocote-wood-sleeve-inlay-ring",
        "ref_url": "https://shopaydins.com/cdn/shop/products/grain-bocote-wood-black-tungsten-ring-brushed-domed-aytr183-8-7-aydins-jewelry-634412.jpg?v=1691602071&width=2048",
        "product_desc": ("GRAIN - Black Tungsten Carbide Wedding Band, 8mm wide, brushed domed "
                         "profile, with genuine BOCOTE WOOD INLAY across the center of the band. "
                         "Bocote wood has distinctive dark striping and golden-brown coloring with "
                         "visible grain."),
        "fidelity": ("Domed black tungsten carbide ring with a brushed finish. Across the CENTER of "
                     "the band is a CHANNEL INLAY of genuine BOCOTE WOOD - the wood has distinctive "
                     "DARK BROWN STRIPES against a WARM GOLDEN-YELLOW BROWN background, with natural "
                     "wavy grain patterns. The wood inlay is the focal point. Do NOT change the wood "
                     "color, do NOT add stones, do NOT add metallic inlays."),
        "core_feature": "bocote wood inlay",
    },
    {
        "codename": "G1654",
        "handle": "14k-rose-gold-wedding-band-with-orange-goldstone-inlay-beveled-edge-polished-design",
        "ref_url": "https://shopaydins.com/cdn/shop/products/orange-goldstone-inlaid-14k-rose-gold-wedding-band-for-mens-with-beveled-edges-polished-finish-8mm-g1654-beog-aydins-jewelry-614189.jpg?v=1691602534&width=2048",
        "product_desc": ("G1654 - Solid 14K ROSE GOLD Wedding Band, 8mm width, high-polish finish, "
                         "beveled edges, with ORANGE GOLDSTONE INLAY channel-set flush down the "
                         "center of the band. Orange goldstone is hand-made glass with copper "
                         "crystals creating an amber sparkle effect."),
        "fidelity": ("Solid 14K ROSE GOLD ring (warm pink-gold metal, NOT silver, NOT yellow gold). "
                     "Beveled edges, high-polished finish. CENTER channel inlay contains ORANGE "
                     "GOLDSTONE - a warm amber-orange stone with visible sparkly copper-colored "
                     "metallic flecks (like a glowing ember/coppery galaxy effect). The base ring "
                     "color is ROSE GOLD (pinkish warm gold). Do NOT make it silver, white gold, "
                     "or yellow gold. Do NOT change the orange color of the inlay."),
        "core_feature": "rose gold + orange goldstone inlay",
    },
]

OUTPUT_ROOT = Path("/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-10-test-5more")
OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

def make_shots(product):
    cn = product["codename"]
    return [
        {"name":"hero.jpg","shot_type":"hero editorial product shot","scene":"ring placed on dark walnut wood surface next to a tumbler of amber whiskey and worn leather wallet, warm side light from a window at golden hour, masculine editorial composition, 3/4 angle showing top face and inner band of ring, soft natural shadow","allow_humans":False},
        {"name":"image-2.jpg","shot_type":"lifestyle ring on hand","scene":"the ring worn on the ring finger of a man's well-groomed left hand, hand resting naturally on a dark navy tailored suit jacket cuff with a glimpse of a leather watch strap, soft warm side light, sophisticated editorial wedding photography style, hand in soft focus around the ring, only the hand visible no face no upper body, masculine hand with neat clean nails","allow_humans":True},
        {"name":"image-3.jpg","shot_type":"extreme macro close-up","scene":"extreme macro close-up of the ring filling the frame, showing the surface texture and inlay in razor-sharp detail, dramatic side lighting that highlights the materials and finish, deep black background, jewelry catalog macro photography style","allow_humans":False},
        {"name":"image-4.jpg","shot_type":"outdoor lifestyle scene","scene":"ring resting on a weathered wooden picnic table at a mountain cabin retreat, autumn maple leaves scattered nearby, vintage brass compass and folded plaid wool blanket in soft focus background, late afternoon golden light, peaceful outdoor wedding venue mood","allow_humans":False},
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
    parts = [{"inline_data": {"mime_type": "image/jpeg", "data": ref_b64}}, {"text": prompt_text}]
    body = {"contents": [{"parts": parts}], "generationConfig": {"responseModalities": ["IMAGE"]}}
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code}: {e.read().decode()[:200]}")
        return None
    for p in (data.get("candidates") or [{}])[0].get("content", {}).get("parts", []):
        inline = p.get("inline_data") or p.get("inlineData")
        if inline and inline.get("data"):
            return base64.b64decode(inline["data"])
    return None

for product in PRODUCTS:
    handle = product["handle"]
    out_dir = OUTPUT_ROOT / handle
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n=== {product['codename']} ({product['core_feature']}) ===")
    req = urllib.request.Request(product["ref_url"], headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            ref_bytes = r.read()
        (out_dir / "SHOPIFY-REFERENCE.jpg").write_bytes(ref_bytes)
        print(f"  reference: {len(ref_bytes)} bytes")
    except Exception as e:
        print(f"  REF FAIL: {e}")
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

print(f"\n=== Done ===")
