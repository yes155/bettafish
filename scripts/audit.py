#!/usr/bin/env python3
"""Audit the generated foundation and enforce preview launch controls."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from html import unescape as html_unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
CONFIG = json.loads((ROOT / "config" / "site.json").read_text(encoding="utf-8"))
PEOPLE = json.loads((ROOT / "data" / "people.json").read_text(encoding="utf-8"))
EDITORIAL_REVIEW_PATH = ROOT / "data" / "editorial-review-candidates.csv"
CLINICAL_REVIEW_PATH = ROOT / "data" / "clinical-review-candidates.csv"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.meta: list[dict[str, str]] = []
        self.canonicals: list[str] = []
        self.icons: list[str] = []
        self.title_count = 0
        self.h1_count = 0
        self.schema_blocks: list[str] = []
        self.images: list[dict[str, str]] = []
        self._in_title = False
        self._in_schema = False
        self._schema_buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value or "" for key, value in attrs}
        if tag == "a" and data.get("href"):
            self.links.append(data["href"])
        elif tag == "meta":
            self.meta.append(data)
        elif tag == "link":
            rel = data.get("rel", "").split()
            if "canonical" in rel:
                self.canonicals.append(data.get("href", ""))
            if "icon" in rel:
                self.icons.append(data.get("href", ""))
        elif tag == "title":
            self.title_count += 1
            self._in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "img":
            self.images.append(data)
        elif tag == "script" and data.get("type") == "application/ld+json":
            self._in_schema = True
            self._schema_buffer = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_schema:
            self.schema_blocks.append("".join(self._schema_buffer))
            self._in_schema = False

    def handle_data(self, data: str) -> None:
        if self._in_schema:
            self._schema_buffer.append(data)


def output_for_url(url: str) -> Path:
    if url == "/":
        return PUBLIC / "index.html"
    if url.endswith(".html"):
        return PUBLIC / url.lstrip("/")
    return PUBLIC / url.lstrip("/") / "index.html"


def media_public_url(media: dict[str, str]) -> str:
    output = Path(media["output_file"])
    if not output.parts or output.parts[0] != "public":
        return ""
    return "/" + Path(*output.parts[1:]).as_posix()


def absolute_media_url(media: dict[str, str]) -> str:
    return CONFIG["base_url"] + media_public_url(media)


def webp_dimensions(path: Path) -> tuple[int, int] | None:
    data = path.read_bytes()
    if len(data) < 20 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        return None
    offset = 12
    while offset + 8 <= len(data):
        chunk_type = data[offset:offset + 4]
        size = int.from_bytes(data[offset + 4:offset + 8], "little")
        chunk = data[offset + 8:offset + 8 + size]
        if chunk_type == b"VP8X" and len(chunk) >= 10:
            return (
                int.from_bytes(chunk[4:7], "little") + 1,
                int.from_bytes(chunk[7:10], "little") + 1,
            )
        if chunk_type == b"VP8 " and len(chunk) >= 10 and chunk[3:6] == b"\x9d\x01\x2a":
            return (
                int.from_bytes(chunk[6:8], "little") & 0x3FFF,
                int.from_bytes(chunk[8:10], "little") & 0x3FFF,
            )
        if chunk_type == b"VP8L" and len(chunk) >= 5 and chunk[0] == 0x2F:
            bits = int.from_bytes(chunk[1:5], "little")
            return ((bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1)
        offset += 8 + size + (size % 2)
    return None


def png_dimensions(path: Path) -> tuple[int, int] | None:
    data = path.read_bytes()[:24]
    if len(data) != 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        return None
    return (int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big"))


def media_dimensions(path: Path, media_format: str) -> tuple[int, int] | None:
    if media_format == "webp":
        return webp_dimensions(path)
    if media_format == "png":
        return png_dimensions(path)
    return None


def resolve_internal(href: str) -> Path | None:
    if href.startswith(("mailto:", "tel:", "#")):
        return None
    parsed = urlparse(href)
    if parsed.scheme in ("http", "https"):
        if parsed.netloc != CONFIG["domain"]:
            return None
        path = parsed.path
    elif parsed.scheme:
        return None
    else:
        path = parsed.path
    if not path.startswith("/"):
        return None
    return output_for_url(path)


def collect_source_refs(value: object) -> set[int]:
    refs: set[int] = set()
    if isinstance(value, dict):
        refs.update(int(source_id) for source_id in value.get("sources", []))
        for child in value.values():
            refs.update(collect_source_refs(child))
    elif isinstance(value, list):
        for child in value:
            refs.update(collect_source_refs(child))
    return refs


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []
    checks: list[dict[str, str]] = []
    with EDITORIAL_REVIEW_PATH.open(newline="", encoding="utf-8") as handle:
        editorial_candidates = {row["url"]: row for row in csv.DictReader(handle)}
    with CLINICAL_REVIEW_PATH.open(newline="", encoding="utf-8") as handle:
        clinical_candidates = {row["url"]: row for row in csv.DictReader(handle)}
    review_candidates = {**editorial_candidates, **clinical_candidates}
    approved_review_urls: set[str] = set()
    for candidate in review_candidates.values():
        if candidate["status"] not in {"pending", "approved"}:
            failures.append(f"{candidate['url']}: review candidate has an unsupported status")
            continue
        source_path = ROOT / candidate["source_file"]
        current_hash = hashlib.sha256(source_path.read_bytes()).hexdigest() if source_path.is_file() else ""
        if current_hash != candidate["source_sha256"]:
            failures.append(f"{candidate['url']}: review candidate hash does not match the current source")
        if candidate["status"] == "approved":
            approved_review_urls.add(candidate["url"])
            if not candidate.get("approved_date"):
                failures.append(f"{candidate['url']}: approved review record has no approval date")
            evidence = ROOT / candidate.get("approval_evidence", "")
            if not evidence.is_file():
                failures.append(f"{candidate['url']}: approval evidence file is missing")
        elif candidate.get("approved_date") or candidate.get("approval_evidence"):
            failures.append(f"{candidate['url']}: pending review record contains approval evidence")
    with (ROOT / "data" / "media-manifest.csv").open(newline="", encoding="utf-8") as handle:
        media = list(csv.DictReader(handle))
    approved_media_by_url = {
        row["page_url"]: row
        for row in media
        if row["status"] == "approved" and row["role"] in {"article-hero", "hub-hero"}
    }

    if not PUBLIC.exists():
        failures.append("Generated public directory is missing; run the build first.")
    manifest_path = PUBLIC / "build-manifest.json"
    if not manifest_path.exists():
        failures.append("Generated build manifest is missing.")
        manifest = []
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    forbidden = [
        (re.compile(r"mybettacare\.com", re.I), "legacy MyBettaCare.com identity"),
        (re.compile(r"\bburlington\b", re.I), "unverified Burlington office claim"),
        (re.compile(r"(?:/workspace/|file://|localhost:)", re.I), "local machine path or host"),
        (re.compile(r"\b(?:TODO|PLACEHOLDER)\b", re.I), "placeholder marker"),
        (re.compile(r"\[(?:274|307|523|624|625|678)\]"), "unresolved legacy citation token"),
        (re.compile(r"\b(?:2\s+to\s+3|3\s+to\s+5|10\s+to\s+14)\s+days\b", re.I), "unsupported survival timeline"),
        (re.compile(r"fatal intestinal blockages|powerful natural laxative|zero risk|9\.8/10|8\.5/10", re.I), "unsafe or invented care claim"),
        (re.compile(r"\b2\s+to\s+4\s+hours\b|female betta fish typically live longer|almost entirely immune", re.I), "unsupported lifespan or morphology claim"),
        (re.compile(r"100% of (?:its )?aggression|adult cherry shrimp.*safe from bettas|do not possess the cognitive neural structures", re.I), "unsupported compatibility claim"),
        (re.compile(r"remain(?:s)? (?:unpublished|ungenerated)|clinical review pending|not yet approved for publication", re.I), "stale prepublication wording"),
        (re.compile(r"Evidence update:\s+[A-Z][a-z]+\s+\d{4}", re.I), "internal evidence-update note"),
    ]

    for item in manifest:
        html_path = ROOT / item["output"]
        if not html_path.exists():
            failures.append(f"Manifest output missing: {item['output']}")
            continue
        body = html_path.read_text(encoding="utf-8")
        source_page = json.loads((ROOT / item["source"]).read_text(encoding="utf-8"))
        parser = PageParser()
        parser.feed(body)
        label = item["url"]
        if parser.title_count != 1:
            failures.append(f"{label}: expected one title, found {parser.title_count}")
        if parser.h1_count != 1:
            failures.append(f"{label}: expected one H1, found {parser.h1_count}")
        descriptions = [meta.get("content", "") for meta in parser.meta if meta.get("name", "").lower() == "description"]
        if len(descriptions) != 1 or not descriptions[0].strip():
            failures.append(f"{label}: missing or duplicate meta description")
        robots = [meta.get("content", "") for meta in parser.meta if meta.get("name", "").lower() == "robots"]
        if CONFIG["sitewide_noindex"] and robots != ["noindex, nofollow"]:
            failures.append(f"{label}: preview page is not noindex, nofollow")
        if len(parser.canonicals) != 1 or not parser.canonicals[0].startswith(CONFIG["base_url"] + "/"):
            failures.append(f"{label}: canonical is missing, duplicate or uses the wrong domain")
        if parser.icons != [CONFIG["favicon_path"]]:
            failures.append(f"{label}: favicon link is missing, duplicated or uses the wrong asset")
        logo_images = [image for image in parser.images if image.get("src") == CONFIG["logo_path"]]
        if len(logo_images) != 2 or any(image.get("alt") != "" for image in logo_images):
            failures.append(f"{label}: header/footer logo contract is not satisfied")
        if len(parser.schema_blocks) != 1:
            failures.append(f"{label}: expected one JSON-LD block")
        else:
            try:
                schema = json.loads(parser.schema_blocks[0])
                serialized = json.dumps(schema)
                if CONFIG["base_url"] not in serialized:
                    failures.append(f"{label}: schema does not reference the canonical domain")
                if label == "/" and CONFIG["base_url"] + CONFIG["logo_path"] not in serialized:
                    failures.append(f"{label}: Organization schema does not reference the approved logo")
                if re.search(r"PostalAddress|LocalBusiness", serialized):
                    failures.append(f"{label}: unverified location schema is present")
                if source_page.get("person_id"):
                    if '"@type": "ProfilePage"' not in serialized or '"@type": "Person"' not in serialized:
                        failures.append(f"{label}: profile page is missing ProfilePage or Person schema")
                if source_page.get("page_type") == "article":
                    graph = schema.get("@graph", [])
                    article_nodes = [node for node in graph if node.get("@type") == "Article"]
                    faq_nodes = [node for node in graph if node.get("@type") == "FAQPage"]
                    if len(article_nodes) != 1:
                        failures.append(f"{label}: expected one Article schema node")
                    else:
                        article = article_nodes[0]
                        if not article.get("author") or not article.get("editor"):
                            failures.append(f"{label}: Article schema is missing author or editor")
                        if not article.get("citation"):
                            failures.append(f"{label}: Article schema has no source citations")
                    visible_faq = [
                        item
                        for section in source_page.get("sections", []) if section.get("type") == "faq"
                        for item in section.get("items", [])
                    ]
                    if visible_faq:
                        if len(faq_nodes) != 1:
                            failures.append(f"{label}: visible FAQ is missing one FAQPage schema node")
                        else:
                            schema_questions = [item.get("name") for item in faq_nodes[0].get("mainEntity", [])]
                            visible_questions = [item["question"] for item in visible_faq]
                            if schema_questions != visible_questions:
                                failures.append(f"{label}: FAQ schema does not match the visible questions")
                    source_items = [
                        item
                        for section in source_page.get("sections", []) if section.get("type") == "sources"
                        for item in section.get("items", [])
                    ]
                    source_ids = [int(item["id"]) for item in source_items]
                    if len(source_ids) != len(set(source_ids)):
                        failures.append(f"{label}: duplicate source identifiers")
                    missing_refs = sorted(collect_source_refs(source_page) - set(source_ids))
                    if missing_refs:
                        failures.append(f"{label}: citation references missing source entries {missing_refs}")
            except json.JSONDecodeError as error:
                failures.append(f"{label}: invalid JSON-LD ({error})")
        for field in ("author_id", "reviewer_id", "clinical_reviewer_id"):
            person_id = source_page.get(field)
            if not person_id:
                continue
            if person_id not in PEOPLE:
                failures.append(f"{label}: unknown editorial person {person_id}")
                continue
            person = PEOPLE[person_id]
            expected_credit = f'{person["role_label"]} {person["name"]}'
            visible_text = re.sub(r"<[^>]+>", " ", body)
            visible_text = html_unescape(re.sub(r"\s+", " ", visible_text))
            if expected_credit not in visible_text:
                failures.append(f"{label}: missing editorial credit '{expected_credit}'")
            if f'href="{person["profile_url"]}"' not in body:
                failures.append(f"{label}: editorial credit does not link to {person['profile_url']}")
            if field != "author_id" and f'href="{person["profile_url"]}" rel="author"' in body:
                failures.append(f"{label}: reviewer link is incorrectly marked as the page author")
        for pattern, name in forbidden:
            if pattern.search(body):
                failures.append(f"{label}: contains {name}")
        approved_media = approved_media_by_url.get(label)
        if approved_media:
            expected_src = media_public_url(approved_media)
            matching_images = [image for image in parser.images if image.get("src") == expected_src]
            if len(matching_images) != 1:
                failures.append(f"{label}: approved hero image is missing or duplicated")
            else:
                rendered_image = matching_images[0]
                if rendered_image.get("alt") != approved_media["alt"]:
                    failures.append(f"{label}: rendered hero alt text differs from the media manifest")
                if rendered_image.get("width") != approved_media["width"] or rendered_image.get("height") != approved_media["height"]:
                    failures.append(f"{label}: rendered hero dimensions differ from the media manifest")
            schema_text = parser.schema_blocks[0] if parser.schema_blocks else ""
            if '"@type": "ImageObject"' not in schema_text or absolute_media_url(approved_media) not in schema_text:
                failures.append(f"{label}: approved hero is missing ImageObject schema")
        for href in parser.links:
            target = resolve_internal(href)
            if target is not None and not target.exists():
                failures.append(f"{label}: broken internal link {href}")

    with (ROOT / "data" / "page-registry.csv").open(newline="", encoding="utf-8") as handle:
        registry = list(csv.DictReader(handle))
    with (ROOT / "data" / "source-register.csv").open(newline="", encoding="utf-8") as handle:
        source_register_urls = {row["source_file"] for row in csv.DictReader(handle)}
    source_pages = {
        page["url"]: page
        for source in (ROOT / "content" / "pages").glob("*.json")
        for page in [json.loads(source.read_text(encoding="utf-8"))]
    }
    source_urls = set(source_pages)
    generated_source_urls = {
        row["url"] for row in registry
        if row["source_file"].endswith(".json")
        and row["status"] != "planned-research"
        and not row["status"].startswith("planned-")
    }
    registry_json_urls = {
        row["url"] for row in registry
        if row["source_file"].endswith(".json") and row["status"] != "planned-research"
    }
    if source_urls != registry_json_urls:
        failures.append(f"Source/registry URL mismatch: sources={sorted(source_urls)} registry={sorted(registry_json_urls)}")
    manifest_urls = {item["url"] for item in manifest}
    if manifest_urls != generated_source_urls:
        failures.append(
            f"Source/output drift: generated={sorted(manifest_urls)} expected={sorted(generated_source_urls)}"
        )

    expected_authority_expansion = {
        "/anatomy/betta-fish-sleep/",
        "/anatomy/swim-bladder-treatment/",
        "/aquascaping/fin-safe-plants/",
        "/behavior/flaring-triggers/",
        "/behavior/hearing-music/",
        "/behavior/unhappy-betta/",
        "/biology-genetics/color-change/",
        "/biology-genetics/colors/",
        "/biology-genetics/giant-betta/",
        "/biology-genetics/plakat-betta/",
        "/biology-genetics/species/",
        "/breeding/gender-identification/",
        "/breeding/pairing-fry-care/",
        "/care/heaters-calibration/",
        "/care/indian-almond-leaves/",
        "/care/tank-setup/",
        "/diseases/columnaris-treatment/",
        "/diseases/dropsy-treatment/",
        "/diseases/velvet-treatment/",
        "/economics/betta-fish-price/",
        "/maintenance/water-change/",
        "/morphology/growth-rate-size/",
        "/origins/wild-habitats/",
        "/sensory/light-requirements/",
    }
    authority_expansion = [row for row in registry if row["url"] in expected_authority_expansion]
    if {row["url"] for row in authority_expansion} != expected_authority_expansion:
        failures.append("Authority expansion does not match the owner-approved 24-article set")
    planned_research = [row for row in authority_expansion if row["status"] == "planned-research"]
    planned_editorial_review = [
        row for row in authority_expansion if row["status"] == "planned-editorial-review"
    ]
    planned_authority_clinical_review = [
        row for row in authority_expansion if row["status"] == "planned-clinical-review"
    ]
    editorial_review_scope = [
        row for row in authority_expansion if row["url"] in editorial_candidates
    ]
    unexpected_authority_status = [
        row["url"] for row in authority_expansion
        if row["status"] not in {"approved", "planned-research", "planned-editorial-review", "planned-clinical-review"}
    ]
    if unexpected_authority_status:
        failures.append(
            "Authority-expansion URLs have unsupported workflow status: "
            + ", ".join(unexpected_authority_status)
        )
    registered_urls = {row["url"] for row in registry}
    for row in authority_expansion:
        if not row["source_file"].startswith("content/pages/") or not row["source_file"].endswith(".json"):
            failures.append(f"{row['url']}: authority article is missing an explicit source mapping")
        if not row["output_file"].startswith("public/"):
            failures.append(f"{row['url']}: authority article is missing an explicit output mapping")
        if row["parent_hub"] not in registered_urls:
            failures.append(f"{row['url']}: authority article parent hub is not registered")
        if not row["author"] or not row["reviewer"]:
            failures.append(f"{row['url']}: authority article is missing editorial ownership")
        if row["status"].startswith("planned-") and output_for_url(row["url"]).exists():
            failures.append(f"{row['url']}: blocked authority article leaked into generated output")
    authority_queries = [row["primary_query"].strip().lower() for row in authority_expansion]
    if len(authority_queries) != len(set(authority_queries)):
        failures.append("Authority expansion contains duplicate primary-query ownership")
    for row in planned_research:
        if (ROOT / row["source_file"]).exists():
            failures.append(f"{row['url']}: planned-research source exists and must be audited before promotion")
    for row in editorial_review_scope:
        page = source_pages.get(row["url"])
        if not page:
            failures.append(f"{row['url']}: editorial-review article has no permanent JSON source")
            continue
        if page.get("status") != "planned-editorial-review" or page.get("indexable"):
            failures.append(f"{row['url']}: editorial-review source must be planned and non-indexable")
        if page.get("author_id") != "farrukh-abdullah" or page.get("reviewer_id") != "kate-barrington":
            failures.append(f"{row['url']}: editorial-review source has incorrect ownership")
        source_sections = [section for section in page.get("sections", []) if section.get("type") == "sources"]
        if not source_sections or not source_sections[0].get("items"):
            failures.append(f"{row['url']}: editorial-review source has no references")
            continue
        source_ids = {int(item["id"]) for item in source_sections[0]["items"]}
        unregistered_sources = sorted(
            item["url"] for item in source_sections[0]["items"]
            if item["url"] not in source_register_urls
        )
        if unregistered_sources:
            failures.append(f"{row['url']}: sources are missing from the source register: {unregistered_sources}")
        missing_refs = sorted(collect_source_refs(page) - source_ids)
        if missing_refs:
            failures.append(f"{row['url']}: editorial-review references missing entries {missing_refs}")
        serialized_source = json.dumps(page)
        unsafe_care_patterns = (
            r"exactly\s+1\s+to\s+2\s+medium-sized.*leaves",
            r"all\s+betta\s+fish\s+need\s+a\s+heater\s+to\s+survive",
            r"metabolic\s+shutdown|immune\s+collapse|toxic\s+organic\s+blockages",
            r"boil.*exactly\s+2\s+minutes",
            r"using\s+a\s+mirror\s+for\s+exactly\s+5\s+minutes\s+per\s+day\s+is\s+healthy",
            r"structured\s+workout\s+encourages\s+a\s+healthy\s+digestive\s+tract",
            r"water\s+conducts\s+sound\s+waves\s+4\.3\s+times\s+faster.*magnifying",
            r"music\s+waves.*over-stimulate.*lateral\s+line",
            r"plakat\s+bettas\s+display\s+higher\s+aggression\s+levels",
            r"frequently\s+outliving\s+long-finned\s+varieties",
            r"add\s+up\s+to\s+0\.75\s+inches.*every\s+30\s+days",
            r"daily\s+water\s+changes.*growth-inhibiting\s+pheromones",
            r"giant\s+bettas\s+have\s+a\s+shorter\s+lifespan\s+of\s+exactly\s+2\s+to\s+3\s+years",
            r"giants\s+achieve\s+true\s+4-inch\s+scale",
            r"diagnose\s+(?:an\s+)?unhappy\s+betta.*(?:exactly\s+)?3\s+primary",
            r"bottom.*(?:swim\s+bladder\s+inflammation|nitrite\s+poisoning|cold\s+shock)",
            r"happy.*(?:vibrant|active).*(?:bubble\s+nests?)",
            r"exactly\s+8\s+to\s+12\s+hours.*(?:light|dark)",
            r"suspended\s+animation|complete\s+loss\s+of\s+motion",
            r"require.*(?:leaf\s+hammock|betta\s+bed).*(?:1\s+to\s+2\s+inches)",
            r"prevent\s+severe\s+psychological\s+depression",
            r"chronic\s+rod/cone\s+fatigue|severe\s+stress,\s+immune\s+suppression",
            r"exactly\s+8\s+to\s+12\s+hours\s+of\s+light.*12\s+to\s+16\s+hours",
            r"motionless\s+suspended\s+sleep",
            r"live\s+plants\s+absorb\s+toxic\s+ammonia,\s+nitrites?,\s+and\s+nitrates?\s+continuously",
            r"rigid\s+molded\s+plastic.*(?:puncture|tear).*betta\s+fins",
            r"zero\s+specialized\s+soil\s+substrates",
            r"outcompeting\s+nuisance\s+algae\s+and\s+stabilizing\s+water\s+chemistry",
            r"(?:4\s+to\s+6\s+weeks|4-6\s+weeks).*2\s*ppm\s+ammonia",
            r"nitrite\s+(?:levels?\s+)?spike.*10\s+to\s+14\s+days",
            r"50%\s+water\s+change.*nitrate.*below\s+20\s*ppm",
            r"50-watt\s+adjustable\s+heater",
            r"under\s+5\s+gallons?.*lethal\s+metabolic\s+shock",
            r"only\s+physical\s+water\s+removal\s+controls\s+nitrate",
            r"weekly\s+(?:10\s+to\s+20|10-20)%.*(?:zero|0)\s+ammonia",
            r"complete\s+water\s+(?:change|swap).*nitrifying\s+bacteria",
            r"all\s+(?:quality\s+)?dechlorinators?.*heavy\s+metals",
            r"tannins?.*naturally\s+lower\s+pH.*sooth",
            r"over\s+150\s+species\s+of\s+annual\s+and\s+perennial\s+fish.*Betta\s+genus",
            r"(?:there\s+are\s+)?4\s+major\s+wild\s+Betta\s+species\s+complexes",
            r"wild\s+Bettas?.*survive.*(?:leaping\s+between|resting\s+within\s+wet\s+mud)",
            r"all\s+Betta\s+fish\s+are\s+strictly\s+tropical\s+freshwater",
            r"Betta\s+imbellis.*best\s+wild\s+species\s+for\s+beginners",
            r"cohabits?\s+peacefully\s+with\s+conspecifics",
            r"multiple\s+Betta\s+imbellis.*same.*15-gallon\s+aquarium",
            r"currents?\s+sweep\s+away\s+foam\s+rafts",
            r"mouthbrooders?.*10\s+to\s+14\s+days",
            r"Coccina\s+Complex.*4\.0\s+to\s+5\.5",
            r"rarest\s+Betta\s+fish\s+color\s+is",
            r"(?:3|three)\s+primary\s+biological\s+factors.*color",
            r"most\s+accurate\s+way.*female.*ovipositor",
            r"fins?.*three\s+times\s+their\s+body\s+length",
            r"strictly\s+between\s+80.?F\s+and\s+82.?F",
            r"eggs?\s+hatch\s+within\s+exactly\s+24\s+to\s+36\s+hours",
            r"(?:0\.5|one-half)\s+inch.*(?:per|every)\s+month",
            r"four-inch\s+adult\s+size",
        )
        for pattern in unsafe_care_patterns:
            if re.search(pattern, serialized_source, re.I):
                failures.append(f"{row['url']}: unsupported absolute care instruction remains in source")

    expected_editorial_urls = {row["url"] for row in editorial_review_scope}
    if set(editorial_candidates) != expected_editorial_urls:
        failures.append("Editorial-review candidate register does not match the planned editorial URLs")
    for row in editorial_review_scope:
        candidate = editorial_candidates.get(row["url"])
        if not candidate:
            continue
        source_path = ROOT / row["source_file"]
        current_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
        if candidate["source_file"] != row["source_file"] or candidate["source_sha256"] != current_hash:
            failures.append(f"{row['url']}: editorial-review candidate hash does not match the current source")
        if candidate["editor"] != "Kate Barrington":
            failures.append(f"{row['url']}: editorial-review candidate has the wrong editor")
        if candidate["status"] not in {"pending", "approved"}:
            failures.append(f"{row['url']}: editorial-review candidate has an unsupported status")
        if candidate["status"] == "pending" and candidate["approved_date"]:
            failures.append(f"{row['url']}: pending editorial candidate has an approval date")
        if candidate["status"] == "approved" and not candidate["approved_date"]:
            failures.append(f"{row['url']}: approved editorial candidate has no approval date")
        if candidate["status"] == "approved" and row["status"] != "approved":
            failures.append(f"{row['url']}: approved editorial candidate is not promoted in the registry")
        if candidate["status"] == "pending" and row["status"] == "approved":
            failures.append(f"{row['url']}: registry promotion lacks editorial approval")
    if planned_research or planned_editorial_review or planned_authority_clinical_review:
        authority_media_pending = [
            row["asset_id"] for row in media
            if row["page_url"] in expected_authority_expansion and row["status"] != "approved"
        ]
        authority_media_status = (
            f"{len(authority_media_pending)} authority images remain pending."
            if authority_media_pending
            else "All 24 authority-article hero images are approved."
        )
        warnings.append(
            f"{len(authority_expansion)} owner-selected authority articles remain blocked: "
            f"{len(planned_editorial_review)} await editorial approval, "
            f"{len(planned_authority_clinical_review)} await exact-version clinical approval, and "
            f"{len(planned_research)} await structured-source conversion. {authority_media_status} G05 remains blocked."
        )

    planned_health = [
        row for row in registry
        if row["page_type"] == "article" and row["status"] == "planned-clinical-review"
    ]
    clinical_review_scope = [row for row in registry if row["url"] in clinical_candidates]
    if set(clinical_candidates) != {row["url"] for row in clinical_review_scope}:
        failures.append("Clinical-review candidate register does not match the clinical source scope")
    for row in clinical_review_scope:
        page = source_pages.get(row["url"])
        if not page:
            failures.append(f"{row['url']}: blocked health article has no permanent JSON source")
            continue
        if page.get("status") != "planned-clinical-review" or page.get("indexable"):
            failures.append(f"{row['url']}: blocked health source must be planned-clinical-review and non-indexable")
        if page.get("clinical_reviewer_id") != "robert-martinez":
            failures.append(f"{row['url']}: assigned clinical reviewer is missing from source")
        if page.get("clinical_review_status") != "pending":
            failures.append(f"{row['url']}: clinical review status is not pending")
        source_sections = [section for section in page.get("sections", []) if section.get("type") == "sources"]
        if not source_sections or not source_sections[0].get("items"):
            failures.append(f"{row['url']}: corrected clinical-review source has no references")
            continue
        source_ids = {int(item["id"]) for item in source_sections[0]["items"]}
        unregistered_sources = sorted(
            item["url"] for item in source_sections[0]["items"]
            if item["url"] not in source_register_urls
        )
        if unregistered_sources:
            failures.append(f"{row['url']}: sources are missing from the source register: {unregistered_sources}")
        missing_refs = sorted(collect_source_refs(page) - source_ids)
        if missing_refs:
            failures.append(f"{row['url']}: corrected source references missing entries {missing_refs}")
        serialized_source = json.dumps(page)
        unsafe_dose_patterns = (
            r"250\s*mg\s*per",
            r"1\s*(?:tablespoon|tbsp).*per\s*(?:3|5)\s*gallons?",
            r"0\.15\s*(?:to|-|–)\s*0\.20\s*ppm",
            r"1\s*drop.*per\s*gallon",
            r"raise.*(?:30\s*°?C|86\s*°?F)",
            r"copper.*(?:exactly\s+14\s+days|0\.20\s+to\s+0\.25)",
            r"(?:10-day|10\s+day)\s+light\s+blackout",
            r"lower.*74.?F",
            r"kanamycin.*nitrofurazone.*(?:exactly\s+10|1\s+measure)",
            r"dissolve\s+exactly\s+1\s+tablespoon",
            r"fast(?:ing)?\s+for\s+exactly\s+72\s+hours",
        )
        for pattern in unsafe_dose_patterns:
            if re.search(pattern, serialized_source, re.I):
                failures.append(f"{row['url']}: unsafe universal dose or heat protocol remains in corrected source")
        candidate = clinical_candidates.get(row["url"])
        if not candidate:
            continue
        source_path = ROOT / candidate["source_file"]
        current_hash = hashlib.sha256(source_path.read_bytes()).hexdigest() if source_path.exists() else ""
        if candidate["source_file"] != row["source_file"] or candidate["source_sha256"] != current_hash:
            failures.append(f"{row['url']}: clinical-review candidate hash or source mapping is stale")
        if candidate["clinical_reviewer"] != "Robert Martinez, DVM" or candidate["status"] not in {"pending", "approved"}:
            failures.append(f"{row['url']}: clinical-review candidate assignment or status is incorrect")
        if candidate["status"] == "approved" and row["status"] != "approved":
            failures.append(f"{row['url']}: approved clinical candidate is not promoted in the registry")
        if candidate["status"] == "pending" and row["status"] == "approved":
            failures.append(f"{row['url']}: registry promotion lacks clinical approval")
    leaked_health = [row["url"] for row in planned_health if output_for_url(row["url"]).exists()]
    if leaked_health:
        failures.append(f"Blocked health articles were generated: {', '.join(leaked_health)}")
    if planned_health:
        warnings.append(
            f"{len(planned_health)} disease-treatment articles remain blocked pending documented clinical review by the assigned aquatic veterinarian; G05 remains blocked."
        )

    robots_text = (PUBLIC / "robots.txt").read_text(encoding="utf-8") if (PUBLIC / "robots.txt").exists() else ""
    if CONFIG["sitewide_noindex"] and robots_text != "User-agent: *\nDisallow: /\n":
        failures.append("Preview robots.txt does not disallow all crawling.")
    sitemap_text = (PUBLIC / "sitemap.xml").read_text(encoding="utf-8") if (PUBLIC / "sitemap.xml").exists() else ""
    if CONFIG["sitewide_noindex"] and "<url>" in sitemap_text:
        failures.append("Preview sitemap contains indexable URLs.")

    headers_path = PUBLIC / "_headers"
    if not headers_path.exists():
        failures.append("Cloudflare security-header configuration is missing.")
    else:
        headers_text = headers_path.read_text(encoding="utf-8")
        for required_header in (
            "X-Content-Type-Options: nosniff",
            "Referrer-Policy: strict-origin-when-cross-origin",
            "Permissions-Policy: camera=(), microphone=(), geolocation=()",
            "X-Frame-Options: DENY",
        ):
            if required_header not in headers_text:
                failures.append(f"Cloudflare header configuration is missing: {required_header}")

    contact_source = json.loads((ROOT / "content" / "pages" / "contact.json").read_text(encoding="utf-8"))
    if not CONFIG.get("contact_email"):
        if contact_source.get("status") != "blocked-owner-input" or contact_source.get("indexable"):
            failures.append("Contact page must remain blocked and non-indexable until a real mailbox is verified.")
        warnings.append("Contact email is not supplied; G03 remains blocked.")
    else:
        contact_output = (PUBLIC / "contact" / "index.html").read_text(encoding="utf-8")
        expected_mailto = f'mailto:{CONFIG["contact_email"]}'
        if contact_source.get("status") == "blocked-owner-input" or not contact_source.get("indexable"):
            failures.append("Contact page is still blocked even though an owner-approved mailbox is configured.")
        if expected_mailto not in contact_output:
            failures.append("Configured contact email is not linked from the generated Contact page.")
        if CONFIG.get("contact_email_status") != "permanent":
            warnings.append("The current contact email is owner-approved but temporary; confirm its replacement before production.")
    if not CONFIG.get("publisher_name"):
        warnings.append("Publisher identity is not supplied; G00/G03 remain blocked.")

    editorial_rows = [row for row in registry if row["page_type"] in {"homepage", "hub", "article"}]
    incomplete_editorial_rows = [row["url"] for row in editorial_rows if not row["author"] or not row["reviewer"]]
    if incomplete_editorial_rows:
        failures.append(f"Editorial registry rows lack author or reviewer: {', '.join(incomplete_editorial_rows)}")
    expected_people = {"farrukh-abdullah", "kate-barrington", "robert-martinez"}
    if set(PEOPLE) != expected_people:
        failures.append("Editorial people registry does not match the approved author, editor and clinical-reviewer identities.")

    asset_ids = [row["asset_id"] for row in media]
    if len(asset_ids) != len(set(asset_ids)):
        failures.append("Media manifest contains duplicate asset identifiers")
    output_files = [row["output_file"] for row in media if row["output_file"]]
    if len(output_files) != len(set(output_files)):
        failures.append("Media manifest maps more than one asset to the same output file")
    for row in media:
        if row["status"] != "approved":
            continue
        source_path = ROOT / row["source_file"]
        output_path = ROOT / row["output_file"]
        if not source_path.is_file():
            failures.append(f"{row['asset_id']}: approved media source is missing")
            continue
        if not output_path.is_file():
            failures.append(f"{row['asset_id']}: approved media output is missing after build")
        actual_hash = hashlib.sha256(source_path.read_bytes()).hexdigest()
        if row["checksum"] != actual_hash:
            failures.append(f"{row['asset_id']}: media checksum does not match its permanent source")
        if row["byte_size"] != str(source_path.stat().st_size):
            failures.append(f"{row['asset_id']}: media byte size does not match its permanent source")
        media_format = row["format"].lower()
        dimensions = media_dimensions(source_path, media_format)
        expected_dimensions = (int(row["width"]), int(row["height"]))
        if dimensions != expected_dimensions or media_format not in {"webp", "png"}:
            failures.append(f"{row['asset_id']}: media format or dimensions do not match the manifest")
    missing_media = [row["asset_id"] for row in media if row["status"] != "approved"]
    if missing_media:
        warnings.append(f"{len(missing_media)} required media assets are not approved; G06/G07 remain blocked.")

    incoming_links = {url: 0 for url in manifest_urls}
    for item in manifest:
        parser = PageParser()
        parser.feed((ROOT / item["output"]).read_text(encoding="utf-8"))
        for href in parser.links:
            parsed = urlparse(href)
            target_url = parsed.path
            if parsed.scheme in {"http", "https"} and parsed.netloc != CONFIG["domain"]:
                continue
            if target_url in incoming_links and target_url != item["url"]:
                incoming_links[target_url] += 1
    orphan_urls = sorted(
        url for url, count in incoming_links.items()
        if url not in {"/", "/404.html"} and count == 0
    )
    if orphan_urls:
        failures.append("Generated pages have no incoming internal links: " + ", ".join(orphan_urls))

    checks.extend([
        {"check": "generated-page-contracts", "status": "PASS" if not failures else "FAIL"},
        {"check": "preview-indexing-controls", "status": "PASS" if CONFIG["sitewide_noindex"] and "<url>" not in sitemap_text else "FAIL"},
        {"check": "legacy-identity-and-office-scan", "status": "PASS" if not any("legacy" in failure or "Burlington" in failure for failure in failures) else "FAIL"},
        {"check": "internal-prepublication-copy", "status": "PASS" if not any("prepublication" in failure or "evidence-update" in failure for failure in failures) else "FAIL"},
        {"check": "blocked-health-output", "status": "PASS" if not leaked_health else "FAIL"},
        {"check": "planned-authority-output", "status": "PASS" if not any(output_for_url(row["url"]).exists() for row in authority_expansion if row["status"].startswith("planned-")) else "FAIL"},
        {"check": "editorial-identity-contract", "status": "PASS" if not incomplete_editorial_rows else "FAIL"},
        {"check": "production-launch", "status": "STOP"},
    ])
    report = {
        "foundation_status": "PASS" if not failures else "FAIL",
        "production_status": "STOP",
        "generated_pages": len(manifest),
        "checks": checks,
        "failures": failures,
        "warnings": warnings,
    }
    (PUBLIC / "audit-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    markdown = [
        "# Foundation Audit Report",
        "",
        f"- Foundation status: **{report['foundation_status']}**",
        "- Production status: **STOP**",
        f"- Generated pages: **{len(manifest)}**",
        "",
        "## Automated checks",
        "",
        "| Check | Status |",
        "|---|---|",
    ]
    markdown.extend(f"| {entry['check']} | {entry['status']} |" for entry in checks)
    markdown.extend(["", "## Failures", ""])
    markdown.extend(f"- {failure}" for failure in failures)
    if not failures:
        markdown.append("- None in the generated foundation.")
    markdown.extend(["", "## Open launch blockers", ""])
    markdown.extend(f"- {warning}" for warning in warnings)
    if not warnings:
        markdown.append("- None reported by automated source and build checks; manual preview and production gates remain open.")
    (PUBLIC / "audit-report.md").write_text("\n".join(markdown) + "\n", encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
