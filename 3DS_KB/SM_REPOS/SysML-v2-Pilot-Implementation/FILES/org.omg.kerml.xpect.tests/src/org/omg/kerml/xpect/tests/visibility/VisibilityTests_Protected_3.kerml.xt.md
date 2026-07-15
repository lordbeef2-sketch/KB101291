# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_3.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_3.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_3.kerml.xt
- source_bytes: 864
- source_sha256: `5374eeed3fc7e1a3d08df5fe591e3cae1397847f5809b5271c33a73e6f50bfca`
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
		classifier PP {
			protected classifier PPP{}
		}
	}
	classifier C specializes P::PP {
		feature CC: PPP;
	}
	
	classifier A specializes P {
		// XPECT errors --> "Couldn't resolve reference to Classifier 'PP::PPP'." at "PP::PPP"
 		classifier AA specializes PP::PPP{}
	}
	classifier B {
		// XPECT errors --> "Couldn't resolve reference to Type 'P::PP::PPP'." at "P::PP::PPP"
		feature BB2: P::PP::PPP;
	}
}

````
