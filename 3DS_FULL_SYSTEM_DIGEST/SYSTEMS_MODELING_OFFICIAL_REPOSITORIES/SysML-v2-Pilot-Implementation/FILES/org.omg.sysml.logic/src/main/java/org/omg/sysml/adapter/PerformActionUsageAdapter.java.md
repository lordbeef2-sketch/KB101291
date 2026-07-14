# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/PerformActionUsageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/PerformActionUsageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/PerformActionUsageAdapter.java
- source_bytes: 1540
- source_sha256: `01bee6371165016095e930c89a6c21c4e205d04f87b6b394f8046c20c876ddc0`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021, 2022 Model Driven Solutions, Inc.
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

import org.omg.sysml.lang.sysml.PerformActionUsage;

public class PerformActionUsageAdapter extends ActionUsageAdapter {

	public PerformActionUsageAdapter(PerformActionUsage element) {
		super(element);
	}
	
	@Override
	public PerformActionUsage getTarget() {
		return (PerformActionUsage)super.getTarget();
	}
	
	/**
	 * @satisfies checkPerformActionUsageSpecialization
	 */
	@Override
	public void addDefaultGeneralType() {
		super.addDefaultGeneralType();
		if (isPerformedAction()) {
			addDefaultGeneralType("performedAction");
		}
	}
		
}

````
