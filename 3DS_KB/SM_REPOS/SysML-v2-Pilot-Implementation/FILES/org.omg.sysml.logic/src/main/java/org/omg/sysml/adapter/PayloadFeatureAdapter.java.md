# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/PayloadFeatureAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/PayloadFeatureAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/PayloadFeatureAdapter.java
- source_bytes: 1781
- source_sha256: `f58169ffa3c29a3387a7d4e9846e3ba6ea86321c9d43c42f090ce1a385fb2394`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021-2022, 2025 Model Driven Solutions, Inc.
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
import org.omg.sysml.lang.sysml.PayloadFeature;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.util.SysMLLibraryUtil;

public class PayloadFeatureAdapter extends FeatureAdapter {

	public PayloadFeatureAdapter(PayloadFeature element) {
		super(element);
	}
	
	@Override
	public PayloadFeature getTarget() {
		return (PayloadFeature)super.getTarget();
	}
	
	/**
	 * @satisfies checkPayloadFeatureRedefinition
	 */
	@Override
	public void addRedefinitions(Element skip) {
		Feature redefinedFeature = (Feature)SysMLLibraryUtil.getLibraryType(getTarget(), getDefaultSupertype("payload"));
		addImplicitGeneralType(SysMLPackage.eINSTANCE.getRedefinition(), redefinedFeature);
	}

}

````
