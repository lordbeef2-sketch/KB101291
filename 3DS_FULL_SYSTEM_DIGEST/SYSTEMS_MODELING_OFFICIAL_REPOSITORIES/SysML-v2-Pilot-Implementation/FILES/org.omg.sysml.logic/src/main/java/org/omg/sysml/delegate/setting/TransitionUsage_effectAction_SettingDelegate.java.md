# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/TransitionUsage_effectAction_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/TransitionUsage_effectAction_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/TransitionUsage_effectAction_SettingDelegate.java
- source_bytes: 2089
- source_sha256: `0a7294403cc0d698cdac29f9516ccb371a57fbbbfe70678bf4f5dfa540d57ebb`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2022 Siemens AG
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
 *  
 *******************************************************************************/

package org.omg.sysml.delegate.setting;

import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.InternalEObject;
import org.omg.sysml.lang.sysml.ActionUsage;
import org.omg.sysml.lang.sysml.TransitionFeatureKind;
import org.omg.sysml.lang.sysml.TransitionUsage;
import org.omg.sysml.util.NonNotifyingEObjectEList;
import org.omg.sysml.util.UsageUtil;

public class TransitionUsage_effectAction_SettingDelegate extends BasicDerivedListSettingDelegate {

	public TransitionUsage_effectAction_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected EList<?> basicGet(InternalEObject owner) {
		EList<ActionUsage> effectActions = 
				new NonNotifyingEObjectEList<>(ActionUsage.class, owner, eStructuralFeature.getFeatureID());
		UsageUtil.getTransitionFeaturesOf((TransitionUsage)owner, TransitionFeatureKind.EFFECT).
			filter(feature->feature instanceof ActionUsage).
			map(feature->(ActionUsage)feature).
			forEachOrdered(effectActions::add);
		return effectActions;
	}

}

````
