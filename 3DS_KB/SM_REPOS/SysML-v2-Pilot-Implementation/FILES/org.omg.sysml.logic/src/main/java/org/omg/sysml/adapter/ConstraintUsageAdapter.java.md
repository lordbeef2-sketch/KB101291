# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConstraintUsageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConstraintUsageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConstraintUsageAdapter.java
- source_bytes: 3233
- source_sha256: `8de22fd342091cb26e6470ebc5f49b9df87a594df03c01a1353de335a2f34759`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021-2025 Model Driven Solutions, Inc.
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

import org.omg.sysml.lang.sysml.BindingConnector;
import org.omg.sysml.lang.sysml.ConstraintUsage;
import org.omg.sysml.lang.sysml.ItemDefinition;
import org.omg.sysml.lang.sysml.ItemUsage;
import org.omg.sysml.lang.sysml.RequirementConstraintKind;
import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.util.UsageUtil;

public class ConstraintUsageAdapter extends OccurrenceUsageAdapter {

	protected BindingConnector resultConnector = null;

	public ConstraintUsageAdapter(ConstraintUsage element) {
		super(element);
	}
	
	@Override
	public ConstraintUsage getTarget() {
		return (ConstraintUsage)super.getTarget();
	}
	
	// Implicit Generalization
	
	/**
	 * @satisfies checkConstraintUsageRequirementConstraintSpecialization
	 * @satisfies checkConstraintUsageCheckedConstraintSpecialization
	 * @satisfies checkStepEnclosedPerformanceSpecialization
	 * @satisfies checkStepOwnedPerformanceSpecialization
	 * @satisfies checkStepSubperformanceSpecialization
	 */
	@Override
	public void computeImplicitGeneralTypes() {
		addRequirementConstraintSubsetting();
		super.computeImplicitGeneralTypes();
		if (isCheckedConstraint()) {
			addDefaultGeneralType("checkedConstraint");
		}
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
	
	public void addRequirementConstraintSubsetting() {
		RequirementConstraintKind kind = UsageUtil.getRequirementConstraintKindOf(getTarget());
		if (kind != null) {
			addDefaultGeneralType(kind.toString());
		}
	}
	
	/**
	 * @satisfies checkConstraintUsageSpecialization
	 */
	@Override
	protected String getDefaultSupertype() {
		return getDefaultSupertype("base");
	}
	
	protected boolean isCheckedConstraint() {
		ConstraintUsage target = getTarget();
		Type owningType = target.getOwningType();
		return target.isComposite() &&
				(owningType instanceof ItemDefinition || owningType instanceof ItemUsage);				
	}
	
	@Override
	public void doTransform() {
		super.doTransform();
		createResultConnector(getTarget().getResult());		
	}
	
}

````
