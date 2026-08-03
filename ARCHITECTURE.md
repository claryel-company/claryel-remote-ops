# CLARYEL RemoteOps architecture

## Objective

Provide a simple, provider-neutral and auditable way to manage an owner-controlled Linux or macOS computer after a minimal operating-system installation.

## Control flow

`human intent -> AI or form-assisted proposal -> normalised change plan -> schema validation -> deterministic risk policy -> human approval when required -> private desired-state commit -> preflight -> backup -> bounded adapter -> health validation -> success or rollback -> audit record`

No AI provider is the configuration source of truth. Git history, deterministic validation and the local privileged boundary remain authoritative.

## Components

### Public engine

Reusable schemas, validation, policy, generic operating-system adapters, synthetic fixtures, packaging and documentation. This repository owns that boundary.

### Private owner repository

Contains machine identity, owner-specific desired state, rollout policy and references to secret identifiers. A private repository is recommended because it provides reviewable history and controlled collaboration. It must not contain secret values or personal documents.

### Local secret and data stores

Credentials, keys, recovery material, documents, databases, logs and backups remain on the device or in owner-approved private storage. They are addressed by reference, not copied into desired-state Git.

### Proposal surface

ChatGPT is the internally tested proposal and operating surface. Claude, Gemini, Perplexity and Grok have technically plausible GitHub or coding-agent paths but remain untested with RemoteOps. A proposal surface may explain and draft; it cannot bypass local controls.

### Privileged executor

A small local service applies only registered operations represented by a validated plan. It does not expose a general shell API. The executor must use narrow operating-system privileges, local IPC, pinned adapters and explicit timeouts.

### Health and rollback controller

Every change declares preconditions, expected health, timeout, backup and rollback. Success is recorded only after independent checks pass. A failed gate restores the last known-good generation or configuration snapshot.

## Risk classes

- `read-only`: discovery and reporting; no mutation.
- `low`: reversible user-level change with automatic validation.
- `medium`: service or package change requiring explicit review.
- `high`: network, identity, boot, storage, remote-access or privilege change requiring explicit approval and verified recovery.
- `forbidden`: arbitrary command execution, secret export, security-control bypass, destructive storage action without a separately governed recovery workflow, or any action outside the adapter allowlist.

## Supported operating systems

The initial validated internal boundary is Linux and macOS. Exact public version support is declared only after reproducible public evidence is recorded. Windows is outside the first public release boundary.

## Simplicity contract

The default interface presents only four actions: connect, describe, approve and verify. Advanced configuration is progressive disclosure. Security controls are not hidden or disabled; they are translated into plain-language consequences and safe defaults.
