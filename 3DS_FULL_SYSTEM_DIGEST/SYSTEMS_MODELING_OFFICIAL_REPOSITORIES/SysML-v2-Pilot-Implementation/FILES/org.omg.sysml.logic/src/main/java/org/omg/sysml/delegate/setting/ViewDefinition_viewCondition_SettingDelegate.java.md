# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/ViewDefinition_viewCondition_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/ViewDefinition_viewCondition_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/ViewDefinition_viewCondition_SettingDelegate.java
- source_bytes: 2018
- source_sha256: `97af350546f3ae0876f22a97f851625ef85651055dc16ee8c7748b73dfb651d9`
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
import org.omg.sysml.lang.sysml.ElementFilterMembership;
import org.omg.sysml.lang.sysml.Expression;
import org.omg.sysml.lang.sysml.ViewDefinition;
import org.omg.sysml.util.NamespaceUtil;
import org.omg.sysml.util.NonNotifyingEObjectEList;

public class ViewDefinition_viewCondition_SettingDelegate extends BasicDerivedListSettingDelegate {

	public ViewDefinition_viewCondition_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected EList<?> basicGet(InternalEObject owner) {
		EList<Expression> viewConditions = new NonNotifyingEObjectEList<>(Expression.class, owner, eStructuralFeature.getFeatureID());
		NamespaceUtil.getOwnedMembersByMembershipIn((ViewDefinition)owner, ElementFilterMembership.class, Expression.class).forEachOrdered(viewConditions::add);
		return viewConditions;
	}

}

````
