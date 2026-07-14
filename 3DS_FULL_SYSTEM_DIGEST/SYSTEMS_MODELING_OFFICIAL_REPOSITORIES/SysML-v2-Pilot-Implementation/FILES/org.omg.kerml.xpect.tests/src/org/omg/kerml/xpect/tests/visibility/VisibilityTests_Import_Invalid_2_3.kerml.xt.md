# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_3.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_3.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_3.kerml.xt
- source_bytes: 1008
- source_sha256: `5474e96ef0848cb80663fd7482a04e9123788030a1ea6b6b9f23a9dd0548be17`
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
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_Private_alias'." at "VisibilityPackage::c_Private_alias"
	public import VisibilityPackage::c_Private_alias::*;
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_Private_alias::c_public'." at "VisibilityPackage::c_Private_alias::c_public"
	public import VisibilityPackage::c_Private_alias::c_public::*;
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_Private_alias::alias_private'." at "VisibilityPackage::c_Private_alias::alias_private"
	public import VisibilityPackage::c_Private_alias::alias_private::*;
}

````
