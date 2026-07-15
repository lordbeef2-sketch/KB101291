# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/SimpleImportAsFeatureTests_BadImportClass2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/SimpleImportAsFeatureTests_BadImportClass2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/validation/SimpleImportAsFeatureTests_BadImportClass2.kerml.xt
- source_bytes: 555
- source_sha256: `c7fe8c9a4f484db89c44a3cf2d4da6c24d37149b8f88d6d0ec7fe6bd9a4063cb`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyOuterPackage.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyOuterPackage.kerml"}
			}
		}
	}
END_SETUP 
*/

package test{
	public import OuterPackage::B::b;
	classifier C {
		// XPECT errors ---> "Couldn't resolve reference to Type 'B'." at "B"
		feature c: B;
	}
}



````
