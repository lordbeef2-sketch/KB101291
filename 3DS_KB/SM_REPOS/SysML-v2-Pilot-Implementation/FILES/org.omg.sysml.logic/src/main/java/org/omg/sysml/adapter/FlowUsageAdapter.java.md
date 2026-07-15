# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/FlowUsageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/FlowUsageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/FlowUsageAdapter.java
- source_bytes: 3845
- source_sha256: `d0e484518af783b37baaf89e989b16c414d5c86cfcfdbf2c14a306774b1e347d`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021-2026 Model Driven Solutions, Inc.
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

import org.omg.sysml.lang.sysml.FlowUsage;
import org.omg.sysml.lang.sysml.OccurrenceUsage;
import org.omg.sysml.lang.sysml.PortionKind;
import org.omg.sysml.util.ConnectorUtil;
import org.omg.sysml.util.UsageUtil;

public class FlowUsageAdapter extends ConnectorAsUsageAdapter {

	public FlowUsageAdapter(FlowUsage feature) {
		super(feature);
	}
	
	@Override
	public FlowUsage getTarget() {
		return (FlowUsage)super.getTarget();
	}
	
	/**
	 * @satisfies checkActionUsageOwnedActionSpecialization
	 * @satisfies checkActionUsageSubactionSpecialization
	 * @satisfies checkStepEnclosedPerformanceSpecialization
	 * @satisfies checkStepOwnedPerformanceSpecialization
	 * @satisfies checkStepSubperformanceSpecialization
	 * @satisfies checkOccurrenceUsageTimeSliceSpecialization
	 * @satisfies checkOccurrenceUsageSnapshotSpecialization
	 * @satisfies checkOccurrenceUsageSuboccurrenceSpecialization
	 */
	@Override
	public void addDefaultGeneralType() {
		super.addDefaultGeneralType();
		
		// From OccurrenceAdapter
		if (isSuboccurrence()) {
			addDefaultGeneralType("suboccurrence");
		}
		PortionKind portionKind = getTarget().getPortionKind();
		if (portionKind  == PortionKind.SNAPSHOT) {
			addDefaultGeneralType("snapshot");
		} else if (portionKind == PortionKind.TIMESLICE) {
			addDefaultGeneralType("timeslice");
		}

		// From ActionUsageAdapter
		if (isActionOwnedComposite()) {
			addDefaultGeneralType("subaction");
		} else if (isPartOwnedComposite()) {
			addDefaultGeneralType("ownedAction");
		}
		
		// From StepAdapter
		if (isStructureOwnedComposite()) {
			addDefaultGeneralType("ownedPerformance");
		} else if (isBehaviorOwnedComposite()) {
			addDefaultGeneralType("subperformance");
		} else if (isBehaviorOwned()) {
			addDefaultGeneralType("enclosedPerformance");
		}
}
	
	@Override
	protected boolean isSuboccurrence() {
		OccurrenceUsage target = getTarget();
		return super.isSuboccurrence() ||
				target.isComposite() && 
			   	target.getOwningType() instanceof OccurrenceUsage;
	}
	
	/**
	 * @satisfies checkFlowUsageFlowSpecialization
	 * @satisfies checkFlowUsageSpecialization
	 */
	@Override
	protected String getDefaultSupertype() {
		return UsageUtil.isMessageConnection(getTarget())?
				getDefaultSupertype("message"):
				getDefaultSupertype("base");
	}
		
	/**
	 * @satisfies validateConnectorRelatedFeatures
	 * (For a FlowUsage that is a message.)
	 */
	protected void makeMessageAbstract() {
		super.postProcess();
		FlowUsage target = getTarget();
		if (UsageUtil.isMessageConnection(target) && target.getRelatedFeature().size() < 2) {
			target.setIsAbstract(true);
		}
	}
	
	@Override
	public void doTransform() {
		ConnectorUtil.transformConnectorEndsOf(getTarget());
		makeMessageAbstract();
		super.doTransform();
	}
	
}

````
