# Linux adapter boundary

The Linux operating path has been tested internally. The public privileged adapter is not yet exported in this release-candidate baseline.

The clean public adapter must:

- support declared Linux versions only;
- expose registered actions rather than arbitrary shell;
- use narrow privilege rules;
- create a restorable snapshot before mutation;
- apply explicit timeouts;
- run independent health checks;
- roll back automatically on failure;
- produce privacy-minimised audit evidence.

Do not mark this directory production-ready until public integration tests reproduce installation, change and rollback from a fresh machine.
