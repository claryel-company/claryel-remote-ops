# Security policy

## Supported versions

No production-supported public version exists yet. Security fixes target the default branch and the latest release candidate.

## Reporting a vulnerability

Do not open a public issue for a vulnerability that could expose credentials, personal data, private repositories, remote-access channels or privilege-escalation paths. Contact the maintainers through the private security-reporting channel configured in the GitHub repository.

Include the affected version, operating system, prerequisites, reproduction steps, observed impact and a safe proof of concept. Do not access systems or data that you do not own or have explicit permission to test.

## Security invariants

1. Public source never contains concrete owner state or secrets.
2. The owner creates a separate personal GitHub repository with `Private` visibility.
3. RemoteOps never makes that repository public, adds collaborators or silently authorizes applications.
4. Private visibility is verified through authenticated GitHub CLI when available.
5. Repository access is restricted to the owner and explicitly authorized people or applications.
6. Passwords, tokens, private keys, recovery codes, personal files, chats, raw logs, databases and backups never enter Git.
7. AI output is never executed directly as arbitrary shell or PowerShell.
8. Every mutation is described by a validated change plan.
9. Risk classification is deterministic and independent of the AI provider.
10. High-risk operations require explicit, attributable approval.
11. Recovery preparation and rollback are verified before high-impact changes.
12. Health gates fail closed.
13. Credentials use least privilege, expiration and revocation.
14. Logs avoid secret values and personal content.

## Private repository controls

- enable a passkey or two-factor authentication on the owner's GitHub account;
- use `Only select repositories` for GitHub Apps and OAuth applications;
- authorize only the personal RemoteOps repository;
- do not add collaborators unless they genuinely need access;
- run `remoteops privacy-check` after setup and permission changes;
- disconnect and revoke access immediately after suspected account or credential exposure;
- treat GitHub as an external service operator, not as an invisible local disk.

## AI account controls

- the owner chooses whether to connect ChatGPT or another provider;
- review every requested repository permission;
- review account Data Controls and training preferences;
- send only minimum sanitized configuration context;
- never paste secret values or personal files into a conversation;
- a read-only app connection must not be represented as write-capable control.

## External communication

The onboarding utility is local before the owner connects anything. It communicates externally only when the owner explicitly uses:

- GitHub for the personal private repository;
- the selected AI provider;
- approved operating-system package sources;
- normal certificate, time and update infrastructure.

The installers add no advertising tracker or unrelated analytics service.

## Prohibited defaults

- password authentication when key-based or platform identity is available;
- root login for routine operation;
- unrestricted repository tokens or all-repository application access;
- unsigned stable releases;
- silent auto-approval;
- direct public exposure of the management endpoint;
- retention of prompts or command output containing personal data without an explicit policy;
- disabling Defender, UAC, BitLocker, SmartScreen, Gatekeeper, FileVault, SIP, LUKS or platform privacy controls to simplify installation;
- claims that a private cloud repository is absolutely invisible or immune from account compromise.

## Release security gates

A stable public release requires secret scanning of full history, dependency review, static validation, installer tests, Windows/Linux/macOS rollback evidence for claimed versions, signed artifacts, checksums, branch protection, least-privilege permission review and an independent assessment of the privileged execution boundary.
