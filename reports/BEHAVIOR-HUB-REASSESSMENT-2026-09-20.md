# Behavior Hub Reassessment — 2026-09-20

## Decision

**Do not create a standalone Behavior hub now.**

Keep the current behavior-oriented articles under `/biology-genetics/` and strengthen navigation from the existing Biology & Genetics hub through the derived related-guides layer.

## Why

The current behavioral cluster is substantial enough to be useful but not coherent enough to justify a separate category owner:

- `/behavior/unhappy-betta/` — welfare/behavior-change triage
- `/anatomy/betta-fish-sleep/` — rest/sleep behavior
- `/behavior/hearing-music/` — sensory response
- `/behavior/flaring-triggers/` — threat/display behavior
- `/behavior/bubble-nests/` — reproductive behavior
- `/behavior/enrichment-safe-toys/` — environmental enrichment

These pages serve different intents and already have clean individual query ownership.

## Keyword-file evidence

The 523-keyword Planner export does **not** contain a strong broad `betta fish behavior` query family that would justify a new category page.

Behavior/welfare demand appears as narrower tasks instead:

- `stressed betta fish` — 5,000 Planner bucket
- `betta fish happy` — 500
- `betta fish playing` — 50
- Bubble-nest, enrichment, sleep, flaring and sensory questions appear as separate tasks rather than one broad category task.

The PAA file also contains multiple social-cognition and welfare questions, but they are heterogeneous: happiness, talking, owner recognition, memory, daily activity and enrichment. They do not yet establish a single broad hub intent that is stronger than the existing Biology & Genetics routing role.

## Cannibalization risk

A new Behavior hub would need a primary query such as `betta fish behavior`, `betta behavior` or `betta fish behavior guide`.

At present that page would likely overlap with:

- Unhappy Betta for behavior/welfare changes;
- Enrichment for activity and stimulation;
- Flaring for aggression/display;
- Sleep for resting behavior;
- Hearing/Music for sensory response.

Creating the hub merely because several URLs use the `/behavior/` path would be architecture-by-folder rather than search-task ownership.

## Navigation action

Use the existing Biology & Genetics hub as the category parent.

Add derived hub links to:
- Bubble Nests
- Enrichment & Safe Toys
- Betta Fish Types

This improves discoverability without changing the approved `content/pages/biology-hub.json` source hash.

## Reassessment trigger

Reconsider a Behavior hub only after launch data provides evidence that a broad behavior category task exists.

Useful triggers:
- sustained GSC impressions for a broad `betta fish behavior` query family;
- several behavior articles earning overlapping broad-category impressions;
- navigation/user-path data showing readers need a separate behavior landing page;
- enough distinct behavior content that Biology & Genetics becomes materially difficult to navigate.

Until then, the cleaner architecture is:

**Biology & Genetics hub → distinct behavior articles → contextual cross-links.**
