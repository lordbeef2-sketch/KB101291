# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/MetadataDefinitionAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/MetadataDefinitionAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/MetadataDefinitionAdapter.java
- source_bytes: 1458
- source_sha256: `fa8e5927667ff48ac2071904d6be7f8cd0af30450d1be9c1fb8f8fe2cf35dfb2`
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

import org.omg.sysml.lang.sysml.MetadataDefinition;

/**
 * This adapter does not introduce any specific behavior compared to the
 * {@link ItemDefinitionAdapter} but it is introduced to allow unexpected behavior
 * changes when regenerating the EMF models (as sometimes the order of multiple
 * generalizations changes).
 */
public class MetadataDefinitionAdapter extends ItemDefinitionAdapter {

	public MetadataDefinitionAdapter(MetadataDefinition element) {
		super(element);
	}
	
	@Override
	public MetadataDefinition getTarget() {
		return (MetadataDefinition)super.getTarget();
	}

}

````
