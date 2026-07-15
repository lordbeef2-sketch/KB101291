# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Feature_featuringType_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Feature_featuringType_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Feature_featuringType_SettingDelegate.java
- source_bytes: 2251
- source_sha256: `2fa0dd0965aef71715f33f23324914cb97a106924ddf4a073b056a0264c9f088`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2022, 2024 Model Driven Solutions, Inc.
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
import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.lang.sysml.TypeFeaturing;
import org.omg.sysml.util.FeatureUtil;
import org.omg.sysml.util.NonNotifyingEObjectEList;

public class Feature_featuringType_SettingDelegate extends BasicDerivedListSettingDelegate {

	public Feature_featuringType_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected EList<?> basicGet(InternalEObject owner) {
		EList<Type> featuringTypes = new NonNotifyingEObjectEList<>(Type.class, owner, eStructuralFeature.getFeatureID());
		((Feature)owner).getOwnedTypeFeaturing().stream().
			map(TypeFeaturing::getFeaturingType).
			filter(featuring->featuring != null).
			forEachOrdered(featuringTypes::add);
		FeatureUtil.forEachImplicitFeaturingTypeOf(((Feature)owner), featuringTypes::add);
		Feature firstChainingFeature = FeatureUtil.getFirstChainingFeatureOf(((Feature)owner));
		if (firstChainingFeature != null) {
			featuringTypes.addAll(firstChainingFeature.getFeaturingType());
		}
		return featuringTypes;
	}

}

````
