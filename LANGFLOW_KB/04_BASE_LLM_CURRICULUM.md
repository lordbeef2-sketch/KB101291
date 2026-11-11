# Base-LLM competence curriculum and build/eval workbook

A base model should learn Langflow by retrieval and repeated **executed** tasks, not by stuffing every upstream file into its context. This corpus supports RAG; it is not a trained checkpoint or a substitute for an execution tool.

## Curriculum
**Unit 1 — Concepts & port types.** Identify flow, project, node, edge, Message/Data/Table/Tools, component templates, sessions, environment variables, and LFX vs Langflow. Explain required fields and type constraints from source.

**Unit 2 — Commands.** Install pinned version, list help, scaffold with `lfx init`, list templates (`lfx create --help`), validate, generate requirements, export, run/serve, and inspect API auth. Require exact command outputs.

**Unit 3 — Basic authoring.** Copy an official starter with `scripts/bootstrap_flow.py`, change only documented fields, validate, execute and compare expected output. Learn exported edge-handle serialization using actual JSON examples.

**Unit 4 — Conditional graphs.** Connect If-Else with both true/false branches and test routing, types and iteration limits.

**Unit 5 — Data and RAG.** Two independent flows: ingest with deterministic source IDs and retrieval with expected matches; test duplicate handling, metadata filters and no cross-tenant leakage. Target 1.13 SQLite-backed KB unless remote pgvector/OpenSearch explicitly selected.

**Unit 6 — Agents, tools, MCP, A2A.** Register tools with schema, restrict side effects, approve actions, handle tool errors and credentials; verify MCP project visibility and transport/auth.

**Unit 7 — API and deployment.** Choose full Langflow run endpoint vs standalone LFX server, assert 200/4xx shapes, mount volumes, protect admin editor, configure auth and secrets.

**Unit 8 — Migration/maintenance.** Upgrade 1.12 flows using version matched examples, catch retired components, preserve a rollback path, measure regressions.

## Starter list (source-anchored)
Official pinned `starter_projects/` includes: Basic Prompting, Simple Agent, Document Q&A, Knowledge Retrieval, Hybrid Search RAG, Vector Store RAG, Memory Chatbot, Multi Agent Flow, Research Translation Loop, Custom Component Generator, Deep Research Agent, and more. `bootstrap_flow.py --list` enumerates every actual JSON artifact.

## Model prompt / repeatable task
"Given the user flow request, output (1) requirements and data contracts, (2) verified component selection with paths, (3) exact version-matched starter source, (4) changed nodes/edges and the generated JSON/Python artifact, (5) required packages/vars without secret values, (6) static validation results, (7) runtime tests and actual outputs, (8) errors/revisions, (9) deployment and rollback notes. **Never claim importable/working unless tested.**"

## Practical local commands
```bash
# from repository root, after clone --recurse-submodules:
python LANGFLOW_KB/scripts/build_corpus.py
python LANGFLOW_KB/scripts/bootstrap_flow.py --list
python LANGFLOW_KB/scripts/bootstrap_flow.py --starter "Basic Prompting" --output ./flows/basic.json
lfx validate ./flows/basic.json --level 4
lfx requirements ./flows/basic.json -o ./flows/requirements.txt
# NOTE: --execute will run any flow-side effects; use only after review:
python LANGFLOW_KB/scripts/validate_and_report.py ./flows/basic.json --level 4
python LANGFLOW_KB/scripts/validate_and_report.py ./flows/basic.json --execute --input-value "Hello" --report ./local-validation.json
```

## Suggested retrieval queries
- "What exact accepted input and output handles does the Knowledge Base 1.13 component use?"
- "Show 1.13.2 official starter JSON containing an Agent and Chat Output."
- "Can LFX serve access Langflow database-backed Memory Base?"
- "Where in source is lfx validate level 4 implemented?"
- "How do I create a custom component with typed input, multiple outputs and safe error reporting?"
- "Find official CLI command syntax and options for lfx export/push/requirements."
- "Find deprecated 1.12 Chroma nodes and new 1.13 migration path."
- "What is different between POST /api/v1/run/id and POST /flows/id/run?"

## Pass/fail rubric
For each module record: `flow_version`, exact flow path/hash, `artifact_created`, `syntax_pass`, `lfx_validate_pass`, `dependencies_resolved`, `runtime_pass`, `negative_test_pass`, `security_review_pass`, `evidence_log_path`. A response with no artifact is a fail. A flow with no runtime test is **unverified**, not a pass. Track failures by category from `AGENTS.md`.
