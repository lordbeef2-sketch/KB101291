# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml/src/org/omg/sysml/util/repository/EMFModelDelta.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml/src/org/omg/sysml/util/repository/EMFModelDelta.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml/src/org/omg/sysml/util/repository/EMFModelDelta.java
- source_bytes: 2983
- source_sha256: `5384322a8154647cec9b29c0363906cefca7343962825edf21a3fa958426c61c`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 * SysML 2 Pilot Implementation
 * Copyright (C) 2025 Model Driven Solutions, Inc.
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
 * You should have received a copy of the Eclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 * 
 * Contributors:
 *   Laszlo Gati, MDS
 *   Ed Seidewitz, MDS
 */
package org.omg.sysml.util.repository;

import java.io.IOException;
import java.util.Collections;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.omg.sysml.lang.sysml.Namespace;
import org.omg.sysml.lang.sysml.SysMLFactory;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.model.Element;
import org.omg.sysml.util.ElementUtil;
import org.omg.sysml.util.NamespaceUtil;

public class EMFModelDelta {
	private static final String NAME_PROPERTY = "declaredName";
	private static final String EXTENSION = "sysmlx";
	
	private final Map<EObject, Element> projectRoots;
	
	public EMFModelDelta(Map<EObject, Element> projectRoots) {
		this.projectRoots = projectRoots;
	}
	
	public Map<EObject, Element> getProjectRoots() {
		return projectRoots;
	}
	
	public Set<EObject> getProjectRootsAsNamespaces() {
		return projectRoots.keySet().stream().map(this::wrapInNamespaceIfNotNamespace).collect(Collectors.toSet());
	}
	
	private EObject wrapInNamespaceIfNotNamespace(EObject eObject) {
		if (eObject.eClass() == SysMLPackage.eINSTANCE.getNamespace()) {
			return eObject;
		} else {
			Namespace root = SysMLFactory.eINSTANCE.createNamespace();
			NamespaceUtil.addOwnedMemberTo(root, (org.omg.sysml.lang.sysml.Element) eObject);
			return root;
		}
	}
	
	public void apply(ResourceSet resourceSet, URI baseUri) throws IOException {
		for (var root : projectRoots.keySet()) {
			var dto = projectRoots.get(root);
			Object name = dto.get(NAME_PROPERTY);
			if (name == null) {
				name = dto.get("@id");
			}
			URI fileURI = baseUri.appendSegment(name.toString()).appendFileExtension(EXTENSION);
			Resource resource = resourceSet.createResource(fileURI);
			resource.getContents().add(wrapInNamespaceIfNotNamespace(root));
			ElementUtil.transformAll(resource, false);
			resource.save(Collections.EMPTY_MAP);
		}
	}
}

````
