# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/base/EqualsFunction.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/base/EqualsFunction.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/base/EqualsFunction.java
- source_bytes: 2682
- source_sha256: `654dbec4df37a3ca03f473dd7c25321e860b16940908b95eba79381f692dd8d2`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021, 2026 Model Driven Solutions, Inc.
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
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.InvocationExpression;
import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.util.EvaluationUtil;
import org.omg.sysml.util.ExpressionUtil;
import org.omg.sysml.util.TypeUtil;

public class EqualsFunction extends BaseFunction {

	@Override
	public String getFunctionName() {
		return "'=='";
	}

	protected boolean isCollection(InvocationExpression invocation, EList<Element> values) {
		Type collectionType = ExpressionUtil.getCollectionDataType(invocation);
		return values != null && values.size() == 1 && values.get(0) instanceof Type && 
			   TypeUtil.specializes((Type)values.get(0), collectionType);
	}
	
	protected boolean compare(EList<Element> x, EList<Element> y) {
		// Note: This allows comparison of arbitrary lists, even though the '==' function args have multiplicity 0..1.
		return EvaluationUtil.equal(x, y);
	}
	
	@Override
	public EList<Element> invoke(InvocationExpression invocation, Element target, ExpressionEvaluator evaluator) {
		EList<Element> x = evaluator.evaluateArgument(invocation, 0, target);
		EList<Element> y = evaluator.evaluateArgument(invocation, 1, target);
		if (isCollection(invocation, x) && isCollection(invocation, y)) {
			x = EvaluationUtil.getElementsOf((Feature)x.get(0), evaluator);
			y = EvaluationUtil.getElementsOf((Feature)y.get(0), evaluator);
		}
		return x == null || y == null? EvaluationUtil.singletonList(invocation): 			
			EvaluationUtil.booleanResult(compare(x, y));
	}

}

````
