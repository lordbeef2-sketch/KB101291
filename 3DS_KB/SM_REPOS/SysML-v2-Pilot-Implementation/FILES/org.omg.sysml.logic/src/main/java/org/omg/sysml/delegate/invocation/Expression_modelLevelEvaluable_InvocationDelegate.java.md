# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Expression_modelLevelEvaluable_InvocationDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Expression_modelLevelEvaluable_InvocationDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Expression_modelLevelEvaluable_InvocationDelegate.java
- source_bytes: 2515
- source_sha256: `baf43ad65ee7b6cf2239599c3ed2afa556940524f8d4bb3a75fe8fb7d0ec2be2`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2024 Model Driven Solutions, Inc.
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
import java.util.List;

import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.util.BasicInvocationDelegate;
import org.omg.sysml.lang.sysml.Expression;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.FeatureDirectionKind;
import org.omg.sysml.util.ExpressionUtil;
import org.omg.sysml.util.FeatureUtil;
import org.omg.sysml.util.TypeUtil;

public class Expression_modelLevelEvaluable_InvocationDelegate extends BasicInvocationDelegate {

	public Expression_modelLevelEvaluable_InvocationDelegate(EOperation operation) {
		super(operation);
	}
	
	@Override
	public Object dynamicInvoke(InternalEObject target, EList<?> arguments) throws InvocationTargetException {
		Expression self = (Expression) target;
		@SuppressWarnings("unchecked")
		EList<Feature> visited = (EList<Feature>) arguments.get(0);

		List<Feature> parameters = TypeUtil.getAllParametersOf(self);
		Feature result = self.getResult();
		if (!parameters.stream().allMatch(param->
				(self.directionOf(param) == FeatureDirectionKind.IN || param == result) && 
				param.getOwnedFeature().isEmpty() &&
				FeatureUtil.getValuationFor(param) == null)) {
			return false;
		} else {
			Expression resultExpression = ExpressionUtil.getResultExpressionOf(self);
			return resultExpression == null || resultExpression.modelLevelEvaluable(visited);
		}
	}

}

````
