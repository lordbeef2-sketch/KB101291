# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/AssociationStructureAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/AssociationStructureAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/AssociationStructureAdapter.java
- source_bytes: 1464
- source_sha256: `b2f562217bebcefcc3bf93a05e2cf301f9248f9c00700942664f03ef465c97d5`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 * SysML 2 Pilot Implementation
 * Copyright (c) 2019 Model Driven Solutions, Inc.
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
 * Contributors:
 *  Zoltan Ujhelyi, MDS
 */

package org.omg.sysml.adapter;

import org.omg.sysml.lang.sysml.AssociationStructure;

/**
 * This adapter does not introduce any specific behavior compared to the
 * {@link AssociationAdapter} but it is introduced to allow unexpected behavior
 * changes when regenerating the EMF models (as sometimes the order of multiple
 * generalizations changes).
 */
public class AssociationStructureAdapter extends AssociationAdapter {

	public AssociationStructureAdapter(AssociationStructure element) {
		super(element);
	}
	
	@Override
	public AssociationStructure getTarget() {
		return (AssociationStructure)super.getTarget();
	}

}

````
