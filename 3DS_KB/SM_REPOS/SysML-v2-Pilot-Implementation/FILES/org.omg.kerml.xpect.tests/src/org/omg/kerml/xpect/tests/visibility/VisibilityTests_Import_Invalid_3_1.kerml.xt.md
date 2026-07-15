# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_3_1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_3_1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_3_1.kerml.xt
- source_bytes: 1448
- source_sha256: `785fdfcdc8524dbcd6be6ee5b6b9db9899b24fcd11bbaa6176902c92b8f278dc`
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
package Classes {
	public import VisibilityPackage::c_Public::*;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_private'." at "c_private"
	feature a : c_private;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_protected'." at "c_protected"
	feature b : c_protected;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Public::c_private'." at "c_Public::c_private"
	feature c : c_Public::c_private;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Public::c_protected'." at "c_Public::c_protected"
	feature d : c_Public::c_protected;
	//XPECT errors --> "Couldn't resolve reference to Type 'VisibilityPackage::c_Public::c_private'." at "VisibilityPackage::c_Public::c_private"
	feature e : VisibilityPackage::c_Public::c_private;
	//XPECT errors --> "Couldn't resolve reference to Type 'VisibilityPackage::c_Public::c_protected'." at "VisibilityPackage::c_Public::c_protected"
	feature f : VisibilityPackage::c_Public::c_protected;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Public::c_public'." at "c_Public::c_public"
	feature g : c_Public::c_public;
}

````
