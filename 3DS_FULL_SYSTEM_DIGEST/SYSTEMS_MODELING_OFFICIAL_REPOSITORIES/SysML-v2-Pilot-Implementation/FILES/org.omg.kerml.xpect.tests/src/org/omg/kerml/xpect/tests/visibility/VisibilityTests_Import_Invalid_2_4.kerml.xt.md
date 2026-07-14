# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_4.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_4.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_4.kerml.xt
- source_bytes: 830
- source_sha256: `9381d6c22a5785eb33c2a8bea5f889f517089c69639b2a2030ea3a3e249848ca`
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
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_Private_alias::alias_protected'." at "VisibilityPackage::c_Private_alias::alias_protected"
	public import VisibilityPackage::c_Private_alias::alias_protected::*;
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_Private_alias::alias_public'." at "VisibilityPackage::c_Private_alias::alias_public"
	public import VisibilityPackage::c_Private_alias::alias_public::*;
}

````
