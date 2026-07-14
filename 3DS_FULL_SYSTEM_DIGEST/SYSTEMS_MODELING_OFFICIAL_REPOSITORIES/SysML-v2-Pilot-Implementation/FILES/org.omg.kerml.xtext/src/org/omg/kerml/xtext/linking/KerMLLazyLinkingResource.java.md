# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xtext/src/org/omg/kerml/xtext/linking/KerMLLazyLinkingResource.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xtext/src/org/omg/kerml/xtext/linking/KerMLLazyLinkingResource.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xtext/src/org/omg/kerml/xtext/linking/KerMLLazyLinkingResource.java
- source_bytes: 1242
- source_sha256: `c20a60c7b7603a0837ac342a5f93ac56ae778c1db914fff9a1634c76dfd060d4`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*****************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2024 Model Driven Solutions, Inc.
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
 * 
 *****************************************************************************/
package org.omg.kerml.xtext.linking;

import org.eclipse.xtext.linking.lazy.LazyLinkingResource;

public class KerMLLazyLinkingResource extends LazyLinkingResource {
	
	public void clearUnresolvableURIFragments() {
		getUnresolvableURIFragments().clear();
	}
	
}

````
