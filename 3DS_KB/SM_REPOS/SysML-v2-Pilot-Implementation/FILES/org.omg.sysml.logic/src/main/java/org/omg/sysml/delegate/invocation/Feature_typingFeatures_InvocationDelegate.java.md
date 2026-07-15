# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Feature_typingFeatures_InvocationDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Feature_typingFeatures_InvocationDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Feature_typingFeatures_InvocationDelegate.java
- source_bytes: 2688
- source_sha256: `6b5f52aa589f6a5f65a47ba778dadcb65428ea39dd9c301a8b4b07445fbf4c08`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2024 Model Driven Solutions, Inc.
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

package org.omg.sysml.delegate.invocation;

import java.lang.reflect.InvocationTargetException;

import org.eclipse.emf.common.util.BasicEList;
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.util.BasicInvocationDelegate;
import org.omg.sysml.lang.sysml.Conjugation;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.util.FeatureUtil;

public class Feature_typingFeatures_InvocationDelegate extends BasicInvocationDelegate {

	public Feature_typingFeatures_InvocationDelegate(EOperation operation) {
		super(operation);
	}
	
	@Override
	public Object dynamicInvoke(InternalEObject target, EList<?> arguments) throws InvocationTargetException {
		Feature self = (Feature) target;

		EList<Feature> typingFeatures = new BasicEList<>();
		if (!self.isConjugated()) {
			// NOTE: Only considers owned Subsettings.
			FeatureUtil.getSubsettedNotCrossedFeaturesOf(self).stream().
				forEachOrdered(typingFeatures::add);
			EList<Feature> chainingFeatures = self.getChainingFeature();
			if (!chainingFeatures.isEmpty()) {
				Feature lastChainingFeature = chainingFeatures.get(chainingFeatures.size() - 1);
				if (!typingFeatures.contains(lastChainingFeature)) {
					typingFeatures.add(lastChainingFeature);
				}
			}
		} else {
			// NOTE: Only considers owned Conjugation.
			Conjugation conjugator = self.getOwnedConjugator();
			if (conjugator != null) {
				Type originalType = conjugator.getOriginalType();
				if (originalType instanceof Feature) {
					typingFeatures.add((Feature)originalType);
				}
			}
		}
		return typingFeatures;
	}

}

````
