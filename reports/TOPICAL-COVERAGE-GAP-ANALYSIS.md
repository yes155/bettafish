# BettaFish.website Topical Coverage Gap Analysis

Date: 2026-09-19
Branch: chatgpt-work

## Coverage map

| Area | Established owners | Status | Missing/weak elements | Decision |
|---|---|---|---|---|
| Care and tank setup | /care/, tank-setup, water-parameters, filtration, heater, diet, water-change, plants, lighting, almond leaves | Strong | Conditioner query is only partly surfaced as its own decision task; older foundation pages need more cross-links. | Water conditioner: MERGE INTO EXISTING OWNER |
| Diseases and health | /diseases/, diagnostic matrix, fin rot, ich, dropsy, velvet, columnaris, buoyancy | Strong | Additional disease pages would require clinical review; no urgent semantic prerequisite gap found. | DEFER new treatment pages |
| Compatibility | /compatibility/, tank-mates, female-sorority | Moderate-strong | Hub keyword ownership conflicts with tank-mates article; species-pair depth is limited. | Fix hub query; guppy page MERGE INTO EXISTING OWNER for now |
| Biology and genetics | biology hub, species, lifespan, tail types, colors, color-change, Plakat, Giant, growth | Strong | No major prerequisite gap. | COVERED |
| Behavior | flaring, hearing/music, unhappy/welfare, sleep (adjacent) | Moderate | Bubble-nest interpretation and enrichment/safe-toy tasks are not fully owned. | Two NEW PAGE CANDIDATES |
| Anatomy | sleep, buoyancy, morphology-related pages | Partial | Teeth/anatomy query is unowned but low priority; no need to force a thin anatomy cluster. | DEFER teeth page |
| Breeding | pairing-fry-care, gender identification | Moderate | Bubble nests are only a subtopic inside broader breeding. | Bubble nests: NEW PAGE CANDIDATE |
| Habitat and origins | wild-habitats, species | Strong | No meaningful gap for launch. | COVERED |
| Aquascaping | fin-safe plants + tank-setup decor guidance | Adequate for current scope | Substrate/hides/decor exist as setup concerns rather than separate tasks. | MERGE INTO EXISTING OWNER |
| Cost and ownership | betta-fish-price + tank-setup equipment planning | Adequate | No separate ownership-cost page needed now. | COVERED |

## Confirmed gap decisions

### 1. Betta bubble nests
**Classification:** NEW PAGE CANDIDATE

Why it qualifies:
- distinct user task: what a bubble nest means, when eggs are involved, and what it does not prove;
- distinct primary query;
- enough behavioral/reproductive evidence can support a useful article;
- can link to breeding without duplicating the entire breeding workflow;
- should explicitly reject “bubble nest = happy/healthy” as a universal rule.

Parent: Biology/Genetics initially, with a behavioral cross-link.  
Approval: Editorial. Clinical only if health/treatment claims are introduced.  
Media: Unique hero required.

### 2. Betta enrichment and safe toys
**Classification:** NEW PAGE CANDIDATE

Why it qualifies:
- distinct welfare decision task;
- current behavior pages do not own physical/cognitive enrichment selection;
- useful article can cover fin/entrapment safety, novelty, observation and stopping conditions without product-ranking content.

Parent: Biology/Genetics until a future Behavior hub is justified.  
Approval: Editorial.  
Media: Unique hero required.

### 3. Betta water conditioner
**Classification:** MERGE INTO EXISTING OWNER

The current Water Parameters article already explains chlorine/chloramine treatment and label-based conditioner use, and Tank Setup also needs conditioner as part of first-fill preparation. A bounded section/FAQ and stronger query mapping should be tested before creating a competing URL.

Canonical owner: /care/water-parameters/  
Supporting owner: /care/tank-setup/

### 4. Guppies with bettas
**Classification:** MERGE INTO EXISTING OWNER

This is a species-pair compatibility question, but the current Tank Mates article is specifically designed to compare companion risks. Add a bounded guppy row/section only if evidence is sufficient. Create a separate URL only if later SERP/research shows a materially different task and enough depth to avoid a thin species-pair article.

Canonical owner: /compatibility/tank-mates/

### 5. Betta teeth/anatomy
**Classification:** DEFER

This is distinct enough to be a future anatomy explainer, but it is lower priority than welfare/behavior gaps and does not unlock a missing prerequisite for the current site.

## Weak semantic bridges

- Older foundation articles have fewer contextual in-body links than the September 2026 correction set.
- Tank Mates should hand off directly to Female Sorority.
- Water Parameters should hand off more clearly to Heater Calibration, Water Change and Tank Setup.
- Clinical triage pages should hand off to the Diagnostic Matrix and vice versa without changing clinical advice.

## Overdeveloped vs underdeveloped

**Most developed:** care/setup, health, biology/genetics.  
**Least developed:** behavior as a category and anatomy as a standalone cluster.

A new Behavior hub is **not** recommended yet. Defer that architecture change until at least Bubble Nests and Enrichment are approved and there is enough child depth to justify a hub.
