# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/test/java/org/omg/sysml/logic/SysMLLibraryUtilTest.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/test/java/org/omg/sysml/logic/SysMLLibraryUtilTest.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/test/java/org/omg/sysml/logic/SysMLLibraryUtilTest.java
- source_bytes: 2559
- source_sha256: `0463f1d564b3f0ac073a76f2fbf036e2b4dbaa6c77bbc17b6cfb72bd7bfd6997`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2026 Obeo
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Eclipse Public License as published by
 * the Eclipse Foundation, version 2 of the License.
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * Eclipse Public License for more details.
 *
 * You should have received a copy of theEclipse Public License
 * along with this program. If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 *
 *******************************************************************************/

package org.omg.sysml.logic;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.resource.impl.ResourceImpl;
import org.junit.Test;
import org.omg.sysml.util.SysMLLibraryUtil;

/**
 * Verifies classification of EMF resources as SysML/KerML model-library
 * resources.
 */
public class SysMLLibraryUtilTest {

	@Test
	public void nullResourceIsNotLibraryResource() {
		assertFalse(SysMLLibraryUtil.isLibraryResource(null));
	}

	@Test
	public void resourceWithoutUriIsNotLibraryResource() {
		assertFalse(SysMLLibraryUtil.isLibraryResource(new ResourceImpl()));
	}

	@Test
	public void configuredModelLibraryDirectoryIsLibraryResource() {
		SysMLLibraryUtil.setModelLibraryDirectory("/tmp/sysml.library");

		ResourceImpl resource = new ResourceImpl(URI.createFileURI("/tmp/sysml.library/Base.sysml"));

		assertTrue(SysMLLibraryUtil.isLibraryResource(resource));
	}

	@Test
	public void conventionalModelLibraryFolderIsLibraryResource() {
		SysMLLibraryUtil.setModelLibraryDirectory("/tmp/other-library");

		ResourceImpl resource = new ResourceImpl(URI.createURI("platform:/resource/sysml.library/Base.sysml"));

		assertTrue(SysMLLibraryUtil.isLibraryResource(resource));
	}

	@Test
	public void ordinaryModelResourceIsNotLibraryResource() {
		SysMLLibraryUtil.setModelLibraryDirectory("/tmp/sysml.library");

		ResourceImpl resource = new ResourceImpl(URI.createFileURI("/tmp/model/Test.sysml"));

		assertFalse(SysMLLibraryUtil.isLibraryResource(resource));
	}
}

````
