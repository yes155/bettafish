# V2 Update Intake Audit

**Assessment date:** 2026-09-02

**Files reviewed:**

- `master-betta-site-package v2.md`
- `sitemap v2.xml`

**Decision:** **PARTIAL ACCEPTANCE — 24 TOPICS ONLY**

Neither file may replace the current repository source or generated sitemap. On 2026-09-02, the owner selected only the 24 new article topics. They are now recorded as non-generated `planned-research` entries; all v2 code, legacy identity, design, contact and sitemap data remain rejected.

## Critical findings

1. The supplied v2 master file is a Python builder script, not an updated article package. It contains no replacement `FILE START` article blocks.
2. The builder maps 34 article filenames, but only 10 of those filenames exist in the current master package. Twenty-four mapped article sources are absent.
3. The builder reintroduces the retired `MyBettaCare` identity, Burlington office, legacy phone number, legacy email and placeholder social destinations.
4. The builder loads Tailwind CSS and Google Fonts from third-party CDNs, conflicting with the current static, script-free privacy and security contract.
5. The Markdown renderer does not HTML-escape source content before insertion, creating an avoidable injection risk.
6. The v2 sitemap contains 37 unique URLs, all on `mybettacare.com` instead of `bettafish.website`.
7. The v2 sitemap proposes 24 URLs that are not in the approved registry but supplies no corresponding article content.
8. The v2 sitemap omits 13 current hub, trust, utility and profile URLs, including the four principal hubs, policies and named people profiles.

## Proposed URLs without source content

- `/anatomy/betta-fish-sleep/`
- `/anatomy/swim-bladder-treatment/`
- `/aquascaping/fin-safe-plants/`
- `/behavior/flaring-triggers/`
- `/behavior/hearing-music/`
- `/behavior/unhappy-betta/`
- `/biology-genetics/color-change/`
- `/biology-genetics/colors/`
- `/biology-genetics/giant-betta/`
- `/biology-genetics/plakat-betta/`
- `/biology-genetics/species/`
- `/breeding/gender-identification/`
- `/breeding/pairing-fry-care/`
- `/care/heaters-calibration/`
- `/care/indian-almond-leaves/`
- `/care/tank-setup/`
- `/diseases/columnaris-treatment/`
- `/diseases/dropsy-treatment/`
- `/diseases/velvet-treatment/`
- `/economics/betta-fish-price/`
- `/maintenance/water-change/`
- `/morphology/growth-rate-size/`
- `/origins/wild-habitats/`
- `/sensory/light-requirements/`

## Current URLs omitted by the v2 sitemap

- `/404.html`
- `/authors/farrukh-abdullah/`
- `/biology-genetics/`
- `/care/`
- `/compatibility/`
- `/corrections-policy/`
- `/disclosure/`
- `/diseases/`
- `/editorial-policy/`
- `/editors/kate-barrington/`
- `/health-disclaimer/`
- `/privacy-policy/`
- `/reviewers/robert-martinez/`
- `/terms/`

The list contains 14 entries because `/404.html` is a utility output rather than a normal XML-sitemap URL. Thirteen indexable architecture URLs are missing from the proposed sitemap.

## Safe disposition

- Preserve the current Python generator, approved domain, registry and source-to-output model.
- Do not copy legacy contact, office, organization or third-party-script code.
- Treat the 24 proposed paths as owner-selected planning URLs, not publishable pages.
- Require a complete source article, page-role decision, evidence record, reviewer assignment and media mapping before adding any proposed URL.
- Generate the real sitemap from approved repository sources; never install the supplied static sitemap directly.

## Required replacement input

Supply the actual updated master content package containing the new or revised article text. Each article must include a stable proposed URL and enough content to audit claims, overlap, internal links, review needs and media requirements.
