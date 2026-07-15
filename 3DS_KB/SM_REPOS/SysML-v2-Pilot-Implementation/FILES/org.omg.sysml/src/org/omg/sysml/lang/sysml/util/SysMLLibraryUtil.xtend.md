# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml/src/org/omg/sysml/lang/sysml/util/SysMLLibraryUtil.xtend

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml/src/org/omg/sysml/lang/sysml/util/SysMLLibraryUtil.xtend`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml/src/org/omg/sysml/lang/sysml/util/SysMLLibraryUtil.xtend
- source_bytes: 2413
- source_sha256: `e2b643e40a7d919f0a769f336bba1e9eb01ba64abd8dde914862057831a2b01e`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtend
/*****************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2019-2020 Model Driven Solutions, Inc.
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

import org.eclipse.xtext.resource.IResourceServiceProvider
import org.eclipse.emf.ecore.resource.Resource
import org.omg.sysml.lang.sysml.Element
import org.omg.sysml.lang.sysml.Type
import org.eclipse.emf.common.util.URI

class SysMLLibraryUtil {
	
	public static final String DEFAULT_MODEL_LIBRARY_PATH = "/resource/sysml.library";
	
	static String modelLibraryPath = DEFAULT_MODEL_LIBRARY_PATH;
	
	def static setModelLibraryDirectory(String dir) {
		val uri = URI.createFileURI(dir);
		modelLibraryPath = uri.devicePath ?: uri.path;
	}

	def static getModelLibraryPath() {
		modelLibraryPath
	}
	
	def static IModelLibraryProvider getInstance(Resource resource) {
		try {
			IResourceServiceProvider.Registry.INSTANCE.getResourceServiceProvider(resource?.getURI)?.get(IModelLibraryProvider)
		} catch (Exception e) {
			System.out.println("[SysMLLibraryUtil] Cannot get library provider: " + e)
			null
		}
	}
	
	def static Element getLibraryElement(Element context, String name) {		
		return getInstance(context.eResource)?.getElement(context, name)
	}
	
	def static Type getLibraryType(Element context, String... defaultNames) {
		for (String defaultName: defaultNames) {
			val element = getLibraryElement(context, defaultName);
			if (element instanceof Type) {
				return element;
			}
		}
		return null;
	}
}
````
