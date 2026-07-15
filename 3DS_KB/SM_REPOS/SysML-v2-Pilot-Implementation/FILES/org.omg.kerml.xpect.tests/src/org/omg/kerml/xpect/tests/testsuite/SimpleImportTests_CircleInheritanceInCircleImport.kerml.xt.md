# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTests_CircleInheritanceInCircleImport.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTests_CircleInheritanceInCircleImport.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTests_CircleInheritanceInCircleImport.kerml.xt
- source_bytes: 888
- source_sha256: `27719bd6b03aa0ef042df23b4b08fde9dc6131d85ee9d9dff19a849d5e4e9846`
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

// XPECT noErrors ---> ""
package test{
	classifier A{
		public import test::B::*;
		//XPECT linkedName at b --> test.B.b
		//*XPECT scope at b ---
		   A.b, B.a, test.A.b, test.B.a,
 		   a, b,
 		   A, A.a, B, B.b, 
 		   test.A, test.A.a, test.B, test.B.b,
		   --- */
		classifier a specializes b{}
	}
	classifier B {
		public import test::A::*;
		//xpect throw an error for testing a
		//linkedName at a --> test.A.a
		//*scope at a ---
 		   a, b,
 		   A, A.a, B, B.b, 
 		   test.A, test.A.a, test.B, test.B.b,
		   --- */
		classifier b specializes a, Base::Anything{}
	}
}

````
