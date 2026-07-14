# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_invalid_0.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_invalid_0.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_invalid_0.kerml.xt
- source_bytes: 771
- source_sha256: `1191e1025531512c6f75dc95af0996f836e987edcc25d5729583dd49c74c590c`
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
	//XPECT errors --> "Couldn't resolve reference to Classifier 'c_Protect'." at "c_Protect"
	classifier A specializes c_Protect{
	}
	//XPECT errors --> "Couldn't resolve reference to Classifier 'c_Protect::c_publicc'." at "c_Protect::c_publicc"
	classifier B specializes c_Protect::c_publicc{
	}
}

````
