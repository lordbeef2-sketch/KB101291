# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_CircleProblem2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_CircleProblem2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_CircleProblem2.kerml.xt
- source_bytes: 537
- source_sha256: `6af06436141f4b96b7792a4f1342eda6f801d72651fbfbaa85933a41dc26834d`
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
package Test1{
	classifier A {
		public import B::*;
		//XPECT linkedName at A --> Test1.A
		//* XPECT scope at A ---
   		A, A.B, A.B.B, B, B.B, Test1.A, Test1.A.B, Test1.A.B.B
 	--- */
		classifier B specializes A{}
	}
}

````
