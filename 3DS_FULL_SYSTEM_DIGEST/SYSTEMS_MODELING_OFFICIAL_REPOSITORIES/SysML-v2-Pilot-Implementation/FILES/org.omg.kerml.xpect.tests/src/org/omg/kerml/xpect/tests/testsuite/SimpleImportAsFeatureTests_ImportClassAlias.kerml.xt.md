# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportAsFeatureTests_ImportClassAlias.kerml.xt

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportAsFeatureTests_ImportClassAlias.kerml.xt`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.xpect.tests/src/org/omg/kerml/xpect/tests/testsuite/SimpleImportAsFeatureTests_ImportClassAlias.kerml.xt
- source_bytes: 889
- source_sha256: `22eb4babdd06e4f4f323f842ba34b45315733149f5ee95bf3f3f3fe76f501f68`
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
	alias aliass for OuterPackage::A;
	classifier C {
		//XPECT linkedName at aliass --> OuterPackage.A
		//* XPECT scope at aliass ---
		   C, C.c, C.c.a1, C.self, C.self.that, OuterPackage.A, OuterPackage.A.a1,
		   OuterPackage.B, OuterPackage.B.b, OuterPackage.B.b.a1, aliass, aliass.a1, c, c.a1, self,
		   self.that, test.C, test.C.c, test.C.c.a1, test.C.self, test.C.self.that, test.aliass,
		   test.aliass.a1
		--- */
		feature c: aliass;
	}
}

````
