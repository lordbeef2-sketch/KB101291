# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImport_ImportClassWithAlias_FT.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImport_ImportClassWithAlias_FT.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImport_ImportClassWithAlias_FT.kerml.xt
- source_bytes: 1838
- source_sha256: `b91c11b97b976a3a1f237721ac6477f511ac7bda488820dabc0e2288529fff43`
- decoded_as: `utf-8`


## EXACT SOURCE

````xtext
//* 
XPECT_SETUP org.omg.kerml.xpect.tests.parsing.KerMLParsingTest
	ResourceSet {
		ThisFile {}
		File {from ="/library/Base.kerml"}
		File {from ="/src/DependencyOuterPackage_Feature_FT.kerml"}
	}
	Workspace {
		JavaProject {
			SrcFolder {
				ThisFile {}
				File {from ="/library/Base.kerml"}
				File {from ="/src/DependencyOuterPackage_Feature_FT.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors ---> ""
package test{
	alias aliass for OuterPackage::A;
	//XPECT linkedName at aliass --> OuterPackage.A
	feature C {
		//* XPECT scope at aliass---
		   C, C.c, C.c.a1, C.c.a1.self, C.c.a1.that, C.c.a1.that.self, C.c.self, C.c.that,
		   C.c.that.self, C.self, C.that, C.that.self, OuterPackage.A, OuterPackage.A.a1,
		   OuterPackage.A.a1.self, OuterPackage.A.a1.that, OuterPackage.A.a1.that.self, OuterPackage.A.self,
		   OuterPackage.A.that, OuterPackage.A.that.self, OuterPackage.B, OuterPackage.B.b,
		   OuterPackage.B.b.a1, OuterPackage.B.b.a1.self, OuterPackage.B.b.a1.that,
		   OuterPackage.B.b.a1.that.self, OuterPackage.B.b.self, OuterPackage.B.b.that, OuterPackage.B.b.that.self,
		   OuterPackage.B.self, OuterPackage.B.that, OuterPackage.B.that.self, aliass, aliass.a1,
		   aliass.a1.self, aliass.a1.that, aliass.a1.that.self, aliass.self, aliass.that,
		   aliass.that.self, c, c.a1, c.a1.self, c.a1.that, c.a1.that.self, c.self, c.that, c.that.self,
		   self, test.C, test.C.c, test.C.c.a1, test.C.c.a1.self, test.C.c.a1.that,
		   test.C.c.a1.that.self, test.C.c.self, test.C.c.that, test.C.c.that.self, test.C.self, test.C.that,
		   test.C.that.self, test.aliass, test.aliass.a1, test.aliass.a1.self, test.aliass.a1.that,
		   test.aliass.a1.that.self, test.aliass.self, test.aliass.that, test.aliass.that.self, that, that.self
		--- */
		feature c : aliass;
	}
}

````
