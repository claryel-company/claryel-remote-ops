#!/usr/bin/env python3
"""Safe onboarding utility for CLARYEL RemoteOps."""

from __future__ import annotations

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

SUPPORTED = {"Linux": "linux", "Darwin": "macos", "Windows": "windows"}
SUPPORTED_IDS = frozenset(SUPPORTED.values())
SENSITIVE_SUFFIXES = {".env", ".key", ".pem", ".p12", ".pfx", ".kdbx", ".sqlite", ".db", ".log", ".bak"}
SENSITIVE_NAMES = {
    "id_rsa",
    "id_ed25519",
    "credentials.json",
    "secrets.json",
    "passwords.txt",
    "recovery-codes.txt",
}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]


def fail(message: str, code: int = 1) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(code)


def run(command: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)
    except OSError as exc:
        fail(f"Cannot run {command[0]}: {exc}")


def current_platform() -> str:
    system = platform.system()
    if system not in SUPPORTED:
        fail(f"Unsupported operating system: {system or 'unknown'}")
    return SUPPORTED[system]


def workspace_path(value: str) -> Path:
    target = Path(value).expanduser().resolve()
    if not (target / ".git").is_dir():
        fail(f"Not a RemoteOps Git workspace: {target}")
    return target


def write_onboarding_files(target: Path, platform_id: str) -> None:
    (target / ".gitignore").write_text(
        """# Never commit secrets or personal content
.env
.env.*
*.key
*.pem
*.p12
*.pfx
*.kdbx
*.log
*.db
*.sqlite
backups/
logs/
personal/
secrets/
credentials/
recovery/
""",
        encoding="utf-8",
    )
    (target / "README.md").write_text(
        f"""# My private CLARYEL RemoteOps configuration

This repository belongs to its owner and must remain **Private** on GitHub.

Managed platform: `{platform_id}`

This repository may contain reviewed computer configuration and change history.
It must never contain passwords, access tokens, private keys, recovery codes,
personal documents, chat exports, raw logs, databases or backups.

RemoteOps does not add collaborators or change repository visibility. Review
GitHub access settings regularly and remove any person or application that does
not need access.
""",
        encoding="utf-8",
    )
    (target / "PRIVACY.md").write_text(
        """# Privacy boundary

## Stored here

- computer identifier chosen by the owner;
- approved configuration intent;
- reviewable change history;
- references to local secret identifiers, never secret values.

## Never stored here

- passwords, tokens, private keys or recovery codes;
- personal documents, photos, email or chat history;
- raw logs, databases, telemetry or backups;
- unrestricted remote-access credentials.

GitHub and the selected AI provider are external services. RemoteOps contacts
them only when the owner explicitly connects and uses them. Installing software
may also contact package sources approved by the owner.
""",
        encoding="utf-8",
    )
    (target / "CHATGPT_SETUP.md").write_text(
        """# Connect ChatGPT safely

1. In ChatGPT, open Settings and Apps.
2. Select the GitHub app when it is available for your plan and experience.
3. Authorize only this private repository, not all repositories.
4. Review the requested permissions before approving them.
5. In ChatGPT Data Controls, turn off “Improve the model for everyone” when you
   do not want new conversations used to improve general models.
6. Never paste passwords, private keys, recovery codes or personal files into a
   chat. Ask RemoteOps to prepare a plan using sanitized configuration only.
7. Ask ChatGPT to explain the impact, recovery path and verification before any
   important change.

GitHub app availability and write capability vary by ChatGPT plan and mode. A
read-only connection cannot apply changes. Use only an explicitly approved,
repository-scoped write-capable workflow when needed.
""",
        encoding="utf-8",
    )


def doctor(_: argparse.Namespace) -> None:
    platform_id = current_platform()
    git_path = shutil.which("git")
    if not git_path:
        fail("Git is required for the owner-controlled configuration history. Install Git, then run doctor again.")
    print(
        json.dumps(
            {
                "ok": True,
                "platform": platform_id,
                "git": git_path,
                "githubCli": shutil.which("gh"),
                "scope": "safe-owner-controlled-workspace",
                "privilegedAdapterEvidence": "pending-public-release-evidence"
                if platform_id == "windows"
                else "internally-tested-public-evidence-pending",
            },
            indent=2,
        )
    )


def init_workspace(args: argparse.Namespace) -> None:
    platform_id = current_platform()
    target = Path(args.path).expanduser().resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and any(target.iterdir()):
        fail(f"Target directory is not empty: {target}")
    target.mkdir(mode=0o700, parents=True, exist_ok=True)
    result = run(["git", "init", "-b", "main"], cwd=target)
    if result.returncode != 0:
        fail(result.stderr.strip() or "git init failed")
    (target / "desired-state.json").write_text(
        json.dumps(
            {
                "schemaVersion": "1.0",
                "device": {"id": "replace-with-private-device-id", "platform": platform_id},
                "policies": {"approval": "risk-based", "rollback": "required"},
                "services": [],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    write_onboarding_files(target, platform_id)
    try:
        os.chmod(target, 0o700)
    except OSError:
        pass
    print(f"Your private local RemoteOps workspace was created at {target}")
    print("It is not uploaded anywhere until you explicitly connect and push a private repository.")
    print("Never store secret values or personal files in Git.")


def ensure_initial_commit(target: Path) -> None:
    add = run(["git", "add", "desired-state.json", ".gitignore", "README.md", "PRIVACY.md", "CHATGPT_SETUP.md"], cwd=target)
    if add.returncode != 0:
        fail(add.stderr.strip() or "Cannot stage initial private configuration")
    status = run(["git", "status", "--porcelain"], cwd=target)
    if not status.stdout.strip():
        return
    if run(["git", "config", "user.name"], cwd=target).returncode != 0:
        run(["git", "config", "user.name", "CLARYEL RemoteOps Owner"], cwd=target)
    if run(["git", "config", "user.email"], cwd=target).returncode != 0:
        run(["git", "config", "user.email", "remoteops-owner@localhost"], cwd=target)
    commit = run(["git", "commit", "-m", "Initialize private RemoteOps configuration"], cwd=target)
    if commit.returncode != 0:
        fail(commit.stderr.strip() or commit.stdout.strip() or "Cannot create initial commit")


def github_visibility(repository: str, cwd: Path) -> dict[str, object] | None:
    if not shutil.which("gh"):
        return None
    auth = run(["gh", "auth", "status"], cwd=cwd)
    if auth.returncode != 0:
        return None
    view = run(["gh", "repo", "view", repository, "--json", "nameWithOwner,visibility,url,viewerPermission"], cwd=cwd)
    if view.returncode != 0:
        fail(view.stderr.strip() or "GitHub CLI could not inspect the repository")
    try:
        return json.loads(view.stdout)
    except json.JSONDecodeError as exc:
        fail(f"GitHub CLI returned invalid repository metadata: {exc}")


def connect_repository(args: argparse.Namespace) -> None:
    target = workspace_path(args.path)
    ensure_initial_commit(target)
    existing = run(["git", "remote", "get-url", "origin"], cwd=target)
    if existing.returncode == 0:
        fail(f"This workspace already has an origin remote: {existing.stdout.strip()}")

    if args.create_private:
        if not shutil.which("gh"):
            fail("GitHub CLI is required for automatic private-repository creation. Install gh and run 'gh auth login'.")
        auth = run(["gh", "auth", "status"], cwd=target)
        if auth.returncode != 0:
            fail("GitHub CLI is not authenticated. Run 'gh auth login', choose GitHub.com and HTTPS, then retry.")
        create = run(
            ["gh", "repo", "create", args.create_private, "--private", "--source", ".", "--remote", "origin", "--push"],
            cwd=target,
        )
        if create.returncode != 0:
            fail(create.stderr.strip() or create.stdout.strip() or "Private repository creation failed")
        metadata = github_visibility(args.create_private, target)
        if not metadata or str(metadata.get("visibility", "")).upper() != "PRIVATE":
            fail("Repository creation finished but private visibility could not be verified. Stop and inspect GitHub settings.")
        print(json.dumps({"ok": True, "private": True, "repository": metadata}, indent=2))
        print("Only you and collaborators you explicitly add can access this private repository through GitHub permissions.")
        return

    if not args.repository_url:
        fail("Choose --create-private NAME or --repository-url URL")
    if not args.confirm_private:
        fail("Manual connection requires --confirm-private after you have verified the repository is Private in GitHub settings.")
    remote = run(["git", "remote", "add", "origin", args.repository_url], cwd=target)
    if remote.returncode != 0:
        fail(remote.stderr.strip() or "Cannot add the private repository remote")
    metadata = github_visibility(args.repository_url, target)
    if metadata and str(metadata.get("visibility", "")).upper() != "PRIVATE":
        run(["git", "remote", "remove", "origin"], cwd=target)
        fail("The selected GitHub repository is not Private. It was disconnected without pushing.")
    if args.push:
        push = run(["git", "push", "-u", "origin", "main"], cwd=target)
        if push.returncode != 0:
            fail(push.stderr.strip() or "Cannot push the private configuration repository")
    print(json.dumps({"ok": True, "privateVerified": bool(metadata), "remote": args.repository_url}, indent=2))
    if not metadata:
        print("WARNING: GitHub CLI was unavailable, so RemoteOps could not independently verify visibility. Check Settings > General > Visibility before pushing.")


def scan_tracked_files(target: Path) -> list[str]:
    result = run(["git", "ls-files"], cwd=target)
    if result.returncode != 0:
        fail(result.stderr.strip() or "Cannot list tracked files")
    findings: list[str] = []
    for relative in filter(None, result.stdout.splitlines()):
        path = target / relative
        lower_name = path.name.lower()
        if path.suffix.lower() in SENSITIVE_SUFFIXES or lower_name in SENSITIVE_NAMES:
            findings.append(f"sensitive filename: {relative}")
        if not path.is_file() or path.stat().st_size > 1_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                findings.append(f"possible secret content: {relative}")
                break
    return findings


def privacy_check(args: argparse.Namespace) -> None:
    target = workspace_path(args.path)
    remote = run(["git", "remote", "get-url", "origin"], cwd=target)
    if remote.returncode != 0:
        fail("No personal repository is connected yet.")
    remote_url = remote.stdout.strip()
    metadata = github_visibility(remote_url, target)
    findings = scan_tracked_files(target)
    visibility = "unverified"
    if metadata:
        visibility = str(metadata.get("visibility", "unknown")).upper()
        if visibility != "PRIVATE":
            findings.append(f"repository visibility is {visibility}, not PRIVATE")
    payload = {
        "ok": not findings and visibility == "PRIVATE",
        "remote": remote_url,
        "visibility": visibility,
        "repository": metadata,
        "findings": findings,
    }
    print(json.dumps(payload, indent=2))
    if visibility == "unverified":
        fail("Install and authenticate GitHub CLI so RemoteOps can verify private visibility.", 2)
    if findings:
        fail("Privacy check failed. Do not push further changes until every finding is resolved.", 3)


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
    if device.get("platform") not in SUPPORTED_IDS:
        fail("device.platform must be windows, linux or macos")
    policies = payload.get("policies") or {}
    if policies.get("rollback") != "required":
        fail("rollback policy must be required")
    print(json.dumps({"ok": True, "file": str(path), "platform": device.get("platform")}, indent=2))


def status(args: argparse.Namespace) -> None:
    target = workspace_path(args.path)
    branch = run(["git", "branch", "--show-current"], cwd=target)
    state = run(["git", "status", "--porcelain"], cwd=target)
    remote = run(["git", "remote", "get-url", "origin"], cwd=target)
    manifest = target / "desired-state.json"
    platform_id = None
    if manifest.is_file():
        try:
            platform_id = json.loads(manifest.read_text(encoding="utf-8")).get("device", {}).get("platform")
        except (OSError, json.JSONDecodeError):
            platform_id = "invalid"
    print(
        json.dumps(
            {
                "ok": True,
                "path": str(target),
                "platform": platform_id,
                "branch": branch.stdout.strip() or None,
                "clean": not bool(state.stdout.strip()),
                "remoteConfigured": remote.returncode == 0,
                "remote": remote.stdout.strip() if remote.returncode == 0 else None,
            },
            indent=2,
        )
    )


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        prog="remoteops",
        description="Prepare the safe owner-controlled workspace used by CLARYEL RemoteOps.",
    )
    sub = root.add_subparsers(dest="command", required=True)
    doctor_command = sub.add_parser("doctor", help="check prerequisites without changing the computer")
    doctor_command.set_defaults(handler=doctor)
    init_command = sub.add_parser("init", help="create your private local computer-configuration workspace")
    init_command.add_argument("--path", required=True)
    init_command.set_defaults(handler=init_workspace)
    connect_command = sub.add_parser("connect", help="create or connect your personal private GitHub repository")
    connect_command.add_argument("--path", required=True)
    group = connect_command.add_mutually_exclusive_group(required=True)
    group.add_argument("--create-private", metavar="NAME", help="create a private repository in your authenticated GitHub account")
    group.add_argument("--repository-url", help="connect an existing repository URL")
    connect_command.add_argument("--confirm-private", action="store_true", help="confirm an existing repository is private")
    connect_command.add_argument("--push", action="store_true", help="push the initial configuration after connecting")
    connect_command.set_defaults(handler=connect_repository)
    privacy_command = sub.add_parser("privacy-check", help="verify private visibility and scan tracked files for common secrets")
    privacy_command.add_argument("--path", required=True)
    privacy_command.set_defaults(handler=privacy_check)
    validate_command = sub.add_parser("validate", help="validate a Windows, Linux or macOS desired-state file")
    validate_command.add_argument("file")
    validate_command.set_defaults(handler=validate_manifest)
    status_command = sub.add_parser("status", help="show the private workspace status")
    status_command.add_argument("--path", required=True)
    status_command.set_defaults(handler=status)
    return root


def main() -> None:
    args = parser().parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
