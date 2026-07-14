# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesInnerClassAndOuterClass_Rdef.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesInnerClassAndOuterClass_Rdef.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesInnerClassAndOuterClass_Rdef.kerml.xt
- source_bytes: 813
- source_sha256: `df75ad98bf59d63d49c0a1d8d7b2164b2d49b07cd867b9b8fff5fe5d79b27c03`
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
	feature A{
		feature A {
			//XPECT linkedName at A --> test.A.A
			//* XPECT scope at A ---
			A, A.B, A.B.B, A.B.self, A.B.that, A.B.that.self, A.self, A.that, A.that.self,
			B, B.B, B.self, B.that, B.that.self, self, test.A, test.A.A, test.A.A.B,
			test.A.A.B.B, test.A.A.B.self, test.A.A.B.that, test.A.A.B.that.self, test.A.A.self,
			test.A.A.that, test.A.A.that.self, test.A.self, test.A.that, test.A.that.self, that,
			that.self
			--- */
			feature B : A;
		}
	}
}

````
