# Privacy boundary

## Public repository

May contain reusable source, schemas, policies, synthetic examples, tests, release metadata and public documentation.

## Private desired-state repository

May contain owner-specific configuration, machine identifiers, group membership, approved rollout policy and references to secret identifiers. Keep access narrow and review changes.

## Never store in Git

- passwords, tokens, private keys and recovery codes;
- personal documents, photos, email or chat history;
- raw prompts or model conversations containing private information;
- service databases, telemetry, logs or backups;
- secret values embedded in configuration;
- unrestricted remote-access credentials.

## Local processing

Restricted personal or business data should remain local whenever possible. When an external AI provider is used, send only the minimum sanitised context required to draft a proposal. The proposal must not include secret values.

## Incident response

If private data enters public history, stop publication, revoke exposed credentials, preserve evidence, remove the data using an approved history-rewrite process, review downstream copies and publish an incident notice when required.
