# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/KerMLValidationTest.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/KerMLValidationTest.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/KerMLValidationTest.java
- source_bytes: 528
- source_sha256: `f8b855dfe227f65ee0ac22ccd6e46ca3bb9b1ca64f8e522855e9f7967117f611`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.kerml.xpect.tests.validation;

import org.eclipse.xpect.runner.XpectRunner;
import org.eclipse.xpect.runner.XpectTestFiles;
import org.eclipse.xpect.xtext.lib.tests.ValidationTest;
import org.junit.BeforeClass;
import org.junit.runner.RunWith;
import org.omg.kerml.xpect.KerMLXtextTests;

@RunWith(XpectRunner.class)
@XpectTestFiles(fileExtensions = "xt")
public class KerMLValidationTest extends ValidationTest {
	
	@BeforeClass
	public static void setup() {
		KerMLXtextTests.setup();
	}

}

````
