# NI KB SINGLE ENTRY

<!--KB_ENTRY canonical=true kb=NI protocol=NI_KB_RAILS_V1 -->

This is the only valid starting point for the NI knowledge base. It governs only `FULL_SYSTEM_DIGEST/`. The sibling `3DS_FULL_SYSTEM_DIGEST/` is a separate KB and must never be opened, indexed, required, or cited by this protocol.

## ENTRY LOCK

1. Read this control document completely.
2. Set state to `NI_CORPUS_INGESTING`.
3. Do not search, route, answer a domain question, or generate an artifact until the NI corpus gate passes.
4. A deep link to any other NI document is not an alternate entry. Return here first.

This control file is intentionally outside the evidence manifest and is consumed as the entry document. The evidence corpus contains 1844 Markdown documents. Including this controller, the independent NI KB contains 1845 Markdown documents.

## NI-ONLY MANIFEST ANCHOR

- manifest: `00_MACHINE_MANIFEST.md`
- required manifest SHA-256: `a63b4afe00f3582f08f1f486f8d341c2705741449efb91fb11e9d4c8e6990696`
- listed evidence rows: `1843`
- explicit manifest exclusion: the manifest itself

## REQUIRED SERIAL READ

1. Evidence ordinal 1: read `00_MACHINE_MANIFEST.md` completely, reach EOF, verify its anchored hash, and parse every row.
2. Evidence ordinals 2 through 1844: read every manifest row in its listed order.
3. For each document, consume all bytes through EOF, verify byte count and SHA-256, decode and parse the complete Markdown, and record `ordinal`, `path`, `bytes`, `sha256`, `eof=true`, and `markdown_parsed=true`.
4. Do not sort, filter, sample, skip, parallelize branches, or advance before the current document passes.

## NI COMPLETION CERTIFICATE

For every accepted evidence document, append this BOM-free UTF-8 record:

```text
<ordinal><TAB><NI-root-relative-path><TAB><decimal-bytes><TAB><lowercase-sha256><LF>
```

SHA-256 of the complete 1844-record stream must equal:

```text
2c2de3d71eb38b688874212c2594ed7c78e9ccefea4612cfc0ba667630dda2e8
```

Only then set state to `NI_CORPUS_READY`.

An interrupted pass may resume only from a durable continuous prefix. A completed pass may be reused only when the certificate, document count, and manifest hash match exactly. Any NI corpus change invalidates the cache. No 3DS state or certificate participates.

## NI QUERY RAILS

These rails remain locked until `NI_CORPUS_READY`:

- primary digest: `00_FULL_SYSTEM_DIGEST.md`
- machine routing: `NI_ECOSYSTEM/00_MACHINE_ROUTING.md`
- LabVIEW G, VI Server, and VI Scripting: `NI_LABVIEW/PROGRAMMING_REFERENCE/` plus `NI_LABVIEW/USER_MANUAL/`
- LabVIEW releases and compatibility: `NI_LABVIEW/RELEASES/`
- NI products and drivers: matching `NI_ECOSYSTEM/BUNDLES/` records
- NI Python, gRPC, REST, OpenAPI, and source interfaces: matching `NI_ECOSYSTEM/OSS_INTERFACES/` records
- Python language/runtime: `PYTHON_3_12_13/`

Resolve the target NI product, 2024+ release, interface, and language. Require exact evidence for every VI, node, connector terminal, property, method, event, class, endpoint, enum, type, unit, error, lifecycle rule, and cleanup path. VI generation must cross-check VI Scripting construction mechanics against the target VI or driver connector record.

## NI OUTPUT GATE

Every released answer or artifact must state the NI product/release, execution surface, language/runtime, dependencies, privileges, runtime-validation status, destructive effects, cleanup/rollback, and exact NI KB paths used.

On failure, stop with one of: `NI_CORPUS_INTEGRITY_FAILURE`, `SOURCE_NOT_IN_NI_CORPUS`, `VERSION_CONFLICT`, or `RUNTIME_NOT_VALIDATED`. Never fill a gap from the 3DS KB or unsupported model memory.
