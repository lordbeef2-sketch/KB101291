# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_5.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_5.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_5.kerml.xt
- source_bytes: 1045
- source_sha256: `b1a09e8cac0693bf971eedce63ff67e55b16981116918c186b5527c687f850d5`
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
	classifier A specializes c_Public_alias{
 		classifier AA specializes alias_protected{}
 		
 		// A::alias_protected does not resolve because qualified names currently require public visibility.
 		// XPECT errors --> "Couldn't resolve reference to Classifier 'A::alias_protected'." at "A::alias_protected" 		
 		classifier BB specializes A::alias_protected{}
 		// XPECT errors --> "Couldn't resolve reference to Classifier 'Test3::A::alias_protected'." at "Test3::A::alias_protected" 		
 		classifier CC specializes Test3::A::alias_protected{}
	}
}

````
