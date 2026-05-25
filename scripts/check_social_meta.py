#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path


SITE_URL = "https://raiders0786.github.io/web3-security-resources/"
DEFAULT_IMAGE = SITE_URL + "assets/social/web3-security-resources-og-v2.png"
AI_IMAGE = SITE_URL + "assets/social/ai-era-smart-contract-auditor-og-v1.png"


class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {}

    def handle_starttag(self, tag, attrs):
        if tag != "meta":
            return
        data = dict(attrs)
        key = data.get("property") or data.get("name")
        if key:
            self.meta[key] = data.get("content", "")


def read_meta(path):
    parser = MetaParser()
    parser.feed(Path(path).read_text(encoding="utf-8"))
    return parser.meta


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def check_page(path, expected_image, forbidden_image=None):
    meta = read_meta(path)
    for key in ("og:image", "og:image:secure_url", "twitter:image"):
        require(meta.get(key) == expected_image, f"{path}: {key} is {meta.get(key)!r}")
    require(meta.get("og:image:type") == "image/png", f"{path}: missing png image type")
    require(meta.get("og:image:width") == "1200", f"{path}: missing image width")
    require(meta.get("og:image:height") == "630", f"{path}: missing image height")
    if forbidden_image:
        html = Path(path).read_text(encoding="utf-8")
        require(forbidden_image not in html, f"{path}: contains forbidden image {forbidden_image}")


def check_asset(path):
    data = Path(path).read_bytes()
    require(data.startswith(b"\x89PNG\r\n\x1a\n"), f"{path}: not a PNG")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    require((width, height) == (1200, 630), f"{path}: expected 1200x630, got {width}x{height}")


def main():
    check_page("site/index.html", DEFAULT_IMAGE, forbidden_image=AI_IMAGE)
    check_page("site/roadmaps/ai-era-smart-contract-auditor/index.html", AI_IMAGE)
    check_asset("docs/assets/social/web3-security-resources-og-v2.png")
    check_asset("docs/assets/social/ai-era-smart-contract-auditor-og-v1.png")


if __name__ == "__main__":
    main()
