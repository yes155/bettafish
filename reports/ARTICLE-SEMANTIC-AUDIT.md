# BettaFish.website Article Semantic Audit

Date: 2026-09-19
Repository: yes155/bettafish
Branch audited: chatgpt-work
Candidate: d4d150d

## Executive summary

- Articles audited: **34**
- Homepage/category hubs additionally reviewed for role separation: **5**
- PASS: **24**
- MINOR IMPROVEMENT: **9**
- MATERIAL REVISION: **0**
- EDITORIAL REAPPROVAL REQUIRED: **1**
- CLINICAL REAPPROVAL REQUIRED: **0**
- BLOCKER: **0**
- Material keyword-ownership/cannibalization conflicts: **1**
- Genuine near-term topical gaps: **2**
- Proposed topics better merged into an existing owner: **2**
- Deferred low-priority new-page candidates: **1**
- Excluded/deferred keyword-noise families retained from reconciliation: **4**

No hash-locked article source was changed during this audit.

## Overall finding

The current 34-article set is already disciplined: openings are answer-first, page purposes are generally clear, claims are bounded, FAQ sections are connected to the page task, and health pages distinguish observation/triage from diagnosis. The audit does not support broad rewriting or word-count expansion.

The main semantic weaknesses are concentrated in older foundation articles that have no article-body contextual links, one visible H1 on the female-sorority page that promises a setup formula more strongly than the page itself does, and one hub/child primary-query conflict in Compatibility.

## Article results

| URL | Result | Main finding | Approval impact |
|---|---|---|---|
| /care/water-parameters/ | MINOR IMPROVEMENT | Strong answer, but sections on cycling, heaters and water changes need clearer handoffs to their dedicated owners. | Prefer non-substantive linking/role clarification; source edits would require editorial review. |
| /care/diet-feeding/ | MINOR IMPROVEMENT | Intent satisfied; add contextual handoffs to water-quality and buoyancy/health owners rather than expanding sickness advice. | Class A if implemented outside locked source; otherwise editorial reapproval. |
| /care/filtration/ | MINOR IMPROVEMENT | Strong low-flow/filter intent; lacks contextual links to tank setup and water parameters. | Class A if external link layer; otherwise editorial reapproval. |
| /diseases/diagnostic-matrix/ | MINOR IMPROVEMENT | Safe triage role is clear; body should hand off explicitly to condition-specific clinical guides. | Non-substantive link correction only; no clinical wording change proposed. |
| /diseases/fin-rot/ | MINOR IMPROVEMENT | Safe boundary is strong; needs explicit contextual link to diagnostic matrix and water parameters. | No clinical reapproval if wording is unchanged. |
| /diseases/ich-treatment/ | MINOR IMPROVEMENT | Strong clinical scope and lifecycle framing; needs related-guide handoffs. | No clinical reapproval if wording is unchanged. |
| /compatibility/tank-mates/ | MINOR IMPROVEMENT | Broad owner is correct, but female-group content overlaps the dedicated sorority owner without a direct contextual link. | Class A linking/role clarification. |
| /compatibility/female-sorority/ | EDITORIAL REAPPROVAL REQUIRED | Content is cautious, but H1 “How to Set Up… Tank Size & Hierarchy Rules” overpromises a reproducible setup formula. | Visible H1/source meaning change requires editorial reapproval. |
| /biology-genetics/lifespan/ | MINOR IMPROVEMENT | Intro answers the query well; visible H1 is more academic than the search task. Search-title override already mitigates SERP mismatch. | Keep source locked unless H1 is later changed. |
| /biology-genetics/tail-types/ | MINOR IMPROVEMENT | Strong comparison content; lacks contextual handoffs to Plakat, growth and care implications. | Class A linking if external layer. |
| /care/tank-setup/ | PASS | Clear setup owner; tank-size/bowl/setup variants belong here. | None. |
| /maintenance/water-change/ | PASS | Distinct maintenance task, bounded by test results rather than universal percentages. | None. |
| /care/indian-almond-leaves/ | PASS | Correctly separates husbandry use from cure/dose folklore. | None. |
| /care/heaters-calibration/ | PASS | Distinct equipment/verification task with appropriate manufacturer-label boundary. | None. |
| /aquascaping/fin-safe-plants/ | PASS | Clear plant-selection owner; does not drift into generic aquascaping. | None. |
| /sensory/light-requirements/ | PASS | Clear light-dark-cycle task and evidence limits. | None. |
| /diseases/dropsy-treatment/ | PASS | Urgency-first clinical framing; no unsafe universal treatment recipe. | None. |
| /diseases/velvet-treatment/ | PASS | Differentiates suspicion from diagnosis and avoids universal copper/heat recipes. | None. |
| /diseases/columnaris-treatment/ | PASS | Strong recognition/escalation boundary; avoids antibiotic prescription. | None. |
| /anatomy/swim-bladder-treatment/ | PASS | Symptom-first buoyancy triage; avoids universal fasting claims. | None. |
| /behavior/unhappy-betta/ | PASS | Converts vague “unhappy” query into observable welfare checks without diagnosing emotion. | None. |
| /anatomy/betta-fish-sleep/ | PASS | Answers normal rest vs warning signs with appropriate uncertainty. | None. |
| /behavior/hearing-music/ | PASS | Keeps evidence boundary between hearing/vibration and unsupported music-preference claims. | None. |
| /behavior/flaring-triggers/ | PASS | Clear trigger/stress distinction; avoids prescribing mirror exercise. | None. |
| /breeding/pairing-fry-care/ | PASS | Welfare-first sequence with separation planning; does not normalize permanent pairing. | None. |
| /breeding/gender-identification/ | PASS | Multi-trait identification with juvenile/Plakat uncertainty. | None. |
| /origins/wild-habitats/ | PASS | Strong ecology-to-care bridge without “puddle” myth simplification. | None. |
| /morphology/growth-rate-size/ | PASS | Distinguishes measurement, growth and adult-size uncertainty. | None. |
| /biology-genetics/species/ | PASS | Distinct taxonomy/diversity task; not a purchase catalogue. | None. |
| /biology-genetics/colors/ | PASS | Correctly separates phenotype terminology from genetic certainty. | None. |
| /biology-genetics/color-change/ | PASS | Separates expected variation from husbandry/health escalation. | None. |
| /biology-genetics/plakat-betta/ | PASS | Clear form/history/care scope; no fighting promotion. | None. |
| /biology-genetics/giant-betta/ | PASS | Distinct size/genetics planning task with uncertainty preserved. | None. |
| /economics/betta-fish-price/ | PASS | Search intent satisfied with setup/ongoing-cost framing and dated price limits. | None. |

## Homepage and hub role separation

- **Homepage vs Care hub:** acceptable gateway–category overlap. Homepage routes the whole site; Care sequences husbandry decisions.
- **Care hub vs Tank Setup:** acceptable hub–child overlap. Tank Setup owns setup/tank-size/bowl/minimum-housing variants.
- **Diseases hub vs Diagnostic Matrix:** acceptable hub–child overlap. Hub routes health topics; matrix owns symptom-first triage.
- **Biology hub vs species/lifespan/colors/tail types:** acceptable hub–child overlap.
- **Compatibility hub vs Tank Mates:** **ownership conflict at registry-query level.** The hub currently targets “betta fish tank mates,” while the article targets “best betta fish tank mates.” Their copy is differentiated, but the query assignment is too close.

## Highest-priority findings

1. Reassign the Compatibility hub primary query from “betta fish tank mates” to a category-level concept such as “betta fish compatibility”; keep /compatibility/tank-mates/ as the broad tank-mates owner.
2. Do not create a separate tank-size page; /care/tank-setup/ already owns that task.
3. Do not create a separate absence-feeding page; /care/diet-feeding/ already owns it as a bounded FAQ/task.
4. Add contextual semantic handoffs to older foundation articles that currently have no body-level links.
5. Change the female-sorority H1 only through editorial reapproval; the body is already appropriately cautious.
6. Keep the Lifespan source locked; the metadata override already aligns search intent, so an H1 rewrite is not urgent.
7. Keep health-page wording unchanged; the audit found no reason to reopen medication, dose, temperature, diagnosis or urgency language.
8. Treat “betta water conditioner” as a bounded expansion of the water-parameters/tank-setup owner before creating a new URL.
9. Treat “guppies with bettas” as a section/FAQ expansion of the tank-mates owner unless later SERP evidence proves a distinct task requiring full-page depth.
10. Prioritize Bubble Nests and Enrichment/Safe Toys as the clearest net-new topical opportunities.

## Proposed source-changing correction

### Female sorority H1

**Before**
How to Set Up a Female Betta Sorority: Tank Size & Hierarchy Rules

**After (proposed)**
Can Female Bettas Live Together? Sorority Risks, Warning Signs & Separation Planning

**Why:** the current body explicitly says there is no tank-size/group-number formula that makes a sorority safe. The proposed H1 better matches the registered query and the article's actual conclusion.

**Approval:** Editorial reapproval required because this changes the hash-locked visible source.

## Evidence and safety

No article was flagged for unsupported universal treatment rules, invented certainty, medication/dose shortcuts, or unsafe diagnosis. The seven clinical guides remain best treated as exact-version reviewed educational pages. This audit proposes **no clinical-content wording changes**.

## Internal linking

The newer September 2026 editorial set already uses strong “Related…” sections. The older foundation group is noticeably weaker because several pages contain no structured body links. Do not rewrite them just to add words. Add only links that clarify ownership/handoffs.

## Scope conclusion

The site does not need a broad semantic rewrite. It needs a small ownership cleanup, selective contextual linking, one editorial H1 correction, and disciplined expansion into genuinely distinct tasks.
