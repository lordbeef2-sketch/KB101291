# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/metamodel/TransitionFeatureKind.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/metamodel/TransitionFeatureKind.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/metamodel/TransitionFeatureKind.java
- source_bytes: 241
- source_sha256: `00c9cd9e814e0c8c6442e4c7388ed8b63decf2a6c40c230f6fae55801a01ba29`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.metamodel;

import com.fasterxml.jackson.annotation.JsonProperty;

public enum TransitionFeatureKind {
    @JsonProperty("effect") EFFECT,
    @JsonProperty("guard") GUARD,
    @JsonProperty("trigger") TRIGGER
}
````
