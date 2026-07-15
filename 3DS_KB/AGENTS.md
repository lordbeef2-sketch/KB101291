# 3DS KB SINGLE ENTRY

<!--KB_ENTRY canonical=true kb=3DS protocol=3DS_KB_RAILS_V1 -->

This is the only valid starting point for the 3DS / CATIA Magic / No Magic knowledge base. It governs only `3DS_KB/`. The sibling `NI_KB/` is a separate NI KB and must never be opened, indexed, required, or cited by this protocol.

## ENTRY LOCK

1. Read this control document completely.
2. Set state to `3DS_CORPUS_INGESTING`.
3. Do not search, route, answer a domain question, or generate an artifact until the 3DS corpus gate passes.
4. A deep link to any other 3DS document is not an alternate entry. Return here first.

This control file is intentionally outside the evidence manifest and is consumed as the entry document. The evidence corpus contains 163670 Markdown documents. Including this controller, the independent 3DS KB contains 163671 Markdown documents.

## 3DS-ONLY MANIFEST ANCHORS

- manifest: `00_MACHINE_MANIFEST.md`
- required manifest SHA-256: `639bad0eb2833d5448cb49ee0b4d613d8c76d5cec7c02b109bbf8b5c01562177`
- listed evidence rows: `163668`
- explicit manifest exclusions: the manifest itself and `00_VALIDATION.md`
- required `00_VALIDATION.md` SHA-256: `42b5dadf3683b30632472f1ad1ea2cab9ed7b77b8b86e28b2da26fbb6f792221`

## REQUIRED SERIAL READ

1. Evidence ordinal 1: read `00_MACHINE_MANIFEST.md` completely, reach EOF, verify its anchored hash, and parse every row.
2. Evidence ordinal 2: read `00_VALIDATION.md` completely and verify its explicit hash.
3. Evidence ordinals 3 through 163670: read every manifest row in its listed order.
4. For each document, consume all bytes through EOF, verify byte count and SHA-256, decode and parse the complete Markdown, and record `ordinal`, `path`, `bytes`, `sha256`, `eof=true`, and `markdown_parsed=true`.
5. Do not sort, filter, sample, skip, parallelize branches, or advance before the current document passes.

## 3DS COMPLETION CERTIFICATE

For every accepted evidence document, append this BOM-free UTF-8 record:

```text
<ordinal><TAB><3DS-root-relative-path><TAB><decimal-bytes><TAB><lowercase-sha256><LF>
```

SHA-256 of the complete 163670-record stream must equal:

```text
f1798d6892b64d92a239d9604197a32e5a7b4cabde119c7fae0c465850c9e1f5
```

Only then set state to `3DS_CORPUS_READY`.

An interrupted pass may resume only from a durable continuous prefix. A completed pass may be reused only when the certificate, document count, manifest hash, and validation hash match exactly. Any 3DS corpus change invalidates the cache. No NI state or certificate participates.

## 3DS QUERY RAILS

These rails remain locked until `3DS_CORPUS_READY`:

- primary digest and load policy: `00_FULL_SYSTEM_DIGEST.md`
- truth and version controls: `00_TRUTH_RAILS.md` and `00_VERSION_MATRIX.md`
- machine routing: `00_MACHINE_ROUTING.md`
- Java plugins/OpenAPI: exact `CAMEO_JAVA_OPENAPI_<target-release>/` plus matching `NOMAGIC_DOCS/SPACES/DEVG*`
- macros and in-product scripting: matching Developer Guide and product space plus exact target-version API surface
- Teamwork Cloud, Simulation, and REST: `CURRENT_AUTHORITATIVE_SOURCES/` plus matching official product space
- SysML v2, KerML, and Systems Modeling API: `OMG_SYSML_V2_AND_KERML_SPECS/` plus `SM_REPOS/`
- legacy evidence: `LEGACY_PACK/` only as a non-overriding fallback

Resolve the target product, release, execution surface, and language. Never mix Java OpenAPI, JVM, plugin metadata, REST schemas, or model semantics across release lines without explicitly identifying the dependency. If the request omits a 3DS release, target 2026x Refresh1 and state that target.

## 3DS OUTPUT GATE

Every released answer or artifact must state the 3DS product/release, execution surface, language/runtime, dependencies, authentication/privileges, runtime-validation status, transactions, destructive effects, cleanup/rollback, and exact 3DS KB paths used.

On failure, stop with one of: `3DS_CORPUS_INTEGRITY_FAILURE`, `SOURCE_NOT_IN_3DS_CORPUS`, `VERSION_CONFLICT`, `IMPLEMENTATION_NOT_PUBLIC`, or `RUNTIME_NOT_VALIDATED`. Never fill a gap from the NI KB or unsupported model memory.
