# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/metamodel/FeatureDirectionKind.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/metamodel/FeatureDirectionKind.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/metamodel/FeatureDirectionKind.java
- source_bytes: 224
- source_sha256: `1149a3852248edeaca4509dafcbd3f0aee5313abded305e1c2bd414c914db90c`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.metamodel;

import com.fasterxml.jackson.annotation.JsonProperty;

public enum FeatureDirectionKind {
    @JsonProperty("in") IN,
    @JsonProperty("inout") INOUT,
    @JsonProperty("out") OUT
}
````
