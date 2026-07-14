# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/KerMLXpectGlobalScopeProvider.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/KerMLXpectGlobalScopeProvider.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/KerMLXpectGlobalScopeProvider.java
- source_bytes: 1249
- source_sha256: `c65f06fc6115ea1632010acde55b210b1c794d91549b5b4705efbb1b2f98d0c9`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 * SysML 2 Pilot Implementation
 * Copyright (c) 2019 Model Driven Solutions, Inc.
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
 * 
 * Contributors:
 *  Ed Seidewitz, MDS
 */
package org.omg.kerml.xpect;

import com.google.common.base.Predicate;
import org.eclipse.xtext.resource.IEObjectDescription;
import org.omg.kerml.xtext.scoping.KerMLGlobalScopeProvider;

public class KerMLXpectGlobalScopeProvider extends KerMLGlobalScopeProvider {
	
  @Override
  public Predicate<IEObjectDescription> getRootFilter() {
    return description -> (!"Base".equals(description.getName().getFirstSegment()));
  }
}
````
