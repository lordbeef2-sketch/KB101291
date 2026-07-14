# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/base/AtFunction.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/base/AtFunction.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/base/AtFunction.java
- source_bytes: 1913
- source_sha256: `9ed0eaa7bbf2471d1edd35d80a5bee04cc9a639724b3dfe2ad5040ed30f55db6`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021-2022 Model Driven Solutions, Inc.
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
 * You should have received a copy of theEclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *  
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 *  
 *******************************************************************************/

package org.omg.sysml.expressions.functions.base;

import org.eclipse.emf.common.util.EList;
import org.omg.sysml.expressions.ExpressionEvaluator;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.InvocationExpression;
import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.util.EvaluationUtil;

public class AtFunction extends BaseFunction {
	
	@Override
	public String getFunctionName() {
		return "'@'";
	}

	@Override
	public EList<Element> invoke(InvocationExpression invocation, Element target, ExpressionEvaluator evaluator) {
		Type testedType = EvaluationUtil.getTypeArgument(invocation);
		if (testedType != null) {
			EList<Element> values = evaluator.evaluateArgument(invocation, 0, target);
			if (values != null) {
				return EvaluationUtil.booleanResult(values.stream().anyMatch(value->EvaluationUtil.isType(invocation, value, testedType)));
			}
		}
		return EvaluationUtil.singletonList(invocation);
	}

}

````
