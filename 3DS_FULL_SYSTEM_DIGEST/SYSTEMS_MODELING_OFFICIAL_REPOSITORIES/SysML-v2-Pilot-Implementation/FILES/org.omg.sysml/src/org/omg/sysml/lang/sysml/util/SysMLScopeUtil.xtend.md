# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml/src/org/omg/sysml/lang/sysml/util/SysMLScopeUtil.xtend

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml/src/org/omg/sysml/lang/sysml/util/SysMLScopeUtil.xtend`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml/src/org/omg/sysml/lang/sysml/util/SysMLScopeUtil.xtend
- source_bytes: 2031
- source_sha256: `c819b9c48e0c5c7ac870479e7c95c06e1288f504f5bb12e3744475a8b00187aa`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtend
/*****************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021-2022 Model Driven Solutions, Inc.
  *    
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Eclipse Public License as published by
 * the Eclipse Foundation, version 2 of the License.
 * (at your option) any later version.
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
 *****************************************************************************/

package org.omg.sysml.lang.sysml.util

import org.eclipse.emf.ecore.EObject
import org.eclipse.emf.ecore.EReference
import org.eclipse.emf.ecore.resource.Resource
import org.eclipse.xtext.resource.IResourceServiceProvider
import org.eclipse.xtext.scoping.IScopeProvider
import org.omg.sysml.lang.sysml.Element

class SysMLScopeUtil {
	
	def static IScopeProvider getScopeProvider(Resource resource) {
		try {
			IResourceServiceProvider.Registry.INSTANCE.getResourceServiceProvider(resource?.getURI)?.get(IScopeProvider)
		} catch (Exception e) {
			System.out.println("[SysMLScopeUtil] Cannot get scope provider: " + e)
			null
		}
	}

	def static ISysMLScope getScopeFor(Resource resource, EObject context, EReference reference) {
		return getScopeProvider(resource).getScope(context, reference) as ISysMLScope
	}
	
	def static Element getElementFor(EObject context, EReference reference, String name) {
		return getScopeFor(context.eResource(), context, reference).getElement(name)
	}
	
}
````
