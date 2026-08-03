# Create and connect your personal private repository

This guide creates the private configuration history for **your own computer**.
The repository belongs to your GitHub account. RemoteOps never makes it public,
never adds collaborators and never changes access without your explicit action.

## What “Private” means

A private GitHub repository is not visible to the public. Access is limited by
GitHub permissions to:

- you, the repository owner;
- collaborators or organisation members you explicitly authorize;
- GitHub Apps or OAuth applications you explicitly authorize;
- GitHub as the service operator, subject to its security, legal and operational
  controls.

Private does **not** mean that nobody can ever access the repository. A stolen
account, an over-permissioned application, an invited collaborator or a service
security incident can still create risk. Use a passkey or two-factor
authentication, grant access only to this repository and review access regularly.

GitHub documentation:

- https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration

## What belongs in the repository

Allowed:

- a private computer identifier chosen by you;
- approved configuration intent;
- package and service state without secret values;
- reviewable change plans and approval history;
- references to locally stored secret identifiers.

Never store:

- passwords, tokens, private keys or recovery codes;
- personal documents, photos, email or chat exports;
- raw logs, databases, telemetry or backups;
- unrestricted remote-access credentials;
- `.env`, `.pem`, `.key`, `.p12`, `.pfx`, password-manager or database files.

The generated `.gitignore` blocks common dangerous filenames. Run
`remoteops privacy-check` before every important push.

## Before you start

1. Create or sign in to your personal GitHub account.
2. Enable a passkey or two-factor authentication.
3. Install RemoteOps using the Windows, macOS or Ubuntu installer.
4. Open Terminal or PowerShell.
5. Find the private local workspace path printed by the installer.

Typical paths:

- Windows: `%LOCALAPPDATA%\CLARYEL\RemoteOps\state`
- macOS: `~/Library/Application Support/CLARYEL/RemoteOps/state`
- Ubuntu: `~/.local/share/claryel-remoteops/state`

## Recommended: automatic private creation

Install GitHub CLI from https://cli.github.com/ and authenticate:

```text
gh auth login
```

Choose:

1. `GitHub.com`;
2. `HTTPS`;
3. browser authentication;
4. only the permissions shown by GitHub that you understand.

Then create the private repository.

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

RemoteOps asks GitHub CLI to create the repository with `--private`, pushes the
initial non-secret configuration and then verifies that GitHub reports the
repository visibility as `PRIVATE`.

## Manual creation in the GitHub website

1. Open https://github.com/new.
2. In **Owner**, select your personal account.
3. Enter a name such as `remoteops-my-computer`.
4. Select **Private**.
5. Do not add a README, `.gitignore` or licence; RemoteOps already created them.
6. Click **Create repository**.
7. Copy the HTTPS repository URL.

Connect it only after confirming the page displays **Private**.

### Ubuntu

```bash
remoteops connect \
  --path "$HOME/.local/share/claryel-remoteops/state" \
  --repository-url "https://github.com/YOUR-ACCOUNT/remoteops-my-computer.git" \
  --confirm-private \
  --push
```

### macOS

```bash
remoteops connect \
  --path "$HOME/Library/Application Support/CLARYEL/RemoteOps/state" \
  --repository-url "https://github.com/YOUR-ACCOUNT/remoteops-my-computer.git" \
  --confirm-private \
  --push
```

### Windows PowerShell

```powershell
remoteops connect `
  --path "$env:LOCALAPPDATA\CLARYEL\RemoteOps\state" `
  --repository-url "https://github.com/YOUR-ACCOUNT/remoteops-my-computer.git" `
  --confirm-private `
  --push
```

When GitHub CLI is authenticated, RemoteOps independently checks the visibility
before pushing. Without GitHub CLI, the manual confirmation is recorded but the
visibility cannot be independently verified by the local tool.

## Verify privacy

Run after setup and after changing repository permissions.

### Ubuntu

```bash
remoteops privacy-check --path "$HOME/.local/share/claryel-remoteops/state"
```

### macOS

```bash
remoteops privacy-check --path "$HOME/Library/Application Support/CLARYEL/RemoteOps/state"
```

### Windows PowerShell

```powershell
remoteops privacy-check --path "$env:LOCALAPPDATA\CLARYEL\RemoteOps\state"
```

A successful result must show:

```json
{
  "ok": true,
  "visibility": "PRIVATE",
  "findings": []
}
```

## Check who and what has access

On the repository page:

1. Open **Settings**.
2. Open **Collaborators and teams** or **Manage access**.
3. Remove everyone who does not require access.
4. Review installed GitHub Apps and OAuth applications in your GitHub account.
5. Keep the repository private.
6. Do not enable public GitHub Pages for the private configuration repository.

## Disconnect immediately

Remove the local remote without deleting local configuration:

```text
git remote remove origin
```

Then revoke the application or collaborator in GitHub settings. Rotating or
revoking credentials is required if a token, key or recovery code was exposed.
