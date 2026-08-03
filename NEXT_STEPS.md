# Next steps

## Current state

The repository contains the public product boundary, security model, schemas, safe onboarding CLI, validation, release plan and managed end-user guidance. Linux, macOS and ChatGPT operating paths are recorded as internally tested. Public reproducibility and a clean implementation export are not yet complete.

## Release gates

1. Change the GitHub repository visibility from private to public.
2. Complete reviewed clean export of the Linux and macOS execution adapters.
3. Publish synthetic installation, change, failure and rollback fixtures.
4. Record dated public evidence for Linux and macOS.
5. Run an independent security review focused on privilege boundaries, repository compromise and rollback integrity.
6. Publish signed release artifacts and checksums.
7. Validate the 20-language website and user-help paths.
8. Mark Claude, Gemini, Perplexity or Grok as tested only after repeatable RemoteOps evidence exists.

## Immediate implementation order

- P0: repository visibility, secret scan and branch protection;
- P0: public adapter clean export and provenance review;
- P0: deterministic risk policy and rollback integration tests;
- P1: signed installers and update channel;
- P1: accessibility and novice onboarding tests;
- P1: independent security assessment;
- P2: additional AI-provider compatibility validation.
