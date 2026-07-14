# QUERY RAILS

<!--KB_RAIL_CONTROL ordinal=3 required_state=CORPUS_READY next=RAILS/03_OUTPUT_CONTRACT.md -->

Opening this document without a valid full-corpus completion certificate is a protocol failure. Return to `AGENTS.md`.

## RAIL SELECTION

Choose exactly one primary rail from the requested product and execution surface. Add secondary rails only when the stated cross-check requires them.

| rail | primary control and evidence roots | mandatory cross-check |
|---|---|---|
| NI LabVIEW G and VI Scripting | `FULL_SYSTEM_DIGEST/00_FULL_SYSTEM_DIGEST.md`; `FULL_SYSTEM_DIGEST/NI_LABVIEW/PROGRAMMING_REFERENCE/`; `FULL_SYSTEM_DIGEST/NI_LABVIEW/USER_MANUAL/` | exact node, property, method, event, connector pane, type, ownership, and error behavior |
| NI driver and product APIs | `FULL_SYSTEM_DIGEST/NI_ECOSYSTEM/00_MACHINE_ROUTING.md`; matching `BUNDLES/` record | exact requested language surface plus product/driver concept record |
| NI Python | `FULL_SYSTEM_DIGEST/PYTHON_3_12_13/`; matching `NI_ECOSYSTEM/OSS_INTERFACES/` record | NI signature/source plus Python 3.12 runtime behavior |
| NI C, C++, CVI, C#, .NET, REST, gRPC, CLI | matching NI bundle and OSS interface record | language match, calling order, types, lifecycle, cleanup, and version |
| 3DS Java plugin/OpenAPI | `3DS_FULL_SYSTEM_DIGEST/00_TRUTH_RAILS.md`; exact `CAMEO_JAVA_OPENAPI_<release>/`; matching `NOMAGIC_DOCS/SPACES/DEVG*` | exact target-version class/member plus transaction, session, lifecycle, and cleanup workflow |
| 3DS macro or in-product script | matching Developer Guide and product space | exact scripting engine, supported language, versioned API surface, and security boundary |
| 3DS REST, Teamwork Cloud, or Simulation | `CURRENT_AUTHORITATIVE_SOURCES/`; matching product space | exact method, path, schema, authentication, transaction, and error contract |
| SysML v1/UAF/UPDM/DataHub | matching official product space and Java OpenAPI | exact profile, stereotype, metaclass, diagram, migration, or integration identity |
| SysML v2/KerML/Systems Modeling API | `OMG_SYSML_V2_AND_KERML_SPECS/`; `SYSTEMS_MODELING_OFFICIAL_REPOSITORIES/` | formal grammar/semantic identity plus commit-pinned official example or service definition |
| Legacy evidence | matching `LEGACY_PACK/` record | may supplement but never override exact official current/versioned evidence |

## VERSION LOCK

- Resolve product, release, execution surface, and language before selecting symbols.
- For NI, prefer matching 2024+ records; use legacy or NXG only when requested or required for migration.
- For 3DS, never combine Java OpenAPI, plugin metadata, JVM, REST, or model semantics across release lines without identifying the dependency. If no release is specified, target 2026x Refresh1 and say so.
- A current-shared page without explicit release evidence remains `current-shared`; do not invent version precision.

## EVIDENCE WALK

1. Read the selected corpus routing/truth control completely.
2. Resolve the exact symbol, endpoint, grammar production, VI, property, method, class, enum, error, or concept.
3. Read the complete primary evidence records containing that identity.
4. Read the complete mandatory secondary records.
5. Reconcile version, lifecycle, transaction, authentication, privileges, destructive effects, cleanup, and rollback.
6. Reject unsupported names or behavior instead of filling gaps from model memory.
7. Keep the exact repository-relative evidence paths for the response trace.

The one permitted next control document is `RAILS/03_OUTPUT_CONTRACT.md`.
