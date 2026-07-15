# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTestsFromOtherFile_Import2.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTestsFromOtherFile_Import2.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTestsFromOtherFile_Import2.kerml.xt
- source_bytes: 1468
- source_sha256: `f7f668e8abad2d6324ddf2af173bab09b93dc5d2bf57ad950fa9eab8fa7ff741`
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

// XPECT noErrors --> ""
package test {
	public import OuterPackage::*;
	//XPECT linkedName at B --> OuterPackage.B
	//* XPECT scope at B ---
	       B.b.a1, test.B.b.a1, Try.try.a1, test.Try.try.a1, Try.b.a1, test.Try.b.a1,
		   Try, A, A.a1, B,
		   test.Try, test.A, test.A.a1, test.B, 
		   OuterPackage.A,OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b.a1,
	--- */
	classifier Try specializes B{
		//XPECT linkedName at b --> OuterPackage.B.b
		//* XPECT scope at b ---
		   A, A.a1, B, B.b, B.b.a1, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B,
		   OuterPackage.B.b, OuterPackage.B.b.a1, Try, Try.b, Try.b.a1, Try.self, Try.self.that, Try.try,
		   Try.try.a1, Try.try.self, Try.try.that, Try.try.that.self, b, b.a1, self, self.that,
		   test.A, test.A.a1, test.B, test.B.b, test.B.b.a1, test.Try, test.Try.b, test.Try.b.a1,
		   test.Try.self, test.Try.self.that, test.Try.try, test.Try.try.a1, test.Try.try.self,
		   test.Try.try.that, test.Try.try.that.self, try, try.a1, try.self, try.that, try.that.self
	--- */
		feature try : b;
	}
}

````
