# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/TriggerInvocationExpressionAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/TriggerInvocationExpressionAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/TriggerInvocationExpressionAdapter.java
- source_bytes: 2861
- source_sha256: `9c1a9ce395c18f78889623bda8e33d50a3c3ca11cd23788768cef23aae7359d4`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2022, 2025 Model Driven Solutions, Inc.
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

import java.util.Collections;

import org.omg.sysml.lang.sysml.AcceptActionUsage;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.lang.sysml.TriggerInvocationExpression;
import org.omg.sysml.lang.sysml.TriggerKind;
import org.omg.sysml.util.ImplicitGeneralizationMap;
import org.omg.sysml.util.TypeUtil;

public class TriggerInvocationExpressionAdapter extends InvocationExpressionAdapter {

	public TriggerInvocationExpressionAdapter(TriggerInvocationExpression element) {
		super(element);
	}
	
	@Override
	public TriggerInvocationExpression getTarget() {
		return (TriggerInvocationExpression)super.getTarget();
	}
	
	@Override
	public void computeImplicitGeneralTypes() {
		//checkTriggerInvocationExpressionSpecialization
		TriggerInvocationExpression target = getTarget();
		TriggerKind kind = target.getKind();
		if (kind != null) {
			addDefaultGeneralType(SysMLPackage.eINSTANCE.getFeatureTyping(), 
					ImplicitGeneralizationMap.getDefaultSupertypeFor(target.getClass(), kind.toString()));
		}
		super.computeImplicitGeneralTypes();
	}
	
	
	/**
	 * @satisfies checkAcceptActionUsageReceiverBindingConnector
	 */
	public void addReceiverBinding() {
		//checkAcceptActionUsageReceiverBindingConnector
		TriggerInvocationExpression target = getTarget();
		Feature receiverParameter = TypeUtil.getOwnedParameterOf(target, 1, Feature.class);
		if (receiverParameter != null) {
			target.getFeaturingType().stream().filter(AcceptActionUsage.class::isInstance).forEach(action -> {
				Feature actionParameter = TypeUtil.getOwnedParameterOf(action, 1, Feature.class);
				addBindingConnector(Collections.singletonList(action), actionParameter, receiverParameter);
			});
		}
	}
	
	@Override
	public void doTransform() {
		super.doTransform();
		addReceiverBinding();
	}

}

````
