# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesInnerClassAndOuterClassWithAlias.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesInnerClassAndOuterClassWithAlias.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesInnerClassAndOuterClassWithAlias.kerml.xt
- source_bytes: 661
- source_sha256: `96b87941786f05041600388cb4496cd6ddf446bf0a68e258633a837d94856aca`
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
	alias A for A1;
	classifier A1{
		classifier A{
			//XPECT linkedName at A --> test.A1.A
			//* XPECT scope at A ---
			A.B.B, A1.A.B.B, B.B, test.A.A.B.B, test.A1.A.B.B,
		    A, A.B, A1, A1.A, A1.A.B, B, 
		    test.A, test.A.A, test.A.A.B, test.A1, test.A1.A, test.A1.A.B,
		--- */
			classifier B specializes A{}
		}
	}
}

````
