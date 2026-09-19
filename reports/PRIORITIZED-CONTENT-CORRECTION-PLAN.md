# BettaFish.website Prioritized Content Correction Plan

Date: 2026-09-19
Branch: chatgpt-work

## Principle

Do not invalidate exact-version approvals for cosmetic gains. Fix ownership and metadata first, then use non-substantive linking where possible. Reopen source content only when the semantic benefit is material.

## Class A — normally no new content approval required

### A1. Fix Compatibility hub keyword ownership
Priority: P0

- Current registry primary query for /compatibility/: **betta fish tank mates**
- Proposed registry primary query: **betta fish compatibility**
- Keep /compatibility/tank-mates/ as owner of **best betta fish tank mates** and broad companion comparison.

Why: this removes the only material hub/child keyword ownership conflict without rewriting approved copy.

### A2. Document canonical ownership for high-risk overlaps
Priority: P0

Record:
- tank size/bowls -> /care/tank-setup/
- absence feeding -> /care/diet-feeding/
- fin regrowth -> /diseases/fin-rot/
- plants -> /aquascaping/fin-safe-plants/
- lifespan -> /biology-genetics/lifespan/

### A3. Add non-substantive contextual handoffs
Priority: P1

Target older foundation pages:
- water-parameters -> tank-setup, heaters-calibration, water-change
- diet-feeding -> water-parameters, swim-bladder triage where relevant
- filtration -> tank-setup, water-parameters
- diagnostic-matrix -> condition-specific clinical guides
- fin-rot -> diagnostic-matrix, water-parameters
- ich -> diagnostic-matrix, water-parameters
- tank-mates -> female-sorority
- lifespan -> related biology/care owner
- tail-types -> Plakat and relevant care owner

Implementation constraint: if the only way to add these links is to edit a hash-locked JSON source, do not make the edit under Class A. Either add a derived/non-source link layer or move that item to Class B.

### A4. Preserve clinical source wording
Priority: P0

Do not change diagnosis, treatment, medication, dosage, temperature, urgency, prognosis or escalation language. No clinical reapproval is justified by this semantic audit.

### A5. Broaden Heater query ownership
Priority: P0  
Status: **Completed**

- Registry owner changed from `betta fish heater calibration` to **`betta fish heater`**.
- Existing article already covers heater need, selection, sizing, placement, calibration and verification.
- No approved source copy changed.

Why: the new Keyword Planner file shows materially broader demand around the generic heater task, while the current page already fulfills it.

## Class B — editorial reapproval required

### B1. Female sorority H1
Priority: P1  
Status: **Approved and applied 2026-09-19**

**Before**
How to Set Up a Female Betta Sorority: Tank Size & Hierarchy Rules

**Proposed after**
Can Female Bettas Live Together? Sorority Risks, Warning Signs & Separation Planning

Why: the current article repeatedly states that no tank size/group number guarantees safety. The visible H1 should reflect the actual decision task rather than imply a reliable setup formula.

Scope: H1 only initially. Do not rewrite the already cautious body unless the editor requests it.

### B2. Water-conditioner bounded expansion
Priority: P2

Only if keyword mapping requires stronger coverage, add a short section/FAQ to /care/water-parameters/ covering:
- chlorine vs chloramine;
- conditioner label matching;
- actual treated volume;
- why a conditioner is not a universal fix for every source-water problem.

Do not create a new page first.

### B3. Guppy compatibility bounded expansion
Priority: P2

Only if evidence supports it, add a concise guppy-specific row/section to /compatibility/tank-mates/. Keep the main task as risk assessment and separation planning. Do not create a new URL first.

### B4. Net-new Bubble Nests article
Priority: P1 future content  
Status: **Research brief complete** — see `reports/BUBBLE-NESTS-RESEARCH-BRIEF.md`

Requirements:
- unique query/task;
- clear “nest does not prove happiness” boundary;
- link to breeding guide;
- editorial sources/review;
- unique hero image.

### B5. Net-new Enrichment and Safe Toys article
Priority: P1 future content  
Status: **Research brief complete** — see `reports/ENRICHMENT-SAFE-TOYS-RESEARCH-BRIEF.md`

Requirements:
- welfare-first selection criteria;
- fin/entrapment hazard checks;
- observation/stopping conditions;
- no unsupported “toy improves intelligence/happiness” claims;
- editorial review;
- unique hero image.

### B6. Net-new Betta Fish Types overview
Priority: P1 future content  
Status: **Research brief and non-publishing draft complete**

Files:
- `reports/BETTA-FISH-TYPES-RESEARCH-BRIEF.md`
- `drafts/pages/betta-fish-types.json`

Requirements:
- explain that “type” is an umbrella term, not a single scientific category;
- separate tail form, color/pattern, body form, sex and true species;
- keep Tail Types, Colors, Species, Plakat, Giant and Gender Identification as canonical child owners;
- avoid rarity/sales rankings;
- editorial review required;
- unique hero image required.

### B7. Rising symptom-intent expansion
Priority: P1  
Status: **Approved and applied 2026-09-19** — top-of-tank FAQ added; bottom/not-eating remain consolidated under existing owners

- keep bottom/top/not-eating variants under existing behavior/triage owners;
- add only a bounded “staying at top” FAQ first;
- do not create thin symptom URLs;
- do not alter clinically reviewed pages in this round.

### B8. Female Betta broad-query expansion
Priority: P2  
Status: **Approved and applied 2026-09-19** — Gender Identification broadened to female-vs-male differences and shared care

- test broadening `/breeding/gender-identification/` before creating a new URL;
- keep Sorority as female-group owner;
- keep routine care, size and compatibility with their existing canonical owners.

### B9. PAA care FAQ expansion
Priority: P2  
Status: **Approved and applied 2026-09-19** — touching FAQ added to Tank Setup; hunger/pellet/human-food FAQs added to Diet; bite FAQ remains deferred

- handling/touch/bite -> Tank Setup;
- hunger/pellet/human-food variants -> Diet & Feeding;
- no standalone PAA pages.

## Class C — clinical reapproval required

**No Class C correction is recommended from this audit.**

Trigger Class C only if a future edit changes:
- disease differentiation;
- diagnosis language;
- medication/dose;
- temperature/treatment protocol;
- prognosis;
- urgency or veterinary-escalation guidance;
- a new health-treatment page.

## Recommended correction order

1. Registry ownership correction for Compatibility hub.
2. Freeze all approved clinical wording.
3. Implement contextual handoffs through a non-source layer if available.
4. Submit only the Female Sorority H1 change for editorial reapproval.
5. Update keyword ownership documentation for conditioner and guppy decisions.
6. Bubble Nests research/source brief — **completed**.
7. Enrichment/Safe Toys research/source brief — **completed**.
8. Betta Fish Types research brief and draft — **completed**; submit with the current Kate editorial batch.
9. Defer Teeth/Anatomy and additional treatment pages.
10. Re-run build/audit after report-layer or registry changes.
11. Keep site noindex until the separate deployment/launch gates pass.

## Exact keyword editorial patch handoff

Prepared: `reports/KATE-KEYWORD-PATCH-REVIEW-HANDOFF-2026-09-19.md`

This handoff contains five exact review copies and must be treated as approval-gated. No corresponding `content/pages/` source has been changed.

## Do not do

- Do not rewrite all 34 articles.
- Do not add words for “topical authority.”
- Do not create a URL for every spreadsheet cluster.
- Do not merge clinically reviewed pages because they share symptom vocabulary.
- Do not alter hash-locked sources under the guise of internal-link cleanup.
