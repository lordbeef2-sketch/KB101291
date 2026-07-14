# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/DerivedPropertySettingDelegateFactory.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/DerivedPropertySettingDelegateFactory.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic/src/main/java/org/omg/sysml/delegate/setting/DerivedPropertySettingDelegateFactory.java
- source_bytes: 2738
- source_sha256: `1723b2b6042b1cfd1d1fd9b9a5ac0d03b7afef541603d5554b0b28ddf100ecbe`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2022 Model Driven Solutions, Inc.
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

import java.lang.reflect.Constructor;
import java.util.HashMap;
import java.util.Map;

import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.emf.ecore.EStructuralFeature.Internal.SettingDelegate;

public class DerivedPropertySettingDelegateFactory 
	implements EStructuralFeature.Internal.SettingDelegate.Factory {
	
	public static final String SYSML_ANNOTATION = "http://www.omg.org/spec/SysML";
	
	private static final String PACKAGE_NAME = DerivedPropertySettingDelegateFactory.class.getPackage().getName();
	
	private final Map<EStructuralFeature, Constructor<?>> constructorMap = new HashMap<>();
	
	protected Constructor<?> getDelegateConstructor(EStructuralFeature eStructuralFeature) {
		Constructor<?> constructor = constructorMap.get(eStructuralFeature);
		if (constructor == null) {
			try {
				String delegateName = PACKAGE_NAME + "." + 
						eStructuralFeature.getEContainingClass().getName() + "_" + 
						eStructuralFeature.getName() + "_SettingDelegate";
				constructor = Class.forName(delegateName).getConstructor(EStructuralFeature.class);
				constructorMap.put(eStructuralFeature, constructor);
			} catch (ClassNotFoundException e) {
			} catch (Exception e) {
				throw new RuntimeException(e);
			}
		}
		return constructor;
	}
	
	@Override
	public SettingDelegate createSettingDelegate(EStructuralFeature eStructuralFeature) {
		Constructor<?> constructor = getDelegateConstructor(eStructuralFeature);
		if (constructor == null) {
			return new DefaultDerivedPropertySettingDelegate(eStructuralFeature);
		} else {
			try {
				return (SettingDelegate) constructor.newInstance(eStructuralFeature);
			} catch (Exception e) {
				throw new RuntimeException(e);
			}
		}
	}

}

````
