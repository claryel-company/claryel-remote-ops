# Privacy and network boundary

CLARYEL RemoteOps is designed around owner control and minimum disclosure. It
must not be marketed as communicating with no external systems because the
owner may deliberately use GitHub, an AI provider and software package sources.

## Local by default

Before a repository or AI provider is connected, the onboarding workspace is
local to the owner's computer.

RemoteOps does not intentionally upload:

- personal documents or photos;
- passwords, tokens, private keys or recovery codes;
- chat exports or browser profiles;
- raw logs, databases, telemetry or backups;
- unrestricted remote-access credentials.

## Owner-selected external services

| Service | When contacted | Data boundary |
|---|---|---|
| GitHub | Only when the owner creates, connects, pulls or pushes the personal private repository | Reviewed non-secret configuration and change history only |
| ChatGPT or another AI provider | Only when the owner connects and uses that provider | Minimum sanitized task context only |
| Operating-system package sources | When the owner approves installation or update of software | Package requests required for the approved operation |
| Time, certificate and update infrastructure | As required by the operating system and approved tools | Normal platform metadata governed by those tools |

RemoteOps does not add an advertising network, analytics tracker or unrelated
telemetry service to the onboarding utility or installers.

## Private GitHub repository

A private repository is hidden from the public internet through GitHub access
controls. It is accessible to the owner, explicitly authorized collaborators,
authorized applications and GitHub as the service operator. It is not a promise
of absolute invisibility or immunity from account compromise.

Required controls:

- passkey or two-factor authentication;
- repository visibility set to `Private`;
- only selected-repository application access;
- no unnecessary collaborators;
- periodic `remoteops privacy-check`;
- immediate credential revocation after suspected exposure.

## ChatGPT account control

The owner controls which OpenAI account is used, which app is connected and
which repository is authorized. ChatGPT app availability and permissions vary
by plan and experience. The owner should review Data Controls and disable
“Improve the model for everyone” when appropriate for a personal account.

RemoteOps cannot override the privacy, retention, legal or security policies of
GitHub, OpenAI or another chosen provider. Users must review those providers'
current terms and controls.

## Encryption wording

Use precise wording:

- HTTPS/TLS protects network transport to supported services;
- GitHub protects private repository access through its platform controls;
- local disk encryption such as BitLocker, FileVault or LUKS protects data at
  rest when enabled and correctly managed by the owner;
- encryption does not protect against a compromised account, unlocked device,
  malicious collaborator or incorrectly granted application permission.

Do not use unverifiable phrases such as “nobody can ever see it”, “zero data can
leak” or “military-grade/super-corporate encryption”.
