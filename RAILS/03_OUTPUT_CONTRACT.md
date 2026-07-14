# OUTPUT CONTRACT

<!--KB_RAIL_CONTROL ordinal=4 required_state=CORPUS_READY next=RAILS/99_RELEASE_GATE.md -->

No generated answer or artifact may be released until it satisfies this contract and the final release gate.

## REQUIRED TRACE

Every substantive answer or generated artifact must identify:

- product and target release;
- execution surface and language/runtime;
- required modules, drivers, libraries, services, licenses, and privileges;
- compile-time or construction-time assumptions;
- runtime dependencies and what was not runtime-validated offline;
- destructive effects, transaction boundaries, cleanup, rollback, and undo behavior;
- exact repository-relative corpus paths used as evidence.

## GENERATION RULES

- Never invent a LabVIEW node, VI, connector terminal, property, method, event, enum, class, endpoint, field, stereotype, metaclass, grammar production, CLI option, or plugin descriptor entry.
- Preserve names, capitalization, types, units, parameter direction, calling order, ownership, threading, error behavior, and version exactly.
- VI generation must cross-check VI Scripting construction mechanics against the target VI or driver connector/parameter record.
- Java model mutation must use the target-version editing/session/transaction and cleanup pattern.
- REST generation must have an exact method/path/schema match.
- SysML v2 or KerML generation must have formal grammar/specification or official repository evidence.
- Distinguish `SOURCE_SUPPORTED`, `COMPILE_OR_CONSTRUCTION_VALIDATED`, `RUNTIME_DEPENDENT`, and `RUNTIME_VALIDATED`. Do not claim a stronger state than the evidence establishes.

## REQUIRED FAILURE LABELS

- Missing evidence: `SOURCE_NOT_IN_CORPUS`
- Integrity or incomplete-ingestion failure: `CORPUS_INTEGRITY_FAILURE`
- Conflicting release evidence: `VERSION_CONFLICT`
- Documented surface with proprietary implementation internals: `IMPLEMENTATION_NOT_PUBLIC`
- Runtime unavailable for execution testing: `RUNTIME_NOT_VALIDATED`

## FINAL CONTROL STEP

Read `RAILS/99_RELEASE_GATE.md`. Do not emit the domain answer before that gate passes.
