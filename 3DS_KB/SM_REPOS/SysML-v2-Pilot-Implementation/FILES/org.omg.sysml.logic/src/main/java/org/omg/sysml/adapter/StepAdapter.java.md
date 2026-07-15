# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/StepAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/StepAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/StepAdapter.java
- source_bytes: 1950
- source_sha256: `7443b5367abd65caa8772d388e13f406cac43fc6fdff7184b4d2f0c7b3548ef5`
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

import org.omg.sysml.lang.sysml.PayloadFeature;
import org.omg.sysml.lang.sysml.Step;

public class StepAdapter extends FeatureAdapter {
	
	public StepAdapter(Step element) {
		super(element);
	}
	
	@Override
	public Step getTarget() {
		return (Step)super.getTarget();
	}
	
	/**
	 * @satisfies checkStepOwnedPerformanceSpecialization
	 * @satisfies checkStepSubperformanceSpecialization
	 * @satisfies checkStepEnclosedPerformanceSpecialization
	 * @satisfies checkStepSpecialization
	 */
	@Override
	protected String getDefaultSupertype() {
		return getDefaultSupertype(
			isStructureOwnedComposite()?
				"ownedPerformance":
			isBehaviorOwnedComposite()?
				"subperformance":
			isBehaviorOwned()? 
				"enclosedPerformance":
			isIncomingTransfer()?
				"incomingTransfer":
				"base");
	}
	
	public boolean isIncomingTransfer() {
		return getTarget().getOwnedFeature().stream().anyMatch(PayloadFeature.class::isInstance);
	}

}

````
