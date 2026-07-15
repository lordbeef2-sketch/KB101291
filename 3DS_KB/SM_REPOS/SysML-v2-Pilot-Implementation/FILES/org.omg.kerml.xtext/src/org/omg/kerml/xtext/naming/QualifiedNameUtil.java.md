# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xtext/src/org/omg/kerml/xtext/naming/QualifiedNameUtil.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xtext/src/org/omg/kerml/xtext/naming/QualifiedNameUtil.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xtext/src/org/omg/kerml/xtext/naming/QualifiedNameUtil.java
- source_bytes: 2121
- source_sha256: `ef47e0b162be545c384316fffd4234881db95291c5726f7419005abad174afd7`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/**
 * SysML 2 Pilot Implementation
 * Copyright (C) 2025 Model Driven Solutions, Inc.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Eclipse Public License as published by
 * the Eclipse Foundation, version 2 of the License.
 * (at your option) any later version.
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
 *   Laszlo Gati, MDS
 *   Ed Seidewitz. MDS
 */
package org.omg.kerml.xtext.naming;

import java.util.List;

import org.eclipse.xtext.naming.QualifiedName;
import org.omg.sysml.util.ElementUtil;

/**
 * This class provides utility methods for qualified names that abstracts the representation of
 * globally scoped qualified names. The current implementation presumes that globally scoped
 * qualified names are represented as Xtext QualifiedNames whose first symbol is specific
 * String identified by ElementUtil.isGlobalScopeSymbol.
 */
public class QualifiedNameUtil {
	
	public static QualifiedName createQualifiedName(List<String> segments) {
		return QualifiedName.create(segments);
	}
	
	public static boolean isGlobalScopeQualification(QualifiedName qualifiedName) {
		return qualifiedName != null &&
				qualifiedName.getSegmentCount() > 0 &&
				ElementUtil.isGlobalScopeSymbol(qualifiedName.getFirstSegment()); 
	}

	public static QualifiedName getNonGlobalQualifiedName(QualifiedName qualifiedName) {
		return isGlobalScopeQualification(qualifiedName)? qualifiedName.skipFirst(1): qualifiedName;
	}
	
	public static String toQualifiedNameString(QualifiedName qualifiedName) {
		return ElementUtil.toQualifiedNameString(qualifiedName.getSegments());
	}
}

````
