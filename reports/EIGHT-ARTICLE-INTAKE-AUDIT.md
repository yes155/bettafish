# Eight-Article Intake Audit

**Assessment date:** 2026-09-02

**Input:** `compiled-eight-articles.md`

**Decision:** **ACCEPT AS SOURCE MATERIAL / DO NOT GENERATE**

The attachment contains full copy for exactly the eight authority-expansion URLs that were absent from `master-betta-site-package v3.md`. Together, the v3 package and this attachment account for all 24 owner-selected expansion article bodies. None is yet approved for generated output.

## Inventory result

| URL | Body present | Initial risk | Intake decision |
|---|---:|---|---|
| `/diseases/velvet-treatment/` | Yes | High-risk pet health | Clinical rewrite and evidence review required |
| `/diseases/columnaris-treatment/` | Yes | High-risk pet health | Clinical rewrite and evidence review required |
| `/care/indian-almond-leaves/` | Yes | Animal welfare | Evidence and claim-limit review required |
| `/care/heaters-calibration/` | Yes | Animal welfare | Evidence and product-intent review required |
| `/behavior/hearing-music/` | Yes | Ordinary | Evidence and terminology review required |
| `/behavior/flaring-triggers/` | Yes | Animal welfare | Evidence and welfare review required |
| `/biology-genetics/plakat-betta/` | Yes | Ordinary | Evidence and terminology review required |
| `/biology-genetics/giant-betta/` | Yes | Animal welfare | Evidence and growth-claim review required |

## Hard blockers found

1. **No citations or source list:** the package contains no external URLs, numbered citations or reference section. Search-volume and difficulty figures are also unsourced.
2. **Unsafe clinical instructions:** the Velvet and Columnaris drafts prescribe named medications, exact concentrations, fixed treatment durations and temperature changes. They also use cure language and definitive diagnostic framing. These pages cannot be generated until claims are corrected, evidence is attached and Robert Martinez, DVM, approves the exact final versions.
3. **Absolute or weakly supported statements:** several care, behavior and genetics passages present uncertain outcomes as universal facts. These require qualification and evidence mapping.
4. **Internal links are not implemented:** the drafts name related pages but do not provide approved URL destinations or complete anchor-to-target records.
5. **Media is not supplied:** the package defines 24 image briefs and placeholder markers, three per article, but includes no image files, provenance, approval state, dimensions, crops, captions or ImageObject records.
6. **Legacy packaging language:** the document introduction calls the site MyBettaCare.com and describes the articles as already published. Neither statement may enter BettaFish.website source or output.

## Controlled correction path

1. Convert each article into the permanent structured JSON content contract using its mapped `content/pages/*.json` path.
2. Replace the legacy identity with BettaFish.website and remove publishing claims.
3. Perform claim-by-claim evidence research and add visible sources.
4. Correct absolute, diagnostic, dosing and cure claims before editorial review.
5. Record complete internal-link targets and test them against the registry.
6. Create a controlled media manifest before producing or integrating images.
7. Obtain Kate Barrington's approval for the six non-clinical articles and Robert Martinez, DVM's approval for the exact two corrected clinical versions.
8. Promote and generate one reviewed batch at a time; keep the public sitemap empty while sitewide noindex is active.

The current build must continue to emit zero pages for these eight URLs until the applicable promotion gates pass.
