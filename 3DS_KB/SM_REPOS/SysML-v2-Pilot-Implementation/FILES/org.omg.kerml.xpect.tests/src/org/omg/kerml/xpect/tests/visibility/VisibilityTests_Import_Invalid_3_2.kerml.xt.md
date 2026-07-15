# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_3_2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_3_2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_3_2.kerml.xt
- source_bytes: 1042
- source_sha256: `8522542ddcb1ad42c33669376898ff331fb596baf33062df3cd13504e2e8bb49`
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
	public import VisibilityPackage::c_clazz::*;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Protect'." at "c_Protect"
	feature a : c_Protect;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Protect::c_protect'." at "c_Protect::c_protect"
	feature b : c_Protect::c_protect;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Package'." at "c_Package"
	feature c : c_Package;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Package::c_publicc'." at "c_Package::c_publicc"
	feature d : c_Package::c_publicc;
	//XPECT errors --> "Couldn't resolve reference to Type 'c_Public::c_protect'." at "c_Public::c_protect"
	feature e : c_Public::c_protect;
}

````
