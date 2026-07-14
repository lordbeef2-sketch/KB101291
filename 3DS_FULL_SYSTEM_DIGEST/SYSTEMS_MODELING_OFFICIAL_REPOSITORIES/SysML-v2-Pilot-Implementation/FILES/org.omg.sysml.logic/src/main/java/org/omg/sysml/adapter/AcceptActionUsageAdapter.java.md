# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/AcceptActionUsageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/AcceptActionUsageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/AcceptActionUsageAdapter.java
- source_bytes: 2420
- source_sha256: `946c09a315971792628e8df7ef59f2c304ae002b61a6b27c94b13bb77e57d39e`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2022 Model Driven Solutions, Inc.
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
 * You should have received a copy of the Eclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *  
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 *******************************************************************************/
package org.omg.sysml.adapter;

import org.omg.sysml.lang.sysml.AcceptActionUsage;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.FeatureMembership;
import org.omg.sysml.lang.sysml.TransitionFeatureKind;
import org.omg.sysml.lang.sysml.TransitionFeatureMembership;

public class AcceptActionUsageAdapter extends ActionUsageAdapter {

	public AcceptActionUsageAdapter(AcceptActionUsage action) {
		super(action);
	}

	public AcceptActionUsage getTarget() {
		return (AcceptActionUsage)super.getTarget();
	}
	
	// Implicit Generalization
	
	@Override
	public void computeImplicitGeneralTypes() {
		addComputedRedefinitions(null);
	}
	
	@Override
	public void addDefaultGeneralType() {
		// Don't add a default type for a transition trigger action because such
		// an action will always redefine TransitionAction::accepter anyway: checkAcceptActionUsageTriggerActionSpecialization
		if (!isTriggerAction()) {
			super.addDefaultGeneralType();
		}
	}
	
	public boolean isTriggerAction() {
		FeatureMembership owningFeatureMembership = getTarget().getOwningFeatureMembership();
		return owningFeatureMembership instanceof TransitionFeatureMembership &&
				((TransitionFeatureMembership)owningFeatureMembership).getKind() == TransitionFeatureKind.TRIGGER;
	}
	
	// Computed Redefinition
	
	@Override
	public void addComputedRedefinitions(Element skip) {
		addDefaultGeneralType();
		super.addComputedRedefinitions(skip);
	}

}

````
