# Three New Articles — Hero Media Specifications

Date: 2026-09-19  
Branch: `chatgpt-work`  
Status: **Pre-promotion media brief only**

Global production standard:
- 1600×900
- 16:9
- WEBP
- one unique article hero per URL
- no text inside the image
- no logos or watermark
- no fighting, injury, distress or implied cohabitation
- keep the complete fish and fin edges visible
- natural aquarium lighting
- avoid reusing fish, layout or focal composition from existing heroes

---

## 1. Bubble Nests

Candidate URL: `/behavior/bubble-nests/`  
Proposed asset ID: `bubble-nests-hero`  
Proposed source file: `assets/source/betta-bubble-nest-surface-behavior.webp`  
Proposed output file: `public/assets/images/betta-bubble-nest-surface-behavior.webp`

### Production prompt

Photorealistic natural-history editorial image of one healthy adult male Betta splendens alone in a calm planted aquarium, positioned beneath a clearly visible cluster of small natural bubble-nest bubbles at the water surface. Use a short- to medium-finned blue-and-rust domestic male that is visually distinct from existing site heroes. Include a few floating plant roots or a broad leaf near the surface for context, open surface access, gentle aquarium lighting and realistic bubble size. The fish should be prominent but not touch the nest. No female fish, eggs, fry, breeding embrace, aggression, labels, text, logos or watermark. Do not imply that the nest proves happiness or health. Premium documentary aquarium photography, 1600×900, 16:9.

### Alt text

Male betta beneath a natural bubble nest at the aquarium surface

### Caption

Male Betta splendens can build bubble nests while housed alone; the nest is reproductive behavior, not a standalone welfare score.

### Description

Documentary hero showing one healthy male domestic Betta splendens beneath a natural surface bubble nest in a calm aquarium, with open surface access and minimal floating vegetation. The image illustrates bubble-nest behavior without showing a female, spawning or eggs and without implying that nest presence proves health or happiness.

### Focal / crop

- focal point: right or center-right fish, nest visible above
- preserve full fish and complete bubble cluster
- reserve some negative space on the left
- no forced crop

---

## 2. Betta Fish Enrichment

Candidate URL: `/behavior/enrichment-safe-toys/`  
Proposed asset ID: `enrichment-safe-toys-hero`  
Proposed source file: `assets/source/betta-enriched-aquarium-exploration.webp`  
Proposed output file: `public/assets/images/betta-enriched-aquarium-exploration.webp`

### Production prompt

Photorealistic welfare-first editorial scene of one healthy adult Betta splendens exploring a thoughtfully furnished aquarium. Show a visually distinctive copper-green short-finned betta moving through open swimming space beside soft live plants, one broad resting leaf, smooth natural wood or a smooth open refuge, and a clear unobstructed route to the surface. The aquarium should look enriched but not cluttered. Avoid mirrors, exercise devices, plastic novelty toys, tight tunnels, sharp decor, food, another fish, hands or forced contact. The fish should appear calm and able to choose between open space, shelter and resting structure. Natural daylight-balanced aquarium lighting, 1600×900, 16:9, no text, labels, logos or watermark.

### Alt text

Betta exploring a planted aquarium with open swimming space and safe resting areas

### Caption

Useful enrichment starts with safe environmental complexity, choice and open swimming space—not forced interaction with novelty objects.

### Description

Welfare-focused hero of one domestic Betta splendens in a planted, structurally enriched aquarium with open swimming routes, broad resting leaves, a smooth refuge and clear surface access. The scene avoids mirrors, forced-contact devices and toy clutter.

### Focal / crop

- focal point: left-center or center fish
- preserve open surface, resting leaf and refuge
- leave visible open water so the tank does not look overcrowded
- no forced crop

---

## 3. Types of Betta Fish

Candidate URL: `/biology-genetics/betta-fish-types/`  
Proposed asset ID: `betta-fish-types-hero`  
Proposed source file: `assets/source/domestic-betta-types-comparison.webp`  
Proposed output file: `public/assets/images/domestic-betta-types-comparison.webp`

### Production prompt

Premium natural-history editorial comparison showing four anatomically credible domestic Betta splendens in four clearly separated visual panels or aquarium windows, each fish alone. Use distinct forms so the image communicates that “type” can describe different domestic traits: one blue Halfmoon with broad caudal fin, one red Crowntail with clearly separated fin rays, one red-white-black koi-pattern Plakat with short fins, and one larger-bodied teal Giant-type short-finned domestic betta. Keep all fish at visually balanced scale without implying exact equal body size. Use clean neutral aquarium backgrounds and consistent daylight-balanced lighting. No wild species, no shared tank, no fighting, no labels, no arrows, no price/show ribbons, no text, no logos or watermark. 1600×900, 16:9.

### Alt text

Four domestic bettas showing different tail forms, colors and body forms in separate panels

### Caption

Domestic betta “types” can describe different traits such as fin form, color pattern and body form; those labels are not automatically separate species.

### Description

Four-panel editorial comparison of distinct domestic Betta splendens forms: Halfmoon, Crowntail, koi-pattern Plakat and a larger-bodied Giant-type fish. Separate panels prevent any implication of cohabitation and visually support the article's distinction between domestic forms and true species.

### Focal / crop

- equal panel weight
- preserve complete fish and fin edges
- do not imply identical physical scale
- no forced crop

---

## Manifest rule

Do not add any of these rows to `data/media-manifest.csv` until:
1. the corresponding article exact version is editorially approved;
2. the final hero file exists;
3. dimensions, byte size and SHA-256 checksum are known;
4. visual QA confirms uniqueness and species/form accuracy.

At promotion, use:
- role: `article-hero`
- credit: `Owner-created`
- rights status: `owner-supplied`
- approved: `true`
- status: `approved`
