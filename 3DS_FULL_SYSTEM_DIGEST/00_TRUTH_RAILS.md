# TRUTH RAILS

## SOURCE AUTHORITY

1. Exact official source embedded in a matching version record.
2. Normalized content in the same official record.
3. Formal OMG specification or commit-pinned Systems Modeling repository source.
4. Current official REST schema or Java OpenAPI page.
5. Legacy synthesized material, only when it does not conflict with sources above.

## VERSION LOCK

- Never mix Java OpenAPI members, plugin descriptors, dependencies, JVM requirements, or REST payloads across release lines without explicitly identifying the cross-version dependency.
- If the request names a version, search only its matching documentation and Javadoc first.
- If the request omits a version, target 2026x Refresh1 and state that target.
- Treat current shared spaces as the 2026x/2026x Refresh1 product line only when their page content or URL identifies that line; otherwise label the answer current-shared and avoid invented version precision.

## GENERATION PROOF

- Do not invent a class, method, enum, endpoint, stereotype, metaclass, CLI flag, plugin XML field, or SysML grammar production.
- For Java, require an exact Javadoc class/member match plus relevant Developer Guide workflow.
- For REST, require an exact path/method/schema match from the embedded OpenAPI/Swagger source.
- For SysML v2 textual syntax, require grammar/spec/example evidence from the formal specification or official release repository.
- For model mutation, require the target-version transaction/editing/session pattern and error cleanup path.
- Distinguish compile-valid, runtime-dependent, and runtime-validated. Offline generation can establish the first only when dependencies/signatures are fully represented.

## FAILURE BEHAVIOR

- On missing source evidence: report `SOURCE_NOT_IN_CORPUS`; do not guess.
- On version conflict: report both facts with source paths and request/choose an explicit target.
- On vendor source 404: preserve the 404 in the catalog and use enclosing-class/search-index evidence only if it actually contains the required signature.
- On proprietary binary-only behavior: explain that documentation is present but implementation internals are not public.

## RESPONSE TRACE

Every generated solution should carry: target release, execution surface, language/runtime, dependencies, privileges/authentication, destructive effects, rollback/undo behavior, and corpus source paths used.
