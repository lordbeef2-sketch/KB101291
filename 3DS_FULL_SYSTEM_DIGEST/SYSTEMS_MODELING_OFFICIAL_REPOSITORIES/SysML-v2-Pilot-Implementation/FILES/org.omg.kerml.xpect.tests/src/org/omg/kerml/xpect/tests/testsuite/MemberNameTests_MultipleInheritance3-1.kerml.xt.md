# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance3-1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance3-1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance3-1.kerml.xt
- source_bytes: 1843
- source_sha256: `44bfc53527bbaac2980a606c849fa6176c370dd0a83efbfc3dfe12c13ae58c5d`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* This testcase is very similar to MultipleInheritance3, but change test.A.a to test.A.AA.
   This change enabled to add xpect linking test.
 */
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
	classifier A{
		classifier AA {
			classifier aa{}		
		}
	}
	classifier B specializes A{
		//XPECT linkedName at AA --> test.A.AA
		classifier b specializes AA {}
	}
	classifier C specializes B{
		//* XPECT scope at AA ---
 		A, A.AA, A.AA.aa, B, B.AA, B.AA.aa, B.b, B.b.aa, C, C.AA, C.AA.aa, C.b, C.b.aa, C.c2, C.c2.aa, C.c3, C.c3.aa, D, D.aa, D.d, 
 		AA, AA.aa, b, b.aa, c2, c2.aa, c3, c3.aa,
 		test.A, test.A.AA, test.A.AA.aa, test.B, test.B.AA, test.B.AA.aa, test.B.b, test.B.b.aa, test.C, test.C.AA, test.C.AA.aa,
		test.C.b, test.C.b.aa, test.C.c2, test.C.c2.aa,  test.C.c3, test.C.c3.aa, test.D, test.D.aa, test.D.d,
		--- */
		//XPECT linkedName at AA --> test.A.AA
		classifier c2 specializes AA {}
		//XPECT linkedName at b --> test.B.b
		//* XPECT scope at b ---
  		A, A.AA, A.AA.aa, B, B.AA, B.AA.aa, B.b, B.b.aa, C, C.AA, C.AA.aa, C.b, C.b.aa, C.c2, C.c2.aa, C.c3, C.c3.aa, D, D.aa, D.d, 
 		AA, AA.aa, b, b.aa, c2, c2.aa, c3, c3.aa,
 		test.A, test.A.AA, test.A.AA.aa, test.B, test.B.AA, test.B.AA.aa, test.B.b, test.B.b.aa, test.C, test.C.AA, test.C.AA.aa,
		test.C.b, test.C.b.aa, test.C.c2, test.C.c2.aa,  test.C.c3, test.C.c3.aa, test.D, test.D.aa, test.D.d,
		--- */
		classifier c3 specializes b {}
	}
	classifier D specializes C::AA{
		//XPECT linkedName at aa --> test.A.AA.aa
		classifier d specializes aa  {}
	}
}

````
