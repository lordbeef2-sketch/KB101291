# LANGUAGE AND EXECUTION SURFACES

| Surface | Languages/representations | Authority path | Generation rule |
|---|---|---|---|
| Cameo/Magic plugin | Java, plugin XML | versioned Java OpenAPI + Developer Guide | exact target-version signatures and descriptor fields only |
| Cameo macro/script | vendor-supported script engines; version-dependent | matching Developer Guide/modeling-tool docs | never assume CPython/Jython/JS/Groovy availability across versions |
| External product automation | Python, PowerShell, curl, Java, other HTTP clients | exact REST schema + product docs | language may vary; HTTP contract may not |
| Systems Modeling API | Python notebooks, Java service implementation, JSON/JSON-LD, HTTP | official Cookbook/API Services repositories + formal API spec | pin repository commit and schema vocabulary |
| SysML v2 source | textual SysML, KerML, XMI/model interchange | formal specs + official release examples/libraries | syntax and qualified library names must be source-backed |
| Transformations | QVTo, Java, grammar/model artifacts | formal transformation spec + official repository | cite mapping identity and both source/target metaclasses |
| Reports/templates | Velocity/template languages, Java helper APIs | matching docs and OpenAPI | escape output and preserve version-specific engine behavior |
| Operations | PowerShell, shell, configuration formats | Installation, Teamwork Cloud, licensing docs | identify host OS, product version, privileges, backup/rollback |

Python is included as a first-class external automation language through the official API Cookbook notebooks and retained legacy Python sources. It is not automatically equivalent to an in-process Cameo OpenAPI runtime.
