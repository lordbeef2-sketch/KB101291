# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ViewpointUsageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ViewpointUsageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ViewpointUsageAdapter.java
- source_bytes: 1890
- source_sha256: `8f9644426a7d218536521abe7eccc4e309a183ee76d14028f440f2b2851bcca5`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021 Model Driven Solutions, Inc.
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

import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.lang.sysml.ViewDefinition;
import org.omg.sysml.lang.sysml.ViewUsage;
import org.omg.sysml.lang.sysml.ViewpointUsage;

public class ViewpointUsageAdapter extends RequirementUsageAdapter {

	public ViewpointUsageAdapter(ViewpointUsage element) {
		super(element);
	}
	
	@Override
	public ViewpointUsage getTarget() {
		return (ViewpointUsage)super.getTarget();
	}
	
	/**
	 * @satisfies checkViewpointUsageViewpointSatisfactionSpecialization
	 * @satisfies checkViewpointUsageSpecialization
	 */
	@Override
	protected String getDefaultSupertype() {
		return isSatisfiedViewpoint()?
					getDefaultSupertype("satisfied"):
					getDefaultSupertype("base");
	}
	
	public boolean isSatisfiedViewpoint() {
		Type owningType = getTarget().getOwningType();
		return owningType instanceof ViewDefinition | owningType instanceof ViewUsage;
	}

}

````
