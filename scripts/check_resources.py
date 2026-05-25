#!/usr/bin/env python3
import re
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
RESOURCE_FILE = DOCS / "data" / "resources.yml"
MAX_VERIFIED_AGE_DAYS = 365
REQUIRED_RESOURCE_FIELDS = {
    "title",
    "url",
    "category",
    "track",
    "level",
    "free_or_paid",
    "last_verified",
    "why_it_matters",
    "status",
    "audience",
    "stage",
    "ecosystem",
    "evidence_type",
    "notes",
}


def fail(message, failures):
    failures.append(message)


def load_resources():
    return yaml.safe_load(RESOURCE_FILE.read_text(encoding="utf-8"))


def check_resources(resources, failures):
    seen_urls = {}
    seen_titles = {}
    today = date.today()
    for idx, item in enumerate(resources):
        label = item.get("title") or f"entry #{idx + 1}"
        missing = sorted(REQUIRED_RESOURCE_FIELDS - set(item))
        if missing:
            fail(f"{label}: missing fields {', '.join(missing)}", failures)
        url = item.get("url", "")
        parsed = urlparse(url)
        if parsed.scheme != "https":
            fail(f"{label}: URL must use https: {url}", failures)
        if url in seen_urls:
            fail(f"{label}: duplicate URL also used by {seen_urls[url]}", failures)
        seen_urls[url] = label
        title_key = label.lower()
        if title_key in seen_titles:
            fail(f"{label}: duplicate title also used by {seen_titles[title_key]}", failures)
        seen_titles[title_key] = label
        verified = item.get("last_verified")
        if not isinstance(verified, date):
            try:
                verified = datetime.strptime(str(verified), "%Y-%m-%d").date()
            except ValueError:
                fail(f"{label}: invalid last_verified {verified!r}", failures)
                continue
        age = (today - verified).days
        if age < 0:
            fail(f"{label}: last_verified is in the future", failures)
        if age > MAX_VERIFIED_AGE_DAYS:
            fail(f"{label}: last_verified is stale by {age - MAX_VERIFIED_AGE_DAYS} days", failures)
        for field in ("audience", "stage", "ecosystem"):
            if not isinstance(item.get(field), list) or not item[field]:
                fail(f"{label}: {field} must be a non-empty list", failures)


def check_markdown_front_matter(failures):
    for path in DOCS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if not text.startswith("---\n"):
            fail(f"{rel}: missing front matter", failures)
            continue
        end = text.find("\n---", 4)
        if end == -1:
            fail(f"{rel}: malformed front matter", failures)
            continue
        meta = yaml.safe_load(text[4:end]) or {}
        if not meta.get("title"):
            fail(f"{rel}: missing title front matter", failures)
        if not meta.get("description"):
            fail(f"{rel}: missing description front matter", failures)


def check_resource_markdown_drift(resources):
    warnings = []
    known_urls = {item["url"] for item in resources}
    ignored_domains = {
        "www.digibastion.com",
        "vantage.digibastion.com",
        "x.com",
        "t.me",
    }
    link_pattern = re.compile(r"\[[^\]]+\]\((https://[^)]+)\)")
    for path in (DOCS / "resources").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for url in link_pattern.findall(text):
            clean = url.split("#", 1)[0].rstrip("/")
            candidates = {url, clean, clean + "/"}
            if any(candidate in known_urls for candidate in candidates):
                continue
            if urlparse(url).netloc in ignored_domains:
                continue
            warnings.append(f"{path.relative_to(ROOT)}: Markdown link not present in resources.yml: {url}")
    return warnings


def main():
    failures = []
    resources = load_resources()
    if not isinstance(resources, list):
        raise SystemExit("resources.yml must contain a YAML list")
    check_resources(resources, failures)
    check_markdown_front_matter(failures)
    warnings = check_resource_markdown_drift(resources)
    if failures:
        print("Resource validation failed:")
        for message in failures:
            print(f"- {message}")
        raise SystemExit(1)
    print(f"Resource validation passed: {len(resources)} entries checked.")
    if warnings:
        print(f"Resource drift warnings: {len(warnings)} Markdown links are not catalogued.")
        for message in warnings[:20]:
            print(f"- {message}")
        if len(warnings) > 20:
            print(f"- ... {len(warnings) - 20} more")


if __name__ == "__main__":
    main()
