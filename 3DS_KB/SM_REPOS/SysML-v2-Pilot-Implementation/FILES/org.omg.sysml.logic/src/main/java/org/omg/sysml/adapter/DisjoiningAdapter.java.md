# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/DisjoiningAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/DisjoiningAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/DisjoiningAdapter.java
- source_bytes: 3074
- source_sha256: `19152247dfbb90225b59051e5749b24d7929a19a6c77925b2772be24519381ce`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2024 Model Driven Solutions, Inc.
 * Copyright (c) 2024 Budapest University of Technology and Economics
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
 * You should have received a copy of theEclipse Public License
 * along with this program.  If not, see <https://www.eclipse.org/legal/epl-2.0/>.
 *  
 * @license EPL-2.0 <http://spdx.org/licenses/EPL-2.0>
 *  
 *******************************************************************************/

package org.omg.sysml.adapter;

import org.eclipse.emf.common.util.EList;
import org.omg.sysml.lang.sysml.Disjoining;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.lang.sysml.Type;

public class DisjoiningAdapter extends RelationshipAdapter {

	public DisjoiningAdapter(Disjoining element) {
		super(element);
	}
	
	@Override
	public Disjoining getTarget() {
		return (Disjoining)super.getTarget();
	}
	
	@Override
	public void postProcess() {
		Disjoining obj = getTarget();
		
		// If a Disjoining is parsed targeting a Feature chain, then the disjoiningType will be empty,
		// but the Disjoining will own the disjoiningType. So, in this case, the disjoiningType should
		// be set to the (last) ownedRelatedelement.
		Object disjoiningType = obj.eGet(SysMLPackage.Literals.DISJOINING__DISJOINING_TYPE, false);
		if (disjoiningType == null) {
			// Handle a disjoiningType that is a Feature chain.
			EList<Element> ownedRelatedElements = obj.getOwnedRelatedElement();
			if (!ownedRelatedElements.isEmpty()) {
				obj.setDisjoiningType((Feature)ownedRelatedElements.get(ownedRelatedElements.size() - 1));
			}
		}
		
		// If the typedDisjoined (source) is empty, set it to the owningRelatedElement, if it is a Type.
		// Otherwise, set it to the first ownedRelatedElement, to the first ownedRelatedElement,
		// which will be a Feature chain.
		Object typeDisjoined = obj.eGet(SysMLPackage.Literals.DISJOINING__TYPE_DISJOINED, false);
		if (typeDisjoined == null) {
			Element owner = obj.getOwningRelatedElement();
			if (owner instanceof Type) {
				// Handle a Disjoining owned by the typeDisjoined.
				obj.setTypeDisjoined((Type)owner);
			} else {
				// Handle a typeDisjoined that is a Feature chain.
				EList<Element> ownedRelatedElements = obj.getOwnedRelatedElement();
				if (!ownedRelatedElements.isEmpty()) {
					obj.setTypeDisjoined((Feature)ownedRelatedElements.get(0));
				}
			}
		}
	}
	
}

````
