# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/metamodel/StateSubactionKind.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/metamodel/StateSubactionKind.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/metamodel/StateSubactionKind.java
- source_bytes: 224
- source_sha256: `afb3689ce6e6cebea699fbea404c85908f71828a6efc4e55aba6831b6b5a0df6`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.metamodel;

import com.fasterxml.jackson.annotation.JsonProperty;

public enum StateSubactionKind {
    @JsonProperty("do") DO,
    @JsonProperty("entry") ENTRY,
    @JsonProperty("exit") EXIT
}
````
