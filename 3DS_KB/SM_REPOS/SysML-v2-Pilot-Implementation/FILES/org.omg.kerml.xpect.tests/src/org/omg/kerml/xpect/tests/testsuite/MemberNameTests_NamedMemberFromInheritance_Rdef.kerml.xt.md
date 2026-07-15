# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberFromInheritance_Rdef.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberFromInheritance_Rdef.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_NamedMemberFromInheritance_Rdef.kerml.xt
- source_bytes: 2447
- source_sha256: `0a0b1999dbe96de0034305216430c2d56ef4ea4ce65a211639ea322196c5e564`
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
	feature A{
		feature a {}
		alias aa for a;
	}
//* XPECT scope at A ---
	A, A.a, A.a.self, A.a.that, A.a.that.self, A.aa, A.aa.self, A.aa.that,
	A.aa.that.self, A.self, A.that, A.that.self, B, B.a, B.a.self, B.a.that, B.a.that.self, B.aa,
	B.aa.self, B.aa.that, B.aa.that.self, B.b, B.b.self, B.b.that, B.b.that.self, B.b_alias,
	B.b_alias.self, B.b_alias.that, B.b_alias.that.self, B.self, B.that, B.that.self, test.A,
	test.A.a, test.A.a.self, test.A.a.that, test.A.a.that.self, test.A.aa, test.A.aa.self,
	test.A.aa.that, test.A.aa.that.self, test.A.self, test.A.that, test.A.that.self, test.B,
	test.B.a, test.B.a.self, test.B.a.that, test.B.a.that.self, test.B.aa, test.B.aa.self,
	test.B.aa.that, test.B.aa.that.self, test.B.b, test.B.b.self, test.B.b.that,
	test.B.b.that.self, test.B.b_alias, test.B.b_alias.self, test.B.b_alias.that,
	test.B.b_alias.that.self, test.B.self, test.B.that, test.B.that.self
--- */
	feature B subsets A{
		//* XPECT scope at aa ---
	A, A.a, A.a.self, A.a.that, A.a.that.self, A.aa, A.aa.self, A.aa.that,
	A.aa.that.self, A.self, A.that, A.that.self, B, B.a, B.a.self, B.a.that, B.a.that.self, B.aa,
	B.aa.self, B.aa.that, B.aa.that.self, B.b, B.b.self, B.b.that, B.b.that.self, B.b_alias,
	B.b_alias.self, B.b_alias.that, B.b_alias.that.self, B.self, B.that, B.that.self, a, a.self,
	a.that, a.that.self, aa, aa.self, aa.that, aa.that.self, b, b.self, b.that,
	b.that.self, b_alias, b_alias.self, b_alias.that, b_alias.that.self, self, test.A, test.A.a,
	test.A.a.self, test.A.a.that, test.A.a.that.self, test.A.aa, test.A.aa.self, test.A.aa.that,
	test.A.aa.that.self, test.A.self, test.A.that, test.A.that.self, test.B, test.B.a, test.B.a.self,
	test.B.a.that, test.B.a.that.self, test.B.aa, test.B.aa.self, test.B.aa.that,
	test.B.aa.that.self, test.B.b, test.B.b.self, test.B.b.that, test.B.b.that.self, test.B.b_alias,
	test.B.b_alias.self, test.B.b_alias.that, test.B.b_alias.that.self, test.B.self, test.B.that,
	test.B.that.self, that, that.self
--- */
//		XPECT linkedName at aa --> test.A.a
		feature b subsets aa;
		alias b_alias for b;
	}
}

````
