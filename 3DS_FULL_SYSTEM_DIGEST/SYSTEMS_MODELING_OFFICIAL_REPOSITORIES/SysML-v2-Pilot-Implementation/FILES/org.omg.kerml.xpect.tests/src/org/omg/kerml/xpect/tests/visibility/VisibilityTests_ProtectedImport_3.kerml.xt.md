# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_3.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_3.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ProtectedImport_3.kerml.xt
- source_bytes: 839
- source_sha256: `24c37f455a942ccf78229635817a415df0df02864bdcefb2d0662c22abdd0609`
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
		// XPECT errors --> "Couldn't resolve reference to Classifier 'A::c_Protect'." at "A::c_Protect"
  		classifier EE specializes A::c_Protect{}
	}
	
 	//special case when full qualifiedname within the specialization.
		
}
	

````
