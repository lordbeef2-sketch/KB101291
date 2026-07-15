# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesImport_FT.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesImport_FT.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesImport_FT.kerml.xt
- source_bytes: 955
- source_sha256: `040bdae89718c1e54a5b8586ec160aca2501c2004492b7ad375d468762b5c959`
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
	feature something1 : A{}
	//pass junit test
	//* XPECT errors at A ---
	   "Couldn't resolve reference to Type 'B'." at "B"
	   --- */
	feature something2 : B{}
}


````
