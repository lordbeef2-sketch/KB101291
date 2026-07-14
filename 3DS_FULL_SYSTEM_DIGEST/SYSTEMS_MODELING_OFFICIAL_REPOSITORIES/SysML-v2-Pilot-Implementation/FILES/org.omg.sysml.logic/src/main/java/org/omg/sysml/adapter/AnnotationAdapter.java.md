# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/AnnotationAdapter.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/AnnotationAdapter.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/adapter/AnnotationAdapter.java
- source_bytes: 1994
- source_sha256: `e86b171df258b507cf1806195d731f9e996acc35f8ce98353001df18d74d382b`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2024, 2025 Model Driven Solutions, Inc.
 * Copyright (c) 2024 Budapest University of Technology and Economics
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

import org.omg.sysml.lang.sysml.AnnotatingElement;
import org.omg.sysml.lang.sysml.Annotation;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.lang.sysml.SysMLPackage;

public class AnnotationAdapter extends RelationshipAdapter {

	public AnnotationAdapter(Annotation element) {
		super(element);
	}
	
	@Override
	public Annotation getTarget() {
		return (Annotation)super.getTarget();
	}
	
	@Override
	public void postProcess() {
		Annotation obj = getTarget();
		
		// If the Annotation is not owned by an AnnotatingElement, then the annotatedElement is the owningRelatedElement.
		Object annotatedElement = obj.eGet(SysMLPackage.Literals.ANNOTATION__ANNOTATED_ELEMENT, false);
		if (annotatedElement == null) {
			Element owningRelatedElement = obj.getOwningRelatedElement();
			if (!(owningRelatedElement instanceof AnnotatingElement)) {
				obj.setAnnotatedElement(owningRelatedElement);
			}
		}
	}
	
}

````
