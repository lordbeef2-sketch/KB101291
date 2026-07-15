# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Valid_2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Valid_2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Valid_2.kerml.xt
- source_bytes: 925
- source_sha256: `8108054c1f541aa940594b41fd89edb0d39d1314dd8895792cb1e25d95e4820a`
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
package Test3{
	public import VisibilityPackage::c_Public::*;
	public import VisibilityPackage::c_Public::c_public::*;
	public import VisibilityPackage::c_Public_alias::*;
	public import VisibilityPackage::c_Public_alias::c_public::*;
	public import VisibilityPackage::c_Public_alias::alias_public::*;
	public import VisibilityPackage::c_clazz::*;
	public import VisibilityPackage::c_clazz::c_Public::*;
	public import VisibilityPackage::c_clazz::c_Public::c_publicc::*;
	public import VisibilityPackage::c_clazz::c_Public::c_publicc;
	feature try : c_publicc;
}

````
