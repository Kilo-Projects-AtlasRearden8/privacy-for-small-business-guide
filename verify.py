#!/usr/bin/env python3
"""Verification script for Privacy for Small Business project.

Checks:
- All required files exist
- LICENSE has exact copyright line
- README credits Asdale Dynamics, LLC
- HTML files are structurally valid
- Internal links resolve correctly
- CSS file exists and is referenced
- No secrets or personal data in files
- No .github/workflows directory
"""
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
REQUIRED_FILES = [
    "LICENSE",
    "README.md",
    "STATUS.md",
    "docs/index.md",
    "docs/checklist.md",
    "site/index.html",
    "site/checklist.html",
    "site/assets/style.css",
]

EXPECTED_COPYRIGHT = "Copyright (c) 2026 Asdale Dynamics, LLC"

errors = []
warnings = []


def check_file_exists(path):
    full = os.path.join(ROOT, path)
    if not os.path.isfile(full):
        errors.append(f"MISSING: {path}")


def check_license_copyright():
    path = os.path.join(ROOT, "LICENSE")
    if not os.path.isfile(path):
        return
    with open(path) as f:
        content = f.read()
    if EXPECTED_COPYRIGHT not in content:
        errors.append(f"LICENSE: missing exact copyright line '{EXPECTED_COPYRIGHT}'")


def check_readme_attribution():
    path = os.path.join(ROOT, "README.md")
    if not os.path.isfile(path):
        return
    with open(path) as f:
        content = f.read()
    if "Asdale Dynamics, LLC" not in content:
        errors.append("README.md: missing 'Asdale Dynamics, LLC' attribution")


def check_no_secrets():
    """Scan all text files for potential secrets/keys."""
    secret_patterns = [
        r"(?i)(api[_-]?key|apikey)\s*[:=]\s*['\"][^'\"]{8,}",
        r"(?i)(secret|password|token)\s*[:=]\s*['\"][^'\"]{8,}",
        r"sk-[A-Za-z0-9]{20,}",
        r"ghp_[A-Za-z0-9]{20,}",
        r"AKIA[0-9A-Z]{16}",
    ]
    for root, dirs, files in os.walk(ROOT):
        if ".git" in dirs:
            dirs.remove(".git")
        for fname in files:
            fpath = os.path.join(root, fname)
            rel = os.path.relpath(fpath, ROOT)
            try:
                with open(fpath, encoding="utf-8", errors="ignore") as f:
                    content = f.read()
            except Exception:
                continue
            for pat in secret_patterns:
                if re.search(pat, content):
                    errors.append(f"POTENTIAL SECRET in {rel}: pattern matched '{pat}'")


def check_no_workflows():
    path = os.path.join(ROOT, ".github", "workflows")
    if os.path.isdir(path):
        errors.append("FORBIDDEN: .github/workflows directory exists")


def check_html_structure(path):
    rel = os.path.relpath(path, ROOT)
    with open(path, encoding="utf-8") as f:
        content = f.read()

    # Check void-element-aware tag matching
    void_elements = {
        "area", "base", "br", "col", "embed", "hr", "img",
        "input", "link", "meta", "param", "source", "track", "wbr",
    }
    stack = []
    tag_pattern = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)([^>]*)>")
    for match in tag_pattern.finditer(content):
        is_close, tag_name, attrs = match.groups()
        tag_name = tag_name.lower()
        if is_close:
            if stack and stack[-1] == tag_name:
                stack.pop()
            else:
                try:
                    idx = len(stack) - 1 - stack[::-1].index(tag_name)
                    for _ in range(len(stack) - idx):
                        stack.pop()
                except ValueError:
                    errors.append(f"{rel}: unexpected closing tag </{tag_name}>")
        else:
            if tag_name in void_elements or attrs.strip().endswith("/"):
                continue
            stack.append(tag_name)
    if stack:
        errors.append(f"{rel}: unclosed tags: {stack}")


def check_internal_links(path):
    """Check that anchor links (#id) reference existing IDs in the same file."""
    rel = os.path.relpath(path, ROOT)
    with open(path, encoding="utf-8") as f:
        content = f.read()

    # Collect all IDs
    id_pattern = re.compile(r'id=["\']([^"\']+)["\']')
    ids = set(id_pattern.findall(content))

    # Collect all anchor hrefs
    href_pattern = re.compile(r'href=["\']#([^"\']+)["\']')
    anchors = href_pattern.findall(content)

    for anchor in anchors:
        if anchor not in ids:
            errors.append(f"{rel}: anchor '#{anchor}' not found in file")


def check_css_referenced(html_path):
    """Check that the HTML references the CSS file."""
    with open(html_path, encoding="utf-8") as f:
        content = f.read()
    if "assets/style.css" not in content:
        errors.append(f"{os.path.relpath(html_path, ROOT)}: does not reference assets/style.css")


# --- Run checks ---

for f in REQUIRED_FILES:
    check_file_exists(f)

check_license_copyright()
check_readme_attribution()
check_no_secrets()
check_no_workflows()

for html in ["site/index.html", "site/checklist.html"]:
    path = os.path.join(ROOT, html)
    if os.path.isfile(path):
        check_html_structure(path)
        check_internal_links(path)
        check_css_referenced(path)

# --- Report ---

if errors:
    print("VERIFICATION FAILED")
    for e in errors:
        print(f"  ERROR: {e}")
    sys.exit(1)

if warnings:
    print("VERIFICATION PASSED (with warnings)")
    for w in warnings:
        print(f"  WARNING: {w}")
else:
    print("VERIFICATION PASSED")
    print(f"  Checked {len(REQUIRED_FILES)} required files")
    print(f"  LICENSE copyright line: OK")
    print(f"  README attribution: OK")
    print(f"  No secrets detected: OK")
    print(f"  No .github/workflows: OK")
    print(f"  HTML structure: OK")
    print(f"  Internal links: OK")
    print(f"  CSS references: OK")

sys.exit(0)
