# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase1.kerml.xt
- source_bytes: 758
- source_sha256: `a6035c204ee3500a1b505c29ac1d8eb2a8001468118966ba7aff5f9c6bc161f9`
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
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyOuterPackage.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors ---> ""
package test{
	public import OuterPackage::*;
	classifier A{
		classifier a2{}
	}
	//XPECT linkedName at A::a2 --> test.A.a2
	//* XPECT scope at A::a2 ---
		    A, A.a2, B, 
		    test.A, test.A.a2, test.B, 
		    OuterPackage.A.a1, OuterPackage.B, OuterPackage.A, OuterPackage.B.b.a1,
		--- */
	classifier B specializes A::a2 {}
}

````
