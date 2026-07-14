# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/MultiplicityRange_upperBound_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/MultiplicityRange_upperBound_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/MultiplicityRange_upperBound_SettingDelegate.java
- source_bytes: 1884
- source_sha256: `f92523dd4f20f17be35080594618403ca54a7dc40903922a1870c2a2aa72bf9e`
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

import java.util.List;
import java.util.stream.Collectors;

import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.InternalEObject;
import org.omg.sysml.lang.sysml.Expression;
import org.omg.sysml.lang.sysml.MultiplicityRange;
import org.omg.sysml.util.NamespaceUtil;

public class MultiplicityRange_upperBound_SettingDelegate extends BasicDerivedObjectSettingDelegate {

	public MultiplicityRange_upperBound_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}
	
	@Override
	public Expression basicGet(InternalEObject owner) {
		List<Expression> bounds = NamespaceUtil.getOwnedMembersOf((MultiplicityRange)owner).
				filter(Expression.class::isInstance).map(Expression.class::cast).
				collect(Collectors.toList());
		return bounds.isEmpty()? null:
			   bounds.size() == 1? bounds.get(0):
			   bounds.get(1);
	}

}

````
