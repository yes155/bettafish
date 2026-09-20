# Keyword reconciliation

Date: 2026-09-19  
Source workbooks: `download-export-v2.xlsx`, `Master_Keyword_Data.xlsx`, `clusterd topics.xlsx`

## Decision rule

A separate page is justified only when the query has a distinct user task, enough supporting evidence for a useful answer, and a clean internal-link role. Variants already answered by an approved guide stay with that guide. Broad aquarium queries, unrelated species, shopping-only noise and low-value novelty terms are excluded from the editorial roadmap.

The volume figures below are directional sums from the supplied keyword export. They are prioritization inputs, not traffic forecasts.

## Existing-page ownership

| Query family | Assigned owner | Decision |
|---|---|---|
| Betta care | `/care/` | Keep the care hub as the category owner; the homepage remains the site-wide gateway. |
| Tank setup and tank size | `/care/tank-setup/` | Merge tank-size variants here. Do not create a second tank-size guide. |
| Water parameters | `/care/water-parameters/` | Own temperature, pH, ammonia, nitrite, nitrate and stability queries. |
| Food, pellets and feeding | `/care/diet-feeding/` | Own “best food,” pellet and feeding-frequency variants. |
| How long a betta can go without food | `/care/diet-feeding/` | Keep as an absence-planning FAQ. The approved guide already answers it without unsafe survival promises. |
| Filters and flow | `/care/filtration/` | Own sponge, HOB and low-flow filter queries. |
| Bowls and minimum housing | `/care/tank-setup/` | Address as a setup/welfare subtopic; avoid a competing bowl article. |
| Water changes | `/maintenance/water-change/` | Own frequency, amount, replacement-water and biofilter-safe maintenance. |
| Heaters | `/care/heaters-calibration/` | Own “does a betta need a heater,” sizing, placement and calibration variants. |
| Compatibility category | `/compatibility/` | Own the category-level “betta fish compatibility” task; do not compete with the tank-mates article. |\n| Tank mates | `/compatibility/tank-mates/` | Own broad tank-mate comparisons and species-pair questions unless a later task proves materially distinct. |
| Female cohabitation | `/compatibility/female-sorority/` | Keep separate because the risk model and stop conditions are distinct. |
| Fin damage and regrowth | `/diseases/fin-rot/` | Keep regrowth questions with the clinically reviewed fin-damage guide. |
| Plants | `/aquascaping/fin-safe-plants/` | Own live/artificial plant and fin-safety queries. |
| Lifespan | `/biology-genetics/lifespan/` | Keep lifespan and aging variants together. |

## New-page queue

These are roadmap candidates, not approved pages. Each must receive structured sources, a unique hero image, editorial review and—when health advice is involved—clinical review before registry promotion.

| Priority | Proposed page | Directional volume | Why it is separate |
|---|---|---:|---|
| P1 | Betta bubble nests: meaning, eggs and warning signs | 8,310 | A distinct behavior/reproduction task only partially covered by the breeding guide. It must explicitly avoid using a nest as proof of happiness. |
| P1 | Betta water conditioner: chlorine, chloramine and safe use | 1,690 | A distinct source-water safety task. It should support, not duplicate, tank setup and water parameters. |
| P2 | Betta enrichment and safe toys | 2,540 | A distinct welfare task with no current owner. Evidence quality and fin/entrapment safety need careful review. |
| P2 | Can guppies live with bettas? | 1,940 | A species-pairing decision that can use a tighter compatibility matrix and separation plan than the broad tank-mates guide. |
| P3 | Do betta fish have teeth? | 1,600 | A distinct but lower-priority anatomy explainer; defer until higher-value welfare/behavior gaps are covered. |

## Merge-into-existing decisions\n\n| Cluster | Owner | Decision |\n|---|---|---|\n| Betta water conditioner | `/care/water-parameters/` | Merge into the existing owner first. The current guide already covers chlorine/chloramine and label-based conditioner use; strengthen mapping or a bounded section/FAQ before considering a new URL. |\n| Guppies with bettas | `/compatibility/tank-mates/` | Merge into the broad tank-mates owner first. Add a bounded species-pair row/FAQ only if supported by evidence; split later only if a materially distinct search task is demonstrated. |\n\n## Excluded or deferred clusters

| Cluster | Decision | Reason |
|---|---|---|
| Betta fish names | Exclude from the authority roadmap | Search demand exists, but the task does not strengthen evidence-led care, health or welfare expertise. |
| Generic aquarium conditioner, tanks, gravel and testing services | Exclude | Much of the export is broad aquarium or commercial noise rather than betta-specific intent. |
| “Best” product roundups | Defer | No product-testing program or affiliate methodology is approved. Informational selection criteria belong in existing guides. |
| Additional disease-treatment pages | Defer | Any new treatment page requires the same exact-version aquatic-veterinary review used for the current clinical set. |

## Cannibalization controls

- A new page must receive one unique primary query in `data/page-registry.csv`.
- The parent hub must link to it, and it must link back to its broader owner page.
- Existing owner pages should receive supporting internal links only after the new page is approved.
- No roadmap item becomes indexable from a spreadsheet row alone.
- The build audit continues to reject duplicate primary queries, orphan pages, missing review evidence and unapproved media.
