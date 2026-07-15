# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Feature_ownedFeatureInverting_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Feature_ownedFeatureInverting_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Feature_ownedFeatureInverting_SettingDelegate.java
- source_bytes: 1971
- source_sha256: `e4e93df13ca673c20622cf569bb0d11de51090e582a4a840006a61d5410b7b22`
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
 *  
 *******************************************************************************/

package org.omg.sysml.delegate.setting;

import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.InternalEObject;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.FeatureInverting;
import org.omg.sysml.util.NonNotifyingEObjectEList;

public class Feature_ownedFeatureInverting_SettingDelegate extends BasicDerivedListSettingDelegate {

	public Feature_ownedFeatureInverting_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected EList<?> basicGet(InternalEObject owner) {
		EList<FeatureInverting> invertings = new NonNotifyingEObjectEList<>(FeatureInverting.class, owner, eStructuralFeature.getFeatureID());
		((Feature)owner).getOwnedRelationship().stream().
			filter(rel->(rel instanceof FeatureInverting) && ((FeatureInverting)rel).getFeatureInverted() == owner).
			map(FeatureInverting.class::cast).
			forEachOrdered(invertings::add);
		return invertings;
	}

}

````
