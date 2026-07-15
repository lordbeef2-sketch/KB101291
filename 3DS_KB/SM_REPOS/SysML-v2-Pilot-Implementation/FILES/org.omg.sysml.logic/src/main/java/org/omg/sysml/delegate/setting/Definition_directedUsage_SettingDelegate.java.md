# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Definition_directedUsage_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Definition_directedUsage_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Definition_directedUsage_SettingDelegate.java
- source_bytes: 1802
- source_sha256: `6b14778248e9a4d5691c395702f3e51037eb5df64989360d91d0434ed0b92b0e`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2025 Model Driven Solutions, Inc.
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
import org.omg.sysml.lang.sysml.Usage;
import org.omg.sysml.util.NonNotifyingEObjectEList;

public class Definition_directedUsage_SettingDelegate extends Type_directedFeature_SettingDelegate {

	public Definition_directedUsage_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);		
	}

	@Override
	protected EList<?> basicGet(InternalEObject owner) {
		EList<Usage> directedUsages = new NonNotifyingEObjectEList<>(Usage.class, owner, eStructuralFeature.getFeatureID());
		super.basicGet(owner).stream().
			filter(Usage.class::isInstance).
			map(Usage.class::cast).
			forEachOrdered(directedUsages::add);
		return directedUsages;
	}
}

````
