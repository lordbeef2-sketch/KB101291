# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml/src/org/omg/sysml/generation/KerMLMOF2KerMLText.xtend

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml/src/org/omg/sysml/generation/KerMLMOF2KerMLText.xtend`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml/src/org/omg/sysml/generation/KerMLMOF2KerMLText.xtend
- source_bytes: 2140
- source_sha256: `26ffb09338862f769a644d51de37286c0406d969d9e83f33a982c300338124a0`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtend
/*******************************************************************************
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
 *******************************************************************************/

package org.omg.sysml.generation

class KerMLMOF2KerMLText extends MOF2KerMLText {
	
	override generate(org.eclipse.uml2.uml.Package model) {
		'''
		standard library package KerML {
			doc 
			/*
			 * This package contains a reflective KerML model of the KerML abstract syntax.
			 */
			 
			private import ScalarValues::*;
			public import Kernel::*;
			
			package Root {
				«model.getPackage("Root").toPackageBody»
			}
			
			package Core {
				public import Root::*;
				
				«model.getPackage("Core").toPackageBody»
			}
			
			package Kernel {
				public import Core::*;
				
				«model.getPackage("Kernel").toPackageBody»
			}
		}
		'''
	}
	
	override toRedefines(org.eclipse.uml2.uml.Property property) {
		var redefinedProperties = property.redefinedProperties.toPropertyList
		if ("annotatedElement".equals(property.name)) {
			redefinedProperties = 
				if (redefinedProperties.empty) "annotatedElement"
				else redefinedProperties + ", annotatedElement"
		}
		toRedefines(redefinedProperties)
	}
	
	static def void main(String[] args) {
		if (args.length >= 2) {
			new KerMLMOF2KerMLText().generate(args.get(0), args.get(1))
		}
	}
	
}
````
