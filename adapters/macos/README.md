# macOS adapter boundary

The macOS operating path has been tested internally. The public privileged adapter is not yet exported in this release-candidate baseline.

The clean public adapter must:

- declare supported macOS and Apple Silicon versions;
- use platform-supported service and configuration mechanisms;
- request only necessary privileges;
- preserve FileVault, Gatekeeper, SIP and privacy controls;
- create a restorable snapshot before mutation;
- run independent health checks;
- roll back automatically on failure;
- produce privacy-minimised audit evidence.

Do not weaken macOS security controls to simplify installation.
