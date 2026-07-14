# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/numerical/ProdFunction.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/numerical/ProdFunction.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/numerical/ProdFunction.java
- source_bytes: 2478
- source_sha256: `9aff432be8050d52b960a6371661a5d5fb5b038e87e9242dc0584842ac7e62d0`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2022, 2025 Model Driven Solutions, Inc.
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

package org.omg.sysml.execution.expressions.functions.numerical;

import org.eclipse.emf.common.util.EList;
import org.omg.sysml.expressions.ExpressionEvaluator;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.InvocationExpression;
import org.omg.sysml.lang.sysml.LiteralInteger;
import org.omg.sysml.lang.sysml.LiteralRational;
import org.omg.sysml.util.EvaluationUtil;

public class ProdFunction extends NumericalFunction {

	@Override
	public String getFunctionName() {
		return "product";
	}

	@Override
	public EList<Element> invoke(InvocationExpression invocation, Element target, ExpressionEvaluator evaluator) {
		EList<Element> list = evaluator.evaluateArgument(invocation, 0, target);
		if (list == null) {
			return EvaluationUtil.singletonList(invocation);
		} else {
			int intResult = 1;
			Double realResult = null;
			for (Element element: list) {
				if (element instanceof LiteralInteger) {
					int value = ((LiteralInteger)element).getValue();
					if (realResult != null) {
						realResult *= value;
					} else {
						intResult *= value;
					}
				} else if (element instanceof LiteralRational) {
					if (realResult == null) {
						realResult = (double) intResult;
					}
					realResult *= ((LiteralRational)element).getValue();
				} else {
					return EvaluationUtil.singletonList(invocation);
				}
			}
			return realResult == null? 
						EvaluationUtil.integerResult(intResult):
						EvaluationUtil.realResult(realResult);
		}
	}

}

````
