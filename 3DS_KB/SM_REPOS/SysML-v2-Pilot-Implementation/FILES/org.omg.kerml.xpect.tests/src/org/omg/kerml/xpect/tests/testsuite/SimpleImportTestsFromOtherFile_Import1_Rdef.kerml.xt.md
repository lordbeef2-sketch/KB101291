# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTestsFromOtherFile_Import1_Rdef.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTestsFromOtherFile_Import1_Rdef.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTestsFromOtherFile_Import1_Rdef.kerml.xt
- source_bytes: 3610
- source_sha256: `91a312f86b55bac823afafeb4d783b5d4ddfa773935c23e418e7a66609004b38`
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

// XPECT noErrors --> ""
package test {
	public import OuterPackage::*;
	//XPECT linkedName at A --> OuterPackage.A
	//* XPECT scope at A ---
	A, A.a1, A.a1.self, A.a1.that, A.a1.that.self, A.self, A.that, A.that.self, B,
	B.b, B.b.a1, B.b.a1.self, B.b.a1.that, B.b.a1.that.self, B.b.self, B.b.that,
	B.b.that.self, B.self, B.that, B.that.self, OuterPackage.A, OuterPackage.A.a1,
	OuterPackage.A.a1.self, OuterPackage.A.a1.that, OuterPackage.A.a1.that.self, OuterPackage.A.self,
	OuterPackage.A.that, OuterPackage.A.that.self, OuterPackage.B, OuterPackage.B.b,
	OuterPackage.B.b.a1, OuterPackage.B.b.a1.self, OuterPackage.B.b.a1.that,
	OuterPackage.B.b.a1.that.self, OuterPackage.B.b.self, OuterPackage.B.b.that, OuterPackage.B.b.that.self,
	OuterPackage.B.self, OuterPackage.B.that, OuterPackage.B.that.self, Try, Try.a1, Try.a1.self,
	Try.a1.that, Try.a1.that.self, Try.self, Try.that, Try.that.self, test.A, test.A.a1,
	test.A.a1.self, test.A.a1.that, test.A.a1.that.self, test.A.self, test.A.that,
	test.A.that.self, test.B, test.B.b, test.B.b.a1, test.B.b.a1.self, test.B.b.a1.that,
	test.B.b.a1.that.self, test.B.b.self, test.B.b.that, test.B.b.that.self, test.B.self, test.B.that,
	test.B.that.self, test.Try, test.Try.a1, test.Try.a1.self, test.Try.a1.that,
	test.Try.a1.that.self, test.Try.self, test.Try.that, test.Try.that.self, test.try, test.try.a1,
	test.try.a1.self, test.try.a1.that, test.try.a1.that.self, test.try.self, test.try.that,
	test.try.that.self, try, try.a1, try.a1.self, try.a1.that, try.a1.that.self, try.self, try.that,
	try.that.self
	--- */
	feature Try subsets A{}
	//XPECT linkedName at B::b --> OuterPackage.B.b
	//* XPECT scope at B::b ---
	A, A.a1, A.a1.self, A.a1.that, A.a1.that.self, A.self, A.that, A.that.self, B,
	B.b, B.b.a1, B.b.a1.self, B.b.a1.that, B.b.a1.that.self, B.b.self, B.b.that,
	B.b.that.self, B.self, B.that, B.that.self, OuterPackage, OuterPackage.A, OuterPackage.A.a1,
	OuterPackage.A.a1.self, OuterPackage.A.a1.that, OuterPackage.A.a1.that.self, OuterPackage.A.self,
	OuterPackage.A.that, OuterPackage.A.that.self, OuterPackage.B, OuterPackage.B.b,
	OuterPackage.B.b.a1, OuterPackage.B.b.a1.self, OuterPackage.B.b.a1.that,
	OuterPackage.B.b.a1.that.self, OuterPackage.B.b.self, OuterPackage.B.b.that, OuterPackage.B.b.that.self,
	OuterPackage.B.self, OuterPackage.B.that, OuterPackage.B.that.self, Try, Try.a1, Try.a1.self,
	Try.a1.that, Try.a1.that.self, Try.self, Try.that, Try.that.self, test, test.A, test.A.a1,
	test.A.a1.self, test.A.a1.that, test.A.a1.that.self, test.A.self, test.A.that,
	test.A.that.self, test.B, test.B.b, test.B.b.a1, test.B.b.a1.self, test.B.b.a1.that,
	test.B.b.a1.that.self, test.B.b.self, test.B.b.that, test.B.b.that.self, test.B.self, test.B.that,
	test.B.that.self, test.Try, test.Try.a1, test.Try.a1.self, test.Try.a1.that,
	test.Try.a1.that.self, test.Try.self, test.Try.that, test.Try.that.self, test.try, test.try.a1,
	test.try.a1.self, test.try.a1.that, test.try.a1.that.self, test.try.self, test.try.that,
	test.try.that.self, try, try.a1, try.a1.self, try.a1.that, try.a1.that.self, try.self, try.that,
	try.that.self
	--- */
	alias try for B::b;
}

````
