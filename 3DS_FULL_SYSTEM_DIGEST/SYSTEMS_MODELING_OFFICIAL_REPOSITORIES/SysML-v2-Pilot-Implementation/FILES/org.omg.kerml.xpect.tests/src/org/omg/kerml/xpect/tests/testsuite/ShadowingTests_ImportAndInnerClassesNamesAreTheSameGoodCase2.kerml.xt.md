# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase2.kerml.xt
- source_bytes: 1072
- source_sha256: `b54b0e0ee7dd822f0cfb39086e1778feb78e33bcd5393b92a7e37de198bd490b`
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
	public import OuterPackage::*;
	classifier A{
		classifier a2{}
	}
	//XPECT linkedName at A --> test.A
	//* XPECT scope at A ---
		    A, A.a2, B, B.a2, B.b, 
		    test.A, test.A.a2, test.B, test.B.a2, test.B.b,
		    OuterPackage.A.a1, OuterPackage.B, OuterPackage.A, OuterPackage.B.b.a1,
		--- */
	classifier B specializes A {
		//XPECT linkedName at a2 --> test.A.a2
		//* XPECT scope at a2 ---
		    a2, b, 
		    A, A.a2, B, B.a2, B.b,
		    test.A, test.A.a2, test.B, test.B.a2, test.B.b, 
		    OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b.a1,
		--- */
		classifier b specializes a2 {}
	}
}

````
