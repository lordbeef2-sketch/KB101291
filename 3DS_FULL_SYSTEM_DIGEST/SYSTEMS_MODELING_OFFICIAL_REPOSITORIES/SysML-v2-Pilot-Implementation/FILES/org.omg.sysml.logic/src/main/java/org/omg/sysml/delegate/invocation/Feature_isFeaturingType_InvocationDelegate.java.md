# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Feature_isFeaturingType_InvocationDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Feature_isFeaturingType_InvocationDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Feature_isFeaturingType_InvocationDelegate.java
- source_bytes: 2376
- source_sha256: `44fd4a7253bb0931cff2524bd102ac3a28364791ad21cbcc924daa57caa2ce1c`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2025 Model Driven Solutions, Inc.
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

import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.util.BasicInvocationDelegate;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.util.SysMLLibraryUtil;

public class Feature_isFeaturingType_InvocationDelegate extends BasicInvocationDelegate {

	public Feature_isFeaturingType_InvocationDelegate(EOperation operation) {
		super(operation);
	}
	
	@Override
	public Object dynamicInvoke(InternalEObject target, EList<?> arguments) throws InvocationTargetException {
		Feature self = (Feature) target;
		Type type = (Type) arguments.get(0);
		Type owningType = self.getOwningType();
		if (!self.isVariable()) {
			return type == owningType;
		} else {
			Type occurrencesType = SysMLLibraryUtil.getLibraryType(self, "Occurrences::Occurrence");
			Feature snapshotsFeature = (Feature) SysMLLibraryUtil.getLibraryType(self, "Occurrences::Occurrence::snapshots");
			if (owningType == occurrencesType) {
				return type == snapshotsFeature;
			} else if (type instanceof Feature) {
				Feature feature = (Feature)type;
				return feature.getFeaturingType().contains(owningType) &&
					   feature.redefines(snapshotsFeature);
			}
		}
		return false;
	}

}

````
