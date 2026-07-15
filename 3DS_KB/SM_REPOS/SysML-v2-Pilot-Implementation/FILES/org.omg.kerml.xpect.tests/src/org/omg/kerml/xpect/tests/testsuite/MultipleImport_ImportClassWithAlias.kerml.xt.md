# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImport_ImportClassWithAlias.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImport_ImportClassWithAlias.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/MultipleImport_ImportClassWithAlias.kerml.xt
- source_bytes: 888
- source_sha256: `25eceaa6d2e2d6ef61d25ba64dfc99be27904f2515db7e4adac5e1bba8f0d437`
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

// XPECT noErrors ---> ""
package test{
	alias aliass for OuterPackage::A;
	//XPECT linkedName at aliass --> OuterPackage.A
	classifier C {
		//* XPECT scope at aliass---
		   C, C.c, C.c.a1, C.self, C.self.that, OuterPackage.A, OuterPackage.A.a1,
		   OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, aliass, aliass.a1, c, c.a1, self,
		   self.that, test.C, test.C.c, test.C.c.a1, test.C.self, test.C.self.that, test.aliass,
		   test.aliass.a1
		--- */
		feature c: aliass;
	}
}

````
