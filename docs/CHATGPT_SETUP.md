# Connect ChatGPT to your private RemoteOps repository

ChatGPT is an external service chosen and controlled through your OpenAI
account. RemoteOps does not create a ChatGPT account, change your account
settings or silently authorize repository access.

## Before connecting

1. Finish [`PRIVATE_REPOSITORY_SETUP.md`](PRIVATE_REPOSITORY_SETUP.md).
2. Run `remoteops privacy-check` and require `"ok": true`.
3. Confirm the repository contains no passwords, keys, personal files, raw logs
   or backups.
4. Decide whether ChatGPT needs read-only analysis or a separately approved
   write-capable agent workflow.

## Connect the GitHub app

Availability varies by ChatGPT plan, region and experience.

1. Open ChatGPT.
2. Open **Settings**.
3. Open **Apps**.
4. Find **GitHub** and select **Connect**.
5. Sign in to the GitHub account that owns your private RemoteOps repository.
6. When GitHub asks which repositories the application may access, choose
   **Only select repositories**.
7. Select only your personal private repository, for example
   `remoteops-my-computer`.
8. Review every requested permission before accepting.
9. Do not grant access to all repositories unless you deliberately need it.

Official OpenAI guide:
https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt

## Data Controls

For a personal ChatGPT account, review:

1. **Settings**;
2. **Data Controls**;
3. **Improve the model for everyone**.

Turn it off when you do not want new conversations used to improve general
models. Your plan or managed workspace may have different controls.

Official OpenAI guide:
https://help.openai.com/en/articles/7730893-data-controls-faq

## First safe prompt

Use a request like this:

```text
Use only my selected private RemoteOps repository.
Do not request, expose or store passwords, tokens, private keys, recovery codes,
personal files, raw logs, databases or backups.
Read the repository instructions first.
For every requested computer change:
1. explain the result in ordinary language;
2. create a bounded change plan;
3. state the risk and affected components;
4. state the recovery and rollback path;
5. ask for approval when required;
6. do not execute arbitrary shell or PowerShell commands directly;
7. verify the result after the approved action.
Start by reading README.md, START_HERE.md, PRIVACY.md and desired-state.json.
```

## What ChatGPT may receive

Only the minimum sanitized context required for the task:

- desired package or service state;
- non-secret computer profile;
- sanitized health summaries;
- bounded change plans;
- verification results without private content.

## What ChatGPT must not receive

- passwords, tokens, private keys or recovery codes;
- personal documents, photos, email or chat exports;
- complete home-directory listings;
- browser profiles, cookies or session databases;
- raw logs containing personal content;
- backups or unrestricted remote credentials.

## Read versus write

A GitHub connection may be read-only in some ChatGPT experiences. Reading and
explaining the repository does not automatically provide permission to write,
open Pull Requests or apply computer changes.

A write-capable workflow must be separately available, explicitly authorized
and restricted to the single private repository. RemoteOps still treats every
AI result as an untrusted proposal until deterministic checks and required
approval pass.

## Disconnect

You can disconnect GitHub from ChatGPT in **Settings > Apps**. Also review and
revoke the corresponding application authorization in GitHub settings when you
no longer need it.
