# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/OwningMembership_ownedMemberElement_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/OwningMembership_ownedMemberElement_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/OwningMembership_ownedMemberElement_SettingDelegate.java
- source_bytes: 2306
- source_sha256: `15eaca3c4bf7a376fc5bd65c1ad70ae6638131c32b7cebd1619a7aed84ffe9e2`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2022 Model Driven Solutions, Inc.
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
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.OwningMembership;

public class OwningMembership_ownedMemberElement_SettingDelegate extends BasicDerivedObjectSettingDelegate {

	public OwningMembership_ownedMemberElement_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected Element basicGet(InternalEObject owner) {
		return ((OwningMembership)owner).getOwnedRelatedElement().stream().findFirst().orElse(null);
	}
	
	protected <T> T basicGet(InternalEObject owner, Class<T> kind) {
		return ((OwningMembership)owner).getOwnedRelatedElement().stream().
				findFirst().
				filter(kind::isInstance).
				map(kind::cast).
				orElse(null);
	}
	
	@Override
    protected void set(InternalEObject owner, Object newOwnedMemberElement) {
		if (newOwnedMemberElement != null) { 
			EList<Element> ownedRelatedElements = ((OwningMembership)owner).getOwnedRelatedElement();
			ownedRelatedElements.remove(((OwningMembership)owner).getOwnedMemberElement());
			ownedRelatedElements.add(0, (Element)newOwnedMemberElement);
		}
    }

}

````
