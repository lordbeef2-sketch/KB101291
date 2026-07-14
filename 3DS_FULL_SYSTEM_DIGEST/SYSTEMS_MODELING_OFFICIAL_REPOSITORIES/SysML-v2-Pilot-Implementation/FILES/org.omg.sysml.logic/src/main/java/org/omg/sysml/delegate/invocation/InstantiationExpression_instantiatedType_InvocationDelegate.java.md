# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/InstantiationExpression_instantiatedType_InvocationDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/InstantiationExpression_instantiatedType_InvocationDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/InstantiationExpression_instantiatedType_InvocationDelegate.java
- source_bytes: 2156
- source_sha256: `a158f50b2bd36102ef23359ec6c7bf43400ed2b35ddeacf48762901b4f7a1bb1`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2025 Model Driven Solutions, Inc.
 * Copyright (c) 2026 Obeo
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

package org.omg.sysml.delegate.invocation;

import java.lang.reflect.InvocationTargetException;
import java.util.Objects;

import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.InternalEObject;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.FeatureMembership;
import org.omg.sysml.lang.sysml.InstantiationExpression;
import org.omg.sysml.lang.sysml.Membership;
import org.omg.sysml.lang.sysml.Type;

public class InstantiationExpression_instantiatedType_InvocationDelegate extends Expression_evaluate_InvocationDelegate {

	public InstantiationExpression_instantiatedType_InvocationDelegate(EOperation operation) {
		super(operation);
	}
	
	@Override
	public Object dynamicInvoke(InternalEObject target, EList<?> arguments) throws InvocationTargetException {
		InstantiationExpression self = (InstantiationExpression) target;
		Element member = self.getOwnedMembership().stream()
			.filter(m->!(m instanceof FeatureMembership))
			.map(Membership::getMemberElement)
			.filter(Objects::nonNull)
			.findFirst()
			.orElse(null);
		return member instanceof Type ? member: null;
	}

}

````
