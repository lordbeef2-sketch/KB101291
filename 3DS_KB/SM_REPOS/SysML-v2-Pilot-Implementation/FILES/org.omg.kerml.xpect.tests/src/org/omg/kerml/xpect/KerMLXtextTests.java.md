# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/KerMLXtextTests.java

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/KerMLXtextTests.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/KerMLXtextTests.java
- source_bytes: 833
- source_sha256: `e78d4c02b82a82b230377c01a366d4cf460e9e1c35b21f9cbd8f9ea78f50d131`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package org.omg.kerml.xpect;

import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.EStructuralFeature;
import org.eclipse.xpect.xtext.lib.tests.XtextTests;
import org.junit.BeforeClass;
import org.omg.sysml.delegate.setting.DerivedPropertySettingDelegateFactory;
import org.omg.sysml.delegate.invocation.OperationInvocationDelegateFactory;

public class KerMLXtextTests extends XtextTests {

	@BeforeClass
	public static void setup() {
		EStructuralFeature.Internal.SettingDelegate.Factory.Registry.INSTANCE.
			put(DerivedPropertySettingDelegateFactory.SYSML_ANNOTATION, new DerivedPropertySettingDelegateFactory());
		EOperation.Internal.InvocationDelegate.Factory.Registry.INSTANCE.
			put(OperationInvocationDelegateFactory.SYSML_ANNOTATION, new OperationInvocationDelegateFactory());	
	}

}

````
