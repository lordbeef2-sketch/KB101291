# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsFeatureInheritance_1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsFeatureInheritance_1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_ImportAsFeatureInheritance_1.kerml.xt
- source_bytes: 1309
- source_sha256: `52e24c7a22c688d729fdec0a2c96646576854d0d70b5e88a6b31809d099b8a2f`
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
package Classes {
	public import VisibilityPackage::c_Public;
	classifier Try specializes c_Public {
		feature f1: c_protected;
		
 		// The following do not resolve because qualified names currently require public visibility.
 		// XPECT errors --> "Couldn't resolve reference to Type 'Try::c_protected'." at "Try::c_protected" 		
		feature f2: Try::c_protected;
 		// XPECT errors --> "Couldn't resolve reference to Type 'Classes::Try::c_protected'." at "Classes::Try::c_protected" 		
		feature f3: Classes::Try::c_protected;
 		// XPECT errors --> "Couldn't resolve reference to Type 'c_Public::c_protected'." at "c_Public::c_protected" 		
		feature f4: c_Public::c_protected;
 		// XPECT errors --> "Couldn't resolve reference to Type 'Classes::c_Public::c_protected'." at "Classes::c_Public::c_protected" 		
		feature f5: Classes::c_Public::c_protected;
	}
}

````
