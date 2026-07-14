# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesImport_Rdef.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesImport_Rdef.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesImport_Rdef.kerml.xt
- source_bytes: 918
- source_sha256: `668ee0d2c85599c125b4a7ba8d90f5727fdff6ee59f7f137761f1d1fa11238a1`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencySamePackageName_A_Feature.kerml" }
		File {from ="/src/DependencySamePackageName_B_Feature.kerml" }
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencySamePackageName_A_Feature.kerml" }
				File {from ="/src/DependencySamePackageName_B_Feature.kerml" }
			}
		}
	}
END_SETUP 
*/
//Both DepedencySamePackageName_A and DependencySamePackageName_B have the same package names "SamePackage"
//Current implemention public import from the first src package(A).
package test{
	public import SamePackage::container::*;
	alias something1 for A;
	// XPECT errors at A --> "Couldn't resolve reference to Element 'B'." at "B"
	alias something2 for B;
}


````
