# CLARYEL RemoteOps

> Free voice-first management of your own Windows, Ubuntu/Linux or macOS computer through an AI chat you choose.

CLARYEL RemoteOps turns a spoken or typed request into a bounded plan, shows
what will change, asks for approval when required and checks the result.

## Start in four clicks

1. **Choose your computer:**
   - [Windows installer](installers/install-windows.ps1)
   - [macOS installer](installers/install-macos.sh)
   - [Ubuntu installer](installers/install-ubuntu.sh)
2. **Create your personal Private repository:**
   [`docs/PRIVATE_REPOSITORY_SETUP.md`](docs/PRIVATE_REPOSITORY_SETUP.md)
3. **Connect ChatGPT safely:**
   [`docs/CHATGPT_SETUP.md`](docs/CHATGPT_SETUP.md)
4. **Verify privacy:** run `remoteops privacy-check`.

The detailed beginner guide is [`START_HERE.md`](START_HERE.md).

## Your ownership model

### Your computer

RemoteOps is installed inside your user profile. The onboarding utility does not
install an unrestricted remote shell and does not disable Defender, UAC,
BitLocker, Gatekeeper, FileVault, SIP, LUKS or other operating-system security.

### Your personal private repository

You create a separate repository in **your own GitHub account** and select
**Private**. RemoteOps never makes it public, never adds collaborators and never
changes visibility without your explicit action.

A private repository is hidden from the public. Access is controlled by GitHub
and is limited to you, people or applications you explicitly authorize, and
GitHub as the service operator. It is not an honest guarantee that nobody can
ever access it: account compromise, excessive app permissions, collaborators or
provider incidents remain possible risks.

The repository stores only reviewed non-secret configuration and change history.
It must never contain passwords, tokens, private keys, recovery codes, personal
files, chats, raw logs, databases or backups.

### Your ChatGPT account

You decide whether to connect ChatGPT, which GitHub repository it may access and
which permissions to grant. Select **Only select repositories** and choose only
your private RemoteOps repository. Review ChatGPT Data Controls and turn off
**Improve the model for everyone** when appropriate for your account.

GitHub-app availability and write capability vary by ChatGPT plan and mode. A
read-only connection can inspect and explain; it cannot apply changes. Any
write-capable workflow must be separately authorized and restricted to the
single private repository.

## Exact communication boundary

RemoteOps is local before you connect anything. It contacts external systems
only for actions you explicitly choose:

- GitHub when you create, connect, pull or push your private repository;
- ChatGPT or another AI provider when you connect and use it;
- package sources when you approve software installation or updates;
- normal operating-system certificate, time and update infrastructure.

The onboarding utility and installers add no advertising tracker or unrelated
analytics service. They do not intentionally upload personal files, secrets,
chat exports, raw logs, databases or backups.

See [`docs/PRIVACY_AND_NETWORK.md`](docs/PRIVACY_AND_NETWORK.md).

## Install

### Windows 10 or 11

Download [`install-windows.ps1`](installers/install-windows.ps1), open
PowerShell in the download folder and run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\install-windows.ps1
```

### macOS

Download [`install-macos.sh`](installers/install-macos.sh), open Terminal in the
download folder and run:

```bash
chmod +x install-macos.sh
./install-macos.sh
```

### Ubuntu

Download [`install-ubuntu.sh`](installers/install-ubuntu.sh), open Terminal in
the download folder and run:

```bash
chmod +x install-ubuntu.sh
./install-ubuntu.sh
```

Every installer:

1. downloads the public RemoteOps application into your user profile;
2. creates the `remoteops` command;
3. creates a private local workspace;
4. writes a restrictive `.gitignore` and privacy instructions;
5. checks prerequisites and installation;
6. prints the next command for creating your personal private repository.

## Create the private repository automatically

Install and authenticate GitHub CLI, then run the command for your system.

### Ubuntu

```bash
remoteops connect \
  --path "$HOME/.local/share/claryel-remoteops/state" \
  --create-private remoteops-my-computer
```

### macOS

```bash
remoteops connect \
  --path "$HOME/Library/Application Support/CLARYEL/RemoteOps/state" \
  --create-private remoteops-my-computer
```

### Windows PowerShell

```powershell
remoteops connect `
  --path "$env:LOCALAPPDATA\CLARYEL\RemoteOps\state" `
  --create-private remoteops-my-computer
```

The command uses GitHub CLI `--private`, pushes the initial non-secret files and
then checks that GitHub reports the repository visibility as `PRIVATE`.

## Verify privacy

```text
remoteops privacy-check --path YOUR-PRIVATE-WORKSPACE
```

A successful check requires:

```json
{
  "ok": true,
  "visibility": "PRIVATE",
  "findings": []
}
```

The check verifies visibility through authenticated GitHub CLI and scans tracked
files for common secret-key, credential, database, log and backup patterns.

## What you can request

- install, update or remove approved software;
- change approved computer settings;
- check storage, memory, services, updates and system health;
- diagnose and repair bounded problems;
- verify the result and use the declared recovery path when a check fails.

AI output remains an untrusted proposal. Arbitrary AI-generated shell or
PowerShell commands are not the product's safety boundary.

## Current support evidence

| Operating system | Current public status |
|---|---|
| Linux/Ubuntu | Workflow internally tested; stable public adapter evidence pending |
| macOS | Workflow internally tested; stable public adapter evidence pending |
| Windows | Onboarding, installers and schemas available; privileged adapter evidence pending |

## Documentation

- [`START_HERE.md`](START_HERE.md) — beginner setup.
- [`installers/README.md`](installers/README.md) — installer instructions.
- [`docs/PRIVATE_REPOSITORY_SETUP.md`](docs/PRIVATE_REPOSITORY_SETUP.md) — personal private GitHub repository.
- [`docs/CHATGPT_SETUP.md`](docs/CHATGPT_SETUP.md) — repository-scoped ChatGPT setup.
- [`docs/PRIVACY_AND_NETWORK.md`](docs/PRIVACY_AND_NETWORK.md) — exact external-service boundary.
- [`SECURITY.md`](SECURITY.md) and [`THREAT_MODEL.md`](THREAT_MODEL.md) — security model.
- [`USER_GUIDES/locales/`](USER_GUIDES/locales/) — managed help in 20 languages.

## Licence

Code is Apache-2.0. Documentation and managed localisation are CC BY-SA 4.0
unless a file states otherwise.
