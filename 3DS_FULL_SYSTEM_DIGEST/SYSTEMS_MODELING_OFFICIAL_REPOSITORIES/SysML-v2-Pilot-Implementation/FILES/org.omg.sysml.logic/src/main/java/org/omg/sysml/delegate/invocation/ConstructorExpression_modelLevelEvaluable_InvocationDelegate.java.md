# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/ConstructorExpression_modelLevelEvaluable_InvocationDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/ConstructorExpression_modelLevelEvaluable_InvocationDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/ConstructorExpression_modelLevelEvaluable_InvocationDelegate.java
- source_bytes: 1900
- source_sha256: `a8574a9633872cf233af244d7a7a1226c450f461f2fd50ada4d98ba644422ece`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2025 Model Driven Solutions, Inc.
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

import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.InternalEObject;
import org.omg.sysml.lang.sysml.ConstructorExpression;
import org.omg.sysml.lang.sysml.Feature;

public class ConstructorExpression_modelLevelEvaluable_InvocationDelegate extends Expression_modelLevelEvaluable_InvocationDelegate {

	public ConstructorExpression_modelLevelEvaluable_InvocationDelegate(EOperation operation) {
		super(operation);
	}
	
	@Override
	public Object dynamicInvoke(InternalEObject target, EList<?> arguments) throws InvocationTargetException {
		ConstructorExpression self = (ConstructorExpression) target;
		@SuppressWarnings("unchecked")
		EList<Feature> visited = (EList<Feature>) arguments.get(0);

		return self.getArgument().stream().allMatch(arg->arg.modelLevelEvaluable(visited));
	}
}

````
