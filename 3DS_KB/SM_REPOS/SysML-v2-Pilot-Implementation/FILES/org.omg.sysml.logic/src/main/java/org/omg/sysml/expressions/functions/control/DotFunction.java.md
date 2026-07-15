# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/control/DotFunction.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/control/DotFunction.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/control/DotFunction.java
- source_bytes: 2718
- source_sha256: `1a35ef9c9a91601ca658042b1eca36e899709aa888342f68c39d964e2c9cad0e`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2022 Model Driven Solutions, Inc.
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

import org.eclipse.emf.common.util.BasicEList;
import org.eclipse.emf.common.util.EList;
import org.omg.sysml.expressions.ExpressionEvaluator;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.InvocationExpression;
import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.util.EvaluationUtil;
import org.omg.sysml.util.ExpressionUtil;

public class DotFunction extends ControlFunction {

	@Override
	public String[] getFunctionNames() {
		return new String[]{"'.'"};
	}

	@Override
	public EList<Element> invoke(InvocationExpression invocation, Element target, ExpressionEvaluator evaluator) {
		EList<Element> list = evaluator.evaluateArgument(invocation, 0, target);			
		if (list != null) {
			Element targetFeature = ExpressionUtil.getTargetFeatureFor(invocation);
			if (targetFeature instanceof Feature) {
				Type type = target instanceof Type? (Type)target: null;
				EList<Element> result = new BasicEList<>();
				for (Element element: list) {
					if (element instanceof Feature) {
						EList<Feature> chainingFeatures = new BasicEList<>();
						chainingFeatures.add((Feature)element);
						EList<Feature> targetChainingFeatures = ((Feature) targetFeature).getChainingFeature();
						if (targetChainingFeatures.isEmpty()) {
							chainingFeatures.add((Feature)targetFeature);
						} else {
							chainingFeatures.addAll(targetChainingFeatures);
						}
						EList<Element> value = evaluator.evaluateFeatureChain(chainingFeatures, type);
						if (value != null) {
							result.addAll(value);
						}
					}
				}
				return result;
			}
		}
		return EvaluationUtil.singletonList(invocation);
	}

}

````
