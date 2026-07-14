# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/AnalysisCaseUsageAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/AnalysisCaseUsageAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/AnalysisCaseUsageAdapter.java
- source_bytes: 1895
- source_sha256: `81d4432defe3866f33f483bdfdb6569bccb9ee9eda066dc1852c9ca7436cbf81`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021, 2023, 2025 Model Driven Solutions, Inc.
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

import org.omg.sysml.lang.sysml.AnalysisCaseDefinition;
import org.omg.sysml.lang.sysml.AnalysisCaseUsage;
import org.omg.sysml.lang.sysml.Type;

public class AnalysisCaseUsageAdapter extends CaseUsageAdapter {

	public AnalysisCaseUsageAdapter(AnalysisCaseUsage element) {
		super(element);
	}
	
	@Override
	public AnalysisCaseUsage getTarget() {
		return (AnalysisCaseUsage)super.getTarget();
	}
	
	@Override
	protected String getSubactionType() {
		//checkAnalysisCaseUsageSpecialization
		//checkAnalysisCaseUsageSubAnalysisCaseSpecialization
		return isSubAnalysisCase()? "subAnalysisCase": super.getSubactionType();	
	}
		
	public boolean isSubAnalysisCase() {
		AnalysisCaseUsage target = getTarget();
		Type owningType = target.getOwningType();
		return target.isComposite() &&
			   (owningType instanceof AnalysisCaseDefinition || owningType instanceof AnalysisCaseUsage);
	}
	
}

````
