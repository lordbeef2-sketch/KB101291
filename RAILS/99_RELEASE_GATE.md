# RELEASE GATE

<!--KB_RAIL_CONTROL ordinal=5 required_state=CORPUS_READY release_state=READY -->

## STATIC RAIL VALIDATION

- validated UTC: `2026-07-14T18:53:27.6237655Z`
- validation result: `PASS`
- canonical root entry documents: `1`
- canonical root entry: `AGENTS.md`
- boot chain: `AGENTS.md` -> `RAILS/00_BOOT_SEQUENCE.md` -> `RAILS/01_FULL_CORPUS_GATE.md`
- routing remains locked until: `CORPUS_READY`
- post-ingestion chain: `RAILS/02_QUERY_RAILS.md` -> `RAILS/03_OUTPUT_CONTRACT.md` -> `RAILS/99_RELEASE_GATE.md`
- NI manifest rows: `1843`
- 3DS manifest rows: `163667`
- explicit non-manifest 3DS validation record: `1`
- manifest documents read directly: `2`
- total corpus documents: `165513`
- total corpus bytes replayed: `4989524016`
- unique covered corpus paths: `165513`
- missing paths: `0`
- extra paths: `0`
- duplicate paths: `0`
- byte-count mismatches: `0`
- SHA-256 mismatches: `0`
- UTF-8 decode failures: `0`
- full-corpus certificate: `6cc0c983cb29fda365dc7a330f455a35b66fed7cba215b93cd7bcf3c158cfdc4`

## PER-RESPONSE RELEASE CHECK

Set state to `READY` only when all are true:

1. The current session followed the single control chain from `AGENTS.md`.
2. A valid exact-corpus completion certificate established `CORPUS_READY`.
3. The selected query rail matches the requested product, release, execution surface, and language.
4. Primary and mandatory secondary evidence records were read completely.
5. Every generated symbol or operation is supported by exact corpus evidence.
6. The output trace and validation-strength labels are present.
7. No unresolved integrity failure, version conflict, unsupported symbol, or silent source gap remains.

If any item fails, do not release the answer or artifact. Emit the applicable failure label and the failing path or condition.

## READY TOKEN

The internal ready token for this corpus is:

```text
KB101291_RAILS_V1:6cc0c983cb29fda365dc7a330f455a35b66fed7cba215b93cd7bcf3c158cfdc4:READY
```

This token is valid only after the per-response checks pass. It is a state marker, not a substitute for the full ingestion ledger.
