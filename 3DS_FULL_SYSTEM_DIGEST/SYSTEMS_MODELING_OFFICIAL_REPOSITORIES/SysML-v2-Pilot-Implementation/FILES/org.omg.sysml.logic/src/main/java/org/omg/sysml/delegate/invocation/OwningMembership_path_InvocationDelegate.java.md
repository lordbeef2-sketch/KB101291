# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/OwningMembership_path_InvocationDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/OwningMembership_path_InvocationDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/OwningMembership_path_InvocationDelegate.java
- source_bytes: 1938
- source_sha256: `1b40ddac58955df09caaac7fa74e085ed8c751823578d842ff09f0fb33dcee75`
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
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.OwningMembership;

public class OwningMembership_path_InvocationDelegate extends Relationship_path_InvocationDelegate {

	public OwningMembership_path_InvocationDelegate(EOperation operation) {
		super(operation);
	}
	
	@Override
	public String dynamicInvoke(InternalEObject target, EList<?> arguments) throws InvocationTargetException {
		OwningMembership self = (OwningMembership) target;
		Element ownedElement = self.getOwnedMemberElement();
		if (ownedElement != null) {
			String qualifiedName = ownedElement.getQualifiedName();
			if (qualifiedName != null) {
				return qualifiedName + "/owningMembership";
			}
		}
		return super.dynamicInvoke(target, arguments);
	}

}

````
