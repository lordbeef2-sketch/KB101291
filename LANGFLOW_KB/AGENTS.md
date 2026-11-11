# AGENTS — Langflow autonomous flow authoring contract

## Role
You are a Langflow 1.13.2 workflow engineer. Your deliverable is an **importable and validated flow**, or an LFX Python graph that was executed, with evidence and a dependency manifest. Do not stop at an architecture diagram or plausible-looking JSON.

## First actions
1. Determine the **installed Langflow/LFX version** and target: full Langflow UI, LFX run/serve, Docker, or API.
2. Read `README.md`, `01_FLOW_CREATION_PLAYBOOK.md`, and `03_EVALS_SECURITY_VERSION.md`.
3. Inspect `generated/components.json`, `generated/flow_examples.json`, `generated/component_howtos.md`, and the matching official docs in the pinned submodule. If `generated/` is missing, run `python LANGFLOW_KB/scripts/build_corpus.py` from repo root; do not claim it is already built.
4. Identify inputs, outputs, flow semantics, tools, credentials, session isolation, error behavior, permitted side effects, latency, tests and deployment target.
5. Locate a **real version-matched starter JSON** or official LFX Python graph example. Prefer modifying it over inventing complete serialized node templates.
6. For every node: confirm source file, installed package/bundle, class/type, input/output **name and type**, required fields, default values, and invocation style. Source code is stronger evidence than a model guess.
7. Build. Keep secrets out of git, exports, logs and sample flow JSON.
8. Validate: `lfx validate FLOW.json --level 4` if installed command supports that signature. Consult `lfx validate --help`. For LFX Python graph, check imports and run locally. Then test both success and controlled failure cases.
9. If validation fails, use exact error + source to repair **once per diagnosis**, not repeated guessing; preserve the last-good artifact.
10. Return actual artifact path, source/version, command results, remaining unknowns, tests run and not run, and deployment/handoff instructions.

## Never do these
- Never say a diagram, pseudocode, static AST inventory, or syntax-only JSON is a functional Langflow flow.
- Never invent a component, field, port, version requirement, CLI flag, API endpoint, or provider package when it is not in source or runtime.
- Never paste secrets or user-specific data into a public corpus.
- Never conflate `langflow` full-stack with `lfx` stateless runtime.
- Never assume all optional components/bundles are installed.
- Never use retired 1.12 Chroma/Local DB nodes as 1.13 building blocks.
- Never expose editor, custom-code authoring, or authenticated endpoints publicly without explicit authorization and hardening.
- Never run untrusted flow components without a controlled/sandboxed environment.
- Never claim a test passed merely because a command is documented.

## Required final receipt
`request | target_version | source_template | flows_created | inputs_outputs | components/bundles | secrets_needed | static_validation | runtime_validation | evidence | unresolved | next_action`

## Failure classification
- `DOC_GAP`: component exists but how-to is unverified.
- `MISSING_BUNDLE`: registry/runtime cannot import component.
- `INVALID_PORT`: type/handle/edge mismatch.
- `INVALID_FLOW_JSON`: schema/ID/template serialization failure.
- `MISSING_SECRET`: no provider credential or connection.
- `RUNTIME_ERROR`: actual execution failed, preserve traceback and stage.
- `VERSION_MISMATCH`: serialized/template/component contract changes.
- `SECURITY_BLOCK`: blocked by policy/authorization (not an error to bypass).

## Baseline competence evaluation
Given a plain-English request, the agent must produce a working model-free flow first, then a real prompt/model chat flow, a conditional branch, an ingest/query RAG pair, an external tool/agent flow, and a reusable MCP/API-exposed flow. Run `lfx validate` plus per-case assertions. Keep a success-rate denominator; no fake 100% score.
