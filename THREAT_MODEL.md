# Threat model

## Protected assets

- control of the owner's managed computer;
- the owner's personal private repository and desired state;
- credentials, signing keys and recovery material;
- personal files and application data;
- audit history and rollback evidence;
- integrity of public source, installers and release artifacts.

## Trust planes

| Plane | Purpose | Must not contain |
|---|---|---|
| Public source | Reusable engine, installers, schemas, policy, tests and documentation | Real machine identity, secrets, personal data or private topology |
| Personal private GitHub repository | Owner-specific configuration, approved intent and reviewable history | Secret values, personal documents, chats, raw logs, databases or backups |
| Local secret storage | Credentials and recovery material | Git history or AI prompts |
| Local data | Documents, databases, logs and backups | Public source or provider prompts by default |
| AI provider | Proposal generation and explanation after explicit owner connection | Authority to bypass validation or approval, secrets or unrestricted personal data |
| Package sources | Deliver owner-approved software packages | Private repository content or personal files |
| Privileged executor | Apply an approved bounded plan | General conversational access or unrestricted network authority |

## Principal threats and mitigations

| Threat | Mitigation |
|---|---|
| Personal repository is accidentally public | Creation uses `--private`; authenticated GitHub CLI verifies `PRIVATE`; `privacy-check` fails closed |
| Over-permissioned GitHub App accesses other repositories | User instructions require `Only select repositories` and the single personal RemoteOps repository |
| Collaborator or compromised GitHub account reads private configuration | Passkey/2FA, minimum collaborators, periodic access review, revocation and non-secret repository content |
| Secret or personal file is committed | Restrictive `.gitignore`, tracked-file scanning, secret patterns and explicit prohibited-content policy |
| Prompt injection requests a dangerous command | Provider output is converted to a schema-constrained plan; unsupported actions are rejected |
| Repository compromise changes desired state | Reviewable history, protected workflows, pinned revisions and risk-based approval |
| Stolen token grants broad control | Fine-grained or app-scoped permissions, single-repository access, rotation and revocation |
| AI provider receives sensitive content | Minimum sanitized task packages, Data Controls review and local-only paths for restricted data |
| Installer weakens platform security | Validation rejects known security-disabling commands; installers state and preserve platform controls |
| Malicious dependency or update | Provenance, checksums, signed stable artifacts and staged rollout remain release gates |
| Incorrect configuration breaks access | Preflight, recovery preparation, independent health gates and rollback |
| Privileged service is exploited | Minimal allowlist, isolated service account, narrow privileges, local binding and explicit IPC contract |
| Rollback evidence is forged or incomplete | Immutable timestamps, content hashes, independent health probes and retained last-known-good revision |
| Novice approves a misleading plan | Plain-language impact summary, risk label, changed-resource list and safe default refusal |

## External service reality

GitHub and the chosen AI provider are external services. Private repository access controls and HTTPS/TLS reduce exposure but do not create absolute invisibility. RemoteOps cannot prevent provider incidents, legal access, a compromised owner account, an unlocked device or abuse by an explicitly authorized collaborator or application.

The onboarding utility and installers add no advertising network or unrelated analytics service. Installing approved software can contact package repositories and normal operating-system certificate, time and update infrastructure.

## Residual risks

Remote administration remains high impact. A compromised owner account, operating-system vulnerability, malicious maintainer, physical attacker, provider incident or broken recovery channel can still defeat controls. The project reduces, exposes and verifies risk; it cannot remove the need for account security, local disk encryption, backups, physical protection, permission review and independent security assessment.
