# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_2.kerml.xt
- source_bytes: 830
- source_sha256: `896be257c6d212011420bbba2f56c99fbcfab18f05a3fdb177f43ddfa25cdfdd`
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
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_Public_alias::alias_private'." at "VisibilityPackage::c_Public_alias::alias_private"
	public import VisibilityPackage::c_Public_alias::alias_private::*;
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_Public_alias::alias_protected'." at "VisibilityPackage::c_Public_alias::alias_protected"
	public import VisibilityPackage::c_Public_alias::alias_protected::*;
}
	

````
