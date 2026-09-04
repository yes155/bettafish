# MyAxolotl Retrospective: From Reactive Repairs to Preventive Controls

**Project:** MyAxolotl (`myaxolotl.us`)  
**Repository:** `yes155/axolotl-site`  
**Retrospective period:** Initial build through 31 August 2026  
**Purpose:** Record what was corrected, why it failed, how it was verified, and what a future authority site must do before publication.

## 1. Executive conclusion

MyAxolotl was not damaged by one catastrophic technical mistake. It accumulated many smaller omissions because the site was published before a complete launch contract existed. The content corpus, topical structure, static generator, trust model, media system, deployment path, and QA gates were designed at different times rather than as one system.

The month of correction work therefore had two distinct parts:

1. **Original launch omissions:** missing or incomplete trust, metadata, schema, internal-link, media, deployment, and verification controls.
2. **Repair regressions:** a global CSS rule fixed one display problem but affected another page type; a build used stale source or queued jobs; a new image was mapped to the wrong article; generated output drifted from source changes.

The main lesson is not “do more checking.” It is: **define the site as a set of versioned contracts, make every contract testable, and block production when any hard contract fails.**

## 2. Evidence used

This retrospective was reconstructed from:

- the project conversation history and recorded decisions;
- the GitHub commit history from the initial static-site pipeline through the image and Diet-card corrections;
- repository build code, configuration, workflows, and generated output;
- Phase 7–12 semantic, search, integrity, and production QA reports;
- the final Phase 14 launch-verification record;
- the semantic SEO methodology, topical audit structure, knowledge base, and project instructions supplied for MyAxolotl.

The repository history contains 112 commits in the reviewed period. The sequence is especially informative: the initial pipeline landed on 19 August; production launch on 22 August; deployment, layout, branding, metadata, schema, content-safety, build automation, and image corrections continued through 31 August.

## 3. What the site became

By the mature audit stage, MyAxolotl had:

- 108 article pages;
- 12 topical hubs plus the main Axolotls hub;
- 5 interactive tools;
- author, editor, publisher, About, Editorial Policy, Contact, and Privacy trust pages;
- a static Python build system driven by `build/build.py` and `build/config.py`;
- a generated `public/` site deployed through GitHub and Cloudflare;
- a `chatgpt-work` branch and a Windows self-hosted runner for builds that depended on an external DOCX source directory;
- semantic link-graph, search-routing, FAQ, schema, metadata, sitemap, and production verification reports.

This final state should not be confused with the initial launch state. Much of it was built during the correction period.

## 4. Chronological reconstruction

| Date | Workstream | What changed | Lesson for future sites |
|---|---|---|---|
| 19 Aug | Foundation | Static generator and Phase 7 semantic-audit artifacts were committed; tool and Diet↔Health edges followed. | Build the audit model with the generator, not after content is rendered. |
| 22 Aug | Launch | Production launch and a Phase 14 verification record were created. The first record still showed Cloudflare and live-domain verification as unconfirmed. | “Code pushed” and “site live and verified” are separate gates. |
| 23 Aug | Hosting/build | Cloudflare Git deployment, Python/Pillow dependencies, portable paths, logo/favicon, homepage hero, Care hub, Start Here layout, and hero aspect ratio were corrected. | Hosting portability, branding, responsive layout, and image rendering belonged in prelaunch acceptance tests. |
| 24 Aug | Homepage/social | Topic-card color selectors were iterated, Pinterest verification added, social profiles and footer icons added. | Test selectors against rendered markup and include social/domain-verification requirements in the launch manifest. |
| 25 Aug | Technical SEO/content conversion | X metadata, Open Graph parity, BreadcrumbList, truncated titles/descriptions, DOCX list placeholders, editorial-note leaks, and dates were corrected. | Centralize head generation and validate the transformed corpus, not only source documents. |
| 26 Aug | Content architecture/automation | FAQ/schema and remaining metadata corrections, tank setup order, link cleanups, action handoffs, and Windows build automation were added. | Page roles, procedural order, handoff links, and CI must exist before bulk publishing. |
| 27 Aug | Safety and page roles | Legal, Diet, Morphs, Breeding, Culture, Conservation, Health, symptom-checker, heading extraction, pronunciation, and Cost/Buying guidance were corrected. | YMYL-style safety, current-authority checks, and page-role boundaries require editorial gates, not just SEO checks. |
| 28 Aug | Build reliability | Stale queued runs and unrelated generated changes were diagnosed; latest-run cancellation and scope protection were added. | Concurrency, source ownership, and diff-scope rules are part of content integrity. |
| 29–31 Aug | Media system | Category image batches were added; Care, Diet, Tank Setup, Health, Culture, and other heroes were restored or protected; crop, letterbox, and wrong-image mapping problems were corrected. | An image is not complete until mapping, metadata, intrinsic ratio, card behavior, and live rendering all pass. |

## 5. Correction and prevention register

The register below converts actual MyAxolotl work into controls for future sites.

| # | Observed problem | Diagnosis / root cause | Correction made | Preventive control |
|---:|---|---|---|---|
| 1 | Production was initiated while Cloudflare project/domain/live checks were still unverified. | Launch was treated as a repository event rather than an end-to-end production state. | Phase 14 recorded build, GitHub, Cloudflare, HTTPS, representative URLs, robots, sitemap, canonicals, structured data, and live search separately. | A production release cannot pass until the deployment provider, custom domain, HTTPS, and live-route checks all provide evidence. |
| 2 | Build paths failed outside the original Windows machine. | Source and output paths were hard-coded to local directories. | Paths were made repository-relative with `pathlib`; the external source location became explicit. | No absolute developer-machine paths. CI runs the build in a clean checkout before launch. |
| 3 | Cloudflare builds required missing Python image dependencies. | Runtime dependencies were implicit on the development computer. | `requirements.txt` and Pillow dependencies were completed. | Lock and install dependencies in CI; build in the deployment runtime or a matching container. |
| 4 | External DOCX content was invisible to ordinary cloud runners. | The true content source lived outside Git. | A Windows self-hosted runner used `AXOLOTL_SOURCE_DIR` and a controlled junction. | Prefer all source in Git. If external source is unavoidable, document it as a declared dependency and make CI fail clearly when unavailable. |
| 5 | Homepage hero, logo, favicon, and Care-hub presentation required post-launch work. | Brand assets and homepage acceptance criteria were not frozen before release. | Assets and hero presentation were replaced and tuned. | Approve a brand asset manifest and desktop/mobile homepage screenshots before content-scale build begins. |
| 6 | The Start Here section had excess height and visual imbalance. | Grid children were stretched and the card/content density was not tested at target widths. | Alignment was changed from `stretch` to `start`; Start Here copy and layout were rebalanced. | Screenshot-test every major homepage section at phone, tablet, laptop, and wide desktop sizes. |
| 7 | Topic-card colors did not apply consistently. | CSS targeted `.hub-card` while rendered markup also used `.card`; dark-mode rules were not aligned. | Selectors were corrected for actual markup and light/dark variants. | CI must render templates and confirm selectors against the built DOM; do not approve CSS from source inspection alone. |
| 8 | Article hero images were visibly cropped. | A global `aspect-ratio: 3/2` plus `object-fit: cover` forced all article media into one frame. | Article heroes were changed to natural height (`height:auto`) without forced crop. | Define separate media contracts for article heroes, hub cards, social previews, and inline diagrams. Never reuse one global image rule for all contexts. |
| 9 | Diet cards later showed crop or letterbox problems. | The first media fix was too broad; source artworks had mixed ratios and some contained text near edges. | Diet-specific rules preserved full compositions and were scoped to `.hub-diet`; later they used natural dimensions and transparent backgrounds. | Page-type and hub-specific exceptions require visual regression tests on all sibling pages, not only the reported page. |
| 10 | The Beef Heart card showed an obesity graphic. | Image filename/content and page mapping were not verified as a pair. | A dedicated 1600×900 Beef Heart asset and explicit override metadata were added. | Maintain a page→asset manifest with unique path, checksum, dimensions, alt, caption, and human-approved thumbnail. Fail duplicate or suspicious mappings. |
| 11 | The Care Guide hero disappeared or was replaced during later batches. | A fallback or batch process could overwrite a previously approved page image. | An explicit `HERO_IMAGE_OVERRIDES` entry restored and protected the approved Care Guide hero. | Approved flagship images are immutable manifest entries; batch import must fail rather than overwrite them. |
| 12 | Many pages initially relied on placeholder-style hero names or generic artwork. | Media production was not completed as part of page Definition of Done. | Category batches replaced and documented heroes for Morphs, Breeding, Care Basics, Biology, Legal, Cost & Buying, Tank Setup, Health, Culture, Diet, and Merch. | A page cannot enter the launch inventory until its final local image, metadata, dimensions, and rendered preview pass. |
| 13 | Image SEO and accessibility had to be audited separately. | File naming, alt text, captions, descriptions, and dimensions were not treated as a single object. | Overrides stored descriptive filename, alt, caption, description, credit, width, and height. | Use a structured media manifest; automated tests require local WebP/AVIF, meaningful alt, intrinsic size, and no placeholder filename. |
| 14 | Footer social links and Organization profiles were incomplete. | Social identity was added after core templates. | Central social configuration and inline SVG icons were added; Organization `sameAs` was aligned. Discord was intentionally excluded from `sameAs`. | Create a social identity manifest before schema/template work; validate link targets and the exact `sameAs` allowlist. |
| 15 | Open Graph existed but X/Twitter metadata was incomplete. | Head metadata was implemented incrementally and tool pages had separate heads. | Central `page_html()` added X title, description, image, site, and creator; tool pages received equivalent injection. | One metadata API must cover every page type. Tests compare title/description/image parity across HTML, OG, and X tags and require absolute image URLs. |
| 16 | Some article titles and meta descriptions were truncated or out of range. | DOCX-derived fields and automatic shortening were not validated against search-display constraints. | Specific source overrides corrected truncated fields; remaining outliers were reviewed manually. | Validate uniqueness, presence, clipping artifacts, and sensible length. Length is a review signal, not an automatic rewrite instruction. |
| 17 | Breadcrumb schema was missing on rendered pages and standalone tools. | Schema generation did not cover every template family. | BreadcrumbList was added to normal pages and then to standalone tools. | Keep a page-type/schema matrix and test each template against it. |
| 18 | A Pinterest verification HTML file had an empty title and became an audit outlier. | A verification artifact was treated like a normal indexable page by the crawler. | The artifact was preserved for verification and isolated for explicit review rather than blindly rewritten. | Classify special files in the URL inventory: verification, noindex utility, redirect, or indexable content. Never let them silently enter content QA. |
| 19 | Raw `<UL_*>` / `<OL_*>` placeholders appeared after DOCX conversion. | Source conversion emitted intermediate tokens that were not fully resolved. | Converter logic was fixed and the rendered corpus was globally searched for residual tokens. | Maintain “forbidden output patterns” tests for placeholders, editorial markers, unclosed tags, and conversion artifacts. |
| 20 | Editorial notes leaked into an article, hub preview, and search index. | Internal source metadata flowed through the same field used for public introductions. | A repository-controlled intro override removed the leak at all outputs. | Separate editorial metadata from publishable content at the schema level; scan rendered pages and search indexes for internal markers. |
| 21 | Publication/update dates were synthetic or unstable. | Build time and content dates were conflated. | Verified article dates were persisted instead of being regenerated on every build. | Dates are content data with provenance. A build must not invent or silently refresh them. |
| 22 | Visible FAQ sections and FAQPage schema were inconsistent on some pages. | FAQ detection and page intent were treated as bulk rules. | Genuine visible question-answer sections received schema; answer-like sections without a true FAQ were intentionally left without it. | Enforce visible-content/schema parity. Never add FAQPage only to satisfy a warning, and never synthesize FAQs without editorial approval. |
| 23 | Internal linking had weak semantic joints and `/tools` was a dead end. | Hubs and footer links made the site navigable, but contextual relationships were incomplete. | Phase 8 added 22 targeted relationships; content edges rose 414→433, cross-cluster edges 81→100, Health↔Biology 1→10, Breeding↔Diet 0→7, and zero-outbound pages 1→0. | Build a link graph before launch; require purposeful relationship labels, hub return paths, tool↔guide reciprocity, and zero unexplained dead ends. |
| 24 | Some candidate cross-links were tempting but semantically weak. | Link quantity could have been optimized at the expense of relevance. | Unsupported Morphs↔Health and other forced links were explicitly rejected. | Every added internal edge needs a named relationship and a sentence-level contextual bridge. Reject “SEO-only” links. |
| 25 | Search routing returned unsafe or irrelevant results for urgent, symptom, price, typo, and fasting queries. | Full-text relevance alone could not model safety or canonical intent. | Rule families, precedence, route boosts, typo aliases, tool descriptions, and 20+21 smoke tests were added. | Define query-intent fixtures before launch, including safety-critical, commercial, typo, ambiguous, and “must not hijack” tests. |
| 26 | Symptom checker behavior risked overclaiming or poor triage. | A utility was treated as a content feature rather than a health-safety decision aid. | Triage-safe language, escalation paths, and related guidance were added. | Health tools require non-diagnostic language, emergency escalation, source review, and negative tests for dangerous reassurance. |
| 27 | Legal and conservation guidance required factual corrections. | Time-sensitive authority claims were published without a current-authority verification gate. | Federal transport/legal language, conservation roles, and handoffs were clarified. | Time-sensitive legal, health, price, and status claims need dated source verification and a recheck schedule before launch. |
| 28 | Hub/article roles overlapped or lacked action handoffs. | Topical map described topics but not always the canonical job of each page. | Diet, Morphs, Breeding, Culture, Conservation, Health, Tank Setup, and other role/handoff notes were clarified. | Each URL needs a page-role record: primary intent, unique promise, owner query, excluded scope, parent, sibling, prerequisite, and next action. |
| 29 | Duplicate contextual links and weak action handoffs appeared. | Links were added piecemeal without page-level duplicate and path checks. | Duplicate water-change/conditioner links were removed; acclimation, odor, and uneaten-food handoffs were strengthened. | Fail duplicate same-destination links in the main body unless justified; test the user journey, not only link validity. |
| 30 | Builds queued behind stale runs and produced older output after newer changes. | Workflow concurrency used `cancel-in-progress:false`. | Latest-run cancellation was enabled for the main build workflow. | One concurrency group per deployable branch; latest candidate cancels stale candidates; generated commits include loop-prevention markers. |
| 31 | Unrelated generated source/image changes entered otherwise focused fixes. | The build regenerated broad output and the diff was not constrained to expected effects. | Unrelated changes were explicitly excluded in several commits. | Every PR declares expected paths and maximum diff class; CI flags unexpected source, generated, or asset changes. |
| 32 | Direct generated-output changes risked being overwritten by the next build. | The source/generated boundary was not consistently enforced. | Durable fixes moved into `build.py`, `config.py`, CSS source, manifests, or workflows; generated HTML was rebuilt. | Generated output is never the primary edit target. Emergency edits require an immediate source fix and rebuild. |
| 33 | A successful local build did not prove the live site matched it. | Local, GitHub, Cloudflare, and public states could diverge. | Final verification checked SHA parity, deployment, domain, HTTPS, representative 200s, robots, sitemap, canonicals, schema, and live search. | Release evidence must identify source SHA, generated SHA/artifact, Cloudflare deployment, and live checks from the public domain. |

## 6. Quantitative evidence of improvement

### Semantic architecture

| Metric | Before | After |
|---|---:|---:|
| Content internal edges | 414 | 433 |
| Cross-cluster edges | 81 | 100 |
| Average content outbound links | 3.34 | 3.49 |
| Health↔Biology edges | 1 | 10 |
| Breeding↔Diet edges | 0 | 7 |
| Zero-outbound pages | 1 | 0 |

Later phases expanded the content graph further while preserving zero broken links and canonical correctness.

### Search and technical QA

- Phase 10 search smoke: 20/20 passed.
- Phase 11 natural-language search smoke: 21/21 passed.
- Phase 11 weighted QA: 100/100.
- Phase 12 weighted QA: 100/100.
- Phase 12 inventory: 132 audited pages, including 108 articles, 12 hubs, 5 tools, and utility pages.
- Final production verification recorded no launch blockers after Cloudflare and live-domain checks were completed.

### Later on-page audit

A later 136-page audit reported 107 clean pages, 1 critical, 14 important, and 14 minor. The remaining findings were predominantly page-specific title, meta, FAQ/schema, and content-length review items—not sitewide heading, internal-link, or image failures. That is evidence that the systemic corrections worked, but it also shows why a launch gate must inspect both global contracts and individual-page exceptions.

## 7. Root causes

### 7.1 No single prelaunch Definition of Done

The project had good individual ideas—topical mapping, content, tools, schema, images, and hosting—but no one checklist stated what “ready to publish” meant for every page and for the site as a whole.

### 7.2 Source-of-truth fragmentation

Content lived in external DOCX files, templates and overrides lived in Python, styling lived in CSS, tools had standalone heads, and generated HTML lived in `public/`. This created several paths for drift.

### 7.3 Template contracts were implicit

Hero, hub card, tool, article, trust, search, and verification pages did not initially have explicit contracts for metadata, schema, images, aspect ratio, and responsive behavior.

### 7.4 Media was treated as decoration

The late image batches revealed that an image is structured page data. Its identity, page mapping, crop behavior, metadata, and social-preview behavior must be designed together.

### 7.5 QA arrived after production

The strongest audit scripts and reports were created after launch. Once they existed, the site became measurably stable. They should be part of the starter repository for the next site.

### 7.6 The release path lacked an early staging contract

Repository state, generated output, Cloudflare deployment, and live behavior were initially verified separately and late. A branch preview and promotion checklist would have exposed most issues before the custom domain served them.

### 7.7 Fixes were not always scoped by template family

Global CSS and batch asset operations produced regressions. The missing control was a regression matrix: every change declares affected templates and triggers screenshots/tests for all of them.

## 8. What worked well and should be retained

1. **Static, configuration-driven generation.** Once the contracts were centralized, sitewide fixes became consistent and reviewable.
2. **Semantic audit artifacts.** The page-role, graph, gap, and decision reports prevented blind link insertion and cannibalization fixes.
3. **Hard STOP integrity verification.** The Phase 12 method required evidence rather than optimistic completion claims.
4. **Small, named commits.** Commit subjects reveal what was changed and allow precise retrospective analysis.
5. **Search smoke fixtures.** Natural-language and safety-critical search behavior became testable.
6. **Explicit image overrides.** Approved page-specific media could be protected from batch fallback logic.
7. **Source-first fixes.** Durable corrections moved into generator/config/CSS/workflow sources and were rebuilt.
8. **Final live verification.** The mature launch record separated local success from production success.

## 9. Final lessons to carry forward

1. Plan page roles and user journeys before writing the corpus.
2. Put every source required for a build under versioned control when possible.
3. Define page-type contracts before designing individual pages.
4. Define media ratios and display contexts before generating images.
5. Centralize metadata and schema; eliminate one-off page heads.
6. Treat health, legal, financial, price, and status claims as higher-risk content.
7. Build the semantic graph deliberately and record rejected links as well as accepted ones.
8. Test rendered output, not only source files.
9. Use a preview branch and Cloudflare preview before production promotion.
10. Make launch a hard-gated evidence decision, not a date or feeling.
11. Make every repair prove it did not regress sibling templates.
12. Preserve a complete release manifest so the live site can be reproduced and rolled back.

## 10. Retrospective decision

The next authority site should not copy the MyAxolotl sequence. It should copy the mature MyAxolotl controls and run them **before** production. The connected document, **Authority Site Pre-Publication Operating System**, turns these lessons into a reusable workflow for ChatGPT, GitHub, and Cloudflare.
