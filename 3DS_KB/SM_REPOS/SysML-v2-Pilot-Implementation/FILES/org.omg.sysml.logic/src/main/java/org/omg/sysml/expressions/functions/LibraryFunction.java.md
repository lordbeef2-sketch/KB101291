# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/LibraryFunction.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/LibraryFunction.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/expressions/functions/LibraryFunction.java
- source_bytes: 1810
- source_sha256: `c10deb75fe7ab60969d2e0895cfdb954c8b35f131d7d3464a068329686096339`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021-2022, 2025 Model Driven Solutions, Inc.
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
package org.omg.sysml.expressions.functions;

import org.eclipse.emf.common.util.EList;
import org.omg.sysml.expressions.ExpressionEvaluator;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.InvocationExpression;

public interface LibraryFunction {
	
	abstract public String getPackageName();

	public default String getFunctionName() {
		return null;
	}
	
	public default String[] getFunctionNames() {
		String op = getFunctionName();
		return op == null? new String[] {}: new String[] {op};
	}
	
	public default String[] getQualifiedNames() {
		String[] names = getFunctionNames();
		for (int i = 0; i < names.length; i++) {
			names[i] = getPackageName() + "::" + names[i];
		}
		return names;
	}
	
	public EList<Element> invoke(InvocationExpression invocation, Element target, ExpressionEvaluator evaluator);

}

````
