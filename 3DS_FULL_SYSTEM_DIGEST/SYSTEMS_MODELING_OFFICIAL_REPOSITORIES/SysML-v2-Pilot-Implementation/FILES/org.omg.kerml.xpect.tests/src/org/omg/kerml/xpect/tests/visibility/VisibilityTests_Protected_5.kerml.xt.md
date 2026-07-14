# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_5.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_5.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_5.kerml.xt
- source_bytes: 721
- source_sha256: `db3e886601457ecbdf0f3f217e0f19e2fcb3b299f8c8c17f8aa54e02bffc4e6f`
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
			protected classifier PPP{
				classifier PPPP{}
			}
		}
	}
	classifier C specializes P::PP {
		feature CC: PPP;
	}
	classifier D specializes C {
		feature DD: PPP;
	}
	classifier E specializes D {
		feature EE: PPP;
		feature GG: PPP::PPPP;
	}
}

````
