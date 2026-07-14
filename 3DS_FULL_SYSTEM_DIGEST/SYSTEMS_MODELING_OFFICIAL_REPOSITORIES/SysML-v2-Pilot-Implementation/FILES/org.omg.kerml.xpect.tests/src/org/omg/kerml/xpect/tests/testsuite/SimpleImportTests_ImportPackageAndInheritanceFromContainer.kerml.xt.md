# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTests_ImportPackageAndInheritanceFromContainer.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTests_ImportPackageAndInheritanceFromContainer.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportTests_ImportPackageAndInheritanceFromContainer.kerml.xt
- source_bytes: 689
- source_sha256: `e7b7e8efc55a62e2fee4b3dfb52381e03fcf3a4df4101233aa11ffb37b75b8b9`
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
	classifier A {
		public import test::*;
		//XPECT linkedName at A --> test.A
		//*XPECT scope at A ---
		   test.A.A, test.A.A.a, test.A.A.a.a,
		   a, a.A, a.A.a, a.a,
 		   A, A.a,  A.a.a, test.A, test.A.a, test.A.a.a, 
 		   test.A.a.A, test.A.a.A.a,
		   --- */
		classifier a specializes A;
	}
}

 //missing A.A, A.A.a, A.A.a.a
 //A.a.A, A.a.A.a

````
