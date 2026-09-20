# BettaFish.website Cannibalization Register

Date: 2026-09-19
Branch: chatgpt-work

## Summary

The site does not show widespread cannibalization. Most overlap is normal hub-child semantic overlap. One registry-level query ownership conflict should be corrected before indexing.

| Pages | Classification | Evidence | Lowest-risk action |
|---|---|---|---|
| / and /care/ | Acceptable hub–child overlap | Homepage is whole-site gateway; Care is husbandry category owner. | Keep current copy and architecture. |
| /care/ and /care/tank-setup/ | Acceptable hub–child overlap | Care sequences care decisions; Tank Setup owns equipment, cycling, tank size and minimum-housing variants. | Keep Tank Setup as primary owner for setup/tank-size queries. |
| /care/water-parameters/ and /care/tank-setup/ | Partial duplication, low risk | Water Parameters includes cycling context; Tank Setup owns the setup process. | Add contextual handoff; do not create a second cycling page. |
| /care/water-parameters/ and /maintenance/water-change/ | Partial duplication, low risk | Water Parameters explains why changes matter; Water Change owns frequency/method. | Preserve short contextual coverage and hand off to Water Change. |
| /care/water-parameters/ and /care/heaters-calibration/ | Partial duplication, low risk | Water Parameters states target temperature; Heater page owns equipment/calibration. | Keep temperature target on Water Parameters; hand off equipment detail. |
| /diseases/ and /diseases/diagnostic-matrix/ | Acceptable hub–child overlap | Hub routes health topics; matrix owns symptom-first triage. | Keep roles. |
| /diseases/diagnostic-matrix/ and condition pages | Acceptable hub–child overlap | Matrix is non-diagnostic routing; condition pages own condition-specific recognition/planning. | Add explicit condition handoffs where absent. |
| /compatibility/ and /compatibility/tank-mates/ | **Intent differentiation / keyword ownership conflict** | Hub primary query is “betta fish tank mates”; child primary query is “best betta fish tank mates.” | Change hub registered primary query to “betta fish compatibility” or equivalent category-level query. Do not rewrite approved article. |
| /compatibility/tank-mates/ and /compatibility/female-sorority/ | Internal-link ambiguity, low risk | Tank Mates discusses female groups; Sorority is the dedicated high-risk owner. | Add direct contextual link from Tank Mates to Sorority and keep sorority setup details out of the broad page. |
| /biology-genetics/ and /biology-genetics/species/ | Acceptable hub–child overlap | Hub is category map; Species owns taxonomy/diversity. | Keep roles. |
| /biology-genetics/ and /biology-genetics/lifespan/ | Acceptable hub–child overlap | Hub introduces biology; Lifespan owns longevity/aging. | Keep roles. |
| /biology-genetics/colors/ and /biology-genetics/color-change/ | Acceptable sibling differentiation | Colors owns phenotype terminology; Color Change owns “why is my fish changing color?” diagnostic-style task. | Maintain reciprocal contextual links. |
| /biology-genetics/tail-types/ and /biology-genetics/plakat-betta/ | Acceptable sibling differentiation | Tail Types compares fin forms; Plakat owns short-fin form/history/care. | Add/retain contextual handoffs; no merge. |
| /breeding/pairing-fry-care/ and proposed bubble-nest page | Partial current overlap | Breeding necessarily mentions nests, but a bubble-nest query is behavior/reproduction interpretation rather than full breeding process. | New page can be justified if tightly scoped and linked back to breeding. |
| /compatibility/tank-mates/ and proposed guppy page | Potential genuine cannibalization if split now | Broad tank-mates page can answer species-pair suitability in a bounded matrix/FAQ. | Merge into existing owner first; only split if future SERP/evidence shows a materially distinct task. |
| /care/water-parameters/ and proposed water-conditioner page | Potential cannibalization if split now | Existing article already explains chlorine/chloramine and conditioner use. | Expand bounded section/FAQ first; do not create URL yet. |

## Primary correction

**Registry only:**
- Current /compatibility/ primary query: betta fish tank mates
- Proposed category-level query: betta fish compatibility

This is a Class A ownership-documentation correction and should not change the hash-locked child article.

## Merge rules

- Similar words alone are not cannibalization.
- Hub pages may summarize child topics, but should not own the same dominant task.
- A supporting page may mention another topic only to orient the reader and hand off to the canonical owner.
- New pages require a distinct user task, not merely a long-tail keyword.
