# User guide

> Product: CLARYEL RemoteOps
>
> Status: public release candidate
>
> Canonical language: English

## The result

Install RemoteOps on your own Windows, Ubuntu/Linux or macOS computer, create a
personal **Private** repository in your GitHub account, authorize only that
repository in ChatGPT and manage approved computer changes through ordinary
voice or text requests.

## The three things you own and control

1. **Your computer.** RemoteOps is installed in your user profile and does not
   disable operating-system security.
2. **Your private repository.** You create it in your GitHub account. RemoteOps
   does not make it public or add collaborators.
3. **Your ChatGPT account.** You decide whether to connect it, which repository
   it can access and which permissions to grant.

A private repository is hidden from the public, but GitHub remains the service
operator. Access can also be granted to people or applications you authorize.
Use a passkey or two-factor authentication and select only this repository.

## Install

- Windows: [`../installers/install-windows.ps1`](../installers/install-windows.ps1)
- macOS: [`../installers/install-macos.sh`](../installers/install-macos.sh)
- Ubuntu: [`../installers/install-ubuntu.sh`](../installers/install-ubuntu.sh)

Complete command-by-command instructions are in
[`../START_HERE.md`](../START_HERE.md).

## Create the private repository

The recommended command is:

```text
remoteops connect --path YOUR-WORKSPACE --create-private remoteops-my-computer
```

It requires authenticated GitHub CLI. RemoteOps creates the repository with
private visibility, pushes only the non-secret starter configuration and checks
that GitHub reports `PRIVATE`.

Manual creation and platform-specific commands:
[`../docs/PRIVATE_REPOSITORY_SETUP.md`](../docs/PRIVATE_REPOSITORY_SETUP.md).

## Verify privacy

```text
remoteops privacy-check --path YOUR-WORKSPACE
```

Continue only when the output shows:

```json
{
  "ok": true,
  "visibility": "PRIVATE",
  "findings": []
}
```

The check verifies repository visibility through authenticated GitHub CLI and
scans tracked files for common secret, key, database, log and backup patterns.

## Connect ChatGPT

1. Open **ChatGPT > Settings > Apps**.
2. Connect GitHub when available in your plan and experience.
3. Choose **Only select repositories**.
4. Select only your private `remoteops-my-computer` repository.
5. Review requested permissions before approving.
6. Review **Settings > Data Controls > Improve the model for everyone**.
7. Never paste secrets or personal files into the chat.

Detailed guide:
[`../docs/CHATGPT_SETUP.md`](../docs/CHATGPT_SETUP.md).

## First safe request

```text
Use only my selected private RemoteOps repository.
Do not request, expose or store passwords, tokens, private keys, recovery codes,
personal files, raw logs, databases or backups.
Explain every change, risk, verification and recovery path in ordinary language.
Do not execute arbitrary shell or PowerShell commands directly.
Start by reading the repository instructions and explaining the current profile.
```

## External-service boundary

RemoteOps is local before you connect anything. It contacts:

- GitHub only when you create, connect, pull or push your private repository;
- ChatGPT or another AI provider only when you connect and use it;
- package sources only when you approve software installation or updates;
- normal operating-system certificate, time and update infrastructure.

The onboarding tool and installers add no advertising tracker or unrelated
analytics service and do not intentionally upload personal files, passwords,
keys, chats, raw logs, databases or backups.

Exact wording and limitations:
[`../docs/PRIVACY_AND_NETWORK.md`](../docs/PRIVACY_AND_NETWORK.md).

## What can be requested

- install, update or remove approved software;
- change approved computer settings;
- check storage, memory, services, updates and system health;
- diagnose bounded problems;
- verify results and use the declared recovery path.

## Current status

| Platform | Status |
|---|---|
| Linux/Ubuntu | Workflow internally tested; stable public adapter evidence pending |
| macOS | Workflow internally tested; stable public adapter evidence pending |
| Windows | Installer, onboarding and schemas available; privileged adapter evidence pending |

Do not treat the release candidate as an unrestricted remote shell. AI output is
a proposal until deterministic validation and required approval pass.

## Localised help

Managed translations are available in `USER_GUIDES/locales/`. English remains
authoritative when a translation is incomplete or ambiguous.
