# CLARYEL RemoteOps

> Safe, reviewable remote computer management for Linux and macOS.

CLARYEL RemoteOps turns a plain-language request into a constrained configuration proposal, a reviewable Git change, a validated rollout and either a healthy result or an automatic rollback.

The project is designed for people who do not want to become system administrators. The default path is deliberately small:

1. Connect a private configuration repository.
2. Describe the result you want.
3. Review and approve the proposed change.
4. Let RemoteOps validate, apply, check and roll back when necessary.

## Status

**Public release candidate.** The operating pattern has been validated internally on Linux and macOS and with a ChatGPT-driven workflow. The public repository is being prepared as a clean, reusable release boundary. Public reproducibility evidence, packaged installers and independent security review remain release gates.

| Capability | Status |
|---|---|
| Linux operating path | Internally tested |
| macOS operating path | Internally tested |
| ChatGPT operating path | Internally tested |
| Claude path | Documented, not tested with RemoteOps |
| Gemini path | Documented, not tested with RemoteOps |
| Perplexity path | Documented, not tested with RemoteOps |
| Grok path | Documented, not tested with RemoteOps |

## The simple model

```text
plain-language request
        ↓
reviewable change plan
        ↓
private desired-state repository
        ↓
preflight + backup + approval
        ↓
controlled Linux or macOS adapter
        ↓
health checks
        ↓
success or automatic rollback
```

## Privacy boundary

The public repository contains only reusable code, schemas, synthetic examples, tests and documentation.

Your private repository or local storage contains machine identities, owner-specific desired state, private topology and operational history. Passwords, tokens, private keys, recovery codes, personal documents, prompts, conversations, telemetry and backups must never be committed to the public repository.

## Security principles

- No arbitrary AI-generated shell commands are applied directly.
- Every change is represented as a bounded, reviewable plan.
- High-risk changes require explicit approval.
- Configuration is backed up before mutation.
- Health checks run after activation.
- A failed health gate triggers rollback to the last known-good state.
- Secrets stay local or in a dedicated secret manager.
- Providers are replaceable; no AI service is the source of configuration truth.
- Public code and private owner state remain separate trust planes.

## ChatGPT and the Free plan

ChatGPT can connect to GitHub in eligible experiences and plans, but availability varies by plan, region and interface. A universal write-capable GitHub workflow must not be promised for the Free plan. Reading or analysing repositories may be available in some experiences; controlled writes require an approved write-capable app, coding agent, MCP/tool bridge, GitHub Action, CLI or equivalent mechanism with narrowly scoped permissions.

## Repository map

- [`ARCHITECTURE.md`](ARCHITECTURE.md) — system and trust boundaries.
- [`SECURITY.md`](SECURITY.md) — secure defaults and disclosure process.
- [`THREAT_MODEL.md`](THREAT_MODEL.md) — threats, mitigations and residual risks.
- [`docs/RELEASE_PLAN.md`](docs/RELEASE_PLAN.md) — public-release gates and sequence.
- [`docs/AI_COMPATIBILITY.md`](docs/AI_COMPATIBILITY.md) — tested and untested AI paths.
- [`USER_GUIDES/README.md`](USER_GUIDES/README.md) — canonical English user guide.
- [`USER_GUIDES/locales/`](USER_GUIDES/locales/) — managed end-user help in 20 languages.

## Website

- Project site: `https://remoteops.claryel.space`
- Repository: `https://github.com/claryel-company/claryel-remote-ops`

## Licence

Code is released under the Apache License 2.0. Documentation and managed localisation are released under CC BY-SA 4.0 unless a file states otherwise.
