# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xtext/src/org/omg/kerml/xtext/library/LibraryNamespaces.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xtext/src/org/omg/kerml/xtext/library/LibraryNamespaces.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xtext/src/org/omg/kerml/xtext/library/LibraryNamespaces.java
- source_bytes: 2793
- source_sha256: `6d7f668debcfb055881b06d548c970f38513fd6158efc2b6a3e8cf5baf35281b`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 * SysML 2 Pilot Implementation
 * Copyright (C) 2024 Model Driven Solutions, Inc.
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
 *   Laszlo Gati, MDS
 */
package org.omg.kerml.xtext.library;

import java.util.List;

import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.xtext.naming.IQualifiedNameConverter;
import org.eclipse.xtext.naming.IQualifiedNameProvider;
import org.eclipse.xtext.naming.QualifiedName;
import org.omg.kerml.xtext.scoping.KerMLScope;
import org.omg.sysml.lang.sysml.Namespace;

import com.google.inject.Inject;

/**
 * Core logic for determining if a reference is resolvable from a {@link Namespace}.
 * Used by the {@link KerMLScope} to skip unnecessary searches in Namespaces.
 */
public class LibraryNamespaces {
	
	@Inject
	private IQualifiedNameProvider qualifiedNameProvider;
	
	@Inject
	private IQualifiedNameConverter qualifiedNameConverter;
	
	@Inject
	private ILibraryIndexProvider libraryIndexProvider;
	
	public boolean canContainMember(Namespace namespace, QualifiedName prefix, QualifiedName memberQn) {
		
		if (memberQn == null) {
			return true;
		}
		
		if (libraryIndexProvider.isIndexDisabled()) {
			return true;
		};
		
		Resource resourceOfNamespace = namespace.eResource();
		
		if (resourceOfNamespace == null) {
			return true;
		}
		
		LibraryIndex index = libraryIndexProvider.getIndexFor(resourceOfNamespace);
		
		var namespaceFQN = qualifiedNameProvider.getFullyQualifiedName(namespace);
		
		if (namespaceFQN == null || namespaceFQN.isEmpty() || !index.containsNamespace(qualifiedNameConverter.toString(namespaceFQN))) {
			return true;
		}
		
		memberQn = memberQn.startsWith(prefix) ? memberQn.skipFirst(prefix.getSegmentCount()) : memberQn;
		
		return canNamespaceContainQn(index, namespaceFQN, memberQn);
	}	
	
	private boolean canNamespaceContainQn(LibraryIndex index, QualifiedName nestingNamespace, QualifiedName member)
	{
		List<String> segments = member.getSegments();
		
		return segments.isEmpty() || index.containsMember(qualifiedNameConverter.toString(nestingNamespace), segments.get(0));
	}
}

````
