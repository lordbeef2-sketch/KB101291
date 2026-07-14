# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_8.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_8.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_2_8.kerml.xt
- source_bytes: 1024
- source_sha256: `593dc4d89676c9ad4ced3d2aaa225a0c4d3d71e59860450fc325550df7ca4dee`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.visibility.KerMLVisibilityTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyVisibilityPackage.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyVisibilityPackage.kerml"}
			}
		}
	}
END_SETUP 
*/

package Classes {
	public import VisibilityPackage::c_clazz;
	// XPECT errors --> "Couldn't resolve reference to Classifier 'c_clazz::c_Package::c_publicc'." at "c_clazz::c_Package::c_publicc"	
	classifier A specializes c_clazz::c_Package::c_publicc{}
	// XPECT errors --> "Couldn't resolve reference to Type 'c_clazz::c_Package::c_publicc'." at "c_clazz::c_Package::c_publicc"
	feature f : c_clazz::c_Package::c_publicc;
	// XPECT errors --> "Couldn't resolve reference to Classifier 'c_clazz::c_Public::c_protect'." at "c_clazz::c_Public::c_protect"
	classifier B specializes c_clazz::c_Public::c_protect{}
}


````
