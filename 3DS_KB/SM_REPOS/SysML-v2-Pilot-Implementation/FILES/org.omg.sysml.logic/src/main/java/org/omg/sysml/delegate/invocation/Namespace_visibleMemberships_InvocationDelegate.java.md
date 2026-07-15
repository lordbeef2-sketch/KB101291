# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Namespace_visibleMemberships_InvocationDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Namespace_visibleMemberships_InvocationDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/Namespace_visibleMemberships_InvocationDelegate.java
- source_bytes: 2092
- source_sha256: `7c75cd4296ddd7ad81ac20d152bc5b33d09741789e476aa2127a8f81fa1a5e52`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2024 Model Driven Solutions, Inc.
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
import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.util.BasicInvocationDelegate;
import org.omg.sysml.lang.sysml.Namespace;
import org.omg.sysml.lang.sysml.impl.NamespaceImpl;
import org.omg.sysml.util.NamespaceUtil;

public class Namespace_visibleMemberships_InvocationDelegate extends BasicInvocationDelegate {
	
	public Namespace_visibleMemberships_InvocationDelegate(EOperation operation) {
		super(operation);
	}
	
	@Override
	public Object dynamicInvoke(InternalEObject target, EList<?> arguments) throws InvocationTargetException {
		NamespaceImpl self = (NamespaceImpl) target;
		@SuppressWarnings("unchecked")
		EList<Namespace> excluded = (EList<Namespace>) arguments.get(0);
		boolean isRecursive = (boolean) arguments.get(1);
		boolean includeAll = (boolean) arguments.get(2);
		
		return NamespaceUtil.getVisibleMembershipsFor(self, new HashSet<>(excluded), isRecursive, includeAll);
	}

}

````
