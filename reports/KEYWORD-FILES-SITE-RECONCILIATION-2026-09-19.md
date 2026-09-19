# BettaFish.website Keyword Files × Site Reconciliation

Date: 2026-09-19  
Branch: `chatgpt-work`

## Scope

This report reconciles three owner-supplied keyword datasets against the current BettaFish.website page registry, approved article set, keyword-ownership map, cannibalization register and the two new behavior drafts.

Datasets reviewed:

1. `google kw planner data.csv`
2. `google trends rising queries.csv`
3. `PAA-Extractor-betta-fish-2026-08-30.csv`

No approved article source was changed during this analysis.

---

## 1. Data quality and how to use the files

### Google Keyword Planner

- 523 rows.
- 523 unique keyword strings.
- The export uses extremely coarse search-volume buckets: 0, 50, 500, 5,000, 50,000 and 500,000.
- Currency is SAR.
- 29 rows show a positive three-month or YoY change.
- The summed search volume must **not** be treated as market size because close variants and overlapping intents are counted independently and the values are bucketed.

Use the file primarily for:
- cluster-level demand;
- relative priority;
- commercial-intent detection;
- discovering missing query families.

Do not use it for:
- precise traffic forecasts;
- deciding that every 5,000-volume variant deserves its own URL;
- multiplying all keyword volumes into a market-size estimate.

### Google Trends rising queries

- 50 rows.
- Several rows are generic fish/species terms rather than Betta-specific search tasks.
- Large percentage increases can come from tiny baselines. For example, several 180–350% rising queries have search-interest values of 0–1.
- The best use is to identify directional changes that should be checked against existing ownership, not to create pages from percentage growth alone.

### PAA extraction

- 64 rows.
- 58 unique questions.
- Repeated questions include:
  - “Why can't you touch betta fish?” — 4 occurrences;
  - “Are bettas happier alone?” — 2;
  - “What's the rarest betta color?” — 2;
  - “Do betta fish like to be talked to?” — 2.
- The PAA file contains considerable generic-fish noise. Questions that do not concern Bettas should not expand the topical map.

---

## 2. What the keyword files validate in the existing site

The current architecture already owns most of the strongest high-demand care queries.

| Keyword family | Directional demand in file | Current owner | Decision |
|---|---:|---|---|
| Betta tank / aquarium / 5-gallon tank | 50,000 bucket variants | `/care/tank-setup/` | KEEP |
| Betta fish food | 50,000 | `/care/diet-feeding/` | KEEP |
| Betta heater / aquarium heater | 50,000 | `/care/heaters-calibration/` | KEEP, broaden registered query |
| Female betta fish | 50,000 | split between gender + sorority | WEAK OWNER; resolve |
| Betta fish for sale | 50,000 | none | EXCLUDE commercial |
| Betta fish fighter | 50,000 | species/origins context | MERGE, no new URL |
| Plants for bettas | multiple 5,000 variants | `/aquascaping/fin-safe-plants/` | KEEP |
| Filters | multiple 5,000 variants | `/care/filtration/` | KEEP |
| Fin rot | 5,000 variants | `/diseases/fin-rot/` | KEEP |
| Tank mates / fish that live with bettas | 5,000 variants | `/compatibility/tank-mates/` | KEEP |
| Price / cost | 5,000 variants | `/economics/betta-fish-price/` | KEEP |
| Natural habitat | 5,000 variants | `/origins/wild-habitats/` | KEEP |
| Koi / blue / white / green | 5,000 color variants | `/biology-genetics/colors/` | MERGE |
| Breeding | 5,000 variants | `/breeding/pairing-fry-care/` | KEEP |
| Stressed betta | 5,000 | `/behavior/unhappy-betta/` | MERGE |

### Important conclusion

The site does **not** need dozens of new articles to chase the Keyword Planner list.

Most large keyword families are already owned. The next gains should come from:
- correcting ownership wording;
- strengthening missing intent coverage inside existing owners;
- adding only a few genuinely distinct pages.

---

## 3. Class A ownership correction: Heater query

### Current registry query

`betta fish heater calibration`

### File evidence

The strongest demand is for:
- betta fish heater — 50,000 bucket;
- aquarium heater for betta fish — 50,000 bucket;
- betta fish tank heater — 5,000 bucket and +900% three-month change;
- best heater for betta fish — 500 bucket and +900% three-month change.

### Current article scope

The existing Heater article already covers:
- whether a heater is needed;
- selection;
- sizing;
- placement;
- calibration/verification;
- 5-gallon setup;
- temperature monitoring.

### Decision

Change the **registered primary query only** to:

**`betta fish heater`**

Keep calibration as a supporting attribute.

This is a Class A registry/ownership correction because the existing page already fulfills the broader query and its visible title is already “Betta Fish Heater Guide: Sizing, Placement and Calibration.”

---

## 4. Strongest structural gap: “Types of Betta Fish”

### Keyword evidence

The Planner contains:
- betta fish types — 5,000;
- betta fish different types — 5,000;
- different betta fish — 5,000;
- betta fish kinds — 5,000;
- betta fish varieties — 5,000;
- plus several 500-volume “all types / kinds / rare types” variants.

Approximate cluster demand is meaningful even though the values are bucketed.

### Current ownership problem

No current page fully answers the dominant “types” task:

- `/biology-genetics/tail-types/` owns fin shapes only.
- `/biology-genetics/colors/` owns colors/patterns.
- `/biology-genetics/species/` owns domestic-vs-wild taxonomy.
- `/biology-genetics/plakat-betta/` and `/biology-genetics/giant-betta/` own individual forms.
- The Biology hub routes these pages but targets “betta fish biology,” not “betta fish types.”

### Decision

**NEW PAGE CANDIDATE — high priority**

Proposed primary query: **betta fish types**

Recommended page job:

> Explain that “type” can refer to separate classification axes—tail form, color/pattern, body/size form, sex and true species—then route readers to the existing specialist pages.

This should be an overview/bridge article, not a giant duplicate catalog.

Suggested URL:

`/biology-genetics/betta-fish-types/`

Suggested H1:

**Types of Betta Fish: Tail Shapes, Colors, Varieties & Species**

Cannibalization controls:
- summarize, then link;
- Tail Types remains fin-shape owner;
- Colors remains color/pattern owner;
- Species remains taxonomy owner;
- Plakat and Giant remain detailed form owners;
- do not reproduce full child-page tables.

Approval: Editorial.

Unique hero required.

---

## 5. Weak ownership: “Female Betta Fish”

### Keyword evidence

- female betta fish — 50,000 bucket;
- female betta fish care — 50 bucket, +900% YoY;
- female betta fish types — 500;
- female betta fish size — 50;
- PAA asks “Is a male or female betta better?”

### Current coverage

The site splits female-betta intent across:
- `/breeding/gender-identification/` — how to identify sex;
- `/compatibility/female-sorority/` — group/cohabitation risk;
- `/compatibility/tank-mates/` — general compatibility.

There is no clean owner for the broad query **female betta fish**.

### Decision

Do **not** create a new female-betta page immediately.

First test a controlled expansion/repositioning of:

`/breeding/gender-identification/`

Potential broader task:

**Female Betta Fish vs Male: Identification, Behavior & Care Differences**

Keep:
- sorority risk with the Sorority page;
- broad tank mates with Tank Mates;
- basic care with existing Care owners.

This likely requires Class B editorial reapproval because visible scope/H1 would change.

If SERP validation later shows that “female betta fish” requires a full standalone care profile, revisit a separate URL only after defining strict boundaries.

---

## 6. Rising symptom queries: merge, do not create thin pages yet

The strongest rising Betta-specific Trends queries include:

- why is my betta fish staying at the bottom of the tank — +350%;
- why is my betta fish staying at the top of the tank — +300%;
- why does my betta fish stay at the bottom — +180%;
- why is my betta fish not eating — +50%;
- why did my betta fish die — +40%.

The search-interest values for these queries are small, so the percentage increase should not be treated as proof of large absolute demand.

### Current coverage

`/behavior/unhappy-betta/` already covers:
- reduced appetite;
- reduced activity;
- hiding;
- bottom lying;
- glass surfing;
- normal-vs-abnormal behavior context.

`/diseases/diagnostic-matrix/` owns symptom-first triage.

### Decision

**MERGE INTO EXISTING OWNERS**

Recommended additions after review:
- FAQ/section: “Why is my betta staying at the top of the tank?”
- strengthen bottom-position wording around rest vs persistent abnormal behavior;
- explicit handoff for “not eating” to Diet + Diagnostic Matrix;
- do not create “why did my betta die” as a search-targeted post without a strong evidence and sensitivity framework.

Approval:
- editorial for pure behavior/husbandry wording;
- clinical if the change adds diagnostic, treatment or medical-escalation meaning.

---

## 7. PAA opportunity: Handling, touching and bites

Repeated PAA:
- Why can't you touch betta fish? — 4 occurrences;
- Can a betta fish bite hurt?
- Will a betta fish bite your finger?

No current page has a clean handling owner.

### Decision

**MERGE, not a new page**

Best destination:
- Tank Setup FAQ or a bounded Care FAQ explaining that routine handling is unnecessary and physical transfer should minimize direct contact.

Do not build a thin “betta bite” page from PAA repetition alone.

Approval: Editorial unless health/injury treatment is added.

---

## 8. PAA opportunity: happiness, enrichment and social perception

Relevant PAA:
- What do betta fish love the most?
- What things make betta fish happy?
- What can entertain my betta fish?
- How do you tell if a betta fish is happy?
- Do betta fish like their owners?
- Do betta fish like to be talked to?
- How long is a betta's memory?
- What do betta fish do all day?

### Current / planned owners

- happiness/welfare signs -> `/behavior/unhappy-betta/`
- sound/talking -> `/behavior/hearing-music/`
- enrichment -> new draft `/behavior/enrichment-safe-toys/`
- sleep/rest -> `/anatomy/betta-fish-sleep/`

### Decision

The Enrichment draft is validated by PAA as a genuine user task.

Do not create separate “does my betta love me / remember me” pages yet. Those queries need evidence review before expansion because anthropomorphic wording can easily outrun the evidence.

---

## 9. PAA opportunity: feeding questions

PAA strongly reinforces the Diet page:

- how often to feed;
- how long without food;
- hungry/starving;
- pellet-count questions;
- live foods;
- human foods;
- “toxic” foods.

### Current coverage

The Diet page already owns:
- feeding frequency;
- portion logic;
- staple foods;
- live/frozen/freeze-dried foods;
- absence feeding;
- sickness boundary.

### Decision

**KEEP ONE OWNER**

Potential future FAQ additions:
- how to tell if a betta is hungry;
- why fixed pellet counts are unreliable;
- human-food questions;
- toxic-food framing.

Do not create food subpages unless a distinct evidence-rich task emerges.

Editorial reapproval needed for source changes.

---

## 10. Trends: what is genuinely new vs already captured

### Already captured well

- betta fish price +130% -> Price page;
- best plants +80% -> Plants;
- tank size +50% -> Tank Setup;
- betta size +50% -> Growth;
- plants +40% -> Plants;
- tank setup +40% -> Tank Setup;
- pH +40% -> Water Parameters;
- food +40% -> Diet;
- lifespan +40% -> Lifespan;
- can bettas live together +40% -> Tank Mates/Sorority;
- Plakat +30% -> Plakat page;
- filter +30% -> Filtration.

This is strong confirmation that the current architecture is aligned with active search demand.

### Merge into Colors

- koi betta +40%;
- pink betta +70%;
- green betta +60%.

Do not make one page per color.

### Validate before creating anything

- alien betta fish +180%;
- full moon betta fish +80%.

Both have low Trends search-interest values, so the percentage increase is not sufficient evidence for immediate page creation.

Alien Betta may become a future evidence-led type/hybrid article if reliable parentage and care distinctions can be sourced.

“Full Moon” should first be treated as terminology to validate inside Tail Types, because trade usage is inconsistent.

---

## 11. Commercial and irrelevant clusters to exclude

Do not add topical-map URLs for:

- betta fish for sale;
- near me;
- buy/order/shop/online/shipping;
- Petsmart/Petco comparisons;
- retailer-specific age/product pages;
- India-price queries if the target market is not India;
- generic other-species queries such as goldfish, clownfish, axolotl and generic tank terms;
- PAA “junk fish / garbage fish / cleanest fish / friendliest fish” questions.

Compatibility can mention species such as corydoras, tetras, guppies and shrimp only in a Betta-specific decision context.

---

## 12. Updated opportunity ranking

### P0 — Safe ownership correction
1. Change Heater registered primary query to **betta fish heater**.

### P1 — Genuine new content
2. **Betta Fish Types** overview/bridge page.
3. **Bubble Nests** — research brief and draft already prepared.
4. **Enrichment and Safe Toys** — research brief and draft already prepared.

### P1 — Existing-page expansion
5. Rising symptom-state coverage: top/bottom/not eating, routed through Unhappy Betta + Diagnostic Matrix.

### P2 — Existing-page repositioning
6. Broaden Gender Identification to better own **female betta fish** without competing with Sorority.

### P2 — FAQ improvements
7. Handling/touch/bite -> Care/Tank Setup.
8. Diet PAA -> Diet & Feeding.

### P3 — Research/validate
9. Alien Betta.
10. Social cognition: owner recognition, talking, memory.
11. “Full Moon” terminology -> validate and likely merge into Tail Types.

---

## 13. Site-level conclusion

The new files strengthen the case for **precision expansion**, not mass publishing.

Current strongest areas:
- care/setup;
- food;
- heating/filtration;
- water;
- plants;
- health;
- compatibility;
- lifespan/growth;
- price.

Most important under-owned task:
- **betta fish types**.

Most important current-page query mismatch:
- **heater** — registry is too narrow.

Most important rising-intent improvement:
- **symptom position/appetite** queries, merged safely into existing behavior/health owners.

Most important PAA-supported new article:
- **enrichment**, already drafted.

The site should resist creating URLs for every color, tank size, retailer, species-pair or PAA variant. Canonical ownership and bounded supporting coverage remain the better semantic strategy.
