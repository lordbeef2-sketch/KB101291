# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberFromOtherPackage2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberFromOtherPackage2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberFromOtherPackage2.kerml.xt
- source_bytes: 2332
- source_sha256: `f9eabb29f4df84780b200fb3cdfeb1c057d4cd2e94528f0f99cc68e2c6d90c12`
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
package test{
	package P{
		classifier A {
			classifier AA{
				classifier AAA{}
			}
		}
		alias A_alias for A;
	}
	
	alias P1 for P;
	//XPECT linkedName at P1::A_alias --> test.P.A
	//* XPECT scope at P1::A_alias ---
		P.A, P.A.AA, P.A.AA.AAA, P.A.AA.AAA.self, P.A.AA.AAA.self.that, P.A.AA.self,
		P.A.AA.self.that, P.A.self, P.A.self.that, P.A_alias, P.A_alias.AA, P.A_alias.AA.AAA,
		P.A_alias.AA.AAA.self, P.A_alias.AA.AAA.self.that, P.A_alias.AA.self, P.A_alias.AA.self.that,
		P.A_alias.self, P.A_alias.self.that, P1.A, P1.A.AA, P1.A.AA.AAA, P1.A.AA.AAA.self,
		P1.A.AA.AAA.self.that, P1.A.AA.self, P1.A.AA.self.that, P1.A.self, P1.A.self.that, P1.A_alias,
		P1.A_alias.AA, P1.A_alias.AA.AAA, P1.A_alias.AA.AAA.self, P1.A_alias.AA.AAA.self.that,
		P1.A_alias.AA.self, P1.A_alias.AA.self.that, P1.A_alias.self, P1.A_alias.self.that, a, a.AA,
		a.AA.AAA, a.AA.AAA.self, a.AA.AAA.self.that, a.AA.self, a.AA.self.that, a.self,
		a.self.that, a.that, a.that.self, test.P.A, test.P.A.AA, test.P.A.AA.AAA,
		test.P.A.AA.AAA.self, test.P.A.AA.AAA.self.that, test.P.A.AA.self, test.P.A.AA.self.that,
		test.P.A.self, test.P.A.self.that, test.P.A_alias, test.P.A_alias.AA, test.P.A_alias.AA.AAA,
		test.P.A_alias.AA.AAA.self, test.P.A_alias.AA.AAA.self.that, test.P.A_alias.AA.self,
		test.P.A_alias.AA.self.that, test.P.A_alias.self, test.P.A_alias.self.that, test.P1.A, test.P1.A.AA,
		test.P1.A.AA.AAA, test.P1.A.AA.AAA.self, test.P1.A.AA.AAA.self.that, test.P1.A.AA.self,
		test.P1.A.AA.self.that, test.P1.A.self, test.P1.A.self.that, test.P1.A_alias, test.P1.A_alias.AA,
		test.P1.A_alias.AA.AAA, test.P1.A_alias.AA.AAA.self, test.P1.A_alias.AA.AAA.self.that,
		test.P1.A_alias.AA.self, test.P1.A_alias.AA.self.that, test.P1.A_alias.self, test.P1.A_alias.self.that,
		test.a, test.a.AA, test.a.AA.AAA, test.a.AA.AAA.self, test.a.AA.AAA.self.that,
		test.a.AA.self, test.a.AA.self.that, test.a.self, test.a.self.that, test.a.that,
		test.a.that.self
--- */
	feature a: P1::A_alias ;
	
}

````
