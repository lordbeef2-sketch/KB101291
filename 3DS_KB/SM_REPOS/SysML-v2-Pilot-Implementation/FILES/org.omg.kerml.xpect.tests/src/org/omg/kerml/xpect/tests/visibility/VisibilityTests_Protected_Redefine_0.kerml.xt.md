# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_Redefine_0.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_Redefine_0.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/visibility/VisibilityTests_Protected_Redefine_0.kerml.xt
- source_bytes: 1073
- source_sha256: `54d7e4e5d5a8f76bf8355d7e1312788860ad72438729bf3bf2a19090cc4c0c56`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.visibility.KerMLVisibilityTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
			}
		}
	}
END_SETUP 
*/

package testt {

	classifier P{
		classifier PP {
			protected feature PPP;
			protected feature PPP1;
			private feature PPP2;
		}
	}
	classifier A specializes P::PP{
		feature aa subsets PPP;
		feature bb redefines PPP1;
		feature cc subsets dd;
		feature dd;
		//XPECT errors --> "Couldn't resolve reference to Feature 'PPP2'." at "PPP2"
		feature ee: A redefines PPP2;
	}
	classifier B specializes A {
	}
	classifier C specializes B {
		feature ff subsets aa;
		feature gg redefines bb;
		feature hh subsets ii;
		feature ii;
		//XPECT errors --> "Couldn't resolve reference to Feature 'PPP1'." at "PPP1"
		feature jj: C redefines PPP1;
		//XPECT errors --> "Couldn't resolve reference to Feature 'PPP2'." at "PPP2"
		feature kk: C redefines PPP2;
	}
}

````
