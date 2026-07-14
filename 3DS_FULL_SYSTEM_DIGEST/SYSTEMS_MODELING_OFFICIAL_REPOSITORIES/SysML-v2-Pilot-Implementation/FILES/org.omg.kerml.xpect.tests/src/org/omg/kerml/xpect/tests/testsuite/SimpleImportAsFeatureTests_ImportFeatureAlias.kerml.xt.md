# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportAsFeatureTests_ImportFeatureAlias.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportAsFeatureTests_ImportFeatureAlias.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportAsFeatureTests_ImportFeatureAlias.kerml.xt
- source_bytes: 1018
- source_sha256: `a8d8c2177c524fddcbd86d09d4ccb7cd92e70f767eecc9ac1e8b81e0be4eff83`
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
				File {from ="/src/DependencyOuterPackage.kerml"}
				File {from ="/library/Base.kerml"}
			}
		}
	}
END_SETUP 
*/

// XPECT noErrors --> ""
package test{
	alias aliass for OuterPackage::B::b;
	classifier C {
		//XPECT linkedName at aliass --> OuterPackage.B.b
		//* XPECT scope at aliass ---
		   C, C.c, C.c.a1, C.c.self, C.c.that, C.c.that.self, C.self, C.self.that,
		   OuterPackage.A, OuterPackage.A.a1, OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1,
		   aliass, aliass.a1, c, c.a1, c.self, c.that, c.that.self, self, self.that, test.C,
		   test.C.c, test.C.c.a1, test.C.c.self, test.C.c.that, test.C.c.that.self, test.C.self,
		   test.C.self.that, test.aliass, test.aliass.a1
		--- */
		
		feature c: aliass;
	}
}

````
