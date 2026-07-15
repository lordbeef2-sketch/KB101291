# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xtext/src/org/omg/kerml/xtext/naming/KerMLQualifiedNameProvider.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xtext/src/org/omg/kerml/xtext/naming/KerMLQualifiedNameProvider.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xtext/src/org/omg/kerml/xtext/naming/KerMLQualifiedNameProvider.java
- source_bytes: 1629
- source_sha256: `949d0b5a60d1209708e5098e56ba3a001f0f606c32e2a005de9d837015d17b88`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 * SysML 2 Pilot Implementation
 * Copyright (c) 2020,2023 Model Driven Solutions, Inc. 
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
 * Contributors:
 *  Zoltan Ujhelyi, MDS
 */

package org.omg.kerml.xtext.naming;

import org.eclipse.emf.ecore.EObject;
import org.eclipse.xtext.naming.DefaultDeclarativeQualifiedNameProvider;
import org.eclipse.xtext.util.SimpleAttributeResolver;
import org.omg.sysml.util.ElementUtil;

import com.google.common.base.Function;

public class KerMLQualifiedNameProvider extends DefaultDeclarativeQualifiedNameProvider {

	private Function<EObject, String> resolver = SimpleAttributeResolver.newResolver(String.class, "declaredName");
	
	@Override
	protected Function<EObject, String> getResolver() {
		Function<EObject, String> parentResolver = resolver;
		return object -> {
			String unescapedName = parentResolver.apply(object);
			return unescapedName == null ? null : "'" + ElementUtil.escapeString(unescapedName) + "'";
		};
	}

}

````
