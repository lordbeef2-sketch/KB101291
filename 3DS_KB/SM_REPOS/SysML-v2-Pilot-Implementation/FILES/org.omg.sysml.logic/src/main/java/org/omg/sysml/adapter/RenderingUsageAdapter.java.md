# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/RenderingUsageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/RenderingUsageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/RenderingUsageAdapter.java
- source_bytes: 2757
- source_sha256: `03c22aa9441ac3ba5d46547d5af8976fbb049d2b5c970d70f8ffaa88655e1b1b`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021, 2023 Model Driven Solutions, Inc.
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
import org.omg.sysml.lang.sysml.FeatureMembership;
import org.omg.sysml.lang.sysml.RenderingDefinition;
import org.omg.sysml.lang.sysml.RenderingUsage;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.lang.sysml.ViewRenderingMembership;

public class RenderingUsageAdapter extends PartUsageAdapter {

	public RenderingUsageAdapter(RenderingUsage element) {
		super(element);
	}
	
	/**
	 * @satisfies checkPartUsageSubpartSpecialization
	 */
	@Override
	public void addDefaultGeneralType() {
		super.addDefaultGeneralType();
		if (isSubitem()) {
			addDefaultGeneralType("subpart");
		}
	}
	
	@Override
	public RenderingUsage getTarget() {
		return (RenderingUsage)super.getTarget();
	}
	
	/**
	 * @satisfies checkRenderingUsageRedefinition
	 */
	@Override
	public void addRedefinitions(Element skip) {
		super.addRedefinitions(skip);
		if (isViewRendering()) {
			addImplicitGeneralType(SysMLPackage.eINSTANCE.getRedefinition(), getLibraryType(getDefaultSupertype("viewRendering")));
		}
	}
	
	/**
	 * @satisfies checkRenderingUsageSubrenderingSpecialization
	 * @satisfies checkRenderingUsageSpecialization
	 */
	@Override
	protected String getDefaultSupertype() {
		return isSubrendering()?
					getDefaultSupertype("subrendering"):
					getDefaultSupertype("base");
	}
	
	public boolean isViewRendering() {
		FeatureMembership membership = getTarget().getOwningFeatureMembership();
		return membership instanceof ViewRenderingMembership;
	}
	
	public boolean isSubrendering() {
		Type owningType = getTarget().getOwningType();
		return owningType instanceof RenderingDefinition | owningType instanceof RenderingUsage;
	}
	
}

````
