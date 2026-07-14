# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_4.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_4.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_4.kerml.xt
- source_bytes: 853
- source_sha256: `73acfe12e61d4c1cccee54501a732752b4f1bb31beaf33cb23c8511abf2480de`
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
		// This does not resolve because qualified names currently require public visbility.
		// XPECT errors --> "Couldn't resolve reference to Classifier 'Test3::A::c_Protect'." at "Test3::A::c_Protect"
 		classifier EE specializes Test3::A::c_Protect{}
	}
 	//special case when full qualifiedname within the specialization.
		
}

````
