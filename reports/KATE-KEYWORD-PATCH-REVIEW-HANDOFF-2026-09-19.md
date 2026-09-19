# Kate Barrington Editorial Patch Review Handoff — Keyword Reconciliation

Date: 2026-09-19  
Branch: `chatgpt-work`  
Scope: **Five exact proposed revisions**  
Clinical review requested: **No, provided the wording is approved as drafted and no medical meaning is added**

## Important review rule

These are review copies only. The approved source files under `content/pages/` have **not** been changed.

If an item is approved, apply only the approved diff to the source file, then regenerate its exact-version hash and update the editorial review evidence.

---

## Item 1 — Female Sorority H1

Original:
- `content/pages/female-sorority.json`
- original blob: `97825e8e2f404b4dfc18c2db8d9a6519fd4442a9`

Review copy:
- `drafts/revisions/female-sorority-editorial-revision.json`
- review blob: `debde24089108983fc8240a83878d8f6425f7fe4`

### Exact change

Only the H1 changes.

**Before**

How to Set Up a Female Betta Sorority: Tank Size & Hierarchy Rules

**After**

Can Female Bettas Live Together? Sorority Risks, Warning Signs & Separation Planning

No body, FAQ, source, title, description, URL, hero or health wording changes.

---

## Item 2 — Unhappy Betta: top-of-tank FAQ

Original:
- `content/pages/unhappy-betta.json`
- original blob: `008d86e494841f750de053587e2e0e1fc35f1b58`

Review copy:
- `drafts/revisions/unhappy-betta-top-of-tank-editorial-revision.json`
- review blob: `e0fa72de70ff86042a797e68b01d651ef44a2467`

### Exact addition

Add one FAQ immediately after the existing bottom-of-tank FAQ:

**Question:** Why is my betta staying at the top of the tank?

**Answer:** Bettas normally visit the surface to breathe and may also rest near the top, so surface position alone is not a diagnosis. A persistent change from the fish's usual pattern deserves a check of temperature, ammonia, nitrite, nitrate, pH, filter operation, appetite and swimming. Seek qualified help when the change occurs with abnormal breathing, loss of balance, injury, appetite loss or other persistent signs.

Sources: existing local sources 3 and 4.

No diagnostic label or treatment protocol is added.

---

## Item 3 — Gender Identification: broaden female-betta query coverage

Original:
- `content/pages/gender-identification.json`
- original blob: `a98f7fd6b37e6031e2a58fa719eaaa26bcbc533b`

Review copy:
- `drafts/revisions/gender-identification-female-query-editorial-revision.json`
- review blob: `770e15424e1845f82d6accde83b6687b679c2e2e`

### Metadata/H1 changes

**Title**
- Before: Male vs Female Betta Fish: Identification Guide | BettaFish.website
- After: Female Betta Fish vs Male: Identification, Differences and Care | BettaFish.website

**Description**
- Revised to include identification, behavior and shared care needs while preserving uncertainty.

**H1**
- Before: Male vs Female Betta Fish: How to Identify Sex
- After: Female Betta Fish vs Male: Identification, Differences & Care

**Intro**
- Broadened to state that males and females share the same core species-level husbandry while sex can affect reproductive anatomy and some behavior.

### New bounded sections

1. **Do female bettas need different care?**
   - same core species-level aquarium system;
   - no separate female temperature/water/feeding target;
   - individual fin form, age, health and behavior still matter;
   - female sex does not make cohabitation automatically safe.

2. **Are female bettas less aggressive than males?**
   - females can flare, chase and show aggression;
   - sex/strain variation exists;
   - sex does not predict one individual's temperament;
   - female sex is not a compatibility guarantee.

### New FAQs

- Are female bettas smaller than males?
- What types of female bettas are there?

### Boundaries

Still excluded:
- sorority setup;
- community tank-mate matrix;
- complete routine care;
- growth guide;
- color/pattern taxonomy;
- tail-type comparison.

This keeps `/compatibility/female-sorority/` and the other child owners intact.

---

## Item 4 — Tank Setup: handling/touching FAQ

Original:
- `content/pages/tank-setup.json`
- original blob: `987f9b02c3f4e52ff3cb20ec79ccfee6c06f61b5`

Review copy:
- `drafts/revisions/tank-setup-handling-faq-editorial-revision.json`
- review blob: `3dec8af6105c27abf4b251ad7db0e9ac4faddcee`

### Exact FAQ addition

**Question:** Can you touch a betta fish?

**Answer:** Routine touching is unnecessary. Fish skin and mucus are important protective barriers, and veterinary guidance recommends minimizing direct restraint. If a fish must be handled for a procedure, contact should be gentle and brief; for ordinary aquarium transfers, use appropriate fish-transfer equipment rather than holding the fish in your hand.

### Source addition

Add local source 6:

**Management of Aquarium Fish**  
Merck Veterinary Manual  
https://www.merckvetmanual.com/exotic-and-laboratory-animals/aquarium-fish/management-of-aquarium-fish

This URL is already represented in the global source register as SRC-064.

### Deliberately not added

The PAA query about a betta bite/finger is **not** included in the exact patch set because the current authoritative evidence set does not cleanly support a useful Betta-specific bite-risk answer without drifting into unsupported human-injury claims.

---

## Item 5 — Diet & Feeding: exact-query PAA FAQs

Original:
- `content/pages/diet-feeding.json`
- original blob: `e20d83289a62a744237507e3b8de71afd74c3662`

Review copy:
- `drafts/revisions/diet-feeding-paa-editorial-revision.json`
- review blob: `0b89caa429f8a0ac05999b7e986d63a65210aa64`

### New FAQs

**How can I tell if my betta is hungry?**

An eager feeding response does not prove that a betta is underfed. Use a measured routine, follow the food label, watch whether the fish finishes the portion without repeated leftovers, and track body condition over time rather than feeding continuously because the fish approaches the glass.

**How many pellets should I feed my betta?**

There is no universal pellet count. Pellet diameter, density and formulation vary by brand, while fish size, age and condition also differ. Start with the product's betta-specific directions and adjust from the fish's response rather than using one fixed number for every food.

**Can betta fish eat human food?**

Human food should not replace a complete species-appropriate betta diet. Use food formulated for carnivorous bettas as the regular staple and avoid building the routine diet around kitchen foods that were not formulated for aquarium fish.

Existing local sources 1 and 2 support the additions.

No disease treatment, medicated-food protocol or toxicity list is added.

---

## Approval response format

For each item, record one of:

- **Approved as submitted**
- **Approved with requested changes** — include exact requested wording
- **Not approved** — include reason

## After approval

For each approved item:

1. apply only the accepted diff to `content/pages/`;
2. preserve all unrelated copy;
3. compute the new exact source SHA-256;
4. update the editorial review register/evidence;
5. rebuild and run audit;
6. verify no new keyword-owner conflict;
7. keep sitewide prepublication indexing controls unchanged.
