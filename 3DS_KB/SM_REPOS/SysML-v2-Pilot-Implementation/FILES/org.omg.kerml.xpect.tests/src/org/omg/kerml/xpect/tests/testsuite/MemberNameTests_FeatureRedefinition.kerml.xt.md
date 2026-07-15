# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_FeatureRedefinition.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_FeatureRedefinition.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_FeatureRedefinition.kerml.xt
- source_bytes: 965
- source_sha256: `9ed9cdeb9fa1b82d37b9cbc59a9942d5f75fd968790687761149834372cf074f`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
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

// XPECT noErrors --> ""
package testt {
	feature A{
		feature a{}
	}
	alias B for A;
	//XPECT linkedName at B::a --> testt.A.a
	//* XPECT scope at B::a ---
	A, A.a, A.a.self, A.a.that, A.a.that.self, A.self, A.that, A.that.self, B, B.a,
	B.a.self, B.a.that, B.a.that.self, B.self, B.that, B.that.self, C, C.self, C.that,
	C.that.self, testt, testt.A, testt.A.a, testt.A.a.self, testt.A.a.that, testt.A.a.that.self,
	testt.A.self, testt.A.that, testt.A.that.self, testt.B, testt.B.a, testt.B.a.self,
	testt.B.a.that, testt.B.a.that.self, testt.B.self, testt.B.that, testt.B.that.self, testt.C,
	testt.C.self, testt.C.that, testt.C.that.self
	--- */
	alias C for B::a;
}
````
