# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xtext/src/org/omg/sysml/xtext/naming/SysMLQualifiedNameConverter.xtend

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xtext/src/org/omg/sysml/xtext/naming/SysMLQualifiedNameConverter.xtend`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xtext/src/org/omg/sysml/xtext/naming/SysMLQualifiedNameConverter.xtend
- source_bytes: 1677
- source_sha256: `0ded84d4811333922a6778b389734b0342456750a74baa55cc4671bcdb2a10bc`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtend
/*****************************************************************************
 * SysML 2 Pilot Implementation
 *  Copyright (c) 2022 Model Driven Solutions, Inc.
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
package org.omg.sysml.xtext.naming

import org.omg.kerml.xtext.naming.KerMLQualifiedNameConverter

class SysMLQualifiedNameConverter extends KerMLQualifiedNameConverter {
	
	override toQualifiedName(String qualifiedNameText) {
		var unconjugatedQualifiedNameText = qualifiedNameText
		
		val isConjugated = qualifiedNameText !== null && qualifiedNameText.startsWith("~");
		if (isConjugated) {
			unconjugatedQualifiedNameText = unconjugatedQualifiedNameText.substring(1).trim()
		}
		
		var qualifiedName = super.toQualifiedName(unconjugatedQualifiedNameText)
		
		if (isConjugated) {
			qualifiedName = qualifiedName.append("~" + qualifiedName.lastSegment)
		}
		
		qualifiedName
	}
}
````
