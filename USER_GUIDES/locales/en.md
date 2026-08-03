# CLARYEL RemoteOps — installation and private setup

RemoteOps manages your own Windows, Ubuntu/Linux or macOS computer through an AI chat you choose.

## 1. Install

- [Windows installer](../../installers/install-windows.ps1)
- [macOS installer](../../installers/install-macos.sh)
- [Ubuntu installer](../../installers/install-ubuntu.sh)

Run the downloaded installer. It installs RemoteOps in your user profile, creates a private local workspace and does not disable operating-system security.

## 2. Create your personal Private repository

Install GitHub CLI, run `gh auth login`, then run the command printed by the installer:

```text
remoteops connect --path YOUR-WORKSPACE --create-private remoteops-my-computer
```

The repository is created in your GitHub account with `Private` visibility. RemoteOps does not make it public or add collaborators.

Private means hidden from the public. Access is still possible for you, people or applications you authorize, and GitHub as the service operator. Protect the account with a passkey or two-factor authentication.

Never store passwords, tokens, keys, recovery codes, personal files, chats, raw logs, databases or backups in Git.

## 3. Verify privacy

```text
remoteops privacy-check --path YOUR-WORKSPACE
```

Continue only when the result shows `"ok": true`, `"visibility": "PRIVATE"` and no findings.

## 4. Connect ChatGPT

1. Open **ChatGPT > Settings > Apps > GitHub**.
2. Choose **Only select repositories**.
3. Select only `remoteops-my-computer`.
4. Review permissions before approving.
5. Review **Settings > Data Controls > Improve the model for everyone**.
6. Never paste secrets or personal files into the chat.

GitHub-app availability and write capability vary by ChatGPT plan and mode. A read-only connection cannot apply changes.

## Communication boundary

RemoteOps contacts GitHub only when you connect or synchronize your private repository, ChatGPT only when you choose to use it, and package sources only for software operations you approve. The installers add no advertising tracker or unrelated analytics service.

Detailed guides: [private repository](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [privacy and network](../../docs/PRIVACY_AND_NETWORK.md).
