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
