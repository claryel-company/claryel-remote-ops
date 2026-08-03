# Start here: install, create your private repository and connect ChatGPT

This is the shortest complete setup for a person who does not want to learn
system-administration commands.

## What you are creating

You will have three owner-controlled parts:

1. **Your computer** — Windows, Ubuntu/Linux or macOS.
2. **Your personal private GitHub repository** — created in your account and
   hidden from the public.
3. **Your ChatGPT account** — connected only when you choose, with access limited
   to the single private repository.

RemoteOps is the public open-source safety layer between the conversation and
the computer. It does not make your repository public, add collaborators or
silently connect an AI provider.

## Important honest privacy statement

The repository is private from the public, not invisible to the GitHub service.
Only you, explicitly authorized people or applications, and GitHub as the
service operator can access it through GitHub permissions. Protect the account
with a passkey or two-factor authentication and authorize only this repository.

ChatGPT and GitHub are external services. RemoteOps contacts them only when you
explicitly connect and use them. Software installation may contact package
sources you approve. The installers add no advertising tracker or unrelated
analytics service and do not intentionally upload personal files, passwords,
keys, chats, raw logs, databases or backups.

## Step 1 — choose your installer

### Windows 10 or 11

1. Download [`installers/install-windows.ps1`](installers/install-windows.ps1).
2. Open the Downloads folder.
3. Right-click inside the folder and open PowerShell or Terminal.
4. Run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\install-windows.ps1
```

The temporary execution-policy setting ends when the window closes. The
installer does not disable Defender, UAC, BitLocker or SmartScreen.

### macOS

1. Download [`installers/install-macos.sh`](installers/install-macos.sh).
2. Open Terminal and move to the Downloads folder.
3. Run:

```bash
chmod +x install-macos.sh
./install-macos.sh
```

The installer does not disable Gatekeeper, FileVault, SIP or privacy controls.

### Ubuntu

1. Download [`installers/install-ubuntu.sh`](installers/install-ubuntu.sh).
2. Open Terminal in the Downloads folder.
3. Run:

```bash
chmod +x install-ubuntu.sh
./install-ubuntu.sh
```

The installer asks before using `sudo apt` for missing Python, Git or curl.

## Step 2 — secure your GitHub account

1. Create or sign in to your personal GitHub account.
2. Enable a passkey or two-factor authentication.
3. Do not share the account.
4. Do not add collaborators unless they genuinely need access.

## Step 3 — create your personal private repository

The easiest method uses GitHub CLI.

1. Install GitHub CLI from https://cli.github.com/.
2. Run:

```text
gh auth login
```

3. Choose GitHub.com, HTTPS and browser authentication.
4. Run the command printed by the installer.

Typical commands:

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

### Windows

```powershell
remoteops connect `
  --path "$env:LOCALAPPDATA\CLARYEL\RemoteOps\state" `
  --create-private remoteops-my-computer
```

RemoteOps creates the repository with private visibility, pushes only the
starter non-secret configuration and asks GitHub to confirm that visibility is
`PRIVATE`.

A manual website path is documented in
[`docs/PRIVATE_REPOSITORY_SETUP.md`](docs/PRIVATE_REPOSITORY_SETUP.md).

## Step 4 — verify privacy

Run the command for your system.

### Ubuntu

```bash
remoteops privacy-check --path "$HOME/.local/share/claryel-remoteops/state"
```

### macOS

```bash
remoteops privacy-check --path "$HOME/Library/Application Support/CLARYEL/RemoteOps/state"
```

### Windows

```powershell
remoteops privacy-check --path "$env:LOCALAPPDATA\CLARYEL\RemoteOps\state"
```

Continue only when the result shows:

```json
{
  "ok": true,
  "visibility": "PRIVATE",
  "findings": []
}
```

## Step 5 — connect ChatGPT

1. Open ChatGPT.
2. Open **Settings > Apps**.
3. Select the GitHub app when it is available in your plan and experience.
4. Sign in to the GitHub account that owns the private repository.
5. Choose **Only select repositories**.
6. Select only `remoteops-my-computer`.
7. Review requested permissions before approving.
8. Open **Settings > Data Controls** and review **Improve the model for
   everyone**. Turn it off when appropriate for your account.

Detailed instructions:
[`docs/CHATGPT_SETUP.md`](docs/CHATGPT_SETUP.md).

## Step 6 — send the first safe request

```text
Use only my selected private RemoteOps repository.
Never request, expose or store passwords, tokens, private keys, recovery codes,
personal files, raw logs, databases or backups.
Read the repository instructions first.
Explain every change in ordinary language, state the risk and recovery path,
and do not execute arbitrary shell or PowerShell commands directly.
Start by checking the repository and explaining the current computer profile.
```

## Step 7 — understand the current release status

RemoteOps currently provides the installers, private workspace, repository
setup, privacy verification, schemas and controlled workflow.

- Linux and macOS workflows are internally tested; stable public adapter and
  rollback evidence is still being completed.
- Windows onboarding and installers are available; stable privileged Windows
  execution evidence is still being completed.

Do not treat the release candidate as an unrestricted remote-administration
agent. The safety model requires registered actions, explicit approval for
important changes, health checks and recovery.

## The rule that prevents most mistakes

Never approve a change you do not understand. Ask the AI to explain the effect,
risk, verification and rollback in simpler language.
