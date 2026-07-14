# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTestsFromOtherFile_Import1.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTestsFromOtherFile_Import1.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTestsFromOtherFile_Import1.kerml.xt
- source_bytes: 1301
- source_sha256: `2632c82b030a93ee6457cad6f194969065404c4d0e63fe33165a6866119bc995`
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
	//XPECT linkedName at A --> OuterPackage.A
	//* XPECT scope at A ---
	       B.b.a1, test.B.b.a1, try.a1, test.try.a1,
		   Try, Try.a1, A, A.a1, B,
		   test.Try, test.Try.a1, test.A, test.A.a1, test.B, 
		   OuterPackage.A,OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b.a1,
	--- */
	classifier Try specializes A{}
	//XPECT linkedName at B::b --> OuterPackage.B.b
	//* XPECT scope at B::b ---
		A, A.a1, B, B.b, B.b.a1, OuterPackage.A, OuterPackage.A.a1, OuterPackage.B,
		OuterPackage.B.b, OuterPackage.B.b.a1, Try, Try.a1, Try.self, Try.self.that, test.A, test.A.a1,
		test.B, test.B.b, test.B.b.a1, test.Try, test.Try.a1, test.Try.self,
		test.Try.self.that, test.try, test.try.a1, test.try.self, test.try.that, test.try.that.self, try,
		try.a1, try.self, try.that, try.that.self
	--- */
	feature try : B::b;
}

````
