# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/test/java/org/omg/sysml/logic/InstantiationExpression_instantiatedType_InvocationDelegateTest.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/test/java/org/omg/sysml/logic/InstantiationExpression_instantiatedType_InvocationDelegateTest.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/test/java/org/omg/sysml/logic/InstantiationExpression_instantiatedType_InvocationDelegateTest.java
- source_bytes: 2201
- source_sha256: `334f35ba9d05814c7c2a02a59b5d236910bbee1d27ff91b43ce4c4c4b83b5b42`
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

import java.lang.reflect.InvocationTargetException;

import org.eclipse.emf.ecore.InternalEObject;
import org.junit.BeforeClass;
import org.junit.Test;
import org.omg.sysml.delegate.invocation.InstantiationExpression_instantiatedType_InvocationDelegate;
import org.omg.sysml.lang.sysml.InvocationExpression;
import org.omg.sysml.lang.sysml.SysMLFactory;
import org.omg.sysml.lang.sysml.SysMLPackage;

public class InstantiationExpression_instantiatedType_InvocationDelegateTest {

	@BeforeClass
	public static void setUp() {
		SysMLLogicStandaloneSetup.doSetup();
	}

	/**
	 * Test the call of InstantiationExpression_instantiatedType_InvocationDelegate will not throw an NPE
	 * @throws InvocationTargetException
	 */
	@Test
	public void incompleteInstantiationExpression() throws InvocationTargetException {
		InvocationExpression invocationExpression = SysMLFactory.eINSTANCE.createInvocationExpression();
		invocationExpression.getOwnedRelationship().add(SysMLFactory.eINSTANCE.createMembership());
		new InstantiationExpression_instantiatedType_InvocationDelegate(SysMLPackage.eINSTANCE.getInstantiationExpression__InstantiatedType())
			.dynamicInvoke((InternalEObject) invocationExpression,null);
	}
}

````
