# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/control/ForAllFunction.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/control/ForAllFunction.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/control/ForAllFunction.java
- source_bytes: 2548
- source_sha256: `824bc0c1b3c361ede3a4e77502fb6da0285da71eaf972adea062d6088d6b25cf`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2026 Model Driven Solutions, Inc.
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
package org.omg.sysml.execution.expressions.functions.control;

import org.eclipse.emf.common.util.EList;
import org.omg.sysml.expressions.ExpressionEvaluator;
import org.omg.sysml.expressions.functions.control.ControlFunction;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.Expression;
import org.omg.sysml.lang.sysml.InvocationExpression;
import org.omg.sysml.util.EvaluationUtil;

public class ForAllFunction extends ControlFunction {

	@Override
	public String getFunctionName() {
		return "forAll";
	}

	public Boolean forAll(InvocationExpression invocation, Element target,
			ExpressionEvaluator evaluator, Boolean test) {
		EList<Element> list = evaluator.evaluateArgument(invocation, 0, target);
		Element expr = evaluator.argumentValue(invocation, 1, target);
		if (list == null || !(expr instanceof Expression)) {
			return null;
		} else {
			for (Element value: list) {
				if (value == null) {
					return null;
				} else {
					EList<Element> exprValue = evaluator.evaluateExpression((Expression)expr, target, value);
					if (exprValue == null || exprValue.size() != 1) {
						return null;
					} else if (!test.equals(EvaluationUtil.valueOf(exprValue.get(0)))) {
						return false;
					}
				}
			}
			return true;
		}
	}
	
	@Override
	public EList<Element> invoke(InvocationExpression invocation, Element target,
			ExpressionEvaluator evaluator) {
		Boolean result = forAll(invocation, target, evaluator, true);
		return result == null? EvaluationUtil.singletonList(invocation): EvaluationUtil.booleanResult(result);
	}

}

````
