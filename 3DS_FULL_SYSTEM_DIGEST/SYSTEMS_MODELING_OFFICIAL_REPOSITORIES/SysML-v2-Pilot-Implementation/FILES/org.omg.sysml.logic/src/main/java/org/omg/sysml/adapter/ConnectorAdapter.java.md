# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConnectorAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConnectorAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ConnectorAdapter.java
- source_bytes: 3020
- source_sha256: `79f1343d89980d6e416cef9f46966db3498048274451d63a95506c1844aeaf51`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021, 2024, 2025 Model Driven Solutions, Inc.
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

import org.omg.sysml.lang.sysml.Connector;
import org.omg.sysml.lang.sysml.Expression;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.util.ConnectorUtil;
import org.omg.sysml.util.ElementUtil;
import org.omg.sysml.util.TypeUtil;

public class ConnectorAdapter extends FeatureAdapter {

	public ConnectorAdapter(Connector feature) {
		super(feature);
	}
	
	@Override
	public Connector getTarget() {
		return (Connector)super.getTarget();
	}
	
	/**
	 * @satisfies checkConnectorBinaryObjectSpecialization
	 * @satisfies checkConnectorBinarySpecialization
	 * @satisfies checkConnectorObjectSpecialization
	 * @satisfies checkConnectorSpecialization
	 */
	@Override
	protected String getDefaultSupertype() {
		Connector target = getTarget();
		int numEnds = TypeUtil.getOwnedEndFeaturesOf(target).size();
		return hasStructureType()?
				numEnds != 2? 
					getDefaultSupertype("object"):
					getDefaultSupertype("binaryObject"):
				numEnds != 2? 
					getDefaultSupertype("base"):
					getDefaultSupertype("binary");
	}
	
	/**
	 * @satisfies checkConnectorTypeFeaturing
	 */
	protected void addContextFeaturingType() {
		addFeaturingTypeIfNecessary(ConnectorUtil.getContextTypeFor(getTarget()));
	}
	
	public static void addEndSubsetting(Connector target) {
		for (Feature end: target.getConnectorEnd()) {
			if (end != null) {
				Expression expression = end.getOwnedFeature().stream().
						filter(Expression.class::isInstance).
						map(Expression.class::cast).
						findFirst().orElse(null);
				if (expression != null) {
					ElementUtil.transform(expression);
					TypeUtil.addImplicitGeneralTypeTo(end, SysMLPackage.eINSTANCE.getSubsetting(), expression.getResult());
				}
			}
		}
	}
	
	/**
	 * @satisfies checkConnectorTypeFeaturing
	 */
	@Override
	public void doTransform() {
		Connector target = getTarget();
		super.doTransform();
		addContextFeaturingType();
		addEndSubsetting(target);
	}
	
}

````
