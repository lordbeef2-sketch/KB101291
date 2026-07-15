# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_5.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_5.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_5.kerml.xt
- source_bytes: 790
- source_sha256: `368e14fb64a2c436fc24a8b2b4423647caa4693a2e6983567d0f2476415d7ccf`
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
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_clazz::c_Protect'." at "VisibilityPackage::c_clazz::c_Protect"
	public import VisibilityPackage::c_clazz::c_Protect::*;
	//XPECT errors --> "Couldn't resolve reference to Namespace 'VisibilityPackage::c_clazz::c_Protect::c_publicc'." at "VisibilityPackage::c_clazz::c_Protect::c_publicc"
	public import VisibilityPackage::c_clazz::c_Protect::c_publicc::*;
}


````
