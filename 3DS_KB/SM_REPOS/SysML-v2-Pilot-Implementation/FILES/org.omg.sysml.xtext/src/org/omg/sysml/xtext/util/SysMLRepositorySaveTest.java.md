# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xtext/src/org/omg/sysml/xtext/util/SysMLRepositorySaveTest.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xtext/src/org/omg/sysml/xtext/util/SysMLRepositorySaveTest.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xtext/src/org/omg/sysml/xtext/util/SysMLRepositorySaveTest.java
- source_bytes: 4637
- source_sha256: `4b1a22c1b7a954ba732fc9ea0c7616b382f2f6b5f7e7cb8c9f478cd1e609090a`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
/*******************************************************************************
 * SysML 2 Pilot Implementation
 * Copyright (c) 2021-2023 Model Driven Solutions, Inc.
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

package org.omg.sysml.xtext.util;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SysMLRepositorySaveTest extends SysMLRepositorySaveUtil {
	
	protected static final String[] TEST_FILES = {
		"01-Parts Tree/1c-Parts Tree Redefinition.sysml",
		"02-Parts Interconnection/2a-Parts Interconnection.sysml",
		"03-Function-based Behavior/3a-Function-based Behavior-1.sysml",
		"03-Function-based Behavior/3a-Function-based Behavior-2.sysml",
		"03-Function-based Behavior/3a-Function-based Behavior-3.sysml",
		"03-Function-based Behavior/3d-Function-based Behavior-item.sysml",
		"04-Functional Allocation/4a-Functional Allocation.sysml",
		"05-State-based Behavior/5-State-based Behavior-1.sysml",
		"05-State-based Behavior/5-State-based Behavior-1a.sysml",
		"06-Individual and Snapshots/6-Individual and Snapshots.sysml",
		"07-Variant Configuration/7b-Variant Configurations.sysml",
		"08-Requirements/8-Requirements.sysml",
		"09-Verification/9-Verification-simplified.sysml",
		"10-Analysis and Trades/10b-Trade-off Among Alternative Configurations.sysml",
		"10-Analysis and Trades/10c-Fuel Economy Analysis.sysml",
		"10-Analysis and Trades/10d-Dynamics Analysis.sysml",
		"11-View and Viewpoint/11a-View-Viewpoint.sysml",
		"11-View and Viewpoint/11b-Safety and Security Feature Views.sysml",
		"12-Dependency Relationships/12a-Dependency.sysml",
		"12-Dependency Relationships/12b-Allocation.sysml",
		"13-Model Containment/13a-Model Containment.sysml",
		"13-Model Containment/13b-Safety and Security Features Element Group.sysml",
		"13-Model Containment/13b-Safety and Security Features Element Group-1.sysml",
		"13-Model Containment/13b-Safety and Security Features Element Group-2.sysml",
		"14-Language Extensions/14a-Language Extensions.sysml",
		"14-Language Extensions/14b-Language Extensions.sysml",
		"14-Language Extensions/14c-Language Extensions.sysml",
		"15-Properties-Values-Expressions/15_05-Unification of Expression and Constraint Definition.sysml",
		"15-Properties-Values-Expressions/15_10-Primitive Data Types.sysml",
		"15-Properties-Values-Expressions/15_19-Materials with Properties.sysml",
		"17-Sequence Modeling/17a-Sequence-Modeling.sysml",
		"17-Sequence Modeling/17b-Sequence-Modeling.sysml",
		"18-Use Case/18-Use Case.sysml",
		"../training/19. Terminate Actions/Terminate Actions Example-1.sysml",
		"../examples/Association Examples/ProductSelection_UnownedEnds.sysml",
		"../examples/Geometry Examples/SimpleQuadcopter.sysml"
	};
	
	protected String testFilePath;

	public SysMLRepositorySaveTest(String testFilePath) {
		super();
		this.testFilePath = testFilePath;
	}
	
	@Override
	protected String[] processArgs(String[] args) {
		
		args = super.processArgs(args);
		
		if (args != null) {
			if (!args[0].endsWith("/")) {
				args[0] += "/";
			}
			args[0] += this.testFilePath;
		}
		
		return args;
	}
	
	public static void main(String[] args) {
		List<String> failedTests = new ArrayList<>();
		String[] args1 = Arrays.copyOf(args, args.length);
		for (String testFile: TEST_FILES) {
			try {
				SysMLRepositorySaveTest test = new SysMLRepositorySaveTest(testFile);
				test.run(args1);
				if (!test.isCommitted()) {
					failedTests.add(testFile);
				}
				System.out.println();				
			} catch (Exception e) {
				System.out.println("Error: " + e);
				failedTests.add(testFile);
			}
		}
		
		if (failedTests.isEmpty()) {
			System.out.println("NO FAILED TESTS");
		} else {
			System.out.println("FAILED TESTS:");
			for (String testFile: failedTests) {
				System.out.println(testFile);
			}
		}
	}

}

````
