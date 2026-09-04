# Page-Type Contracts

## Homepage

Must contain:

- direct value proposition;
- Start Here sequence;
- topic navigation;
- trust/evidence summary;
- clear next action.

Metadata/schema: WebSite, Organization and WebPage; canonical; OG/X once social media exists.

Launch blockers: approved hero or explicit no-hero owner decision, complete media manifest, responsive screenshots.

## Hub

Must contain:

- unique introduction and role boundary;
- decision or learning sequence;
- child-page cards with unique descriptions;
- prerequisite and next-step handoffs;
- no generic list-only layout.

Metadata/schema: CollectionPage and BreadcrumbList.

## Article

Must contain:

- direct answer near the beginning;
- sections tied to actual subquestions or processes;
- evidence and source provenance;
- author, reviewer where required, and editorial dates;
- exclusions and canonical handoffs;
- related next action.

Metadata/schema: Article and BreadcrumbList. FAQPage only when a visible, exact FAQ exists.

## Health article

Inherits the Article contract and additionally requires:

- symptom-first language without claiming individualized diagnosis;
- explicit water-quality and environmental checks;
- current authoritative sources for medication, dosing and prognosis claims;
- qualified reviewer identity;
- escalation to an aquatic veterinarian or appropriate professional;
- an honest statement when prognosis is poor or uncertainty is high.

## Trust page

Must contain accurate, stable publisher information. No office, credential, staff, review or contact claim may be inferred or invented.

Schema varies by AboutPage, ContactPage, PrivacyPolicy or WebPage. Person/ProfilePage is emitted for the approved author and reviewer identities, with externally supported experience and explicit scope limits.

## Search and tools

Not included in the foundation launch scope. Adding either is an architecture change requiring dedicated contracts, fixtures and accessibility/safety testing.
