# Langflow — LLM Flow Engineering Knowledge Base

**Upstream pin:** Langflow `v1.13.2` (2026-11-10), commit `8b42952d734de18e34c2838ff6c634efb1815878`.
**KB revision:** 2026-11-11. **Source anchored, NOT a claim of runtime/evaluation success.**

## Objective

Enable a base LLM, assisted by retrieval and a local Langflow/LFX runtime, to **design, build, validate, execute, debug, and maintain actual Langflow flows**. This is not merely an encyclopedia. The LLM must choose real components and ports, start with version-matched serialized templates, construct or modify flow JSON or an LFX Python graph, install required bundles, and pass validation.

## Corpus design

- **Full pinned upstream corpus**: [`upstream-langflow/`](upstream-langflow) is a Git submodule that pins the **whole** Langflow repo (source, docs, CLI code, API schemas, frontend, starter flows, tests, and provider/bundle implementations) to a specific commit. `git clone` alone does **not** populate submodule contents; use `--recurse-submodules`.
- **Machine-built, searchable reference**: [`scripts/build_corpus.py`](scripts/build_corpus.py) scans the pinned tree and produces per-component cards, CLI/API symbol maps, starter-flow examples, source hashes, and retrieval chunks in `generated/`.
- **Execution rails**: [`AGENTS.md`](AGENTS.md) defines the actions a base LLM must take to deliver verified flows rather than unsupported JSON.
- **Engineering playbooks**: see [source/commands](00_SOURCE_LEDGER.md), [build flows](01_FLOW_CREATION_PLAYBOOK.md), [component and CLI reference](02_COMPONENTS_AND_COMMANDS.md), [operations and evaluation](03_EVALS_SECURITY_VERSION.md).

This KB adds a module to `KB101291`; existing `3DS_KB` and `NI_KB` are preserved. **Only general-purpose public Langflow material belongs here.**

## Quick preparation

```bash
git clone --recurse-submodules https://github.com/lordbeef2-sketch/KB101291.git
cd KB101291
git submodule update --init --recursive
git -C LANGFLOW_KB/upstream-langflow rev-parse HEAD
# must be 8b42952d734de18e34c2838ff6c634efb1815878
python LANGFLOW_KB/scripts/build_corpus.py
```

Generated artifacts (local, deterministic with the same Python interpreter/source): `manifest.json`, `components.json`, `component_howtos.md`, `cli_symbols.json`, `api_routes.json`, `environment_variables.json`, `flow_examples.json`, `documents.jsonl`, `source_inventory.json`. These outputs are **not checked in by this initial write**; generate and ingest them. Coverage depends on successfully populating the submodule.

## LLM retrieval order

1. `AGENTS.md` + requested task + current installed Langflow/LFX version.
2. `01_FLOW_CREATION_PLAYBOOK.md` and `03_EVALS_SECURITY_VERSION.md` for build and validation contract.
3. Generated component cards, `flow_examples.json`, source citations.
4. Version-matched docs in `upstream-langflow/docs/docs`.
5. Original component class, CLI implementation, API OpenAPI spec, tests in pinned source.
6. Installed `--help`, installed components, actual flow export and runtime logs as the final authority.

A base LLM **alone** cannot certify that a flow runs. It needs a local validation/execution loop, installed components, and credentials for provider-backed tests. The corpus supplies sources and construction rules; runtime testing supplies proof.

## Update process

Keep the old pin and audit trail. Review Langflow upstream release notes and security advisories before upgrading; create a new versioned branch/checkpoint; change the gitlink to the reviewed tag; regenerate the corpus and run regression/evaluation tests; then merge. Never silently assume `main` upstream is the same as this pin.

Primary upstream: https://github.com/langflow-ai/langflow/releases/tag/v1.13.2
