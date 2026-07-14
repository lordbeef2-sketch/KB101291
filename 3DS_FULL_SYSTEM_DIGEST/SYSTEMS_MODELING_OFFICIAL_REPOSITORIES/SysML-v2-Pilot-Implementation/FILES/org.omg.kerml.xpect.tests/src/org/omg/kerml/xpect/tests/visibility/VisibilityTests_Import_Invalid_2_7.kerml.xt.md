# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_7.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_7.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_7.kerml.xt
- source_bytes: 820
- source_sha256: `deada318325a0c30602e1c8625598404d0216d53bb2d064ddf72652aaea33031`
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


package Test3{
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_clazz::c_Package::c_publicc'." at "VisibilityPackage::c_clazz::c_Package::c_publicc"
	public import VisibilityPackage::c_clazz::c_Package::c_publicc::*;
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_clazz::c_Public::c_protect'." at "VisibilityPackage::c_clazz::c_Public::c_protect"
	public import VisibilityPackage::c_clazz::c_Public::c_protect::*;
}


````
