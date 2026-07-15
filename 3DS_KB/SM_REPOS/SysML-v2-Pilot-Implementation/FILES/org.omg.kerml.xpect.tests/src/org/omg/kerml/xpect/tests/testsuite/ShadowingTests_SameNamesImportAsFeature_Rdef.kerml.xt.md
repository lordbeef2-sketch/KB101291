# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesImportAsFeature_Rdef.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesImportAsFeature_Rdef.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesImportAsFeature_Rdef.kerml.xt
- source_bytes: 963
- source_sha256: `f9c310808e61414e8d691c9c8c6f846f363c8555769786412b9c364c0192a58b`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencySamePackageName_A_Feature.kerml"}
		File {from ="/src/DependencySamePackageName_B_Feature.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencySamePackageName_A_Feature.kerml"}
				File {from ="/src/DependencySamePackageName_B_Feature.kerml"}
			}
		}
	}
END_SETUP 
*/
//Both DepedencySamePackageName_A and DependencySamePackageName_B have the same package names "SamePackage"
//Current implemention public import from the first src package(A).
//XPECT noErrors --> ""
package test{
	public import SamePackage::container;
	feature something1 subsets container.A{}
	// XPECT errors --> "Couldn't resolve reference to Feature 'B'." at "B"
	feature something2 subsets container.B{}
}

````
