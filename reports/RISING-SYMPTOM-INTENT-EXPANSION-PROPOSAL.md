# Rising Symptom-Intent Expansion Proposal

Date: 2026-09-19  
Branch: `chatgpt-work`  
Status: **Proposal only — no approved source changes**

## Trigger from the new keyword files

The Trends export surfaced several rising Betta-specific symptom/state queries:

- why is my betta fish staying at the bottom of the tank;
- why is my betta fish staying at the top of the tank;
- why does my betta fish stay at the bottom;
- why is my betta fish not eating;
- why did my betta fish die.

The percentage changes are directional signals only. Several have low absolute Trends interest, so they do not justify one URL per query.

## Canonical ownership decision

| Query/task | Canonical owner | Supporting owner | Decision |
|---|---|---|---|
| betta staying at bottom | `/behavior/unhappy-betta/` | `/diseases/diagnostic-matrix/` | KEEP / strengthen mapping |
| betta staying at top | `/behavior/unhappy-betta/` | `/diseases/diagnostic-matrix/` | MERGE INTO EXISTING OWNER |
| betta not eating | `/behavior/unhappy-betta/` | `/care/diet-feeding/`, Diagnostic Matrix | MERGE INTO EXISTING OWNER |
| why did my betta die | DEFER | Diseases hub / future mortality guidance if justified | Do not target yet |

## Existing coverage

### Bottom of tank

`/behavior/unhappy-betta/` already has the FAQ:

**Why is my betta lying on the bottom?**

The current answer correctly distinguishes normal resting from persistent abnormal behavior and routes the reader to temperature, water chemistry, responsiveness, breathing, appetite and balance checks.

**Action:** no new page and no urgent rewrite. Record keyword ownership and retain the existing FAQ.

### Not eating

Current coverage already exists in two places:

- `/behavior/unhappy-betta/` lists reduced appetite as a general warning sign and recommends water/environment checks.
- `/care/diet-feeding/` has a bounded sickness section that rejects improvised cure foods and routes persistent appetite loss to broader assessment.

**Action:** keep Unhappy Betta as the symptom-intent owner and Diet as the feeding-context owner.

### Top of tank

There is no equally explicit FAQ for a Betta persistently staying near the surface.

**Action:** propose one bounded FAQ addition to `/behavior/unhappy-betta/`.

## Proposed Class B editorial addition

### Proposed FAQ

**Question:** Why is my betta staying at the top of the tank?

**Proposed answer:**

> Bettas normally visit the surface to breathe and may rest near the top, so surface position alone is not a diagnosis. A persistent change from the fish's usual pattern deserves a husbandry check: confirm temperature, ammonia, nitrite, nitrate, pH, filter operation and whether the fish is eating and swimming normally. Use the symptom-triage guide or seek qualified fish-health help when the change is accompanied by abnormal breathing, loss of balance, injury, appetite loss or other persistent signs.

### Review classification

**Editorial reapproval required** because the visible source changes.

Clinical reapproval is **not automatically required** if the final wording stays observational, does not name a diagnosis and does not change treatment/urgency guidance. If the edit adds causes such as hypoxia, gill disease, infection, medication or treatment advice, move the change to clinical review.

## Optional “not eating” FAQ

A new FAQ is not strictly necessary because the intent is already covered in the behavior table and Diet sickness section.

If stronger exact-query matching is desired, proposed bounded FAQ:

**Question:** Why is my betta not eating?

**Answer direction:**
- one missed meal is not enough to diagnose a problem;
- check food freshness/routine and recent changes;
- test temperature and water parameters;
- look for breathing, swimming, swelling or injury changes;
- route persistent appetite loss to the Diagnostic Matrix / qualified help;
- do not prescribe peas, fasting, medicated food or a cure food from appetite loss alone.

This would also require editorial reapproval and must not add diagnostic or treatment meaning without clinical review.

## “Why did my betta die?” decision

Do not create a search-targeted article now.

Reasons:
- the query can imply many causes that cannot be reconstructed reliably after death;
- a useful page would need careful evidence about water testing, timeline, other fish, recent changes and when veterinary/postmortem assessment can help;
- a simplistic list of causes would conflict with the site's diagnostic-boundary rules.

Classification: **DEFER pending a dedicated evidence and sensitivity brief.**

## Cannibalization rule

Do not create:
- `/behavior/betta-at-bottom/`
- `/behavior/betta-at-top/`
- `/health/betta-not-eating/`

These are symptom variants, not independent topic entities. Keep the behavior/welfare page as the canonical observational owner and hand off to the clinical matrix when red flags appear.

## Recommended next implementation

1. Add keyword-ownership rows for bottom/top/not-eating.
2. Keep bottom coverage unchanged.
3. Prepare the single “staying at top” FAQ for Kate editorial review.
4. Add “not eating” FAQ only if exact-query coverage is still weak after indexing/measurement.
5. Do not modify the Diagnostic Matrix or any clinically reviewed source in this round.
