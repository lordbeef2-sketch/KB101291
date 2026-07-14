# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/control/ReduceFunction.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/control/ReduceFunction.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/control/ReduceFunction.java
- source_bytes: 2893
- source_sha256: `ff0f1d04184d7454f9e5d5f9a7ffc71901513b5ff5ad83db6411e438597e654d`
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

import java.util.function.BiFunction;

import org.eclipse.emf.common.util.EList;
import org.omg.sysml.expressions.ExpressionEvaluator;
import org.omg.sysml.expressions.functions.control.ControlFunction;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.Expression;
import org.omg.sysml.lang.sysml.InvocationExpression;
import org.omg.sysml.util.EvaluationUtil;

public class ReduceFunction extends ControlFunction {

	@Override
	public String getFunctionName() {
		return "reduce";
	}

	protected EList<Element> reduce(InvocationExpression invocation, EList<Element> list,
			BiFunction<Element, Element, Element> compute) {
		Element result = null;
		for (Element value: list) {
			if (value == null) {
				return EvaluationUtil.singletonList(invocation);
			} else {
				result = compute.apply(result, value);
				if (result == null) {
					return EvaluationUtil.singletonList(invocation);
				}
			}
		}
		return EvaluationUtil.singletonList(result);
	}

	@Override
	public EList<Element> invoke(InvocationExpression invocation, Element target,
			ExpressionEvaluator evaluator) {
		EList<Element> list = evaluator.evaluateArgument(invocation, 0, target);
		Element expr = evaluator.argumentValue(invocation, 1, target);
		if (list == null || !(expr instanceof Expression)) {
			return EvaluationUtil.singletonList(invocation);
		} else if (list.isEmpty()) {
			return EvaluationUtil.nullList();
		} else {
			return reduce(invocation, list, new BiFunction<>() {
				@Override
				public Element apply(Element result, Element value) {
					if (result == null) {
						return value;
					} else {
						EList<Element> exprValue = evaluator.evaluateExpression((Expression)expr, target, result, value);
						return exprValue == null || exprValue.size() != 1? null: exprValue.get(0);	
					}
				}			
			});
		}
	}

}

````
