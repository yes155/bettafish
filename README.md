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

The current **54-page** prepublication candidate builds reproducibly on `chatgpt-work` and passes the repository audit:

- 1 homepage, 4 hubs, 37 articles, 8 trust/policy pages, 3 profiles and 1 utility page;
- 25 editorial exact-version review rows and seven clinical exact-version review rows;
- 47 registered media assets, all approved and present;
- unique primary-query ownership, no unexplained orphan routes and unique required hero media;
- generated metadata, schema, canonical, robots/sitemap and Cloudflare header configuration pass the automated contracts;
- `sitewide_noindex` remains enabled.

Generated search metadata can be refined through `data/seo-overrides.json` without changing reviewer-approved source files or their hashes.

The repository/content candidate is **not yet approved for production**. Remaining hard blockers are outside the content inventory:

- Gate G00 owner inputs: audience/business-outcome wording, monetization stance and 30/90/180-day success metrics;
- Cloudflare branch-preview URL tied to the candidate SHA;
- responsive/keyboard/accessibility visual review on the deployed preview;
- live HTTPS/security-header/indexing-control verification;
- owner preview sign-off;
- recorded Cloudflare deployment IDs and rollback target.

The public-domain state is not treated as verified by repository CI. Keep the site noindex and do not merge to `main` until the preview and release gates pass.

Exact-version reviewer handoff and approval tracking are recorded in
`data/editorial-review-candidates.csv`, `data/clinical-review-candidates.csv`,
and the matching evidence files under `reports/`.
