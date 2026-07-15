# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/StateUsageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/StateUsageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/StateUsageAdapter.java
- source_bytes: 1728
- source_sha256: `565b640f34e851d16aeb175ec67e5b859c49289bd25e95a8bd2e76c74df37306`
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

import org.omg.sysml.lang.sysml.StateUsage;

public class StateUsageAdapter extends ActionUsageAdapter {

	public StateUsageAdapter(StateUsage element) {
		super(element);
	}
	
	@Override
	public StateUsage getTarget() {
		return (StateUsage)super.getTarget();
	}
	
	/**
	 * @satisfies checkStateUsageExclusiveStateSpecialization
	 * @satisfies checkStateUsageSubstateSpecialization
	 */
	@Override
	protected String getSubactionType() {
		return isExclusiveState()? "exclusiveState":
			   isSubstate()? "substate": 
			   super.getSubactionType();	
	}
	
	public boolean isExclusiveState() {
		return getTarget().isSubstateUsage(false);
	}
		
	public boolean isSubstate() {
		return getTarget().isSubstateUsage(true);
	}
	
}

````
