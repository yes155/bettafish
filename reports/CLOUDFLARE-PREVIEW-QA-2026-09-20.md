# Cloudflare Preview QA Checklist — Candidate 90a45a1

**Candidate SHA:** `90a45a1237192fc10221231c1f6bfc3d8a8b236d`  
**Cloudflare deployment:** `1b60c46c-1c18-4696-83c7-46b8bdab147f`  
**Branch preview:** `https://chatgpt-work.bettafish-4kt.pages.dev`  
**Status:** Awaiting visual/browser verification

## Representative routes

Check all four viewports on at least these routes:

1. `/` — homepage
2. `/care/` — category hub
3. `/care/tank-setup/` — long-form care article
4. `/diseases/diagnostic-matrix/` — high-risk health decision page
5. `/biology-genetics/betta-fish-types/` — new comparison article
6. `/behavior/bubble-nests/` — new behavior article
7. `/behavior/enrichment-safe-toys/` — new welfare article
8. `/about/` — trust/profile layout

## Required viewports

| Viewport | Target |
|---|---|
| Mobile | 360 × 800 |
| Tablet | 768 × 1024 |
| Laptop | 1366 × 768 |
| Wide desktop | 1920 × 1080 |

## Visual checks

For every representative route confirm:

- no horizontal overflow;
- no clipped/truncated H1 or card title;
- content column uses the available width without a large empty right rail;
- hero image is not unintentionally cropped;
- fish/fins remain visible where required;
- hero overlay text remains readable;
- article thumbnails keep their intended aspect ratio;
- light-mode body text has sufficient contrast;
- dark-mode body text, links, callouts and tool/article components remain readable;
- section spacing is consistent and no oversized blank gaps appear;
- breadcrumbs wrap cleanly;
- tables are usable on mobile;
- source/review lines align correctly;
- footer does not overflow or collapse;
- new Bubble Nests, Enrichment and Betta Fish Types heroes display correctly.

## Interaction checks

- desktop navigation works;
- mobile menu opens/closes;
- keyboard Tab reaches nav and actionable elements in sensible order;
- visible keyboard focus exists;
- dropdowns are keyboard accessible;
- internal links from the Biology hub / related guides reach the three new pages;
- no dead buttons or placeholder controls;
- back/forward navigation does not break menu state.

## Prepublication SEO/security checks

Using browser DevTools or a header checker, verify:

### HTTPS
- preview loads over HTTPS;
- no mixed-content warnings;
- assets also load over HTTPS.

### Headers
Expected from the repository Cloudflare header configuration:
- `Strict-Transport-Security`
- `X-Content-Type-Options`
- `Referrer-Policy`
- `Permissions-Policy`
- frame protection via CSP `frame-ancestors` and/or `X-Frame-Options`

Record actual values here:

| Header | Observed value | Pass |
|---|---|---|
| Strict-Transport-Security |  | ☐ |
| X-Content-Type-Options |  | ☐ |
| Referrer-Policy |  | ☐ |
| Permissions-Policy |  | ☐ |
| CSP / frame protection |  | ☐ |

### Indexing
- `/robots.txt` blocks crawling in preview/prepublication mode;
- generated pages carry noindex while `sitewide_noindex=true`;
- no preview URL is included in a production sitemap;
- canonical URLs point to `https://bettafish.website/.../`, not the pages.dev hostname.

### Structured/social metadata
On homepage + one article + one health page verify:
- canonical;
- title;
- meta description;
- Open Graph title/description/image;
- JSON-LD parses and matches the page;
- author/reviewer links resolve.

## Sign-off table

| Area | Result | Notes |
|---|---|---|
| 360×800 | ☐ PASS ☐ FAIL | |
| 768×1024 | ☐ PASS ☐ FAIL | |
| 1366×768 | ☐ PASS ☐ FAIL | |
| 1920×1080 | ☐ PASS ☐ FAIL | |
| Keyboard/navigation | ☐ PASS ☐ FAIL | |
| Dark mode | ☐ PASS ☐ FAIL | |
| HTTPS/headers | ☐ PASS ☐ FAIL | |
| Noindex/robots | ☐ PASS ☐ FAIL | |
| Canonical/schema/OG | ☐ PASS ☐ FAIL | |
| Owner preview approval | ☐ APPROVED ☐ CHANGES REQUIRED | |

G04 and G12 remain open until this sheet is completed against the exact candidate SHA.
