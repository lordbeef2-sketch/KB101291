# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ExpressionAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ExpressionAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ExpressionAdapter.java
- source_bytes: 4034
- source_sha256: `6d36adc21422646efc4962e14bbca2e37ff47bf5b730727a69d9715ae729cf65`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021-2022, 2024-2025 Model Driven Solutions, Inc.
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
import java.util.List;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.Expression;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.FeatureValue;
import org.omg.sysml.lang.sysml.Multiplicity;
import org.omg.sysml.lang.sysml.Type;
import org.omg.sysml.util.ExpressionUtil;
import org.omg.sysml.util.ImplicitGeneralizationMap;

public class ExpressionAdapter extends StepAdapter {

	public static final String EXPRESSION_GUARD_FEATURE = "TransitionPerformances::TransitionPerformance::guard";

	public ExpressionAdapter(Expression element) {
		super(element);
	}
	
	@Override
	public Expression getTarget() {
		return (Expression)super.getTarget();
	}
	
	// Implicit Generalization
	
	/**
	 * @satisfies checkStepOwnedPerformanceSpecialization
	 * @satisfies checkStepSubperformanceSpecialization
	 * @satisfies checkStepEnclosedPerformanceSpecialization
	 * 
	 * Note: These are satisfied by getDefaultSupertype in StepAdapter, 
	 * which is overridden in ExpressionAdapater.
	 */
	@Override
	public void addDefaultGeneralType() {
		super.addDefaultGeneralType();
		if (isStructureOwnedComposite()) {
			addDefaultGeneralType("ownedPerformance");
		}
		if (isBehaviorOwnedComposite()) {
			addDefaultGeneralType("subperformance");
		}
		if (isBehaviorOwned()) {
			addDefaultGeneralType("enclosedPerformance");
		}
	}
	
	/**
	 * @satisfies checkExpressionSpecialization
	 */
	@Override
	protected String getDefaultSupertype() {
		return getDefaultSupertype("base");
	}
	
	// Computed Redefinition

	@Override
	protected List<? extends Feature> getRelevantFeatures(Type type) {
		Expression target = getTarget();
		Type owningType = target.getOwningType();
		return ExpressionUtil.isTransitionGuard(target)?
					type == owningType? Collections.singletonList(target):
					Collections.singletonList((Feature)getLibraryType(EXPRESSION_GUARD_FEATURE)):
			   owningType instanceof FeatureValue? Collections.emptyList():
			   super.getRelevantFeatures(type);
	}
	
	@Override
	protected List<Type> getGeneralTypes(Type type, Element skip) {
		Expression target = getTarget();
		Type owningType = target.getOwningType();
		return ExpressionUtil.isTransitionGuard(target) && type == owningType?
				Collections.singletonList(getLibraryType(ImplicitGeneralizationMap.getDefaultSupertypeFor(type.getClass(), "base"))):
				super.getGeneralTypes(type, skip);
	}
	
	// Transformation
	
	/**
	 * @satisfies checkExpressionTypeFeaturing
	 * @satisfies checkExpressionResultBindingConnector
	 * @satisfies checkMultiplicityRangeExpressionTypeFeaturing
	 */
	@Override
	public void doTransform() {
		Expression expression = getTarget();
		super.doTransform();
		if (expression.getOwningNamespace() instanceof Multiplicity || 
				expression.getOwningMembership() instanceof FeatureValue) {
			addImplicitFeaturingTypesIfNecessary();
		}
		createResultConnector(expression.getResult());
	}
		
}

````
