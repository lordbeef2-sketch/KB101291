# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/linking/KerMLLinkingTest.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/linking/KerMLLinkingTest.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/linking/KerMLLinkingTest.java
- source_bytes: 515
- source_sha256: `2edf745d4c1e5ce6d4b1fed3d4c058af2f6162ef78b30a99faf15c7be4dcfbdb`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.kerml.xpect.tests.linking;

import org.junit.BeforeClass;
import org.junit.runner.RunWith;
import org.omg.kerml.xpect.KerMLXtextTests;
import org.eclipse.xpect.runner.XpectRunner;
import org.eclipse.xpect.runner.XpectTestFiles;
import org.eclipse.xpect.xtext.lib.tests.LinkingTest;

@RunWith(XpectRunner.class)
@XpectTestFiles(fileExtensions = "xt")
public class KerMLLinkingTest extends LinkingTest {

	@BeforeClass
	public static void setup() {
		KerMLXtextTests.setup();
	}

}

````
