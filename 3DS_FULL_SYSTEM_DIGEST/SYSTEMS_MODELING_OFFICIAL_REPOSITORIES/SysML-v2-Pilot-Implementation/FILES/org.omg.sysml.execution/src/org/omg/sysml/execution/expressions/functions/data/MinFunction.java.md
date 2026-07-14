# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/data/MinFunction.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/data/MinFunction.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/data/MinFunction.java
- source_bytes: 1818
- source_sha256: `dc5edb7aff9997ae17fafee86829c3e1b81570ac57ac649f0e5bf37ad17c2503`
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
 * You should have received a copy of theEclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *  
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 *  
 *******************************************************************************/

package org.omg.sysml.execution.expressions.functions.data;

import org.eclipse.emf.common.util.EList;
import org.omg.sysml.expressions.functions.data.ArithmeticFunction;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.util.EvaluationUtil;

public class MinFunction extends ArithmeticFunction {
	
	@Override
	public String getFunctionName() {
		return "min";
	}
	
	@Override
	protected EList<Element> binaryIntegerOp(int x, int y) {
		return x < y? EvaluationUtil.integerResult(x): EvaluationUtil.integerResult(y);
	}
	
	@Override
	protected EList<Element> binaryRealOp(double x, double y) {
		return x < y? EvaluationUtil.realResult(x): EvaluationUtil.realResult(y);
	}

	@Override
	protected EList<Element> binaryStringOp(String x, String y) {
		return x.compareTo(y) < 0? EvaluationUtil.stringResult(x): EvaluationUtil.stringResult(y);
	}

}

````
