# Agent instructions

## Authority

Before structural work, read the authoritative CLARYEL project context in `claryel-company/claryel-platform`, then read this repository's `README.md`, `ARCHITECTURE.md`, `SECURITY.md`, `THREAT_MODEL.md`, `REPOSITORY.yaml` and `NEXT_STEPS.md`.

## Repository purpose

This repository owns the reusable public CLARYEL RemoteOps release boundary. It does not own concrete CLARYEL machines, private fleet state, customer data, secrets, support operations or commercial orchestration.

## Mandatory rules

1. Keep durable project documentation in English.
2. Keep managed end-user translations under `USER_GUIDES/locales/` or website localisation resources.
3. Never commit real hostnames, IP addresses, usernames, repository tokens, SSH keys, personal files, prompts, conversations, logs, telemetry or backups.
4. Use synthetic examples only.
5. Treat AI output as an untrusted proposal until validated by deterministic policy and human approval where required.
6. Do not add an arbitrary-shell execution path.
7. Preserve the public/private trust-plane boundary.
8. Mark capabilities as tested, documented-but-untested, planned or blocked. Never infer readiness from architecture alone.
9. Update the user guide and threat model with every material user-visible or security change.
10. Use branches, validation and Pull Requests for changes.

## Validation

Run:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

## Release safety

A release must not be described as production-ready until Linux and macOS installation, configuration, health-check and rollback evidence is reproducible from the public repository and the security review gate is complete.
