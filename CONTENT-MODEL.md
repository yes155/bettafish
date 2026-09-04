# Content Model

## Source-of-truth hierarchy

| Published value | Authoritative source |
|---|---|
| Domain, brand and site-wide indexability | `config/site.json` |
| URL, role, parent, intent, status and output mapping | `data/page-registry.csv` |
| Page copy and page-level metadata | `content/pages/*.json` |
| Author/editor identities, profile URLs and external identity links | `data/people.json` |
| Hero, card, social, logo and favicon mapping | `data/media-manifest.csv` |
| Evidence provenance | `data/source-register.csv` |
| Styling and responsive behaviour | `site/styles/main.css` and `DESIGN-SYSTEM.md` |
| Generated HTML, sitemap and robots | `public/`, produced by `scripts/build.py` |

## Structured page source

Every JSON page source contains:

- `url`
- `page_type`
- `status`
- `indexable`
- `title`
- `description`
- `h1`
- `eyebrow`
- `intro`
- `updated`
- `sections`

Editorial guides also use `author_id` and `reviewer_id`. Profile pages use `person_id`. Each identifier must resolve through `data/people.json`, and the generator emits linked visible credits plus Person schema.

The generator escapes text content. Deliberate links and cards are structured objects rather than arbitrary HTML.

## Publication statuses

| Status | Meaning |
|---|---|
| `review` | Built for preview review; not production-approved |
| `draft` | Built only when useful for architecture/design preview |
| `blocked-owner-input` | Missing a real owner-supplied fact or identity |
| `planned` | Registry entry only; no output expected |
| `approved` | Eligible for production only after all applicable gates pass |

## Health-content rule

No disease, treatment or diagnostic page can move to `approved` without:

1. claim-level current sources;
2. author and editorial reviewer assignment;
3. a qualified health reviewer where the claim risk requires one; Kate Barrington's editorial review does not by itself satisfy an aquatic-veterinary review gate;
4. non-diagnostic language;
5. emergency/escalation guidance;
6. dated review evidence.
