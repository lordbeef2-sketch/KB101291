# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/AssertConstraintUsage_assertedConstraint_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/AssertConstraintUsage_assertedConstraint_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/AssertConstraintUsage_assertedConstraint_SettingDelegate.java
- source_bytes: 1682
- source_sha256: `ff7da9a3fee2753d28938b49ab1c4e3ee723aa68069f84a16a7b86c12d6bdeb1`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2022 Siemens AG
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

import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.InternalEObject;
import org.omg.sysml.lang.sysml.AssertConstraintUsage;
import org.omg.sysml.lang.sysml.ConstraintUsage;
import org.omg.sysml.util.FeatureUtil;

public class AssertConstraintUsage_assertedConstraint_SettingDelegate extends BasicDerivedObjectSettingDelegate {

	public AssertConstraintUsage_assertedConstraint_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected EObject basicGet(InternalEObject owner) {
		return FeatureUtil.getEffectiveReferencedFeatureOf((AssertConstraintUsage)owner, ConstraintUsage.class);
	}

}

````
