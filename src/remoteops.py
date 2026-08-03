#!/usr/bin/env python3
"""Safe release-candidate onboarding utility for CLARYEL RemoteOps."""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

SUPPORTED = {"Linux": "linux", "Darwin": "macos"}


def fail(message: str, code: int = 1) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(code)


def run(command: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)


def doctor(_: argparse.Namespace) -> None:
    system = platform.system()
    if system not in SUPPORTED:
        fail(f"Unsupported operating system: {system or 'unknown'}")
    missing = [name for name in ("git",) if shutil.which(name) is None]
    if missing:
        fail(f"Missing required tools: {', '.join(missing)}")
    print(json.dumps({"ok": True, "platform": SUPPORTED[system], "git": shutil.which("git")}, indent=2))


def init_workspace(args: argparse.Namespace) -> None:
    target = Path(args.path).expanduser().resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and any(target.iterdir()):
        fail(f"Target directory is not empty: {target}")
    target.mkdir(mode=0o700, parents=True, exist_ok=True)
    result = run(["git", "init", "-b", "main"], cwd=target)
    if result.returncode != 0:
        fail(result.stderr.strip() or "git init failed")
    manifest = target / "desired-state.json"
    manifest.write_text(
        json.dumps(
            {
                "schemaVersion": "1.0",
                "device": {"id": "replace-with-private-device-id", "platform": SUPPORTED[platform.system()]},
                "policies": {"approval": "risk-based", "rollback": "required"},
                "services": [],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    os.chmod(target, 0o700)
    print(f"Private desired-state workspace created at {target}")
    print("Replace the synthetic device ID before committing. Never store secret values in Git.")


def validate_manifest(args: argparse.Namespace) -> None:
    path = Path(args.file).expanduser().resolve()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Cannot read valid JSON from {path}: {exc}")
    required = {"schemaVersion", "device", "policies"}
    missing = sorted(required - payload.keys())
    if missing:
        fail(f"Missing required keys: {', '.join(missing)}")
    if payload.get("schemaVersion") != "1.0":
        fail("Unsupported schemaVersion")
    device = payload.get("device") or {}
    if device.get("platform") not in {"linux", "macos"}:
        fail("device.platform must be linux or macos")
    policies = payload.get("policies") or {}
    if policies.get("rollback") != "required":
        fail("rollback policy must be required")
    print(json.dumps({"ok": True, "file": str(path), "platform": device.get("platform")}, indent=2))


def status(args: argparse.Namespace) -> None:
    target = Path(args.path).expanduser().resolve()
    if not (target / ".git").is_dir():
        fail(f"Not a Git workspace: {target}")
    branch = run(["git", "branch", "--show-current"], cwd=target)
    state = run(["git", "status", "--porcelain"], cwd=target)
    remote = run(["git", "remote", "get-url", "origin"], cwd=target)
    print(
        json.dumps(
            {
                "ok": True,
                "path": str(target),
                "branch": branch.stdout.strip() or None,
                "clean": not bool(state.stdout.strip()),
                "remoteConfigured": remote.returncode == 0,
            },
            indent=2,
        )
    )


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="remoteops", description="CLARYEL RemoteOps safe onboarding utility")
    sub = root.add_subparsers(dest="command", required=True)
    doctor_command = sub.add_parser("doctor", help="check local prerequisites without changing the computer")
    doctor_command.set_defaults(handler=doctor)
    init_command = sub.add_parser("init", help="create a private desired-state workspace")
    init_command.add_argument("--path", required=True)
    init_command.set_defaults(handler=init_workspace)
    validate_command = sub.add_parser("validate", help="validate a desired-state JSON file")
    validate_command.add_argument("file")
    validate_command.set_defaults(handler=validate_manifest)
    status_command = sub.add_parser("status", help="show private workspace status")
    status_command.add_argument("--path", required=True)
    status_command.set_defaults(handler=status)
    return root


def main() -> None:
    args = parser().parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
