# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/IncludeUseCaseUsageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/IncludeUseCaseUsageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/IncludeUseCaseUsageAdapter.java
- source_bytes: 2238
- source_sha256: `c259385e1ef1c7d56f2ffde1e2a8e5dc478b8a64fd6cd802932cda07c5bbd4a9`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021, 2022, 2025, 2026 Model Driven Solutions, Inc.
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
import org.omg.sysml.lang.sysml.IncludeUseCaseUsage;
import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.lang.sysml.UseCaseDefinition;
import org.omg.sysml.lang.sysml.UseCaseUsage;

public class IncludeUseCaseUsageAdapter extends UseCaseUsageAdapter {

	public IncludeUseCaseUsageAdapter(IncludeUseCaseUsage element) {
		super(element);
	}
	
	@Override
	public IncludeUseCaseUsage getTarget() {
		return (IncludeUseCaseUsage)super.getTarget();
	}
	
	/**
	 * @satisfies checkIncludeUseCaseUsageSpecialization
	 */
	public boolean isSubUseCase() {
		Type owningType = getTarget().getOwningType();
		return owningType instanceof UseCaseDefinition || owningType instanceof UseCaseUsage;
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
		
	@Override
	public boolean hasRelevantSubjectParameter() {
		Type owningType = getTarget().getOwningType();
		return owningType instanceof CaseDefinition || owningType instanceof CaseUsage;
	}
	
}

````
