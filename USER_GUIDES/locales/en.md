# CLARYEL RemoteOps — simple guide

RemoteOps helps you manage your own Linux or macOS computer without memorising administration commands.

## Four steps

1. **Connect** a private configuration repository.
2. **Describe** the result you want in plain language.
3. **Approve** the clear change plan after checking impact, risk, backup and rollback.
4. **Verify** the health result. A failed check must restore the last known-good state.

## Keep private

Never put passwords, tokens, private keys, recovery codes, personal files, prompts, conversations, logs or backups in the public repository. Computer-specific configuration belongs in your private repository; secret values stay in local secret storage.

## AI status

ChatGPT is internally tested with the CLARYEL operating path. Claude, Gemini, Perplexity and Grok are documented but not tested with RemoteOps. GitHub access in ChatGPT Free is not guaranteed and write-capable control is not advertised as a universal Free-plan feature.

## Safe rule

If you do not understand a proposed change, do not approve it. Ask for a simpler explanation and a visible rollback path.
