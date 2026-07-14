# FULL CORPUS GATE

<!--KB_RAIL_CONTROL ordinal=2 required_state=BOOT_LOCKED unlock_state=CORPUS_READY -->

No query rail is available until every corpus Markdown document has been fully consumed and verified. Relevance, context limits, time, or a direct deep link do not permit skipping.

## ANCHORED MANIFESTS

| corpus | manifest | required manifest SHA-256 | manifest rows | explicit exclusions |
|---|---|---|---:|---|
| NI | `FULL_SYSTEM_DIGEST/00_MACHINE_MANIFEST.md` | `a63b4afe00f3582f08f1f486f8d341c2705741449efb91fb11e9d4c8e6990696` | 1843 | manifest itself |
| 3DS | `3DS_FULL_SYSTEM_DIGEST/00_MACHINE_MANIFEST.md` | `970850c22779e502a3fe269e1a4d7518cf3b3552fb7ba4c4b03b29ee428276dc` | 163667 | manifest itself and `00_VALIDATION.md` |

The required SHA-256 for `3DS_FULL_SYSTEM_DIGEST/00_VALIDATION.md` is `9f54ecb7be879caef8efaa210d935d410847ee7239d6c5a6788efd16f55298b8`.

## ONE SERIAL READ ORDER

Set state to `CORPUS_INGESTING`. Use repository-relative POSIX paths in the ledger.

1. Ordinal 1: read all bytes of `FULL_SYSTEM_DIGEST/00_MACHINE_MANIFEST.md`, reach EOF, parse every manifest row, and verify its anchored hash.
2. Ordinals 2 through 1844: read every NI manifest row in its listed order.
3. Ordinal 1845: read all bytes of `3DS_FULL_SYSTEM_DIGEST/00_MACHINE_MANIFEST.md`, reach EOF, parse every manifest row, and verify its anchored hash.
4. Ordinal 1846: read `3DS_FULL_SYSTEM_DIGEST/00_VALIDATION.md` and verify its explicit hash.
5. Ordinals 1847 through 165513: read every 3DS manifest row in its listed order.

Do not traverse the two corpora concurrently. Do not sort, filter, deduplicate, sample, summarize in place of reading, jump to an index, or advance an ordinal before the current document reaches EOF.

## PER-DOCUMENT ACCEPTANCE

For every ordinal:

1. Open the exact path as a binary stream.
2. Consume the complete stream through EOF.
3. Verify the byte count and SHA-256 against the controlling manifest or explicit control value.
4. Decode and parse the full Markdown document. Preserve code fences, tables, front matter, source blocks, headings, and final nonblank content.
5. Record `ordinal`, `path`, `bytes`, `sha256`, `eof=true`, and `markdown_parsed=true` in durable ingestion state.
6. Advance only if all fields pass.

A hash operation alone proves byte access but not Markdown ingestion. Both `eof=true` and `markdown_parsed=true` are required.

## COMPLETION CERTIFICATE

For each accepted document, append this UTF-8, BOM-free record to the certificate stream:

```text
<ordinal><TAB><repository-relative-path><TAB><decimal-bytes><TAB><lowercase-sha256><LF>
```

SHA-256 the complete 165513-record stream. The only accepted result is:

```text
6cc0c983cb29fda365dc7a330f455a35b66fed7cba215b93cd7bcf3c158cfdc4
```

Required final facts:

- accepted documents: `165513`
- unique paths: `165513`
- duplicate paths: `0`
- missing corpus paths: `0`
- unlisted corpus paths: `0`
- first path: `FULL_SYSTEM_DIGEST/00_MACHINE_MANIFEST.md`
- final path: `3DS_FULL_SYSTEM_DIGEST/SYSTEMS_MODELING_OFFICIAL_REPOSITORIES/SysML-v2-Release/FILES/sysml.library.xmi.implied/Systems_Library/Views.sysmlx.md`

## RESUME AND CACHE

- An interrupted first pass may resume only from a durable, continuous verified prefix whose manifest hashes still match the anchors above.
- A completed pass may be reused by later sessions only when the stored completion certificate, document count, manifest hashes, and explicit validation hash all match this document.
- Any corpus addition, removal, rename, byte change, manifest change, missing ledger segment, or certificate mismatch invalidates the cache and requires a complete replay.
- Control files must still be read from `AGENTS.md` in their required order for every new session.

## FAILURE STATE

On any failure, set state to `CORPUS_INTEGRITY_FAILURE`, report the ordinal and path, and stop. No query rail may open.

## UNLOCK

Only after every requirement passes, set state to `CORPUS_READY`.

The one permitted next document is `RAILS/02_QUERY_RAILS.md`.
