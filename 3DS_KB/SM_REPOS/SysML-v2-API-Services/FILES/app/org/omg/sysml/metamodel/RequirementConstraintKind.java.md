# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/metamodel/RequirementConstraintKind.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/metamodel/RequirementConstraintKind.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/metamodel/RequirementConstraintKind.java
- source_bytes: 226
- source_sha256: `23dbd454d0dc20f184d088285dfd782609b0b37290336665a2ccad4d23350726`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.metamodel;

import com.fasterxml.jackson.annotation.JsonProperty;

public enum RequirementConstraintKind {
    @JsonProperty("assumption") ASSUMPTION,
    @JsonProperty("requirement") REQUIREMENT
}
````
