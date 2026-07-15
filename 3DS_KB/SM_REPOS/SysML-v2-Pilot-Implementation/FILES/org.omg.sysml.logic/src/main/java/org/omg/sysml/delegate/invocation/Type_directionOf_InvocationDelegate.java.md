# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Type_directionOf_InvocationDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Type_directionOf_InvocationDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Type_directionOf_InvocationDelegate.java
- source_bytes: 3001
- source_sha256: `040e9bc8e6c62c4511589d8a9f10ed0bb5a819a94b5f971c2fe9b07d8d86df3c`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2024, 2025 Model Driven Solutions, Inc.
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
import java.util.HashSet;
import java.util.Set;

import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.util.BasicInvocationDelegate;
import org.omg.sysml.lang.sysml.Conjugation;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.FeatureDirectionKind;
import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.util.TypeUtil;

public class Type_directionOf_InvocationDelegate extends BasicInvocationDelegate {

	public Type_directionOf_InvocationDelegate(EOperation operation) {
		super(operation);
	}
	
	@Override
	public Object dynamicInvoke(InternalEObject target, EList<?> arguments) throws InvocationTargetException {
		Type self = (Type) target;
		Feature feature = (Feature) arguments.get(0);
		
		return directionOf(feature, self, new HashSet<Type>());
	}
	
	protected static FeatureDirectionKind directionOf(Feature feature, Type type, Set<Type> visited) {
		visited.add(type);
		Conjugation conjugator = type.getOwnedConjugator();
		if (feature.getOwningType() == type) {
			return feature.getDirection();
		} else if (conjugator != null) {
			Type originalType = conjugator.getOriginalType();
			if (originalType == null || visited.contains(originalType)) {
				return null;
			} else {
				FeatureDirectionKind originalDirection = directionOf(feature, originalType, visited);
				return originalDirection == FeatureDirectionKind.IN? FeatureDirectionKind.OUT:
					   originalDirection == FeatureDirectionKind.OUT? FeatureDirectionKind.IN:
					   originalDirection;
			}
		} else {
			for (Type general: TypeUtil.getGeneralTypesOf(type)) {
				if (general != null && !visited.contains(general)) {
					FeatureDirectionKind direction = directionOf(feature, general, visited);
					if (direction != null) {
						return direction;
					}
				}
			}
			return null;
		}
	}

}

````
