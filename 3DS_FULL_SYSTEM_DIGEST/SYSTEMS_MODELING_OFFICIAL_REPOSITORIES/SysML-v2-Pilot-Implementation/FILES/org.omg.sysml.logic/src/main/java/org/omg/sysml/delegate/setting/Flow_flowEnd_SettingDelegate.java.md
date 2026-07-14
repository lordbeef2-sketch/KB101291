# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Flow_flowEnd_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Flow_flowEnd_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Flow_flowEnd_SettingDelegate.java
- source_bytes: 1812
- source_sha256: `96c0b6a2463cd4d432e8b43607119f4437f9da980ba6b4ad67bec26b3e4c5fea`
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
import org.omg.sysml.lang.sysml.FlowEnd;
import org.omg.sysml.util.NonNotifyingEObjectEList;

public class Flow_flowEnd_SettingDelegate extends Connector_connectorEnd_SettingDelegate {

	public Flow_flowEnd_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected EList<FlowEnd> basicGet(InternalEObject owner) {
		EList<FlowEnd> flowEnds = new NonNotifyingEObjectEList<>(FlowEnd.class, owner, eStructuralFeature.getFeatureID());
		super.basicGet(owner).stream().
			filter(FlowEnd.class::isInstance).
			map(FlowEnd.class::cast).
			forEachOrdered(flowEnds::add);
		return flowEnds;
	}

}

````
