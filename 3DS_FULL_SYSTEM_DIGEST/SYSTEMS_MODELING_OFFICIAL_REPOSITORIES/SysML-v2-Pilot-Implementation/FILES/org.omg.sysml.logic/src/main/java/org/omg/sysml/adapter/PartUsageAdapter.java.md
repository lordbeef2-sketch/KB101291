# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/PartUsageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/PartUsageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/PartUsageAdapter.java
- source_bytes: 3161
- source_sha256: `7f854166bea59328d75059af322b4c765a1c8456f9fdfd16c5d205928ffdb4a5`
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

package org.omg.sysml.adapter;

import org.omg.sysml.lang.sysml.CaseDefinition;
import org.omg.sysml.lang.sysml.CaseUsage;
import org.omg.sysml.lang.sysml.PartUsage;
import org.omg.sysml.lang.sysml.RequirementDefinition;
import org.omg.sysml.lang.sysml.RequirementUsage;
import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.util.UsageUtil;

public class PartUsageAdapter extends ItemUsageAdapter {

	public PartUsageAdapter(PartUsage element) {
		super(element);
	}
	
	public PartUsage getTarget() {
		return (PartUsage)super.getTarget();
	}
	
	/**
	 * @satisfies checkPartUsageActorSpecialization
	 * @satisfies checkPartUsageStakeholderSpecialization
	 * @satisfies checkPartUsageSubpartSpecialization
	 */
	@Override
	protected String getDefaultSupertype() {
		return isRequirementActor()? getDefaultSupertype("requirementActor"):
			   isRequirementStakeholder()? getDefaultSupertype("requirementStakeholder"):
			   isCaseActor()? getDefaultSupertype("caseActor"):
			   super.getDefaultSupertype();
	}
	
	protected boolean isRequirementActor() {
		PartUsage target = getTarget();
		Type owningType = target.getOwningType();
		return UsageUtil.isActorParameter(target) &&
			   ( owningType instanceof RequirementDefinition ||
				 owningType instanceof RequirementUsage);
	}

	protected boolean isRequirementStakeholder() {
		/*
		 * Note: checkPartUsageStakeholderSpecialization OCL doesn't explicitly require the owningType 
		 * to be a RequirmentDefinition or RequirementUsage. However, a valid stakeholder must be owned
		 * by a RequirementDefinition or RequirementUsage and, if it isn't the implied subsetting won't
		 * be valid, so don't add it.
		 */
		PartUsage target = getTarget();
		Type owningType = target.getOwningType();
		return UsageUtil.isStakeholderParameter(target) &&
			   ( owningType instanceof RequirementDefinition ||
				 owningType instanceof RequirementUsage);
	}

	protected boolean isCaseActor() {
		PartUsage target = getTarget();
		Type owningType = target.getOwningType();
		return UsageUtil.isActorParameter(target) &&
			   ( owningType instanceof CaseDefinition ||
				 owningType instanceof CaseUsage);
	}

}

````
