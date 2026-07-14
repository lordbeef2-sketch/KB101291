# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/OperatorExpressionAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/OperatorExpressionAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/OperatorExpressionAdapter.java
- source_bytes: 1810
- source_sha256: `0d2db33d836c908b735a018589e07e74e8b8825f15d7eff7dc9bd2ed7f60f535`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021-2024 Model Driven Solutions, Inc.
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

package org.omg.sysml.adapter;

import org.omg.sysml.lang.sysml.OperatorExpression;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.util.ExpressionUtil;

public class OperatorExpressionAdapter extends InvocationExpressionAdapter {
	
	public OperatorExpressionAdapter(OperatorExpression element) {
		super(element);
	}
	
	@Override
	public OperatorExpression getTarget() {
		return (OperatorExpression)super.getTarget();
	}
	
	/**
	 * @satisfies checkOperatorExpressionSpecialization
	 */
	@Override
	public void computeImplicitGeneralTypes() {
		OperatorExpression target = getTarget();
		String operator = target.getOperator();
		if (operator != null) {
			addDefaultGeneralType(SysMLPackage.eINSTANCE.getFeatureTyping(), ExpressionUtil.getOperatorQualifiedNames(operator));
		}
		super.computeImplicitGeneralTypes();
	}
	
}

````
