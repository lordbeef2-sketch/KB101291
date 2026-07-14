# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/sequence/SequenceFunction.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/sequence/SequenceFunction.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.execution/src/org/omg/sysml/execution/expressions/functions/sequence/SequenceFunction.java
- source_bytes: 1223
- source_sha256: `aa6a6984cb3feb3bdd2929799a5fe94d3c762c6c7b147d736e43eedd109a23ae`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021, 2025 Model Driven Solutions, Inc.
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

import org.omg.sysml.expressions.functions.LibraryFunction;

public abstract class SequenceFunction implements LibraryFunction {

	@Override
	public String getPackageName() {
		return "SequenceFunctions";
	}

}

````
