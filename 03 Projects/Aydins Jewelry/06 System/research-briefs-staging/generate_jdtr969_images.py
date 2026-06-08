"""Generate 4 lifestyle images for JDTR969 via Gemini 3.1 with reference image,
then upload to Shopify Files, then return URLs."""
import base64, json, time
from pathlib import Path
import urllib.request, urllib.error

ROOT = Path("/home/openclaw/.openclaw")
GEMINI_ENV = ROOT / "agents/beta/credentials/gemini.env"
SHOPIFY_CFG = ROOT / "agents/beta/shopify/config.json"
REF_IMG = Path("/tmp/jd_0969.jpg")
OUT_DIR = ROOT / "vault/brands/aydins/etsy-exports/2026-06-04/images/jdtr969"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Load Gemini API key
gemini_key = None
for line in GEMINI_ENV.read_text().splitlines():
    if line.startswith("GEMINI_API_KEY="):
        gemini_key = line.split("=", 1)[1].strip().strip('"').strip("'")
        break
assert gemini_key, "GEMINI_API_KEY not found"

# Load Shopify token
cfg = json.load(open(SHOPIFY_CFG))
STORE = "aydinsjewelry.myshopify.com"
SHOP_TOKEN = cfg["stores"][STORE]["accessToken"]

MODEL = "gemini-3.1-flash-image"

REF_B64 = base64.b64encode(REF_IMG.read_bytes()).decode()

# 4 different prompts, all using the reference image
STRICT_PRESERVE = (
    "STRICT FIDELITY: preserve exact materials, exact blue meteorite-textured inlay pattern, "
    "exact silver arrow design running through the inlay, exact black tungsten base, exact domed profile, "
    "exact brushed beveled edges, exact ring profile and width from the reference. "
    "Do NOT change the inlay pattern, do NOT change the arrow shape, do NOT add stones, "
    "do NOT add stripes, do NOT add engravings, do NOT alter the finish. "
    "No text or logos anywhere in the frame. No watermarks. No visible brand badges."
)

PROMPTS = {
    "hero.jpg": (
        "Take the EXACT ring shown in the input reference image. Place it as the hero of a cinematic product photograph. "
        "Scene: ring resting upright on a weathered grey granite ledge with a deep moody blue dusk sky in the background. "
        "Subtle wisps of cool mist. Soft cool moonlight key from upper left, faint warm rim light from behind to separate it from the dark sky. "
        "Shallow depth of field, 35mm lens look, square 2048x2048. "
        + STRICT_PRESERVE
    ),
    "image-2.jpg": (
        "Take the EXACT ring shown in the input reference image. Place it worn on a man's left ring finger, close-up of the hand with the ring as the focal point. "
        "Scene: man's hand resting on a teak yacht deck rail, dusk over a deep blue ocean horizon out of focus behind. "
        "Casual linen shirt cuff visible. Soft cool dusk light. Natural masculine hand, mid-30s skin. "
        "Photorealistic, shallow depth of field, 35mm lens look, square 2048x2048. "
        + STRICT_PRESERVE
    ),
    "image-3.jpg": (
        "Take the EXACT ring shown in the input reference image. Render an extreme macro close-up of the inlay, "
        "filling 80 percent of the frame. Highlight the texture of the blue meteorite-style inlay and the silver arrow design. "
        "Tilt the ring slightly to show depth. Soft directional studio light from upper left. "
        "Dark neutral grey background out of focus. Photorealistic, very shallow depth of field, square 2048x2048. "
        + STRICT_PRESERVE
    ),
    "image-4.jpg": (
        "Take the EXACT ring shown in the input reference image. Place it worn on a man's left ring finger, close-up of the hand. "
        "Scene: hand resting on the rim of a traditional archery quiver, with cedar arrow shafts and natural fletched feathers in soft focus behind. "
        "Warm late-afternoon golden hour outdoor light. Dark olive canvas jacket cuff visible. "
        "The silver arrow on the ring echoes the real arrows in the background. "
        "Photorealistic, shallow depth of field, 35mm lens look, square 2048x2048. "
        + STRICT_PRESERVE
    ),
}

def call_gemini(prompt):
    body = {
        "contents": [{
            "role": "user",
            "parts": [
                {"inlineData": {"mimeType": "image/jpeg", "data": REF_B64}},
                {"text": prompt},
            ],
        }],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
    }
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={gemini_key}"
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST", headers={"Content-Type": "application/json"})
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                resp = json.loads(r.read())
            break
        except urllib.error.HTTPError as e:
            err_body = e.read().decode()[:400]
            if e.code in (429, 503) and attempt == 0:
                time.sleep(30); continue
            raise RuntimeError(f"Gemini HTTP {e.code}: {err_body}")
    for cand in resp.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                return base64.b64decode(inline["data"])
    raise RuntimeError(f"No image returned: {resp}")

# Generate the 4 images
print(f"Reference: {REF_IMG} ({REF_IMG.stat().st_size:,}b)")
for fname, prompt in PROMPTS.items():
    out = OUT_DIR / fname
    print(f"\nGenerating {fname}...")
    try:
        img_bytes = call_gemini(prompt)
        out.write_bytes(img_bytes)
        print(f"  -> {out} ({len(img_bytes):,}b)")
    except Exception as e:
        print(f"  FAILED: {e}")
        continue
    time.sleep(2)  # be kind

# === Upload all 4 to Shopify Files ===
print("\n=== Uploading to Shopify CDN ===")

STAGED_MUT = """
mutation stagedUploadsCreate($input: [StagedUploadInput!]!) {
  stagedUploadsCreate(input: $input) {
    stagedTargets { url resourceUrl parameters { name value } }
    userErrors { field message }
  }
}
"""
FILE_CREATE = """
mutation fileCreate($files: [FileCreateInput!]!) {
  fileCreate(files: $files) {
    files { id fileStatus ... on MediaImage { image { url } } }
    userErrors { field message }
  }
}
"""
FILE_QUERY = """
query getFile($id: ID!) {
  node(id: $id) {
    ... on MediaImage { id fileStatus image { url } }
  }
}
"""

def gql(query, variables=None):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        f"https://{STORE}/admin/api/2025-01/graphql.json",
        data=body, method="POST",
        headers={"Content-Type": "application/json", "X-Shopify-Access-Token": SHOP_TOKEN},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

def stage_and_post(file_path):
    size = file_path.stat().st_size
    resp = gql(STAGED_MUT, {"input": [{
        "filename": file_path.name, "mimeType": "image/jpeg",
        "resource": "IMAGE", "fileSize": str(size), "httpMethod": "POST"
    }]})
    target = resp["data"]["stagedUploadsCreate"]["stagedTargets"][0]
    # multipart POST to staged URL
    boundary = "----JDTR969Boundary" + str(int(time.time()*1000))
    body = b""
    for p in target["parameters"]:
        body += f'--{boundary}\r\nContent-Disposition: form-data; name="{p["name"]}"\r\n\r\n{p["value"]}\r\n'.encode()
    body += f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{file_path.name}"\r\nContent-Type: image/jpeg\r\n\r\n'.encode()
    body += file_path.read_bytes()
    body += f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(target["url"], data=body, method="POST",
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    urllib.request.urlopen(req, timeout=120).read()
    return target["resourceUrl"]

def create_and_wait(resource_url, alt):
    resp = gql(FILE_CREATE, {"files": [{"originalSource": resource_url, "contentType": "IMAGE", "alt": alt}]})
    file_id = resp["data"]["fileCreate"]["files"][0]["id"]
    for _ in range(60):
        q = gql(FILE_QUERY, {"id": file_id})
        node = q["data"]["node"] or {}
        status = node.get("fileStatus")
        img = node.get("image") or {}
        if status == "READY" and img.get("url"):
            return img["url"]
        if status == "FAILED":
            raise RuntimeError(f"file FAILED: {q}")
        time.sleep(1)
    raise RuntimeError("file not READY after 60s")

uploaded_urls = {}
for fname in PROMPTS.keys():
    out = OUT_DIR / fname
    if not out.exists():
        print(f"  SKIP {fname} (not generated)")
        continue
    try:
        resource_url = stage_and_post(out)
        cdn_url = create_and_wait(resource_url, f"JDTR969 {fname.replace('.jpg','').replace('-',' ')}")
        uploaded_urls[fname] = cdn_url
        print(f"  {fname} -> {cdn_url}")
    except Exception as e:
        print(f"  FAILED upload {fname}: {e}")

# Save URL mapping for downstream CSV update
out_json = OUT_DIR.parent.parent.parent / "jdtr969-image-cdn-urls.json"
out_json.write_text(json.dumps(uploaded_urls, indent=2))
print(f"\nSaved URL map: {out_json}")
for k, v in uploaded_urls.items(): print(f"  {k}: {v}")
