# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ParameterMembershipAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ParameterMembershipAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ParameterMembershipAdapter.java
- source_bytes: 1612
- source_sha256: `aa358766683b441460fce8cd970a8088803ae3c8c0b547613a783af3fe120d03`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2026 Model Driven Solutions, Inc.
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

package org.omg.sysml.adapter;

import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.ParameterMembership;

public class ParameterMembershipAdapter extends FeatureMembershipAdapter {

	public ParameterMembershipAdapter(ParameterMembership element) {
		super(element);
	}
	
	@Override
	public ParameterMembership getTarget() {
		return (ParameterMembership)super.getTarget();
	}
	
	@Override
	public void postProcess() {
		super.postProcess();
		ParameterMembership target = getTarget();
		Feature parameter = target.getOwnedMemberParameter();
		if (parameter != null) {
			parameter.setDirection(target.parameterDirection());
		}
	}

}

````
