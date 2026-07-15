# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml/src/org/omg/sysml/lang/sysml/util/ISysMLScope.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml/src/org/omg/sysml/lang/sysml/util/ISysMLScope.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml/src/org/omg/sysml/lang/sysml/util/ISysMLScope.java
- source_bytes: 1194
- source_sha256: `3fc767cc771a8cc360de78ac5a803ce862bc949e56f96a8aa108040cdff8e0d1`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021-2022 Model Driven Solutions, Inc.
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
 * You should have received a copy of theEclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *  
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 *  
 * Contributors:
 *  Ed Seidewitz, MDS
 *  
 *******************************************************************************/

package org.omg.sysml.lang.sysml.util;

import org.eclipse.xtext.scoping.IScope;
import org.omg.sysml.lang.sysml.Element;

public interface ISysMLScope extends IScope {
	Element getElement(String name);
}

````
