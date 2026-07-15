# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance2x.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance2x.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance2x.kerml.xt
- source_bytes: 1675
- source_sha256: `f362015e2c627468e4b419cec5d15fd64fd0c54c179021cc86e35e96838baacd`
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

//this test is similar to MultipleInheritance2 but the order of classes defined are the different.
// XPECT noErrors --> ""
package test{
	
	//* XPECT scope at B ---
 		A, A.AA, B, B.AA, B.b,C, C.AA, C.b, C.c, D,	EE,  
 		test.A, test.A.AA, test.B, test.B.AA, test.B.b, test.C, test.C.AA, test.C.b,test.C.c, test.D, test.EE,
	--- */			
	classifier C specializes B{
		//* XPECT scope at AA ---
 		A, A.AA, AA, B, B.AA, B.b,C, C.AA, C.b, C.c, D, EE, b, c,  
 		test.A, test.A.AA, test.B, test.B.AA, test.B.b,	test.C, test.C.AA, test.C.b, test.C.c, test.D, test.EE,
	--- */
		classifier c specializes AA {}
	}
	//* XPECT scope at A ---
 		A, A.AA, B, B.AA, B.b, C, C.AA, C.b, C.c, D, EE, 
 		test.A, test.A.AA, test.B, test.B.AA, test.B.b, test.C, test.C.AA, test.C.b,test.C.c, test.D, test.EE,
	--- */
	classifier B specializes A{
		//* XPECT scope at AA ---
 		A, A.AA, AA, B, B.AA, B.b,C, C.AA, C.b, C.c, D, EE, b,   
 		test.A, test.A.AA, test.B, test.B.AA, test.B.b,	test.C, test.C.AA, test.C.b, test.C.c, test.D, test.EE,
	--- */
		classifier b specializes AA {}
	}
	
	classifier A{
		classifier AA {}
	}
	classifier EE{}
	//* XPECT scope at C::AA ---
 		A, A.AA, B, B.AA, B.b, C, C.AA, C.b, C.c, D, EE, 
 		test.A, test.A.AA, test.B, test.B.AA, test.B.b, test.C, test.C.AA, test.C.b,test.C.c, test.D, test.EE,
	--- */
	classifier D specializes C::AA{}
}

````
