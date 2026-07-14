# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/DefaultDerivedPropertySettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/DefaultDerivedPropertySettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/DefaultDerivedPropertySettingDelegate.java
- source_bytes: 2031
- source_sha256: `7a10546564c22428880f7d2ed3da14f97571b8298fb8b6b899929691f7b53212`
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
import org.eclipse.emf.ecore.EAnnotation;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.InternalEObject;
import org.omg.sysml.lang.sysml.util.DerivedEObjectEList;

public class DefaultDerivedPropertySettingDelegate extends BasicDerivedListSettingDelegate {
	
	private Class<?> type;
	private int featureID;
	private int sourceFeatureID;
	
	public DefaultDerivedPropertySettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
		this.type = eStructuralFeature.getEType().getInstanceClass();
		this.featureID = eStructuralFeature.getFeatureID();
		EAnnotation annotation = eStructuralFeature.getEAnnotation("subsets");
		EStructuralFeature sourceFeature = (EStructuralFeature)annotation.getReferences().get(0);
		this.sourceFeatureID = sourceFeature.getFeatureID();
	}

	@Override
	protected EList<?> basicGet(InternalEObject owner) {
		return new DerivedEObjectEList<>(type, owner, featureID, new int[] {sourceFeatureID});
	}

}

````
