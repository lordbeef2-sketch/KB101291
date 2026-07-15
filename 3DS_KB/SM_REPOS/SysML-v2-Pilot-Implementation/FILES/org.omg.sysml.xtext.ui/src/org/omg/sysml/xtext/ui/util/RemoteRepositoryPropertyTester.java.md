# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xtext.ui/src/org/omg/sysml/xtext/ui/util/RemoteRepositoryPropertyTester.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xtext.ui/src/org/omg/sysml/xtext/ui/util/RemoteRepositoryPropertyTester.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xtext.ui/src/org/omg/sysml/xtext/ui/util/RemoteRepositoryPropertyTester.java
- source_bytes: 1653
- source_sha256: `a57a8eb55e94963c131c6b18d112a7a77459ea3d13ad1169deac75ce5bc96cf4`
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
 *   Zoltan Ujhelyi, MDS
 */
package org.omg.sysml.xtext.ui.util;

import java.util.Objects;

import org.eclipse.core.expressions.PropertyTester;
import org.eclipse.core.resources.IProject;
import org.omg.sysml.xtext.ui.handlers.PullRepositoryProject;

public class RemoteRepositoryPropertyTester extends PropertyTester {

	private static final String REPOSITORY_DESCRIPTOR_TESTER = "repository_descriptor";
	
	public RemoteRepositoryPropertyTester() {
	}

	@Override
	public boolean test(Object receiver, String property, Object[] args, Object expectedValue) {
		if (Objects.equals(REPOSITORY_DESCRIPTOR_TESTER, REPOSITORY_DESCRIPTOR_TESTER) && receiver instanceof IProject project && project.isAccessible()) {
			return project.getFile(PullRepositoryProject.REPOSITORY_CONFIGURATION_FILE).exists();
		}
		return false;
	}

}

````
