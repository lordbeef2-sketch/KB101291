# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/query/impl/package-info.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/query/impl/package-info.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/query/impl/package-info.java
- source_bytes: 1697
- source_sha256: `1636dd50320e16663fbbcc9a7b4e2226e17b5aa2344fd3e2efaf21c850b55ace`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * SysML v2 REST/HTTP Pilot Implementation
 * Copyright (C) 2020  InterCAX LLC
 * Copyright (C) 2020  California Institute of Technology ("Caltech")
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

@AnyMetaDefs(value = {
        @AnyMetaDef(name = "ConstraintMetaDef", metaType = "string", idType = "java.util.UUID",
                metaValues = {
                        @MetaValue(value = "CompositeConstraint", targetEntity = CompositeConstraintImpl.class),
                        @MetaValue(value = "PrimitiveConstraint", targetEntity = PrimitiveConstraintImpl.class),
                }),
        @AnyMetaDef(name = "QueryMetaDef", metaType = "string", idType = "java.util.UUID",
                metaValues = {
                        @MetaValue(value = "Query", targetEntity = QueryImpl.class),
                }),
})

@GenericGenerators(value = {
        @GenericGenerator(name = "UseExistingOrGenerateUUIDGenerator", strategy = "jpa.UseExistingOrGenerateUUIDGenerator")
})
package org.omg.sysml.query.impl;

import org.hibernate.annotations.*;
````
