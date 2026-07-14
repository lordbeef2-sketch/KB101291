# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/sequence/IncludingAtFunction.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/sequence/IncludingAtFunction.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/sequence/IncludingAtFunction.java
- source_bytes: 2372
- source_sha256: `4cc9ce1ca5a1a56a6909417e7a40b75fe3b46c1eb5723430ba6dfd6e12f11979`
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
 * You should have received a copy of theEclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *  
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 *  
 *******************************************************************************/
package org.omg.sysml.execution.expressions.functions.sequence;

import org.eclipse.emf.common.util.BasicEList;
import org.eclipse.emf.common.util.EList;
import org.omg.sysml.expressions.ExpressionEvaluator;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.InvocationExpression;
import org.omg.sysml.util.EvaluationUtil;

public class IncludingAtFunction extends SequenceFunction {

	@Override
	public String getFunctionName() {
		return "includingAt";
	}
	
	@Override
	public EList<Element> invoke(InvocationExpression invocation, Element target, ExpressionEvaluator evaluator) {
		EList<Element> seq = evaluator.evaluateArgument(invocation, 0, target);
		EList<Element> values = evaluator.evaluateArgument(invocation, 1, target);
		Element index = evaluator.argumentValue(invocation, 2, target);
		if (seq == null || values == null || index == null) {
			return EvaluationUtil.singletonList(invocation);
		} else {
			Object indexValue = EvaluationUtil.valueOf(index);
			if (!(indexValue == null || indexValue instanceof Integer)) {
				return EvaluationUtil.singletonList(invocation);
			} else {
				int i = indexValue == null? seq.size(): ((Integer)indexValue) - 1;
				if (i < 0) {
					i = 0;
				}
				EList<Element> result = new BasicEList<>(seq.subList(0, i));
				result.addAll(values);
				result.addAll(seq.subList(i, seq.size()));
				return result;
			}
		}
	}

}

````
