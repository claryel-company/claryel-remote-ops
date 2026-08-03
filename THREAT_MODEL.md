# Threat model

## Protected assets

- control of the managed computer;
- private desired state and machine identity;
- credentials, signing keys and recovery material;
- personal files and application data;
- audit history and rollback evidence;
- integrity of public source and release artifacts.

## Trust planes

| Plane | Purpose | Must not contain |
|---|---|---|
| Public source | Reusable engine, schemas, policy, tests and documentation | Real machine identity, secrets, personal data or private topology |
| Private desired state | Owner-specific configuration and approved intent | Secret values or personal documents |
| Local secret storage | Credentials and recovery material | Public Git history |
| Local data | Documents, databases, logs and backups | Public source or provider prompts by default |
| AI provider | Proposal generation and explanation | Authority to bypass validation or approval |
| Privileged executor | Apply an approved bounded plan | General conversational access or unrestricted network authority |

## Principal threats and mitigations

| Threat | Mitigation |
|---|---|
| Prompt injection requests a dangerous command | Provider output is converted to a schema-constrained plan; unsupported actions are rejected |
| Repository compromise changes desired state | Protected branches, signed commits/releases, review, pinned revisions and risk-based approval |
| Stolen token grants broad control | Fine-grained short-lived tokens, minimum repository scope, rotation and revocation |
| Malicious dependency or update | Pinned dependencies, provenance, signed artifacts, checksum verification and staged rollout |
| Incorrect configuration breaks access | Preflight, configuration snapshot, out-of-band recovery where available, health gates and rollback |
| Private data enters the public repository | CI secret patterns, synthetic fixtures, review checklist and public/private ownership rules |
| AI provider retains sensitive content | Sanitised task packages, minimum context, provider policy review and local-only paths for restricted data |
| Privileged service is exploited | Minimal allowlist, isolated service account, narrow sudo rules, local binding and explicit IPC contract |
| Rollback evidence is forged or incomplete | Immutable timestamps, content hashes, independent health probes and retained last-known-good revision |
| Novice approves a misleading plan | Plain-language impact summary, risk label, changed-resource list and safe default refusal |

## Residual risks

Remote administration remains high impact. A compromised owner account, operating-system vulnerability, malicious maintainer, physical attacker or broken recovery channel can still defeat controls. The project reduces and exposes risk; it cannot remove the need for account security, backups, physical protection and independent review.
