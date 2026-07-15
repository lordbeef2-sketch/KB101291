# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTests_ImportPackageAndInheritanceFromContainer_Rdef.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTests_ImportPackageAndInheritanceFromContainer_Rdef.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTests_ImportPackageAndInheritanceFromContainer_Rdef.kerml.xt
- source_bytes: 1022
- source_sha256: `f8b55b1102df07007dc6226d92e1f8165bfc8384ffe916d1b5c2fbd73bbe0f45`
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

// XPECT noErrors ---> ""
package test{
	feature A {
		public import test::*;
		//XPECT linkedName at A --> test.A
		//*XPECT scope at A ---
		A, A.a, A.a.a, A.a.self, A.a.that, A.a.that.self, A.self, A.that, A.that.self,
		a, a.A, a.A.a, a.A.self, a.A.that, a.A.that.self, a.a, a.self, a.that,
		a.that.self, self, test.A, test.A.A, test.A.A.a, test.A.A.a.a, test.A.A.a.self,
		test.A.A.a.that, test.A.A.a.that.self, test.A.A.self, test.A.A.that, test.A.A.that.self,
		test.A.a, test.A.a.A, test.A.a.A.a, test.A.a.A.self, test.A.a.A.that,
		test.A.a.A.that.self, test.A.a.a, test.A.a.self, test.A.a.that, test.A.a.that.self, test.A.self,
		test.A.that, test.A.that.self, that, that.self
		--- */
		feature a subsets A;
	}
}

````
