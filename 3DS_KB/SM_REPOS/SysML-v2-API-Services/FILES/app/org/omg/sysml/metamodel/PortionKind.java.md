# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/metamodel/PortionKind.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/metamodel/PortionKind.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/metamodel/PortionKind.java
- source_bytes: 204
- source_sha256: `58b46a3618e146124bd469299ca26423dc4542547938ef46cc7c0f83e857552e`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.metamodel;

import com.fasterxml.jackson.annotation.JsonProperty;

public enum PortionKind {
    @JsonProperty("snapshot") SNAPSHOT,
    @JsonProperty("timeslice") TIMESLICE
}
````
