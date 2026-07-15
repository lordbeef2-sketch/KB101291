# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/AllSysMLXpectTests.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/AllSysMLXpectTests.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/src/org/omg/sysml/xpect/tests/AllSysMLXpectTests.java
- source_bytes: 485
- source_sha256: `c63a11167f9618ff60fb4f0b8affd77226b8031da0ad964bd3099414aada5da4`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.sysml.xpect.tests;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import org.junit.runners.Suite.SuiteClasses;

@SuiteClasses({ 
		org.omg.sysml.xpect.tests.expression.SysMLTests.class,
		org.omg.sysml.xpect.tests.simpletests.SysMLTests.class,
		org.omg.sysml.xpect.tests.validation.invalid.SysMLTests.class,
		org.omg.sysml.xpect.tests.validation.valid.SysMLTests.class,
})
@RunWith(Suite.class)
public class AllSysMLXpectTests {

}

````
