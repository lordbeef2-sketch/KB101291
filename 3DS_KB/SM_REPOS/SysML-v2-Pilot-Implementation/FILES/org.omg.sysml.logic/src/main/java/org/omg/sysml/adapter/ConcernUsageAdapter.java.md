# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConcernUsageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConcernUsageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConcernUsageAdapter.java
- source_bytes: 2048
- source_sha256: `2c199722fcffa145fb1a234245d97618447321185c5bb10758590e951836c9b2`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021, 2023 Model Driven Solutions, Inc.
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

import org.omg.sysml.lang.sysml.ConcernUsage;
import org.omg.sysml.util.UsageUtil;

public class ConcernUsageAdapter extends RequirementUsageAdapter {

	public ConcernUsageAdapter(ConcernUsage element) {
		super(element);
	}
	
	@Override
	public ConcernUsage getTarget() {
		return (ConcernUsage)super.getTarget();
	}
	
	/**
	 * @satisfies checkRequirementUsageSubrequirementSpecialization
	 */
	@Override
	public void addDefaultGeneralType() {
		super.addDefaultGeneralType();
		if (UsageUtil.isSubrequirement(getTarget())) {
			addDefaultGeneralType("subrequirement");
		}
	}
	
	/**
	 * @satisfies checkConcernUsageSpecialization
	 */
	@Override
	protected String getDefaultSupertype() {
		return getDefaultSupertype("base");
	}
	
	/**
	 * @satisfies checkConcernUsageFramedConcernSpecialization
	 */
	@Override
	public void addRequirementConstraintSubsetting() {
		if (UsageUtil.isFramedConcern(getTarget())) {
			addSubsetting(getDefaultSupertype("concern"));
		} else {
			super.addRequirementConstraintSubsetting();
		}
	}
	
}

````
