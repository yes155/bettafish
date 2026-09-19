# Kate Barrington Editorial Review Handoff — Semantic Upgrade Set

Date: 2026-09-19  
Branch: `chatgpt-work`  
Scope: **Three editorial items only**  
Clinical review requested: **No**

## Review item 1 — Female Sorority H1 only

Current source: `content/pages/female-sorority.json`  
Current source blob: `97825e8e2f404b4dfc18c2db8d9a6519fd4442a9`  
Proposal file: `reports/FEMALE-SORORITY-H1-REAPPROVAL-PROPOSAL.md`

**Current H1**

How to Set Up a Female Betta Sorority: Tank Size & Hierarchy Rules

**Proposed H1**

Can Female Bettas Live Together? Sorority Risks, Warning Signs & Separation Planning

Requested review: approve or reject the H1 change only. No body, FAQ, source, URL, hero or health-language change is requested.

## Review item 2 — Bubble Nests draft

Draft source: `drafts/pages/bubble-nests.json`  
Git blob: `a01d7aaa3a7b34c6e17084734924740a07446f3b`  
Research brief: `reports/BUBBLE-NESTS-RESEARCH-BRIEF.md`  
Candidate URL: `/behavior/bubble-nests/`  
Status: draft only; not registered for build; non-indexable

### Editorial task

Review:
- factual accuracy and source-to-claim fit;
- H1/introduction match to “betta bubble nest” intent;
- the boundary that a bubble nest is **not** a standalone happiness or health test;
- separation from the existing breeding/fry-care owner;
- clarity around eggs, paternal care and male nest construction;
- any wording that overstates evidence.

### Evidence set

- SRC-021 — Betta husbandry and paternal care
- SRC-041 — housing/furnishing study including nest-building observations
- SRC-054 — Betta bubble-nesting vs mouthbrooding evolution
- SRC-072 — bubble-nest mucus/pharyngeal-organ study
- SRC-073 — 2025 reproductive review

No clinical treatment guidance is included.

## Review item 3 — Enrichment and Safe Toys draft

Draft source: `drafts/pages/enrichment-safe-toys.json`  
Git blob: `2d07f5c270ffa9ffee261b85d4f5960ffa5b27f6`  
Research brief: `reports/ENRICHMENT-SAFE-TOYS-RESEARCH-BRIEF.md`  
Candidate URL: `/behavior/enrichment-safe-toys/`  
Status: draft only; not registered for build; non-indexable

### Editorial task

Review:
- factual accuracy and welfare framing;
- whether the article stays principles-based rather than becoming a product roundup;
- physical-safety screening criteria;
- the mirror/reflection handoff to the existing flaring article;
- the boundary that interaction with an object does not prove welfare benefit;
- wording around the 2026 tactile-stimulation study;
- any anthropomorphic or unsupported “boredom/happiness” language.

### Evidence set

- SRC-041 — tank size/furnishings and behavior
- SRC-042 — space/environmental enrichment and behavior
- SRC-035 — mirror endocrine/aggression response
- SRC-037 — individual variability in mirror response
- SRC-074 — 2026 tactile-stimulation Betta study

No product endorsement, medication, dosage or disease-treatment guidance is included.

## Exact-version handling

These drafts must not be moved into `content/pages/`, added to the review registers as approved, or promoted in `data/page-registry.csv` until editorial approval is documented.

After approval:
1. apply only requested editorial changes;
2. freeze the approved exact files;
3. calculate and record source SHA-256 hashes in the editorial review register;
4. create unique hero assets and media-manifest rows;
5. add planned registry ownership with unique primary queries;
6. run build and audit;
7. keep sitewide noindex until separate production gates pass.

## Requested response format

For each item, record:
- **Approved as submitted**, or
- **Approved with requested changes**, followed by exact requested changes, or
- **Not approved**, with the reason.

For the Female Sorority item, review only the proposed H1 unless a separate broader review is explicitly requested.
