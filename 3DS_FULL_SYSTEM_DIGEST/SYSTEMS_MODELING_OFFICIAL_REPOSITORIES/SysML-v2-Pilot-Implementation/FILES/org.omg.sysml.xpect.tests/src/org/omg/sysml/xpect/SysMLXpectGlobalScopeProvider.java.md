# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/SysMLXpectGlobalScopeProvider.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/SysMLXpectGlobalScopeProvider.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/SysMLXpectGlobalScopeProvider.java
- source_bytes: 1255
- source_sha256: `1ccda3b340f25cfba9f420ee9edcf9f50837dc69039856a6da1c4011829de9cb`
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
package org.omg.sysml.xpect;

import com.google.common.base.Predicate;
import org.eclipse.xtext.resource.IEObjectDescription;
import org.omg.sysml.xtext.scoping.SysMLGlobalScopeProvider;

public class SysMLXpectGlobalScopeProvider extends SysMLGlobalScopeProvider {
	
  @Override
  public Predicate<IEObjectDescription> getRootFilter() {
    return description -> (!"Base".equals(description.getName().getFirstSegment()));
  }
  
}

````
