# Owner-Selected 24-Article Authority Expansion

**Selection date:** 2026-09-02
**Status:** All 24 structured sources complete: 20 in editorial review and four in exact-version clinical review; no expansion pages generated or added to the public sitemap

The owner selected exactly 24 new article topics from the supplied v2 sitemap. The v2 builder, legacy domain, contact details, office claim, design code and sitemap remain rejected. These topics are recorded as `planned-research` so the site can establish topical authority without weakening the approved architecture or publishing incomplete material.

All 24 proposed article bodies are now accounted for: 16 are contained in `master-betta-site-package v3.md`, and the remaining eight are contained in `compiled-eight-articles.md`. Presence is not approval; all 24 remain blocked from generated output until their evidence, claims, review, links and media pass the promotion requirements below.

The first seven controlled batches completed 14 structured sources across care, behavior, form, welfare, sleep, environment, maintenance, habitat and taxonomy. Six further controlled batches converted the final 10 topics: color and color change; sex identification and breeding; growth; price; velvet and columnaris; and dropsy and buoyancy disorders. Twenty non-clinical sources are held at `planned-editorial-review`. The four new disease-treatment sources are held at `planned-clinical-review`, with exact hashes recorded for Robert Martinez, DVM. No selected expansion article remains at `planned-research`.

## Controlled topical map

| Parent hub | Planned URL | Primary role | Risk / required review |
|---|---|---|---|
| Care | `/care/tank-setup/` | Safe setup sequence | Animal welfare / Kate Barrington |
| Care | `/maintenance/water-change/` | Test-led maintenance | Animal welfare / Kate Barrington |
| Care | `/care/indian-almond-leaves/` | Evidence and claim limits | Animal welfare / Kate Barrington |
| Care | `/care/heaters-calibration/` | Temperature calibration | Animal welfare / Kate Barrington |
| Care | `/aquascaping/fin-safe-plants/` | Plant safety and selection | Animal welfare / Kate Barrington |
| Care | `/sensory/light-requirements/` | Light-dark cycle | Animal welfare / Kate Barrington |
| Care | `/economics/betta-fish-price/` | Ownership cost context | Ordinary, date-sensitive / Kate Barrington |
| Diseases | `/diseases/dropsy-treatment/` | Symptom cluster and escalation | High-risk health / Robert Martinez, DVM |
| Diseases | `/diseases/velvet-treatment/` | Identification and escalation | High-risk health / Robert Martinez, DVM |
| Diseases | `/diseases/columnaris-treatment/` | Urgent recognition and escalation | High-risk health / Robert Martinez, DVM |
| Diseases | `/anatomy/swim-bladder-treatment/` | Buoyancy-disorder triage | High-risk health / Robert Martinez, DVM |
| Biology & genetics | `/behavior/unhappy-betta/` | Welfare observations | Animal welfare / Kate Barrington |
| Biology & genetics | `/anatomy/betta-fish-sleep/` | Normal rest behavior | Ordinary / Kate Barrington |
| Biology & genetics | `/behavior/hearing-music/` | Sound and vibration | Ordinary / Kate Barrington |
| Biology & genetics | `/behavior/flaring-triggers/` | Trigger and stress distinctions | Animal welfare / Kate Barrington |
| Biology & genetics | `/breeding/pairing-fry-care/` | Welfare-first breeding decisions | Animal welfare / Kate Barrington |
| Biology & genetics | `/breeding/gender-identification/` | Multi-trait sex identification | Ordinary / Kate Barrington |
| Biology & genetics | `/origins/wild-habitats/` | Habitat and care context | Ordinary / Kate Barrington |
| Biology & genetics | `/morphology/growth-rate-size/` | Size and growth variation | Ordinary / Kate Barrington |
| Biology & genetics | `/biology-genetics/species/` | Domestic and wild diversity | Ordinary / Kate Barrington |
| Biology & genetics | `/biology-genetics/colors/` | Color and pattern terminology | Ordinary / Kate Barrington |
| Biology & genetics | `/biology-genetics/color-change/` | Normal change versus warning signs | Animal welfare / Kate Barrington |
| Biology & genetics | `/biology-genetics/plakat-betta/` | Short-fin form and care | Ordinary / Kate Barrington |
| Biology & genetics | `/biology-genetics/giant-betta/` | Size terminology and space needs | Animal welfare / Kate Barrington |

## Source-to-output control

Every topic now has a permanent JSON source and explicit future output path in `data/page-registry.csv`. The audit fails if a source appears while its registry status is still `planned-research`, if a planned source is emitted before approval, or if a clinical-review candidate hash changes without an updated review record.

No new standalone hubs are introduced. All 24 topics inherit ownership from one of the three existing relevant hubs, preventing orphan mini-silos while preserving the exact selected article URLs.

## Promotion requirements for each article

An article may move beyond its current blocked review state only after all of the following exist:

1. A complete structured source file in the permanent content directory.
2. Query, entity, intent, overlap and cannibalization evidence.
3. Claim-level citations and freshness classification.
4. Farrukh Abdullah authorship and the assigned review record.
5. Robert Martinez, DVM, approval for the four high-risk health topics.
6. An approved hero-media row, filename, alt text, caption, crop plan and ImageObject mapping—or an explicit approved image-free decision.
7. Internal links from the parent hub and at least one contextually related article, with reciprocal links where useful.
8. Successful build, generated-output inspection, exact diff review and representative mobile/desktop preview QA.

Until these conditions are met, none of the 24 pages belongs in the generated sitemap or deployment candidate.
