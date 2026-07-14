# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Definition_ownedMetadata_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Definition_ownedMetadata_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Definition_ownedMetadata_SettingDelegate.java
- source_bytes: 1901
- source_sha256: `e34951b0f0508fee1d16654a7d876fb625100bf11ac134463e28e03d7aa43a0c`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2026 Model Driven Solutions, Inc.
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
import org.omg.sysml.lang.sysml.Definition;
import org.omg.sysml.lang.sysml.MetadataUsage;
import org.omg.sysml.util.NonNotifyingEObjectEList;

public class Definition_ownedMetadata_SettingDelegate extends BasicDerivedListSettingDelegate {

	public Definition_ownedMetadata_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected EList<MetadataUsage> basicGet(InternalEObject owner) {
		EList<MetadataUsage> ownedMetadata = new NonNotifyingEObjectEList<>(MetadataUsage.class, owner, eStructuralFeature.getFeatureID());
		((Definition)owner).getMember().stream().
			filter(MetadataUsage.class::isInstance).
			map(MetadataUsage.class::cast).
			forEachOrdered(ownedMetadata::add);
		return ownedMetadata;
	}

}

````
