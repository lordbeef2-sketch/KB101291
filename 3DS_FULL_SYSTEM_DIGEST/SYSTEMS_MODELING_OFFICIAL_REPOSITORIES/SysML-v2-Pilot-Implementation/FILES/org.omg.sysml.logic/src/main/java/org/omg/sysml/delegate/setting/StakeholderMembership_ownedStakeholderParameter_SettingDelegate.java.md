# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/StakeholderMembership_ownedStakeholderParameter_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/StakeholderMembership_ownedStakeholderParameter_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/StakeholderMembership_ownedStakeholderParameter_SettingDelegate.java
- source_bytes: 1542
- source_sha256: `7b16e2630bb16893ff7243e77401236f9598560d43bdc261a88261419506bede`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
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

import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.InternalEObject;
import org.omg.sysml.lang.sysml.PartUsage;

public class StakeholderMembership_ownedStakeholderParameter_SettingDelegate extends ParameterMembership_ownedMemberParameter_SettingDelegate {

	public StakeholderMembership_ownedStakeholderParameter_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}
	
	@Override
	public PartUsage basicGet(InternalEObject membership) {
		return basicGet(membership, PartUsage.class);
	}

}

````
