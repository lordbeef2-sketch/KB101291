# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Flow_payloadType_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Flow_payloadType_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Flow_payloadType_SettingDelegate.java
- source_bytes: 2049
- source_sha256: `ea39b743c878f04ff0cb876f5b0893620831a0cfd9dc6e3f5d44024c3e6ae4d0`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2022 Siemens AG
 * Copyright (c) 2022, 2025 Model Driven Solutions, Inc.
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
import org.omg.sysml.lang.sysml.Classifier;
import org.omg.sysml.lang.sysml.PayloadFeature;
import org.omg.sysml.lang.sysml.Flow;
import org.omg.sysml.util.NonNotifyingEObjectEList;

public class Flow_payloadType_SettingDelegate extends BasicDerivedListSettingDelegate {

	public Flow_payloadType_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected EList<Classifier> basicGet(InternalEObject owner) {
		EList<Classifier> payloadType = new NonNotifyingEObjectEList<>(Classifier.class, owner, eStructuralFeature.getFeatureID());
		PayloadFeature payloadFeature = ((Flow)owner).getPayloadFeature();
		if (payloadFeature != null) {
			payloadFeature.getType().stream().
				filter(Classifier.class::isInstance).
				map(Classifier.class::cast).
				forEachOrdered(payloadType::add);
		}
		return payloadType;
	}

}

````
