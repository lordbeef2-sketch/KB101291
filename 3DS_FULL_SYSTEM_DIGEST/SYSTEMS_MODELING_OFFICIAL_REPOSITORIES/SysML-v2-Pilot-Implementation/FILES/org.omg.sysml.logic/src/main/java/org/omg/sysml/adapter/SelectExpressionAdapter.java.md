# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/SelectExpressionAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/SelectExpressionAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/SelectExpressionAdapter.java
- source_bytes: 2021
- source_sha256: `2276dfc9bf7a019736ad7c77ef62a92008eef04edb722ca3274e334c28ac665a`
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

package org.omg.sysml.adapter;

import org.eclipse.emf.common.util.EList;
import org.omg.sysml.lang.sysml.Expression;
import org.omg.sysml.lang.sysml.SelectExpression;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.util.ElementUtil;
import org.omg.sysml.util.TypeUtil;

public class SelectExpressionAdapter extends OperatorExpressionAdapter {

	public SelectExpressionAdapter(SelectExpression element) {
		super(element);
	}
	
	@Override
	public SelectExpression getTarget() {
		return (SelectExpression)super.getTarget();
	}

	/**
	 * @satisfies checkSelectExpressionResultSpecialization
	 */
	@Override
	protected void addResultTyping() {
		SelectExpression target = getTarget();
		EList<Expression> arguments = target.getArgument();
		if (!arguments.isEmpty()) {
			Expression collectionExpression = arguments.get(0);
			ElementUtil.transform(collectionExpression);
			TypeUtil.addImplicitGeneralTypeTo(target.getResult(),
					SysMLPackage.eINSTANCE.getSubsetting(), ((Expression)collectionExpression).getResult());
		}
	}
	
}

````
