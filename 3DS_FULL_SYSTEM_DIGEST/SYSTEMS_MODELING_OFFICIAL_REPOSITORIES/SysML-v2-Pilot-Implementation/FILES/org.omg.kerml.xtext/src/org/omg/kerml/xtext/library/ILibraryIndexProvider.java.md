# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xtext/src/org/omg/kerml/xtext/library/ILibraryIndexProvider.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xtext/src/org/omg/kerml/xtext/library/ILibraryIndexProvider.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xtext/src/org/omg/kerml/xtext/library/ILibraryIndexProvider.java
- source_bytes: 1773
- source_sha256: `842a0cd59d07e87449664dcd0afe4bc22b6cc1b56e3ea6a04297c6e3ec1c8799`
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

import org.eclipse.emf.ecore.resource.Resource;

/**
 * Common interface for providing pre-calculated library indexes for library resources.
 * The indexes are used by the
 * {@link org.omg.kerml.xtext.library.LibraryNamespaces LibraryNamespaces}
 * during name resolution.
 */
public interface ILibraryIndexProvider {
	/**
	 * Use this method to return a library index for a given resource. Return an
	 * {@link org.omg.kerml.xtext.library.LibraryIndex#EMPTY_INDEX empty index} in case there is no
	 * index for the given resource. Never return null.
	 */
	 public LibraryIndex getIndexFor(Resource resource);
	 
	 /**
	  * Use this method to disable the library index.
	  */
	 public void setIndexDisabled(boolean doNotUse);
	 
	 public boolean isIndexDisabled();
	 
	 /**
	  * Use this method to dispose the library index for a given method. 
	  */
	 public void dropIndexOf(Resource resource);
}

````
