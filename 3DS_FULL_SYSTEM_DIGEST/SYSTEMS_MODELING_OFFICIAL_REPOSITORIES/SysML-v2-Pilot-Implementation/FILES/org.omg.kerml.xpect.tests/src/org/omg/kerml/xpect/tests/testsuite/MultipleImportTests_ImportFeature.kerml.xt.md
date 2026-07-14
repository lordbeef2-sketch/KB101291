# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImportTests_ImportFeature.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImportTests_ImportFeature.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImportTests_ImportFeature.kerml.xt
- source_bytes: 2182
- source_sha256: `9f6e07d0358158d85ee2ba66d3055ce62dac0fe876832cbee7931e7245c89294`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyOuterPackage.kerml"}
		File {from ="/src/DependencyMultipleMembership.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyOuterPackage.kerml"}
				File {from ="/src/DependencyMultipleMembership.kerml"}
			}
		}
	}
END_SETUP 
*/
// XPECT noErrors ---> ""
package test{
	//* XPECT scope at OuterPackage2::C::b ---
		D, D.self, D.self.that, D.try, D.try.a1, D.try.self, D.try.that,
		D.try.that.self, OuterPackage, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B,
		OuterPackage.B.b, OuterPackage.B.b.a1, OuterPackage2, OuterPackage2.B, OuterPackage2.B.b,
		OuterPackage2.B.b.a1, OuterPackage2.C, OuterPackage2.C.b, OuterPackage2.C.b.a1, OuterPackage2.C.c,
		OuterPackage2.C.c.self, OuterPackage2.C.c.that, OuterPackage2.C.c.that.self, b, b.a1, test, test.D,
		test.D.self, test.D.self.that, test.D.try, test.D.try.a1, test.D.try.self, test.D.try.that,
		test.D.try.that.self, test.b, test.b.a1
	--- */
	public import OuterPackage2::C::b;
	classifier D{
		//XPECT linkedName at b --> OuterPackage.B.b
		//* XPECT scope at b ---
		D, D.self, D.self.that, D.try, D.try.a1, D.try.self, D.try.that,
		D.try.that.self, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b,
		OuterPackage.B.b.a1, OuterPackage2.B, OuterPackage2.B.b, OuterPackage2.B.b.a1, OuterPackage2.C,
		OuterPackage2.C.b, OuterPackage2.C.b.a1, OuterPackage2.C.c, OuterPackage2.C.c.self,
		OuterPackage2.C.c.that, OuterPackage2.C.c.that.self, b, b.a1, self, self.that, test.D, test.D.self,
		test.D.self.that, test.D.try, test.D.try.a1, test.D.try.self, test.D.try.that,
		test.D.try.that.self, test.b, test.b.a1, try, try.a1, try.self, try.that, try.that.self
		--- */
		feature try : b;
	}
}
//* Note: difference between two scopes are
   OuterPackage, OuterPackage2, test, Base --------------- scope at OuterPacakge2::C::b
   try, try.a1 --------------------------------------------scope at b
 */

````
