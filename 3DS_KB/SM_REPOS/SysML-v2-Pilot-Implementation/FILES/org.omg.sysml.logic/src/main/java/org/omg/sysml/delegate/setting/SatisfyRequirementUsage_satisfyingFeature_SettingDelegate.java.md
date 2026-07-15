# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/SatisfyRequirementUsage_satisfyingFeature_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/SatisfyRequirementUsage_satisfyingFeature_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/SatisfyRequirementUsage_satisfyingFeature_SettingDelegate.java
- source_bytes: 2076
- source_sha256: `284d102c211cb865f0ae477fd30a0b1d9f0e3276abe6caa9209b3940383227f5`
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
import org.omg.sysml.lang.sysml.Expression;
import org.omg.sysml.lang.sysml.FeatureReferenceExpression;
import org.omg.sysml.lang.sysml.FeatureValue;
import org.omg.sysml.lang.sysml.SatisfyRequirementUsage;
import org.omg.sysml.util.FeatureUtil;
import org.omg.sysml.util.UsageUtil;

public class SatisfyRequirementUsage_satisfyingFeature_SettingDelegate extends BasicDerivedObjectSettingDelegate {

	public SatisfyRequirementUsage_satisfyingFeature_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected EObject basicGet(InternalEObject owner) {
		FeatureValue featureValue = UsageUtil.getSatisfyingFeatureValueOf((SatisfyRequirementUsage)owner);
		if (featureValue != null) {
			Expression value = featureValue.getValue();
			if (value instanceof FeatureReferenceExpression) {
				return FeatureUtil.getBasicFeatureOf(((FeatureReferenceExpression)value).getReferent());
			}
		}
		return null;
	}

}

````
