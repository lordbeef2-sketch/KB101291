# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Valid_3_1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Valid_3_1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Valid_3_1.kerml.xt
- source_bytes: 495
- source_sha256: `119e6f496664185901b5124131b294e6295119c4e7c34c44f6e04bdf05cf6923`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.visibility.KerMLVisibilityTest
	ResourceSet {
		ThisFile {}
		File {from ="/src/DependencyVisibilityPackage.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/src/DependencyVisibilityPackage.kerml"}
			}
		}
	}
END_SETUP 
*/
//XPECT noErrors ---> ""
package Classes {
	public import VisibilityPackage::c_Public::*;
	feature a : c_public;
	feature b : VisibilityPackage::c_Public::c_public;
}

````
