# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/TypeFeaturingAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/TypeFeaturingAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/TypeFeaturingAdapter.java
- source_bytes: 1927
- source_sha256: `81ece64ea721d5099fdde54203345646d3531954f6e62ab42e7b71d9f9ff024a`
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

import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.TypeFeaturing;
import org.omg.sysml.lang.sysml.SysMLPackage;

public class TypeFeaturingAdapter extends RelationshipAdapter {

	public TypeFeaturingAdapter(TypeFeaturing element) {
		super(element);
	}
	
	@Override
	public TypeFeaturing getTarget() {
		return (TypeFeaturing)super.getTarget();
	}
	
	@Override
	public void postProcess() {
		TypeFeaturing obj = getTarget();
		
		// If the featureOfType is empty, then set it to the owningRelatedElement (if this is a Feature).
		Object featureOfType = obj.eGet(SysMLPackage.Literals.TYPE_FEATURING__FEATURE_OF_TYPE, false);
		if (featureOfType == null) {
			Element owner = obj.getOwningRelatedElement();
			if (owner instanceof Feature) {
				obj.setFeatureOfType((Feature)owner);
			}
		}
	}
	
}

````
