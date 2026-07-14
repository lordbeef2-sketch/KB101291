# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesGoodCaseWithAlias.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesGoodCaseWithAlias.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesGoodCaseWithAlias.kerml.xt
- source_bytes: 999
- source_sha256: `08241bbd9d05edfa1a77cf60a2efc388a16ecc2ef423b8ad4ad776b9745c3214`
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
	alias A1 for A;
	classifier A{
		classifier a1{}
	}
	//A.a2, B.a2 should not be included.
	//XPECT linkedName at A --> test.A
	//* XPECT scope at A ---
		    A, A.a1, A1, A1.a1, B, B.a1, B.A, B.A.a2, B.b, 
		    test.A, test.A.a1, test.A1, test.A1.a1, test.B, test.B.a1, test.B.A, test.B.A.a2, test.B.b,
		--- */
	classifier B specializes A{
		classifier A{
			classifier a2{}
		}
		//XPECT linkedName at a1 --> test.A.a1
		//* XPECT scope at a1 ---
		    A, A.a2, A1, A1.a1, B, B.a1, B.A, B.A.a2, B.b, 
		    a1, b, test.A, test.A.a1, test.A1, test.A1.a1, test.B, test.B.a1, test.B.A, test.B.A.a2, test.B.b,
		--- */
		classifier b specializes a1{}
	}
}

````
