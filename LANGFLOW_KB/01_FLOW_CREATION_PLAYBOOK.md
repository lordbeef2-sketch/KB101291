# Flow creation playbook: from natural language to a real Langflow graph

**Objective:** an LLM must produce an importable and version-valid `.json` flow or an executable `.py` LFX graph, not just suggestions. Target release `v1.13.2`.

## 1. Specify the contract
Capture: caller and trigger; example inputs/outputs; source systems; retrieval corpus and metadata; model/provider; tools and side effects; latency; persistence/memory/session isolation; deployment (IDE/LFX/API/MCP); credentials; failure paths; security; acceptance cases. If unspecified, choose a minimal, safe model-free prototype and mark assumptions.

## 2. Choose authoring path
**Path A (visual/export JSON):** Select an official 1.13.2 starter project JSON from `upstream-langflow/src/backend/base/langflow/initial_setup/starter_projects`. Copy it, preserve `data.nodes`/`data.edges` structure, unique node IDs and correct connection handles, adjust component templates using real catalog fields, then validate with `lfx validate`. Best for producing files users can import to the visual builder.

**Path B (programmatic LFX Python):** Build a `Graph` with `lfx.components` and execute via `lfx run`. Best when building from code in a tool-using local agent. Always confirm exact import symbols in tagged source and installed bundles. Not all Langflow database-backed state is available in standalone stateless LFX. Do not label a script as an exported UI flow JSON.

**Path C (full Langflow API):** Use `/api/v1/flows` management endpoints for create/import and `POST /api/v1/run/{flow_id}` for execution, with configured auth. If deploying to LFX, use its *distinct* `POST /flows/{flow_id}/run` API. Inspect the installed `/openapi.json` for the exact route and request schemas before integration.

## 3. Component selection and wiring
1. Retrieve per-component guide from `generated/component_guides/` and consult its authoritative source/docs.
2. Confirm input and output names, types, required/default fields, side effects, installable bundle and `tool_mode` support.
3. Design data type conversions deliberately: `Message` vs `Data` vs `DataFrame`/`Table` vs tool object. Use Parser/Type Convert or specific adapters only when the actual source permits.
4. Draw the actual typed graph and validate each edge: source node/output -> target node/input; source type compatible with accepted target types; no accidental cycles except supported Loop orchestration; no disconnected required path.
5. Use the **source of real exported edges** as a serialization template. Actual `sourceHandle` and `targetHandle` are structured/reactflow strings, NOT plain `"message"` and `"input_value"` unless the selected serializer specifies that. See `upstream-langflow/docs/docs/Flows/concepts-flows-import.mdx`.
6. Keep unique flow and node IDs, stable provenance and source version. Preserve flow metadata/position and explicit API-exposed fields where required.
7. Use global variables/connection references rather than literal secrets.

## 4. Proven construction examples
**Known-good starter baseline, no invented graph schema**:
```bash
# after recursive clone
cp "LANGFLOW_KB/upstream-langflow/src/backend/base/langflow/initial_setup/starter_projects/Simple Agent.json" ./Simple_Agent.json
lfx validate ./Simple_Agent.json
lfx requirements ./Simple_Agent.json -o requirements.txt
lfx run ./Simple_Agent.json --input-value "Hello" --format json
```
File path and runtime package must be verified after checkout. `lfx run` may require provider credentials; missing credentials are not graph-invalidity. For new deployments, install the appropriate bundles and exact Langflow/LFX versions.

**Programmatic LFX (from pinned official `lfx-run.mdx` example)**:
```python
import os
from lfx import components as cp
from lfx.graph import Graph

async def get_graph() -> Graph:
    chat_input = cp.ChatInput()
    agent = cp.AgentComponent()
    agent.set(
        model_name="gpt-4.1-mini",
        agent_llm="OpenAI",
        api_key=os.getenv("OPENAI_API_KEY"),
        input_value=chat_input.message_response,
    )
    chat_output = cp.ChatOutput().set(input_value=agent.message_response)
    return Graph(chat_input, chat_output)
```
This snippet illustrates the API, but the official tagged example uses an additional URL toolkit and explicit logging. Prefer its full code when running (see `docs/docs/Lfx/lfx-run.mdx`). Actual execution is not asserted here.

## 5. Flow recipes (every recipe must become a test case)
| Recipe | Graph concept | Must verify |
|---|---|---|
| Echo / transform | Chat Input -> transformation -> Chat Output | No model or credentials; exact output |
| Basic prompting | Chat Input -> Prompt -> LLM -> Chat Output | Prompt variables, model, auth, session ID |
| Agent + tools | Chat Input -> Agent (tool-mode component(s)) -> Chat Output | Tool descriptions, policy, failure cases |
| Conditional route | Chat Input -> If-Else -> branch A/B -> output | True, false, case sensitivity, loop guard |
| Retrieval RAG | File ingest -> Split Text/Parser -> embedding -> Knowledge Base ingest; separate query -> Knowledge Base retrieve -> LLM | Chunk IDs, retrieval hits, citations, no duplicate ingest |
| Long-term memory | Chat Input -> Agent + Memory Base / Message History -> Output | Tenant/session separation; persistence |
| Batch transform | Inputs -> Loop/Batch Run/Parser -> output | Item ordering, per-item failure, expected rows |
| External APIs | API Request / OpenAPI / MCP Tools -> parse -> output | Auth, SSRF/outbound restrictions, timeouts |
| Reusable subflow | Run Flow / Flow-as-Tool -> parent output | Child flow ID, nested error, trace |
| Human review | Agent or Human Input approval gate -> protected tool | No side effect before approved checkpoint |
| API service | Valid flow -> `lfx serve` or Langflow run endpoint | Auth, request/response contract, status codes |
| A2A/MCP | Agent/MCP server/client with project endpoint | Server auth, tools visibility, schema correctness |

## 6. Validation ladder
- **Level 0**: JSON or Python syntax parse; no secrets in checked-in artifact.
- **Level 1**: `lfx validate FLOW.json` (validate options with `lfx validate --help`); structural shape, orphan/reachability warnings.
- **Level 2**: Validate exact installed component registry and bundles.
- **Level 3**: Input/output edge type compatibility.
- **Level 4**: Required fields, provider credentials/variable references, missing connection wiring. Run `lfx validate FLOW.json --level 4` when supported.
- **Level 5**: Runtime execute with known input and assert output shape/content, session behavior, and correct external effects.
- **Level 6**: Malformed input, missing secret, timeout, tool failure, branch coverage, concurrent sessions, upgrade/reimport, API/MCP exposure and security boundary tests.

Source for validator levels: `src/lfx/src/lfx/cli/validate.py`, `lfx/cli/validation/`. No validation level guarantees functional logic by itself.

## 7. Repair loop
For each failure, record `run_id, Langflow version, flow hash, component, field, error, category`; inspect installed help, pinned implementation, docs, matching tests. Make one scoped change and rerun failed test plus regression tests. Never replay a previously ineffective modification with no new evidence.

## 8. Final deliverable
Flow JSON or LFX script + dependency lock/requirements + configuration template without secrets + example inputs/expected outputs + validation command output + runtime traces + limitations and deploy instructions. Mark unexecuted tests explicitly.

**Source pointers:** `docs/docs/Flows/concepts-flows-import.mdx`, `docs/docs/Lfx/lfx-run.mdx`, `docs/docs/Lfx/lfx-serve.mdx`, `docs/docs/Lfx/lfx-devops-sdk.mdx`, `src/backend/base/langflow/initial_setup/starter_projects/`, `src/lfx/src/lfx/cli/validation/`.
