# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/TransitionUsage_guardExpression_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/TransitionUsage_guardExpression_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/TransitionUsage_guardExpression_SettingDelegate.java
- source_bytes: 2098
- source_sha256: `41e9c6e5018dacc988d16ba0c7291c17eb96cb1c993bb3ed4c67bef79f0ad20d`
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
import org.omg.sysml.lang.sysml.Expression;
import org.omg.sysml.lang.sysml.TransitionFeatureKind;
import org.omg.sysml.lang.sysml.TransitionUsage;
import org.omg.sysml.util.NonNotifyingEObjectEList;
import org.omg.sysml.util.UsageUtil;

public class TransitionUsage_guardExpression_SettingDelegate extends BasicDerivedListSettingDelegate {

	public TransitionUsage_guardExpression_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected EList<?> basicGet(InternalEObject owner) {
		EList<Expression> guardExpressions = 
				new NonNotifyingEObjectEList<>(Expression.class, owner, eStructuralFeature.getFeatureID());
		UsageUtil.getTransitionFeaturesOf((TransitionUsage)owner, TransitionFeatureKind.GUARD).
			filter(feature->feature instanceof Expression).
			map(feature->(Expression)feature).
			forEachOrdered(guardExpressions::add);
		return guardExpressions;
	}

}

````
