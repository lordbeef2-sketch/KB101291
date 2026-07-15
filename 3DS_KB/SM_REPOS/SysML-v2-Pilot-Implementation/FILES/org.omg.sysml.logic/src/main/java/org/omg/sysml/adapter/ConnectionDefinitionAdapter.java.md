# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConnectionDefinitionAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConnectionDefinitionAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConnectionDefinitionAdapter.java
- source_bytes: 1856
- source_sha256: `abbd12f7e12674aac869d8aeac1bdd4722de1dd66851101fe6523817344ac446`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021 Model Driven Solutions, Inc.
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

import org.omg.sysml.lang.sysml.ConnectionDefinition;

public class ConnectionDefinitionAdapter extends PartDefinitionAdapter {

	public ConnectionDefinitionAdapter(ConnectionDefinition element) {
		super(element);
	}
	
	@Override
	public ConnectionDefinition getTarget() {
		return (ConnectionDefinition)super.getTarget();
	}
	
	/**
	 * @satisfies checkConnectionDefinitionSpecializations
	 * @satisfies checkInterfaceDefinitionSpecialization
	 * @satisfies checkAllocationDefinitionSpecialization
	 * @satisfies checkConnectionDefinitionBinarySpecialization
	 * @satisfies checkInterfaceDefinitionBinarySpecialization
	 * @satisfies checkAllocationDefinitionSpecialization
	 */
	@Override
	protected String getDefaultSupertype() {
		return getTarget().getOwnedEndFeature().size() != 2 ?
				getDefaultSupertype("base") :
				getDefaultSupertype("binary");
	}

}

````
