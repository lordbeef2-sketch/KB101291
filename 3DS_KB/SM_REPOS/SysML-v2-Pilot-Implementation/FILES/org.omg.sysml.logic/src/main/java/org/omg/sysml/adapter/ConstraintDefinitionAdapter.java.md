# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConstraintDefinitionAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConstraintDefinitionAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConstraintDefinitionAdapter.java
- source_bytes: 1516
- source_sha256: `016d7a3d2929e77af039d95ddfb4b544f8cff85c6151587c55e0e5991434f0eb`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021, 2024, 2025 Model Driven Solutions, Inc.
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

import org.omg.sysml.lang.sysml.ConstraintDefinition;

public class ConstraintDefinitionAdapter extends OccurrenceDefinitionAdapter {

	public ConstraintDefinitionAdapter(ConstraintDefinition element) {
		super(element);
	}
	
	@Override
	public ConstraintDefinition getTarget() {
		return (ConstraintDefinition)super.getTarget();
	}
	
	/**
	 * @satisfies checkFunctionResultBindingConnector
	 */
	@Override
	public void doTransform() {
		super.doTransform();
		createResultConnector(getTarget().getResult());		
	}
	
}

````
