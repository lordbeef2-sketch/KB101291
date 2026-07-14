# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/IfActionUsageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/IfActionUsageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/IfActionUsageAdapter.java
- source_bytes: 1576
- source_sha256: `6ecb9a4d5343d434e5e5f3a7727aec8f37a5aed7cb7e7b336c58316b20290187`
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

import org.omg.sysml.lang.sysml.IfActionUsage;

public class IfActionUsageAdapter extends ActionUsageAdapter {

	public IfActionUsageAdapter(IfActionUsage element) {
		super(element);
	}
	
	@Override
	public IfActionUsage getTarget() {
		return (IfActionUsage)super.getTarget();
	}
	
	/**
	 * @satisfies checkIfActionUsageSpecialization
	 */
	@Override
	public void addDefaultGeneralType() {
		super.addDefaultGeneralType();
		if (isIfThenElse()) {
			addDefaultGeneralType("ifThenElse");
		}
	}
	
	public boolean isIfThenElse() {
		return getTarget().getElseAction() != null;
	}
	
}

````
