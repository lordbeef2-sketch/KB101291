# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/DifferencingAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/DifferencingAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/DifferencingAdapter.java
- source_bytes: 2263
- source_sha256: `f3bf60b3c557458d897aa3a3bb0f94d0c238612fb8ee76a4e98d77f4635df4b0`
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
import org.omg.sysml.lang.sysml.Differencing;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.SysMLPackage;

public class DifferencingAdapter extends RelationshipAdapter {

	public DifferencingAdapter(Differencing element) {
		super(element);
	}
	
	@Override
	public Differencing getTarget() {
		return (Differencing)super.getTarget();
	}
	
	@Override
	public void postProcess() {
		Differencing obj = getTarget();
		
		// If a Differencing is parsed targeting a Feature chain, then the differencingType will be empty,
		// but the Differencing will own the differencingType. So, in this case, the differencingType should
		// be set to the (last) ownedRelatedelement.
		Object differencingType = obj.eGet(SysMLPackage.Literals.DIFFERENCING__DIFFERENCING_TYPE, false);
		if (differencingType == null) {
			// Handle a differencingType that is a Feature chain.
			EList<Element> ownedRelatedElements = obj.getOwnedRelatedElement();
			if (!ownedRelatedElements.isEmpty()) {
				obj.setDifferencingType((Feature)ownedRelatedElements.get(ownedRelatedElements.size() - 1));
			}
		}
	}
	
}

````
