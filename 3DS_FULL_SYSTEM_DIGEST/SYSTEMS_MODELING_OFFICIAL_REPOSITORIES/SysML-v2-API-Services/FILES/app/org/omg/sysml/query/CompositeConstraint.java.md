# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/app/org/omg/sysml/query/CompositeConstraint.java

- repository: `SysML-v2-API-Services`
- source_path: `app/org/omg/sysml/query/CompositeConstraint.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/app/org/omg/sysml/query/CompositeConstraint.java
- source_bytes: 1134
- source_sha256: `ff8c7837da992dc378cf4b496b7c55520f2e52336e0ea93dd207fee6cfa3adbd`
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

package org.omg.sysml.query;

import java.util.Collection;

public interface CompositeConstraint {
    Collection<Constraint> getConstraint();

    void setConstraint(Collection<Constraint> constraint);

    CompositeOperator getOperator();

    void setOperator(CompositeOperator operator);
}

````
