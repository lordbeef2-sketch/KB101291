# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/logic/SysMLLogicStandaloneSetup.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/logic/SysMLLogicStandaloneSetup.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/logic/SysMLLogicStandaloneSetup.java
- source_bytes: 3120
- source_sha256: `d6325f69369a9129ad942951d33d1f8d9ab5d75801875bfa59dfea548854d5a2`
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

import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.omg.sysml.delegate.invocation.OperationInvocationDelegateFactory;
import org.omg.sysml.delegate.setting.DerivedPropertySettingDelegateFactory;
import org.omg.sysml.logic.api.IModelLibraryProvider;
import org.omg.sysml.util.SysMLLibraryUtil;

/**
 * Standalone bootstrap for applications using {@code org.omg.sysml.logic}
 * without Xtext or Eclipse.
 *
 * <p>Call this before creating SysML model instances so generated EMF classes
 * cache the SysML-specific setting and invocation delegates.
 */
public final class SysMLLogicStandaloneSetup {

	private static final IModelLibraryProvider DEFAULT_LIBRARY_PROVIDER = new ResourceSetModelLibraryProvider();

	/**
	 * Utility class; not meant to be instantiated.
	 */
	private SysMLLogicStandaloneSetup() {
	}

	/**
	 * Installs the default standalone logic bootstrap using a plain-EMF library
	 * provider.
	 *
	 * <p>Call this before creating or loading SysML model instances that rely on
	 * SysML setting or invocation delegates.
	 */
	public static void doSetup() {
		doSetup(DEFAULT_LIBRARY_PROVIDER);
	}

	/**
	 * Installs the standalone logic bootstrap using the given library provider.
	 *
	 * <p>This registers the SysML derived-property setting delegate factory and
	 * operation invocation delegate factory in the global EMF registries, then
	 * installs the supplied provider for library element lookup.
	 *
	 * @param libraryProvider the provider used to resolve SysML/KerML library
	 *        elements in standalone mode
	 */
	public static void doSetup(IModelLibraryProvider libraryProvider) {
		EStructuralFeature.Internal.SettingDelegate.Factory.Registry.INSTANCE.put(
				DerivedPropertySettingDelegateFactory.SYSML_ANNOTATION,
				new DerivedPropertySettingDelegateFactory());
		EOperation.Internal.InvocationDelegate.Factory.Registry.INSTANCE.put(
				OperationInvocationDelegateFactory.SYSML_ANNOTATION,
				new OperationInvocationDelegateFactory());
		SysMLLibraryUtil.setProviderLookup(resource -> libraryProvider);
	}
}

````
