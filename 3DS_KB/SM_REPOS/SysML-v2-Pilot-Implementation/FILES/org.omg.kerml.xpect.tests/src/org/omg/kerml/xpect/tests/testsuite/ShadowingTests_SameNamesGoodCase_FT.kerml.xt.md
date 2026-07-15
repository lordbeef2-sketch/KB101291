# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesGoodCase_FT.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesGoodCase_FT.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/ShadowingTests_SameNamesGoodCase_FT.kerml.xt
- source_bytes: 2147
- source_sha256: `ff47b078ae8b6232f9d1dc4ca8f4f7a371a63f78ef64a80ffc0702bc95fe9efd`
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
		feature a1{}
	}
	//XPECT linkedName at A --> test.A
	//* XPECT scope at A ---
		A, A.a1, A.a1.self, A.a1.that, A.a1.that.self, A.self, A.that, A.that.self, B,
		B.A, B.A.a2, B.A.a2.self, B.A.a2.that, B.A.a2.that.self, B.A.self, B.A.that,
		B.A.that.self, B.a1, B.a1.self, B.a1.that, B.a1.that.self, B.b, B.b.self, B.b.that,
		B.b.that.self, B.self, B.that, B.that.self, test.A, test.A.a1, test.A.a1.self, test.A.a1.that,
		test.A.a1.that.self, test.A.self, test.A.that, test.A.that.self, test.B, test.B.A, test.B.A.a2,
		test.B.A.a2.self, test.B.A.a2.that, test.B.A.a2.that.self, test.B.A.self, test.B.A.that,
		test.B.A.that.self, test.B.a1, test.B.a1.self, test.B.a1.that, test.B.a1.that.self, test.B.b,
		test.B.b.self, test.B.b.that, test.B.b.that.self, test.B.self, test.B.that, test.B.that.self
	--- */
	feature B : A{
		feature A{
			feature a2{}
		}
		//XPECT linkedName at a1 --> test.A.a1
		//* XPECT scope at a1 ---
		A, A.a2, A.a2.self, A.a2.that, A.a2.that.self, A.self, A.that, A.that.self, B,
		B.A, B.A.a2, B.A.a2.self, B.A.a2.that, B.A.a2.that.self, B.A.self, B.A.that,
		B.A.that.self, B.a1, B.a1.self, B.a1.that, B.a1.that.self, B.b, B.b.self, B.b.that,
		B.b.that.self, B.self, B.that, B.that.self, a1, a1.self, a1.that, a1.that.self, b, b.self,
		b.that, b.that.self, self, test.A, test.A.a1, test.A.a1.self, test.A.a1.that,
		test.A.a1.that.self, test.A.self, test.A.that, test.A.that.self, test.B, test.B.A, test.B.A.a2,
		test.B.A.a2.self, test.B.A.a2.that, test.B.A.a2.that.self, test.B.A.self, test.B.A.that,
		test.B.A.that.self, test.B.a1, test.B.a1.self, test.B.a1.that, test.B.a1.that.self, test.B.b,
		test.B.b.self, test.B.b.that, test.B.b.that.self, test.B.self, test.B.that, test.B.that.self,
		that, that.self
		--- */
		feature b : a1{}
	}
}

````
