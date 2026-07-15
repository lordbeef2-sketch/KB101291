# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/VerificationCaseUsageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/VerificationCaseUsageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/VerificationCaseUsageAdapter.java
- source_bytes: 1977
- source_sha256: `0be02a4d6b59e133952b950ec4ade41ed8b43c3fecba954eb386e56efbafc396`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021, 2023, 2025 Model Driven Solutions, Inc.
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

import org.omg.sysml.lang.sysml.VerificationCaseDefinition;
import org.omg.sysml.lang.sysml.VerificationCaseUsage;
import org.omg.sysml.lang.sysml.Type;

public class VerificationCaseUsageAdapter extends CaseUsageAdapter {

	public VerificationCaseUsageAdapter(VerificationCaseUsage element) {
		super(element);
	}
	
	@Override
	public VerificationCaseUsage getTarget() {
		return (VerificationCaseUsage)super.getTarget();
	}
	
	/**
	 * @satisfies checkVerificationCaseUsageSubVerification
	 * @satisfies checkVerificationCaseUsageSubVerification
	 */
	@Override
	protected String getSubactionType() {
		return isSubVerificationCase()? "subVerificationCase": super.getSubactionType();	
	}
		
	public boolean isSubVerificationCase() {
		VerificationCaseUsage target = getTarget();
		Type owningType = target.getOwningType();
		return target.isComposite() && 
			   (owningType instanceof VerificationCaseDefinition || owningType instanceof VerificationCaseUsage);
	}
	
}

````
