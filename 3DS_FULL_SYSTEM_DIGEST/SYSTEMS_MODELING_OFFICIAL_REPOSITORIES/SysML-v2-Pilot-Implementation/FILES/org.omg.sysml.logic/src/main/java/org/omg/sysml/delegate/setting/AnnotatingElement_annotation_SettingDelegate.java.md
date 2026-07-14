# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/AnnotatingElement_annotation_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/AnnotatingElement_annotation_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/AnnotatingElement_annotation_SettingDelegate.java
- source_bytes: 2067
- source_sha256: `6105a45c0d80db53e7d31330ab9661cc293c270386dba60fee8d1fbbf2b9e290`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2025 Model Driven Solutions, Inc.
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

package org.omg.sysml.delegate.setting;

import org.eclipse.emf.common.util.EList;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.InternalEObject;
import org.omg.sysml.lang.sysml.AnnotatingElement;
import org.omg.sysml.lang.sysml.Annotation;
import org.omg.sysml.lang.sysml.Element;
import org.omg.sysml.util.NonNotifyingEObjectEList;

public class AnnotatingElement_annotation_SettingDelegate extends BasicDerivedListSettingDelegate {

	public AnnotatingElement_annotation_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}

	@Override
	protected EList<Annotation> basicGet(InternalEObject owner) {
		EList<Annotation> annotations = new NonNotifyingEObjectEList<>(Element.class, owner, eStructuralFeature.getFeatureID());
		Annotation owningAnnotatingRelationship = ((AnnotatingElement)owner).getOwningAnnotatingRelationship();
		if (owningAnnotatingRelationship != null) {
			annotations.add(owningAnnotatingRelationship);
		}
		annotations.addAll(((AnnotatingElement)owner).getOwnedAnnotatingRelationship());
		return annotations;
	}

}

````
