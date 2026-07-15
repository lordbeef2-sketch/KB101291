# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_CircleProblem5.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_CircleProblem5.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_CircleProblem5.kerml.xt
- source_bytes: 1422
- source_sha256: `4dc4b4de1a63ab55391ffe5e93c2de6fd37d1048b222e1bf6adec095f9f08dd3`
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


//
//package Test1{
//	classifier A specializes D{
//		classifier B specializes C{}
//	}
//	classifier C specializes A{}
//	classifier D specializes A.B{}
//}


// XPECT noErrors --> ""
package Test1{
		//XPECT linkedName at D --> Test1.D
		//* XPECT scope at D ---
   		A, A.B, A.B.B, C, C.B, D, D.B,
		Test1.A, Test1.A.B, Test1.A.B.B, Test1.C, Test1.C.B, Test1.D, Test1.D.B
 	--- */
	classifier A specializes D, Base::Anything{
		//XPECT linkedName at C --> Test1.C
		//* XPECT scope at C ---
		   B, B.B,
   		A, A.B, A.B.B, C, C.B, D, D.B,
		Test1.A, Test1.A.B, Test1.A.B.B, Test1.C, Test1.C.B, Test1.D, Test1.D.B
 	--- */
		classifier B specializes C{}
	}
	//XPECT linkedName at A --> Test1.A
	//* XPECT scope at A ---
   		A, A.B, A.B.B, C, C.B, D, D.B,
		Test1.A, Test1.A.B, Test1.A.B.B, Test1.C, Test1.C.B, Test1.D, Test1.D.B
 	--- */
	classifier C specializes A{}
	
	//XPECT linkedName at A::B --> Test1.A.B
	//* XPECT scope at A::B ---
   		A, A.B, A.B.B, C, C.B, D, D.B,
		Test1.A, Test1.A.B, Test1.A.B.B, Test1.C, Test1.C.B, Test1.D, Test1.D.B
 	--- */
	classifier D specializes A::B{}
}

````
