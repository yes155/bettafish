# Project Charter: BettaFish.website

**Status:** Owner-approved launch charter
**Last updated:** 2026-09-01
**Production decision:** APPROVED FOR CONTROLLED RELEASE

## Confirmed decisions

| Field | Decision |
|---|---|
| Site name | BettaFish.website |
| Canonical domain | `https://bettafish.website` |
| Legacy identity | `MyBettaCare.com` must not appear in generated output |
| Site type | Editorial authority/information site |
| Delivery route | ChatGPT → GitHub → Cloudflare Pages |
| Design benchmark | Bunstay, used for principles only and never copied |
| Core scope | Betta care, aquarium setup, water, feeding, health, compatibility, behaviour, lifespan and morphology |
| Explicit exclusions | Local-business positioning, Burlington office, invented credentials, fish-fighting promotion, diagnosis presented as veterinary care |
| Risk class | Pet health and animal-welfare guidance; health pages require elevated review |
| Source package | `master-betta-site-package.md`, treated as draft source material rather than unquestioned final copy |
| Build approach | Python static generator using repository-controlled structured content |
| Build command | `python3 scripts/build.py` |
| QA command | `python3 scripts/audit.py` |
| Output directory | `public/` |
| Publisher entity | BettaFish.website |
| Research and writing | Farrukh Abdullah |
| Review and editing | Kate Barrington |
| Public contact | `bettafish.website@gmail.com` |
| Repository | `yes155/bettafish` |
| Integration branch | `chatgpt-work` |

## Owner-approved launch decisions

| Field | Proposed value | Gate impact |
|---|---|---|
| Audience | English-speaking betta owners; US-first search evidence with metric and US units | G00 |
| Primary outcome | Build a trusted organic-search authority resource | G00 |
| Secondary outcome | Future affiliate or advertising revenue only after disclosure and owner approval | G00/G03 |
| 30/90/180-day metrics | Operational SEO framework in `reports/G00-OWNER-DECISION-PACKET-2026-09-20.md` | G00 |

## Launch scope

The current prepublication candidate contains **54 registered pages**:

- 1 homepage;
- 4 journey hubs;
- 37 articles;
- 8 trust/policy pages;
- 3 named profile pages;
- 1 utility 404 page.

The content scope now includes the approved Bubble Nests, Enrichment & Safe Toys, and Betta Fish Types additions. The candidate remains sitewide noindex and is not yet approved for production.

## Gate G00 decision

**PASS.** Owner approval was recorded on 2026-09-20 in `reports/OWNER-LAUNCH-APPROVAL-2026-09-20.md`. The audience, business outcome, monetization stance and 30/90/180-day success framework are now confirmed.
