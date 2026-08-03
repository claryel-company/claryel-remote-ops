# CLARYEL RemoteOps

> Free voice-first computer management for Windows, Linux and macOS through your preferred AI chat.

CLARYEL RemoteOps turns ordinary spoken or typed requests into clear, reviewable and recoverable computer changes.

You can ask an AI chat to:

- install, update or remove software;
- change approved computer settings;
- check storage, memory, services, updates and system health;
- diagnose and repair common problems;
- verify the result and return to the last working state when a health check fails.

You do not need to memorise terminal commands or search through operating-system menus.

## What you use

### 1. An AI chat

Speak or type what you want the computer to do. ChatGPT is the internally tested conversational path. Claude, Gemini, Perplexity and Grok have documented connection paths but remain untested with RemoteOps.

### 2. CLARYEL RemoteOps

The free and open-source safety layer that prepares the plan, classifies risk, asks for approval when necessary, records the change, checks the result and controls rollback.

That is the visible user model.

<details>
<summary>Small technical note</summary>

A private GitHub repository can be used behind the scenes to keep a reviewable history of computer-specific configuration. GitHub is a technical storage, review and approval mechanism; it is not the RemoteOps user interface. Passwords, keys, documents, conversations, logs and backups must not be stored there.

</details>

## The simple path

1. Set up RemoteOps once.
2. Open the AI chat you prefer.
3. Say or type the result you want.
4. Read one short plan explaining impact, risk and recovery.
5. Approve the action when it is clear.
6. RemoteOps applies the registered action and checks the computer.
7. The result is accepted only after health checks pass; otherwise rollback is used.

```text
voice or text request
        ↓
plain-language plan
        ↓
your approval when required
        ↓
controlled action
        ↓
health check
        ↓
success or rollback
```

## Current operating-system status

| Operating system | Current public status |
|---|---|
| Linux | Operating workflow internally tested; public privileged adapter evidence is a release gate |
| macOS | Operating workflow internally tested; public privileged adapter evidence is a release gate |
| Windows | Onboarding workspace and public schemas supported; privileged execution adapter and reproducible public evidence are in preparation |

The product interface targets Windows, Linux and macOS. Stable support claims require dated public installation, change, health-check and rollback evidence for the relevant operating-system version.

## AI status

| AI chat | RemoteOps status |
|---|---|
| ChatGPT | Internally tested |
| Claude | Documented, not tested with RemoteOps |
| Gemini | Documented, not tested with RemoteOps |
| Perplexity | Documented, not tested with RemoteOps |
| Grok | Documented, not tested with RemoteOps |

## Why it is safer than direct AI commands

- AI output is treated as a proposal, not as trusted executable code.
- Arbitrary AI-generated shell commands are not applied directly.
- Every change uses a bounded, reviewable plan.
- High-risk changes require explicit approval.
- Backup and recovery requirements are declared before mutation.
- Health checks run after the action.
- A failed health gate triggers rollback to the last known-good state.
- Secret values and personal data stay outside public source and configuration history.

## Start here

Read [`START_HERE.md`](START_HERE.md) for the shortest non-technical introduction.

The current release-candidate onboarding utility can check prerequisites and create a private desired-state workspace:

```bash
python3 src/remoteops.py doctor
python3 src/remoteops.py init --path "$HOME/.local/share/claryel-remoteops/state"
python3 src/remoteops.py status --path "$HOME/.local/share/claryel-remoteops/state"
```

On Windows, choose a private local directory appropriate for your account, for example:

```powershell
python src/remoteops.py doctor
python src/remoteops.py init --path "$env:LOCALAPPDATA\CLARYEL\RemoteOps\state"
python src/remoteops.py status --path "$env:LOCALAPPDATA\CLARYEL\RemoteOps\state"
```

These commands prepare and validate the owner-controlled workspace. They do not expose a general remote shell and do not claim that every privileged operating-system action is already included in the public release candidate.

## Repository map

- [`START_HERE.md`](START_HERE.md) — the simplest product explanation.
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — system and trust boundaries.
- [`SECURITY.md`](SECURITY.md) — secure defaults and disclosure process.
- [`THREAT_MODEL.md`](THREAT_MODEL.md) — threats, mitigations and residual risks.
- [`docs/RELEASE_PLAN.md`](docs/RELEASE_PLAN.md) — public-release gates and sequence.
- [`docs/AI_COMPATIBILITY.md`](docs/AI_COMPATIBILITY.md) — tested and untested AI paths.
- [`USER_GUIDES/README.md`](USER_GUIDES/README.md) — canonical English user guide.
- [`USER_GUIDES/locales/`](USER_GUIDES/locales/) — managed end-user help in 20 languages.

## Website

- Project site: `https://remoteops.claryel.space`
- Source repository: `https://github.com/claryel-company/claryel-remote-ops`

## Licence

Code is released under the Apache License 2.0. Documentation and managed localisation are released under CC BY-SA 4.0 unless a file states otherwise.
