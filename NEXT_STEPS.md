# Next steps

## Current state

The repository is public and presents RemoteOps as a free voice-first computer-management product for Windows, Linux and macOS.

The public release candidate contains:

- the conversational product model;
- a novice `START_HERE.md` guide;
- Windows, Linux and macOS desired-state and change-plan schemas;
- a safe onboarding CLI that can create workspaces on all three platforms;
- bounded OS adapter contracts with no general shell API;
- deterministic risk, health and rollback architecture;
- architecture, security and threat-model documentation;
- validation, tests and managed end-user guidance.

Linux, macOS and ChatGPT operating paths are recorded as internally tested. Windows onboarding is supported, while privileged Windows execution and reproducible public rollback evidence remain incomplete.

ADR-0056 additionally uses RemoteOps as a reusable safety-contract source for lower-preference desktop/computer-control fallback. Concrete private node execution remains outside this public repository. ADR-0055 remains the Recovery Control Plane and is not replaced by the desktop fallback contract.

## Release gates

1. Complete reviewed clean export of the Linux and macOS execution adapters.
2. Implement the bounded Windows adapter without an unrestricted PowerShell endpoint.
3. Publish synthetic installation, approved change, failure and rollback fixtures for all declared platforms.
4. Record dated public evidence for operating-system versions that receive stable-support claims.
5. Run an independent security review focused on privilege boundaries, repository compromise, AI prompt injection and rollback integrity.
6. Publish signed installers, checksums and a software bill of materials.
7. Validate the complete 20-language voice-first website and user-help paths.
8. Mark additional AI-chat providers as tested only after repeatable RemoteOps evidence exists.

## P1 — reusable desktop/computer-control fallback contract

Implement and test the public policy/schema layer described in `docs/AGENT_EXECUTION_FALLBACK.md`.

Acceptance requires synthetic evidence that a caller can provide:

- stable work/plan and idempotency identity;
- explicit reason why API/integration/browser paths are insufficient;
- target application/window allowlist;
- bounded action set and timeout;
- risk/approval state;
- before-state evidence and expected postcondition;
- safe stop on unexpected UI state;
- rollback/compensation or human-takeover path.

Desktop interaction must not grant shell, administrator/sudo, arbitrary filesystem or secret-store authority by implication. Recovery-required work must use ADR-0055 recovery state/leases.

## Immediate implementation order

- P0: Linux and macOS public adapter clean export and provenance review;
- P0: Windows registered-action adapter for packages, services and read-only health checks;
- P0: deterministic risk policy and rollback integration tests;
- P0: one genuinely simple signed installer per operating system;
- P1: novice voice-request and approval usability tests;
- P1: public bounded desktop-interaction schema and synthetic fixtures;
- P1: independent security assessment;
- P1: signed update channel and recovery documentation;
- P2: additional AI-chat compatibility validation.
