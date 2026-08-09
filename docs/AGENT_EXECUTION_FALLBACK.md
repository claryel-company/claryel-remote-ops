# Agent execution fallback contract

RemoteOps provides reusable safety contracts for bounded computer operations. Under ADR-0056 it may also provide the policy model used by a future desktop/computer-control fallback, but it does not become an unrestricted autonomous remote desktop or shell.

ADR-0055 remains the Recovery Control Plane. A desktop fallback never creates or bypasses node recovery ownership, leases or recovery state.

## Preference boundary

Desktop interaction is used only after an authoritative native API, Integration adapter and accepted browser-DOM path cannot satisfy the requested capability.

The calling control plane must provide the stable work/plan identity, requested capability, fallback reason, target scope, risk/approval state, idempotency identity and expected postcondition.

## Required desktop scope

An accepted desktop operation declares:

- allowed application/process identity;
- allowed window/title/accessibility scope;
- allowed interaction primitives;
- maximum action count and timeout;
- graphical-session and application-health prerequisites;
- before-state evidence;
- expected postcondition and readback method;
- unexpected-state stop rules;
- rollback, compensation or human-takeover path;
- audit/evidence destination.

## Privilege boundary

Desktop interaction never implies shell, sudo/administrator, secret-store, arbitrary filesystem or arbitrary process authority. Privileged operations still run through registered OS adapters.

Credentials and session secrets remain inside the private owner runtime. Public schemas and fixtures use only synthetic examples.

## Safety behavior

- fail closed on ambiguous target application/window state;
- do not guess through unexpected dialogs;
- do not bypass MFA, CAPTCHA, rate limits or platform security prompts;
- preserve one idempotency/correlation identity across retries;
- validate the postcondition independently when risk warrants it;
- require stronger approval for medium/high-risk UI mutation than for an equivalent deterministic native API.

## CLARYEL internal integration

CLARYEL Agent Fabric may use the public RemoteOps contract as one input to its internal execution-surface policy. Node Agent owns concrete local execution/capability registration, ADR-0055 owns recovery arbitration/state and Fleet owns private device placement/desired state. No private CLARYEL topology, credentials or owner state is added to this public repository.
