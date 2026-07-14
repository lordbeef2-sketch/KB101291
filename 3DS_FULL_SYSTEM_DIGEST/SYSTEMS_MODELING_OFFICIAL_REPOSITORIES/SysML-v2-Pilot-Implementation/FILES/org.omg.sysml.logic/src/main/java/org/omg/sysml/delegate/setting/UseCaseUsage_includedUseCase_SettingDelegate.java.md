# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/UseCaseUsage_includedUseCase_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/UseCaseUsage_includedUseCase_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/UseCaseUsage_includedUseCase_SettingDelegate.java
- source_bytes: 2016
- source_sha256: `3344ede936599f46fd8a7958a9b57b1563943926b47fd169be97e0d0f602dea1`
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
import org.omg.sysml.lang.sysml.IncludeUseCaseUsage;
import org.omg.sysml.lang.sysml.UseCaseUsage;
import org.omg.sysml.util.NonNotifyingEObjectEList;

public class UseCaseUsage_includedUseCase_SettingDelegate extends BasicDerivedListSettingDelegate {

	public UseCaseUsage_includedUseCase_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected EList<?> basicGet(InternalEObject owner) {
		EList<UseCaseUsage> includedUseCases = new NonNotifyingEObjectEList<>(UseCaseUsage.class, owner, eStructuralFeature.getFeatureID());
		((UseCaseUsage)owner).getOwnedFeature().stream().
			filter(IncludeUseCaseUsage.class::isInstance).
			map(IncludeUseCaseUsage.class::cast).
			map(IncludeUseCaseUsage::getUseCaseIncluded).
			forEachOrdered(includedUseCases::add);
		return includedUseCases;
	}

}

````
