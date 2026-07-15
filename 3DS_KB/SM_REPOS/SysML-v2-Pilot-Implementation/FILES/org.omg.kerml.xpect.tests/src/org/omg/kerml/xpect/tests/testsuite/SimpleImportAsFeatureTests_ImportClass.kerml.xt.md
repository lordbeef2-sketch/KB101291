# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportAsFeatureTests_ImportClass.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportAsFeatureTests_ImportClass.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportAsFeatureTests_ImportClass.kerml.xt
- source_bytes: 849
- source_sha256: `28222471dc8bdcf40d3572d5afc4553ae5a774126ea4513003e00bdea33d1c93`
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
package test{
	public import OuterPackage::A;
	classifier C {
		//XPECT linkedName at A --> OuterPackage.A
		//* XPECT scope at A ---
		   A, A.a1, C, C.c, C.c.a1, C.self, C.self.that, OuterPackage.A,
		   OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, c, c.a1, self,
		   self.that, test.A, test.A.a1, test.C, test.C.c, test.C.c.a1, test.C.self,
		   test.C.self.that
		--- */
		feature c: A;
	}
}

````
