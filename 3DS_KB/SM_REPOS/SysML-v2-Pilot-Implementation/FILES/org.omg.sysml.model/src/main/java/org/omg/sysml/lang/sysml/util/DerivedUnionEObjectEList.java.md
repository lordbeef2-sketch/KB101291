# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/util/DerivedUnionEObjectEList.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/util/DerivedUnionEObjectEList.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/src/main/java/org/omg/sysml/lang/sysml/util/DerivedUnionEObjectEList.java
- source_bytes: 1571
- source_sha256: `33d2aaf557bf43b2291334479aab7370a05459fa47b8d01f5606fb210d5182f4`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*
 * Copyright (c) 2005, 2018 IBM Corporation and others.
 * All rights reserved.   This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v2.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v20.html
 *
 * Contributors:
 *   IBM - initial API and implementation
 *   Kenn Hussey - 535301
 *
 */
package org.omg.sysml.lang.sysml.util;

import java.util.List;
import java.util.ListIterator;

import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.InternalEObject;

/**
 * A derived list representing a union of all the elements from its source
 * features. This list is ideal for implementing derived union features.
 * 
 * This file comes from https://github.com/eclipse-uml2/uml2/blob/master/plugins/org.eclipse.uml2.common/src/org/eclipse/uml2/common/util/DerivedUnionEObjectEList.java.
 */
public class DerivedUnionEObjectEList<E> extends DerivedEObjectEList<E> {

	public DerivedUnionEObjectEList(Class<?> dataClass, InternalEObject owner,
			int featureID, int[] sourceFeatureIDs) {
		super(dataClass, owner, featureID, sourceFeatureIDs);
	}

	@Override
	public List<E> basicList() {
		return new DerivedUnionEObjectEList<E>(dataClass, owner, featureID,
			sourceFeatureIDs) {

			@Override
			public ListIterator<E> listIterator(int index) {
				return basicListIterator(index);
			}
		};
	}

	@Override
	protected boolean isIncluded(EStructuralFeature feature) {
		return true;
	}

}

````
