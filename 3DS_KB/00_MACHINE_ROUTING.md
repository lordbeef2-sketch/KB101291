# MACHINE ROUTING

| Intent | Primary corpus | Required secondary corpus | Search anchors |
|---|---|---|---|
| Java plugin or OpenAPI code | `CAMEO_JAVA_OPENAPI_<target>` | matching `NOMAGIC_DOCS/SPACES/DEVG*`; `LEGACY_PACK/Code_Samples` | fully-qualified class, member, `Plugin`, `plugin.xml`, session/editing API |
| Macro or in-product script | matching `DEVG*` and modeling-tool space | Java OpenAPI; legacy macro records | `macro`, `script`, `Jython`, `JavaScript`, `Groovy`, `Macro Engine` |
| Python integration | `SM_REPOS/SysML-v2-API-Cookbook` | API Services repo; TWC/Simulation schemas; legacy Python | endpoint path, notebook cell, `requests`, JSON schema |
| PowerShell/curl integration | `CURRENT_AUTHORITATIVE_SOURCES` REST schemas | matching Teamwork Cloud docs; legacy PowerShell | method + path, auth header, commit/query/result |
| Teamwork Cloud administration/API | `NOMAGIC_DOCS/SPACES/MCS*`, `TWCloud*`, current `MCS` | current TWC schema; Developer Guide | authentication, projects, branches, commits, Cassandra, migration |
| Simulation automation | `NOMAGIC_DOCS/SPACES/CST*`, current `MMA`/`SYSML2SP`/`SYSML2EP` | Simulation schema; Java OpenAPI | engine, execution, listener, result, REST operationId |
| SysML v1 model authoring | matching `SYSMLP*`, `MD*`, current `MED` | Java OpenAPI; legacy playbooks | stereotype, profile, diagram, requirement, block, port |
| SysML v2 textual/graphical authoring | `OMG_SYSML_V2_AND_KERML_SPECS` | `SysML-v2-Release`; current `SYSML2P` | grammar production, library qualified name, official example |
| KerML semantics | `OMG_SYSML_V2_AND_KERML_SPECS` | `SysML-v2-Release`; Pilot Implementation | metaclass, constraint, derivation, semantic library |
| SysML v1 to v2 transformation | transformation PDF record | Release/Pilot repository transformation sources | mapping name, source metaclass, target metaclass, QVTo |
| Systems Modeling API | API specification PDF | API Services + Cookbook repositories | service name, endpoint, model schema, query, commit |
| UAF/UPDM | matching `UAF12P*`, `UPDM2P*`, current `UAF2P` | modeling-tool docs; Java OpenAPI | viewpoint, metamodel, migration, validation |
| DataHub/integration | matching `CDH*`, current `CDH` | Developer Guide; Java OpenAPI | OSLC, DOORS, schema mapping, synchronization |
| Report/template generation | `DEVG*`, `MD*`, Java OpenAPI | legacy templates/code | Report Wizard, Velocity, template, report data |
| Installation/licensing/JVM | matching `IL*`, current `IL`, `PC` | Version News | Java version, DSLS, FLEXnet, compatibility |
| CATIA/3DEXPERIENCE integration | current `CATIA`, `CAG`, `CFE`, `CSP`, `CSS` | DataHub/Developer Guide | platform service, FLXML, connector, collaboration |
| EICD/pinout/interface artifacts | `LEGACY_PACK/EICD_Pinouts` | SysML/UAF docs as applicable | connector, signal, pin, interface control |

## RETRIEVAL PROCEDURE

1. Resolve target release and product surface.
2. Search matching-space indexes/catalogs before broad content.
3. Find exact symbol/endpoint/grammar identity.
4. Read normalized content for context and embedded exact source for proof.
5. Cross-check lifecycle, transaction, authentication, and cleanup requirements.
6. Generate code with explicit assumptions and no unsupported symbols.
