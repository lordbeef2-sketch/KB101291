# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/FlowAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/FlowAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/FlowAdapter.java
- source_bytes: 2280
- source_sha256: `9e9c1cef0c4799e45ede462d48a659a2b19826e204959dc48e28b9cdd0522895`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021, 2022, 2025 Model Driven Solutions, Inc.
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

import org.omg.sysml.lang.sysml.Flow;
import org.omg.sysml.util.ConnectorUtil;

public class FlowAdapter extends ConnectorAdapter {

	public FlowAdapter(Flow feature) {
		super(feature);
	}
	
	@Override
	public Flow getTarget() {
		return (Flow)super.getTarget();
	}
	
	/**
	 * @satisfies checkStepOwnedPerformanceSpecialization
	 * @satisfies checkStepSubperformanceSpecialization
	 * @satisfies checkStepEnclosedPerformanceSpecialization
	 */
	@Override
	public void addDefaultGeneralType() {
		super.addDefaultGeneralType();
		if (isStructureOwnedComposite()) {
			addDefaultGeneralType("ownedPerformance");
		}
		if (isBehaviorOwnedComposite()) {
			addDefaultGeneralType("subperformance");
		}
		if (isBehaviorOwned()) {
			addDefaultGeneralType("enclosedPerformance");
		}
	}

	/**
	 * @satisfies checkFlowSpecialization
	 * @satisfies checkFlowWithEndsSpecialization
	 */
	@Override
	protected String getDefaultSupertype() {
		return isFlowTransfer()? getDefaultSupertype("flow"):
			   getDefaultSupertype("base");
	}
	
	protected boolean isFlowTransfer() {
		return !getTarget().getOwnedEndFeature().isEmpty();
	}
		
	@Override
	public void doTransform() {
		ConnectorUtil.transformConnectorEndsOf(getTarget());
		super.doTransform();
	}
	
}

````
