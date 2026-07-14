# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Import_Invalid_1.kerml.xt
- source_bytes: 1797
- source_sha256: `a245dbaa02c31638577acac3e3faab6ec8ed35af18d23ff47503f025bb4ae581`
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


package Test3{
	public import VisibilityPackage::c_clazz::*;
	// XPECT errors --> "Couldn't resolve reference to Classifier 'c_Protect::c_publicc'." at "c_Protect::c_publicc"
	classifier A specializes c_Protect::c_publicc{}
	// XPECT errors --> "Couldn't resolve reference to Classifier 'VisibilityPackage::c_clazz::c_Protect::c_publicc'." at "VisibilityPackage::c_clazz::c_Protect::c_publicc"
	classifier A1 specializes VisibilityPackage::c_clazz::c_Protect::c_publicc{}
	//XPECT errors --> "Couldn't resolve reference to Classifier 'c_Protect'." at "c_Protect"
	classifier B specializes c_Protect{}
	//XPECT errors --> "Couldn't resolve reference to Classifier 'c_Protect::c_protect'." at "c_Protect::c_protect"
	classifier C specializes c_Protect::c_protect{}
	//XPECT errors --> "Couldn't resolve reference to Classifier 'c_Package'." at "c_Package"
	classifier D specializes c_Package{}
	//XPECT errors --> "Couldn't resolve reference to Classifier 'c_Package::c_publicc'." at "c_Package::c_publicc"
	classifier E specializes c_Package::c_publicc{}
	//XPECT errors --> "Couldn't resolve reference to Classifier 'c_Public::c_protect'." at "c_Public::c_protect"
	classifier F specializes c_Public::c_protect{}
	//XPECT errors --> "Couldn't resolve reference to Classifier 'c_Public::c_package'." at "c_Public::c_package"
	classifier G specializes c_Public::c_package{}
}

````
