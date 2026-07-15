# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/control/SelectFunction.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/control/SelectFunction.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/control/SelectFunction.java
- source_bytes: 1916
- source_sha256: `ca5ed325bf6856acc18fc5e1936cb1e1f352d0b7581f340ffab21fe68defac1f`
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
package org.omg.sysml.expressions.functions.control;

import java.util.function.BiFunction;

import org.eclipse.emf.common.util.EList;
import org.omg.sysml.expressions.ExpressionEvaluator;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.InvocationExpression;
import org.omg.sysml.util.EvaluationUtil;

public class SelectFunction extends ControlFunction {

	@Override
	public String getFunctionName() {
		return "select";
	}

	@Override
	public EList<Element> invoke(InvocationExpression invocation, Element target,
			ExpressionEvaluator evaluator) {
		return collectSelected(invocation, target, evaluator, new BiFunction<>() {
			@Override
			public EList<Element> apply(Element value, EList<Element> exprValue) {
				return exprValue != null && exprValue.size() == 1 && Boolean.TRUE.equals(EvaluationUtil.valueOf(exprValue.get(0)))?
						EvaluationUtil.singletonList(value):
						EvaluationUtil.nullList();
			}			
		});
	}

}

````
