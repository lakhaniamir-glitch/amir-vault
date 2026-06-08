#!/usr/bin/env python3
"""Upload AI-generated lifestyle images (hero/image-2/image-3/image-4) for all 50 products
to Shopify Files. Then write a mapping file so the CSV can be updated with public URLs."""
import json
import time
from pathlib import Path
import urllib.request
import urllib.parse

CONFIG = json.load(open('/home/openclaw/.openclaw/agents/beta/shopify/config.json'))
STORE = 'aydinsjewelry.myshopify.com'
TOKEN = CONFIG['stores'][STORE]['accessToken']
API_VERSION = '2025-01'
ENDPOINT = f'https://{STORE}/admin/api/{API_VERSION}/graphql.json'

IMAGES_ROOT = Path('/home/openclaw/vault/brands/aydins/etsy-exports/2026-06-04/images')
OUT_MAPPING = IMAGES_ROOT.parent / 'ai-image-cdn-urls.json'

# Resume if mapping exists
existing = {}
if OUT_MAPPING.exists():
    try:
        existing = json.loads(OUT_MAPPING.read_text())
        print(f'Resuming: {len(existing)} URLs already uploaded')
    except Exception:
        existing = {}


def gql(query, variables=None):
    body = json.dumps({'query': query, 'variables': variables or {}}).encode()
    req = urllib.request.Request(
        ENDPOINT, data=body, method='POST',
        headers={'Content-Type': 'application/json', 'X-Shopify-Access-Token': TOKEN}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


STAGED = """
mutation stagedUploadsCreate($input: [StagedUploadInput!]!) {
  stagedUploadsCreate(input: $input) {
    stagedTargets {
      url
      resourceUrl
      parameters { name value }
    }
    userErrors { field message }
  }
}
"""

FILE_CREATE = """
mutation fileCreate($files: [FileCreateInput!]!) {
  fileCreate(files: $files) {
    files {
      id
      fileStatus
      alt
      ... on MediaImage { image { url } }
    }
    userErrors { field message }
  }
}
"""

FILE_QUERY = """
query getFile($id: ID!) {
  node(id: $id) {
    ... on MediaImage {
      id
      fileStatus
      image { url }
    }
  }
}
"""


def stage_upload(file_path, mime='image/jpeg'):
    size = file_path.stat().st_size
    resp = gql(STAGED, {
        'input': [{
            'filename': file_path.name,
            'mimeType': mime,
            'resource': 'IMAGE',
            'fileSize': str(size),
            'httpMethod': 'POST',
        }]
    })
    targets = resp.get('data', {}).get('stagedUploadsCreate', {}).get('stagedTargets', [])
    if not targets:
        raise RuntimeError(f'stage failed: {resp}')
    return targets[0]


def post_binary(target, file_path):
    """Multipart POST to staged URL (S3-compatible)."""
    boundary = '----AydinsBoundary' + str(int(time.time() * 1000))
    body = b''
    for p in target['parameters']:
        body += f'--{boundary}\r\nContent-Disposition: form-data; name="{p["name"]}"\r\n\r\n{p["value"]}\r\n'.encode()
    body += f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{file_path.name}"\r\nContent-Type: image/jpeg\r\n\r\n'.encode()
    body += file_path.read_bytes()
    body += f'\r\n--{boundary}--\r\n'.encode()
    req = urllib.request.Request(
        target['url'], data=body, method='POST',
        headers={'Content-Type': f'multipart/form-data; boundary={boundary}'}
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.status


def create_file(resource_url, alt_text):
    resp = gql(FILE_CREATE, {
        'files': [{
            'originalSource': resource_url,
            'contentType': 'IMAGE',
            'alt': alt_text,
        }]
    })
    files = resp.get('data', {}).get('fileCreate', {}).get('files', [])
    errs = resp.get('data', {}).get('fileCreate', {}).get('userErrors', [])
    if errs:
        raise RuntimeError(f'fileCreate userErrors: {errs}')
    if not files:
        raise RuntimeError(f'fileCreate empty: {resp}')
    return files[0]['id']


def wait_for_url(file_id, max_wait=60):
    for i in range(max_wait):
        resp = gql(FILE_QUERY, {'id': file_id})
        node = resp.get('data', {}).get('node', {})
        status = node.get('fileStatus')
        img = node.get('image') or {}
        url = img.get('url')
        if status == 'READY' and url:
            return url
        if status == 'FAILED':
            raise RuntimeError(f'file processing failed: {resp}')
        time.sleep(1)
    raise RuntimeError(f'file not ready after {max_wait}s')


def upload_one(file_path, alt):
    target = stage_upload(file_path)
    post_binary(target, file_path)
    file_id = create_file(target['resourceUrl'], alt)
    url = wait_for_url(file_id)
    return url


# Iterate products + AI images
product_dirs = sorted([d for d in IMAGES_ROOT.iterdir() if d.is_dir() and not d.name.startswith('_')])
print(f'Found {len(product_dirs)} product folders')

ai_files = ['hero.jpg', 'image-2.jpg', 'image-3.jpg', 'image-4.jpg']

uploaded = 0
skipped = 0
failed = []
mapping = dict(existing)

for i, pdir in enumerate(product_dirs, 1):
    handle = pdir.name
    for ai_file in ai_files:
        key = f'{handle}/{ai_file}'
        if key in mapping and mapping[key].startswith('http'):
            skipped += 1
            continue
        path = pdir / ai_file
        if not path.exists():
            failed.append((key, 'missing'))
            continue
        try:
            alt = f'{handle.replace("-", " ")} {ai_file.replace(".jpg","").replace("-", " ")}'
            url = upload_one(path, alt[:255])
            mapping[key] = url
            uploaded += 1
            print(f'[{i}/{len(product_dirs)}] {key} -> {url[:60]}...')
        except Exception as e:
            failed.append((key, str(e)[:120]))
            print(f'[{i}/{len(product_dirs)}] FAIL {key}: {e}')
        # Persist mapping after each upload (resilience to interruption)
        OUT_MAPPING.write_text(json.dumps(mapping, indent=2))
        time.sleep(0.3)

print(f'\nDone. uploaded={uploaded} skipped(already_uploaded)={skipped} failed={len(failed)}')
if failed:
    print('Failures:')
    for k, e in failed[:10]:
        print(f'  {k}: {e}')
print(f'Mapping: {OUT_MAPPING}  ({len(mapping)} entries)')
