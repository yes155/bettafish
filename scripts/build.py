#!/usr/bin/env python3
"""Build the BettaFish.website static preview from repository-controlled sources."""

from __future__ import annotations

import csv
import hashlib
import html
import json
import shutil
from datetime import date
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
PAGES = ROOT / "content" / "pages"
CONFIG_PATH = ROOT / "config" / "site.json"
PEOPLE_PATH = ROOT / "data" / "people.json"
REGISTRY_PATH = ROOT / "data" / "page-registry.csv"
MEDIA_PATH = ROOT / "data" / "media-manifest.csv"
EDITORIAL_REVIEW_PATH = ROOT / "data" / "editorial-review-candidates.csv"
CLINICAL_REVIEW_PATH = ROOT / "data" / "clinical-review-candidates.csv"
TEMPLATE_PATH = ROOT / "site" / "templates" / "base.html"
STYLE_PATH = ROOT / "site" / "styles" / "main.css"
STATIC_PATH = ROOT / "site" / "static"

NAV = [
    ("Care", "/care/"),
    ("Diseases & health", "/diseases/"),
    ("Compatibility", "/compatibility/"),
    ("Biology", "/biology-genetics/"),
    ("About", "/about/"),
]
FOOTER_NAV = [
    ("About", "/about/"),
    ("Editorial policy", "/editorial-policy/"),
    ("Corrections", "/corrections-policy/"),
    ("Privacy", "/privacy-policy/"),
    ("Terms", "/terms/"),
    ("Disclosure", "/disclosure/"),
    ("Health disclaimer", "/health-disclaimer/"),
    ("Contact", "/contact/"),
]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def absolute_url(config: dict, url: str) -> str:
    if url == "/":
        return config["base_url"] + "/"
    return config["base_url"] + url


def nav_html(current_url: str, items: list[tuple[str, str]]) -> str:
    links = []
    for label, url in items:
        current = current_url == url or (url != "/" and current_url.startswith(url))
        aria = ' aria-current="page"' if current else ""
        links.append(f'<a href="{esc(url)}"{aria}>{esc(label)}</a>')
    return "\n".join(links)


def breadcrumb_items(page: dict, rows_by_url: dict[str, dict]) -> list[tuple[str, str | None]]:
    if page["url"] == "/":
        return []
    items: list[tuple[str, str | None]] = [("Home", "/")]
    row = rows_by_url[page["url"]]
    parent = row.get("parent_hub", "")
    if parent and parent != "/" and parent in rows_by_url:
        parent_source = ROOT / rows_by_url[parent]["source_file"]
        if parent_source.exists() and parent_source.suffix == ".json":
            parent_page = json.loads(parent_source.read_text(encoding="utf-8"))
            items.append((parent_page["eyebrow"], parent))
    items.append((page["h1"], None))
    return items


def breadcrumbs_html(items: list[tuple[str, str | None]]) -> str:
    if not items:
        return ""
    rendered = []
    for label, url in items:
        if url:
            rendered.append(f'<li><a href="{esc(url)}">{esc(label)}</a></li>')
        else:
            rendered.append(f'<li aria-current="page">{esc(label)}</li>')
    return '<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>' + "".join(rendered) + "</ol></nav>"


def credits_html(page: dict, people: dict[str, dict]) -> str:
    credits = []
    for field in ("author_id", "reviewer_id", "clinical_reviewer_id"):
        person_id = page.get(field)
        if not person_id:
            continue
        if person_id not in people:
            raise ValueError(f"Unknown {field}: {person_id}")
        person = people[person_id]
        rel = ' rel="author"' if field == "author_id" else ""
        credits.append(
            f'<p>{esc(person["role_label"])} '
            f'<a href="{esc(person["profile_url"])}"{rel}>{esc(person["name"])}</a></p>'
        )
    if not credits:
        return ""
    return '<div class="byline" aria-label="Editorial credits">' + "".join(credits) + "</div>"


def citation_links(item: object) -> str:
    if not isinstance(item, dict) or not item.get("sources"):
        return ""
    links = "".join(
        f'<a href="#source-{int(source_id)}" aria-label="Source {int(source_id)}">[{int(source_id)}]</a>'
        for source_id in item["sources"]
    )
    return f'<sup class="citations">{links}</sup>'


def cited_text(item: object) -> str:
    if isinstance(item, dict):
        return esc(item["text"]) + citation_links(item)
    return esc(item)


def render_section(section: dict) -> str:
    section_type = section["type"]
    heading = f'<h2>{esc(section["heading"])}</h2>' if section.get("heading") else ""
    intro = f'<p class="section-intro">{esc(section["intro"])}</p>' if section.get("intro") else ""

    if section_type == "prose":
        body = "".join(f"<p>{cited_text(paragraph)}</p>" for paragraph in section.get("paragraphs", []))
        return f'<section class="content-section prose">{heading}{body}</section>'
    if section_type == "list":
        items = "".join(f"<li>{cited_text(item)}</li>" for item in section.get("items", []))
        return f'<section class="content-section">{heading}{intro}<ul class="content-list">{items}</ul></section>'
    if section_type == "cards":
        cards = []
        for card in section.get("cards", []):
            link = ""
            if card.get("url"):
                link = f'<a class="card-link" href="{esc(card["url"])}">{esc(card.get("label", "Read more"))} <span aria-hidden="true">→</span></a>'
            cards.append(f'<article class="topic-card"><h3>{esc(card["title"])}</h3><p>{esc(card["text"])}</p>{link}</article>')
        return f'<section class="content-section cards-section">{heading}{intro}<div class="card-grid">{"".join(cards)}</div></section>'
    if section_type == "steps":
        steps = "".join(
            f'<li><h3>{esc(step["title"])}</h3><p>{esc(step["text"])}</p></li>'
            for step in section.get("steps", [])
        )
        return f'<section class="content-section steps">{heading}{intro}<ol class="step-list">{steps}</ol></section>'
    if section_type == "callout":
        tone = section.get("tone", "evidence")
        link = ""
        if section.get("url"):
            link = f'<a href="{esc(section["url"])}">{esc(section.get("label", "Learn more"))} <span aria-hidden="true">→</span></a>'
        return f'<aside class="callout callout-{esc(tone)}">{heading}<p>{cited_text(section["text"])}</p>{link}</aside>'
    if section_type == "table":
        headers = "".join(f'<th scope="col">{esc(value)}</th>' for value in section["headers"])
        rows = []
        for row in section.get("rows", []):
            cells = []
            for index, value in enumerate(row):
                tag = "th" if index == 0 else "td"
                scope = ' scope="row"' if index == 0 else ""
                cells.append(f'<{tag}{scope}>{cited_text(value)}</{tag}>')
            rows.append("<tr>" + "".join(cells) + "</tr>")
        caption = f'<caption>{esc(section["caption"])}</caption>' if section.get("caption") else ""
        return (
            f'<section class="content-section table-section">{heading}{intro}'
            f'<div class="table-scroll" tabindex="0" role="region" aria-label="{esc(section.get("caption", section.get("heading", "Data table")))}">'
            f'<table>{caption}<thead><tr>{headers}</tr></thead><tbody>{"".join(rows)}</tbody></table></div></section>'
        )
    if section_type == "faq":
        items = "".join(
            f'<div><dt>{esc(item["question"])}</dt><dd>{cited_text({"text": item["answer"], "sources": item.get("sources", [])})}</dd></div>'
            for item in section.get("items", [])
        )
        return f'<section class="content-section faq-section">{heading}{intro}<dl class="faq-list">{items}</dl></section>'
    if section_type == "sources":
        rendered_sources = []
        for item in section.get("items", []):
            publisher = f' — {esc(item["publisher"])}' if item.get("publisher") else ""
            rendered_sources.append(
                f'<li id="source-{int(item["id"])}"><cite>{esc(item["title"])}</cite>'
                f'{publisher}</li>'
            )
        items = "".join(rendered_sources)
        return f'<section class="content-section sources-section">{heading}{intro}<ol class="source-list">{items}</ol></section>'
    raise ValueError(f"Unsupported section type: {section_type}")


def person_schema(person_id: str, person: dict, config: dict) -> dict:
    return {
        "@type": "Person",
        "@id": absolute_url(config, person["profile_url"]) + "#person",
        "name": person["name"],
        "url": absolute_url(config, person["profile_url"]),
        "jobTitle": person["job_title"],
        "sameAs": person.get("same_as", []),
    }


def media_public_url(media: dict) -> str:
    output = Path(media["output_file"])
    if not output.parts or output.parts[0] != "public":
        raise ValueError(f"Media output must be inside public/: {media['output_file']}")
    return "/" + Path(*output.parts[1:]).as_posix()


def hero_media_html(media: dict | None) -> str:
    if not media:
        return ""
    src = media_public_url(media)
    caption = f'<figcaption>{esc(media["caption"])}</figcaption>' if media.get("caption") else ""
    return (
        '<figure class="hero-media">'
        f'<img src="{esc(src)}" width="{int(media["width"])}" height="{int(media["height"])}" '
        f'alt="{esc(media["alt"])}" decoding="async" fetchpriority="high">'
        f'{caption}</figure>'
    )


def social_image_meta(media: dict | None, config: dict) -> str:
    if not media:
        return ""
    image_url = absolute_url(config, media_public_url(media))
    return "\n".join([
        f'  <meta property="og:image" content="{esc(image_url)}">',
        f'  <meta property="og:image:width" content="{int(media["width"])}">',
        f'  <meta property="og:image:height" content="{int(media["height"])}">',
        f'  <meta property="og:image:alt" content="{esc(media["alt"])}">',
        f'  <meta name="twitter:image" content="{esc(image_url)}">',
        f'  <meta name="twitter:image:alt" content="{esc(media["alt"])}">',
    ])


def schema_for(
    page: dict,
    config: dict,
    crumbs: list[tuple[str, str | None]],
    people: dict[str, dict],
    media: dict | None = None,
) -> dict:
    canonical = absolute_url(config, page["url"])
    webpage_type = {
        "homepage": "WebPage",
        "hub": "CollectionPage",
        "trust": "AboutPage" if page["url"] == "/about/" else "ContactPage" if page["url"] == "/contact/" else "WebPage",
        "profile": "ProfilePage",
        "utility": "WebPage",
    }.get(page["page_type"], "WebPage")
    web_page = {
        "@type": webpage_type,
        "@id": canonical + "#webpage",
        "url": canonical,
        "name": page["title"],
        "description": page["description"],
        "dateModified": page["updated"],
        "isPartOf": {"@id": config["base_url"] + "/#website"},
    }
    graph = [web_page]
    schema_target = web_page
    if page["page_type"] == "article":
        article = {
            "@type": "Article",
            "@id": canonical + "#article",
            "url": canonical,
            "headline": page["h1"],
            "description": page["description"],
            "dateModified": page["updated"],
            "mainEntityOfPage": {"@id": canonical + "#webpage"},
            "isPartOf": {"@id": config["base_url"] + "/#website"},
            "publisher": {"@id": config["base_url"] + "/#organization"},
            "about": {
                "@type": "Thing",
                "name": "Betta splendens",
                "sameAs": "https://www.wikidata.org/wiki/Q11739",
            },
        }
        source_urls = [
            item["url"]
            for section in page.get("sections", []) if section.get("type") == "sources"
            for item in section.get("items", [])
        ]
        if source_urls:
            article["citation"] = source_urls
        web_page["mainEntity"] = {"@id": article["@id"]}
        graph.append(article)
        schema_target = article
    if media:
        image_url = absolute_url(config, media_public_url(media))
        image_id = image_url + "#image"
        image_object = {
            "@type": "ImageObject",
            "@id": image_id,
            "contentUrl": image_url,
            "url": image_url,
            "width": int(media["width"]),
            "height": int(media["height"]),
            "caption": media["caption"],
            "description": media["description"],
            "creditText": media["credit"],
        }
        web_page["primaryImageOfPage"] = {"@id": image_id}
        schema_target["image"] = {"@id": image_id}
        graph.append(image_object)
    included_people = set()
    if page.get("person_id"):
        person_id = page["person_id"]
        if person_id not in people:
            raise ValueError(f"Unknown person_id: {person_id}")
        person = people[person_id]
        person_id_url = absolute_url(config, person["profile_url"]) + "#person"
        web_page["mainEntity"] = {"@id": person_id_url}
        graph.append(person_schema(person_id, person, config))
        included_people.add(person_id)
    for field, schema_field in (
        ("author_id", "author"),
        ("reviewer_id", "editor"),
        ("clinical_reviewer_id", "reviewedBy"),
    ):
        person_id = page.get(field)
        if not person_id:
            continue
        if person_id not in people:
            raise ValueError(f"Unknown {field}: {person_id}")
        person = people[person_id]
        person_id_url = absolute_url(config, person["profile_url"]) + "#person"
        schema_target[schema_field] = {"@id": person_id_url}
        if person_id not in included_people:
            graph.append(person_schema(person_id, person, config))
            included_people.add(person_id)
    if page["url"] == "/":
        graph.extend([
            {
                "@type": "WebSite",
                "@id": config["base_url"] + "/#website",
                "url": config["base_url"] + "/",
                "name": config["name"],
                "inLanguage": config["language"],
            },
            {
                "@type": "Organization",
                "@id": config["base_url"] + "/#organization",
                "name": config["publisher_name"],
                "url": config["base_url"] + "/",
                "logo": absolute_url(config, config["logo_path"]),
                "email": config["contact_email"],
            },
        ])
    elif page["page_type"] == "article":
        graph.append({
            "@type": "Organization",
            "@id": config["base_url"] + "/#organization",
            "name": config["publisher_name"],
            "url": config["base_url"] + "/",
            "logo": absolute_url(config, config["logo_path"]),
            "email": config["contact_email"],
        })
    faq_items = [
        item
        for section in page.get("sections", []) if section.get("type") == "faq"
        for item in section.get("items", [])
    ]
    if faq_items:
        graph.append({
            "@type": "FAQPage",
            "@id": canonical + "#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": item["question"],
                    "acceptedAnswer": {"@type": "Answer", "text": item["answer"]},
                }
                for item in faq_items
            ],
        })
    if crumbs:
        elements = []
        for position, (name, url) in enumerate(crumbs, start=1):
            item = absolute_url(config, url) if url else canonical
            elements.append({"@type": "ListItem", "position": position, "name": name, "item": item})
        graph.append({"@type": "BreadcrumbList", "itemListElement": elements})
    return {"@context": "https://schema.org", "@graph": graph}


def output_path_for(page_url: str) -> Path:
    if page_url == "/":
        return PUBLIC / "index.html"
    if page_url.endswith(".html"):
        return PUBLIC / page_url.lstrip("/")
    return PUBLIC / page_url.lstrip("/") / "index.html"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def approved_review_urls() -> set[str]:
    """Return approved URLs only when their sidecar evidence and source hash match."""
    approved: set[str] = set()
    for register_path in (EDITORIAL_REVIEW_PATH, CLINICAL_REVIEW_PATH):
        with register_path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                if row["status"] != "approved":
                    continue
                source_path = ROOT / row["source_file"]
                evidence_path = ROOT / row.get("approval_evidence", "")
                if not row.get("approved_date"):
                    raise ValueError(f"Approved review record has no approval date: {row['url']}")
                if not evidence_path.is_file():
                    raise FileNotFoundError(f"Approval evidence is missing: {row['url']}")
                if not source_path.is_file() or sha256(source_path) != row["source_sha256"]:
                    raise ValueError(f"Approved source hash is stale: {row['url']}")
                approved.add(row["url"])
    return approved


def publication_section(section: dict, exact_version_approved: bool) -> dict:
    """Remove internal prepublication wording without changing the reviewed source."""
    if not exact_version_approved or section.get("type") != "sources":
        return section
    published = dict(section)
    published["heading"] = "Sources"
    published.pop("intro", None)
    return published


def main() -> None:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    people = json.loads(PEOPLE_PATH.read_text(encoding="utf-8"))
    template = Template(TEMPLATE_PATH.read_text(encoding="utf-8"))
    with REGISTRY_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    rows_by_url = {row["url"]: row for row in rows}
    exact_approved_urls = approved_review_urls()
    with MEDIA_PATH.open(newline="", encoding="utf-8") as handle:
        media_rows = list(csv.DictReader(handle))
    approved_heroes: dict[str, dict] = {}
    for media in media_rows:
        if media["status"] != "approved" or media["role"] not in {"article-hero", "hub-hero"}:
            continue
        if media["page_url"] in approved_heroes:
            raise ValueError(f"Multiple approved hero images for {media['page_url']}")
        approved_heroes[media["page_url"]] = media

    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    (PUBLIC / "assets" / "css").mkdir(parents=True)
    shutil.copy2(STYLE_PATH, PUBLIC / "assets" / "css" / "main.css")
    if STATIC_PATH.exists():
        shutil.copytree(STATIC_PATH, PUBLIC, dirs_exist_ok=True)
    for media in media_rows:
        if media["status"] != "approved":
            continue
        source_path = ROOT / media["source_file"]
        output_path = ROOT / media["output_file"]
        if not source_path.is_file():
            raise FileNotFoundError(f"Approved media source is missing: {media['source_file']}")
        if PUBLIC.resolve() not in output_path.resolve().parents:
            raise ValueError(f"Approved media output is outside public/: {media['output_file']}")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, output_path)

    manifest = []
    generated_urls = []
    requested_indexable_urls: set[str] = set()
    for source in sorted(PAGES.glob("*.json")):
        page = json.loads(source.read_text(encoding="utf-8"))
        if page["url"] not in rows_by_url:
            raise ValueError(f"Page source not in registry: {source}")
        registry_status = rows_by_url[page["url"]]["status"]
        if registry_status.startswith("planned"):
            continue
        if page["status"].startswith("planned") and page["url"] not in exact_approved_urls:
            raise ValueError(f"Registry promotion lacks exact-version approval: {page['url']}")

        crumbs = breadcrumb_items(page, rows_by_url)
        globally_blocked = bool(config["sitewide_noindex"])
        requested_indexable = bool(page.get("indexable")) or page["url"] in exact_approved_urls
        if requested_indexable:
            requested_indexable_urls.add(page["url"])
        indexable = requested_indexable and not globally_blocked
        robots = "index, follow" if indexable else "noindex, nofollow"
        canonical = absolute_url(config, page["url"])
        hero_media = approved_heroes.get(page["url"])
        content = "\n".join(
            render_section(publication_section(section, page["url"] in exact_approved_urls))
            for section in page.get("sections", [])
        )
        rendered = template.safe_substitute(
            language=esc(config["language"]),
            title=esc(page["title"]),
            description=esc(page["description"]),
            robots=robots,
            canonical=esc(canonical),
            site_name=esc(config["name"]),
            schema=json.dumps(schema_for(page, config, crumbs, people, hero_media), ensure_ascii=False).replace("</", "<\\/"),
            twitter_card="summary_large_image" if hero_media else "summary",
            social_image_meta=social_image_meta(hero_media, config),
            favicon_path=esc(config["favicon_path"]),
            logo_path=esc(config["logo_path"]),
            body_class=f'page-{esc(page["page_type"])}',
            primary_nav=nav_html(page["url"], NAV),
            mobile_nav=nav_html(page["url"], NAV),
            breadcrumbs=breadcrumbs_html(crumbs),
            eyebrow=esc(page["eyebrow"]),
            h1=esc(page["h1"]),
            intro=esc(page["intro"]),
            credits=credits_html(page, people),
            hero_media=hero_media_html(hero_media),
            content=content,
            updated=esc(page["updated"]),
            updated_display=date.fromisoformat(page["updated"]).strftime("%B %-d, %Y"),
            footer_nav=nav_html(page["url"], FOOTER_NAV),
        )
        output = output_path_for(page["url"])
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered.rstrip() + "\n", encoding="utf-8")
        generated_urls.append(page["url"])
        manifest.append({
            "url": page["url"],
            "source": str(source.relative_to(ROOT)),
            "source_sha256": sha256(source),
            "output": str(output.relative_to(ROOT)),
            "output_sha256": sha256(output),
            "status": registry_status,
            "page_indexable": requested_indexable,
            "effective_indexable": indexable,
        })

    robots_text = "User-agent: *\nDisallow: /\n" if config["sitewide_noindex"] else f"User-agent: *\nAllow: /\nSitemap: {config['base_url']}/sitemap.xml\n"
    (PUBLIC / "robots.txt").write_text(robots_text, encoding="utf-8")

    sitemap_urls = [] if config["sitewide_noindex"] else [
        url for url in generated_urls
        if url != "/404.html" and url in requested_indexable_urls
    ]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sitemap.extend(f"  <url><loc>{esc(absolute_url(config, url))}</loc></url>" for url in sitemap_urls)
    sitemap.append("</urlset>")
    (PUBLIC / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
    (PUBLIC / "build-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Built {len(manifest)} pages into {PUBLIC}")


if __name__ == "__main__":
    main()
