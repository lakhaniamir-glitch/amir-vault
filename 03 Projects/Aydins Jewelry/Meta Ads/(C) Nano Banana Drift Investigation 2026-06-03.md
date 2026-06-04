# Nano Banana Anchor Fidelity Investigation

Date: 2026-06-03  
Scope: Round 3 Coffee Shop UGC, TYPHOON V1 anchor drift  
Status: Investigation only, no code changes executed

## Bug evidence

Round 3 V1 was anchored to the real Shopify product image for TYPHOON:

- Product: `TYPHOON | Red Burl Wood, Blue Tungsten Ring, Brushed, Flat`
- Handle: `typhoon-red-burl-wood-ring-blue-brushed-flat`
- Source image: `https://cdn.shopify.com/s/files/1/1857/8135/products/typhoon-red-burl-wood-blue-tungsten-ring-brushed-flat-aytr425-8-7-aydins-jewelry-560842.jpg?v=1691605183`
- Generated output: `/home/openclaw/.openclaw/vault/brands/aydins/meta-ads/01-ugc-testimonial/round3-coffee-shop/v1.png`

The final V1 passed general QA, but product fidelity is imperfect. The output captures a blue and warm wood color contrast, but it does not preserve the exact TYPHOON construction.

## Specific drift observed

Compared source TYPHOON product image with the generated V1 output:

- Color: source has deep teal or navy blue exterior with warm orange brown burl wood interior. Output shifts toward brighter cyan blue side bands with orange brown visible as an exterior center stripe.
- Material: source reads as brushed blue tungsten exterior plus polished red burl wood inside. Output reads more like glossy blue metal or plastic with a decorative wood strip.
- Inlay placement: source wood is on the inside wall of the ring. Output places wood as a center exterior inlay around the band.
- Profile: source is a wider, thicker, flat-sided band with darker rounded or beveled edges. Output is narrower with three visible exterior bands and less thickness.
- Recognizability: partial only. It resembles the source color family, but the defining TYPHOON design is not faithfully preserved.

## Root cause analysis

The round 3 generation used an image reference plus text prompt, but the model appears to treat the product image as a loose style reference rather than a locked product identity constraint.

Probable causes:

1. The lifestyle scene request has too much freedom. The model is re-rendering the ring as part of a new scene instead of compositing or preserving it.
2. The prompt says to preserve the ring, but it does not enforce a separate product-mask or identity-preservation step.
3. There is no automated source-versus-output fidelity gate before accepting the image.
4. Retry prompts improved general appearance but still allowed material placement drift, especially for products where the key feature is inside the band rather than outside.
5. The current flow is closer to reference-guided generation than true image-to-image product restaging with strong fidelity.

## Recommended fix, not executed

Use a stricter product-fidelity restaging flow for Meta creative:

1. Product anchor selection
   - Require exact Shopify product handle.
   - Pull featured image or approved product image from Shopify Admin API.
   - Store source image path and product metadata in the manifest.

2. Restaging mode
   - Prefer true image-to-image or scene-restage mode if Nano Banana exposes it.
   - Avoid pure full-regeneration mode for product ads.
   - If available, increase image guidance or reference strength.
   - If available, reduce denoise or scene transformation strength.

3. Prompt hardening
   Add this locked block before scene instructions:

   ```text
   PRODUCT FIDELITY LOCK: Preserve the exact ring from the source product image. Do not invent, redesign, recolor, resize, simplify, or move the inlay. The output ring must match the source product's inlay material, color layout, profile, finish, edge shape, and visible construction. If the source feature is inside the band, keep it inside the band. The lifestyle scene may change, but the ring identity may not.
   ```

4. Fidelity QA gate
   After generation, compare source image and output for:
   - Inlay material
   - Inlay placement
   - Color layout
   - Band profile and thickness
   - Finish, brushed versus polished
   - Edge shape
   - Overall recognizability

5. Auto-reject logic
   - If fidelity is not PASS, reject before general QA.
   - Retry with tighter product crop and stricter fidelity prompt.
   - If it fails twice, mark the variant not recommended and do not hide the issue.

## Suggested implementation shape

Pseudo-flow:

```text
for each creative variant:
  product = Shopify Admin productByHandle(handle)
  assert product.status == ACTIVE and product.totalInventory > 0
  source_image = download(product.featuredImage.url)
  output = nano_banana.scene_restage(
    image=source_image,
    mode="scene-restage" if available,
    image_guidance="high" if available,
    prompt=PRODUCT_FIDELITY_LOCK + scene_prompt
  )
  fidelity = compare_product_fidelity(source_image, output, product.expected_visual_traits)
  if fidelity fails:
    retry with tighter crop and stronger lock
  run text/logo/hand QA only after fidelity passes
```

## Test plan before briefs 2, 3, and 4

1. Build a two-product test set:
   - TYPHOON because it has inside red burl wood and blue tungsten, making drift easy to detect.
   - AVITUS because the blue and black carbon fiber feature is externally visible.

2. Generate one lifestyle restage per product with no ad usage.

3. Run source-versus-output fidelity QA before normal image QA.

4. Acceptance criteria:
   - TYPHOON keeps blue tungsten exterior and red burl wood inside or visibly faithful to source construction.
   - AVITUS keeps black ceramic body and blue/black carbon fiber inlay.
   - No logos, no readable text, no bad hand anatomy.
   - 1080x1350 final crop.

5. If TYPHOON still drifts, do not use inside-feature products for seeded lifestyle ads until a stronger product-preservation mode is confirmed. Use products with visible exterior inlays instead.

## Decision needed

Amir approval is needed before changing code or switching Nano Banana modes. This document is investigation only.
