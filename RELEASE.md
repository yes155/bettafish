# Release and Rollback Procedure

## Branches

- `main`: protected production source.
- `chatgpt-work`: prelaunch integration and Cloudflare branch preview.
- optional `change/<scope>`: one bounded concern.

## Candidate procedure

1. Start from a clean checkout.
2. Run `python3 scripts/build.py`.
3. Run `python3 scripts/audit.py`.
4. Confirm the source diff and generated diff match the declared scope.
5. Push to `chatgpt-work`.
6. Confirm CI belongs to the latest candidate SHA.
7. Review the Cloudflare branch preview at all required viewports.
8. Record warnings and intentional exceptions.
9. Open a pull request to `main` only when all hard gates pass.
10. Merge only after owner approval.

## Cloudflare Pages settings

- Build command: `python3 scripts/build.py && python3 scripts/audit.py`
- Output directory: `public`
- Production branch: `main`
- Preview branch: `chatgpt-work`

Do not connect `bettafish.website` until the preview candidate passes G12.

## Rollback

Before production promotion, record:

- previous production Git SHA;
- candidate Git SHA;
- previous Cloudflare deployment ID;
- candidate Cloudflare deployment ID;
- owner and timestamp.

If any hard live check fails, restore the previous Cloudflare deployment or revert the production commit, verify representative routes, robots, sitemap and HTTPS, then investigate from the preview branch.

## Recorded 2026-09-20 candidate

- Candidate branch: `chatgpt-work`
- Candidate Git SHA: `90a45a1237192fc10221231c1f6bfc3d8a8b236d`
- Candidate Cloudflare deployment ID: `1b60c46c-1c18-4696-83c7-46b8bdab147f`
- Candidate immutable preview: `https://1b60c46c.bettafish-4kt.pages.dev`
- Candidate branch preview: `https://chatgpt-work.bettafish-4kt.pages.dev`
- Previous production Git SHA: `aa696c31ed5274db80a60ed1cd9f7d89a8a2cbce`
- Previous Cloudflare deployment ID: `0758d976-fc9d-41e6-8e21-039fd9aeea43`
- Previous immutable deployment preview: `https://0758d976.bettafish-4kt.pages.dev`
- Recorded by: project owner workflow / ChatGPT-assisted release record
- Recorded at: 2026-09-20

An actual rollback restore is not executed merely as a gate exercise because that would disturb the current production deployment. These identifiers are the pre-promotion rollback target if a hard live check fails.

## Stage 2 indexing release — 2026-09-20

Owner launch approval is recorded in `reports/OWNER-LAUNCH-APPROVAL-2026-09-20.md`.

### Verified pre-index production baseline

- Main Git SHA: `6da9d33425d2e19ba338ca080870eb02b5397f20`
- Cloudflare deployment ID: `3f8b7a05-46ed-4b17-8fdd-c5473850a9bc`
- Deployment result: successful
- Indexing state: sitewide noindex / prepublication

This deployment is the immediate rollback target for the indexing release because it contains the complete approved 54-page site while keeping search indexing disabled.

### Stage 2 change scope

Only the launch-mode configuration changes:

- `sitewide_noindex: true` → `false`
- `environment: prepublication` → `production`

No article, media, schema model, navigation, query ownership, reviewer attribution or editorial source is changed by this stage.
