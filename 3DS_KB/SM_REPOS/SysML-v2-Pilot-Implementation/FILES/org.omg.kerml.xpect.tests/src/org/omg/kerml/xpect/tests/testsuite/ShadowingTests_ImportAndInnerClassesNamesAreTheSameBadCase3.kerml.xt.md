# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase3.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase3.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameBadCase3.kerml.xt
- source_bytes: 998
- source_sha256: `c9a02493d6aae07438b9b7cb22437bb8a1f8f3b3a7b3ba74545a11dd5900b598`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyOuterPackage.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/src/DependencyOuterPackage.kerml"}
				File {from ="/library/Base.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors ---> ""
package test{				
	classifier A{
		classifier a2{}
	}
	classifier inner{
		public import OuterPackage::*;
		classifier B specializes A {
			//XPECT linkedName at a1 --> OuterPackage.A.a1
			//* XPECT scope at a1 ---
			inner.A, inner.A.a1, test.inner.A, test.inner.A.a1,
		    b, a1, 
		    A, A.a1, B, B.a1, B.b, inner, inner.B, inner.B.a1, inner.B.b,
		    test.A, test.A.a2, test.inner, test.inner.B, test.inner.B.a1, test.inner.B.b,
		    OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b.a1,
		--- */
			classifier b specializes a1{}
		}
	}
}

````
