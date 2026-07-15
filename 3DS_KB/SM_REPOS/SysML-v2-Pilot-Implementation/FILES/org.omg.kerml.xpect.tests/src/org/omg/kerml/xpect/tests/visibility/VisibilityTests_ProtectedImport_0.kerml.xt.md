# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_0.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_0.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_0.kerml.xt
- source_bytes: 1295
- source_sha256: `b29618b4547a72ae87a60c98903d9cda626e4a0f2ca4ca87e38169bf0de9143f`
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

// XPECT noErrors ---> ""
package Test3{
	public import VisibilityPackage::*;
	classifier A specializes c_clazz{
 		classifier AA specializes c_Protect::c_publicc{}
 
 		// A::alias_protected does not resolve because qualified names currently require public visibility.
 		// XPECT errors --> "Couldn't resolve reference to Classifier 'A::c_Protect::c_publicc'." at "A::c_Protect::c_publicc" 		
 		classifier BB specializes A::c_Protect::c_publicc{}
  		// XPECT errors --> "Couldn't resolve reference to Classifier 'Test3::A::c_Protect::c_publicc'." at "Test3::A::c_Protect::c_publicc" 		
 		classifier CC specializes Test3::A::c_Protect::c_publicc{}

 		classifier DD specializes c_Protect{}
	}
	classifier B specializes c_Public_alias{
 		classifier AA specializes alias_protected{}
	}
	classifier C specializes c_Public{
		classifier CC specializes c_protected{}
	}
}

````
