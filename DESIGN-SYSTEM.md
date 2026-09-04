# Design System: BettaFish.website

**Status:** Foundation draft
**Reference:** Bunstay, selected by the owner
**Rule:** Reuse principles, not exact layouts, wording, illustrations, colors or component measurements.

## Design direction

BettaFish.website should feel like a calm field guide: editorial, confident, warm and easy to navigate. It should avoid the visual language of a pet store, generic affiliate blog or clinical hospital.

The approved reference contributes these principles:

- a strong editorial headline with a clear welfare position;
- restrained navigation organized around keeper tasks;
- scannable recent-guide and topic-card sections;
- a visible Start Here sequence;
- explicit author, evidence and limitation information;
- generous whitespace and readable long-form typography.

## Brand distinction

BettaFish.website will use its own identity:

- water-inspired deep green rather than copying the reference palette;
- coral used sparingly for actions and warnings;
- a cream reading surface rather than pure white;
- rounded editorial cards with quiet borders instead of heavy shadows;
- a typographic hero until a unique, approved betta visual is supplied.

## Tokens

```css
:root {
  --color-canvas: #f6f2e8;
  --color-surface: #fffdf8;
  --color-ink: #162b28;
  --color-muted: #5d6f6b;
  --color-brand: #164f47;
  --color-brand-strong: #0d3934;
  --color-brand-soft: #dcebe6;
  --color-accent: #c85f50;
  --color-accent-soft: #f5dfd9;
  --color-border: #d8ded8;
  --color-warning: #7b4b15;
  --color-warning-surface: #fff2d8;
  --font-display: Georgia, "Times New Roman", serif;
  --font-body: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --reading-width: 46rem;
  --content-width: 72rem;
  --radius-small: 0.55rem;
  --radius-card: 1.15rem;
  --shadow-card: 0 0.8rem 2.2rem rgba(22, 43, 40, 0.08);
}
```

## Type scale

| Role | Size |
|---|---|
| Hero H1 | `clamp(2.6rem, 7vw, 5.6rem)` |
| Page H1 | `clamp(2.25rem, 5vw, 4.3rem)` |
| H2 | `clamp(1.55rem, 3vw, 2.35rem)` |
| H3 | `1.2rem` |
| Body | `1rem–1.08rem` |
| Small/meta | `0.82–0.9rem` |

Line length is capped at approximately 70 characters for long-form reading. Body line height is at least 1.65.

## Components

- Skip link
- Site header with desktop navigation and native mobile disclosure menu
- Editorial hero
- Topic card grid
- Ordered Start Here steps
- Evidence/trust band
- Long-form article layout
- Callout for limitations and warnings
- Breadcrumbs
- Source/review metadata panel
- Footer trust navigation

## Responsive contract

- Phone: 360×800; one-column cards; no horizontal scrolling; touch targets at least 44px.
- Tablet: 768×1024; two-column cards where content remains readable.
- Laptop: 1366×768; balanced hero and navigation without excessive vertical height.
- Wide desktop: 1920×1080; content remains capped rather than stretching edge to edge.

Breakpoints are content-driven at 45rem and 68rem.

## Accessibility contract

- WCAG 2.2 AA contrast target.
- Visible focus ring on every interactive element.
- Semantic landmarks and one H1 per page.
- Keyboard-operable mobile navigation using native `details/summary`.
- Reduced-motion preference disables transitions.
- No information communicated only by color.
- Images require meaningful alt text and declared dimensions before approval.

## Dark mode

Dark mode is not part of the launch contract. This avoids an untested parallel theme during prepublication. It may be introduced later as a scoped template change with a full screenshot matrix.

## Gate G04 status

**FAIL / STOP.** Tokens and foundation components exist, but real media, representative article/tool templates, phone/tablet/laptop/wide screenshots and owner visual approval are still required.
