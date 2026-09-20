# Three New Articles — Exact Promotion Plan

Date: 2026-09-19  
Branch: `chatgpt-work`  
Status: **Prepared; promotion blocked pending exact editorial approval and final hero assets**

## Candidate set

| Article | Draft | SHA-256 |
|---|---|---|
| Bubble Nests | `drafts/pages/bubble-nests.json` | `e6752af242d900d4aa16a1274680db7b55c312730489dfedbfff13c980f40379` |
| Enrichment & Safe Toys | `drafts/pages/enrichment-safe-toys.json` | `b29f511ee2e3470f87f28076c631938d2d9392c6a56ef5d69a86a6ed0f321952` |
| Betta Fish Types | `drafts/pages/betta-fish-types.json` | `a54643cc577228664c0dda07da20deabfe4c393a1d5ee9f7668ae7481fc739e3` |

No draft file should be edited after approval without generating a new SHA-256 and obtaining reapproval.

---

## Proposed registry ownership

### Bubble Nests

```csv
/behavior/bubble-nests/,article,approved,/biology-genetics/,learn,betta bubble nest,Betta bubble nesting,"Explain bubble-nest biology and paternal function while showing why a nest is not a standalone welfare score","Breeding protocol disease diagnosis and happiness scoring",yes,Farrukh Abdullah,Kate Barrington,ordinary,yearly,bubble-nests-hero,"Article|FAQPage|BreadcrumbList",content/pages/bubble-nests.json,public/behavior/bubble-nests/index.html
```

### Enrichment & Safe Toys

```csv
/behavior/enrichment-safe-toys/,article,approved,/biology-genetics/,decide,betta enrichment,Betta environmental enrichment,"Use Betta-specific welfare evidence to distinguish useful environmental complexity from forced or risky stimulation","Product rankings mirror workouts and medical behavior diagnosis",yes,Farrukh Abdullah,Kate Barrington,animal-welfare,yearly,enrichment-safe-toys-hero,"Article|FAQPage|BreadcrumbList",content/pages/enrichment-safe-toys.json,public/behavior/enrichment-safe-toys/index.html
```

### Betta Fish Types

```csv
/biology-genetics/betta-fish-types/,article,approved,/biology-genetics/,learn,betta fish types,Domestic Betta varieties,"Explain the separate classification axes behind tail forms colors body forms sex and true species then route readers to canonical child guides","Full tail catalogue full color taxonomy species catalogue rarity rankings and sales listings",yes,Farrukh Abdullah,Kate Barrington,ordinary,yearly,betta-fish-types-hero,"Article|FAQPage|BreadcrumbList",content/pages/betta-fish-types.json,public/biology-genetics/betta-fish-types/index.html
```

These rows are proposals only and must not be inserted before approval.

---

## Canonical ownership boundaries

### Bubble Nests
Owns:
- betta bubble nest
- why bettas make bubble nests
- whether a nest proves happiness/health
- why nest building changes

Does not own:
- full breeding protocol -> `/breeding/pairing-fry-care/`
- water quality -> `/care/water-parameters/`
- symptom diagnosis -> Diseases / Unhappy Betta

### Enrichment
Owns:
- betta enrichment
- safe enrichment ideas
- toy screening
- mirrors as enrichment question
- how to judge response

Does not own:
- general tank setup -> `/care/tank-setup/`
- plant selection -> `/aquascaping/fin-safe-plants/`
- flaring diagnosis -> `/behavior/flaring-triggers/`
- feeding quantity -> `/care/diet-feeding/`

### Betta Fish Types
Owns:
- broad “betta fish types / kinds / varieties” orientation task

Does not own:
- fin-form detail -> Tail Types
- color/pattern detail -> Colors
- true species taxonomy -> Species
- Plakat detail -> Plakat
- Giant detail -> Giant
- sex identification -> Gender Identification

---

## Proposed inbound link plan

Use the derived link layer where possible so approved source hashes are not changed unnecessarily.

### Bubble Nests inbound
Preferred:
- `/breeding/pairing-fry-care/` -> Bubble Nests
- `/behavior/unhappy-betta/` -> Bubble Nests
- Biology hub card -> Bubble Nests only if the hub receives separate editorial approval for a visible source edit

### Enrichment inbound
Preferred:
- `/care/tank-setup/` -> Enrichment
- `/aquascaping/fin-safe-plants/` -> Enrichment
- `/behavior/flaring-triggers/` -> Enrichment
- `/behavior/unhappy-betta/` -> Enrichment
- Biology hub card -> Enrichment only with separate hub approval if required

### Betta Fish Types inbound
Preferred:
- `/biology-genetics/tail-types/` -> Betta Fish Types
- `/biology-genetics/colors/` -> Betta Fish Types
- `/biology-genetics/species/` -> Betta Fish Types
- `/biology-genetics/plakat-betta/` -> Betta Fish Types
- `/biology-genetics/giant-betta/` -> Betta Fish Types
- `/breeding/gender-identification/` -> Betta Fish Types
- Biology hub card -> Betta Fish Types only with separate hub approval if required

The new articles already contain contextual outbound links to their established owners.

---

## Exact promotion sequence

1. Record editorial approval against the three draft SHA-256 hashes.
2. Freeze each approved draft.
3. Copy the approved bytes into:
   - `content/pages/bubble-nests.json`
   - `content/pages/enrichment-safe-toys.json`
   - `content/pages/betta-fish-types.json`
4. Preserve source wording exactly; only workflow/status fields may be changed if the project's source contract requires it. Any content change invalidates the approved hash.
5. Add the three approved rows to `data/editorial-review-candidates.csv`.
6. Add the three registry rows to `data/page-registry.csv`.
7. Generate/attach one unique 1600×900 WEBP hero per page.
8. Compute hero checksum, dimensions and byte size.
9. Add three approved rows to `data/media-manifest.csv`.
10. Add derived related-guide mappings for inbound links that do not require source edits.
11. Add search metadata overrides only if the source title would otherwise be masked or truncated.
12. Build.
13. Audit.
14. Verify:
    - no duplicate primary query;
    - no unknown related-guide target;
    - all three hero IDs resolve;
    - all three exact source hashes match the approval register;
    - FAQ schema renders;
    - no clinical-review boundary was crossed;
    - sitewide prepublication/noindex controls remain unchanged.
15. Keep production launch blocked until the separate launch gates pass.

---

## Behavior hub decision

Do **not** create a Behavior hub during this promotion.

After Bubble Nests and Enrichment are promoted, reassess the behavioral cluster containing:
- Unhappy Betta
- Sleep
- Hearing/Music
- Flaring
- Bubble Nests
- Enrichment

A new hub is justified only if it improves navigation and establishes a distinct category task without competing with the existing Biology hub. Do not create it merely because six behavior-related URLs exist.
