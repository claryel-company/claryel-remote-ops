# User guide

> Product: CLARYEL RemoteOps
>
> Guide owner: RemoteOps maintainers
>
> Last scenario validation: 2026-08-03
>
> Status: release-candidate
>
> Canonical language: English

## What RemoteOps does

RemoteOps helps you manage your own Linux or macOS computer without learning every system-administration command. You describe the result, review a simple plan, approve it and receive a verified result or an automatic rollback.

## The simplest safe path

1. **Create a private configuration repository.**
   Keep your computer-specific settings there. Do not store passwords, tokens, private keys or personal documents in Git.
2. **Run the safety check.**
   The check confirms the supported operating system, Git access and local directory permissions.
3. **Connect the private repository.**
   RemoteOps records the repository as desired-state storage; it does not copy your files into the public project.
4. **Describe the result you want.**
   Use ChatGPT or another supported proposal surface. Ask for a plan, not a raw command.
5. **Review the plan.**
   Check the affected services, risk level, backup, expected result and rollback.
6. **Approve only when the impact is clear.**
   High-risk network, identity, storage, boot or remote-access changes require explicit approval.
7. **Verify the result.**
   RemoteOps runs health checks. A failed gate must restore the last known-good state.

## Safe onboarding command

```bash
python3 src/remoteops.py doctor
python3 src/remoteops.py init --path "$HOME/.local/share/claryel-remoteops/state"
python3 src/remoteops.py status --path "$HOME/.local/share/claryel-remoteops/state"
```

The public release-candidate CLI prepares and validates the private desired-state workspace. Public privileged adapters remain gated until clean export and security review are complete.

## What stays private

- computer name, address and topology;
- owner-specific configuration;
- credentials, keys and recovery codes;
- documents, prompts and conversations;
- logs, telemetry, databases and backups.

## AI compatibility

| Provider | RemoteOps status | Important limitation |
|---|---|---|
| ChatGPT | Internally tested | GitHub availability and write capability vary by plan, region and experience |
| Claude | Documented, not tested | Requires an approved Claude Code, GitHub Action or tool path |
| Gemini | Documented, not tested | Requires an approved Gemini CLI, GitHub Action or tool path |
| Perplexity | Documented, not tested | Connector availability depends on plan; permissions must be reviewed carefully |
| Grok | Documented, not tested | Requires an approved coding-agent, CLI or tool path |

## Common problems

| Symptom | Safe action |
|---|---|
| The plan contains a raw shell command | Reject it and request a schema-constrained plan |
| A secret appears in a diff | Revoke the secret, remove it from history and investigate before continuing |
| You do not understand the impact | Do not approve; request a plain-language explanation |
| Health checks fail | Stop further changes and use the declared rollback |
| Remote access is lost | Use the verified local or out-of-band recovery path |
| GitHub is unavailable | Do not apply unrecorded configuration; wait or use the documented offline recovery process |

## Localised help

Managed translations are available in `USER_GUIDES/locales/`. English remains authoritative when a translation is incomplete or ambiguous.
