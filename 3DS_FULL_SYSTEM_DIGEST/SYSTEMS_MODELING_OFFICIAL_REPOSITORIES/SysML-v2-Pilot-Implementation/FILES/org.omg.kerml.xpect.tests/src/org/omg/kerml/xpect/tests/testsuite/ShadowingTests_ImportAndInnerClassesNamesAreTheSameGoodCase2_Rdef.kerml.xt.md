# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase2_Rdef.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase2_Rdef.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_ImportAndInnerClassesNamesAreTheSameGoodCase2_Rdef.kerml.xt
- source_bytes: 2600
- source_sha256: `1e7009501e91ca63195d9d188071ff302ec63f56f0f413b6be3212967170870d`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyOuterPackage_Feature_Rdef.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyOuterPackage_Feature_Rdef.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors ---> ""
package test{
	public import OuterPackage::*;
	feature A{
		feature a2{}
	}
	//XPECT linkedName at A --> test.A
	//* XPECT scope at A ---
		A, A.a2, A.a2.self, A.a2.that, A.a2.that.self, A.self, A.that, A.that.self, B,
		B.b, B.b.self, B.b.that, B.b.that.self, B.self, B.that, B.that.self, OuterPackage.A,
		OuterPackage.A.a1, OuterPackage.A.a1.self, OuterPackage.A.a1.that, OuterPackage.A.a1.that.self,
		OuterPackage.A.self, OuterPackage.A.that, OuterPackage.A.that.self, OuterPackage.B,
		OuterPackage.B.b, OuterPackage.B.b.a1, OuterPackage.B.b.a1.self, OuterPackage.B.b.a1.that,
		OuterPackage.B.b.a1.that.self, OuterPackage.B.b.self, OuterPackage.B.b.that, OuterPackage.B.b.that.self,
		OuterPackage.B.self, OuterPackage.B.that, OuterPackage.B.that.self, test.A, test.A.a2,
		test.A.a2.self, test.A.a2.that, test.A.a2.that.self, test.A.self, test.A.that,
		test.A.that.self, test.B, test.B.b, test.B.b.self, test.B.b.that, test.B.b.that.self,
		test.B.self, test.B.that, test.B.that.self
	--- */
	feature B subsets A {
		//XPECT linkedName at a2 --> test.A.a2
		//* XPECT scope at a2 ---
        A, A.a2, A.a2.self, A.a2.that, A.a2.that.self, A.self, A.that, A.that.self, B,
        B.a2, B.a2.self, B.a2.that, B.a2.that.self, B.self, B.that, B.that.self,
        OuterPackage.A, OuterPackage.A.a1, OuterPackage.A.a1.self, OuterPackage.A.a1.that,
        OuterPackage.A.a1.that.self, OuterPackage.A.self, OuterPackage.A.that, OuterPackage.A.that.self,
        OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, OuterPackage.B.b.a1.self,
        OuterPackage.B.b.a1.that, OuterPackage.B.b.a1.that.self, OuterPackage.B.b.self, OuterPackage.B.b.that,
        OuterPackage.B.b.that.self, OuterPackage.B.self, OuterPackage.B.that, OuterPackage.B.that.self, a2,
        a2.self, a2.that, a2.that.self, self, test.A, test.A.a2, test.A.a2.self, test.A.a2.that,
        test.A.a2.that.self, test.A.self, test.A.that, test.A.that.self, test.B, test.B.a2, test.B.a2.self,
        test.B.a2.that, test.B.a2.that.self, test.B.self, test.B.that, test.B.that.self, that,
        that.self
		--- */
		feature b redefines a2 {}
	}
}

````
