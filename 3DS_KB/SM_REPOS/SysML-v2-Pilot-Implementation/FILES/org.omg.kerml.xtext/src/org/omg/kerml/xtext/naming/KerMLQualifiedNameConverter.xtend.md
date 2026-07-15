# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xtext/src/org/omg/kerml/xtext/naming/KerMLQualifiedNameConverter.xtend

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xtext/src/org/omg/kerml/xtext/naming/KerMLQualifiedNameConverter.xtend`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xtext/src/org/omg/kerml/xtext/naming/KerMLQualifiedNameConverter.xtend
- source_bytes: 2094
- source_sha256: `5295d24a9b590e5c529e1f9fa18626115c27322420beb15e950dde55d7f7d58b`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtend
/*****************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2018 IncQuery Labs Ltd.
 * Copyright (c) 2019, 2021 Model Driven Solutions, Inc.
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
 *  Zoltan Kiss, IncQuery
 *  Balazs Grill, IncQuery
 *  Ed Seidewitz, MDS
 * 
 *****************************************************************************/
package org.omg.kerml.xtext.naming

import org.eclipse.xtext.naming.IQualifiedNameConverter
import org.eclipse.xtext.naming.QualifiedName
import com.google.common.base.Preconditions
import org.omg.sysml.util.ElementUtil

class KerMLQualifiedNameConverter implements IQualifiedNameConverter {
	
	override toQualifiedName(String qualifiedNameText) {
		Preconditions.checkArgument(qualifiedNameText !== null, "Qualified name cannot be null")

		val qualifiedNameAsText =
			if (qualifiedNameText.endsWith("::")) qualifiedNameText.substring(0, qualifiedNameText.length - 2)
			else qualifiedNameText
			
		Preconditions.checkArgument(!qualifiedNameAsText.empty, "Qualified name cannot be empty")

		val segments = ElementUtil.parseQualifiedName(qualifiedNameAsText)		
		QualifiedNameUtil.createQualifiedName(segments)
	}

	override toString(QualifiedName name) {
		Preconditions.checkArgument(name !== null, "Qualified name cannot be null")			
		QualifiedNameUtil.toQualifiedNameString(name)
	}
	
}

````
