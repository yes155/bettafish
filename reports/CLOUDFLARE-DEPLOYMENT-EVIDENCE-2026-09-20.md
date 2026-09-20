# Cloudflare Deployment and Rollback Evidence — 2026-09-20

## Candidate preview

- Branch: `chatgpt-work`
- Candidate Git SHA: `90a45a1237192fc10221231c1f6bfc3d8a8b236d`
- GitHub validation: **PASS**
- Cloudflare Pages check: **PASS**
- Cloudflare deployment ID: `1b60c46c-1c18-4696-83c7-46b8bdab147f`
- Immutable deployment preview: `https://1b60c46c.bettafish-4kt.pages.dev`
- Branch preview: `https://chatgpt-work.bettafish-4kt.pages.dev`
- Cloudflare check recorded at: 2026-09-20 12:47 UTC

GitHub's Cloudflare Pages check reports **Deployed successfully** for the exact candidate SHA above.

## Rollback baseline

- Production branch: `main`
- Previous production Git SHA: `aa696c31ed5274db80a60ed1cd9f7d89a8a2cbce`
- GitHub validation: **PASS**
- Cloudflare Pages check: **PASS**
- Previous Cloudflare deployment ID: `0758d976-fc9d-41e6-8e21-039fd9aeea43`
- Immutable deployment preview: `https://0758d976.bettafish-4kt.pages.dev`
- Cloudflare check recorded at: 2026-09-19 09:30 UTC

## Rollback instruction

If any hard live check fails after production promotion:

1. restore Cloudflare deployment `0758d976-fc9d-41e6-8e21-039fd9aeea43`, **or** revert production source to Git SHA `aa696c31ed5274db80a60ed1cd9f7d89a8a2cbce`;
2. verify the homepage and representative article routes;
3. verify `robots.txt`, `sitemap.xml`, HTTPS and security headers;
4. verify the custom domain is serving the restored deployment;
5. investigate and fix only on `chatgpt-work` before another production attempt.

## Gate interpretation

- G12 deployment evidence: **PARTIAL PASS** — exact candidate URL and deployment ID now recorded.
- G14 rollback evidence: **READY / DRY-RUN NOT YET EXECUTED** — previous Git SHA and deployment ID are recorded; an actual restore should not be performed solely to prove the gate unless needed, because it would unnecessarily disturb the current production site.
- G13 production: still **BLOCKED** — the approved candidate has not been intentionally promoted to production and sitewide noindex remains enabled.

## Environment limitation

Automated HTTP access from the current assistant environment cannot resolve the Cloudflare Pages preview hostname, so browser/network checks for status codes, response headers and viewport rendering remain manual/Cloud Browser tasks. This limitation does not affect the recorded GitHub/Cloudflare deployment evidence.
