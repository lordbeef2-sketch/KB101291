# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberFromOtherPackage.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberFromOtherPackage.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberFromOtherPackage.kerml.xt
- source_bytes: 1036
- source_sha256: `6814d370af02f1b810462b0bd3ddd4fca6d8e438fd296d435f9833546da3faf9`
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
//XPECT noErrors ---> ""
package test{
	package P{
		classifier A {}
		alias A_alias for A;
	}
	alias P1 for P;
	//XPECT linkedName at P1::A_alias --> test.P.A
	//* XPECT scope at P1::A_alias ---
		P.A, P.A.self, P.A.self.that, P.A_alias, P.A_alias.self, P.A_alias.self.that,
		P1.A, P1.A.self, P1.A.self.that, P1.A_alias, P1.A_alias.self, P1.A_alias.self.that,
		a, a.self, a.self.that, a.that, a.that.self, test.P.A, test.P.A.self,
		test.P.A.self.that, test.P.A_alias, test.P.A_alias.self, test.P.A_alias.self.that, test.P1.A,
		test.P1.A.self, test.P1.A.self.that, test.P1.A_alias, test.P1.A_alias.self,
		test.P1.A_alias.self.that, test.a, test.a.self, test.a.self.that, test.a.that, test.a.that.self
--- */
	feature a: P1::A_alias;
}

````
