# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/indexing/KerMLIndexerTest.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/indexing/KerMLIndexerTest.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/indexing/KerMLIndexerTest.java
- source_bytes: 2247
- source_sha256: `2c56b86475038a1395033d94a6f02ac1bef0d994bcfc48eb21270ef089db2144`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.kerml.xpect.tests.indexing;

import org.eclipse.xpect.XpectImport;
import org.eclipse.xpect.expectation.ILinesExpectation;
import org.eclipse.xpect.expectation.LinesExpectation;
import org.eclipse.xpect.runner.LiveExecutionType;
import org.eclipse.xpect.runner.Xpect;
import org.eclipse.xpect.runner.XpectRunner;
import org.eclipse.xpect.runner.XpectTestFiles;
import org.eclipse.xpect.xtext.lib.setup.ThisResource;
import org.eclipse.xpect.xtext.lib.setup.XtextStandaloneSetup;
import org.eclipse.xpect.xtext.lib.setup.XtextWorkspaceSetup;
import org.eclipse.xtext.resource.IEObjectDescription;
import org.eclipse.xtext.resource.IResourceDescription;
import org.eclipse.xtext.resource.XtextResource;
import org.junit.BeforeClass;
import org.junit.runner.RunWith;
import org.omg.kerml.xpect.KerMLXtextTests;
import com.google.common.base.Function;
import com.google.common.collect.Iterables;
import com.google.inject.Inject;


/**
 * This class is a copied version of
 * {@link org.eclipse.xpect.xtext.lib.tests.ResourceDescriptionTest} where the
 * name output was updated to be KerML/SysML compatible.
 *
 */
@RunWith(XpectRunner.class)
@XpectTestFiles(fileExtensions = "xt")
@XpectImport({ XtextStandaloneSetup.class, XtextWorkspaceSetup.class })
public class KerMLIndexerTest {

	@BeforeClass
	public static void setup() {
		KerMLXtextTests.setup();
	}

	protected static class EObjectDescriptionToStringMapper implements Function<IEObjectDescription, String> {
		public String apply(IEObjectDescription desc) {
			return desc.getEClass().getEPackage().getNsPrefix() + "::" + desc.getEClass().getName() + ": " 
					+ desc.getName().toString("::");
		}
	}

	@Inject
	private IResourceDescription.Manager manager;
	
	@Xpect(liveExecution = LiveExecutionType.FAST)
	public void exportedObjects(@LinesExpectation ILinesExpectation expectation, @ThisResource XtextResource resource) {
		IResourceDescription resourceDescription = manager.getResourceDescription(resource);
		Iterable<IEObjectDescription> exportedObjects = resourceDescription.getExportedObjects();
		expectation.assertEquals(Iterables.transform(exportedObjects, new EObjectDescriptionToStringMapper()));
	}
}

````
