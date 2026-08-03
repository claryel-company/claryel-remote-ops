# User guide

> Product: CLARYEL RemoteOps
>
> Last scenario validation: 2026-08-03
>
> Status: public release candidate
>
> Canonical language: English

## The product in one sentence

CLARYEL RemoteOps is a free, open-source way to manage your own Windows, Linux or macOS computer by speaking or typing to an AI chat.

## What you can ask for

- install, update or remove software;
- change approved computer settings;
- check storage, memory, services, updates and security state;
- investigate common problems;
- apply an approved repair;
- verify the result and use rollback when the required health check fails.

## What you need to understand

### Your AI chat is the control surface

Describe the result in normal language. ChatGPT is the internally tested conversational path. Other AI chats have documented integration paths but remain untested with RemoteOps.

### RemoteOps is the safety layer

RemoteOps converts the request into a bounded plan. It does not give the AI an unrestricted shell.

### GitHub is a background technical mechanism

A private GitHub repository can keep computer-specific configuration history and approvals. It is not the primary user interface. Do not store passwords, private keys, personal documents, conversations, raw logs or backups in Git.

## The simplest safe path

1. **Prepare RemoteOps once.**
   Run the prerequisite check and create the private workspace.
2. **Open your AI chat.**
   Speak or type the desired result.
3. **Read the short plan.**
   Check the intended result, affected parts, risk and recovery path.
4. **Approve only when clear.**
   High-risk network, identity, storage, boot, remote-access or privilege changes require explicit approval.
5. **Receive a verified result.**
   RemoteOps runs health checks. A failed gate must use the declared recovery method.

## Prepare the workspace

### Linux or macOS

```bash
python3 src/remoteops.py doctor
python3 src/remoteops.py init --path "$HOME/.local/share/claryel-remoteops/state"
python3 src/remoteops.py status --path "$HOME/.local/share/claryel-remoteops/state"
```

### Windows PowerShell

```powershell
python src/remoteops.py doctor
python src/remoteops.py init --path "$env:LOCALAPPDATA\CLARYEL\RemoteOps\state"
python src/remoteops.py status --path "$env:LOCALAPPDATA\CLARYEL\RemoteOps\state"
```

The onboarding utility prepares and validates the owner-controlled configuration workspace. It does not expose general remote command execution.

## Operating-system status

| Platform | Status |
|---|---|
| Linux | Internally tested workflow; stable public evidence pending |
| macOS | Internally tested workflow; stable public evidence pending |
| Windows | Onboarding and schemas supported; privileged adapter and public rollback evidence pending |

## What stays private

- computer name, address and private topology;
- owner-specific configuration history;
- credentials, keys and recovery codes;
- documents, prompts and conversations;
- logs, telemetry, databases and backups.

## Common problems

| Symptom | Safe action |
|---|---|
| The plan contains an unregistered raw shell command | Reject it and request a schema-constrained plan |
| A secret appears in a change | Revoke the secret, remove it from history and investigate before continuing |
| You do not understand the impact | Do not approve; request a simpler explanation |
| Health checks fail | Stop further changes and use the declared rollback |
| Remote access is lost | Use the verified local or out-of-band recovery path |
| The AI chat is unavailable | Do not apply an unrecorded change; use the documented local recovery process |

## Localised help

Managed translations are available in `USER_GUIDES/locales/`. English remains authoritative when a translation is incomplete or ambiguous.
