# Evaluation, troubleshooting, operations, security, upgrades

## Release gate: 1.13.2 (Nov 10, 2026)
1. Official packages, Docker, tagged source default `LANGFLOW_AUTO_LOGIN=false`: require credentials and nontrivial `LANGFLOW_SUPERUSER_PASSWORD` + persistent `LANGFLOW_SECRET_KEY`; verify login before exposing access.
2. 1.13 local Knowledge/Memory moves from Chroma to SQLite/sqlite-vec; retired Chroma/Local DB nodes must be replaced. For local legacy migration: backup app DB **and** knowledge-base directory; ensure local filesystem, around 4x free space, single writer during migration, and ability to recover. Do not casually enable multiple workers during migration. Chroma Cloud stores require separate migration. Docs: `docs/docs/Develop/knowledge-storage-upgrade.mdx`.
3. Only after flows are valid and tested should API serving, MCP, A2A, external endpoints or deployment be enabled.
4. 1.13.2 includes security fixes related to flow permissions, authorization, outbound OpenAPI requests, MCP visibility, and custom Python code authoring. Review upstream advisories and release notes; do not equate version number with invulnerability.

## Production architecture
- Prefer PostgreSQL for the Langflow application's production relational DB, not an unmanaged SQLite app DB serving multiworker production.
- Use TLS, reverse proxy/API gateway, non-public editor, explicitly scoped accounts, least-privilege custom code, ingress/egress restrictions, tight CORS, SSRF protection, approval before side effects, protected secrets, trace redaction, per-tenant session isolation.
- For multiworker event/build coordination, inspect queue support and Redis configuration for the installed version; Python local asyncio queue is not shared.
- Backup: application data/DB, `~/.langflow/knowledge_bases` or `LANGFLOW_KNOWLEDGE_BASES_DIR`, flow JSON, global variable metadata, environment references, connection prerequisites.
- Distinguish server telemetry/traces from Langflow flow outputs; set cost and retention limits. Avoid logging raw model prompts, provider tokens, API keys or personal source data.

## Troubleshooting decision tree
| Failure | Diagnostic / corrective direction |
|---|---|
| Component missing | Compare export node type against installed bundle registry; install matched provider extension; restart; retry validate |
| Edge type mismatch | Retrieve `inputs`/`outputs`, expected handles and Data/Message/Table types; use documented conversion component |
| Run stuck/looping | Inspect iteration guard and data routing, `If-Else` default route; stop and inspect events |
| API 401/403 | Distinguish API key vs session auth, role, flow permissions, recent 1.13 auth defaults |
| API 404 | Confirm full Langflow vs LFX service, exact path/prefix, flow ID, project visibility |
| Secret/variable unresolved | Inspect environment precedence, global variables and connection references without revealing values |
| RAG no results | Ingest status, same KB/provider, same embedding model, identifier, chunk text, metadata filters, search query |
| RAG migration failing | Check local disk, DB + KB backup, free space, migration status; do not delete originals |
| MCP tools not appearing | Check registered project, endpoint, client auth, visibility, tool schema, compatible transport |
| Custom code blocked | Require proper admin authoring privilege; do not bypass security policy |
| Streaming/multiworker inconsistent | Inspect queue/backend event coordination and shared Redis configuration |
| Flow JSON import invalid | Export a known-good 1.13 flow and diff serialization, node IDs, template fields and edge handles |

## Evaluation manifest for a base LLM
Every evaluation case must have a natural-language user request, selected component set, a canonical starter source/flow JSON or LFX script, negative tests, expected output types and exact local commands. Cases:
1. Model-free passthrough/string transform (must run without a model provider).
2. Prompt template and LLM with correctly referenced API key.
3. If-Else both branches, max iterations.
4. Local file ingestion to knowledge base + retrieval with deterministic fixture.
5. Session-separated message history.
6. Agent with safe tool + intentional tool exception.
7. Reusable Run Flow.
8. Authenticated REST LFX serve and Langflow run.
9. MCP tool discovery with authenticated project.
10. Custom component with typed inputs/outputs and broken-input rejection.
11. Flow JSON export/import roundtrip.
12. 1.12 -> 1.13 retired component detection/migration warnings.

**Score** = fully passed tests / total tests actually executed; record separate `not_run` and `skipped`. Do not score missing credentials as success. Keep flow, command, installed version, output, and sanitized logs as evidence.

## Self-improvement loop
Generate corpus -> sample component how-tos -> compose evaluation flows -> validate -> execute in local sandbox -> capture failure IDs -> patch recipes/guide with source line references -> rerun -> record revision/hash. Never change upstream gitlink without release review.

## Important limitations
Without executing against a real installed Langflow/LFX instance and known provider credentials, this KB can supply source-accurate instructions and candidate flows, but **cannot certify all generated flows as functional**. Static class/document extraction and Git-submodule pin are not tests.

Sources: https://docs.langflow.org/release-notes, https://docs.langflow.org/knowledge-storage-upgrade, `docs/docs/Deployment/security.mdx`, `docs/docs/Deployment/deployment-tweaks-policy.mdx`, `docs/docs/Lfx/lfx-devops-sdk.mdx`.
