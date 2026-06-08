#!/usr/bin/env python3
"""Generate image-4.jpg for Etsy products: on-finger lifestyle shot using SHOPIFY-REFERENCE.jpg as input.
Model: gemini-3.1-flash-image (per Amir's instruction 2026-06-08).
Reference-image rule (locked 2026-06-04): every real-product image must use the source photo as input.

Usage:
  python3 generate_etsy_image4.py                # all 50 products
  python3 generate_etsy_image4.py nurgle-black-diamond-titanium-wedding-ring   # single product (test)
"""
import base64
import json
import sys
import time
from pathlib import Path
import urllib.request
import urllib.error

ROOT = Path("/home/openclaw/.openclaw")
ENV_FILE = ROOT / "agents/beta/credentials/gemini.env"
IMAGES_ROOT = ROOT / "vault/brands/aydins/etsy-exports/2026-06-04/images"
MANIFEST_PATH = IMAGES_ROOT.parent / "image-4-generation-manifest.json"
MODEL = "gemini-3.1-flash-image"

# Feature-to-environment mapping per product handle.
# Pick a scene that matches the ring's character. Same skeleton prompt, scene varies.
ENV_MAP = {
    "addersfield-gold-tungsten-ring-gold-brushed-flat": "tailored navy suit cuff and a tumbler of amber whiskey on dark walnut desk, warm late-afternoon side light, leather chair edge",
    "alabaster-silver-ring-white-ceramic-domed": "clean white marble countertop in a modern apartment, soft morning daylight, white linen shirt sleeve, minimalist",
    "alexander-black-gray-lava-rock-stone-inlay": "rocky volcanic shore with weathered grey stones, overcast moody light, dark olive canvas jacket cuff",
    "auric-silver-tungsten-ring-white-black-and-gold-foil-resin-inlay": "rich black leather armchair and brass side table with a small art-deco lamp, warm low light, charcoal suit cuff",
    "aurion-gold-tungsten-ring-gold-foil-inlay-beveled-8mm": "polished dark walnut desk with vintage fountain pen and gold-edged journal, warm tungsten lamp, navy blazer sleeve",
    "aydins-tungsten-carbide-mens-band-black-hammered-stepped-edge-8mm-tungsten-wedding-ring": "rustic forge workshop with anvil and glowing coals out of focus, soot on hand, dark canvas apron, warm orange backlight",
    "baldur-domed-tungsten-rune-wedding-band": "weathered viking-style longship oar handle, cold dawn light over a fjord, dark wool sleeve, stoic Nordic mood",
    "blackjack-tungsten-ring-black-brushed-beveled": "green-felt poker table with stacks of black chips out of focus, dim casino lighting from above, sharp dark suit cuff",
    "brave-blue-tungsten-ring-blue-brushed-flat": "wooden boat dock at sunset over a calm blue lake, denim shirt cuff, gentle golden hour reflection on water",
    "bridgeport-purple-aluminum-ring-green-groove": "creative studio with paint-splattered wooden workbench, eclectic green and purple color objects out of focus, warm afternoon light through industrial window",
    "cairns-rose-gold-tungsten-ring-purple-groove": "rose gold ceramic coffee mug and a sprig of lavender on linen tablecloth, soft morning daylight, white shirt sleeve",
    "clematis-tungsten-black-beveled-and-purple-inside-aluminum-ring": "garden bed of blooming purple clematis vines on a wood trellis, dappled afternoon sunlight, casual dark gardening shirt cuff",
    "cosmic-black-tungsten-ring-crushed-alexandrite-goldstone-inlay-domed": "backyard astronomy setup with a brass telescope and starry deep-blue sky just after dusk, dark sweater cuff, faint Milky Way glow",
    "crimsen-red-tungsten-ring-brushed-domed": "wrapped around the gear shift of a red vintage sports car, leather interior, low evening sun through the windshield, driving gloves removed",
    "custom-logo-laser-engraved-signet-ring-gold-silver-black": "vintage leather-topped writing desk with wax seal stamp and embossed letterhead, warm desk lamp, white shirt sleeve, classic gentleman's office",
    "dominus-domed-tungsten-carbide-ring-2mm-10mm": "minimalist modern office with brushed concrete desk, simple stainless mechanical watch nearby, soft north-facing daylight, charcoal suit sleeve",
    "elysian-black-titanium-ring-with-polished-beveled-edges-and-brush-finished-center-8mm": "matte black slate countertop in a high-end loft kitchen, brushed steel pendant lamp above, dark grey henley sleeve",
    "emperor-black-tungsten-ring-blue-brushed-flat": "stormy harbor at twilight with weathered wood pier and rope coil, deep navy waterproof jacket sleeve, cool blue cast light",
    "ferrari-black-and-red-tungsten-carbide-ring": "leather-wrapped steering wheel of a red sports car, deep red stitching, dashboard out of focus with no readable badges or symbols, golden hour through windshield",
    "fingerprint-jewelry-his-and-her-fingerprint-couples-ring-promise-ring-plus-engraved-ring-personalized-ring-anniversary-ring-tungsten-4": "two hands gently overlapping, man's hand wearing the ring on top, partner's hand below with delicate band visible, warm window light in a quiet bedroom, white linen bedding",
    "fingerprint-jewelry-his-and-her-fingerprint-couples-ring-promise-ring-plus-engraved-ring-personalized-ring-anniversary-ring-tungsten-6": "two hands clasped near a small bouquet of soft white flowers on a wooden bench, golden hour outdoor light, casual wedding-day mood",
    "galaxy-titanium-polished-beveled-edge-with-blue-green-opal-inlay-8-mm": "open observatory dome at night with the Milky Way visible above, dark sweater sleeve, the opal inlay catches faint starlight reflection",
    "geelong-green-aluminum-ring-purple-groove": "creative graphic-design studio desk with green plants and a purple notebook out of focus, white shirt sleeve, afternoon natural light",
    "glowhigh-domed-blue-tungsten-carbide-wedding-ring-with-brushed-finish": "edge of a calm blue alpine lake at dusk, dark blue technical jacket cuff, soft cool blue light, ripples on water",
    "gunnar-yellow-gold-tungsten-ring-with-rosewood-and-crushed-turquoise-inlay-8mm": "southwestern leather workbench with turquoise stones and tooled leather strap, warm late-afternoon sun, denim shirt cuff",
    "hartman-white-tungsten-blue-yellow-wood-ring": "artist's painting studio with canvas and yellow and blue oil paint tubes out of focus, paint-flecked white shirt sleeve, soft north-facing daylight",
    "ironlance-black-tungsten-ring-with-flat-brushed-center-and-8-laser-engraved-crosses-8mm": "old stone chapel interior with candle flames and a leather-bound bible on a wooden pew, warm candlelight, dark suit sleeve, reverent quiet mood",
    "jakub-black-tungsten-ring-gold-groove": "sophisticated home library with leather-bound books and brass desk lamp, warm low light, dark herringbone jacket cuff",
    "knox-gold-tungsten-ring-black-hammered": "blacksmith forge workshop with hammered metal tools and a glowing forge out of focus, dark leather apron, soot on hand, warm orange backlight",
    "leporis-black-tungsten-ring-round-cut-white-cz": "black tie event with crystal champagne flute and white tablecloth out of focus, crisp white tuxedo shirt cuff and onyx cufflink, soft chandelier light",
    "lusters-black-tungsten-ring-with-purple-tiger-cowrie-inlay": "tropical beach at golden hour with seashells and warm tide on dark sand, casual linen shirt cuff, the purple cowrie inlay catches the sunset",
    "maestro-mens-silver-brushed-tungsten-wedding-band-with-gold-groove-in-center-7mm": "concert hall stage with sheet music on a music stand and conductor's baton out of focus, warm spotlight, formal black tuxedo cuff",
    "nemesis-black-tungsten-ring-white-round-cz-beveled-edge-ring": "black tie gala with marble bar and crystal glassware out of focus, sharp black tuxedo sleeve with onyx cufflink, dramatic spotlight",
    "nurgle-black-diamond-titanium-wedding-ring": "moody dark gothic library with candelabra and weathered leather books, dark velvet sleeve, deep shadows, the black diamonds catch faint candlelight, KNIGHT character mood",
    "nymeria-tension-set-blue-sapphire-titanium-band-with-blue-stripe-4mm": "yacht teak deck at dusk over deep blue ocean, light blue linen shirt cuff, the sapphire catches the last sunlight, refined coastal mood",
    "peachland-black-tungsten-ring-green-celtic-dragon-inlay": "medieval longsword pommel resting on a wooden table with a worn map and brass compass, dim torchlight, dark leather sleeve, Celtic warrior mood",
    "phantom-black-titanium-brushed-center-spinner-mens-wedding-ring-with-spinning-polished-base-8mm": "modern coffee shop bar counter with a flat-white espresso cup and notebook, dark grey hoodie sleeve, soft window light, casual everyday mood",
    "raptor-black-tungsten-ring-blue-offset-groove": "matte black motorcycle fuel tank with blue accent stripe out of focus, black leather glove resting nearby, golden hour garage light, aggressive masculine mood",
    "revolution-tungsten-carbide-spinner-ring-spinning-wedding-band-8mm": "casual standing desk with a fidget toy and a notebook, soft daylight from window, plain grey t-shirt sleeve, calm focused mood",
    "revolve-black-tungsten-brushed-finish-spinner-ring-polished-base-spinning-wedding-band-6mm-8mm": "minimalist desk with a paperback book and a black ceramic coffee cup, warm late-morning light, plain dark t-shirt sleeve",
    "ridges-genuine-damascus-steel-silver-ring-with-olive-wood-sleeve-inlay": "blacksmith forge bench with a damascus blade out of focus and olive wood handle scales, soot on hand, dark canvas apron, warm forge backlight",
    "ridwan-black-tungsten-ring-green-groove": "deep evergreen forest trail at golden hour with moss-covered stones, olive utility jacket cuff, soft dappled sunlight",
    "rugged-black-tungsten-ring-gun-metal-hammered-center-with-stepped-edge": "weathered mountain overlook with grey granite ledge, cold morning mist, dark technical jacket cuff, rugged outdoorsman mood",
    "sequoia-iron-wood-black-shiny-domed": "old-growth redwood forest with sun rays through the canopy, deep brown wool flannel cuff, warm forest floor light, calm natural mood",
    "signet-ring-custom-signet-ring-fingerprint-ring-laser-engraved-gold-signet-ring-silver-signet-ring-black-signet-ring": "vintage mahogany executive desk with leather blotter, brass paperweight and an embossed envelope, warm desk lamp, white French-cuff shirt sleeve",
    "smokeylade-black-gun-metal-tungsten-with-domed-brushed-ring": "dim speakeasy whiskey bar with crystal tumbler of bourbon and a cigar cutter on dark wood, warm low light, charcoal blazer cuff",
    "spartanite-black-ring-black-brushed-domed-orange-groove": "matte black sport motorcycle with orange accent stripe out of focus, black riding glove nearby, warm garage light, athletic masculine mood",
    "stainless-steel-fingerprint-dog-tag-black-style-2": "worn around a man's neck on a stainless ball chain, dark grey crewneck t-shirt visible, soft side light, casual quiet portrait, no face",
    "valor-silver-tungsten-ring-silver-inlay-black-diamonds": "black tie formal event with marble bar top and crystal glassware out of focus, sharp black tuxedo cuff with onyx cufflink, soft chandelier light",
    "yorkshire-brushed-finish-black-ceramic-wedding-band-with-beveled-edges-6mm-8mm": "minimalist concrete loft kitchen with matte black espresso machine and white ceramic cup, soft north-facing daylight, dark henley sleeve",
}


def load_env():
    env = {}
    for raw in ENV_FILE.read_text().splitlines():
        line = raw.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def build_prompt(handle, env_desc):
    is_dog_tag = "dog-tag" in handle
    placement = (
        "worn around a man's neck on a chain, no face visible, close-up of the dog tag against a t-shirt"
        if is_dog_tag
        else "worn on a man's left ring finger, close-up of the hand with the ring as the focal point, natural masculine hand, mid-30s skin"
    )
    return (
        "Take the EXACT ring shown in the input reference image and place it in this lifestyle scene: " + placement + ". "
        "Scene: " + env_desc + ". "
        "Photorealistic, cinematic lighting, shallow depth of field, 35mm lens look, "
        "high detail on metal finish and inlay texture. Square 2048x2048. "
        "STRICT FIDELITY: preserve exact materials, exact inlay pattern, exact metal finish, exact colors, exact ring profile and width from the reference. "
        "Do NOT add stones, do NOT add stripes, do NOT add engravings, do NOT change the inlay, do NOT alter the finish (brushed vs polished vs hammered). "
        "No text or logos anywhere in the frame. No visible brand badges. No watermarks."
    )


def generate(handle, api_key):
    folder = IMAGES_ROOT / handle
    ref_path = folder / "SHOPIFY-REFERENCE.jpg"
    out_path = folder / "image-4.jpg"
    if not ref_path.exists():
        return {"handle": handle, "status": "skip_no_reference"}
    env_desc = ENV_MAP.get(handle)
    if not env_desc:
        return {"handle": handle, "status": "skip_no_env_mapping"}

    ref_b64 = base64.b64encode(ref_path.read_bytes()).decode()
    prompt = build_prompt(handle, env_desc)

    body = {
        "contents": [{
            "role": "user",
            "parts": [
                {"inlineData": {"mimeType": "image/jpeg", "data": ref_b64}},
                {"text": prompt},
            ],
        }],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
    }
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={api_key}"
    data_bytes = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data_bytes, headers={"Content-Type": "application/json"}, method="POST")

    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                resp = json.loads(r.read())
            break
        except urllib.error.HTTPError as e:
            err_body = e.read().decode()[:500]
            if e.code in (429, 503) and attempt == 0:
                time.sleep(30)
                continue
            return {"handle": handle, "status": "http_error", "code": e.code, "body": err_body}
        except Exception as e:
            return {"handle": handle, "status": "error", "error": str(e)}

    img_bytes = None
    texts = []
    for cand in resp.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            if "text" in part:
                texts.append(part["text"])
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                img_bytes = base64.b64decode(inline["data"])
                break
        if img_bytes:
            break
    if not img_bytes:
        return {"handle": handle, "status": "no_image_returned", "texts": texts[:3]}

    out_path.write_bytes(img_bytes)
    return {
        "handle": handle,
        "status": "ok",
        "out": str(out_path),
        "size_bytes": len(img_bytes),
        "env": env_desc,
        "prompt": prompt[:300],
    }


def main():
    env = load_env()
    api_key = env["GEMINI_API_KEY"]

    only = sys.argv[1] if len(sys.argv) > 1 else None
    handles = [only] if only else sorted(ENV_MAP.keys())

    results = []
    for i, handle in enumerate(handles, 1):
        print(f"[{i}/{len(handles)}] {handle}")
        result = generate(handle, api_key)
        print(f"  -> {result.get('status')}")
        results.append(result)
        time.sleep(2)  # small pause to be kind to API

    manifest = {
        "model": MODEL,
        "ran_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "count_total": len(results),
        "count_ok": sum(1 for r in results if r.get("status") == "ok"),
        "results": results,
    }
    existing = json.loads(MANIFEST_PATH.read_text()) if MANIFEST_PATH.exists() else {"runs": []}
    existing.setdefault("runs", []).append(manifest)
    MANIFEST_PATH.write_text(json.dumps(existing, indent=2))
    print(f"\nManifest: {MANIFEST_PATH}")
    print(f"Success: {manifest['count_ok']}/{manifest['count_total']}")


if __name__ == "__main__":
    main()
