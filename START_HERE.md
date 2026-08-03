# Start here

## What is CLARYEL RemoteOps?

CLARYEL RemoteOps is a free, open-source way to manage your own Windows, Linux or macOS computer through a conversation with an AI chat.

You speak or type the result you want. RemoteOps turns it into a clear plan, checks the risk, asks for approval when needed and verifies the computer after the change.

## What can I ask for?

Examples:

- “Install the applications I need for work.”
- “Remove unused software without deleting my documents.”
- “Keep this computer updated and tell me when something fails.”
- “Check memory, storage and running services.”
- “Configure the computer for maximum performance.”
- “Fix this problem and return to the previous state if the repair does not work.”

## What do I need?

### An AI chat

Use an AI chat that can participate in the documented RemoteOps workflow. ChatGPT is the internally tested conversational path.

### RemoteOps

RemoteOps is the free safety and execution layer. It converts the conversation into a bounded plan instead of giving the AI an unrestricted remote shell.

That is all a normal user needs to understand.

<details>
<summary>What happens behind the scenes?</summary>

A private GitHub repository can keep the configuration history and approval record. GitHub is not the control screen. It is a technical version-history mechanism used by the safe workflow.

Never store passwords, private keys, personal documents, conversations, raw logs or backups in Git.

</details>

## How does one request work?

1. You say what you want.
2. The AI explains the intended result.
3. RemoteOps creates a structured plan.
4. You see important impact and risk.
5. A recovery path is prepared.
6. You approve the action when required.
7. A registered operating-system action runs.
8. Health checks confirm success or trigger rollback.

## Is it ready for every system action?

Not yet. This is a public release candidate.

- Linux and macOS operating workflows are internally tested, with public reproducibility evidence still required for stable support.
- Windows onboarding and schemas are available, while the privileged Windows adapter and public rollback evidence are still being prepared.

RemoteOps must not claim stable operating-system support before the relevant public evidence exists.

## Prepare a workspace

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

These commands prepare the private configuration workspace. They do not grant arbitrary remote control and do not disable operating-system security.

## The most important rule

Do not approve a change you do not understand. Ask the AI to explain it in simpler language and show the recovery path.
