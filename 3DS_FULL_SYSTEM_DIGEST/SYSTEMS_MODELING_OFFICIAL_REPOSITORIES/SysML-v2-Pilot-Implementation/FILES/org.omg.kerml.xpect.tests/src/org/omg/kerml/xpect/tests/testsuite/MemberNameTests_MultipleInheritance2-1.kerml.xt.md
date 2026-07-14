# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance2-1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance2-1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MemberNameTests_MultipleInheritance2-1.kerml.xt
- source_bytes: 1137
- source_sha256: `50e6e16aac1b3b45e4fea1afba9d17e9039cee8025ffdc399ad4a0e861c8907e`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//*
   This testcase is very similar to MultipleInheritance2.  But change test.A.a to test.A.AA.
   xpect throws RuntimeException error when test.A.a but not test.A.AA
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
//RuntimeExcpetion happend for adding linking test to A.a so
//copied from MultipleInheritance2, rename a to AA then possible to perform linking test
//XPECT noErrors ---> ""
package test{
	classifier A{
		classifier AA {}
	}
	classifier B specializes A{
		//XPECT linkedName at AA --> test.A.AA  
		classifier b specializes AA {}
	}
	classifier C specializes B{
		//XPECT linkedName at AA --> test.A.AA
		classifier c specializes AA {}
	}
	//* XPECT scope at C::AA ---
 		A, A.AA, B, B.AA, B.b, C, C.AA, C.b, C.c, D,
 		test.A, test.A.AA, test.B, test.B.AA, test.B.b, test.C, test.C.AA, test.C.b, test.C.c, test.D, 
 	--- */
	classifier D specializes C::AA{}
}

````
