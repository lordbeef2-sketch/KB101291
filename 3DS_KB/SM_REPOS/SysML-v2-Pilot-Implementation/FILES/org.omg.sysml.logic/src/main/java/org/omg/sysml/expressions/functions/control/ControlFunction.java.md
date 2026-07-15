# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/control/ControlFunction.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/control/ControlFunction.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/control/ControlFunction.java
- source_bytes: 2448
- source_sha256: `99cbba34372e84d1df57e539fbdd20bfa0d76b9bd277dc8bb2bd15d0a03629a6`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021, 2025-2026 Model Driven Solutions, Inc.
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

package org.omg.sysml.expressions.functions.control;

import java.util.function.BiFunction;

import org.eclipse.emf.common.util.BasicEList;
import org.eclipse.emf.common.util.EList;
import org.omg.sysml.expressions.ExpressionEvaluator;
import org.omg.sysml.expressions.functions.LibraryFunction;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.Expression;
import org.omg.sysml.lang.sysml.InvocationExpression;
import org.omg.sysml.util.EvaluationUtil;

public abstract class ControlFunction implements LibraryFunction {

	@Override
	public String getPackageName() {
		return "ControlFunctions";
	}

	protected EList<Element> collectSelected(InvocationExpression invocation, Element target,
			ExpressionEvaluator evaluator,
			BiFunction<Element, EList<Element>, EList<Element>> select) {
		EList<Element> list = evaluator.evaluateArgument(invocation, 0, target);
		Element expr = evaluator.argumentValue(invocation, 1, target);
		if (list == null || !(expr instanceof Expression)) {
			return EvaluationUtil.singletonList(invocation);
		} else {
			EList<Element> result = new BasicEList<>();
			for (Element value: list) {
				if (value == null) {
					return EvaluationUtil.singletonList(invocation);
				} else {
					EList<Element> exprValue = evaluator.evaluateExpression((Expression)expr, target, value);
					if (exprValue != null) {
						result.addAll(select.apply(value, exprValue));
					}
				}
			}
			return result;
		}
	}
}

````
