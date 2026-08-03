# Windows adapter boundary

Windows is part of the CLARYEL RemoteOps product interface. The public onboarding workspace and Windows plan schemas are supported in the release candidate.

The privileged Windows execution adapter is not yet represented as production-ready. Before that claim, the public adapter must provide reproducible installation, approved change, health-check failure and rollback evidence.

## Required implementation rules

The clean Windows adapter must:

- expose registered actions rather than unrestricted PowerShell or Command Prompt execution;
- use Windows Package Manager or another approved package mechanism for declared software actions;
- use documented Windows service and configuration interfaces;
- request only the minimum required privileges;
- preserve Microsoft Defender, firewall, BitLocker, SmartScreen and account protections unless a separately governed change explicitly requires otherwise;
- prepare an appropriate recovery mechanism before mutation;
- apply explicit timeouts;
- run independent health checks;
- roll back automatically when the declared recovery method supports it;
- produce privacy-minimised audit evidence.

## Planned public action families

- package installation, update and removal;
- registered service-state management;
- approved startup and energy-policy configuration;
- read-only health and inventory checks;
- approved update-policy actions;
- bounded repair operations with declared verification and recovery.

## Prohibited shortcut

Do not implement the Windows adapter as an AI-accessible arbitrary PowerShell endpoint. Conversational output must first become a schema-valid plan and pass deterministic policy, approval and recovery checks.
