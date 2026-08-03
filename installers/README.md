# Install CLARYEL RemoteOps

Choose the installer for the computer you own and administer.

## Windows 10 or 11

1. Download `install-windows.ps1`.
2. Open PowerShell as your normal user.
3. Run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\install-windows.ps1
```

The process-scoped execution-policy change ends when that PowerShell window is
closed. The installer does not disable Defender, UAC, BitLocker or SmartScreen.

## macOS

1. Download `install-macos.sh`.
2. Open Terminal in the download directory.
3. Run:

```bash
chmod +x install-macos.sh
./install-macos.sh
```

The installer does not disable Gatekeeper, FileVault, SIP or macOS privacy
controls.

## Ubuntu

1. Download `install-ubuntu.sh`.
2. Open Terminal in the download directory.
3. Run:

```bash
chmod +x install-ubuntu.sh
./install-ubuntu.sh
```

If Python, Git or curl is missing, the installer asks before using `apt` and
`sudo` to install those prerequisites.

## What every installer does

1. downloads the public RemoteOps source into your user profile;
2. creates a command named `remoteops`;
3. creates a private local workspace owned by your user account;
4. writes privacy-safe starter files and a restrictive `.gitignore`;
5. checks the installation;
6. prints the next command for creating your personal private repository.

## What no installer does

- it does not create a public repository;
- it does not add collaborators;
- it does not connect ChatGPT without your action;
- it does not upload personal files, secrets, chats, raw logs or backups;
- it does not disable operating-system security;
- it does not install an unrestricted remote shell.

Continue with [`../docs/PRIVATE_REPOSITORY_SETUP.md`](../docs/PRIVATE_REPOSITORY_SETUP.md).
