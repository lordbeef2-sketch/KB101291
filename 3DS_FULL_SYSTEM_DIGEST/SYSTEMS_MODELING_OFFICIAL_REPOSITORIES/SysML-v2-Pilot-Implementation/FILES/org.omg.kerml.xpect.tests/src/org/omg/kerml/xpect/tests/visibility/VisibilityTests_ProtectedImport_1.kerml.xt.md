# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_1.kerml.xt
- source_bytes: 1143
- source_sha256: `c94cf92959b25fdffcb2f0d66e5ae56edee899d8abbee597dd9322df53c230b4`
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
 		
 		feature ff: c_Protect subsets gg;
 		protected feature gg;
	}
}

````
