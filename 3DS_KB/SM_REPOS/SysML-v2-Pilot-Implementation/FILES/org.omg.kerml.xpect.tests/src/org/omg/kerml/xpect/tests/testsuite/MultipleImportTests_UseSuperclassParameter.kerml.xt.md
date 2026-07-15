# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImportTests_UseSuperclassParameter.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImportTests_UseSuperclassParameter.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImportTests_UseSuperclassParameter.kerml.xt
- source_bytes: 1048
- source_sha256: `0da1ed43792e1277962c2bee9547d53b02ecf2475a01b7ebfac836d67911c627`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/src/DependencyOuterPackage.kerml"}
		File {from ="/src/DependencyMultipleMembership.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/src/DependencyOuterPackage.kerml"}
				File {from ="/src/DependencyMultipleMembership.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors --> ""
package test{
	public import OuterPackage2::*;
	//XPECT linkedName at C::b --> OuterPackage.B.b
	//* XPECT scope at C::b ---
	   	   OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, 
	   	   OuterPackage2.B, OuterPackage2.B.b, OuterPackage2.B.b.a1, OuterPackage2.C, OuterPackage2.C.c, OuterPackage2.C.b.a1, OuterPackage2.C.b,
	   	   
	   	   B.b.a1, C.b.a1, try.a1,
	   	   test.B.b.a1, test.C.b.a1, test.try.a1,
		   B, B.b, C, C.b, C.c, try,
		   test.B, test.B.b, test.C, test.C.b, test.C.c, test.try, 
   	--- */
	feature try : C::b;
}

````
