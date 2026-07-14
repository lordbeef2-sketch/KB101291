# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Usage_nestedMetadata_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Usage_nestedMetadata_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Usage_nestedMetadata_SettingDelegate.java
- source_bytes: 1886
- source_sha256: `74b0f80da5cc5b4167465b9e77db3cf01bf6fc538c014a40e97e336857ec3cac`
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
import org.omg.sysml.lang.sysml.MetadataUsage;
import org.omg.sysml.lang.sysml.Usage;
import org.omg.sysml.util.NonNotifyingEObjectEList;

public class Usage_nestedMetadata_SettingDelegate extends BasicDerivedListSettingDelegate {

	public Usage_nestedMetadata_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected EList<MetadataUsage> basicGet(InternalEObject owner) {
		EList<MetadataUsage> nestedMetadata = new NonNotifyingEObjectEList<>(MetadataUsage.class, owner, eStructuralFeature.getFeatureID());
		((Usage)owner).getMember().stream().
			filter(MetadataUsage.class::isInstance).
			map(MetadataUsage.class::cast).
			forEachOrdered(nestedMetadata::add);
		return nestedMetadata;
	}

}

````
