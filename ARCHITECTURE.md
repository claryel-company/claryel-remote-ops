# CLARYEL RemoteOps architecture

## Objective

Provide a simple, provider-neutral and auditable way to manage an owner-controlled Windows, Linux or macOS computer through a voice or text conversation with an AI chat.

The user interface is the conversation. Git and GitHub are optional technical mechanisms for reviewable configuration history and approval; they are not the primary user experience.

## Control flow

`human voice or text intent -> AI-assisted proposal -> normalised change plan -> schema validation -> deterministic risk policy -> human approval when required -> private desired-state history -> preflight -> recovery preparation -> bounded operating-system adapter -> health validation -> success or rollback -> audit record`

No AI provider is the configuration source of truth. Deterministic validation, recorded desired state and the local privileged boundary remain authoritative.

## Components

### Conversational surface

The owner speaks or types a desired result in an AI chat. ChatGPT is the internally tested conversational path. Other AI chats may draft the same provider-neutral plan but remain untested until repeatable evidence is recorded.

The conversational surface may propose and explain. It cannot approve its own high-risk changes or bypass the local safety layer.

### Public RemoteOps engine

Reusable schemas, validation, policy, generic operating-system adapter contracts, synthetic fixtures, packaging and documentation. This repository owns that boundary.

### Private configuration history

Contains machine identity, owner-specific desired state, rollout policy and references to secret identifiers. A private repository can provide reviewable history and controlled collaboration, but it is an implementation detail hidden from the default novice workflow.

It must not contain secret values, personal documents, conversations, raw logs or backups.

### Local secret and data stores

Credentials, keys, recovery material, documents, databases, logs and backups remain on the device or in owner-approved private storage. They are addressed by reference, not copied into desired-state history or AI prompts.

### Privileged executor

A small local service applies only registered operations represented by a validated plan. It does not expose a general shell API. The executor must use narrow operating-system privileges, local IPC, pinned adapters and explicit timeouts.

### Health and rollback controller

Every mutation declares preconditions, expected health, timeout, recovery preparation and rollback. Success is recorded only after independent checks pass. A failed gate restores the last known-good generation or configuration snapshot when the adapter declares that recovery path.

## Operating-system adapter status

### Linux

The operating workflow is internally tested. A stable public support claim remains gated on reproducible installation, approved change, failed health-check and rollback evidence from public artefacts.

### macOS

The operating workflow is internally tested. The adapter must preserve FileVault, Gatekeeper, System Integrity Protection and platform privacy controls. Stable public support remains evidence-gated.

### Windows

The onboarding workspace and public plan schemas support Windows. The privileged Windows adapter is a separate release gate and must use registered PowerShell, package-management, service and system-configuration operations rather than an unrestricted shell. Restore, health-check and rollback evidence must be published before a stable Windows support claim.

## Risk classes

- `read-only`: discovery and reporting; no mutation.
- `low`: reversible user-level change with automatic validation.
- `medium`: service or package change requiring explicit review.
- `high`: network, identity, boot, storage, remote-access or privilege change requiring explicit approval and verified recovery.
- `forbidden`: arbitrary command execution, secret export, security-control bypass, destructive storage action without a separately governed recovery workflow, or any action outside the adapter allowlist.

## Simplicity contract

The default interface presents only four concepts:

1. speak or type the required result;
2. read the short plan;
3. approve when required;
4. receive a verified result or rollback.

Advanced configuration uses progressive disclosure. Security controls are not hidden or disabled; they are translated into plain-language consequences and safe defaults.
