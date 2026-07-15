# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/LibraryPackageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/LibraryPackageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/LibraryPackageAdapter.java
- source_bytes: 2457
- source_sha256: `d7a5dcefc3b9e42a23ec3ef1b6dab1cb7b688566b25f88f5d7ceb3a3bc1230a1`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2026 Model Driven Solutions, Inc.
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

package org.omg.sysml.adapter;

import java.util.UUID;

import org.eclipse.emf.ecore.resource.Resource;
import org.omg.sysml.util.ElementUtil;
import org.omg.sysml.lang.sysml.LibraryPackage;

public class LibraryPackageAdapter extends PackageAdapter {

	public final String KERML_LIBRARY_BASE_URI = "https://www.omg.org/spec/KerML/";
	public final String SYSML_LIBRARY_BASE_URI = "https://www.omg.org/spec/SysML/";
	
	// UUID for "NameSpace_URL", per ITU-T Rec. X.667 (10/2012), Annex D.9
	public final UUID UUID_NAMESPACE_URL = UUID.fromString("6ba7b811-9dad-11d1-80b4-00c04fd430c8");

	public LibraryPackageAdapter(LibraryPackage element) {
		super(element);
	}
	
	public LibraryPackage getTarget() {
		return (LibraryPackage)super.getTarget();
	}
	
	/**
	 * If this is a standard library Package, then create the elementId as a named-based UUID
	 * using a URL constructed from the KerML or SysML base URI and the Package's name.
	 */
	@Override
	public String createElementId() {
		LibraryPackage target = getTarget();
		
		if (target.isStandard()) {
			Resource resource = target.eResource();
			if (resource != null) {
				String uri = resource.getURI().toString().contains("Kernel")? KERML_LIBRARY_BASE_URI: SYSML_LIBRARY_BASE_URI;
				String qualifiedName = target.getQualifiedName();
				if (qualifiedName != null) {
					return ElementUtil.constructNameUUID(UUID_NAMESPACE_URL, uri + qualifiedName).toString();
				}
			}
		}
		
		return super.createElementId();
	}
	
}

````
