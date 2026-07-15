# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_0.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_0.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_0.kerml.xt
- source_bytes: 1078
- source_sha256: `fde09fe2a89b3976578ffa851bfabcc2137e45187bdcbad5808ebead73d7e9f8`
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
	classifier P{
		protected classifier PP{}
	}
	classifier A specializes P {
 		classifier AA specializes PP{}
 		
 		// P::PP does not resolve because qualified names currently require public visibility.
 		// XPECT errors --> "Couldn't resolve reference to Classifier 'P::PP'." at "P::PP"
 		classifier BB specializes P::PP{}
  		// XPECT errors --> "Couldn't resolve reference to Classifier 'Test3::P::PP'." at "Test3::P::PP"
 		classifier CC specializes Test3::P::PP{}
 		
 		feature DD: PP;
	}	
	classifier B {
		feature BB1: P;
		// XPECT errors --> "Couldn't resolve reference to Type 'P::PP'." at "P::PP"
		feature BB2: P::PP; 
	}
}

````
