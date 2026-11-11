# Sources, provenance and completeness

## Current pinned release
- Official release: https://github.com/langflow-ai/langflow/releases/tag/v1.13.2 (2026-11-10).
- Tag commit: `8b42952d734de18e34c2838ff6c634efb1815878`.
- Full upstream source: `LANGFLOW_KB/upstream-langflow` (**git submodule**, NOT a standalone copy of files).
- Published docs: https://docs.langflow.org/ ; pinned docs source: `upstream-langflow/docs/docs`.
- Source CLI implementation: `upstream-langflow/src/lfx/src/lfx/cli` and `upstream-langflow/src/backend/base/langflow/cli`.
- Core components: `upstream-langflow/src/lfx/src/lfx/components`.
- Separate provider bundles: `upstream-langflow/src/bundles`.
- Backend APIs: `upstream-langflow/src/backend/base/langflow/api`; docs/OpenAPI: `upstream-langflow/docs/openapi`.
- Reference examples: `upstream-langflow/src/backend/base/langflow/initial_setup/starter_projects`.
- Official tests: upstream test directories and CI workflows.

## Source-of-truth levels
**A** = deployed version's `--help`, `/openapi.json`, installed component registry and proven test runs.
**B** = pinned tag's source, release notes, matching docs, example JSON and tests.
**C** = this generated/static extraction; inspect dynamic fields at runtime.
**D** = old KB prose and untested LLM inference, not authoritative.

The extractor collects **all relevant first-party files** and marks provenance; it cannot prove optional third-party installations. Official component docs may be missing for some classes. Mark those `howto_source=code_only` and do not invent provider-specific setups. Redact secrets before ingestion.

## Critical 1.13 delta vs 1.12
- Default packaged authentication now requires sign-in (`LANGFLOW_AUTO_LOGIN=false`). Set a secure superuser password and protect keys.
- New local Knowledge Base and Memory Base storage is **SQLite/sqlite-vec**, replacing local Chroma. Chroma and Local DB components are retired. Chroma Cloud not automatically supported.
- Back up both application database and knowledge base directory BEFORE first 1.13 start. See https://docs.langflow.org/knowledge-storage-upgrade .
- Release adds audit logs, reusable connections and concurrent editing protection.
- 1.13.2 release notes include fixes involving MCP access, flow/event permissions, outbound request policy, restricted custom code, document identity preservation, parser types, and KB migration. Security review must use actual release notes and advisories.
- Custom Python authoring now requires administrator privileges by default (verify instance policy).
- Full LFX/Langflow command/route inventory must be versioned from the installed runtime; source paths are not an availability guarantee.

## Historical KB
Previous September 2026 Langflow System Digest covered 1.12.x. Preserve it externally as history; do not copy internal or potentially private Drive text into a public repo.

## Completeness accounting
1. **All first-party source and docs pinned**: yes, via a gitlink (available only after recursive clone).
2. **All first-party components enumeratable**: yes, via static AST extraction, with dynamic omissions flagged.
3. **All actual installed commands/flags validated here**: no; requires target interpreter's CLI help.
4. **All optional provider component how-tos fully authored**: no; reference upstream bundled docs/source and flag uncovered cases.
5. **All flows runtime-validated on user's machine**: no; run local eval suite after install.

This distinction prevents a base LLM mistaking coverage of files for verified operational mastery.
