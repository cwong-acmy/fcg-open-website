# -*- coding: utf-8 -*-
"""
Localisation for the Direction B portal pages.

Design constraint: **only copy changes between locales, never layout.** So the
builder generates each page once from `pages_content.py`, then swaps text nodes
and a short list of translatable attributes. Markup, classes, tokens and CSS are
byte-identical across locales by construction — there is nothing to keep in sync.

`extract_strings(html)` returns every translatable string on a page.
`translate(html, table)` swaps them. A string with no entry in the table is
reported, so nothing is silently left in English.

Simplified is written for mainland readers; Traditional is written for
Taiwan/Hong Kong readers and uses that region's IT vocabulary rather than a
glyph-for-glyph conversion of the Simplified text — 介面 not 接口, 資料 not 數據,
伺服器 not 服務器, 軟體 not 軟件, 預設 not 默認, 快取 not 緩存, 網路 not 網絡.
"""

from html.parser import HTMLParser

# Tags whose text is code, data or a proper noun — never translated.
SKIP_TEXT_IN = {"script", "style", "code", "pre"}

# Void elements have no end tag. Pushing them onto the open-element stack and
# never popping them corrupts every ancestor test that follows — the hero's
# <br> left h1 on the stack permanently, so the footer heading also looked like
# it was inside a heading.
VOID = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}


def _push(stack, tag):
    if tag not in VOID:
        stack.append(tag)


def _pop(stack, tag):
    """Unwind to the matching tag, tolerating unclosed elements."""
    if tag in VOID or tag not in stack:
        return
    while stack:
        if stack.pop() == tag:
            return


# Headings whose text nodes may carry a "h:" prefixed override.
HEADING_TAGS = {"h1", "h2", "h3"}

# Attributes that carry user-visible copy.
TRANSLATABLE_ATTRS = {"placeholder", "aria-label", "title", "alt", "content"}

# Strings that are the same in every locale (product names, codes, versions,
# endpoint paths, language button labels). Never reported as missing.
INVARIANT = {
    "FCG", "G-Link", "F-Link", "TMC", "TMC API", "G-Link Hotel", "F-Link Flight",
    "G-Link Hotel API", "F-Link Flight API", "ENG", "简体", "繁體", "EN", "中文",
    "Go", "Java", "Python", "Node.js", "Node.js (in progress)", "REST", "API",
    "SDK", "MCP", "AI", "Codex", "Cursor", "Claude Code", "Kiro", "Gemini CLI",
    "POST", "GET", "SKILL.md", "USD", "CNY",
    "·", "/", "*", "→", "—", "AppKey", "AppSecret", "Webhooks", "BSP", "OTA",
    "100 req / min", "v1.0.0", "v2.0.0", "v2.5.3", "Bearer",
    # API field and type names shown as data, not prose
    "code", "data", "message", "language", "string", "array<object>",
    "request_id", "trace_id", "downstream_request_id", "HTTP / JSON",
    # partner lockups and stat suffixes render as-is in every locale
    "PST", "CONNEXUS TRAVEL", "SABRE", "HILTON", "AMADEUS", "华住", "IHG",
    "MARRIOTT", "M+", "TMC Java SDK", "TMC Python SDK", "TMC API Skills",
    "SKILL.md structure", "application/json", "REST API", "MCP server",
    "Model Context Protocol",
    # fragments left when an HTML entity splits a text node:
    # {lang} -> "lang", array&lt;object&gt; -> "array" / "object"
    "lang", "array", "object",
}


# HTMLParser lowercases attribute names, which silently breaks case-sensitive
# SVG attributes — viewBox becomes viewbox and the wordmark stops rendering.
# Only the ones these documents actually use need restoring, and the lossless
# assertion in build-pages.py fails loudly if a new one ever appears.
SVG_CASE = {
    "viewbox": "viewBox",
    "preserveaspectratio": "preserveAspectRatio",
    "gradienttransform": "gradientTransform",
    "clippathunits": "clipPathUnits",
    "patterncontentunits": "patternContentUnits",
    "stddeviation": "stdDeviation",
    "attributename": "attributeName",
    "repeatcount": "repeatCount",
    "pathlength": "pathLength",
    "spreadmethod": "spreadMethod",
    "startoffset": "startOffset",
    "textlength": "textLength",
    "lengthadjust": "lengthAdjust",
    "markerwidth": "markerWidth",
    "markerheight": "markerHeight",
    "refx": "refX",
    "refy": "refY",
}


def norm(s):
    """Collapse internal whitespace so a table key is one clean line."""
    return " ".join((s or "").split())


class _Extract(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.found = []

    def handle_starttag(self, tag, attrs):
        _push(self.stack, tag)
        for name, value in attrs:
            if name in TRANSLATABLE_ATTRS and norm(value or ""):
                self.found.append(norm(value))

    def handle_startendtag(self, tag, attrs):
        for name, value in attrs:
            if name in TRANSLATABLE_ATTRS and norm(value or ""):
                self.found.append(norm(value))

    def handle_endtag(self, tag):
        _pop(self.stack, tag)

    def handle_data(self, data):
        if any(t in SKIP_TEXT_IN for t in self.stack):
            return
        text = norm(data)
        if text:
            self.found.append(text)


import re

# Shapes that are never copy: endpoint paths, error codes, install commands,
# the viewport meta value, bare identifiers.
INVARIANT_RE = [
    re.compile(r"^/"),                        # /openapi/v1/glink/...
    re.compile(r"^[A-Z]{2,4}\d{3}$"),         # MCP001, SDK002
    re.compile(r"^width=device-width"),       # viewport meta
    re.compile(r"^(npx|pip|go get|mvn) "),    # install commands
    re.compile(r"^[a-z]+([A-Z][a-z]+)+$"),    # camelCase identifiers
    re.compile(r"^\d+(\.\d+)*\s*(px|ch|%)?$"),
]


def _translatable(s):
    """Skip punctuation, numbers, identifiers, paths and known invariants."""
    if s in INVARIANT:
        return False
    if not any(ch.isalpha() for ch in s):
        return False
    if any(rx.match(s) for rx in INVARIANT_RE):
        return False
    return True


def extract_strings(html):
    p = _Extract()
    p.feed(html)
    seen, out = set(), []
    for s in p.found:
        if s in seen or not _translatable(s):
            continue
        seen.add(s)
        out.append(s)
    return out


class _Translate(HTMLParser):
    """Rebuilds the document, swapping text nodes and translatable attributes."""

    def __init__(self, table, missing):
        super().__init__(convert_charrefs=False)
        self.table = table
        self.missing = missing
        self.stack = []
        self.out = []

    def _attrs(self, attrs):
        parts = []
        for name, value in attrs:
            name = SVG_CASE.get(name, name)
            if value is None:
                parts.append(f" {name}")
                continue
            v = value
            if name in TRANSLATABLE_ATTRS and norm(value):
                v = self._swap(value, False)
            parts.append(f' {name}="{v}"')
        return "".join(parts)

    def _swap(self, raw, in_heading=False):
        key = norm(raw)
        if not key:
            return raw
        if in_heading and ("h:" + key) in self.table:
            key = "h:" + key
        if key in self.table:
            # keep the original leading/trailing whitespace so inline runs like
            # "text <code>x</code> more text" keep their spacing
            lead = raw[: len(raw) - len(raw.lstrip())]
            tail = raw[len(raw.rstrip()) :]
            return lead + self.table[key] + tail
        if _translatable(key):
            self.missing.add(key)
        return raw

    def handle_starttag(self, tag, attrs):
        _push(self.stack, tag)
        self.out.append(f"<{tag}{self._attrs(attrs)}>")

    def handle_startendtag(self, tag, attrs):
        self.out.append(f"<{tag}{self._attrs(attrs)}>")

    def handle_endtag(self, tag):
        _pop(self.stack, tag)
        self.out.append(f"</{tag}>")

    def handle_data(self, data):
        if any(t in SKIP_TEXT_IN for t in self.stack):
            self.out.append(data)
            return
        # A fragment inside a heading can need a different translation from the
        # same word used as a label: "Platform" is the second line of the hero
        # h1 and also a footer column heading. A "h:" prefixed entry wins inside
        # h1/h2/h3, so neither has to be reworded.
        in_heading = any(t in HEADING_TAGS for t in self.stack)
        self.out.append(self._swap(data, in_heading) if data.strip() else data)

    def handle_comment(self, data):
        self.out.append(f"<!--{data}-->")

    def handle_decl(self, decl):
        self.out.append(f"<!{decl}>")

    def handle_entityref(self, name):
        self.out.append(f"&{name};")

    def handle_charref(self, name):
        self.out.append(f"&#{name};")

    def unknown_decl(self, data):
        self.out.append(f"<![{data}]>")


def translate(html, table):
    """Return (translated_html, missing_strings)."""
    missing = set()
    p = _Translate(table, missing)
    p.feed(html)
    p.close()
    return "".join(p.out), missing


# ---------------------------------------------------------------- collisions
# The table is keyed on the exact string, so one string gets one translation
# everywhere. That is fine for a word used consistently, and wrong when a
# headline fragment happens to match a label: "Platform" as the second half of
# "FCG Developer<br>Platform" collided with the footer column heading and
# translated the hero to "FCG平台". Flag any string that appears both inside a
# heading and outside one.

class _Contexts(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.seen = {}

    def handle_starttag(self, tag, attrs):
        _push(self.stack, tag)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        _pop(self.stack, tag)

    def handle_data(self, data):
        if any(t in SKIP_TEXT_IN for t in self.stack):
            return
        key = norm(data)
        if not key or not _translatable(key):
            return
        in_heading = any(t in HEADING_TAGS for t in self.stack)
        self.seen.setdefault(key, set()).add("heading" if in_heading else "body")


def find_context_collisions(html, table=None):
    """Strings living in both a heading and ordinary copy on the same page.
    A key with a "h:" override is already resolved, so it is not a collision."""
    p = _Contexts()
    p.feed(html)
    overridden = {k[2:] for k in (table or {}) if k.startswith("h:")}
    return {
        k for k, ctx in p.seen.items() if len(ctx) > 1 and k not in overridden
    }
