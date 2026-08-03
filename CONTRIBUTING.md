# Contributing

## Before contributing

Read `AGENTS.md`, `ARCHITECTURE.md`, `SECURITY.md` and `THREAT_MODEL.md`. Use synthetic data only.

## Workflow

1. Open or select an issue that states the user outcome and security boundary.
2. Create a focused branch.
3. Add tests and user-guide updates with the change.
4. Run `python3 scripts/validate.py` and the test suite.
5. Open a Pull Request describing impact, risk, validation and rollback.
6. Do not merge until required checks and review are complete.

## Public-data rule

Never contribute real device identity, private repository content, credentials, personal data, prompts, conversations, telemetry or backups. Replace examples with clearly synthetic values.

## Security-sensitive changes

Changes to privilege, authentication, network exposure, update verification, plan validation, approval or rollback require threat-model review and a maintainer with security responsibility.

## Localisation

Canonical technical facts are English. End-user localisation lives under `USER_GUIDES/locales/` and the managed website resources. A translation must preserve safety warnings, tested-status labels and the public/private boundary.
