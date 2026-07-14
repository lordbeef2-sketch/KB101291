# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ClassifierAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ClassifierAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/ClassifierAdapter.java
- source_bytes: 1920
- source_sha256: `7aff10726a704241a3e9d98ea45b6ca7e381999a36a5eec46540dab21a099a24`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021-2022 Model Driven Solutions, Inc.
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

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.eclipse.emf.ecore.EClass;
import org.omg.sysml.lang.sysml.Classifier;
import org.omg.sysml.lang.sysml.Feature;
import org.omg.sysml.lang.sysml.SysMLPackage;
import org.omg.sysml.lang.sysml.Type;

public class ClassifierAdapter extends TypeAdapter {
	
	public ClassifierAdapter(Classifier element) {
		super(element);
	}
	
	@Override
	public Classifier getTarget() {
		return (Classifier)super.getTarget();
	}

	@Override
	protected EClass getSpecializationEClass() {
		return SysMLPackage.eINSTANCE.getSubclassification();
	}
	
	@Override
	protected List<Type> getBaseTypes() {
		return super.getBaseTypes().stream().
				flatMap(type->type instanceof Feature? 
						((Feature)type).getType().stream(): 
						Stream.of(type)).
				filter(Classifier.class::isInstance).
				collect(Collectors.toList());
	}
	
}

````
