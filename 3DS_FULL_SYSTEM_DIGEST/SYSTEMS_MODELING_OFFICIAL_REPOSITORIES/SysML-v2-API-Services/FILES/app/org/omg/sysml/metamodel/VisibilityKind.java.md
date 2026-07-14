# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/metamodel/VisibilityKind.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/metamodel/VisibilityKind.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/metamodel/VisibilityKind.java
- source_bytes: 242
- source_sha256: `e0c78d356f2961836b4bda6cda294a6674aa154ca9010603caf3a12f5c125723`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.metamodel;

import com.fasterxml.jackson.annotation.JsonProperty;

public enum VisibilityKind {
    @JsonProperty("private") PRIVATE,
    @JsonProperty("protected") PROTECTED,
    @JsonProperty("public") PUBLIC
}
````
