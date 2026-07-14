# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/ControlNode_multiplicityHasBounds_InvocationDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/ControlNode_multiplicityHasBounds_InvocationDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/invocation/ControlNode_multiplicityHasBounds_InvocationDelegate.java
- source_bytes: 2074
- source_sha256: `05598bf9ad67a451180f74ce40c694e4afd241d8712174c704cd9cbd78930c93`
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

import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.InternalEObject;
import org.eclipse.emf.ecore.util.BasicInvocationDelegate;
import org.omg.sysml.lang.sysml.Multiplicity;
import org.omg.sysml.lang.sysml.MultiplicityRange;

public class ControlNode_multiplicityHasBounds_InvocationDelegate extends BasicInvocationDelegate {

	public ControlNode_multiplicityHasBounds_InvocationDelegate(EOperation operation) {
		super(operation);
	}
	
	@Override
	public Object dynamicInvoke(InternalEObject target, EList<?> arguments) throws InvocationTargetException {
		Multiplicity mult = (Multiplicity) arguments.get(0);
		int lower = (int) arguments.get(1);
		int upper = (int) arguments.get(2);
		
		return mult != null &&
				(mult instanceof MultiplicityRange? ((MultiplicityRange)mult).hasBounds(lower, upper):
				 mult.allSupertypes().stream().anyMatch(sup -> 
					sup instanceof MultiplicityRange && ((MultiplicityRange)sup).hasBounds(lower, upper)));
	}

}

````
