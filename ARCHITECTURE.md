# CLARYEL RemoteOps architecture

## Objective

Provide a simple, provider-neutral and auditable way to manage an owner-controlled Windows, Linux or macOS computer through a voice or text conversation with an AI chat.

The user interface is the conversation. The owner creates a separate personal **Private** repository in the owner's own GitHub account for non-secret configuration history. GitHub is a technical history and approval mechanism, not the primary user experience.

## Ownership model

The complete user-controlled boundary contains:

1. the owner's computer and local RemoteOps installation;
2. the owner's personal private GitHub repository;
3. the owner's selected AI account and explicitly granted repository access.

RemoteOps never changes the personal repository to public, never adds collaborators and never silently authorizes an AI provider. Private visibility hides the repository from the public, while GitHub remains the service operator and explicitly authorized people or applications may have access.

## Control flow

`human voice or text intent -> AI-assisted proposal -> normalised change plan -> schema validation -> deterministic risk policy -> human approval when required -> personal private desired-state history -> preflight -> recovery preparation -> bounded operating-system adapter -> health validation -> success or rollback -> audit record`

No AI provider is the configuration source of truth. Deterministic validation, recorded desired state and the local privileged boundary remain authoritative.

## Components

### Conversational surface

The owner speaks or types a desired result in an AI chat. ChatGPT is the internally tested conversational path. Other AI chats may draft the same provider-neutral plan but remain untested until repeatable evidence is recorded.

The owner controls the AI account, connection and permissions. The conversational surface may propose and explain. It cannot approve its own high-risk changes or bypass the local safety layer.

### Public RemoteOps engine

Reusable schemas, validation, policy, generic operating-system adapter contracts, transparent installers, synthetic fixtures, packaging and documentation. This public repository contains no concrete owner computer identity, personal repository content, credentials, personal files or private operational history.

### Personal private configuration repository

The owner creates this repository in the owner's own GitHub account and selects `Private`. It contains only machine identity chosen by the owner, owner-specific desired state, rollout policy, bounded change history and references to local secret identifiers.

RemoteOps requires:

- private visibility verification through authenticated GitHub CLI when available;
- no collaborators unless the owner explicitly adds them;
- repository-scoped application access;
- periodic `remoteops privacy-check`;
- no secret values, personal documents, conversations, raw logs, databases, telemetry or backups.

Private visibility is an access-control boundary, not a guarantee of absolute invisibility. Account compromise, over-permissioned applications, authorized collaborators and provider incidents remain residual risks.

### Local secret and data stores

Credentials, keys, recovery material, documents, databases, logs and backups remain on the device or in owner-approved private storage. They are addressed by reference, not copied into the private configuration repository or AI prompts.

### Privileged executor

A small local service applies only registered operations represented by a validated plan. It does not expose a general shell API. The executor must use narrow operating-system privileges, local IPC, pinned adapters and explicit timeouts.

### Health and rollback controller

Every mutation declares preconditions, expected health, timeout, recovery preparation and rollback. Success is recorded only after independent checks pass. A failed gate restores the last known-good generation or configuration snapshot when the adapter declares that recovery path.

## External communication boundary

RemoteOps is local before the owner connects anything. External communication is limited to owner-selected actions:

- GitHub when the owner creates, connects, pulls or pushes the personal private repository;
- the selected AI provider when the owner connects and uses it;
- approved package sources for software installation or update;
- normal operating-system certificate, time and update infrastructure.

The onboarding utility and installers add no advertising network or unrelated analytics service. They do not intentionally upload personal files, secrets, chat exports, raw logs, databases or backups.

RemoteOps cannot override the privacy, retention, legal or security policies of GitHub, OpenAI or another owner-selected provider.

## Operating-system adapter status

### Linux

The operating workflow is internally tested. A stable public support claim remains gated on reproducible installation, approved change, failed health-check and rollback evidence from public artefacts.

### macOS

The operating workflow is internally tested. The adapter must preserve FileVault, Gatekeeper, System Integrity Protection and platform privacy controls. Stable public support remains evidence-gated.

### Windows

The guided installer, onboarding workspace and public plan schemas support Windows. The privileged Windows adapter is a separate release gate and must use registered PowerShell, package-management, service and system-configuration operations rather than an unrestricted shell. Restore, health-check and rollback evidence must be published before a stable Windows support claim.

## Risk classes

- `read-only`: discovery and reporting; no mutation.
- `low`: reversible user-level change with automatic validation.
- `medium`: service or package change requiring explicit review.
- `high`: network, identity, boot, storage, remote-access or privilege change requiring explicit approval and verified recovery.
- `forbidden`: arbitrary command execution, secret export, security-control bypass, destructive storage action without a separately governed recovery workflow, or any action outside the adapter allowlist.

## Simplicity contract

The default setup presents seven clear steps:

1. choose the Windows, macOS or Ubuntu installer;
2. create the private local workspace;
3. create the owner's personal `Private` GitHub repository;
4. verify `PRIVATE` visibility and scan tracked files;
5. authorize only that repository in the selected AI account;
6. speak or type the required result and review the plan;
7. receive a verified result or rollback.

Advanced configuration uses progressive disclosure. Security controls are not hidden or disabled; they are translated into plain-language consequences and safe defaults.
