# Security policy

## Supported versions

No production-supported public version exists yet. Security fixes target the default branch and the latest release candidate.

## Reporting a vulnerability

Do not open a public issue for a vulnerability that could expose credentials, personal data, private repositories, remote-access channels or privilege-escalation paths. Contact the maintainers through the private security-reporting channel configured in the GitHub repository.

Include the affected version, operating system, prerequisites, reproduction steps, observed impact and a safe proof of concept. Do not access systems or data that you do not own or have explicit permission to test.

## Security invariants

1. Public source never contains concrete owner state or secrets.
2. AI output is never executed directly as arbitrary shell.
3. Every mutation is described by a validated change plan.
4. Risk classification is deterministic and independent of the AI provider.
5. High-risk operations require explicit, attributable approval.
6. Backup and rollback are verified before high-impact changes.
7. Health gates fail closed.
8. Private desired state is versioned separately from public code.
9. Credentials use least privilege, expiration and revocation.
10. Logs avoid secret values and personal content.

## Prohibited defaults

- password authentication when key-based or platform identity is available;
- root login for routine operation;
- unrestricted repository tokens;
- unsigned updates;
- silent auto-approval;
- direct public exposure of the management endpoint;
- retention of prompts or command output containing personal data without an explicit policy;
- disabling platform security controls to make installation easier.

## Release security gates

A public production release requires secret scanning of full history, dependency review, static validation, Linux and macOS rollback tests, signed artifacts, checksums, branch protection, least-privilege permission review and an independent assessment of the privileged execution boundary.
