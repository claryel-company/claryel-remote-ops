#!/usr/bin/env python3
"""Validate the public CLARYEL RemoteOps repository without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "REPOSITORY.yaml",
    "NEXT_STEPS.md",
    "LICENSE",
    "SECURITY.md",
    "THREAT_MODEL.md",
    "ARCHITECTURE.md",
    "USER_GUIDES/README.md",
    "schemas/desired-state.schema.json",
    "schemas/change-plan.schema.json",
]
LOCALES = ["en", "it", "de", "fr", "es", "nl", "pt", "pl", "ro", "cs", "sv", "el", "da", "fi", "zh-CN", "hi", "ar", "id", "uk", "ru"]
FORBIDDEN = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]


def error(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    failures = 0
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            error(f"missing required file: {relative}")
            failures += 1
    for locale in LOCALES:
        path = ROOT / "USER_GUIDES" / "locales" / f"{locale}.md"
        if not path.is_file():
            error(f"missing locale guide: {locale}")
            failures += 1
    for relative in ("schemas/desired-state.schema.json", "schemas/change-plan.schema.json", "examples/desired-state.example.json", "examples/change-plan.example.json"):
        path = ROOT / relative
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            error(f"invalid JSON in {relative}: {exc}")
            failures += 1
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in FORBIDDEN:
            if pattern.search(text):
                error(f"possible secret in {path.relative_to(ROOT)}")
                failures += 1
    if failures:
        return 1
    print(f"RemoteOps validation passed for {len(LOCALES)} managed locales.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
