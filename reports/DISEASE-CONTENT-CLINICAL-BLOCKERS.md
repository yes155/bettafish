# Disease Content Clinical Review Blockers

**Assessment date:** 2026-09-01

**Editorial review:** Approved by Kate Barrington

**Assigned clinical reviewer:** Robert Martinez, DVM

**Clinical approval of corrected pages:** Not yet recorded

**Publishing decision:** Keep all three corrected sources ungenerated and non-indexable until version-specific clinical approval

Kate Barrington's approval satisfies the site's writing and aquarium-editorial review record. Robert Martinez, DVM, is now the assigned clinical reviewer; his aquatic-veterinary background is supported by his [official professional biography](https://www.aquaticvetconsulting.com/about) and a [WAVMA presenter biography](https://www.wavma.org/Webinars/b1089-fish-er-medicine-97942). Assignment does not equal approval: the corrected versions must still receive a documented clinical review before they can be generated or credited to him.

## Blocked URLs

| URL | Main blocker | Severity |
|---|---|---|
| `/diseases/diagnostic-matrix/` | Prescribes erythromycin, copper, malachite green, kanamycin, Epsom salt and fasting from symptom descriptions without a confirmed diagnosis. | Critical |
| `/diseases/fin-rot/` | Presents salt baths and broad-spectrum antibiotics as stage-based treatment protocols with fixed doses and duration. | Critical |
| `/diseases/ich-treatment/` | Prescribes 30°C heat, salt, malachite green, formalin and copper protocols with fixed concentrations and cure language. | Critical |

## Claims that must not reach generated output

- Erythromycin at 250 mg per 10 gallons every 24 hours for four days.
- Kanamycin and Epsom-salt instructions for “curing” dropsy.
- One tablespoon of salt per three gallons and seven- or fourteen-day bath protocols.
- Raising every suspected ich case to 30°C/86°F.
- Copper sulfate targets of 0.15–0.20 ppm or one-drop-per-gallon malachite-green/formalin instructions.
- Statements that a symptom proves a named disease or that a treatment guarantees eradication, recovery or survival.

## Corrections completed for clinical review

1. The diagnostic matrix is now symptom-first triage built around water testing, observation and veterinary escalation.
2. The fin-damage draft separates physical and environmental possibilities from suspected infectious disease and contains no drug or salt dose.
3. The ich draft explains signs, confirmation, transmission and lifecycle without a universal heat, salt, copper, formalin or malachite-green protocol.
4. All three sources state that diagnosis and treatment planning depend on the fish, aquarium system and professional direction.
5. All three are permanent JSON sources with visible citations, assigned reviewer metadata, `planned-clinical-review` status and `indexable: false`.

The remaining G05 action is version-specific clinical review and approval. `data/clinical-review-candidates.csv` records the three candidate source hashes. Record the approved hash and date before changing status, generating output or displaying the clinical-review credit.

## Evidence boundary

The [Merck Veterinary Manual's aquarium-fish guidance](https://www.merckvetmanual.com/exotic-and-laboratory-animals/aquarium-fish/management-of-aquarium-fish) emphasizes diagnostic work, environmental management and targeted therapy, and discourages prophylactic medication without diagnostic testing. Dr. Martinez must approve the corrected pages before their registry status changes from `planned-clinical-review`, before output is generated, and before a “Clinically reviewed by” credit is displayed.
