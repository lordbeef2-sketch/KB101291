# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_6.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_6.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_6.kerml.xt
- source_bytes: 793
- source_sha256: `7f7a545065334dbeaf53f662652a28121e0680617d885a1c817f78158aa91083`
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
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_clazz::c_Protect::c_protect'." at "VisibilityPackage::c_clazz::c_Protect::c_protect"
	public import VisibilityPackage::c_clazz::c_Protect::c_protect::*;
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_clazz::c_Package'." at "VisibilityPackage::c_clazz::c_Package"
	public import VisibilityPackage::c_clazz::c_Package::*;
	
}


````
