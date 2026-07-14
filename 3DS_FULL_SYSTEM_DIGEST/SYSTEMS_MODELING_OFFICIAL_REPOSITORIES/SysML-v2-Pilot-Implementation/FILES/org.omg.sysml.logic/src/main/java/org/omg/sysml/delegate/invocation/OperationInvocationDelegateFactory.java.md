# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/OperationInvocationDelegateFactory.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/OperationInvocationDelegateFactory.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/OperationInvocationDelegateFactory.java
- source_bytes: 1677
- source_sha256: `7698f1c7943c9321c138da413c4dd882c26dbbb47121ee75533ced0deec845b2`
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

import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.EOperation.Internal.InvocationDelegate;
import org.eclipse.emf.ecore.util.BasicInvocationDelegate;

public class OperationInvocationDelegateFactory implements InvocationDelegate.Factory {
	
	public static final String SYSML_ANNOTATION = "http://www.omg.org/spec/SysML";

	@Override
	public InvocationDelegate createInvocationDelegate(EOperation eOperation) {
		if (eOperation.getEAnnotation(SYSML_ANNOTATION) == null) {
			// This is not our operation, use default invocation delegate
			return new BasicInvocationDelegate(eOperation);
		}
		
		return new OperationInvocationDelegateSelector(eOperation);
	}
 
}

````
