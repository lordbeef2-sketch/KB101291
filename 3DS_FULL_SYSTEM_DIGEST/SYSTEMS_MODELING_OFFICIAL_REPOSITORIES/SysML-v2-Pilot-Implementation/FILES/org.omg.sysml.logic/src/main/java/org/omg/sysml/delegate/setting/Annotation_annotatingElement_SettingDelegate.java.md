# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Annotation_annotatingElement_SettingDelegate.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Annotation_annotatingElement_SettingDelegate.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/Annotation_annotatingElement_SettingDelegate.java
- source_bytes: 1688
- source_sha256: `7f712efb60253dd535dbe6a11df5eef08a35a830500343726f9a0c5788b2c0d5`
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

import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.InternalEObject;
import org.omg.sysml.lang.sysml.Annotation;
import org.omg.sysml.lang.sysml.Element;

public class Annotation_annotatingElement_SettingDelegate extends BasicDerivedObjectSettingDelegate {

	public Annotation_annotatingElement_SettingDelegate(EStructuralFeature eStructuralFeature) {
		super(eStructuralFeature);
	}
	
	@Override
	public Element basicGet(InternalEObject annotation) {
		Element ownedAnnotatingElement = ((Annotation)annotation).getOwnedAnnotatingElement();
		return ownedAnnotatingElement != null? ownedAnnotatingElement:
			((Annotation)annotation).getOwningAnnotatingElement();
	}

}

````
