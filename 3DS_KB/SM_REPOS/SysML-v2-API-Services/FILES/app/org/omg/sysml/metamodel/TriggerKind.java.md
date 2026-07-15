# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/metamodel/TriggerKind.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/metamodel/TriggerKind.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/metamodel/TriggerKind.java
- source_bytes: 217
- source_sha256: `d27c79eac209bc17b36990910f2e9669a04e87a6dfa4958cd0c0339dfaff0690`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.metamodel;

import com.fasterxml.jackson.annotation.JsonProperty;

public enum TriggerKind {
    @JsonProperty("after") AFTER,
    @JsonProperty("at") AT,
    @JsonProperty("when") WHEN
}
````
