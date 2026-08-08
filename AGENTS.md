<!-- CLARYEL-AGENT-ENTRY:START -->
# CLARYEL repository entry point

This repository is one bounded component of the CLARYEL architecture. Project-wide assumptions, architecture, decisions, terminology, repository ownership, routing, development rules and project-wide metric definitions are authoritative only in `claryel-company/claryel-platform`.

Before any analysis, command or edit:

1. Confirm that this repository is inside the active-only scope.
2. Open `claryel-company/claryel-platform` first.
3. Read `ASSUMPTIONS.md`, `ARCHITECTURE.md`, `DECISIONS.md`, related ADRs, `REPOSITORIES.md`, `TASK_ROUTING.md`, `TERMINOLOGY.md`, `DEVELOPMENT_RULES.md`, `METRICS.md`, `docs/standards/product-system-documentation.md` and `repository-catalog.yaml` there.
4. For project-wide numerical metrics, read `docs/standards/canonical-code-metrics.md` and use the central implementation rather than a repository-local counter.
5. Confirm that the requested capability belongs to `claryel-remote-ops` before implementation.
6. Read this repository's `README.md`, `ARCHITECTURE.md`, `SECURITY.md`, `THREAT_MODEL.md`, `REPOSITORY.yaml`, `DOCUMENTATION.yaml` when present, `NEXT_STEPS.md` and `USER_GUIDES/README.md`.
7. Update affected lifecycle documentation in the same governed change.
8. Do not duplicate project-wide documentation, project-wide metric definitions or functionality owned by another repository.
<!-- CLARYEL-AGENT-ENTRY:END -->

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
