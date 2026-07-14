# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/AllKerMLXpectTests.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/AllKerMLXpectTests.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/AllKerMLXpectTests.java
- source_bytes: 1204
- source_sha256: `74d522afc7806814ad8ba8770f2e0cb6cc8bae20717fb2c8fe2270fa5d8a0003`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.kerml.xpect.tests;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import org.junit.runners.Suite.SuiteClasses;
import org.omg.kerml.xpect.tests.imports.global.KerMLImportGlobalTest;
import org.omg.kerml.xpect.tests.imports.local.KerMLImportLocalTest;
import org.omg.kerml.xpect.tests.imports.recursive.KerMLImportRecursiveTest;
import org.omg.kerml.xpect.tests.indexing.KerMLIndexerTest;
import org.omg.kerml.xpect.tests.linking.KerMLLinkingTest;
import org.omg.kerml.xpect.tests.parsing.KerMLParsingTest;
import org.omg.kerml.xpect.tests.scoping.KerMLScopingTest;
import org.omg.kerml.xpect.tests.testsuite.KerMLXtextTest;
import org.omg.kerml.xpect.tests.validation.KerMLValidationTest;
import org.omg.kerml.xpect.tests.visibility.KerMLVisibilityTest;

@SuiteClasses({ 
		KerMLImportGlobalTest.class, //
		KerMLImportLocalTest.class, //
		KerMLImportRecursiveTest.class, //
		KerMLLinkingTest.class,//
		KerMLParsingTest.class, //
		KerMLScopingTest.class, //
		KerMLXtextTest.class, //
		KerMLValidationTest.class, //
		KerMLVisibilityTest.class,
		KerMLIndexerTest.class
})
@RunWith(Suite.class)
public class AllKerMLXpectTests {

}

````
