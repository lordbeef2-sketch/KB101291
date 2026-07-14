# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/query/PrimitiveOperator.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/query/PrimitiveOperator.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/query/PrimitiveOperator.java
- source_bytes: 1301
- source_sha256: `f5ca8238de2e627a9e649fab2ac1f176304dc9c7c6b304f55013c3b3f19c6010`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * SysML v2 REST/HTTP Pilot Implementation
 * Copyright (C) 2020  InterCAX LLC
 * Copyright (C) 2020  California Institute of Technology ("Caltech")
 * Copyright (C) 2025  Twingineer LLC
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Eclipse Public License as published by
 * the Eclipse Foundation, version 2 of the License.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * Eclipse Public License for more details.
 *
 * You should have received a copy of the Eclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 */

package org.omg.sysml.query;

import com.fasterxml.jackson.annotation.JsonProperty;

public enum PrimitiveOperator {
    @JsonProperty("<")
    LESS_THAN,
    @JsonProperty("<=")
    LESS_THAN_OR_EQUALS,
    @JsonProperty("=")
    EQUALS,
    @JsonProperty(">")
    GREATER_THAN,
    @JsonProperty(">=")
    GREATER_THAN_OR_EQUALS,
    @JsonProperty("in")
    IN,
    @JsonProperty("instanceOf")
    INSTANCE_OF,
}

````
