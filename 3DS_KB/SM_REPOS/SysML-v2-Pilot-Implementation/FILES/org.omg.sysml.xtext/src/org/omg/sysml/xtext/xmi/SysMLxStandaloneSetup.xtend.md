# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xtext/src/org/omg/sysml/xtext/xmi/SysMLxStandaloneSetup.xtend

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xtext/src/org/omg/sysml/xtext/xmi/SysMLxStandaloneSetup.xtend`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xtext/src/org/omg/sysml/xtext/xmi/SysMLxStandaloneSetup.xtend
- source_bytes: 1858
- source_sha256: `f665fb061c1b31032cb5539e4446a6daab62873ac435d327742cb7f65395d76f`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtend
/**
 * SysML 2 Pilot Implementation
 * Copyright (C) 2025  Model Driven Solutions, Inc.
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
package org.omg.sysml.xtext.xmi

import com.google.inject.Guice
import com.google.inject.Inject
import org.eclipse.emf.ecore.resource.Resource
import org.eclipse.xtext.ISetup
import org.eclipse.xtext.resource.FileExtensionProvider
import org.eclipse.xtext.resource.IResourceServiceProvider

class SysMLxStandaloneSetup implements ISetup {
	
	@Inject
	FileExtensionProvider fileExtensionProvider
	
	@Inject
	IResourceServiceProvider resourceServiceProvider
	
	@Inject
	Resource.Factory resourceFactory
	
	override createInjectorAndDoEMFRegistration() {
		val injector = createInjector()
		injector.injectMembers(this)
		
		fileExtensionProvider.fileExtensions.forEach[ 
			IResourceServiceProvider.Registry.INSTANCE.extensionToFactoryMap.put(it, resourceServiceProvider)
			Resource.Factory.Registry.INSTANCE.extensionToFactoryMap.put(it, resourceFactory)
		]
		
		injector
	}
	
	static def doSetup(){
		new SysMLxStandaloneSetup().createInjectorAndDoEMFRegistration
	}
	
	def createInjector() {
		return Guice.createInjector(new SysMLxRuntimeModule());
	}
}

````
