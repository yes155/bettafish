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

## Class B — editorial reapproval required

### B1. Female sorority H1
Priority: P1

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
8. Defer Teeth/Anatomy and additional treatment pages.
9. Re-run build/audit after report-layer or registry changes.
10. Keep site noindex until the separate deployment/launch gates pass.

## Do not do

- Do not rewrite all 34 articles.
- Do not add words for “topical authority.”
- Do not create a URL for every spreadsheet cluster.
- Do not merge clinically reviewed pages because they share symptom vocabulary.
- Do not alter hash-locked sources under the guise of internal-link cleanup.
