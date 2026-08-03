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
    "START_HERE.md",
    "AGENTS.md",
    "CLAUDE.md",
    "REPOSITORY.yaml",
    "NEXT_STEPS.md",
    "LICENSE",
    "SECURITY.md",
    "THREAT_MODEL.md",
    "ARCHITECTURE.md",
    "USER_GUIDES/README.md",
    "adapters/windows/README.md",
    "adapters/linux/README.md",
    "adapters/macos/README.md",
    "schemas/desired-state.schema.json",
    "schemas/change-plan.schema.json",
    "examples/desired-state.windows.example.json",
    "installers/README.md",
    "installers/install-windows.ps1",
    "installers/install-macos.sh",
    "installers/install-ubuntu.sh",
    "docs/PRIVATE_REPOSITORY_SETUP.md",
    "docs/CHATGPT_SETUP.md",
    "docs/PRIVACY_AND_NETWORK.md",
]
LOCALES = ["en", "it", "de", "fr", "es", "nl", "pt", "pl", "ro", "cs", "sv", "el", "da", "fi", "zh-CN", "hi", "ar", "id", "uk", "ru"]
JSON_FILES = [
    "schemas/desired-state.schema.json",
    "schemas/change-plan.schema.json",
    "examples/desired-state.example.json",
    "examples/desired-state.windows.example.json",
    "examples/change-plan.example.json",
]
FORBIDDEN = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]
INSTALLER_FORBIDDEN = [
    re.compile(r"Set-ExecutionPolicy\s+Unrestricted", re.I),
    re.compile(r"DisableRealtimeMonitoring", re.I),
    re.compile(r"spctl\s+--master-disable", re.I),
    re.compile(r"csrutil\s+disable", re.I),
    re.compile(r"ufw\s+disable", re.I),
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
    for relative in JSON_FILES:
        path = ROOT / relative
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            error(f"invalid JSON in {relative}: {exc}")
            failures += 1

    desired_schema = json.loads((ROOT / "schemas/desired-state.schema.json").read_text(encoding="utf-8"))
    platforms = desired_schema["properties"]["device"]["properties"]["platform"]["enum"]
    if platforms != ["windows", "linux", "macos"]:
        error(f"unexpected platform contract: {platforms}")
        failures += 1

    change_schema = json.loads((ROOT / "schemas/change-plan.schema.json").read_text(encoding="utf-8"))
    adapters = change_schema["properties"]["operations"]["items"]["properties"]["adapter"]["enum"]
    if adapters != ["windows", "linux", "macos"]:
        error(f"unexpected adapter contract: {adapters}")
        failures += 1

    installer_markers = {
        "installers/install-windows.ps1": ["LOCALAPPDATA", "does not disable Defender", "private local configuration workspace"],
        "installers/install-macos.sh": ["Application Support/CLARYEL/RemoteOps", "does not disable Gatekeeper", "private local configuration workspace"],
        "installers/install-ubuntu.sh": ["claryel-remoteops", "apt-get", "private local configuration workspace"],
    }
    for relative, markers in installer_markers.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                error(f"installer {relative} missing marker: {marker}")
                failures += 1
        for pattern in INSTALLER_FORBIDDEN:
            if pattern.search(text):
                error(f"installer {relative} contains prohibited security weakening: {pattern.pattern}")
                failures += 1

    document_markers = {
        "README.md": ["private", "GitHub", "ChatGPT", "privacy-check"],
        "START_HERE.md": ["private", "GitHub", "ChatGPT", "Only select repositories"],
        "docs/PRIVATE_REPOSITORY_SETUP.md": ["Private", "GitHub", "privacy-check", "two-factor authentication"],
        "docs/CHATGPT_SETUP.md": ["ChatGPT", "GitHub", "Only select repositories", "Data Controls"],
        "docs/PRIVACY_AND_NETWORK.md": ["GitHub", "AI provider", "external services", "absolute invisibility"],
    }
    for relative, markers in document_markers.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for marker in markers:
            if marker.lower() not in text.lower():
                error(f"onboarding document {relative} missing {marker}")
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
    print(f"RemoteOps validation passed for installers, private onboarding, Windows, Linux, macOS and {len(LOCALES)} managed locales.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
