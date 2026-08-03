# Public release plan

## Release objective

Publish a free, reusable and security-reviewed RemoteOps release that a non-specialist can install on a minimally configured Linux or macOS computer, connect to a private desired-state repository and operate through a simple reviewed workflow.

## Release sequence

### 1. Establish the public boundary

- public repository and Apache-2.0 licence;
- English canonical technical documentation;
- 20-language managed end-user help;
- synthetic examples only;
- full-history secret scan;
- public/private provenance review.

### 2. Export the tested implementation

- clean Linux adapter;
- clean macOS adapter;
- deterministic change-plan validator;
- risk policy;
- preflight and backup controller;
- health checks and rollback controller;
- local privileged service with a minimal allowlist.

### 3. Package the novice path

- one-command signed installer for each supported operating system;
- guided private-repository connection;
- four-step user interface: connect, describe, approve, verify;
- advanced settings behind progressive disclosure;
- accessible error and recovery guidance.

### 4. Prove safety and repeatability

- fresh Linux installation test;
- fresh macOS installation test;
- network-change rollback test;
- service failure test;
- invalid plan rejection test;
- secret-leak prevention test;
- lost-provider and lost-GitHub recovery test;
- signed evidence bundle with timestamps and hashes.

### 5. Release

- signed tag and artifacts;
- checksums and software bill of materials;
- security advisory process;
- compatibility matrix;
- website and repository cross-links;
- public limitations and known issues.

## Version gates

### `0.1.0-rc1`

Documentation, schemas, safe onboarding CLI, localisation and public/private boundary.

### `0.1.0-rc2`

Clean Linux and macOS adapters with integration tests and rollback evidence.

### `1.0.0`

Independent security review complete, signed installers published, reproducible tests green and novice onboarding validated.

## Success criteria

A new user can understand the trust model, prepare a private workspace and identify exactly what is tested without reading internal architecture. A production release requires a complete safe change cycle from request through rollback using only public artifacts.
