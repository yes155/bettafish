# Project Charter: BettaFish.website

**Status:** Draft for owner approval
**Last updated:** 2026-09-01
**Production decision:** STOP

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

## Proposed decisions requiring owner confirmation

| Field | Proposed value | Gate impact |
|---|---|---|
| Audience | English-speaking betta owners; US-first search evidence with metric and US units | G00 |
| Primary outcome | Build a trusted organic-search authority resource | G00 |
| Secondary outcome | Future affiliate or advertising revenue only after disclosure and owner approval | G00/G03 |
| 30/90/180-day metrics | Not yet supplied | G00 |
| Repository | Not yet created/connected | G10/G12 |

## Launch scope

The first planned content release contains:

- homepage;
- four journey hubs: Care, Diseases & Health, Compatibility, Biology & Genetics;
- ten core articles from the master package;
- About, Contact, Editorial Policy, Corrections Policy, Privacy Policy, Terms, Disclosure and Health Disclaimer;
- linked author and reviewer profiles for Farrukh Abdullah and Kate Barrington.

## Gate G00 decision

**FAIL / STOP.** The domain, scope, exclusions, risk class, publisher entity, editorial identities, public contact channel and delivery route are resolved. Success metrics and the monetization decision remain open.
