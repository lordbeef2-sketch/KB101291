# BOOT SEQUENCE

<!--KB_RAIL_CONTROL ordinal=1 required_state=ENTRY_LOCKED next=RAILS/01_FULL_CORPUS_GATE.md -->

Read this document completely. There is no branch at boot.

## STATE TRANSITION

1. Confirm the session began at repository-root `AGENTS.md`.
2. Confirm no domain document was used before this control document.
3. Set state to `BOOT_LOCKED`.
4. Open only `RAILS/01_FULL_CORPUS_GATE.md`.

If any confirmation fails, discard all derived domain conclusions and restart at `AGENTS.md`.

## PROHIBITED WHILE BOOT_LOCKED

- choosing NI or 3DS;
- choosing a version, language, API, product, or task rail;
- semantic search or vector retrieval over corpus content;
- answering from model memory as though it came from this corpus;
- generating LabVIEW, VI Scripting, Python, C, C++, C#, Java, REST, SysML, KerML, shell, or plugin artifacts;
- treating an `INDEX.md`, catalog, routing page, source record, example, or attachment as an alternate entry point.

## ONLY NEXT DOCUMENT

`RAILS/01_FULL_CORPUS_GATE.md`
