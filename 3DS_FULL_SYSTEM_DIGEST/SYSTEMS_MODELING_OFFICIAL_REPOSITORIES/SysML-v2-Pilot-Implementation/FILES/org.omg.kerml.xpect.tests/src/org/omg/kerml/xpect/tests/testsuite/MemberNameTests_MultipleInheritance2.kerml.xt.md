# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance2.kerml.xt
- source_bytes: 1257
- source_sha256: `787c8ddb2cfaf55b70a6160e213c5c1f0ad8960fa773cc07c4f981ad190f7252`
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
	classifier <'A_Id'> A{
		classifier <'a_Id'> a {}
	}
	classifier <'B_Id'> B specializes A{
		classifier <'b_Id'> b specializes a {}
	}
	classifier <'C_Id'> C specializes B{
		classifier <'c_Id'> c specializes a {}
	}
	//* XPECT scope at C::a ---
 		A, A_Id, A.a, A.a_Id, A_Id.a, A_Id.a_Id, B, B_Id, B.a, B.a_Id, B_Id.a, B_Id.a_Id, B.b, B.b_Id, B_Id.b, B_Id.b_Id, C,C_Id, C.a, C.a_Id, C_Id.a, C_Id.a_Id, C.b, C.b_Id, C_Id.b, C_Id.b_Id, C.c, C.c_Id, C_Id.c, C_Id.c_Id, D, D_Id,
 		test.A, test.A_Id, test.A.a, test.A.a_Id, test.A_Id.a, test.A_Id.a_Id, test.B, test.B_Id, test.B.a, test.B.a_Id, test.B_Id.a, test.B_Id.a_Id, test.B.b, test.B.b_Id, test.B_Id.b, test.B_Id.b_Id, test.C, test.C_Id, test.C.a, test.C.a_Id, test.C_Id.a, test.C_Id.a_Id, test.C.b, test.C.b_Id, test.C_Id.b, test.C_Id.b_Id, test.C.c, test.C.c_Id, test.C_Id.c, test.C_Id.c_Id, test.D, test.D_Id 
 	--- */
	classifier <'D_Id'> D specializes C::a{}
}

````
