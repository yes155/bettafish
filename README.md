# BettaFish.website

Prepublication source repository for **bettafish.website**.

The project is intentionally configured as a blocked, noindex preview until every hard launch gate passes. The source files in `content/`, `config/`, `data/`, `site/`, and `scripts/` are authoritative. The generated `public/` directory is never the primary edit target.

## Technology

- Static HTML generator written in Python 3 standard library
- No runtime database or server-side application
- Build command: `python3 scripts/build.py`
- QA command: `python3 scripts/audit.py`
- Generated output: `public/`
- Intended deployment: GitHub branch preview to Cloudflare Pages

## Local build

```bash
python3 scripts/build.py
python3 scripts/audit.py
python3 -m http.server 8000 --directory public
```

Then open `http://localhost:8000/`.

## Current status

The complete 51-page local candidate builds reproducibly and passes the automated audit. All 20 editorial and seven clinical candidates have written exact-version approval tied to matching SHA-256 hashes, and all 44 registered media assets are approved and present.

Generated search metadata can be refined through `data/seo-overrides.json` without changing reviewer-approved source files or their hashes. The audit enforces unique search metadata, universal navigation and footer coverage, unique editorial hero media, and correct robots/sitemap behavior in both preview and production modes.

It is **not approved for production**. The following remain hard blockers:

- a clean GitHub Actions pass for the new candidate commit;
- restoration of the Cloudflare deployment/custom-domain path (the public domain returned a 502 on 2026-09-19);
- Cloudflare branch-preview deployment and responsive visual approval;
- live accessibility, security-header, HTTPS and indexing-control verification;
- recorded candidate SHA, deployment ID, owner sign-off and rollback target.

Exact-version reviewer handoff and approval tracking are recorded in
`reports/EXACT-VERSION-REVIEW-HANDOFF.md`, `data/editorial-review-candidates.csv`
and `data/clinical-review-candidates.csv`.
