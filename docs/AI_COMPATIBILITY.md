# AI compatibility

## Principle

RemoteOps is provider-neutral. An AI system may draft and explain a proposal, but deterministic validation, approval, private desired state, privileged execution, health checks and rollback remain outside the model.

## Current matrix

| Provider | Technical path | RemoteOps evidence | Release label |
|---|---|---|---|
| ChatGPT | GitHub app or agent experience plus an approved write-capable workflow | Internal CLARYEL operating path tested | Tested internally |
| Claude | Claude Code, Claude Code GitHub Actions or an approved tool bridge | No repeatable RemoteOps test recorded | Not tested |
| Gemini | Gemini CLI and official GitHub Action or an approved tool bridge | No repeatable RemoteOps test recorded | Not tested |
| Perplexity | GitHub connector or MCP/tool integration where eligible | No repeatable RemoteOps test recorded | Not tested |
| Grok | Grok Build, compatible coding-agent CLI or approved tool bridge | No repeatable RemoteOps test recorded | Not tested |

## ChatGPT Free-plan conclusion

A universal GitHub management path is not guaranteed on the Free plan. OpenAI documents that app availability can vary by plan, region and experience, and the pricing comparison does not promise internal-source connectors on Free. RemoteOps therefore does not advertise write-capable GitHub administration as a Free-plan feature.

A Free user may still use ChatGPT for general explanation, file-based assistance or any GitHub app capability actually exposed to that account. Applying changes requires a separately approved write-capable mechanism with narrowly scoped permissions.

## Evidence rule

A provider becomes `tested` only when the same public scenario is repeated and recorded:

1. inspect desired state;
2. propose a schema-valid change;
3. create a reviewable Git change through an approved path;
4. obtain the required approval;
5. apply through the bounded executor;
6. pass health checks or complete rollback;
7. retain privacy-safe evidence.

Marketing language must match this matrix.
