# All components and commands — source-backed operating map

## All components: authoritative retrieval
All shipped first-party classes and bundled provider sources reside in the pinned gitlink. Run `python LANGFLOW_KB/scripts/build_corpus.py` to produce an AST inventory and **one guide per component**, with class name, source file, resolved display name/description, inputs, outputs, field defaults, method links, matching official documentation and confidence. Source extraction is static; dynamic field changes and optional imports must be confirmed against the installed runtime.

**Categories (not exhaustive):** inputs/outputs; ChatInput/ChatOutput; text; prompt; language models; agents; embeddings; tools and toolkits; Knowledge Base ingest/retrieve; Memory Base; Message History; files and data loaders; splitting; parsers; data operations; Python Interpreter; URL/API Request; SQL; vector stores; Loop; Batch Run; If-Else; Run Flow; Webhook; Human Input; MCP Tools; A2A; cloud integrations; custom Python components; per-provider plugins.

**Every component guide must answer**: name, feature/intent, source+docs, Python class, installable bundle and dependencies, environment/connection configuration, required/optional fields with exact names/types, outputs with exact names/types/method, connection examples, usage snippet or official tutorial, failure modes, version/legacy status, and security implications. If not in official source, use `UNKNOWN`; no invented settings.

Component operations:
- **If-Else**: compares `input_text` to `match_text` using equals/not equals/contains/starts with/ends with/regex; outputs `true_result`/`false_result`. Default route when iteration cap reached should be explicit. See `docs/docs/Components/if-else.mdx`.
- **Knowledge Base**: select Ingest or Retrieve. Ingest expects `input_df` and column metadata/embedding; Retrieve accepts `search_query`, `top_k`, metadata filter. Output is a table; store selection/provider is part of KB configuration. See `docs/docs/Components/knowledge-base.mdx`.
- **Custom Python**: subclass `lfx.custom.Component` (or current `lfx.custom.custom_component.component.Component` depending on API), define `inputs = [...]`, `outputs = [Output(name=...,method=...)]`, implement return method. `LANGFLOW_COMPONENTS_PATH` categories need `__init__.py`; do not collide input names with method names. Source: `docs/docs/Components/components-custom-components.mdx`.
- **LFX vs full Langflow**: LFX runs stateless/no application database, with separate dependency/bundle packaging. Stateful storage components may not behave as they do in the full Langflow server.

## Langflow CLI (full app)
```bash
langflow --help
langflow run --help
langflow admin --help
langflow api-key --help
langflow migration --help
langflow copy-db --help
```
Canonical full app manual: `docs/docs/Develop/configuration-cli.mdx`. `langflow api-key` only works under auto-login; **1.13 defaults auto-login OFF**. For credential-backed users use authenticated Settings or API. CLI values take precedence over env vars; boolean switch supports `--no-...`.

## LFX command families (runtime + DevOps SDK)
```bash
lfx --help
lfx run --help
lfx serve --help
lfx prewarm --help
lfx observability doctor --help
lfx extension --help
lfx extension list
lfx init --help
lfx login --help
lfx create --help
lfx validate --help
lfx requirements --help
lfx status --help
lfx push --help
lfx pull --help
lfx export --help
```
Extra entrypoint: `lfx-mcp` (see `docs/docs/Lfx/lfx-mcp.mdx`). Source extraction scans all Typer decorators and command implementations; exact flags appear in installed `--help` and pinned docs. Do not infer flags from a Python function name alone.

### Verified documented examples
```bash
lfx init demo-project
lfx create --help       # discover supported starter/template flags first
lfx validate flows/Simple_Agent.json
lfx requirements flows/Simple_Agent.json -o requirements.txt
lfx run flows/Simple_Agent.json --input-value "Hello" --format json
lfx serve flows/Simple_Agent.json --env-file .env
lfx export flows/Simple_Agent.json -o flows/Simple_Agent.normalized.json
lfx status
lfx pull
lfx push
```
Remote push/pull/login require `.lfx/environments.yaml` and credentials. **No automatic remote writes** as part of data generation.

## APIs
- Full Langflow: `POST /api/v1/run/{FLOW_ID_OR_NAME}` authenticated with `x-api-key` (check target build).
- Webhook: `POST /api/v1/webhook/{FLOW_ID}`; verify per-flow/auth policy.
- Flow/project create/list/export/import, user management, audit, monitoring: inspect pinned OpenAPI/docs and live `/openapi.json`.
- Workflow API v2: `POST /api/v2/workflows` (Beta, version-dependent).
- LFX server: `POST /flows/{flow_id}/run` (not the same URL prefix as full Langflow).
- MCP project endpoint pattern: `/api/v1/mcp/project/{project_id}/streamable` (verify project visibility and auth); A2A route versions vary.
- For API POSTs, confirm actual request and response models; `session_id`, `tweaks`, API key, and named input fields are not interchangeable across surfaces.

## Static vs live inventory
The generator creates `generated/cli_symbols.json` and `generated/api_routes.json` from every matching source file. These may include internal methods, handlers and routes not enabled in a target deployment. A real server's `/openapi.json` and CLI `--help` are required to produce the **actual operational command index**, with options and signatures.

Source docs for full CLI and API: `docs/docs/Develop/configuration-cli.mdx`, `docs/docs/Lfx/lfx-overview.mdx`, `docs/docs/Lfx/lfx-devops-sdk.mdx`, `docs/docs/API-Reference/`.
